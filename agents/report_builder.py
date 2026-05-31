"""
Report Builder - Converts JSON pipeline output into a styled HTML report.

Produces a fully self-contained (inline CSS/JS) HTML file saved to
outputs/reports/daily_report_YYYY-MM-DD.html
"""

import json
import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

REPORTS_DIR = Path(__file__).parent.parent / "outputs" / "reports"
DOCS_DIR = Path(__file__).parent.parent / "docs"


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


def _cvss_class(score: float) -> str:
    if score >= 9.0:
        return "critical"
    if score >= 7.0:
        return "high"
    return "medium"


def _risk_badge_style(level: str) -> str:
    colors = {"Critical": "#dc2626", "High": "#ea580c", "Medium": "#ca8a04"}
    return colors.get(level, "#6b7280")


def build_html_report(results: dict) -> str:
    run_date = results.get("run_date", "")
    run_ts = results.get("run_timestamp", "")
    cves = results.get("high_severity_cves", [])
    kev_entries = results.get("new_kev_entries", [])
    kev_hits = results.get("monitored_hits", [])
    executive_summary = results.get("executive_summary", "") or "No summary available."
    risk_narrative = results.get("risk_narrative", "") or "No risk narrative available."
    action_items = results.get("action_items", []) or []
    pipeline_errors = results.get("pipeline_errors", [])

    risk_level = _compute_risk_level(results)
    avg_cvss = _compute_avg_cvss(cves)
    kev_due_week = _kev_due_this_week(kev_entries, run_date)
    badge_color = _risk_badge_style(risk_level)

    # Build CVE table rows
    cve_rows = []
    for cve in cves:
        score = cve.get("cvss_score", 0)
        cls = _cvss_class(score)
        desc = cve.get("description", "")
        pub = str(cve.get("published_date", ""))[:10]
        cve_rows.append(
            f'<tr>'
            f'<td><a class="cve-link" href="https://nvd.nist.gov/vuln/detail/{cve.get("cve_id","")}" '
            f'target="_blank" rel="noopener noreferrer">{cve.get("cve_id","")}</a></td>'
            f'<td><span class="score-badge {cls}">{score}</span></td>'
            f'<td>{pub}</td>'
            f'<td class="desc-cell">{desc[:200]}{"…" if len(desc) > 200 else ""}</td>'
            f'</tr>'
        )
    cve_rows_html = "\n".join(cve_rows) if cve_rows else '<tr><td colspan="4" class="empty-row">No high-severity CVEs found.</td></tr>'

    # Build KEV table rows
    kev_rows = []
    for entry in kev_entries:
        ransomware = entry.get("knownRansomwareCampaignUse", "Unknown")
        r_class = "ransomware-known" if ransomware == "Known" else "ransomware-unknown"
        vendor_product = f"{entry.get('vendorProject', '')} / {entry.get('product', '')}"
        kev_rows.append(
            f'<tr>'
            f'<td><a class="cve-link" href="https://nvd.nist.gov/vuln/detail/{entry.get("cveID","")}" '
            f'target="_blank" rel="noopener noreferrer">{entry.get("cveID","")}</a></td>'
            f'<td>{vendor_product}</td>'
            f'<td>{entry.get("dateAdded","")}</td>'
            f'<td>{entry.get("dueDate","")}</td>'
            f'<td><span class="badge {r_class}">{ransomware}</span></td>'
            f'</tr>'
        )
    kev_rows_html = "\n".join(kev_rows) if kev_rows else '<tr><td colspan="5" class="empty-row">No new KEV entries found.</td></tr>'

    # Action items
    action_html = ""
    if action_items:
        items_html = "\n".join(f"<li>{item}</li>" for item in action_items)
        action_html = f"<ol class='action-list'>{items_html}</ol>"
    else:
        action_html = "<p class='empty-msg'>No action items available.</p>"

    # Pipeline warnings
    warnings_html = ""
    if pipeline_errors:
        errs = "\n".join(f"<li>{e}</li>" for e in pipeline_errors)
        warnings_html = f"""
        <div class="warning-box">
            <strong>Pipeline Warnings:</strong>
            <ul>{errs}</ul>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vulnerability Intelligence Report — {run_date}</title>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  :root {{
    --bg: #0f1117;
    --surface: #1a1d27;
    --surface2: #22263a;
    --border: #2d3148;
    --text: #e2e8f0;
    --text-muted: #94a3b8;
    --accent: #6366f1;
    --critical: #dc2626;
    --high: #ea580c;
    --medium: #ca8a04;
    --success: #16a34a;
  }}
  body {{ background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, monospace; line-height: 1.6; }}
  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}

  /* Header */
  .header {{ background: linear-gradient(135deg, #1a1d27 0%, #0f1117 100%); border-bottom: 1px solid var(--border); padding: 24px 32px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; }}
  .header-left h1 {{ font-size: 1.5rem; font-weight: 700; letter-spacing: 0.01em; color: #f1f5f9; }}
  .header-left h1 span {{ color: var(--accent); }}
  .header-meta {{ font-size: 0.8rem; color: var(--text-muted); margin-top: 4px; }}
  .risk-badge {{ display: inline-flex; align-items: center; gap: 6px; padding: 8px 20px; border-radius: 9999px; font-weight: 700; font-size: 0.95rem; letter-spacing: 0.05em; text-transform: uppercase; background: {badge_color}22; color: {badge_color}; border: 2px solid {badge_color}; }}
  .risk-dot {{ width: 8px; height: 8px; border-radius: 50%; background: {badge_color}; animation: pulse 2s infinite; }}
  @keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.4; }} }}

  /* Layout */
  .container {{ max-width: 1400px; margin: 0 auto; padding: 32px; }}

  /* KPI cards */
  .kpi-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 32px; }}
  .kpi-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 20px 24px; }}
  .kpi-label {{ font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 8px; }}
  .kpi-value {{ font-size: 2.5rem; font-weight: 700; line-height: 1; color: #f1f5f9; }}
  .kpi-value.danger {{ color: var(--critical); }}
  .kpi-value.warn {{ color: var(--high); }}
  .kpi-sub {{ font-size: 0.75rem; color: var(--text-muted); margin-top: 4px; }}

  /* Sections */
  .section {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 24px; }}
  .section-title {{ font-size: 1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--accent); margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid var(--border); }}
  .section p {{ color: var(--text-muted); line-height: 1.8; }}

  /* Action list */
  .action-list {{ padding-left: 20px; }}
  .action-list li {{ color: var(--text-muted); margin-bottom: 10px; padding-left: 4px; line-height: 1.7; }}
  .action-list li::marker {{ color: var(--accent); font-weight: 700; }}
  .empty-msg {{ color: var(--text-muted); font-style: italic; }}

  /* Tables */
  .table-wrapper {{ overflow-x: auto; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 0.875rem; }}
  th {{ background: var(--surface2); padding: 10px 14px; text-align: left; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-muted); border-bottom: 1px solid var(--border); cursor: pointer; user-select: none; white-space: nowrap; }}
  th:hover {{ color: var(--text); }}
  th .sort-icon {{ margin-left: 4px; opacity: 0.4; }}
  th.sorted .sort-icon {{ opacity: 1; color: var(--accent); }}
  td {{ padding: 10px 14px; border-bottom: 1px solid var(--border); vertical-align: top; }}
  tr:last-child td {{ border-bottom: none; }}
  tr:hover td {{ background: var(--surface2); }}
  .empty-row {{ text-align: center; color: var(--text-muted); font-style: italic; padding: 24px; }}
  .desc-cell {{ max-width: 500px; color: var(--text-muted); font-size: 0.8rem; }}

  /* Score badges */
  .score-badge {{ display: inline-block; padding: 2px 8px; border-radius: 6px; font-weight: 700; font-size: 0.8rem; }}
  .score-badge.critical {{ background: #dc262622; color: #dc2626; border: 1px solid #dc262644; }}
  .score-badge.high {{ background: #ea580c22; color: #ea580c; border: 1px solid #ea580c44; }}
  .score-badge.medium {{ background: #ca8a0422; color: #ca8a04; border: 1px solid #ca8a0444; }}

  /* Misc badges */
  .badge {{ display: inline-block; padding: 2px 10px; border-radius: 9999px; font-size: 0.75rem; font-weight: 600; }}
  .ransomware-known {{ background: #dc262622; color: #dc2626; border: 1px solid #dc262644; }}
  .ransomware-unknown {{ background: #37415122; color: #94a3b8; border: 1px solid #37415144; }}
  .cve-link {{ color: var(--accent); font-family: monospace; }}

  /* Warning */
  .warning-box {{ background: #78350f22; border: 1px solid #92400e; border-radius: 8px; padding: 16px; margin-bottom: 24px; color: #fbbf24; font-size: 0.875rem; }}
  .warning-box ul {{ padding-left: 16px; margin-top: 8px; }}

  /* Footer */
  footer {{ margin-top: 48px; padding: 24px 0; border-top: 1px solid var(--border); text-align: center; color: var(--text-muted); font-size: 0.8rem; }}
  footer a {{ color: var(--text-muted); }}
  footer a:hover {{ color: var(--text); }}
</style>
</head>
<body>

<div class="header">
  <div class="header-left">
    <h1>Vulnerability <span>Intelligence</span> Report</h1>
    <div class="header-meta">Date: {run_date} &nbsp;|&nbsp; Generated: {run_ts}</div>
  </div>
  <div class="risk-badge">
    <span class="risk-dot"></span>
    {risk_level} Risk
  </div>
</div>

<div class="container">
  {warnings_html}

  <div class="kpi-grid">
    <div class="kpi-card">
      <div class="kpi-label">Total CVEs Found</div>
      <div class="kpi-value {'danger' if len(cves) >= 20 else 'warn' if len(cves) >= 5 else ''}">{len(cves)}</div>
      <div class="kpi-sub">CVSS &ge; 7.0 in last 24h</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-label">CVSS Avg Score</div>
      <div class="kpi-value {'danger' if avg_cvss >= 9.0 else 'warn' if avg_cvss >= 7.0 else ''}">{avg_cvss}</div>
      <div class="kpi-sub">across all found CVEs</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-label">KEV New Entries</div>
      <div class="kpi-value {'danger' if len(kev_entries) >= 3 else 'warn' if len(kev_entries) >= 1 else ''}">{len(kev_entries)}</div>
      <div class="kpi-sub">added in last 7 days</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-label">KEV Due This Week</div>
      <div class="kpi-value {'danger' if kev_due_week >= 2 else 'warn' if kev_due_week >= 1 else ''}">{kev_due_week}</div>
      <div class="kpi-sub">remediation deadlines</div>
    </div>
  </div>

  <div class="section">
    <div class="section-title">Executive Summary</div>
    <p>{executive_summary}</p>
  </div>

  <div class="section">
    <div class="section-title">Risk Narrative</div>
    <p>{risk_narrative}</p>
  </div>

  <div class="section">
    <div class="section-title">Prioritized Action Items</div>
    {action_html}
  </div>

  <div class="section">
    <div class="section-title">High Severity CVEs — {len(cves)} found (CVSS &ge; 7.0)</div>
    <div class="table-wrapper">
      <table id="cve-table">
        <thead>
          <tr>
            <th onclick="sortTable('cve-table',0)" data-col="0">CVE ID <span class="sort-icon">&#8597;</span></th>
            <th onclick="sortTable('cve-table',1)" data-col="1">CVSS <span class="sort-icon">&#8597;</span></th>
            <th onclick="sortTable('cve-table',2)" data-col="2">Published <span class="sort-icon">&#8597;</span></th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
{cve_rows_html}
        </tbody>
      </table>
    </div>
  </div>

  <div class="section">
    <div class="section-title">CISA KEV — {len(kev_entries)} new entries (last 7 days)</div>
    <div class="table-wrapper">
      <table id="kev-table">
        <thead>
          <tr>
            <th onclick="sortTable('kev-table',0)" data-col="0">CVE ID <span class="sort-icon">&#8597;</span></th>
            <th onclick="sortTable('kev-table',1)" data-col="1">Vendor / Product <span class="sort-icon">&#8597;</span></th>
            <th onclick="sortTable('kev-table',2)" data-col="2">Date Added <span class="sort-icon">&#8597;</span></th>
            <th onclick="sortTable('kev-table',3)" data-col="3">Due Date <span class="sort-icon">&#8597;</span></th>
            <th>Ransomware</th>
          </tr>
        </thead>
        <tbody>
{kev_rows_html}
        </tbody>
      </table>
    </div>
  </div>

  <footer>
    Data sources: &nbsp;
    <a href="https://nvd.nist.gov/" target="_blank" rel="noopener noreferrer">NVD (National Vulnerability Database)</a>
    &nbsp;&bull;&nbsp;
    <a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog" target="_blank" rel="noopener noreferrer">CISA Known Exploited Vulnerabilities Catalog</a>
    <br><br>
    Generated by Vulnerability Intelligence Pipeline &bull; {run_ts}
  </footer>
</div>

<script>
const sortState = {{}};
function sortTable(tableId, col) {{
  const table = document.getElementById(tableId);
  const tbody = table.querySelector('tbody');
  const rows = Array.from(tbody.querySelectorAll('tr'));
  const key = tableId + ':' + col;
  const asc = sortState[key] !== true;
  sortState[key] = asc;

  // Update sort icons
  table.querySelectorAll('th').forEach((th, i) => {{
    th.classList.toggle('sorted', i === col);
    const icon = th.querySelector('.sort-icon');
    if (icon) icon.textContent = i === col ? (asc ? '↑' : '↓') : '⇅';
  }});

  rows.sort((a, b) => {{
    const aText = (a.cells[col] ? a.cells[col].textContent : '').trim();
    const bText = (b.cells[col] ? b.cells[col].textContent : '').trim();
    const aNum = parseFloat(aText);
    const bNum = parseFloat(bText);
    if (!isNaN(aNum) && !isNaN(bNum)) return asc ? aNum - bNum : bNum - aNum;
    return asc ? aText.localeCompare(bText) : bText.localeCompare(aText);
  }});

  rows.forEach(r => tbody.appendChild(r));
}}
</script>

</body>
</html>"""


