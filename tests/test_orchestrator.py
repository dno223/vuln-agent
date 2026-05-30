"""
Unit tests for the Orchestrator Agent.

Uses unittest.mock to avoid hitting any live APIs or the filesystem.
"""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, call, patch

from agents.orchestrator import build_markdown, run_pipeline, save_reports

# ---------------------------------------------------------------------------
# Shared fixtures
# ---------------------------------------------------------------------------

SAMPLE_CVES = [
    {
        "cve_id": "CVE-2021-44228",
        "description": "Apache Log4j2 RCE via JNDI lookup.",
        "cvss_score": 10.0,
        "published_date": "2021-12-10T00:00:00.000",
    },
    {
        "cve_id": "CVE-2023-44487",
        "description": "HTTP/2 Rapid Reset denial-of-service.",
        "cvss_score": 7.5,
        "published_date": "2023-10-10T00:00:00.000",
    },
]

SAMPLE_KEV_RESULTS = {
    "new_kev_entries": [
        {
            "cveID": "CVE-2024-21762",
            "vendorProject": "Fortinet",
            "product": "FortiOS",
            "vulnerabilityName": "Fortinet FortiOS OOB Write",
            "dateAdded": "2024-02-09",
            "dueDate": "2024-02-16",
            "knownRansomwareCampaignUse": "Known",
        }
    ],
    "monitored_hits": [
        {
            "cveID": "CVE-2021-44228",
            "vendorProject": "Apache",
            "product": "Log4j2",
            "vulnerabilityName": "Apache Log4j2 RCE",
            "dateAdded": "2021-12-10",
            "dueDate": "2021-12-24",
            "knownRansomwareCampaignUse": "Known",
        }
    ],
    "total_kev_count": 1200,
}

SAMPLE_SUMMARY = {
    "executive_summary": "Critical vulnerabilities require immediate attention.",
    "action_items": [
        "Patch Log4j2 immediately.",
        "Update Fortinet FortiOS.",
        "Audit Exchange servers.",
        "Enable WAF rules.",
        "Run emergency vulnerability scan.",
    ],
    "risk_narrative": "The threat landscape is severe. Ransomware actors are active.",
}

FULL_RESULTS = {
    "run_date": "2026-05-30",
    "run_timestamp": "2026-05-30T12:00:00Z",
    "high_severity_cves": SAMPLE_CVES,
    "new_kev_entries": SAMPLE_KEV_RESULTS["new_kev_entries"],
    "monitored_hits": SAMPLE_KEV_RESULTS["monitored_hits"],
    "total_kev_count": 1200,
    "executive_summary": SAMPLE_SUMMARY["executive_summary"],
    "action_items": SAMPLE_SUMMARY["action_items"],
    "risk_narrative": SAMPLE_SUMMARY["risk_narrative"],
    "pipeline_errors": [],
}


# ---------------------------------------------------------------------------
# run_pipeline
# ---------------------------------------------------------------------------

