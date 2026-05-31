"""
Orchestrator Agent - Chains cve_monitor → cisa_tracker → summarizer into a
single daily vulnerability intelligence pipeline.

Saves results to outputs/reports/ as both JSON (raw data) and Markdown.
"""

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from agents.cisa_tracker import run_cisa_tracker
from agents.cve_monitor import get_high_severity_cves
from agents.report_builder import copy_report_to_docs, save_html_report, update_reports_index
from agents.summarizer import generate_summary

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

REPORTS_DIR = Path(__file__).parent.parent / "outputs" / "reports"
CVSS_THRESHOLD = float(os.getenv("CVSS_THRESHOLD", "7.0"))


def run_pipeline(cvss_threshold: float = CVSS_THRESHOLD) -> dict:
    """
    Execute the full vulnerability intelligence pipeline in sequence.

    Steps:
      1. Fetch high-severity CVEs from NVD (last 24 h, CVSS ≥ threshold)
      2. Cross-reference with the CISA KEV catalog
      3. Generate an executive summary via the Claude API

    Each step runs independently: if one raises an exception it is logged
    and the pipeline continues with whatever data is available.

    Args:
        cvss_threshold: Minimum CVSS score for CVE inclusion (default: 7.0)

    Returns:
        Flat results dict containing all pipeline outputs plus metadata.
    """
    now = datetime.now(timezone.utc)
    results: dict = {
        "run_date": now.strftime("%Y-%m-%d"),
        "run_timestamp": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "high_severity_cves": [],
        "new_kev_entries": [],
        "monitored_hits": [],
        "total_kev_count": 0,
        "executive_summary": "",
        "action_items": [],
        "risk_narrative": "",
        "pipeline_errors": [],
    }

    # Step 1 — CVE Monitor
    logger.info("Step 1/3: Fetching high-severity CVEs from NVD API")
    try:
        results["high_severity_cves"] = get_high_severity_cves(
            cvss_threshold=cvss_threshold
        )
        logger.info("Fetched %d high-severity CVEs", len(results["high_severity_cves"]))
    except Exception as e:
        msg = f"cve_monitor failed: {e}"
        logger.error(msg)
        results["pipeline_errors"].append(msg)

    # Step 2 — CISA Tracker
    logger.info("Step 2/3: Cross-referencing with CISA KEV catalog")
    cve_ids = [cve["cve_id"] for cve in results["high_severity_cves"]]
    try:
        kev_results = run_cisa_tracker(cve_ids=cve_ids)
        results["new_kev_entries"] = kev_results["new_kev_entries"]
        results["monitored_hits"] = kev_results["monitored_hits"]
        results["total_kev_count"] = kev_results["total_kev_count"]
        logger.info(
            "KEV: %d new entries, %d monitored hits, %d total in catalog",
            len(results["new_kev_entries"]),
            len(results["monitored_hits"]),
            results["total_kev_count"],
        )
    except Exception as e:
        msg = f"cisa_tracker failed: {e}"
        logger.error(msg)
        results["pipeline_errors"].append(msg)

    # Step 3 — Summarizer
    logger.info("Step 3/3: Generating executive summary via Claude API")
    vulnerability_data = {
        "high_severity_cves": results["high_severity_cves"],
        "new_kev_entries": results["new_kev_entries"],
        "monitored_hits": results["monitored_hits"],
    }
    try:
        summary = generate_summary(vulnerability_data)
        results["executive_summary"] = summary["executive_summary"]
        results["action_items"] = summary["action_items"]
        results["risk_narrative"] = summary["risk_narrative"]
    except Exception as e:
        msg = f"summarizer failed: {e}"
        logger.error(msg)
        results["pipeline_errors"].append(msg)

    return results