def save_html_report(results: dict, report_dir: Path = REPORTS_DIR) -> Path:
    report_dir.mkdir(parents=True, exist_ok=True)
    date_str = results["run_date"]
    html_path = report_dir / f"daily_report_{date_str}.html"
    html_path.write_text(build_html_report(results), encoding="utf-8")
    logger.info("Saved HTML report: %s", html_path)
    return html_path


def update_reports_index(results: dict, docs_dir: Path = DOCS_DIR) -> Path:
    docs_dir.mkdir(parents=True, exist_ok=True)
    index_path = docs_dir / "reports-index.json"

    existing: list = []
    if index_path.exists():
        try:
            existing = json.loads(index_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            existing = []

    date_str = results["run_date"]
    cves = results.get("high_severity_cves", [])
    kev_entries = results.get("new_kev_entries", [])

    entry = {
        "date": date_str,
        "filename": f"daily_report_{date_str}.html",
        "cve_count": len(cves),
        "kev_count": len(kev_entries),
        "risk_level": _compute_risk_level(results),
        "avg_cvss": _compute_avg_cvss(cves),
    }

    existing = [e for e in existing if e.get("date") != date_str]
    existing.append(entry)
    existing.sort(key=lambda e: e.get("date", ""), reverse=True)

    index_path.write_text(json.dumps(existing, indent=2), encoding="utf-8")
    logger.info("Updated reports index: %s", index_path)
    return index_path


def copy_report_to_docs(results: dict, docs_dir: Path = DOCS_DIR) -> Path:
    date_str = results["run_date"]
    src = REPORTS_DIR / f"daily_report_{date_str}.html"
    docs_dir.mkdir(parents=True, exist_ok=True)
    dest = docs_dir / f"daily_report_{date_str}.html"
    dest.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    logger.info("Copied HTML report to docs: %s", dest)
    return dest
