# Vulnerability Intelligence Report

**Date:** 2026-05-31  
**Generated:** 2026-05-31T01:26:03Z  

---

## Executive Summary

Your organization faces significant cybersecurity risks with 33 high-severity vulnerabilities identified across multiple systems, including critical remote code execution flaws scoring up to 8.8 on the CVSS scale. Five new vulnerabilities have been added to CISA's Known Exploited Vulnerabilities catalog in the past week, indicating active threat actor interest in similar attack vectors. The vulnerability landscape includes SQL injection attacks, authentication bypasses, and remote code execution capabilities that could allow attackers to completely compromise affected systems.

---

## Risk Narrative

The current threat landscape presents a perfect storm of exploitable vulnerabilities across critical business systems. The presence of multiple SQL injection vulnerabilities in student management systems and web applications creates direct pathways for data theft and system compromise. Remote code execution flaws in widely-used WordPress plugins pose particularly severe risks, as they allow attackers to gain complete control over web servers with minimal effort. The high CVSS scores ranging from 7.3 to 8.8 indicate that these vulnerabilities can be exploited with relative ease and minimal user interaction.

The addition of five new entries to CISA's Known Exploited Vulnerabilities catalog within the past week signals heightened threat actor activity and demonstrates that similar vulnerability classes are being actively targeted in the wild. This trend, combined with the age of some vulnerabilities dating back to 2018, suggests that attackers are systematically scanning for and exploiting unpatched systems. The business impact of successful exploitation could include complete system compromise, data breaches affecting student records, website defacement, and potential lateral movement throughout the network infrastructure, making immediate remediation efforts critical for maintaining operational security.

---

## Prioritized Action Items

1. Immediately patch or isolate all WordPress plugins with remote code execution vulnerabilities (CVE-2026-7465) and account takeover flaws (CVE-2026-7459)
2. Apply security updates to TRENDnet TEW-432BRP devices or replace with current models to address critical buffer overflow vulnerabilities (CVE-2026-10119, CVE-2026-10120)
3. Audit and remediate all student management systems for SQL injection vulnerabilities (CVE-2026-10110, CVE-2026-10111) through input validation and parameterized queries
4. Conduct emergency assessment of Palo Alto Networks PAN-OS systems for CVE-2026-0257 exploitation and apply vendor patches immediately
5. Implement web application firewalls and input validation controls for eNdonesia Portal systems while planning migration from the vulnerable 8.7 version

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