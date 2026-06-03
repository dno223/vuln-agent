# Vulnerability Intelligence Report

**Date:** 2026-06-03  
**Generated:** 2026-06-03T12:41:20Z  

---

## Executive Summary

Our security posture faces significant threats from 73 high-severity vulnerabilities, primarily affecting WordPress themes and medical devices. Critical concerns include PHP remote file inclusion vulnerabilities (CVSS 8.1) enabling code execution, authentication bypass in Collibra Agent (CVSS 8.2), and network vulnerabilities in Dräger patient monitors (CVSS 8.6). Seven new CISA Known Exploited Vulnerabilities were added recently, indicating active threat exploitation. Immediate remediation is required for internet-facing systems and critical infrastructure.

---

## Risk Narrative

The current threat landscape shows attackers actively exploiting known vulnerabilities, evidenced by seven new CISA KEV additions. Medical device vulnerabilities pose patient safety risks and regulatory compliance issues. PHP remote file inclusion flaws in popular WordPress themes create widespread web application compromise opportunities. Authentication bypass vulnerabilities enable unauthorized system access and data exfiltration. The concentration of high-severity vulnerabilities across diverse platforms indicates sophisticated threat actors targeting multiple attack vectors simultaneously, requiring coordinated defensive responses.

---

## Prioritized Action Items

1. Immediately patch or isolate all Dräger patient monitoring systems due to network vulnerabilities that could compromise patient safety.
2. Update all WordPress themes affected by PHP remote file inclusion vulnerabilities within 48 hours to prevent code execution attacks.
3. Apply authentication fixes to all Collibra Agent instances and restrict REST API access to authorized networks only.
4. Prioritize patching of the seven newly added CISA KEV entries across Linux, Android, Oracle WebLogic, and Palo Alto systems.
5. Implement network segmentation and monitoring for all affected systems until patches can be fully deployed and verified.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2019-25719 | 8.6 | 2026-06-02 | Dräger Infinity Acute Care System and Standalone Infinity M540 patient monitors running software versions VG4.1.1, VG4.0 |
| CVE-2025-58707 | 8.1 | 2026-06-02 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2025-58897 | 8.1 | 2026-06-02 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2025-68886 | 8.1 | 2026-06-02 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2025-69369 | 8.1 | 2026-06-02 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2026-10621 | 7.5 | 2026-06-02 | Path traversal in restore handler in Collibra Agent, allows an attacker to write arbitrary files via a crafted ZIP archi |
| CVE-2026-10622 | 8.2 | 2026-06-02 | Improper Authentication in REST API in Collibra Agent, allows a remote unauthenticated attacker to access privileged fun |
| CVE-2026-39552 | 8.1 | 2026-06-02 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2026-39553 | 8.1 | 2026-06-02 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2026-39555 | 8.1 | 2026-06-02 | Deserialization of Untrusted Data vulnerability in Elated-Themes Askka allows Object Injection.