def build_markdown(results: dict) -> str:
    """
    Render pipeline results as a formatted Markdown report.

    Args:
        results: Dict returned by run_pipeline()

    Returns:
        Multi-line Markdown string.
    """
    lines: list[str] = []

    lines += [
        "# Vulnerability Intelligence Report",
        "",
        f"**Date:** {results['run_date']}  ",
        f"**Generated:** {results['run_timestamp']}  ",
        "",
    ]

    if results.get("pipeline_errors"):
        lines += ["## Pipeline Warnings", ""]
        for err in results["pipeline_errors"]:
            lines.append(f"- {err}")
        lines.append("")

    # Executive Summary
    lines += [
        "---",
        "",
        "## Executive Summary",
        "",
        results.get("executive_summary") or "_No summary available._",
        "",
    ]

    # Risk Narrative
    lines += [
        "---",
        "",
        "## Risk Narrative",
        "",
        results.get("risk_narrative") or "_No risk narrative available._",
        "",
    ]

    # Action Items
    lines += ["---", "", "## Prioritized Action Items", ""]
    action_items = results.get("action_items") or []
    if action_items:
        for i, item in enumerate(action_items, 1):
            lines.append(f"{i}. {item}")
    else:
        lines.append("_No action items available._")
    lines.append("")

    # CVE Table
    cves = results.get("high_severity_cves") or []
    lines += ["---", "", f"## High Severity CVEs (CVSS ≥ 7.0)", ""]
    if cves:
        lines += [
            "| CVE ID | CVSS | Published | Description |",
            "|--------|------|-----------|-------------|",
        ]
        for cve in cves:
            desc = cve.get("description", "")[:120].replace("|", "\\|")
            pub = str(cve.get("published_date", ""))[:10]
            lines.append(
                f"| {cve.get('cve_id', '')} "
                f"| {cve.get('cvss_score', '')} "
                f"| {pub} "
                f"| {desc} |"
            )
    else:
        lines.append("_No high-severity CVEs found in the last 24 hours._")
    lines.append("")

    # KEV New Entries Table
    kev_entries = results.get("new_kev_entries") or []
    lines += ["---", "", "## CISA KEV New Entries (Last 7 Days)", ""]
    if kev_entries:
        lines += [
            "| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |",
            "|--------|-----------------|------------|----------|------------|",
        ]
        for entry in kev_entries:
            vendor_product = (
                f"{entry.get('vendorProject', '')} / {entry.get('product', '')}"
            )
            lines.append(
                f"| {entry.get('cveID', '')} "
                f"| {vendor_product} "
                f"| {entry.get('dateAdded', '')} "
                f"| {entry.get('dueDate', '')} "
                f"| {entry.get('knownRansomwareCampaignUse', '')} |"
            )
    else:
        lines.append("_No new CISA KEV entries in the last 7 days._")
    lines.append("")

    lines += [
        "---",
        "",
        f"*Total entries in CISA KEV catalog: {results.get('total_kev_count', 0)}*",
    ]

    return "\n".join(lines)


def save_reports(results: dict, report_dir: Path = REPORTS_DIR) -> tuple[Path, Path]:
    """
    Write JSON and Markdown reports to disk.

    Args:
        results: Dict returned by run_pipeline()
        report_dir: Directory to write reports into (created if absent)

    Returns:
        Tuple of (json_path, markdown_path).
    """
    report_dir.mkdir(parents=True, exist_ok=True)
    date_str = results["run_date"]

    json_path = report_dir / f"daily_report_{date_str}.json"
    json_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    logger.info("Saved JSON report: %s", json_path)

    md_path = report_dir / f"daily_report_{date_str}.md"
    md_path.write_text(build_markdown(results), encoding="utf-8")
    logger.info("Saved Markdown report: %s", md_path)

    return json_path, md_path


def save_all_reports(results: dict, report_dir: Path = REPORTS_DIR) -> tuple[Path, Path, Path]:
    """
    Write JSON, Markdown, and HTML reports, then update the docs index.

    Args:
        results: Dict returned by run_pipeline()
        report_dir: Directory to write reports into

    Returns:
        Tuple of (json_path, markdown_path, html_path).
    """
    json_path, md_path = save_reports(results, report_dir)
    html_path = save_html_report(results, report_dir)
    update_reports_index(results)
    copy_report_to_docs(results)
    return json_path, md_path, html_path


def main() -> None:
    """Entry point — runs the full pipeline and saves reports."""
    logger.info("Starting vulnerability intelligence pipeline")

    results = run_pipeline()

    json_path, md_path, html_path = save_all_reports(results)

    error_count = len(results["pipeline_errors"])
    print("\nPipeline complete.")
    print(f"  High-severity CVEs : {len(results['high_severity_cves'])}")
    print(f"  New KEV entries    : {len(results['new_kev_entries'])}")
    print(f"  Monitored hits     : {len(results['monitored_hits'])}")
    print(f"  Pipeline errors    : {error_count}")
    print(f"  JSON report        : {json_path}")
    print(f"  Markdown report    : {md_path}")
    print(f"  HTML report        : {html_path}")

    if error_count:
        print("\nPipeline warnings:")
        for err in results["pipeline_errors"]:
            print(f"  - {err}")


if __name__ == "__main__":
    main()
