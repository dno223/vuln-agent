"""Tests for agents/email_alert.py — all SMTP calls are mocked."""

import os
import smtplib
from unittest.mock import MagicMock, patch

import pytest

from agents.email_alert import (
    _build_subject,
    _compute_avg_cvss,
    _compute_risk_level,
    _kev_due_this_week,
    build_email_html,
    send_alert,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SAMPLE_RESULTS = {
    "run_date": "2026-05-30",
    "run_timestamp": "2026-05-30T08:00:00Z",
    "high_severity_cves": [
        {
            "cve_id": "CVE-2021-44228",
            "description": "Apache Log4j2 RCE via JNDI lookup.",
            "cvss_score": 10.0,
            "published_date": "2021-12-10T00:00:00.000",
        },
        {
            "cve_id": "CVE-2023-44487",
            "description": "HTTP/2 Rapid Reset DoS.",
            "cvss_score": 7.5,
            "published_date": "2023-10-10T00:00:00.000",
        },
    ],
    "new_kev_entries": [
        {
            "cveID": "CVE-2024-21762",
            "vendorProject": "Fortinet",
            "product": "FortiOS",
            "vulnerabilityName": "Fortinet FortiOS Out-of-Bound Write",
            "dateAdded": "2024-02-09",
            "dueDate": "2026-06-01",
            "knownRansomwareCampaignUse": "Known",
        },
    ],
    "monitored_hits": [],
    "executive_summary": "Three critical vulns identified.",
    "action_items": [
        "Patch Log4j2 immediately.",
        "Review Exchange servers.",
        "Scan internet-facing assets.",
        "Update FortiOS firmware.",
        "Brief incident response team.",
    ],
    "risk_narrative": "Ransomware operators are exploiting these CVEs.",
    "pipeline_errors": [],
    "total_kev_count": 1200,
}

ENV_VARS = {
    "EMAIL_SENDER": "sender@example.com",
    "EMAIL_PASSWORD": "app-password-123",
    "EMAIL_RECIPIENTS": "alice@example.com,bob@example.com",
}


# ---------------------------------------------------------------------------
# Helper unit tests
# ---------------------------------------------------------------------------

class TestComputeRiskLevel:
    def test_critical_on_max_cvss_gte_9(self):
        results = {"high_severity_cves": [{"cvss_score": 9.5}], "monitored_hits": [], "new_kev_entries": []}
        assert _compute_risk_level(results) == "Critical"

    def test_critical_on_monitored_hits(self):
        results = {"high_severity_cves": [{"cvss_score": 7.5}], "monitored_hits": [{"cveID": "CVE-X"}], "new_kev_entries": []}
        assert _compute_risk_level(results) == "Critical"

    def test_high_on_cvss_gte_7(self):
        results = {"high_severity_cves": [{"cvss_score": 8.0}], "monitored_hits": [], "new_kev_entries": []}
        assert _compute_risk_level(results) == "High"

    def test_high_on_kev_entries(self):
        results = {"high_severity_cves": [], "monitored_hits": [], "new_kev_entries": [{"cveID": "CVE-Y"}]}
        assert _compute_risk_level(results) == "High"

    def test_medium_when_no_threats(self):
        results = {"high_severity_cves": [], "monitored_hits": [], "new_kev_entries": []}
        assert _compute_risk_level(results) == "Medium"


class TestComputeAvgCvss:
    def test_average_of_two_scores(self):
        cves = [{"cvss_score": 10.0}, {"cvss_score": 7.0}]
        assert _compute_avg_cvss(cves) == 8.5

    def test_empty_list_returns_zero(self):
        assert _compute_avg_cvss([]) == 0.0

    def test_skips_entries_without_score(self):
        cves = [{"cvss_score": 9.0}, {"description": "no score"}]
        assert _compute_avg_cvss(cves) == 9.0


class TestKevDueThisWeek:
    def test_counts_entry_due_within_7_days(self):
        entries = [{"dueDate": "2026-06-04"}]
        assert _kev_due_this_week(entries, "2026-05-30") == 1

    def test_excludes_entry_due_after_7_days(self):
        entries = [{"dueDate": "2026-06-10"}]
        assert _kev_due_this_week(entries, "2026-05-30") == 0

    def test_excludes_past_due(self):
        entries = [{"dueDate": "2026-05-01"}]
        assert _kev_due_this_week(entries, "2026-05-30") == 0

    def test_invalid_date_string_skipped(self):
        entries = [{"dueDate": "not-a-date"}]
        assert _kev_due_this_week(entries, "2026-05-30") == 0


class TestBuildSubject:
    def test_subject_contains_date_and_risk(self):
        subject = _build_subject(SAMPLE_RESULTS)
        assert "2026-05-30" in subject
        assert "Critical" in subject

    def test_subject_contains_counts(self):
        subject = _build_subject(SAMPLE_RESULTS)
        assert "2 CVEs" in subject
        assert "1 KEV hits" in subject


# ---------------------------------------------------------------------------
# HTML builder tests
# ---------------------------------------------------------------------------

class TestBuildEmailHtml:
    def test_contains_run_date(self):
        html = build_email_html(SAMPLE_RESULTS)
        assert "2026-05-30" in html

    def test_contains_risk_level(self):
        html = build_email_html(SAMPLE_RESULTS)
        assert "Critical" in html

    def test_contains_executive_summary(self):
        html = build_email_html(SAMPLE_RESULTS)
        assert "Three critical vulns identified." in html

    def test_contains_risk_narrative(self):
        html = build_email_html(SAMPLE_RESULTS)
        assert "Ransomware operators" in html

    def test_contains_action_items(self):
        html = build_email_html(SAMPLE_RESULTS)
        assert "Patch Log4j2 immediately." in html

    def test_contains_kev_entry(self):
        html = build_email_html(SAMPLE_RESULTS)
        assert "CVE-2024-21762" in html
        assert "Fortinet" in html

    def test_ransomware_known_row_highlighted_red(self):
        html = build_email_html(SAMPLE_RESULTS)
        # Known ransomware rows get a red background (#fef2f2)
        assert "#fef2f2" in html

    def test_contains_cve_entry(self):
        html = build_email_html(SAMPLE_RESULTS)
        assert "CVE-2021-44228" in html

    def test_top_10_cves_sorted_by_cvss(self):
        # The higher-score CVE (10.0) should appear before the lower one (7.5)
        html = build_email_html(SAMPLE_RESULTS)
        pos_log4j = html.find("CVE-2021-44228")
        pos_http2 = html.find("CVE-2023-44487")
        # Both should be present
        assert pos_log4j != -1
        assert pos_http2 != -1
        # Higher CVSS first in the CVE table section (which comes after KEV)
        cve_table_start = html.find("Top 10 CVEs by CVSS Score")
        assert html.find("CVE-2021-44228", cve_table_start) < html.find("CVE-2023-44487", cve_table_start)

    def test_footer_contains_generator_attribution(self):
        html = build_email_html(SAMPLE_RESULTS)
        assert "Vuln Intelligence Agent" in html

    def test_empty_results_does_not_raise(self):
        minimal = {
            "run_date": "2026-05-30",
            "run_timestamp": "2026-05-30T08:00:00Z",
            "high_severity_cves": [],
            "new_kev_entries": [],
            "monitored_hits": [],
            "executive_summary": "",
            "action_items": [],
            "risk_narrative": "",
            "pipeline_errors": [],
        }
        html = build_email_html(minimal)
        assert "No high-severity CVEs found." in html
        assert "No new KEV entries found." in html
        assert "No action items available." in html

    def test_description_truncated_at_160_chars(self):
        long_desc = "A" * 200
        data = dict(SAMPLE_RESULTS)
        data["high_severity_cves"] = [
            {"cve_id": "CVE-2099-0001", "cvss_score": 9.0, "description": long_desc, "published_date": ""}
        ]
        html = build_email_html(data)
        assert "A" * 160 in html
        assert "A" * 161 not in html


# ---------------------------------------------------------------------------
# send_alert tests
# ---------------------------------------------------------------------------

class TestSendAlert:
    def _make_smtp_mock(self):
        smtp_instance = MagicMock()
        smtp_cm = MagicMock()
        smtp_cm.__enter__ = MagicMock(return_value=smtp_instance)
        smtp_cm.__exit__ = MagicMock(return_value=False)
        return smtp_cm, smtp_instance

    @patch.dict(os.environ, ENV_VARS, clear=False)
    @patch("agents.email_alert.smtplib.SMTP")
    def test_sends_email_when_configured(self, mock_smtp_cls):
        smtp_cm, smtp_instance = self._make_smtp_mock()
        mock_smtp_cls.return_value = smtp_cm

        result = send_alert(SAMPLE_RESULTS)

        assert result is True
        mock_smtp_cls.assert_called_once_with("smtp.gmail.com", 587)
        smtp_instance.starttls.assert_called_once()
        smtp_instance.login.assert_called_once_with("sender@example.com", "app-password-123")
        smtp_instance.sendmail.assert_called_once()

    @patch.dict(os.environ, ENV_VARS, clear=False)
    @patch("agents.email_alert.smtplib.SMTP")
    def test_sends_to_all_recipients(self, mock_smtp_cls):
        smtp_cm, smtp_instance = self._make_smtp_mock()
        mock_smtp_cls.return_value = smtp_cm

        send_alert(SAMPLE_RESULTS)

        _, call_args, _ = smtp_instance.sendmail.mock_calls[0]
        recipients_arg = call_args[1]
        assert "alice@example.com" in recipients_arg
        assert "bob@example.com" in recipients_arg

    @patch.dict(os.environ, {**ENV_VARS, "EMAIL_SENDER": ""}, clear=False)
    @patch("agents.email_alert.smtplib.SMTP")
    def test_skips_when_no_sender(self, mock_smtp_cls):
        result = send_alert(SAMPLE_RESULTS)
        assert result is False
        mock_smtp_cls.assert_not_called()

    @patch.dict(os.environ, {**ENV_VARS, "EMAIL_PASSWORD": ""}, clear=False)
    @patch("agents.email_alert.smtplib.SMTP")
    def test_skips_when_no_password(self, mock_smtp_cls):
        result = send_alert(SAMPLE_RESULTS)
        assert result is False
        mock_smtp_cls.assert_not_called()

    @patch.dict(os.environ, {**ENV_VARS, "EMAIL_RECIPIENTS": ""}, clear=False)
    @patch("agents.email_alert.smtplib.SMTP")
    def test_skips_when_no_recipients(self, mock_smtp_cls):
        result = send_alert(SAMPLE_RESULTS)
        assert result is False
        mock_smtp_cls.assert_not_called()

    @patch.dict(os.environ, {**ENV_VARS, "EMAIL_RECIPIENTS": "  ,  ,  "}, clear=False)
    @patch("agents.email_alert.smtplib.SMTP")
    def test_skips_when_recipients_all_whitespace(self, mock_smtp_cls):
        result = send_alert(SAMPLE_RESULTS)
        assert result is False
        mock_smtp_cls.assert_not_called()

    @patch.dict(os.environ, ENV_VARS, clear=False)
    @patch("agents.email_alert.smtplib.SMTP")
    def test_returns_false_on_auth_error(self, mock_smtp_cls):
        smtp_cm, smtp_instance = self._make_smtp_mock()
        smtp_instance.login.side_effect = smtplib.SMTPAuthenticationError(535, b"Bad credentials")
        mock_smtp_cls.return_value = smtp_cm

        result = send_alert(SAMPLE_RESULTS)
        assert result is False

    @patch.dict(os.environ, ENV_VARS, clear=False)
    @patch("agents.email_alert.smtplib.SMTP")
    def test_returns_false_on_smtp_exception(self, mock_smtp_cls):
        smtp_cm, smtp_instance = self._make_smtp_mock()
        smtp_instance.sendmail.side_effect = smtplib.SMTPException("send failed")
        mock_smtp_cls.return_value = smtp_cm

        result = send_alert(SAMPLE_RESULTS)
        assert result is False

    @patch.dict(os.environ, ENV_VARS, clear=False)
    @patch("agents.email_alert.smtplib.SMTP")
    def test_returns_false_on_network_error(self, mock_smtp_cls):
        mock_smtp_cls.side_effect = OSError("Connection refused")

        result = send_alert(SAMPLE_RESULTS)
        assert result is False

    @patch.dict(os.environ, ENV_VARS, clear=False)
    @patch("agents.email_alert.smtplib.SMTP")
    def test_html_report_path_arg_is_accepted(self, mock_smtp_cls):
        """html_report_path is optional; passing it should not raise."""
        smtp_cm, smtp_instance = self._make_smtp_mock()
        mock_smtp_cls.return_value = smtp_cm

        result = send_alert(SAMPLE_RESULTS, html_report_path="/tmp/report.html")
        assert result is True

    @patch.dict(os.environ, ENV_VARS, clear=False)
    @patch("agents.email_alert.smtplib.SMTP")
    def test_subject_line_in_message(self, mock_smtp_cls):
        import email as email_lib
        from email.header import decode_header as dh

        smtp_cm, smtp_instance = self._make_smtp_mock()
        mock_smtp_cls.return_value = smtp_cm

        send_alert(SAMPLE_RESULTS)

        raw_message = smtp_instance.sendmail.call_args[0][2]
        parsed = email_lib.message_from_string(raw_message)
        parts = dh(parsed.get("Subject", ""))
        subject = "".join(
            p.decode(enc or "utf-8") if isinstance(p, bytes) else p
            for p, enc in parts
        )
        assert "Vuln Intel Report" in subject
        assert "2026-05-30" in subject
