"""
Unit tests for CVE Monitor Agent.

Uses unittest.mock to avoid hitting the live NVD API.
"""

import unittest
from datetime import datetime, timezone
from unittest.mock import MagicMock, patch

from agents.cve_monitor import (
    extract_cvss_score,
    extract_description,
    fetch_cves,
    filter_and_format_cves,
    get_high_severity_cves,
    get_nvd_api_key,
)


class TestGetNvdApiKey(unittest.TestCase):
    """Tests for get_nvd_api_key function."""

    @patch.dict("os.environ", {"NVD_API_KEY": "test-api-key"})
    def test_returns_api_key_when_set(self):
        """Should return the API key when NVD_API_KEY is set."""
        result = get_nvd_api_key()
        self.assertEqual(result, "test-api-key")

    @patch.dict("os.environ", {}, clear=True)
    def test_returns_none_when_not_set(self):
        """Should return None when NVD_API_KEY is not set."""
        result = get_nvd_api_key()
        self.assertIsNone(result)


class TestFetchCves(unittest.TestCase):
    """Tests for fetch_cves function."""

    @patch("agents.cve_monitor.requests.get")
    def test_fetch_cves_success(self, mock_get):
        """Should return vulnerabilities list on successful API call."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "vulnerabilities": [{"cve": {"id": "CVE-2024-0001"}}]
        }
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = fetch_cves()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["cve"]["id"], "CVE-2024-0001")

    @patch("agents.cve_monitor.requests.get")
    def test_fetch_cves_with_api_key(self, mock_get):
        """Should include API key in headers when provided."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"vulnerabilities": []}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        fetch_cves(api_key="test-key")

        call_kwargs = mock_get.call_args.kwargs
        self.assertEqual(call_kwargs["headers"]["apiKey"], "test-key")

    @patch("agents.cve_monitor.requests.get")
    def test_fetch_cves_with_custom_dates(self, mock_get):
        """Should use provided start and end dates."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"vulnerabilities": []}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        start = datetime(2024, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        end = datetime(2024, 1, 2, 0, 0, 0, tzinfo=timezone.utc)

        fetch_cves(start_date=start, end_date=end)

        call_kwargs = mock_get.call_args.kwargs
        self.assertIn("pubStartDate", call_kwargs["params"])
        self.assertIn("2024-01-01", call_kwargs["params"]["pubStartDate"])

    @patch("agents.cve_monitor.requests.get")
    def test_fetch_cves_empty_response(self, mock_get):
        """Should handle empty vulnerabilities list."""
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = fetch_cves()

        self.assertEqual(result, [])


class TestExtractCvssScore(unittest.TestCase):
    """Tests for extract_cvss_score function."""

    def test_extract_cvss_v31(self):
        """Should extract CVSS v3.1 score."""
        cve_item = {
            "cve": {
                "metrics": {
                    "cvssMetricV31": [{"cvssData": {"baseScore": 9.8}}]
                }
            }
        }
        result = extract_cvss_score(cve_item)
        self.assertEqual(result, 9.8)

    def test_extract_cvss_v30(self):
        """Should extract CVSS v3.0 score when v3.1 not available."""
        cve_item = {
            "cve": {
                "metrics": {
                    "cvssMetricV30": [{"cvssData": {"baseScore": 8.5}}]
                }
            }
        }
        result = extract_cvss_score(cve_item)
        self.assertEqual(result, 8.5)

    def test_extract_cvss_v2(self):
        """Should extract CVSS v2.0 score when v3.x not available."""
        cve_item = {
            "cve": {
                "metrics": {
                    "cvssMetricV2": [{"cvssData": {"baseScore": 7.5}}]
                }
            }
        }
        result = extract_cvss_score(cve_item)
        self.assertEqual(result, 7.5)

    def test_extract_cvss_prefers_v31(self):
        """Should prefer v3.1 over v3.0 and v2.0."""
        cve_item = {
            "cve": {
                "metrics": {
                    "cvssMetricV31": [{"cvssData": {"baseScore": 9.0}}],
                    "cvssMetricV30": [{"cvssData": {"baseScore": 8.0}}],
                    "cvssMetricV2": [{"cvssData": {"baseScore": 7.0}}],
                }
            }
        }
        result = extract_cvss_score(cve_item)
        self.assertEqual(result, 9.0)

    def test_extract_cvss_no_metrics(self):
        """Should return None when no metrics available."""
        cve_item = {"cve": {}}
        result = extract_cvss_score(cve_item)
        self.assertIsNone(result)

    def test_extract_cvss_empty_metrics(self):
        """Should return None when metrics dict is empty."""
        cve_item = {"cve": {"metrics": {}}}
        result = extract_cvss_score(cve_item)
        self.assertIsNone(result)


class TestExtractDescription(unittest.TestCase):
    """Tests for extract_description function."""

    def test_extract_english_description(self):
        """Should extract English description."""
        cve_item = {
            "cve": {
                "descriptions": [
                    {"lang": "en", "value": "A critical vulnerability."}
                ]
            }
        }
        result = extract_description(cve_item)
        self.assertEqual(result, "A critical vulnerability.")

    def test_extract_description_multiple_languages(self):
        """Should prefer English when multiple languages available."""
        cve_item = {
            "cve": {
                "descriptions": [
                    {"lang": "es", "value": "Una vulnerabilidad critica."},
                    {"lang": "en", "value": "A critical vulnerability."},
                ]
            }
        }
        result = extract_description(cve_item)
        self.assertEqual(result, "A critical vulnerability.")

    def test_extract_description_no_english(self):
        """Should return placeholder when no English description."""
        cve_item = {
            "cve": {
                "descriptions": [
                    {"lang": "es", "value": "Una vulnerabilidad critica."}
                ]
            }
        }
        result = extract_description(cve_item)
        self.assertEqual(result, "No description available")

    def test_extract_description_empty(self):
        """Should return placeholder when no descriptions."""
        cve_item = {"cve": {"descriptions": []}}
        result = extract_description(cve_item)
        self.assertEqual(result, "No description available")


class TestFilterAndFormatCves(unittest.TestCase):
    """Tests for filter_and_format_cves function."""

    def test_filter_high_severity(self):
        """Should filter CVEs with CVSS >= 7.0."""
        vulnerabilities = [
            {
                "cve": {
                    "id": "CVE-2024-0001",
                    "published": "2024-01-15T10:00:00.000",
                    "descriptions": [{"lang": "en", "value": "High severity vuln"}],
                    "metrics": {
                        "cvssMetricV31": [{"cvssData": {"baseScore": 9.8}}]
                    },
                }
            },
            {
                "cve": {
                    "id": "CVE-2024-0002",
                    "published": "2024-01-15T11:00:00.000",
                    "descriptions": [{"lang": "en", "value": "Low severity vuln"}],
                    "metrics": {
                        "cvssMetricV31": [{"cvssData": {"baseScore": 3.5}}]
                    },
                }
            },
        ]

        result = filter_and_format_cves(vulnerabilities)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["cve_id"], "CVE-2024-0001")
        self.assertEqual(result[0]["cvss_score"], 9.8)

    def test_filter_custom_threshold(self):
        """Should respect custom CVSS threshold."""
        vulnerabilities = [
            {
                "cve": {
                    "id": "CVE-2024-0001",
                    "published": "2024-01-15T10:00:00.000",
                    "descriptions": [{"lang": "en", "value": "Medium vuln"}],
                    "metrics": {
                        "cvssMetricV31": [{"cvssData": {"baseScore": 5.0}}]
                    },
                }
            },
        ]

        result = filter_and_format_cves(vulnerabilities, cvss_threshold=4.0)

        self.assertEqual(len(result), 1)

    def test_filter_excludes_no_cvss(self):
        """Should exclude CVEs without CVSS score."""
        vulnerabilities = [
            {
                "cve": {
                    "id": "CVE-2024-0001",
                    "published": "2024-01-15T10:00:00.000",
                    "descriptions": [{"lang": "en", "value": "No score vuln"}],
                    "metrics": {},
                }
            },
        ]

        result = filter_and_format_cves(vulnerabilities)

        self.assertEqual(len(result), 0)

    def test_format_output_structure(self):
        """Should return correctly formatted dict structure."""
        vulnerabilities = [
            {
                "cve": {
                    "id": "CVE-2024-0001",
                    "published": "2024-01-15T10:00:00.000",
                    "descriptions": [{"lang": "en", "value": "Test vulnerability"}],
                    "metrics": {
                        "cvssMetricV31": [{"cvssData": {"baseScore": 8.0}}]
                    },
                }
            },
        ]

        result = filter_and_format_cves(vulnerabilities)

        self.assertEqual(len(result), 1)
        cve = result[0]
        self.assertIn("cve_id", cve)
        self.assertIn("description", cve)
        self.assertIn("cvss_score", cve)
        self.assertIn("published_date", cve)
        self.assertEqual(cve["cve_id"], "CVE-2024-0001")
        self.assertEqual(cve["description"], "Test vulnerability")
        self.assertEqual(cve["cvss_score"], 8.0)
        self.assertEqual(cve["published_date"], "2024-01-15T10:00:00.000")


class TestGetHighSeverityCves(unittest.TestCase):
    """Tests for get_high_severity_cves function."""

    @patch("agents.cve_monitor.fetch_cves")
    @patch("agents.cve_monitor.get_nvd_api_key")
    def test_integration_with_api_key(self, mock_get_key, mock_fetch):
        """Should use API key when available."""
        mock_get_key.return_value = "test-key"
        mock_fetch.return_value = [
            {
                "cve": {
                    "id": "CVE-2024-0001",
                    "published": "2024-01-15T10:00:00.000",
                    "descriptions": [{"lang": "en", "value": "Test vuln"}],
                    "metrics": {
                        "cvssMetricV31": [{"cvssData": {"baseScore": 9.0}}]
                    },
                }
            }
        ]

        result = get_high_severity_cves()

        mock_fetch.assert_called_once_with(api_key="test-key")
        self.assertEqual(len(result), 1)

    @patch("agents.cve_monitor.fetch_cves")
    @patch("agents.cve_monitor.get_nvd_api_key")
    def test_integration_without_api_key(self, mock_get_key, mock_fetch):
        """Should work without API key."""
        mock_get_key.return_value = None
        mock_fetch.return_value = []

        result = get_high_severity_cves()

        mock_fetch.assert_called_once_with(api_key=None)
        self.assertEqual(result, [])

    @patch("agents.cve_monitor.fetch_cves")
    @patch("agents.cve_monitor.get_nvd_api_key")
    def test_custom_threshold(self, mock_get_key, mock_fetch):
        """Should pass custom CVSS threshold."""
        mock_get_key.return_value = None
        mock_fetch.return_value = [
            {
                "cve": {
                    "id": "CVE-2024-0001",
                    "published": "2024-01-15T10:00:00.000",
                    "descriptions": [{"lang": "en", "value": "Test vuln"}],
                    "metrics": {
                        "cvssMetricV31": [{"cvssData": {"baseScore": 5.0}}]
                    },
                }
            }
        ]

        result = get_high_severity_cves(cvss_threshold=4.0)

        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
