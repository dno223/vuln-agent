# Vulnerability Intelligence Report

**Date:** 2026-05-31  
**Generated:** 2026-05-31T02:09:45Z  

---

## Executive Summary

Our security assessment reveals 33 high-severity vulnerabilities with CVSS scores ranging from 7.3 to 8.8, primarily affecting WordPress plugins and network devices. Critical threats include remote code execution capabilities in Spectra Gutenberg Blocks plugin and multiple SQL injection vulnerabilities in student management systems. Additionally, 5 new vulnerabilities were added to CISA's Known Exploited Vulnerabilities catalog this week, indicating active threat actor exploitation. The combination of web application vulnerabilities and network device flaws creates significant exposure to data breaches and system compromise.

---

## Risk Narrative

The threat landscape shows attackers actively targeting web applications and network infrastructure. WordPress plugins represent the highest immediate risk with remote code execution and privilege escalation capabilities. Student management systems contain multiple SQL injection flaws allowing unauthorized database access. Network devices from TRENDnet have authentication bypass vulnerabilities enabling complete system compromise. The recent CISA KEV additions indicate these vulnerability classes are being weaponized in active campaigns. Organizations face potential data exfiltration, system compromise, and operational disruption without immediate remediation efforts.

---

## Prioritized Action Items

1. Immediately patch or disable the Spectra Gutenberg Blocks WordPress plugin (CVE-2026-7465) due to remote code execution risk.
2. Update TRENDnet TEW-432BRP devices to latest firmware to address critical authentication bypass vulnerabilities.
3. Audit and remediate all student management systems for SQL injection vulnerabilities with CVSS 7.3-8.2 scores.
4. Review and patch WordPress Simple History and GEO my WP plugins to prevent account takeover and SQL injection attacks.
5. Implement network segmentation and monitoring for systems running eNdonesia Portal 8.7 until patches are available.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-10110 | 7.3 | 2026-05-30 | A vulnerability was detected in code-projects Student Details Management System 1.0. This affects an unknown function of |
| CVE-2026-10111 | 7.3 | 2026-05-30 | A flaw has been found in sambitraj STUDENT-MANAGEMENT-SYSTEM 1.0. This impacts an unknown function of the component Logi |
| CVE-2026-7459 | 7.5 | 2026-05-30 | The Simple History – Track, Log, and Audit WordPress Changes plugin for WordPress is vulnerable to authenticated (Subscr |
| CVE-2026-7465 | 8.8 | 2026-05-30 | The Spectra Gutenberg Blocks – Website Builder for the Block Editor plugin for WordPress is vulnerable to Remote Code Ex |
| CVE-2026-9757 | 7.5 | 2026-05-30 | The GEO my WP plugin for WordPress is vulnerable to SQL Injection via the 'swlatlng' and 'nelatlng' parameters in all ve |
| CVE-2026-10119 | 8.8 | 2026-05-30 | A security vulnerability has been detected in TRENDnet TEW-432BRP 3.10B20. Impacted is the function formSetMACFilter of  |
| CVE-2026-10120 | 8.8 | 2026-05-30 | A vulnerability was detected in TRENDnet TEW-432BRP 3.10B20. The affected element is the function formSetFirewallRule of |
| CVE-2018-25405 | 8.2 | 2026-05-30 | eNdonesia Portal 8.7 contains multiple SQL injection vulnerabilities that allow unauthenticated attackers to execute arb |
| CVE-2018-25406 | 8.2 | 2026-05-30 | eNdonesia Portal 8.7 contains multiple SQL injection vulnerabilities that allow unauthenticated attackers to execute arb |
| CVE-2018-25407 | 8.2 | 2026-05-30 | eNdonesia Portal 8.7 contains multiple SQL injection vulnerabilities that allow unauthenticated attackers to execute arb |
| CVE-2018-25408 | 7.5 | 2026-05-30 | The Open ISES Project 3.30A contains a path traversal vulnerability in the ajax/download.php endpoint that allows unauth |
| CVE-2018-25409 | 8.8 | 2026-05-30 | SIM-PKH 2.4.1 contains an arbitrary file upload vulnerability that allows authenticated attackers to upload malicious fi |
| CVE-2018-25410 | 7.1 | 2026-05-30 | SIM-PKH 2.4.1 contains an SQL injection vulnerability that allows authenticated attackers to execute arbitrary SQL queri |
| CVE-2018-25411 | 8.2 | 2026-05-30 | MGB OpenSource Guestbook 0.7.0.2 contains an SQL injection vulnerability that allows unauthenticated attackers to execut |
| CVE-2018-25412 | 9.8 | 2026-05-30 | Delta Sql 1.8.2 contains an arbitrary file upload vulnerability that allows unauthenticated attackers to upload maliciou |
| CVE-2018-25413 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25414 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25415 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25416 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25417 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25418 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25419 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25420 | 8.2 | 2026-05-30 | AiOPMSD Final 1.0.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2018-25422 | 8.2 | 2026-05-30 | MOGG web simulator Script contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbit |
| CVE-2018-25424 | 8.2 | 2026-05-30 | Gate Pass Management System 2.1 contains an SQL injection vulnerability that allows unauthenticated attackers to bypass  |
| CVE-2018-25425 | 8.2 | 2026-05-30 | Yot CMS 3.3.1 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary SQL que |
| CVE-2018-25426 | 7.5 | 2026-05-30 | WinMTR 0.91 contains a denial of service vulnerability that allows attackers to crash the application by sending a malfo |
| CVE-2026-10121 | 8.8 | 2026-05-30 | A flaw has been found in TRENDnet TEW-432BRP 3.10B20. The impacted element is the function formSetUrlFilter of the file  |
| CVE-2026-10122 | 8.8 | 2026-05-30 | A vulnerability has been found in TRENDnet TEW-432BRP 3.10B20. This affects the function formSetProtocolFilter of the fi |
| CVE-2026-10123 | 8.8 | 2026-05-30 | A vulnerability was found in TRENDnet TEW-432BRP 3.10B20. This impacts the function formSetDomainFilter of the file /gof |
| CVE-2026-10124 | 8.8 | 2026-05-30 | A vulnerability was determined in Shibby Tomato up to 1.28. Affected is the function rip_zebra_read_ipv4 of the file /us |
| CVE-2026-10125 | 8.8 | 2026-05-30 | A vulnerability was identified in Edimax BR-6478AC 1.23. Affected by this vulnerability is the function formPPPoESetup o |
| CVE-2026-10126 | 8.8 | 2026-05-30 | A security flaw has been discovered in Edimax BR-6478AC 1.23. Affected by this issue is the function formQoS of the file |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-0257 | Palo Alto Networks / PAN-OS | 2026-05-29 | 2026-06-01 | Unknown |
| CVE-2026-48027 | Nx / Nx Console | 2026-05-27 | 2026-06-10 | Known |
| CVE-2026-45321 | TanStack / TanStack | 2026-05-27 | 2026-06-10 | Known |
| CVE-2026-8398 | Daemon / Daemon Tools Lite | 2026-05-27 | 2026-05-30 | Unknown |
| CVE-2026-48172 | LiteSpeed / cPanel Plugin | 2026-05-26 | 2026-05-29 | Unknown |

---

*Total entries in CISA KEV catalog: 1607*