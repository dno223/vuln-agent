"""
Email Alert Agent - Sends daily vulnerability intelligence reports via Gmail SMTP.

Reads config from .env:
  EMAIL_SENDER     — Gmail address used as sender
  EMAIL_PASSWORD   — Gmail App Password (not your account password)
  EMAIL_RECIPIENTS — Comma-separated list of recipient addresses

Provides:
  send_alert(report_data, html_report_path) — send the daily report email
  main()                                    — standalone test with synthetic data
"""

import logging
import os
import smtplib
from datetime import datetime, timedelta, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from typing import Union

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


# ---------------------------------------------------------------------------
# Internal helpers (mirrors report_builder to avoid circular imports)
# ---------------------------------------------------------------------------

def _compute_risk_level(results: dict) -> str:
    cves = results.get("high_severity_cves", [])
    kev_hits = results.get("monitored_hits", [])
    kev_entries = results.get("new_kev_entries", [])
    max_cvss = max((c.get("cvss_score", 0) for c in cves), default=0)
    if max_cvss >= 9.0 or len(kev_hits) > 0:
        return "Critical"
    if max_cvss >= 7.0 or len(kev_entries) > 0:
        return "High"
    return "Medium"


def _compute_avg_cvss(cves: list) -> float:
    scores = [c.get("cvss_score", 0) for c in cves if c.get("cvss_score")]
    return round(sum(scores) / len(scores), 1) if scores else 0.0


