# Vulnerability Intelligence Report

**Date:** 2026-05-30  
**Generated:** 2026-05-30T19:32:45Z  

---

## Executive Summary

Our organization faces significant cybersecurity exposure with 42 high-severity vulnerabilities identified, including several critical flaws with scores up to 9.9. The threat landscape has intensified with 5 new vulnerabilities added to CISA's Known Exploited Vulnerabilities catalog in the past week, indicating active exploitation in the wild. Remote access systems and web applications appear to be primary attack vectors, with multiple buffer overflow and server-side request forgery vulnerabilities present.

---

## Risk Narrative

The current vulnerability landscape presents a multi-vector attack surface that could enable attackers to gain unauthorized system access, execute arbitrary code, and potentially compromise sensitive data. The presence of multiple high-severity vulnerabilities in commonly used components like FreeRDP and web application frameworks creates opportunities for both targeted attacks and automated exploitation campaigns. The combination of buffer overflow vulnerabilities, server-side request forgery flaws, and authentication bypass issues could allow attackers to establish footholds in our network and move laterally to critical systems.

The addition of 5 new entries to CISA's Known Exploited Vulnerabilities catalog within the past week signals an escalating threat environment where vulnerabilities are being weaponized rapidly. This trend, combined with our current exposure to 42 high-severity vulnerabilities, creates a compound risk scenario that could result in business disruption, data breaches, and regulatory compliance issues. Immediate remediation efforts must focus on the most critical vulnerabilities while establishing improved monitoring and response capabilities to address future threats more effectively.

---

## Prioritized Action Items

1. Immediately patch cpp-httplib to version 0.44.0 or higher to address the critical CVSS 9.9 vulnerability that allows HTTP header manipulation
2. Update Formie CMS plugin to versions 2.2.20 or 3.1.24 to prevent unauthenticated code execution through crafted form submissions
3. Upgrade all FreeRDP implementations to version 3.26.0 to eliminate multiple buffer overflow vulnerabilities affecting both client and server components
4. Review and update patch management processes to ensure faster response to CISA KEV additions, implementing automated monitoring for new entries
5. Conduct emergency security assessment of all web-facing applications and remote access solutions to identify additional exposure points

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-44285 | 7.7 | 2026-05-29 | FastGPT is an AI Agent building platform. Prior to 4.15.0-beta1, a Server-Side Request Forgery (SSRF) vulnerability allo |
| CVE-2026-44420 | 8.8 | 2026-05-29 | FreeRDP is a free implementation of the Remote Desktop Protocol. Prior to 3.26.0, a malicious RDP client can trigger a h |
| CVE-2026-44421 | 8.8 | 2026-05-29 | FreeRDP is a free implementation of the Remote Desktop Protocol. Prior to 3.26.0, a malicious RDP server can trigger a h |
| CVE-2026-44422 | 7.5 | 2026-05-29 | FreeRDP is a free implementation of the Remote Desktop Protocol. Prior to 3.26.0, FreeRDP's RDPEAR NDR parser accepts on |
| CVE-2026-45372 | 9.9 | 2026-05-29 | cpp-httplib is a C++11 single-file header-only cross platform HTTP/HTTPS library. Prior to 0.44.0, when cpp-httplib's se |
| CVE-2026-45697 | 9.8 | 2026-05-29 | Formie is a Craft CMS plugin for creating forms. Prior to 2.2.20 and 3.1.24, unauthenticated users could submit crafted  |
| CVE-2026-47123 | 7.5 | 2026-05-29 | FreeScout is a free help desk and shared inbox built with PHP's Laravel framework. Prior to 1.8.220, the email processin |
| CVE-2026-48555 | 7.4 | 2026-05-29 | Spatie Laravel Media Library before version 11.23.0 contains a server-side request forgery vulnerability that allows rem |
| CVE-2026-48557 | 8.8 | 2026-05-29 | Spatie Laravel Media Library before version 11.23.0 contains a file upload restriction bypass in FileAdder::defaultSanit |
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