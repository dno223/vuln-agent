"""
SeptZen Site Dependency Vulnerability Watcher
=============================================
Reads DEPENDENCIES.md from the septzen-site repo, extracts all external
packages and CDN dependencies, cross-references against NVD CVE database
and CISA KEV catalog, and sends email alerts for any hits.

Usage:
    python site_watcher.py                    # Run once
    python site_watcher.py --dry-run          # Check without sending email
    python site_watcher.py --output report.json  # Save JSON report
"""

import argparse
import json
import logging
import os
import re
import smtplib
import sys
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# ── Configuration ─────────────────────────────────────────────────────────────

NVD_API_KEY     = os.getenv('NVD_API_KEY', '')
SMTP_HOST       = os.getenv('SMTP_HOST', 'smtp.gmail.com')
SMTP_PORT       = int(os.getenv('SMTP_PORT', 587))
SMTP_USER       = os.getenv('SMTP_USER', '')
SMTP_PASSWORD   = os.getenv('SMTP_PASSWORD', '')
ALERT_TO_EMAIL  = os.getenv('ALERT_TO_EMAIL', '')
ALERT_FROM_NAME = os.getenv('ALERT_FROM_NAME', 'SeptZen Vuln Watcher')
DAYS_BACK       = int(os.getenv('VULN_DAYS_BACK', 7))
MIN_CVSS_SCORE  = float(os.getenv('MIN_CVSS_SCORE', 5.0))

NVD_BASE_URL    = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
KEV_URL         = 'https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json'

# ── Dependency definitions ─────────────────────────────────────────────────────
# Each entry maps to NVD CPE keywords and search terms.
# Extend this list as new packages are added to DEPENDENCIES.md

SITE_DEPENDENCIES = [
    {
        'name': 'EmailJS Browser SDK',
        'version': '4.x',
        'type': 'npm',
        'package': '@emailjs/browser',
        'nvd_keywords': ['emailjs'],
        'cpe_keywords': ['emailjs'],
        'risk_context': 'Used in contact form and compliance checker lead gate — XSS or data exfil risk',
    },
    {
        'name': 'Cloudflare Pages',
        'version': 'managed',
        'type': 'hosting',
        'package': 'cloudflare-pages',
        'nvd_keywords': ['cloudflare pages', 'cloudflare workers'],
        'cpe_keywords': ['cloudflare'],
        'risk_context': 'Hosting platform — supply chain or infrastructure compromise risk',
    },
    {
        'name': 'Cloudflare DNS over HTTPS API',
        'version': 'public',
        'type': 'api',
        'package': 'cloudflare-doh',
        'nvd_keywords': ['cloudflare dns', 'dns over https'],
        'cpe_keywords': ['cloudflare'],
        'risk_context': 'Used in DMARC checker for live DNS lookups',
    },
    {
        'name': 'Bunny Fonts CDN',
        'version': 'latest',
        'type': 'cdn',
        'package': 'bunny-fonts',
        'nvd_keywords': ['bunny fonts', 'fonts.bunny.net'],
        'cpe_keywords': ['bunny fonts'],
        'risk_context': 'CDN font delivery via fonts.bunny.net — GDPR-compliant Google Fonts mirror',
    },
    {
        'name': 'Syne Font',
        'version': 'latest',
        'type': 'font',
        'package': 'syne',
        'nvd_keywords': ['syne font'],
        'cpe_keywords': ['syne'],
        'risk_context': 'Font asset via Bunny Fonts CDN',
    },
    {
        'name': 'JetBrains Mono Font',
        'version': 'latest',
        'type': 'font',
        'package': 'jetbrains-mono',
        'nvd_keywords': ['jetbrains mono', 'jetbrains font'],
        'cpe_keywords': ['jetbrains'],
        'risk_context': 'Font asset via Bunny Fonts CDN',
    },
]

# ── NVD Client ────────────────────────────────────────────────────────────────

