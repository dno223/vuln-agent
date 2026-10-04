# Vulnerability Intelligence Report

**Date:** 2026-10-04  
**Generated:** 2026-10-04T13:42:06Z  

---

## Executive Summary

Our environment faces significant exposure across 18 high-severity vulnerabilities, including two CVSS 10.0 critical flaws in Ahsay AhsayCBS and InternLM MindSearch enabling remote code execution with no authentication barriers. Seven new CISA Known Exploited Vulnerabilities were added this week spanning Fortinet, Cisco, Apple, and Zammad products, signaling active threat actor exploitation in the wild. Privilege escalation risks in Ultimate Member and LaraDashboard, combined with an unauthenticated class instantiation flaw in OpenAM, further expand the attack surface. Immediate patching and compensating controls are required to reduce organizational risk.

---

## Risk Narrative

The current threat landscape presents a compounding risk of remote code execution, privilege escalation, and active exploitation. Two CVSS 10.0 vulnerabilities represent worst-case scenarios allowing complete system compromise. The addition of seven KEV entries confirms adversaries are actively weaponizing similar flaws across enterprise technologies including Cisco, Fortinet, and Apple. Privilege escalation paths in web platforms could enable attackers to move laterally and achieve persistent access. XSS vulnerabilities, while lower severity, facilitate credential theft and session hijacking. Collectively, these findings indicate elevated risk of data breach, operational disruption, and potential regulatory liability if remediation is not prioritized immediately.

---

## Prioritized Action Items

1. Immediately patch or isolate Ahsay AhsayCBS (CVE-2026-105134, CVSS 10.0) and InternLM MindSearch (CVE-2026-105135, CVSS 10.0) due to critical remote code execution exposure.
2. Apply vendor patches for all seven newly added CISA KEV entries affecting Fortinet FortiMail, Cisco Catalyst SD-WAN Manager, Apple products, and Zammad within 24-48 hours per federal remediation guidance.
3. Remediate the unauthenticated arbitrary class instantiation vulnerability in OpenAM (CVE-2026-105115, CVSS 8.6) by upgrading to version 16.1.3 or later immediately.
4. Address privilege escalation vulnerabilities in Ultimate Member (CVE-2026-96451) and WCMS remote code execution (CVE-2026-105123), both CVSS 8.8, by patching or disabling affected plugins.
5. Audit and patch remaining high-severity vulnerabilities including LaraDashboard privilege escalation and XSS flaws to eliminate residual attack surface within the next two weeks.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-105115 | 8.6 | 2026-10-03 | OpenAM before 16.1.3 contains an unauthenticated arbitrary class instantiation vulnerability in the legacy JAX-RPC SOAP  |
| CVE-2026-103065 | 8.2 | 2026-10-03 | Improper Validation of Specified Quantity in Input vulnerability in Themeum Kirki kirki allows Accessing Functionality N |
| CVE-2026-103342 | 7.1 | 2026-10-03 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Unlimited Elements |
| CVE-2026-96451 | 8.8 | 2026-10-03 | Authorization Bypass Through User-Controlled Key vulnerability in Ultimate Member Ultimate Member ultimate-member allows |
| CVE-2026-105123 | 8.8 | 2026-10-04 | W (vincent-peugnet/wcms) through 3.18.0 contains a remote code execution vulnerability that allows authenticated editors |
| CVE-2026-105126 | 7.2 | 2026-10-04 | LaraDashboard before 1.4.8 contains an improper privilege management vulnerability that allows authenticated Admin users |
| CVE-2026-105133 | 7.3 | 2026-10-04 | A vulnerability was detected in Ahsay AhsayCBS up to 10.3.2. This affects the function checkSysPwd of the file com/ahsay |
| CVE-2026-105134 | 10.0 | 2026-10-04 | A flaw has been found in Ahsay AhsayCBS up to 10.3.2. This vulnerability affects unknown code of the file /rps/api/json/ |
| CVE-2026-105135 | 10.0 | 2026-10-04 | A vulnerability has been found in InternLM MindSearch 0.1.0. This issue affects the function ExecutionAction.run of the  |
| CVE-2026-103062 | 7.1 | 2026-10-04 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Cozmoslabs Transla |
| CVE-2026-103344 | 7.1 | 2026-10-04 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Unlimited Elements |
| CVE-2026-103354 | 7.1 | 2026-10-04 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Liquid Web / Stell |
| CVE-2026-103355 | 9.3 | 2026-10-04 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Unlimited Elements |
| CVE-2026-97276 | 7.1 | 2026-10-04 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in VeronaLabs WP Stat |
| CVE-2026-97307 | 7.5 | 2026-10-04 | Insertion of Sensitive Information Into Sent Data vulnerability in StylemixThemes Cost Calculator Builder cost-calculato |
| CVE-2026-105147 | 7.3 | 2026-10-04 | A vulnerability was determined in SciPhi-AI R2R up to 3.6.6. This affects an unknown part of the component JWT Secret Ha |
| CVE-2026-105148 | 7.3 | 2026-10-04 | A vulnerability was identified in SciPhi-AI R2R up to 3.6.6. This vulnerability affects unknown code of the file py/shar |
| CVE-2026-105149 | 7.3 | 2026-10-04 | A security flaw has been discovered in mooSocial up to 3.2.4. This issue affects some unknown processing of the file /st |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-102490 | Zammad GmbH / Zammad | 2026-10-02 | 2026-10-05 | Unknown |
| CVE-2026-102489 | Zammad GmbH / Zammad | 2026-10-02 | 2026-10-05 | Unknown |
| CVE-2026-104286 | Fortinet / FortiMail | 2026-10-01 | 2026-10-04 | Unknown |
| CVE-2026-76504 | Cisco / Catalyst SD-WAN Manager | 2026-09-30 | 2026-10-03 | Unknown |
| CVE-2026-86950 | Apple / Multiple Products | 2026-09-29 | 2026-10-02 | Unknown |
| CVE-2026-88772 | Citrix / NetScaler | 2026-09-27 | 2026-09-30 | Unknown |
| CVE-2026-88771 | Citrix / NetScaler | 2026-09-27 | 2026-09-30 | Unknown |

---

*Total entries in CISA KEV catalog: 1733*