This issue affects Askk |
| CVE-2026-7195 | 8.8 | 2026-06-02 | CWE-20: Improper Input Validation in web services in Progress Sitefinity 14.1.x through 14.3.x, 14.4.x before 14.4.8152, |
| CVE-2026-7198 | 9.8 | 2026-06-02 | CWE-284: Improper Access Control in web services in Progress Sitefinity 15.4.8623 before 15.4.8630 allows a remote unaut |
| CVE-2026-7201 | 8.8 | 2026-06-02 | CWE-639: Authorization Bypass Through User-Controlled Key in web services in Progress Sitefinity 15.2.x before 15.2.8441 |
| CVE-2026-7312 | 10.0 | 2026-06-02 | CWE‑522: Insufficiently Protected Credentials in web services in Progress Sitefinity version from 14.0.7700 to 14.4.8152 |
| CVE-2026-7313 | 8.7 | 2026-06-02 | CWE‑522: Insufficiently Protected Credentials in web services in Progress Sitefinity version from 8.0.5700 to 13.3.7652  |
| CVE-2026-10591 | 8.8 | 2026-06-02 | Insufficient access control restrictions in the file write tool in Amazon Kiro IDE before version 0.11 might allow remot |
| CVE-2026-10629 | 9.1 | 2026-06-02 | SIP signaling stack in Verizon IMS (unspecified version) implements SIP signaling without IPsec integrity protection (mi |
| CVE-2026-40619 | 7.8 | 2026-06-02 | A high security vulnerability affecting Security Center main server installations has been identified. It could allow an |
| CVE-2026-40780 | 7.5 | 2026-06-02 | Authentication Bypass Using an Alternate Path or Channel vulnerability in Liquid Web / StellarWP BookIt allows Password  |
| CVE-2026-42654 | 7.1 | 2026-06-02 | Authentication Bypass Using an Alternate Path or Channel vulnerability in WP Swings Wallet System for WooCommerce allows |
| CVE-2026-45553 | 7.5 | 2026-06-02 | NiceGUI is a Python-based UI framework. Prior to version 3.12.0, ui.restructured_text() renders reStructuredText server- |
| CVE-2026-45678 | 7.5 | 2026-06-02 | OpenTelemetry eBPF Instrumentation provides eBPF instrumentation based on the OpenTelemetry standard. Prior to version 0 |
| CVE-2026-45685 | 7.5 | 2026-06-02 | OpenTelemetry eBPF Instrumentation provides eBPF instrumentation based on the OpenTelemetry standard. From version 0.1.0 |
| CVE-2026-45686 | 7.5 | 2026-06-02 | OpenTelemetry eBPF Instrumentation provides eBPF instrumentation based on the OpenTelemetry standard. From version 0.7.0 |
| CVE-2026-47117 | 9.8 | 2026-06-02 | OpenMed before 1.5.2 contains a remote code execution vulnerability in the PII privacy-filter model loading path. The pr |
| CVE-2026-0611 | 9.8 | 2026-06-02 | Spacelabs Healthcare Sentinel versions 10.5.x and higher and 11.x.x before 11.6.0 contain an unauthenticated remote code |
| CVE-2026-10606 | 7.3 | 2026-06-02 | A vulnerability was determined in DedeCMS 5.7.88. The affected element is the function TrimMsg of the file /plus/feedbac |
| CVE-2026-24221 | 7.8 | 2026-06-02 | NVIDIA NVTabular contains a vulnerability where an attacker could cause improper deserialization of untrusted data. A su |
| CVE-2026-24237 | 7.8 | 2026-06-02 | NVIDIA NVTabular contains a vulnerability where an attacker could cause improper deserialization of untrusted data. A su |
| CVE-2026-40715 | 7.8 | 2026-06-02 | Dell ThinOS 10, versions prior to ThinOS10 2602_10.0765, contain an Improper Access Control vulnerability. A low privile |
| CVE-2019-25722 | 7.6 | 2026-06-02 | Dräger SC Monitoring devices (SC 6002XL, SC 6802XL, SC 7000, SC 8000, SC 9000 XL) contain hard-coded plaintext credentia |
| CVE-2021-4478 | 8.2 | 2026-06-02 | Dräger CC-Vision Basic before 7.5.3 and Dräger CC-Vision E-Cal before 7.2.5.0 contain an out-of-bounds write vulnerabili |
| CVE-2026-10607 | 7.3 | 2026-06-02 | A vulnerability was identified in DedeCMS 5.7.88. The impacted element is the function dede_htmlspecialchars of the file |
| CVE-2026-10608 | 7.3 | 2026-06-02 | A security flaw has been discovered in DedeCMS 5.7.88. This affects the function RemoveXSS of the file /plus/carbuyactio |
| CVE-2026-10617 | 7.3 | 2026-06-02 | A security vulnerability has been detected in nextlevelbuilder GoClaw up to 3.11.3. This affects the function resolveAut |
| CVE-2026-1829 | 8.8 | 2026-06-02 | The Content Visibility for Divi Builder plugin for WordPress is vulnerable to Remote Code Execution in all versions up t |
| CVE-2026-28299 | 8.2 | 2026-06-02 | SolarWinds Web Help Desk is found to be affected by a denial-of-service vulnerability, which when exploited, could cause |
| CVE-2026-33245 | 8.0 | 2026-06-02 | React Router is a router for React. In versions 7.7.0 through 7.13.1, when using React Router's unstable React Server Co |
| CVE-2026-34077 | 7.5 | 2026-06-02 | React Router is a router for React. In versions 7.7.0 through 7.13.1, when using React Router's unstable React Server Co |
| CVE-2026-42211 | 8.1 | 2026-06-02 | React Router is a router for React. In versions 7.0.0 through 7.14.1, when using Framework Mode, a combination of steps  |
| CVE-2026-42342 | 7.5 | 2026-06-02 | React Router is a router for React. In versions 7.0.0 through 7.14.x of react-router and versions 2.10.0 through 2.17.4  |
| CVE-2026-49120 | 8.5 | 2026-06-02 | Medplum before 5.1.14 contains a server-side request forgery vulnerability in the subscription worker that allows authen |
| CVE-2026-5073 | 7.5 | 2026-06-02 | The ARMember Premium plugin for WordPress is vulnerable to SQL Injection via the 'order' parameter of the 'arm_directory |
| CVE-2026-5076 | 9.8 | 2026-06-02 | The ARMember Premium plugin for WordPress is vulnerable to an insecure password reset mechanism in all versions up to, a |
| CVE-2026-8035 | 7.1 | 2026-06-02 | Improper input validation in the NI-PAL kernel driver may allow a local authenticated user to cause a denial of service  |
| CVE-2026-8036 | 7.1 | 2026-06-02 | Improper input validation in NI-PAL may allow a local authenticated user to access arbitrary system memory, potentially  |
| CVE-2026-10619 | 7.3 | 2026-06-02 | A vulnerability was detected in sayan365 student-management-system up to 7f3c9ce7d410332335c2affac93a385485051800. This  |
| CVE-2026-10620 | 7.3 | 2026-06-02 | A flaw has been found in code-projects Student Admission System 1.0. Affected is an unknown function of the file /index. |
| CVE-2026-42849 | 9.3 | 2026-06-02 | authentik is an open-source identity provider. Prior to versions 2025.12.5 and 2026.2.3, due to the implementation of st |
| CVE-2026-47201 | 8.5 | 2026-06-02 | authentik is an open-source identity provider. Prior to versions 2025.12.5, 2026.2.3, and 2026.5.1, authentik's SAML Sou |
| CVE-2026-49143 | 8.8 | 2026-06-02 | BrowserStack Runner through 0.9.5 contains a remote code execution vulnerability in the /_log HTTP handler that allows u |
| CVE-2026-49443 | 8.8 | 2026-06-02 | authentik is an open-source identity provider. Prior to versions 2025.12.6, 2026.2.4, and 2026.5.1, an attacker with the |
| CVE-2026-49448 | 9.8 | 2026-06-02 | authentik is an open-source identity provider. Prior to versions 2025.12.6, 2026.2.4, and 2026.5.1, the Source stage can |
| CVE-2021-4480 | 8.2 | 2026-06-02 | Dräger Protector Software prior to version 6.4.2 contains a local privilege escalation vulnerability due to insecure fil |
| CVE-2021-4481 | 8.2 | 2026-06-02 | Dräger Protector Software prior to version 6.4.2 contains a local privilege escalation vulnerability due to insecure fil |
| CVE-2022-4992 | 8.6 | 2026-06-02 | Dräger Infinity Acute Care System and Standalone Infinity M540 patient monitors versions VG4.1.1, VG4.0.3, and lower (wi |
| CVE-2024-14036 | 7.5 | 2026-06-02 | Dräger Core 1.0.5 and Dräger M540 Converter Service 1.0.9 contain a denial of service vulnerability that allows network- |
| CVE-2026-31942 | 7.1 | 2026-06-02 | LibreChat is an enhanced ChatGPT clone that supports multiple AI providers. In versions up to and including 0.7.6, an In |
| CVE-2026-32625 | 9.6 | 2026-06-02 | LibreChat is an enhanced ChatGPT clone that supports multiple AI providers. In versions up to and including 0.8.3, the M |
| CVE-2026-35482 | 8.0 | 2026-06-02 | alf.io is an open source ticket reservation system for conferences, trade shows, workshops, and meetups. Prior to versio |
| CVE-2026-10694 | 7.3 | 2026-06-03 | A vulnerability was detected in SourceCodester Online Food Ordering System 2.0. Affected by this issue is the function i |
| CVE-2026-10704 | 7.3 | 2026-06-03 | A vulnerability was detected in SourceCodester Pizzafy E-Commerce System 1.0. Affected by this vulnerability is the func |
| CVE-2026-50031 | 7.5 | 2026-06-03 | ipmi-oem in FreeIPMI before 1.6.18 has exploitable buffer overflows on response messages. The Intelligent Platform Manag |
| CVE-2025-15654 | 7.1 | 2026-06-03 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Fox-themes Prague  |
| CVE-2026-4035 | 9.1 | 2026-06-03 | A vulnerability in mlflow/mlflow versions prior to 3.11.0 allows for the resolution of environment variables in AI Gatew |
| CVE-2025-14771 | 9.9 | 2026-06-03 | Files or directories accessible to external parties vulnerability in ABB T-MAC Plus.

This issue affects T-MAC Plus: 4.0 |
| CVE-2025-14772 | 8.8 | 2026-06-03 | Authorization bypass through User-Controlled key vulnerability in ABB T-MAC Plus.

This issue affects T-MAC Plus: 4.0-24 |
| CVE-2025-14773 | 8.0 | 2026-06-03 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in ABB T-MAC Plus.

T |
| CVE-2025-14774 | 7.4 | 2026-06-03 | Incorrect Authorization vulnerability in ABB T-MAC Plus.

This issue affects T-MAC Plus: 4.0-24. |
| CVE-2025-15655 | 7.6 | 2026-06-03 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Mojoomla School Ma |
| CVE-2025-15656 | 8.8 | 2026-06-03 | Incorrect Privilege Assignment vulnerability in Mojoomla School Management allows Privilege Escalation.

This issue affe |
| CVE-2026-41032 | 7.5 | 2026-06-03 | It is possible for an unauthenticated adjacent attacker to download log files of the controller, which may disclose some |
| CVE-2026-47065 | 9.8 | 2026-06-03 | ZDRES-232: resolveProxyClass Not Overridden - acceptMatchers Filter Bypass via java.lang.reflect.Proxy


Assessment: Ful |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2022-0492 | Linux / Kernel | 2026-06-02 | 2026-06-05 | Unknown |
| CVE-2025-48595 | Android / Framework | 2026-06-02 | 2026-06-05 | Unknown |
| CVE-2024-21182 | Oracle / WebLogic Server | 2026-06-01 | 2026-06-04 | Unknown |
| CVE-2026-0257 | Palo Alto Networks / PAN-OS | 2026-05-29 | 2026-06-01 | Unknown |
| CVE-2026-48027 | Nx / Nx Console | 2026-05-27 | 2026-06-10 | Known |
| CVE-2026-45321 | TanStack / TanStack | 2026-05-27 | 2026-06-10 | Known |
| CVE-2026-8398 | Daemon / Daemon Tools Lite | 2026-05-27 | 2026-05-30 | Unknown |

---

*Total entries in CISA KEV catalog: 1610*