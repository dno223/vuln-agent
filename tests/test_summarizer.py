"""
Unit tests for the Summarizer Agent.

Uses unittest.mock to avoid hitting the live Claude API.
"""

import json
import unittest
from unittest.mock import MagicMock, call, patch

import anthropic

from agents.summarizer import (
    MODEL,
    format_vulnerability_data,
    generate_summary,
    parse_summary_response,
)

# ---------------------------------------------------------------------------
# Shared fixtures
# ---------------------------------------------------------------------------

SAMPLE_CVE = {
    "cve_id": "CVE-2021-44228",
    "description": "Apache Log4j2 RCE via JNDI lookup in log messages.",
    "cvss_score": 10.0,
    "published_date": "2021-12-10T00:00:00.000",
}

SAMPLE_KEV = {
    "cveID": "CVE-2024-21762",
    "vendorProject": "Fortinet",
    "product": "FortiOS",
    "vulnerabilityName": "Fortinet FortiOS Out-of-Bound Write",
    "dateAdded": "2024-02-09",
    "dueDate": "2024-02-16",
    "knownRansomwareCampaignUse": "Known",
}

SAMPLE_HIT = {
    "cveID": "CVE-2021-44228",
    "vendorProject": "Apache",
    "product": "Log4j2",
    "vulnerabilityName": "Apache Log4j2 RCE Vulnerability",
    "dateAdded": "2021-12-10",
    "dueDate": "2021-12-24",
}

SAMPLE_INPUT = {
    "high_severity_cves": [SAMPLE_CVE],
    "new_kev_entries": [SAMPLE_KEV],
    "monitored_hits": [SAMPLE_HIT],
}

VALID_CLAUDE_RESPONSE = {
    "executive_summary": (
        "The organization faces critical exposure to several actively exploited "
        "vulnerabilities. Immediate action is required on Log4Shell."
    ),
    "action_items": [
        "Patch Apache Log4j2 across all production systems immediately.",
        "Update Fortinet FortiOS to the latest patched release.",
        "Audit all internet-facing Exchange servers for compromise indicators.",
        "Enable WAF rules blocking JNDI exploit patterns.",
        "Conduct emergency vulnerability scan across all production hosts.",
    ],
    "risk_narrative": (
        "The current threat landscape is severe. Multiple critical vulnerabilities "
        "are actively being exploited in the wild by ransomware actors."
    ),
}


def _make_mock_response(text: str) -> MagicMock:
    """Build a mock anthropic Message containing a single text block."""
    block = MagicMock()
    block.type = "text"
    block.text = text

    response = MagicMock()
    response.content = [block]
    return response


# ---------------------------------------------------------------------------
# format_vulnerability_data
# ---------------------------------------------------------------------------

class TestFormatVulnerabilityData(unittest.TestCase):
    """Tests for format_vulnerability_data."""

    def test_includes_cve_id(self):
        result = format_vulnerability_data(SAMPLE_INPUT)
        self.assertIn("CVE-2021-44228", result)

    def test_includes_cvss_score(self):
        result = format_vulnerability_data(SAMPLE_INPUT)
        self.assertIn("10.0", result)

    def test_includes_kev_vendor_and_product(self):
        result = format_vulnerability_data(SAMPLE_INPUT)
        self.assertIn("Fortinet", result)
        self.assertIn("FortiOS", result)

    def test_includes_monitored_hit_name(self):
        result = format_vulnerability_data(SAMPLE_INPUT)
        self.assertIn("Apache Log4j2 RCE Vulnerability", result)

    def test_no_monitored_hits_shows_none_placeholder(self):
        data = {**SAMPLE_INPUT, "monitored_hits": []}
        result = format_vulnerability_data(data)
        self.assertIn("(none)", result)

    def test_empty_dict_returns_string(self):
        result = format_vulnerability_data({})
        self.assertIsInstance(result, str)

    def test_description_capped_at_200_chars(self):
        long_desc = "X" * 500
        data = {
            "high_severity_cves": [{"cve_id": "CVE-2099-1", "cvss_score": 9.0, "description": long_desc}],
            "new_kev_entries": [],
            "monitored_hits": [],
        }
        result = format_vulnerability_data(data)
        self.assertNotIn("X" * 300, result)

    def test_shows_count_of_high_severity_cves(self):
        result = format_vulnerability_data(SAMPLE_INPUT)
        self.assertIn("1 total", result)

    def test_shows_count_of_new_kev_entries(self):
        result = format_vulnerability_data(SAMPLE_INPUT)
        self.assertIn("1 added in last 7 days", result)

    def test_shows_count_of_monitored_hits(self):
        result = format_vulnerability_data(SAMPLE_INPUT)
        self.assertIn("1 matches", result)


