"""
Unit tests for CISA KEV Tracker Agent.

Uses unittest.mock to avoid hitting the live CISA API.
"""

import unittest
from datetime import datetime, timezone
from unittest.mock import MagicMock, patch

from agents.cisa_tracker import (
    fetch_kev_catalog,
    filter_new_entries,
    find_monitored_hits,
    run_cisa_tracker,
)

# ---------------------------------------------------------------------------
# Shared fixtures
# ---------------------------------------------------------------------------

SAMPLE_ENTRY_OLD = {
    "cveID": "CVE-2020-1234",
    "vendorProject": "Acme",
    "product": "WidgetPro",
    "vulnerabilityName": "Acme WidgetPro RCE",
    "dateAdded": "2020-06-15",
    "shortDescription": "Old vulnerability",
    "requiredAction": "Apply patch",
    "dueDate": "2020-07-01",
    "knownRansomwareCampaignUse": "Unknown",
    "notes": "",
}

SAMPLE_ENTRY_RECENT = {
    "cveID": "CVE-2026-9999",
    "vendorProject": "ExampleCorp",
    "product": "SuperLib",
    "vulnerabilityName": "ExampleCorp SuperLib Arbitrary Code Execution",
    "dateAdded": "2026-05-28",
    "shortDescription": "Allows arbitrary code execution",
    "requiredAction": "Update to patched version",
    "dueDate": "2026-06-11",
    "knownRansomwareCampaignUse": "Known",
    "notes": "",
}

SAMPLE_CATALOG = {
    "catalogVersion": "2026.05.30",
    "dateReleased": "2026-05-30T00:00:00Z",
    "count": 2,
    "vulnerabilities": [SAMPLE_ENTRY_OLD, SAMPLE_ENTRY_RECENT],
}


# ---------------------------------------------------------------------------
# fetch_kev_catalog
# ---------------------------------------------------------------------------

class TestFetchKevCatalog(unittest.TestCase):
    """Tests for fetch_kev_catalog function."""

    @patch("agents.cisa_tracker.requests.get")
    def test_returns_parsed_json(self, mock_get):
        """Should return parsed JSON from the CISA feed."""
        mock_response = MagicMock()
        mock_response.json.return_value = SAMPLE_CATALOG
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = fetch_kev_catalog()

        self.assertEqual(result["count"], 2)
        self.assertEqual(len(result["vulnerabilities"]), 2)

    @patch("agents.cisa_tracker.requests.get")
    def test_uses_default_url(self, mock_get):
        """Should request the canonical CISA KEV URL by default."""
        mock_response = MagicMock()
        mock_response.json.return_value = SAMPLE_CATALOG
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        from agents.cisa_tracker import CISA_KEV_URL

        fetch_kev_catalog()

        mock_get.assert_called_once()
        call_args = mock_get.call_args
        self.assertEqual(call_args.args[0], CISA_KEV_URL)

    @patch("agents.cisa_tracker.requests.get")
    def test_custom_url(self, mock_get):
        """Should use a custom URL when provided."""
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        fetch_kev_catalog(url="https://example.com/kev.json")

        mock_get.assert_called_once()
        self.assertEqual(mock_get.call_args.args[0], "https://example.com/kev.json")

    @patch("agents.cisa_tracker.requests.get")
    def test_raises_on_http_error(self, mock_get):
        """Should propagate HTTP errors."""
        import requests as req

        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = req.HTTPError("404")
        mock_get.return_value = mock_response

        with self.assertRaises(req.HTTPError):
            fetch_kev_catalog()


# ---------------------------------------------------------------------------
# filter_new_entries
# ---------------------------------------------------------------------------

