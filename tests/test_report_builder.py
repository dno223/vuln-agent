"""
Unit tests for the Report Builder agent.
"""

import json
import tempfile
import unittest
from pathlib import Path

from agents.report_builder import (
    _compute_avg_cvss,
    _compute_risk_level,
    _cvss_class,
    _kev_due_this_week,
    build_html_report,
    copy_report_to_docs,
    save_html_report,
    update_reports_index,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SAMPLE_CVES = [
    {"cve_id": "CVE-2021-44228", "description": "Log4Shell RCE.", "cvss_score": 10.0, "published_date": "2021-12-10"},
    {"cve_id": "CVE-2023-44487", "description": "HTTP/2 Rapid Reset.", "cvss_score": 7.5, "published_date": "2023-10-10"},
    {"cve_id": "CVE-2024-12345", "description": "Some vulnerability.", "cvss_score": 8.0, "published_date": "2024-01-01"},
]

SAMPLE_KEV_ENTRIES = [
    {
        "cveID": "CVE-2024-21762",
        "vendorProject": "Fortinet",
        "product": "FortiOS",
        "vulnerabilityName": "Fortinet OOB Write",
        "dateAdded": "2024-02-09",
        "dueDate": "2024-02-16",
        "knownRansomwareCampaignUse": "Known",
    },
    {
        "cveID": "CVE-2024-99999",
        "vendorProject": "Acme",
        "product": "Widget",
        "vulnerabilityName": "Acme RCE",
        "dateAdded": "2024-03-01",
        "dueDate": "2024-03-10",
        "knownRansomwareCampaignUse": "Unknown",
    },
]

MINIMAL_RESULTS = {
    "run_date": "2026-05-30",
    "run_timestamp": "2026-05-30T08:00:00Z",
    "high_severity_cves": SAMPLE_CVES,
    "new_kev_entries": SAMPLE_KEV_ENTRIES,
    "monitored_hits": [],
    "total_kev_count": 1200,
    "executive_summary": "Test executive summary.",
    "action_items": ["Patch Log4j immediately.", "Update FortiOS."],
    "risk_narrative": "Test risk narrative.",
    "pipeline_errors": [],
}


# ---------------------------------------------------------------------------
# _compute_risk_level
# ---------------------------------------------------------------------------

class TestComputeRiskLevel(unittest.TestCase):
    def test_critical_high_cvss(self):
        results = {"high_severity_cves": [{"cvss_score": 9.5}], "monitored_hits": [], "new_kev_entries": []}
        self.assertEqual(_compute_risk_level(results), "Critical")

    def test_critical_monitored_hits(self):
        results = {"high_severity_cves": [{"cvss_score": 7.0}], "monitored_hits": [{"cveID": "CVE-X"}], "new_kev_entries": []}
        self.assertEqual(_compute_risk_level(results), "Critical")

    def test_high_kev_entries(self):
        results = {"high_severity_cves": [], "monitored_hits": [], "new_kev_entries": [{"cveID": "CVE-X"}]}
        self.assertEqual(_compute_risk_level(results), "High")

    def test_high_cvss_borderline(self):
        results = {"high_severity_cves": [{"cvss_score": 7.5}], "monitored_hits": [], "new_kev_entries": []}
        self.assertEqual(_compute_risk_level(results), "High")

    def test_medium_no_threats(self):
        results = {"high_severity_cves": [], "monitored_hits": [], "new_kev_entries": []}
        self.assertEqual(_compute_risk_level(results), "Medium")

    def test_empty_dict(self):
        self.assertEqual(_compute_risk_level({}), "Medium")


# ---------------------------------------------------------------------------
# _compute_avg_cvss
# ---------------------------------------------------------------------------

class TestComputeAvgCvss(unittest.TestCase):
    def test_normal_average(self):
        cves = [{"cvss_score": 9.0}, {"cvss_score": 7.0}]
        self.assertEqual(_compute_avg_cvss(cves), 8.0)

    def test_single_cve(self):
        cves = [{"cvss_score": 8.5}]
        self.assertEqual(_compute_avg_cvss(cves), 8.5)

    def test_empty_list(self):
        self.assertEqual(_compute_avg_cvss([]), 0.0)

    def test_missing_score_ignored(self):
        cves = [{"cvss_score": 8.0}, {"description": "no score"}]
        self.assertEqual(_compute_avg_cvss(cves), 8.0)

    def test_rounding(self):
        cves = [{"cvss_score": 7.0}, {"cvss_score": 8.0}, {"cvss_score": 9.0}]
        self.assertEqual(_compute_avg_cvss(cves), 8.0)


# ---------------------------------------------------------------------------
# _cvss_class
# ---------------------------------------------------------------------------

class TestCvssClass(unittest.TestCase):
    def test_critical(self):
        self.assertEqual(_cvss_class(9.0), "critical")
        self.assertEqual(_cvss_class(10.0), "critical")

    def test_high(self):
        self.assertEqual(_cvss_class(7.0), "high")
        self.assertEqual(_cvss_class(8.9), "high")

    def test_medium(self):
        self.assertEqual(_cvss_class(6.9), "medium")
        self.assertEqual(_cvss_class(0.0), "medium")


# ---------------------------------------------------------------------------
# _kev_due_this_week
# ---------------------------------------------------------------------------

class TestKevDueThisWeek(unittest.TestCase):
    def test_entry_due_tomorrow(self):
        entries = [{"dueDate": "2026-05-31"}]
        self.assertEqual(_kev_due_this_week(entries, "2026-05-30"), 1)

    def test_entry_due_exactly_seven_days(self):
        entries = [{"dueDate": "2026-06-06"}]
        self.assertEqual(_kev_due_this_week(entries, "2026-05-30"), 1)

    def test_entry_due_past(self):
        entries = [{"dueDate": "2026-05-20"}]
        self.assertEqual(_kev_due_this_week(entries, "2026-05-30"), 0)

    def test_entry_due_far_future(self):
        entries = [{"dueDate": "2026-07-01"}]
        self.assertEqual(_kev_due_this_week(entries, "2026-05-30"), 0)

    def test_empty_entries(self):
        self.assertEqual(_kev_due_this_week([], "2026-05-30"), 0)

    def test_invalid_date_skipped(self):
        entries = [{"dueDate": "not-a-date"}, {"dueDate": "2026-06-01"}]
        self.assertEqual(_kev_due_this_week(entries, "2026-05-30"), 1)

    def test_multiple_entries(self):
        entries = [
            {"dueDate": "2026-06-01"},
            {"dueDate": "2026-06-03"},
            {"dueDate": "2026-07-01"},
        ]
        self.assertEqual(_kev_due_this_week(entries, "2026-05-30"), 2)


# ---------------------------------------------------------------------------
# build_html_report
# ---------------------------------------------------------------------------

class TestBuildHtmlReport(unittest.TestCase):
    def setUp(self):
        self.html = build_html_report(MINIMAL_RESULTS)

    def test_returns_string(self):
        self.assertIsInstance(self.html, str)

    def test_has_doctype(self):
        self.assertTrue(self.html.strip().startswith("<!DOCTYPE html>"))

    def test_contains_run_date(self):
        self.assertIn("2026-05-30", self.html)

    def test_contains_run_timestamp(self):
        self.assertIn("2026-05-30T08:00:00Z", self.html)

    def test_contains_executive_summary(self):
        self.assertIn("Test executive summary.", self.html)

    def test_contains_risk_narrative(self):
        self.assertIn("Test risk narrative.", self.html)

    def test_contains_action_items(self):
        self.assertIn("Patch Log4j immediately.", self.html)
        self.assertIn("Update FortiOS.", self.html)

    def test_contains_cve_ids(self):
        self.assertIn("CVE-2021-44228", self.html)
        self.assertIn("CVE-2023-44487", self.html)

    def test_contains_kev_entries(self):
        self.assertIn("CVE-2024-21762", self.html)
        self.assertIn("Fortinet", self.html)

    def test_contains_risk_level(self):
        self.assertIn("Critical", self.html)

    def test_ransomware_known_badge(self):
        self.assertIn("ransomware-known", self.html)

    def test_ransomware_unknown_badge(self):
        self.assertIn("ransomware-unknown", self.html)

    def test_contains_nvd_link(self):
        self.assertIn("nvd.nist.gov", self.html)

    def test_contains_cisa_link(self):
        self.assertIn("cisa.gov", self.html)

    def test_sortable_table_script(self):
        self.assertIn("sortTable", self.html)

    def test_no_external_css(self):
        self.assertNotIn('<link rel="stylesheet"', self.html)

    def test_pipeline_warnings_shown(self):
        results_with_errors = {**MINIMAL_RESULTS, "pipeline_errors": ["cve_monitor failed"]}
        html = build_html_report(results_with_errors)
        self.assertIn("cve_monitor failed", html)

    def test_empty_cves_shows_placeholder(self):
        results = {**MINIMAL_RESULTS, "high_severity_cves": []}
        html = build_html_report(results)
        self.assertIn("No high-severity CVEs found", html)

    def test_empty_kev_shows_placeholder(self):
        results = {**MINIMAL_RESULTS, "new_kev_entries": []}
        html = build_html_report(results)
        self.assertIn("No new KEV entries found", html)

    def test_medium_risk_when_no_threats(self):
        results = {
            **MINIMAL_RESULTS,
            "high_severity_cves": [],
            "new_kev_entries": [],
            "monitored_hits": [],
        }
        html = build_html_report(results)
        self.assertIn("Medium", html)


# ---------------------------------------------------------------------------
# save_html_report
# ---------------------------------------------------------------------------

class TestSaveHtmlReport(unittest.TestCase):
    def test_creates_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = save_html_report(MINIMAL_RESULTS, Path(tmp))
            self.assertTrue(path.exists())
            self.assertEqual(path.name, "daily_report_2026-05-30.html")

    def test_file_has_html_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = save_html_report(MINIMAL_RESULTS, Path(tmp))
            content = path.read_text(encoding="utf-8")
            self.assertIn("<!DOCTYPE html>", content)

    def test_creates_parent_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            nested = Path(tmp) / "a" / "b"
            path = save_html_report(MINIMAL_RESULTS, nested)
            self.assertTrue(path.exists())


# ---------------------------------------------------------------------------
# update_reports_index
# ---------------------------------------------------------------------------

class TestUpdateReportsIndex(unittest.TestCase):
    def test_creates_index_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            update_reports_index(MINIMAL_RESULTS, Path(tmp))
            idx = Path(tmp) / "reports-index.json"
            self.assertTrue(idx.exists())

    def test_index_contains_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            update_reports_index(MINIMAL_RESULTS, Path(tmp))
            data = json.loads((Path(tmp) / "reports-index.json").read_text())
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["date"], "2026-05-30")

    def test_index_entry_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            update_reports_index(MINIMAL_RESULTS, Path(tmp))
            entry = json.loads((Path(tmp) / "reports-index.json").read_text())[0]
            self.assertIn("date", entry)
            self.assertIn("filename", entry)
            self.assertIn("cve_count", entry)
            self.assertIn("kev_count", entry)
            self.assertIn("risk_level", entry)
            self.assertIn("avg_cvss", entry)

    def test_upsert_same_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            update_reports_index(MINIMAL_RESULTS, Path(tmp))
            update_reports_index(MINIMAL_RESULTS, Path(tmp))
            data = json.loads((Path(tmp) / "reports-index.json").read_text())
            self.assertEqual(len(data), 1)

    def test_multiple_dates_sorted_desc(self):
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp)
            r1 = {**MINIMAL_RESULTS, "run_date": "2026-05-28", "high_severity_cves": SAMPLE_CVES[:1], "new_kev_entries": []}
            r2 = {**MINIMAL_RESULTS, "run_date": "2026-05-30"}
            update_reports_index(r1, docs)
            update_reports_index(r2, docs)
            data = json.loads((docs / "reports-index.json").read_text())
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]["date"], "2026-05-30")
            self.assertEqual(data[1]["date"], "2026-05-28")

    def test_handles_corrupted_index(self):
        with tempfile.TemporaryDirectory() as tmp:
            idx = Path(tmp) / "reports-index.json"
            idx.write_text("INVALID JSON", encoding="utf-8")
            update_reports_index(MINIMAL_RESULTS, Path(tmp))
            data = json.loads(idx.read_text())
            self.assertEqual(len(data), 1)


# ---------------------------------------------------------------------------
# copy_report_to_docs
# ---------------------------------------------------------------------------

class TestCopyReportToDocs(unittest.TestCase):
    def test_copies_file(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp = Path(tmp_dir)
            reports_dir = tmp / "reports"
            docs_dir = tmp / "docs"

            # Write the HTML to reports dir first
            save_html_report(MINIMAL_RESULTS, reports_dir)

            # Monkey-patch REPORTS_DIR in the module
            import agents.report_builder as rb
            orig = rb.REPORTS_DIR
            rb.REPORTS_DIR = reports_dir
            try:
                dest = copy_report_to_docs(MINIMAL_RESULTS, docs_dir)
                self.assertTrue(dest.exists())
                self.assertEqual(dest.name, "daily_report_2026-05-30.html")
            finally:
                rb.REPORTS_DIR = orig


if __name__ == "__main__":
    unittest.main()