# ---------------------------------------------------------------------------
# parse_summary_response
# ---------------------------------------------------------------------------

class TestParseSummaryResponse(unittest.TestCase):
    """Tests for parse_summary_response."""

    def test_valid_json_returns_all_keys(self):
        result = parse_summary_response(json.dumps(VALID_CLAUDE_RESPONSE))
        self.assertIn("executive_summary", result)
        self.assertIn("action_items", result)
        self.assertIn("risk_narrative", result)

    def test_executive_summary_is_string(self):
        result = parse_summary_response(json.dumps(VALID_CLAUDE_RESPONSE))
        self.assertIsInstance(result["executive_summary"], str)

    def test_action_items_is_list(self):
        result = parse_summary_response(json.dumps(VALID_CLAUDE_RESPONSE))
        self.assertIsInstance(result["action_items"], list)

    def test_action_items_content_preserved(self):
        result = parse_summary_response(json.dumps(VALID_CLAUDE_RESPONSE))
        self.assertEqual(len(result["action_items"]), 5)
        self.assertEqual(result["action_items"][0], VALID_CLAUDE_RESPONSE["action_items"][0])

    def test_risk_narrative_is_string(self):
        result = parse_summary_response(json.dumps(VALID_CLAUDE_RESPONSE))
        self.assertIsInstance(result["risk_narrative"], str)

    def test_raises_on_non_json_input(self):
        with self.assertRaises(ValueError):
            parse_summary_response("This is not JSON at all.")

    def test_raises_on_json_missing_executive_summary(self):
        incomplete = {"action_items": [], "risk_narrative": "..."}
        with self.assertRaises(ValueError):
            parse_summary_response(json.dumps(incomplete))

    def test_raises_on_json_missing_action_items(self):
        incomplete = {"executive_summary": "...", "risk_narrative": "..."}
        with self.assertRaises(ValueError):
            parse_summary_response(json.dumps(incomplete))

    def test_raises_on_json_missing_risk_narrative(self):
        incomplete = {"executive_summary": "...", "action_items": []}
        with self.assertRaises(ValueError):
            parse_summary_response(json.dumps(incomplete))

    def test_leading_and_trailing_whitespace_handled(self):
        text = "   \n" + json.dumps(VALID_CLAUDE_RESPONSE) + "\n   "
        result = parse_summary_response(text)
        self.assertIsNotNone(result)

    def test_empty_json_object_raises(self):
        with self.assertRaises(ValueError):
            parse_summary_response("{}")


# ---------------------------------------------------------------------------
# generate_summary
# ---------------------------------------------------------------------------