class TestFilterNewEntries(unittest.TestCase):
    """Tests for filter_new_entries function."""

    def _ref_date(self):
        return datetime(2026, 5, 30, 12, 0, 0, tzinfo=timezone.utc)

    def test_returns_entries_within_lookback(self):
        """Should include entries added within the last N days."""
        result = filter_new_entries(
            [SAMPLE_ENTRY_OLD, SAMPLE_ENTRY_RECENT],
            days=7,
            reference_date=self._ref_date(),
        )
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["cveID"], "CVE-2026-9999")

    def test_excludes_old_entries(self):
        """Should exclude entries added before the lookback window."""
        result = filter_new_entries(
            [SAMPLE_ENTRY_OLD],
            days=7,
            reference_date=self._ref_date(),
        )
        self.assertEqual(result, [])

    def test_empty_list_returns_empty(self):
        """Should handle an empty vulnerabilities list."""
        result = filter_new_entries([], days=7, reference_date=self._ref_date())
        self.assertEqual(result, [])

    def test_entry_on_cutoff_boundary_is_included(self):
        """An entry dated exactly on the cutoff day should be included."""
        entry = {**SAMPLE_ENTRY_RECENT, "dateAdded": "2026-05-23"}
        result = filter_new_entries(
            [entry],
            days=7,
            reference_date=self._ref_date(),
        )
        self.assertEqual(len(result), 1)

    def test_entry_one_day_before_cutoff_is_excluded(self):
        """An entry dated one day before the cutoff should be excluded."""
        entry = {**SAMPLE_ENTRY_RECENT, "dateAdded": "2026-05-22"}
        result = filter_new_entries(
            [entry],
            days=7,
            reference_date=self._ref_date(),
        )
        self.assertEqual(result, [])

    def test_skips_entry_with_missing_date(self):
        """Should skip entries with no dateAdded field."""
        entry = {**SAMPLE_ENTRY_RECENT, "dateAdded": ""}
        result = filter_new_entries(
            [entry],
            days=7,
            reference_date=self._ref_date(),
        )
        self.assertEqual(result, [])

    def test_skips_entry_with_invalid_date(self):
        """Should skip entries with an unparseable dateAdded value."""
        entry = {**SAMPLE_ENTRY_RECENT, "dateAdded": "not-a-date"}
        result = filter_new_entries(
            [entry],
            days=7,
            reference_date=self._ref_date(),
        )
        self.assertEqual(result, [])

    def test_custom_lookback_window(self):
        """Should respect a custom days parameter."""
        entry = {**SAMPLE_ENTRY_RECENT, "dateAdded": "2026-05-01"}
        result = filter_new_entries(
            [entry],
            days=30,
            reference_date=self._ref_date(),
        )
        self.assertEqual(len(result), 1)


# ---------------------------------------------------------------------------
# find_monitored_hits
# ---------------------------------------------------------------------------

class TestFindMonitoredHits(unittest.TestCase):
    """Tests for find_monitored_hits function."""

    def test_returns_matching_entries(self):
        """Should return entries whose cveID is in the watch list."""
        result = find_monitored_hits(
            [SAMPLE_ENTRY_OLD, SAMPLE_ENTRY_RECENT],
            cve_ids=["CVE-2026-9999"],
        )
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["cveID"], "CVE-2026-9999")

    def test_returns_empty_when_no_match(self):
        """Should return empty list when none of the CVEs are in the catalog."""
        result = find_monitored_hits(
            [SAMPLE_ENTRY_OLD, SAMPLE_ENTRY_RECENT],
            cve_ids=["CVE-1999-0001"],
        )
        self.assertEqual(result, [])

    def test_case_insensitive_matching(self):
        """Should match regardless of CVE ID casing."""
        result = find_monitored_hits(
            [SAMPLE_ENTRY_RECENT],
            cve_ids=["cve-2026-9999"],
        )
        self.assertEqual(len(result), 1)

    def test_empty_cve_ids_returns_empty(self):
        """Should return empty list when no CVE IDs are provided."""
        result = find_monitored_hits(
            [SAMPLE_ENTRY_OLD, SAMPLE_ENTRY_RECENT],
            cve_ids=[],
        )
        self.assertEqual(result, [])

    def test_empty_catalog_returns_empty(self):
        """Should return empty list when the catalog has no entries."""
        result = find_monitored_hits([], cve_ids=["CVE-2026-9999"])
        self.assertEqual(result, [])

    def test_multiple_matches(self):
        """Should return all matching entries when multiple CVEs match."""
        result = find_monitored_hits(
            [SAMPLE_ENTRY_OLD, SAMPLE_ENTRY_RECENT],
            cve_ids=["CVE-2020-1234", "CVE-2026-9999"],
        )
        self.assertEqual(len(result), 2)