class TestRunPipeline(unittest.TestCase):
    """Tests for run_pipeline() — all three agents are mocked."""

    def _patch_all(self, cves=None, kev=None, summary=None):
        """Helper: returns three patchers for the three imported functions."""
        p1 = patch(
            "agents.orchestrator.get_high_severity_cves",
            return_value=cves if cves is not None else SAMPLE_CVES,
        )
        p2 = patch(
            "agents.orchestrator.run_cisa_tracker",
            return_value=kev if kev is not None else SAMPLE_KEV_RESULTS,
        )
        p3 = patch(
            "agents.orchestrator.generate_summary",
            return_value=summary if summary is not None else SAMPLE_SUMMARY,
        )
        return p1, p2, p3

    def test_returns_required_keys(self):
        p1, p2, p3 = self._patch_all()
        with p1, p2, p3:
            result = run_pipeline()
        for key in (
            "run_date", "run_timestamp", "high_severity_cves",
            "new_kev_entries", "monitored_hits", "total_kev_count",
            "executive_summary", "action_items", "risk_narrative",
            "pipeline_errors",
        ):
            self.assertIn(key, result)

    def test_high_severity_cves_populated(self):
        p1, p2, p3 = self._patch_all()
        with p1, p2, p3:
            result = run_pipeline()
        self.assertEqual(result["high_severity_cves"], SAMPLE_CVES)

    def test_kev_results_populated(self):
        p1, p2, p3 = self._patch_all()
        with p1, p2, p3:
            result = run_pipeline()
        self.assertEqual(result["new_kev_entries"], SAMPLE_KEV_RESULTS["new_kev_entries"])
        self.assertEqual(result["monitored_hits"], SAMPLE_KEV_RESULTS["monitored_hits"])
        self.assertEqual(result["total_kev_count"], 1200)

    def test_summary_populated(self):
        p1, p2, p3 = self._patch_all()
        with p1, p2, p3:
            result = run_pipeline()
        self.assertEqual(result["executive_summary"], SAMPLE_SUMMARY["executive_summary"])
        self.assertEqual(result["action_items"], SAMPLE_SUMMARY["action_items"])
        self.assertEqual(result["risk_narrative"], SAMPLE_SUMMARY["risk_narrative"])

    def test_no_errors_on_full_success(self):
        p1, p2, p3 = self._patch_all()
        with p1, p2, p3:
            result = run_pipeline()
        self.assertEqual(result["pipeline_errors"], [])

    def test_cve_ids_passed_to_cisa_tracker(self):
        p1, p2, p3 = self._patch_all()
        with p1, p2 as mock_kev, p3:
            run_pipeline()
        call_kwargs = mock_kev.call_args.kwargs
        self.assertIn("CVE-2021-44228", call_kwargs["cve_ids"])
        self.assertIn("CVE-2023-44487", call_kwargs["cve_ids"])

    def test_cisa_tracker_receives_empty_ids_when_no_cves(self):
        p1, p2, p3 = self._patch_all(cves=[])
        with p1, p2 as mock_kev, p3:
            run_pipeline()
        self.assertEqual(mock_kev.call_args.kwargs["cve_ids"], [])

    def test_cve_monitor_failure_continues_pipeline(self):
        p2 = patch("agents.orchestrator.run_cisa_tracker", return_value=SAMPLE_KEV_RESULTS)
        p3 = patch("agents.orchestrator.generate_summary", return_value=SAMPLE_SUMMARY)
        with patch("agents.orchestrator.get_high_severity_cves", side_effect=Exception("NVD down")):
            with p2, p3:
                result = run_pipeline()
        self.assertEqual(result["high_severity_cves"], [])
        self.assertEqual(len(result["pipeline_errors"]), 1)
        self.assertIn("cve_monitor failed", result["pipeline_errors"][0])

    def test_cisa_tracker_failure_continues_pipeline(self):
        p1 = patch("agents.orchestrator.get_high_severity_cves", return_value=SAMPLE_CVES)
        p3 = patch("agents.orchestrator.generate_summary", return_value=SAMPLE_SUMMARY)
        with p1, patch("agents.orchestrator.run_cisa_tracker", side_effect=Exception("CISA down")), p3:
            result = run_pipeline()
        self.assertEqual(result["new_kev_entries"], [])
        self.assertEqual(result["total_kev_count"], 0)
        self.assertEqual(len(result["pipeline_errors"]), 1)
        self.assertIn("cisa_tracker failed", result["pipeline_errors"][0])

    def test_summarizer_failure_continues_pipeline(self):
        p1 = patch("agents.orchestrator.get_high_severity_cves", return_value=SAMPLE_CVES)
        p2 = patch("agents.orchestrator.run_cisa_tracker", return_value=SAMPLE_KEV_RESULTS)
        with p1, p2, patch("agents.orchestrator.generate_summary", side_effect=Exception("API error")):
            result = run_pipeline()
        self.assertEqual(result["executive_summary"], "")
        self.assertEqual(result["action_items"], [])
        self.assertEqual(len(result["pipeline_errors"]), 1)
        self.assertIn("summarizer failed", result["pipeline_errors"][0])

    def test_all_three_failures_recorded(self):
        with (
            patch("agents.orchestrator.get_high_severity_cves", side_effect=Exception("err1")),
            patch("agents.orchestrator.run_cisa_tracker", side_effect=Exception("err2")),
            patch("agents.orchestrator.generate_summary", side_effect=Exception("err3")),
        ):
            result = run_pipeline()
        self.assertEqual(len(result["pipeline_errors"]), 3)

    def test_run_date_is_today_format(self):
        p1, p2, p3 = self._patch_all()
        with p1, p2, p3:
            result = run_pipeline()
        import re
        self.assertRegex(result["run_date"], r"^\d{4}-\d{2}-\d{2}$")

    def test_run_timestamp_format(self):
        p1, p2, p3 = self._patch_all()
        with p1, p2, p3:
            result = run_pipeline()
        import re
        self.assertRegex(result["run_timestamp"], r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

    def test_cvss_threshold_forwarded_to_cve_monitor(self):
        p2 = patch("agents.orchestrator.run_cisa_tracker", return_value=SAMPLE_KEV_RESULTS)
        p3 = patch("agents.orchestrator.generate_summary", return_value=SAMPLE_SUMMARY)
        with patch("agents.orchestrator.get_high_severity_cves", return_value=[]) as mock_cves:
            with p2, p3:
                run_pipeline(cvss_threshold=9.0)
        mock_cves.assert_called_once_with(cvss_threshold=9.0)


# ---------------------------------------------------------------------------
# build_markdown
# ---------------------------------------------------------------------------

class TestBuildMarkdown(unittest.TestCase):
    """Tests for build_markdown()."""

    def test_contains_report_title(self):
        md = build_markdown(FULL_RESULTS)
        self.assertIn("# Vulnerability Intelligence Report", md)

    def test_contains_run_date(self):
        md = build_markdown(FULL_RESULTS)
        self.assertIn("2026-05-30", md)

    def test_contains_executive_summary(self):
        md = build_markdown(FULL_RESULTS)
        self.assertIn(SAMPLE_SUMMARY["executive_summary"], md)

    def test_contains_risk_narrative(self):
        md = build_markdown(FULL_RESULTS)
        self.assertIn(SAMPLE_SUMMARY["risk_narrative"], md)

    def test_action_items_numbered(self):
        md = build_markdown(FULL_RESULTS)
        self.assertIn("1. Patch Log4j2 immediately.", md)
        self.assertIn("5. Run emergency vulnerability scan.", md)

    def test_cve_table_contains_cve_id(self):
        md = build_markdown(FULL_RESULTS)
        self.assertIn("CVE-2021-44228", md)

    def test_cve_table_contains_cvss_score(self):
        md = build_markdown(FULL_RESULTS)
        self.assertIn("10.0", md)

    def test_kev_table_contains_vendor(self):
        md = build_markdown(FULL_RESULTS)
        self.assertIn("Fortinet", md)
        self.assertIn("FortiOS", md)

    def test_kev_table_contains_date_added(self):
        md = build_markdown(FULL_RESULTS)
        self.assertIn("2024-02-09", md)

    def test_empty_cves_shows_placeholder(self):
        results = {**FULL_RESULTS, "high_severity_cves": []}
        md = build_markdown(results)
        self.assertIn("No high-severity CVEs found", md)

    def test_empty_kev_entries_shows_placeholder(self):
        results = {**FULL_RESULTS, "new_kev_entries": []}
        md = build_markdown(results)
        self.assertIn("No new CISA KEV entries", md)

    def test_empty_summary_shows_placeholder(self):
        results = {**FULL_RESULTS, "executive_summary": ""}
        md = build_markdown(results)
        self.assertIn("No summary available", md)

    def test_empty_action_items_shows_placeholder(self):
        results = {**FULL_RESULTS, "action_items": []}
        md = build_markdown(results)
        self.assertIn("No action items available", md)

    def test_pipeline_errors_section_shown_when_present(self):
        results = {**FULL_RESULTS, "pipeline_errors": ["cve_monitor failed: timeout"]}
        md = build_markdown(results)
        self.assertIn("Pipeline Warnings", md)
        self.assertIn("cve_monitor failed: timeout", md)

    def test_pipeline_errors_section_absent_when_empty(self):
        md = build_markdown(FULL_RESULTS)
        self.assertNotIn("Pipeline Warnings", md)

    def test_total_kev_count_shown(self):
        md = build_markdown(FULL_RESULTS)
        self.assertIn("1200", md)

    def test_returns_string(self):
        md = build_markdown(FULL_RESULTS)
        self.assertIsInstance(md, str)


# ---------------------------------------------------------------------------
# save_reports
# ---------------------------------------------------------------------------

class TestSaveReports(unittest.TestCase):
    """Tests for save_reports() using a real temporary directory."""

    def test_creates_json_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            json_path, _ = save_reports(FULL_RESULTS, Path(tmpdir))
            self.assertTrue(json_path.exists())

    def test_creates_markdown_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            _, md_path = save_reports(FULL_RESULTS, Path(tmpdir))
            self.assertTrue(md_path.exists())

    def test_json_filename_contains_date(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            json_path, _ = save_reports(FULL_RESULTS, Path(tmpdir))
            self.assertIn("2026-05-30", json_path.name)

    def test_markdown_filename_contains_date(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            _, md_path = save_reports(FULL_RESULTS, Path(tmpdir))
            self.assertIn("2026-05-30", md_path.name)

    def test_json_file_is_valid_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            json_path, _ = save_reports(FULL_RESULTS, Path(tmpdir))
            data = json.loads(json_path.read_text())
            self.assertIn("run_date", data)

    def test_json_file_contains_cves(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            json_path, _ = save_reports(FULL_RESULTS, Path(tmpdir))
            data = json.loads(json_path.read_text())
            self.assertEqual(len(data["high_severity_cves"]), 2)

    def test_markdown_file_contains_report_header(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            _, md_path = save_reports(FULL_RESULTS, Path(tmpdir))
            content = md_path.read_text()
            self.assertIn("# Vulnerability Intelligence Report", content)

    def test_creates_report_dir_if_missing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            nested = Path(tmpdir) / "new" / "nested" / "dir"
            save_reports(FULL_RESULTS, nested)
            self.assertTrue(nested.exists())

    def test_returns_tuple_of_paths(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            result = save_reports(FULL_RESULTS, Path(tmpdir))
            self.assertIsInstance(result, tuple)
            self.assertEqual(len(result), 2)
            json_path, md_path = result
            self.assertIsInstance(json_path, Path)
            self.assertIsInstance(md_path, Path)

    def test_json_has_daily_report_prefix(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            json_path, _ = save_reports(FULL_RESULTS, Path(tmpdir))
            self.assertTrue(json_path.name.startswith("daily_report_"))
            self.assertTrue(json_path.name.endswith(".json"))

    def test_markdown_has_daily_report_prefix(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            _, md_path = save_reports(FULL_RESULTS, Path(tmpdir))
            self.assertTrue(md_path.name.startswith("daily_report_"))
            self.assertTrue(md_path.name.endswith(".md"))


if __name__ == "__main__":
    unittest.main()