class TestGenerateSummary(unittest.TestCase):
    """Tests for generate_summary — Claude API is fully mocked."""

    @patch("agents.summarizer.anthropic.Anthropic")
    def test_returns_dict_with_required_keys(self, mock_anthropic_cls):
        mock_client = MagicMock()
        mock_anthropic_cls.return_value = mock_client
        mock_client.messages.create.return_value = _make_mock_response(
            json.dumps(VALID_CLAUDE_RESPONSE)
        )

        result = generate_summary(SAMPLE_INPUT)

        self.assertIn("executive_summary", result)
        self.assertIn("action_items", result)
        self.assertIn("risk_narrative", result)

    @patch("agents.summarizer.anthropic.Anthropic")
    def test_uses_correct_model(self, mock_anthropic_cls):
        mock_client = MagicMock()
        mock_anthropic_cls.return_value = mock_client
        mock_client.messages.create.return_value = _make_mock_response(
            json.dumps(VALID_CLAUDE_RESPONSE)
        )

        generate_summary(SAMPLE_INPUT)

        call_kwargs = mock_client.messages.create.call_args.kwargs
        self.assertEqual(call_kwargs["model"], MODEL)

    @patch("agents.summarizer.anthropic.Anthropic")
    def test_calls_api_exactly_once(self, mock_anthropic_cls):
        mock_client = MagicMock()
        mock_anthropic_cls.return_value = mock_client
        mock_client.messages.create.return_value = _make_mock_response(
            json.dumps(VALID_CLAUDE_RESPONSE)
        )

        generate_summary(SAMPLE_INPUT)

        mock_client.messages.create.assert_called_once()

    @patch("agents.summarizer.anthropic.Anthropic")
    def test_includes_system_prompt(self, mock_anthropic_cls):
        mock_client = MagicMock()
        mock_anthropic_cls.return_value = mock_client
        mock_client.messages.create.return_value = _make_mock_response(
            json.dumps(VALID_CLAUDE_RESPONSE)
        )

        generate_summary(SAMPLE_INPUT)

        call_kwargs = mock_client.messages.create.call_args.kwargs
        self.assertIn("system", call_kwargs)
        self.assertGreater(len(call_kwargs["system"]), 0)

    @patch("agents.summarizer.anthropic.Anthropic")
    def test_sends_user_message_with_vulnerability_data(self, mock_anthropic_cls):
        mock_client = MagicMock()
        mock_anthropic_cls.return_value = mock_client
        mock_client.messages.create.return_value = _make_mock_response(
            json.dumps(VALID_CLAUDE_RESPONSE)
        )

        generate_summary(SAMPLE_INPUT)

        call_kwargs = mock_client.messages.create.call_args.kwargs
        messages = call_kwargs["messages"]
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]["role"], "user")
        self.assertIn("CVE-2021-44228", messages[0]["content"])

    @patch.dict("os.environ", {"ANTHROPIC_API_KEY": "test-key-123"})
    @patch("agents.summarizer.anthropic.Anthropic")
    def test_passes_api_key_from_env(self, mock_anthropic_cls):
        mock_client = MagicMock()
        mock_anthropic_cls.return_value = mock_client
        mock_client.messages.create.return_value = _make_mock_response(
            json.dumps(VALID_CLAUDE_RESPONSE)
        )

        generate_summary(SAMPLE_INPUT)

        mock_anthropic_cls.assert_called_once_with(api_key="test-key-123")

    @patch("agents.summarizer.anthropic.Anthropic")
    def test_propagates_api_error(self, mock_anthropic_cls):
        mock_client = MagicMock()
        mock_anthropic_cls.return_value = mock_client
        mock_client.messages.create.side_effect = anthropic.APIConnectionError(
            request=MagicMock()
        )

        with self.assertRaises(anthropic.APIConnectionError):
            generate_summary(SAMPLE_INPUT)

    @patch("agents.summarizer.anthropic.Anthropic")
    def test_raises_value_error_on_invalid_json_response(self, mock_anthropic_cls):
        mock_client = MagicMock()
        mock_anthropic_cls.return_value = mock_client
        mock_client.messages.create.return_value = _make_mock_response(
            "This is not JSON."
        )

        with self.assertRaises(ValueError):
            generate_summary(SAMPLE_INPUT)

    @patch("agents.summarizer.anthropic.Anthropic")
    def test_empty_input_still_calls_api(self, mock_anthropic_cls):
        mock_client = MagicMock()
        mock_anthropic_cls.return_value = mock_client
        mock_client.messages.create.return_value = _make_mock_response(
            json.dumps(VALID_CLAUDE_RESPONSE)
        )

        result = generate_summary({})

        mock_client.messages.create.assert_called_once()
        self.assertIn("executive_summary", result)

    @patch("agents.summarizer.anthropic.Anthropic")
    def test_action_items_returned_as_list(self, mock_anthropic_cls):
        mock_client = MagicMock()
        mock_anthropic_cls.return_value = mock_client
        mock_client.messages.create.return_value = _make_mock_response(
            json.dumps(VALID_CLAUDE_RESPONSE)
        )

        result = generate_summary(SAMPLE_INPUT)

        self.assertIsInstance(result["action_items"], list)

    @patch("agents.summarizer.anthropic.Anthropic")
    def test_non_text_content_blocks_ignored(self, mock_anthropic_cls):
        """Should handle responses where the first block is not a text block."""
        tool_block = MagicMock()
        tool_block.type = "tool_use"

        text_block = MagicMock()
        text_block.type = "text"
        text_block.text = json.dumps(VALID_CLAUDE_RESPONSE)

        response = MagicMock()
        response.content = [tool_block, text_block]

        mock_client = MagicMock()
        mock_anthropic_cls.return_value = mock_client
        mock_client.messages.create.return_value = response

        result = generate_summary(SAMPLE_INPUT)

        self.assertIn("executive_summary", result)


if __name__ == "__main__":
    unittest.main()