# ---------------------------------------------------------------------------
# run_cisa_tracker
# ---------------------------------------------------------------------------

class TestRunCisaTracker(unittest.TestCase):
    """Tests for run_cisa_tracker function."""

    @patch("agents.cisa_tracker.fetch_kev_catalog")
    def test_returns_required_keys(self, mock_fetch):
        """Result dict must contain new_kev_entries, monitored_hits, total_kev_count."""
        mock_fetch.return_value = SAMPLE_CATALOG

        result = run_cisa_tracker(
            cve_ids=[],
            days=7,
        )

        self.assertIn("new_kev_entries", result)
        self.assertIn("monitored_hits", result)
        self.assertIn("total_kev_count", result)

    @patch("agents.cisa_tracker.fetch_kev_catalog")
    def test_total_kev_count_from_catalog(self, mock_fetch):
        """total_kev_count should reflect the catalog's count field."""
        mock_fetch.return_value = SAMPLE_CATALOG

        result = run_cisa_tracker()

        self.assertEqual(result["total_kev_count"], 2)

    @patch("agents.cisa_tracker.fetch_kev_catalog")
    def test_monitored_hits_populated(self, mock_fetch):
        """Should flag a monitored CVE that appears in the catalog."""
        mock_fetch.return_value = SAMPLE_CATALOG

        result = run_cisa_tracker(cve_ids=["CVE-2020-1234"])

        self.assertEqual(len(result["monitored_hits"]), 1)
        self.assertEqual(result["monitored_hits"][0]["cveID"], "CVE-2020-1234")

    @patch("agents.cisa_tracker.fetch_kev_catalog")
    def test_no_monitored_hits_when_no_overlap(self, mock_fetch):
        """Should return empty monitored_hits when watched CVEs are not in catalog."""
        mock_fetch.return_value = SAMPLE_CATALOG

        result = run_cisa_tracker(cve_ids=["CVE-1999-0001"])

        self.assertEqual(result["monitored_hits"], [])

    @patch("agents.cisa_tracker.fetch_kev_catalog")
    def test_default_cve_ids_is_empty(self, mock_fetch):
        """Should work when cve_ids is not provided."""
        mock_fetch.return_value = SAMPLE_CATALOG

        result = run_cisa_tracker()

        self.assertEqual(result["monitored_hits"], [])

    @patch("agents.cisa_tracker.fetch_kev_catalog")
    def test_total_kev_count_falls_back_to_list_length(self, mock_fetch):
        """Should derive count from list length when count key is absent."""
        catalog_no_count = {
            "vulnerabilities": [SAMPLE_ENTRY_OLD, SAMPLE_ENTRY_RECENT]
        }
        mock_fetch.return_value = catalog_no_count

        result = run_cisa_tracker()

        self.assertEqual(result["total_kev_count"], 2)

    @patch("agents.cisa_tracker.fetch_kev_catalog")
    def test_propagates_request_exception(self, mock_fetch):
        """Should let requests.RequestException bubble up."""
        import requests as req

        mock_fetch.side_effect = req.RequestException("network error")

        with self.assertRaises(req.RequestException):
            run_cisa_tracker()


if __name__ == "__main__":
    unittest.main()