def _kev_due_this_week(kev_entries: list, run_date: str) -> int:
    try:
        base = datetime.strptime(run_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError:
        base = datetime.now(timezone.utc)
    cutoff = base + timedelta(days=7)
    count = 0
    for entry in kev_entries:
        due = entry.get("dueDate", "")
        try:
            due_dt = datetime.strptime(due, "%Y-%m-%d").replace(tzinfo=timezone.utc)
            if base <= due_dt <= cutoff:
                count += 1
        except ValueError:
            pass
    return count


def _build_subject(results: dict) -> str:
    """Compose the email subject line from pipeline results."""
    run_date = results.get("run_date", datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    risk_level = _compute_risk_level(results)
    cve_count = len(results.get("high_severity_cves", []))
    kev_count = len(results.get("new_kev_entries", []))
    return (
        f"\U0001f534 Vuln Intel Report - {run_date} - {risk_level} Risk "
        f"({cve_count} CVEs, {kev_count} KEV hits)"
    )


# ---------------------------------------------------------------------------
# HTML email builder
# ---------------------------------------------------------------------------

def build_email_html(results: dict) -> str:
    """
    Build a fully inline-CSS HTML email from pipeline results.

    The email is designed to render correctly in Gmail, Outlook, and Apple Mail
    using table-based layout with no external dependencies.

    Args:
        results: Pipeline results dict from orchestrator.run_pipeline()

    Returns:
        Complete HTML string ready to send as email body.
    """
    run_date = results.get("run_date", "")
    run_ts = results.get("run_timestamp", "")
    cves = results.get("high_severity_cves", [])
    kev_entries = results.get("new_kev_entries", [])
    executive_summary = results.get("executive_summary") or "No summary available."
    risk_narrative = results.get("risk_narrative") or "No risk narrative available."
    action_items = results.get("action_items") or []

    risk_level = _compute_risk_level(results)
    avg_cvss = _compute_avg_cvss(cves)
    kev_due_week = _kev_due_this_week(kev_entries, run_date)
    cve_count = len(cves)
    kev_count = len(kev_entries)

    risk_fg = {"Critical": "#dc2626", "High": "#ea580c", "Medium": "#b45309"}.get(risk_level, "#6b7280")
    risk_bg = {"Critical": "#fef2f2", "High": "#fff7ed", "Medium": "#fefce8"}.get(risk_level, "#f9fafb")

    def score_style(score: float) -> tuple[str, str]:
        if score >= 9.0:
            return "#fef2f2", "#dc2626"
        if score >= 7.0:
            return "#fff7ed", "#ea580c"
        return "#fefce8", "#b45309"

    def kpi_color(val: float, warn: float, danger: float) -> str:
        if val >= danger:
            return "#dc2626"
        if val >= warn:
            return "#ea580c"
        return "#111827"

    # ---------- Top 10 CVEs by CVSS ----------
    top_cves = sorted(cves, key=lambda c: c.get("cvss_score", 0), reverse=True)[:10]
    cve_rows = []
    for cve in top_cves:
        score = cve.get("cvss_score", 0)
        s_bg, s_fg = score_style(score)
        raw_desc = cve.get("description", "")
        desc = raw_desc[:160] + ("…" if len(raw_desc) > 160 else "")
        pub = str(cve.get("published_date", ""))[:10]
        cve_id = cve.get("cve_id", "")
        cve_rows.append(
            f'<tr>'
            f'<td style="padding:10px 14px;border-bottom:1px solid #e5e7eb;'
            f'font-family:monospace;font-size:13px;color:#4f46e5;white-space:nowrap;">{cve_id}</td>'
            f'<td style="padding:10px 14px;border-bottom:1px solid #e5e7eb;text-align:center;white-space:nowrap;">'
            f'<span style="display:inline-block;padding:2px 8px;border-radius:4px;font-weight:700;'
            f'font-size:12px;background:{s_bg};color:{s_fg};">{score}</span></td>'
            f'<td style="padding:10px 14px;border-bottom:1px solid #e5e7eb;'
            f'font-size:13px;color:#6b7280;white-space:nowrap;">{pub}</td>'
            f'<td style="padding:10px 14px;border-bottom:1px solid #e5e7eb;'
            f'font-size:13px;color:#374151;">{desc}</td>'
            f'</tr>'
        )
    cve_rows_html = "\n".join(cve_rows) if cve_rows else (
        '<tr><td colspan="4" style="padding:20px;text-align:center;'
        'color:#9ca3af;font-style:italic;">No high-severity CVEs found.</td></tr>'
    )

    # ---------- CISA KEV table ----------
    kev_rows = []
    for entry in kev_entries:
        ransomware = entry.get("knownRansomwareCampaignUse", "Unknown")
        if ransomware == "Known":
            row_bg = "#fef2f2"
            b_bg, b_fg = "#fee2e2", "#dc2626"
        else:
            row_bg = "#ffffff"
            b_bg, b_fg = "#f3f4f6", "#6b7280"
        vendor_product = f"{entry.get('vendorProject', '')} / {entry.get('product', '')}"
        kev_rows.append(
            f'<tr style="background:{row_bg};">'
            f'<td style="padding:10px 14px;border-bottom:1px solid #e5e7eb;'
            f'font-family:monospace;font-size:13px;color:#4f46e5;white-space:nowrap;">'
            f'{entry.get("cveID", "")}</td>'
            f'<td style="padding:10px 14px;border-bottom:1px solid #e5e7eb;'
            f'font-size:13px;color:#374151;">{vendor_product}</td>'
            f'<td style="padding:10px 14px;border-bottom:1px solid #e5e7eb;'
            f'font-size:13px;color:#6b7280;white-space:nowrap;">{entry.get("dateAdded", "")}</td>'
            f'<td style="padding:10px 14px;border-bottom:1px solid #e5e7eb;'
            f'font-size:13px;color:#6b7280;white-space:nowrap;">{entry.get("dueDate", "")}</td>'
            f'<td style="padding:10px 14px;border-bottom:1px solid #e5e7eb;text-align:center;">'
            f'<span style="display:inline-block;padding:2px 10px;border-radius:9999px;'
            f'font-size:12px;font-weight:600;background:{b_bg};color:{b_fg};">{ransomware}</span>'
            f'</td></tr>'
        )
    kev_rows_html = "\n".join(kev_rows) if kev_rows else (
        '<tr><td colspan="5" style="padding:20px;text-align:center;'
        'color:#9ca3af;font-style:italic;">No new KEV entries found.</td></tr>'
    )

    # ---------- Action items ----------
    action_rows = []
    for i, item in enumerate(action_items[:5], 1):
        action_rows.append(
            f'<tr>'
            f'<td style="padding:8px 14px;vertical-align:top;font-weight:700;'
            f'color:#4f46e5;font-size:16px;white-space:nowrap;">{i}.</td>'
            f'<td style="padding:8px 14px;font-size:14px;color:#374151;line-height:1.6;">{item}</td>'
            f'</tr>'
        )
    action_rows_html = "\n".join(action_rows) if action_rows else (
        '<tr><td colspan="2" style="padding:20px;color:#9ca3af;'
        'font-style:italic;">No action items available.</td></tr>'
    )

    # ---------- KPI colors ----------
    cve_color = kpi_color(cve_count, 5, 20)
    cvss_color = kpi_color(avg_cvss, 7.0, 9.0)
    kev_color = kpi_color(kev_count, 1, 3)
    due_color = kpi_color(kev_due_week, 1, 2)

    # ---------- Table header style shorthand ----------
    th = (
        'style="padding:10px 14px;text-align:left;font-size:11px;font-weight:600;'
        'text-transform:uppercase;letter-spacing:0.06em;color:#6b7280;'
        'border-bottom:1px solid #e5e7eb;white-space:nowrap;background:#f9fafb;"'
    )
    th_wrap = (
        'style="padding:10px 14px;text-align:left;font-size:11px;font-weight:600;'
        'text-transform:uppercase;letter-spacing:0.06em;color:#6b7280;'
        'border-bottom:1px solid #e5e7eb;background:#f9fafb;"'
    )

    section_header = (
        'style="background:#f5f3ff;padding:12px 18px;border-bottom:1px solid #e5e7eb;"'
    )
    section_title = (
        'style="font-size:12px;font-weight:700;text-transform:uppercase;'
        'letter-spacing:0.08em;color:#4f46e5;"'
    )
    section_wrap = 'style="border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;"'
    kpi_wrap = (
        'style="background:#f9fafb;border:1px solid #e5e7eb;border-radius:10px;padding:16px 18px;"'
    )
    kpi_label = (
        'style="font-size:11px;font-weight:600;text-transform:uppercase;'
        'letter-spacing:0.08em;color:#6b7280;margin-bottom:6px;"'
    )
    kpi_sub = 'style="font-size:11px;color:#9ca3af;margin-top:4px;"'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Vuln Intel Report — {run_date}</title>
</head>
<body style="margin:0;padding:0;background:#f3f4f6;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#f3f4f6;">
<tr><td align="center" style="padding:24px 16px;">

  <table width="700" cellpadding="0" cellspacing="0" border="0"
         style="max-width:700px;width:100%;background:#ffffff;border-radius:12px;
                overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.10);">

    <!-- ===== HEADER ===== -->
    <tr>
      <td style="background:linear-gradient(135deg,#1e1b4b 0%,#312e81 100%);padding:28px 32px;">
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              <div style="font-size:20px;font-weight:800;color:#ffffff;letter-spacing:0.01em;">
                Vulnerability Intelligence Report
              </div>
              <div style="font-size:12px;color:#a5b4fc;margin-top:4px;">
                Date: {run_date} &nbsp;|&nbsp; Generated: {run_ts}
              </div>
            </td>
            <td align="right" style="white-space:nowrap;">
              <span style="display:inline-block;padding:8px 18px;border-radius:9999px;
                           font-weight:700;font-size:13px;letter-spacing:0.05em;
                           text-transform:uppercase;background:{risk_bg};
                           color:{risk_fg};border:2px solid {risk_fg};">
                &#9679; {risk_level} Risk
              </span>
            </td>
          </tr>
        </table>
      </td>
    </tr>

    <!-- ===== KPI ROW ===== -->
    <tr>
      <td style="padding:24px 24px 8px 24px;">
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td width="25%" style="padding-right:8px;">
              <div {kpi_wrap}>
                <div {kpi_label}>Total CVEs</div>
                <div style="font-size:36px;font-weight:700;color:{cve_color};line-height:1;">{cve_count}</div>
                <div {kpi_sub}>CVSS &ge; 7.0 &middot; last 24h</div>
              </div>
            </td>
            <td width="25%" style="padding:0 8px;">
              <div {kpi_wrap}>
                <div {kpi_label}>Avg CVSS</div>
                <div style="font-size:36px;font-weight:700;color:{cvss_color};line-height:1;">{avg_cvss}</div>
                <div {kpi_sub}>across all CVEs found</div>
              </div>
            </td>
            <td width="25%" style="padding:0 8px;">
              <div {kpi_wrap}>
                <div {kpi_label}>New KEV Entries</div>
                <div style="font-size:36px;font-weight:700;color:{kev_color};line-height:1;">{kev_count}</div>
                <div {kpi_sub}>added in last 7 days</div>
              </div>
            </td>
            <td width="25%" style="padding-left:8px;">
              <div {kpi_wrap}>
                <div {kpi_label}>KEV Due This Week</div>
                <div style="font-size:36px;font-weight:700;color:{due_color};line-height:1;">{kev_due_week}</div>
                <div {kpi_sub}>remediation deadlines</div>
              </div>
            </td>
          </tr>
        </table>
      </td>
    </tr>

    <!-- ===== EXECUTIVE SUMMARY ===== -->
    <tr>
      <td style="padding:20px 32px 0 32px;">
        <div {section_wrap}>
          <div {section_header}><span {section_title}>Executive Summary</span></div>
          <div style="padding:16px 18px;font-size:14px;color:#374151;line-height:1.8;">
            {executive_summary}
          </div>
        </div>
      </td>
    </tr>

    <!-- ===== RISK NARRATIVE ===== -->
    <tr>
      <td style="padding:16px 32px 0 32px;">
        <div {section_wrap}>
          <div {section_header}><span {section_title}>Risk Narrative</span></div>
          <div style="padding:16px 18px;font-size:14px;color:#374151;line-height:1.8;">
            {risk_narrative}
          </div>
        </div>
      </td>
    </tr>

    <!-- ===== ACTION ITEMS ===== -->
    <tr>
      <td style="padding:16px 32px 0 32px;">
        <div {section_wrap}>
          <div {section_header}><span {section_title}>Prioritized Action Items</span></div>
          <div style="padding:12px 18px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0">
              {action_rows_html}
            </table>
          </div>
        </div>
      </td>
    </tr>

    <!-- ===== CISA KEV TABLE ===== -->
    <tr>
      <td style="padding:16px 32px 0 32px;">
        <div {section_wrap}>
          <div {section_header}><span {section_title}>CISA KEV &mdash; {kev_count} New Entries (last 7 days)</span></div>
          <div style="overflow-x:auto;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0">
              <thead>
                <tr>
                  <th {th}>CVE ID</th>
                  <th {th_wrap}>Vendor / Product</th>
                  <th {th}>Date Added</th>
                  <th {th}>Due Date</th>
                  <th {th}>Ransomware</th>
                </tr>
              </thead>
              <tbody>{kev_rows_html}</tbody>
            </table>
          </div>
        </div>
      </td>
    </tr>

    <!-- ===== TOP 10 CVEs TABLE ===== -->
    <tr>
      <td style="padding:16px 32px 0 32px;">
        <div {section_wrap}>
          <div {section_header}><span {section_title}>Top 10 CVEs by CVSS Score</span></div>
          <div style="overflow-x:auto;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0">
              <thead>
                <tr>
                  <th {th}>CVE ID</th>
                  <th {th}>CVSS</th>
                  <th {th}>Published</th>
                  <th {th_wrap}>Description</th>
                </tr>
              </thead>
              <tbody>{cve_rows_html}</tbody>
            </table>
          </div>
        </div>
      </td>
    </tr>

    <!-- ===== FOOTER ===== -->
    <tr>
      <td style="padding:28px 32px 32px 32px;">
        <div style="border-top:1px solid #e5e7eb;padding-top:20px;text-align:center;
                    font-size:12px;color:#9ca3af;">
          Generated by <strong style="color:#6b7280;">Vuln Intelligence Agent</strong>
          &bull; {run_ts}<br>
          Data sources: NVD (National Vulnerability Database)
          &bull; CISA Known Exploited Vulnerabilities Catalog
        </div>
      </td>
    </tr>

  </table>
</td></tr>
</table>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def send_alert(
    report_data: dict,
    html_report_path: Union[str, Path, None] = None,
) -> bool:
    """
    Send the daily vulnerability intelligence report via Gmail SMTP.

    Reads EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECIPIENTS from environment.
    Returns immediately with a warning log if any required var is missing.

    Args:
        report_data: Pipeline results dict from orchestrator.run_pipeline()
        html_report_path: Reserved for future attachment support; currently unused.

    Returns:
        True if the email was sent successfully, False otherwise.
    """
    sender = os.getenv("EMAIL_SENDER", "").strip()
    password = os.getenv("EMAIL_PASSWORD", "").strip()
    recipients_raw = os.getenv("EMAIL_RECIPIENTS", "").strip()

    if not sender:
        logger.warning("EMAIL_SENDER not configured — skipping email alert")
        return False
    if not password:
        logger.warning("EMAIL_PASSWORD not configured — skipping email alert")
        return False
    if not recipients_raw:
        logger.warning("EMAIL_RECIPIENTS not configured — skipping email alert")
        return False

    recipients = [r.strip() for r in recipients_raw.split(",") if r.strip()]
    if not recipients:
        logger.warning("EMAIL_RECIPIENTS is empty after parsing — skipping email alert")
        return False

    subject = _build_subject(report_data)
    html_body = build_email_html(report_data)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(sender, password)
            smtp.sendmail(sender, recipients, msg.as_string())
        logger.info(
            "Email alert sent to %d recipient(s): %s",
            len(recipients),
            ", ".join(recipients),
        )
        return True
    except smtplib.SMTPAuthenticationError as e:
        logger.error("SMTP authentication failed — check EMAIL_PASSWORD: %s", e)
        return False
    except smtplib.SMTPException as e:
        logger.error("SMTP error sending email alert: %s", e)
        return False
    except OSError as e:
        logger.error("Network error sending email alert: %s", e)
        return False


def main() -> None:
    """Entry point — builds and sends a test email using synthetic data."""
    sample_data = {
        "run_date": "2026-05-30",
        "run_timestamp": "2026-05-30T08:00:00Z",
        "high_severity_cves": [
            {
                "cve_id": "CVE-2021-44228",
                "description": (
                    "Apache Log4j2 remote code execution vulnerability via JNDI lookup "
                    "in log messages. Affects Log4j2 versions 2.0-beta9 through 2.14.1."
                ),
                "cvss_score": 10.0,
                "published_date": "2021-12-10T00:00:00.000",
            },
            {
                "cve_id": "CVE-2021-26855",
                "description": (
                    "Microsoft Exchange Server server-side request forgery vulnerability "
                    "allowing unauthenticated remote code execution."
                ),
                "cvss_score": 9.8,
                "published_date": "2021-03-02T00:00:00.000",
            },
            {
                "cve_id": "CVE-2023-44487",
                "description": (
                    "HTTP/2 Rapid Reset attack enabling denial-of-service against web servers."
                ),
                "cvss_score": 7.5,
                "published_date": "2023-10-10T00:00:00.000",
            },
        ],
        "new_kev_entries": [
            {
                "cveID": "CVE-2024-21762",
                "vendorProject": "Fortinet",
                "product": "FortiOS",
                "vulnerabilityName": "Fortinet FortiOS Out-of-Bound Write Vulnerability",
                "dateAdded": "2024-02-09",
                "dueDate": "2024-02-16",
                "knownRansomwareCampaignUse": "Known",
            },
            {
                "cveID": "CVE-2024-1709",
                "vendorProject": "ConnectWise",
                "product": "ScreenConnect",
                "vulnerabilityName": "ConnectWise ScreenConnect Authentication Bypass",
                "dateAdded": "2024-02-22",
                "dueDate": "2024-02-29",
                "knownRansomwareCampaignUse": "Known",
            },
        ],
        "monitored_hits": [],
        "executive_summary": (
            "Three critical vulnerabilities were identified in the last 24 hours, "
            "including two with CVSS scores above 9.0. Two new CISA KEV entries "
            "linked to ransomware campaigns require immediate attention. Patch "
            "windows are closing — remediation should begin within 24 hours."
        ),
        "action_items": [
            "Patch Apache Log4j2 (CVE-2021-44228, CVSS 10.0) on all affected systems immediately.",
            "Apply Microsoft Exchange cumulative update for CVE-2021-26855 by end of day.",
            "Review FortiOS and ScreenConnect deployments for the two new CISA KEV entries.",
            "Run authenticated vulnerability scans across internet-facing infrastructure.",
            "Brief incident response team on ransomware-linked KEV entries and escalation path.",
        ],
        "risk_narrative": (
            "The current threat landscape reflects a high volume of critical remote code "
            "execution vulnerabilities being actively weaponised. Ransomware operators are "
            "leveraging the newly added CISA KEV entries within hours of disclosure, "
            "compressing the effective patch window to under 48 hours for high-priority assets."
        ),
        "pipeline_errors": [],
        "total_kev_count": 1200,
    }

    sent = send_alert(sample_data)
    if sent:
        print("Test email sent successfully.")
    else:
        print("Email not sent — check EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECIPIENTS in .env")
        subject = _build_subject(sample_data)
        print(f"\nWould-be subject: {subject}")
        html = build_email_html(sample_data)
        preview_path = Path("outputs/reports/email_preview.html")
        preview_path.parent.mkdir(parents=True, exist_ok=True)
        preview_path.write_text(html, encoding="utf-8")
        print(f"HTML preview saved to: {preview_path}")


if __name__ == "__main__":
    main()