def query_nvd(keyword: str, days_back: int = DAYS_BACK) -> list:
    """Query NVD CVE API for a keyword within the last N days."""
    headers = {'apiKey': NVD_API_KEY} if NVD_API_KEY else {}
    pub_start = (datetime.utcnow() - timedelta(days=days_back)).strftime('%Y-%m-%dT00:00:00.000')
    pub_end   = datetime.utcnow().strftime('%Y-%m-%dT23:59:59.999')

    params = {
        'keywordSearch': keyword,
        'pubStartDate':  pub_start,
        'pubEndDate':    pub_end,
        'resultsPerPage': 20,
    }

    try:
        resp = requests.get(NVD_BASE_URL, params=params, headers=headers, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        return data.get('vulnerabilities', [])
    except requests.RequestException as e:
        logger.warning(f'NVD query failed for "{keyword}": {e}')
        return []


def parse_cvss(vuln_item: dict) -> tuple[Optional[float], str]:
    """Extract CVSS score and severity from NVD vulnerability item."""
    try:
        metrics = vuln_item['cve'].get('metrics', {})
        # Try CVSS v3.1 first, then v3.0, then v2
        for version in ['cvssMetricV31', 'cvssMetricV30', 'cvssMetricV2']:
            if version in metrics and metrics[version]:
                data = metrics[version][0]['cvssData']
                score    = data.get('baseScore', 0.0)
                severity = data.get('baseSeverity', 'UNKNOWN')
                return score, severity
    except (KeyError, IndexError):
        pass
    return None, 'UNKNOWN'


# ── KEV Client ────────────────────────────────────────────────────────────────

def fetch_kev_catalog() -> dict:
    """Fetch CISA Known Exploited Vulnerabilities catalog."""
    try:
        resp = requests.get(KEV_URL, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        # Return as dict keyed by CVE ID for fast lookup
        return {v['cveID']: v for v in data.get('vulnerabilities', [])}
    except requests.RequestException as e:
        logger.warning(f'KEV fetch failed: {e}')
        return {}


# ── Scanner ───────────────────────────────────────────────────────────────────

def scan_dependencies(deps: list, days_back: int = DAYS_BACK) -> dict:
    """Scan all dependencies against NVD and KEV. Returns structured report."""
    logger.info(f'Fetching CISA KEV catalog...')
    kev_catalog = fetch_kev_catalog()
    logger.info(f'KEV catalog loaded: {len(kev_catalog)} entries')

    report = {
        'generated_at': datetime.utcnow().isoformat(),
        'scan_window_days': days_back,
        'total_deps': len(deps),
        'findings': [],
        'summary': {
            'critical': 0,
            'high':     0,
            'medium':   0,
            'low':      0,
            'kev_hits': 0,
            'clean':    0,
        }
    }

    for dep in deps:
        logger.info(f'Scanning: {dep["name"]}')
        dep_findings = []

        for keyword in dep['nvd_keywords']:
            vulns = query_nvd(keyword, days_back)
            for v in vulns:
                cve_id      = v['cve']['id']
                description = v['cve'].get('descriptions', [{}])[0].get('value', 'No description')
                score, severity = parse_cvss(v)
                is_kev      = cve_id in kev_catalog
                published   = v['cve'].get('published', '')[:10]

                if score is None or score < MIN_CVSS_SCORE:
                    continue

                finding = {
                    'cve_id':      cve_id,
                    'description': description[:300],
                    'score':       score,
                    'severity':    severity,
                    'published':   published,
                    'is_kev':      is_kev,
                    'kev_detail':  kev_catalog.get(cve_id, {}),
                    'dep_name':    dep['name'],
                    'dep_context': dep['risk_context'],
                    'keyword':     keyword,
                }
                dep_findings.append(finding)

                # Update summary counts
                sev = severity.upper()
                if sev == 'CRITICAL':   report['summary']['critical'] += 1
                elif sev == 'HIGH':     report['summary']['high']     += 1
                elif sev == 'MEDIUM':   report['summary']['medium']   += 1
                else:                   report['summary']['low']      += 1
                if is_kev:              report['summary']['kev_hits'] += 1

        if not dep_findings:
            report['summary']['clean'] += 1

        report['findings'].extend(dep_findings)

    # Sort: KEV first, then by CVSS score descending
    report['findings'].sort(key=lambda x: (not x['is_kev'], -(x['score'] or 0)))

    logger.info(
        f"Scan complete — {len(report['findings'])} findings | "
        f"Critical: {report['summary']['critical']} | "
        f"High: {report['summary']['high']} | "
        f"KEV: {report['summary']['kev_hits']}"
    )
    return report


# ── Email Alert ───────────────────────────────────────────────────────────────

def build_email_html(report: dict) -> str:
    """Build HTML email body for vulnerability report."""
    findings  = report['findings']
    summary   = report['summary']
    scan_date = report['generated_at'][:10]
    total     = len(findings)

    if total == 0:
        status_color = '#10b981'
        status_text  = 'ALL CLEAR'
        status_desc  = 'No vulnerabilities found in your site dependencies this week.'
    elif summary['critical'] > 0 or summary['kev_hits'] > 0:
        status_color = '#ef4444'
        status_text  = 'ACTION REQUIRED'
        status_desc  = f'{total} vulnerabilit{"y" if total == 1 else "ies"} found — including critical or actively exploited issues.'
    else:
        status_color = '#f59e0b'
        status_text  = 'REVIEW RECOMMENDED'
        status_desc  = f'{total} vulnerabilit{"y" if total == 1 else "ies"} found — no critical issues, but review advised.'

    rows = ''
    for f in findings[:20]:  # Cap at 20 in email
        kev_badge = '<span style="background:#ef4444;color:#fff;padding:2px 8px;border-radius:20px;font-size:11px;font-weight:700;">KEV</span> ' if f['is_kev'] else ''
        sev_color = {
            'CRITICAL': '#ef4444',
            'HIGH':     '#f97316',
            'MEDIUM':   '#f59e0b',
            'LOW':      '#10b981',
        }.get(f['severity'].upper(), '#94a3b8')

        rows += f"""
        <tr style="border-bottom:1px solid #1e3a5f;">
          <td style="padding:12px 8px;">
            {kev_badge}<a href="https://nvd.nist.gov/vuln/detail/{f['cve_id']}"
               style="color:#00d4c8;text-decoration:none;font-family:monospace;">{f['cve_id']}</a>
          </td>
          <td style="padding:12px 8px;color:#94a3b8;font-size:13px;">{f['dep_name']}</td>
          <td style="padding:12px 8px;">
            <span style="color:{sev_color};font-weight:700;">{f['severity']}</span>
            <span style="color:#94a3b8;font-size:12px;"> ({f['score']})</span>
          </td>
          <td style="padding:12px 8px;color:#cbd5e1;font-size:13px;">{f['description'][:120]}...</td>
          <td style="padding:12px 8px;color:#64748b;font-size:12px;font-family:monospace;">{f['published']}</td>
        </tr>"""

    return f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"/></head>
<body style="margin:0;padding:0;background:#020b18;font-family:'Segoe UI',sans-serif;">
  <div style="max-width:800px;margin:0 auto;padding:40px 20px;">

    <!-- Header -->
    <div style="margin-bottom:32px;">
      <div style="font-size:22px;font-weight:800;color:#f0f4f8;letter-spacing:-0.02em;">
        Sept<span style="color:#00d4c8;">Zen</span>
        <span style="font-size:14px;font-weight:400;color:#7a96b0;margin-left:12px;">Site Vulnerability Report</span>
      </div>
      <div style="font-family:monospace;font-size:12px;color:#7a96b0;margin-top:4px;">
        Scan date: {scan_date} · Window: last {report['scan_window_days']} days · septzen.com dependencies
      </div>
    </div>

    <!-- Status Banner -->
    <div style="background:{status_color}18;border:1px solid {status_color}44;border-radius:8px;padding:20px;margin-bottom:32px;">
      <div style="font-size:13px;font-family:monospace;font-weight:700;color:{status_color};letter-spacing:0.15em;margin-bottom:6px;">
        // {status_text}
      </div>
      <div style="color:#f0f4f8;font-size:15px;">{status_desc}</div>
    </div>

    <!-- Summary -->
    <div style="display:flex;gap:16px;margin-bottom:32px;flex-wrap:wrap;">
      <div style="flex:1;min-width:100px;background:#071628;border:1px solid #0e2845;border-radius:8px;padding:16px;text-align:center;">
        <div style="font-size:28px;font-weight:800;color:#ef4444;font-family:monospace;">{summary['critical']}</div>
        <div style="font-size:11px;color:#7a96b0;text-transform:uppercase;letter-spacing:0.1em;">Critical</div>
      </div>
      <div style="flex:1;min-width:100px;background:#071628;border:1px solid #0e2845;border-radius:8px;padding:16px;text-align:center;">
        <div style="font-size:28px;font-weight:800;color:#f97316;font-family:monospace;">{summary['high']}</div>
        <div style="font-size:11px;color:#7a96b0;text-transform:uppercase;letter-spacing:0.1em;">High</div>
      </div>
      <div style="flex:1;min-width:100px;background:#071628;border:1px solid #0e2845;border-radius:8px;padding:16px;text-align:center;">
        <div style="font-size:28px;font-weight:800;color:#f59e0b;font-family:monospace;">{summary['medium']}</div>
        <div style="font-size:11px;color:#7a96b0;text-transform:uppercase;letter-spacing:0.1em;">Medium</div>
      </div>
      <div style="flex:1;min-width:100px;background:#071628;border:1px solid #0e2845;border-radius:8px;padding:16px;text-align:center;">
        <div style="font-size:28px;font-weight:800;color:#ef4444;font-family:monospace;">{summary['kev_hits']}</div>
        <div style="font-size:11px;color:#7a96b0;text-transform:uppercase;letter-spacing:0.1em;">KEV Hits</div>
      </div>
      <div style="flex:1;min-width:100px;background:#071628;border:1px solid #0e2845;border-radius:8px;padding:16px;text-align:center;">
        <div style="font-size:28px;font-weight:800;color:#10b981;font-family:monospace;">{summary['clean']}</div>
        <div style="font-size:11px;color:#7a96b0;text-transform:uppercase;letter-spacing:0.1em;">Clean Deps</div>
      </div>
    </div>

    <!-- Findings Table -->
    {"<p style='color:#10b981;font-family:monospace;font-size:14px;'>✓ No vulnerabilities found in the scan window. All dependencies appear clean.</p>" if total == 0 else f'''
    <table style="width:100%;border-collapse:collapse;background:#071628;border:1px solid #0e2845;border-radius:8px;overflow:hidden;">
      <thead>
        <tr style="background:#0a1e35;">
          <th style="padding:12px 8px;text-align:left;font-family:monospace;font-size:11px;color:#00d4c8;letter-spacing:0.1em;text-transform:uppercase;">CVE ID</th>
          <th style="padding:12px 8px;text-align:left;font-family:monospace;font-size:11px;color:#00d4c8;letter-spacing:0.1em;text-transform:uppercase;">Dependency</th>
          <th style="padding:12px 8px;text-align:left;font-family:monospace;font-size:11px;color:#00d4c8;letter-spacing:0.1em;text-transform:uppercase;">Severity</th>
          <th style="padding:12px 8px;text-align:left;font-family:monospace;font-size:11px;color:#00d4c8;letter-spacing:0.1em;text-transform:uppercase;">Description</th>
          <th style="padding:12px 8px;text-align:left;font-family:monospace;font-size:11px;color:#00d4c8;letter-spacing:0.1em;text-transform:uppercase;">Published</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
    {"<p style='color:#7a96b0;font-size:12px;font-family:monospace;margin-top:8px;'>Showing top 20 of " + str(total) + " findings. Run locally for full report.</p>" if total > 20 else ""}
    '''}

    <!-- Footer -->
    <div style="margin-top:40px;padding-top:20px;border-top:1px solid #0e2845;font-family:monospace;font-size:11px;color:#7a96b0;">
      <div>SeptZen Automated Vulnerability Watcher · septzen.com</div>
      <div style="margin-top:4px;">Sources: NVD API (NIST) · CISA KEV Catalog · Min CVSS: {MIN_CVSS_SCORE}</div>
      <div style="margin-top:4px;">To adjust scan settings, edit VULN_DAYS_BACK and MIN_CVSS_SCORE in your .env</div>
    </div>

  </div>
</body>
</html>"""


def send_alert_email(report: dict, dry_run: bool = False) -> bool:
    """Send vulnerability report email."""
    findings = report['findings']
    summary  = report['summary']
    total    = len(findings)

    subject_prefix = '🔴' if (summary['critical'] > 0 or summary['kev_hits'] > 0) else '🟡' if total > 0 else '🟢'
    subject = f"{subject_prefix} SeptZen Site Vuln Report — {total} finding{'s' if total != 1 else ''} ({report['generated_at'][:10]})"

    html_body = build_email_html(report)

    if dry_run:
        logger.info(f'[DRY RUN] Would send email: "{subject}" to {ALERT_TO_EMAIL}')
        logger.info(f'[DRY RUN] Findings: {total} | Critical: {summary["critical"]} | KEV: {summary["kev_hits"]}')
        return True

    if not all([SMTP_USER, SMTP_PASSWORD, ALERT_TO_EMAIL]):
        logger.error('Email not configured. Set SMTP_USER, SMTP_PASSWORD, ALERT_TO_EMAIL in .env')
        return False

    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From']    = f'{ALERT_FROM_NAME} <{SMTP_USER}>'
        msg['To']      = ALERT_TO_EMAIL
        msg.attach(MIMEText(html_body, 'html'))

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, ALERT_TO_EMAIL, msg.as_string())

        logger.info(f'Email sent to {ALERT_TO_EMAIL}: {subject}')
        return True

    except Exception as e:
        logger.error(f'Email send failed: {e}')
        return False


# ── Report output for dashboard ───────────────────────────────────────────────

def save_report(report: dict, path: str):
    """Save JSON report for dashboard consumption."""
    with open(path, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    logger.info(f'Report saved to {path}')


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='SeptZen site dependency vulnerability watcher')
    parser.add_argument('--dry-run',  action='store_true', help='Check without sending email')
    parser.add_argument('--output',   type=str, default='vuln-report.json', help='JSON report output path')
    parser.add_argument('--days',     type=int, default=DAYS_BACK, help=f'Days back to scan (default: {DAYS_BACK})')
    parser.add_argument('--min-cvss', type=float, default=MIN_CVSS_SCORE, help=f'Minimum CVSS score (default: {MIN_CVSS_SCORE})')
    parser.add_argument('--no-email', action='store_true', help='Skip email, just generate report')
    args = parser.parse_args()

    logger.info('=' * 60)
    logger.info('SeptZen Site Dependency Vulnerability Watcher')
    logger.info(f'Scanning {len(SITE_DEPENDENCIES)} dependencies | Last {args.days} days | Min CVSS {args.min_cvss}')
    logger.info('=' * 60)

    report = scan_dependencies(SITE_DEPENDENCIES, days_back=args.days)
    save_report(report, args.output)

    if not args.no_email:
        send_alert_email(report, dry_run=args.dry_run)

    # Exit code 1 if critical or KEV findings — useful for CI/CD gating
    if report['summary']['critical'] > 0 or report['summary']['kev_hits'] > 0:
        logger.warning('Critical or KEV vulnerabilities found — exit code 1')
        sys.exit(1)

    logger.info('Scan complete.')
    sys.exit(0)


if __name__ == '__main__':
    main()
