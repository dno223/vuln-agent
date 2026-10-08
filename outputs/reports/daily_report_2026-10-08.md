# Vulnerability Intelligence Report

**Date:** 2026-10-08  
**Generated:** 2026-10-08T15:13:41Z  

---

## Executive Summary

Our environment faces significant exposure across 132 high-severity vulnerabilities, including three critical flaws in Fanvil VoIP firmware scoring up to CVSS 10.0 that enable unauthenticated remote code execution and command injection. Backstage developer portal components carry multiple high-severity RCE and configuration vulnerabilities. Additionally, four new CISA Known Exploited Vulnerabilities were added this week affecting Citrix NetScaler, Fortinet FortiMail, and Zammad, indicating active threat actor exploitation in the wild. Immediate patching and network segmentation are essential to reduce organizational risk.

---

## Risk Narrative

Threat actors are actively exploiting vulnerabilities across enterprise networking, email security, and IT service management platforms, as confirmed by four new CISA KEV entries in the past seven days. The Fanvil firmware flaws present severe risk to VoIP infrastructure, enabling unauthenticated attackers to execute arbitrary commands remotely. Backstage RCE vulnerabilities threaten software development pipelines and internal developer portals. Heap overflow flaws in widely deployed libraries like NTFS-3G and libexpat broaden the attack surface significantly. Combined, these vulnerabilities expose the organization to data breaches, operational disruption, ransomware deployment, and supply chain compromise if left unaddressed.

---

## Prioritized Action Items

1. Immediately isolate or patch Fanvil x7a devices running firmware 2.6.0.1182 to remediate CVSS 10.0 and 9.8 remote code execution and command injection vulnerabilities.
2. Apply CISA KEV-mandated patches for Citrix NetScaler, Fortinet FortiMail, and Zammad within the required federal remediation window, prioritizing internet-facing instances.
3. Upgrade all Backstage installations to versions 1.14.8, 1.15.6, or 2.0.1 or later to address remote code execution and configuration vulnerabilities in the techdocs-node plugin.
4. Patch NTFS-3G to version 2026.7.7 or later and update libexpat to commit 13c5f63 or later to mitigate heap buffer overflow vulnerabilities exploitable via malicious file parsing.
5. Conduct an asset inventory scan to confirm all affected software versions are identified and enforce network access controls limiting management portal exposure to trusted IP ranges only.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2025-70516 | 9.1 | 2026-10-07 | The websocket handler of Fanvil x7a firmware version 2.6.0.1182 does not enforce proper authentication restrictions agai |
| CVE-2025-70518 | 10.0 | 2026-10-07 | The management portal's diagnostic ping tool of Fanvil x7a firmware version 2.6.0.1182 does not handle user supplied inp |
| CVE-2025-70521 | 9.8 | 2026-10-07 | The management portal's diagnostic ping tool of Fanvil x7a firmware version 2.6.0.1182 does not handle user supplied inp |
| CVE-2026-106510 | 7.7 | 2026-10-07 | Backstage is an open framework for building developer portals. Prior to 1.14.6, the @backstage/plugin-techdocs-node pack |
| CVE-2026-106556 | 7.7 | 2026-10-07 | Backstage is an open framework for building developer portals. Prior to 1.14.6, the @backstage/plugin-techdocs-node pack |
| CVE-2026-106558 | 8.8 | 2026-10-07 | Backstage is an open framework for building developer portals. Prior to 1.14.8, 1.15.6, and 2.0.1, the @backstage/plugin |
| CVE-2026-106560 | 7.1 | 2026-10-07 | Backstage is an open framework for building developer portals. Prior to 0.3.25, the @backstage/plugin-scaffolder-backend |
| CVE-2026-107202 | 9.1 | 2026-10-07 | A command injection vulnerability exists in the h-ui (version v0.0.25 and below) administrative API due to improper vali |
| CVE-2026-46570 | 8.1 | 2026-10-07 | In NTFS-3G before 2026.7.7, a heap buffer overflow exists in ntfs_index_walk_down() in libntfs-3g/index.c that allows an |
| CVE-2026-77214 | 8.2 | 2026-10-07 | libexpat before commit 13c5f63 contains a heap buffer over-read vulnerability in xmlparse.c. XML_ParseBuffer advances th |
| CVE-2026-107204 | 9.8 | 2026-10-07 | LMCache through 0.5.5 contains an unauthenticated remote code execution vulnerability that allows remote attackers to ex |
| CVE-2026-107205 | 8.6 | 2026-10-07 | LMCache through 0.5.5 contains a missing authentication vulnerability in the multiprocess coordinator that allows remote |
| CVE-2026-107206 | 9.4 | 2026-10-07 | LMCache through 0.5.5 contains a missing authentication vulnerability in the multiprocess mode HTTP server that allows r |
| CVE-2026-107207 | 7.2 | 2026-10-07 | LMCache through 0.5.5 contains a server-side request forgery vulnerability in its frontend monitoring service that allow |
| CVE-2026-107270 | 7.1 | 2026-10-07 | Gophish through 0.12.1 contains an insecure direct object reference vulnerability that allows authenticated users to tak |
| CVE-2026-106557 | 7.7 | 2026-10-07 | Backstage is an open framework for building developer portals. Prior to 1.14.6 and 1.15.4, the @backstage/plugin-techdoc |
| CVE-2026-20328 | 9.1 | 2026-10-07 | A vulnerability in the web-based management interface of Cisco License On-Prem, formerly Cisco Smart Software Manager On |
| CVE-2026-20362 | 7.2 | 2026-10-07 | A vulnerability in the web-based management interface of Cisco Finesse could allow an unauthenticated, remote attacker t |
| CVE-2026-62176 | 9.1 | 2026-10-07 | PraisonAI is a multi-agent teams system. Prior to version 4.6.78, the `deploy/api.py` module generates Python server cod |
| CVE-2026-62251 | 8.1 | 2026-10-07 | Homer is open source telecom observability software. Prior to version 11.0.283, the `V4StatisticsQuery` handler passes t |
| CVE-2026-62252 | 9.8 | 2026-10-07 | Homer is open source telecom observability software. Prior to version 11.0.283, on every fresh Homer deployment using in |
| CVE-2026-62253 | 9.8 | 2026-10-07 | Homer is open source telecom observability software. Prior to version 11.0.283, both JWT middleware functions (`JWTMiddl |
| CVE-2026-76453 | 8.8 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco NX-OS engineering team has co |
| CVE-2026-76454 | 9.1 | 2026-10-07 | A vulnerability in the Cisco Smart Licensing Utility API of Cisco License On-Prem, formerly Cisco Smart Software Manager |
| CVE-2026-76455 | 9.8 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco NX-OS engineering team has co |
| CVE-2026-76456 | 8.6 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco NX-OS engineering team has co |
| CVE-2026-76457 | 8.6 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco NX-OS engineering team has co |
| CVE-2026-76458 | 8.6 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco NX-OS engineering team has co |
| CVE-2026-76459 | 8.8 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco NX-OS engineering team has co |
| CVE-2026-76463 | 8.8 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco networking engineering team h |
| CVE-2026-76464 | 9.6 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco networking engineering team h |
| CVE-2026-76465 | 9.8 | 2026-10-07 | A vulnerability in the MPLS Operation, Administration, and Maintenance (OAM) feature of Cisco NX-OS Software for Cisco N |
| CVE-2026-76467 | 7.5 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco networking engineering team h |
| CVE-2026-76468 | 8.2 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco networking engineering team h |
| CVE-2026-76469 | 7.4 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco networking engineering team h |
| CVE-2026-76470 | 8.8 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco networking engineering team h |
| CVE-2026-76471 | 9.8 | 2026-10-07 | A vulnerability in the NX-API feature of Cisco NX-OS Software could allow an unauthenticated, remote attacker to execute |
| CVE-2026-76472 | 8.8 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco networking engineering team h |
| CVE-2026-76480 | 9.8 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the engineering team for Cisco License  |
| CVE-2026-76482 | 10.0 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the engineering team for Cisco License  |
| CVE-2026-76483 | 9.1 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the engineering team for Cisco License  |
| CVE-2026-76484 | 8.8 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the engineering team for Cisco License  |
| CVE-2026-76485 | 9.8 | 2026-10-07 | A vulnerability in the VXLAN Operation, Administration, and Maintenance (OAM) feature of Cisco NX-OS Software, known as  |
| CVE-2026-76486 | 9.8 | 2026-10-07 | A vulnerability in the VXLAN Operation, Administration, and Maintenance (OAM) feature of Cisco NX-OS Software, known as  |
| CVE-2026-76498 | 9.8 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Application Policy Infrastruc |
| CVE-2026-76499 | 9.8 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Application Policy Infrastruc |
| CVE-2026-76500 | 9.8 | 2026-10-07 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Application Policy Infrastruc |
| CVE-2026-76501 | 9.8 | 2026-10-07 | A vulnerability in the Segment Routing over IPv6 (SRv6) Operation, Administration, and Maintenance (OAM) feature of Cisc |
| CVE-2026-94662 | 7.1 | 2026-10-07 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Unlimited Elements |
| CVE-2026-94670 | 7.1 | 2026-10-07 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Everest Forms allo |
| CVE-2026-95534 | 8.8 | 2026-10-07 | Deserialization of Untrusted Data vulnerability in Unlimited Elements Unlimited Elements For Elementor (Free Widgets, Ad |
| CVE-2026-95595 | 7.1 | 2026-10-07 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Fontsplugin Disabl |
| CVE-2026-95605 | 9.3 | 2026-10-07 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Passionate Program |
| CVE-2026-95606 | 9.8 | 2026-10-07 | Deserialization of Untrusted Data vulnerability in Liquid Web / StellarWP The Events Calendar allows Object Injection.

 |
| CVE-2026-107212 | 7.5 | 2026-10-07 | Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.1.0 to 2.11.0, Rows.Colum |
| CVE-2026-107214 | 7.5 | 2026-10-07 | Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.3.1 to 2.11.0, the decryp |
| CVE-2026-107215 | 7.5 | 2026-10-07 | Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.3.1 to 2.11.0, extractPar |
| CVE-2026-107216 | 7.5 | 2026-10-07 | Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.8.1 to 2.11.0, ANCHORARRA |
| CVE-2026-56851 | 7.5 | 2026-10-07 | The Nickname profile can panic with an out-of-bounds slice error when transforming crafted input into a short destinatio |
| CVE-2026-96335 | 7.5 | 2026-10-07 | Missing Authorization vulnerability in WPMU DEV Forminator allows Exploiting Incorrectly Configured Access Control Secur |
| CVE-2026-106164 | 7.3 | 2026-10-07 | In Progress® Telerik® Document Processing SpreadProcessing library, versions prior to 2026.3.1006, an infinite loop vuln |
| CVE-2026-107217 | 7.5 | 2026-10-07 | Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.0.0 to 2.11.0 in github.c |
| CVE-2026-107219 | 7.5 | 2026-10-07 | Excelize is a Go language library for reading and writing Microsoft Excel spreadsheets. From 2.3.1 to 2.11.0, agile decr |
| CVE-2026-107161 | 7.5 | 2026-10-07 | A heap-based buffer overflow flaw was found in Cyrus SASL. The add_to_challenge() function in the DIGEST-MD5 plugin comp |
| CVE-2026-107227 | 7.5 | 2026-10-07 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process HT |
| CVE-2026-107352 | 7.7 | 2026-10-07 | Missing authorization checks in Amazon Athena engine version 3 request handling could have allowed an authenticated user |
| CVE-2026-76266 | 7.7 | 2026-10-07 | In Splunk Enterprise versions below 10.4.3, 10.2.7, 10.0.10, and 9.4.15 on Linux, a local user who can run commands as t |
| CVE-2026-76268 | 9.8 | 2026-10-07 | In Splunk Enterprise versions below 10.4.3 and 10.2.7, an unauthenticated user with network access to the Patroni Repres |
| CVE-2026-76283 | 7.6 | 2026-10-07 | Protection Mechanism Failure. Splunk addressed multiple internally identified vulnerabilities in Splunk Enterprise versi |
| CVE-2026-105816 | 8.0 | 2026-10-07 | Vault and Vault Enterprise did not consistently verify that stored plugin catalog entries reference binaries within the  |
| CVE-2026-107230 | 7.4 | 2026-10-07 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process HT |
| CVE-2026-107232 | 7.5 | 2026-10-07 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process HT |
| CVE-2026-89322 | 7.2 | 2026-10-07 | Vault and Vault Enterprise did not consistently evaluate ACL policies against the canonical form of resource and policy  |
| CVE-2026-82627 | 7.5 | 2026-10-08 | The Uncanny Automator – AI + Automation for WordPress \| AI Agent, AI Page Builder, Free AI Usage Included plugin for Wor |
| CVE-2026-17196 | 8.8 | 2026-10-08 | The Super Forms – Drag & Drop Form Builder plugin for WordPress is vulnerable to Unrestricted File Type Upload in all ve |
| CVE-2026-17609 | 9.1 | 2026-10-08 | The Super Forms – Drag & Drop Form Builder plugin for WordPress is vulnerable to Arbitrary Directory Deletion in all ver |
| CVE-2026-103309 | 7.5 | 2026-10-08 | The GPTranslate  WordPress plugin before 2.34.14 does not properly restrict who can store translations, and does not esc |
| CVE-2026-103646 | 9.8 | 2026-10-08 | The Ultimate Multisite  WordPress plugin before 2.17.0 does not require authentication before a logged-out checkout is l |
| CVE-2026-103692 | 9.8 | 2026-10-08 | The Frontend Dashboard WordPress plugin before 3.0.5 does not perform any authorisation or nonce check on actions availa |
| CVE-2026-107459 | 9.8 | 2026-10-08 | The SecuShare Pro developed by Openfind has an OS Command Injection vulnerability. Unauthenticated remote attackers can  |
| CVE-2026-85097 | 9.8 | 2026-10-08 | The Bricksforge plugin for WordPress is vulnerable to unauthenticated arbitrary file upload in versions up to, and inclu |
| CVE-2026-105110 | 9.8 | 2026-10-08 | OS Command Injection in the login.xgi CGI endpoint in Iskratel Innbox GPON ONT devices allows an unauthenticated remote  |
| CVE-2026-71183 | 7.1 | 2026-10-08 | An authorization vulnerability in Apache DolphinScheduler allows authenticated users to obtain information about data so |
| CVE-2026-71895 | 7.1 | 2026-10-08 | An authorization vulnerability in Apache DolphinScheduler allows authenticated non-admin users to retrieve Kubernetes co |
| CVE-2026-107510 | 9.1 | 2026-10-08 | An authenticated high privilege user can inject arguments in troubleshooting commands resulting in privilege escalation. |
| CVE-2026-103010 | 7.8 | 2026-10-08 | Heap-based buffer overflow in the legacy Blowfish decryption routine (BlowFishEncryptor::DecryptFromString) in Progressi |
| CVE-2026-103647 | 8.0 | 2026-10-08 | Cross-site scripting in the webmail of Progressive Robot hMailServer 6.3.2 through 6.3.5 allows a remote attacker who ca |
| CVE-2026-103649 | 7.5 | 2026-10-08 | Missing network timeouts in the Linux builds of Progressive Robot hMailServer 6.3.0 through 6.3.5 allow a remote attacke |
| CVE-2026-104658 | 7.8 | 2026-10-08 | The Linux live-update apply helper (hmailserver-update) of Progressive Robot hMailServer 6.3.4 and 6.3.5 runs as root on |
| CVE-2026-104659 | 7.5 | 2026-10-08 | Missing Host header validation and missing throttling of failed administrator sign-ins in the REST API listener of Progr |
| CVE-2026-104660 | 7.8 | 2026-10-08 | Missing authorization on COM objects in Progressive Robot hMailServer 6.0.0 through 6.3.5 (Windows only) lets a local in |
| CVE-2026-104704 | 7.4 | 2026-10-08 | Progressive Robot hMailServer 6.0.0 through 6.3.5 does not enforce TLS for outbound SMTP delivery to a mail exchanger wh |
| CVE-2026-107573 | 7.8 | 2026-10-08 | Incorrect default permissions in the Windows installer of Progressive Robot hMailServer 6.0.0 through 6.3.5 allow a loca |
| CVE-2026-107574 | 7.5 | 2026-10-08 | Inefficient algorithmic complexity in the JSON reader of Progressive Robot hMailServer allows a remote unauthenticated a |
| CVE-2026-107576 | 7.5 | 2026-10-08 | Inefficient algorithmic complexity in the inbound DKIM and ARC signature verification of Progressive Robot hMailServer 6 |
| CVE-2026-107577 | 7.5 | 2026-10-08 | Inefficient algorithmic complexity and a non-terminating loop in the MIME processing of received messages in Progressive |
| CVE-2026-107579 | 7.5 | 2026-10-08 | Inefficient algorithmic complexity in the bounce and complaint processing of Progressive Robot hMailServer 6.3.4 and 6.3 |
| CVE-2026-107584 | 7.4 | 2026-10-08 | Progressive Robot hMailServer 6.0.0 through 6.3.5 fails open when applying DANE (RFC 7672) to outbound SMTP delivery. Th |
| CVE-2026-19083 | 8.8 | 2026-10-08 | Authorization bypass through User-Controlled key vulnerability in AKIN Software Computer Import-Export Industry and Trad |
| CVE-2026-92555 | 9.8 | 2026-10-08 | Insertion of sensitive information into sent data vulnerability in AKIN Software Computer Import-Export Industry and Tra |
| CVE-2026-105076 | 7.6 | 2026-10-08 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Appsbd Vitepos vit |
| CVE-2026-106611 | 7.1 | 2026-10-08 | Cross-Site Request Forgery (CSRF) vulnerability in WPMU DEV Forminator forminator allows Cross Site Request Forgery.This |
| CVE-2026-16169 | 7.5 | 2026-10-08 | IBM DataPower Gateway 11.0.0.0 through 11.0.0.2 could allow a remote attacker to cause a denial of service due to uncont |
| CVE-2026-16170 | 7.5 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-16176 | 7.5 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-16178 | 7.5 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-16179 | 7.5 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-16181 | 7.4 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-16340 | 9.8 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-19218 | 9.1 | 2026-10-08 | Weak Password Recovery Mechanism for Forgotten Password vulnerability in AKIN Software Computer Import-Export Industry a |
| CVE-2026-44031 | 7.5 | 2026-10-08 | Uncontrolled recursion in DcmSequenceOfItems::read() and DcmItem::read() in the dcmdata library of OFFIS DCMTK 3.7.0 all |
| CVE-2026-62142 | 8.8 | 2026-10-08 | Cross-Site Request Forgery (CSRF) vulnerability in Melapress WP 2FA wp-2fa allows Cross Site Request Forgery.This issue  |
| CVE-2026-66479 | 7.1 | 2026-10-08 | Cross-Site Request Forgery (CSRF) vulnerability in Liquid Web / StellarWP WPComplete wpcomplete allows Stored XSS.This i |
| CVE-2026-107611 | 7.1 | 2026-10-08 | An out-of-bounds read vulnerability in the ZRLE decoder of GlavSoft TightVNC Viewer for Windows before 2.8.88 allows a m |
| CVE-2026-107612 | 7.8 | 2026-10-08 | Incorrect permission assignment in GlavSoft TightVNC Server for Windows before 2.8.88 allows a local authenticated user  |
| CVE-2026-107615 | 7.8 | 2026-10-08 | An uncontrolled search path element vulnerability in GlavSoft TightVNC Server for Windows before 2.8.88 allows a local a |
| CVE-2026-14990 | 9.3 | 2026-10-08 | IBM DataPower Gateway 10.6.0.0 through 10.6.0.10 is vulnerable to cross-site scripting. This vulnerability allows an una |
| CVE-2026-14991 | 9.8 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-15762 | 9.8 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-15781 | 8.0 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-15784 | 8.1 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-15819 | 7.5 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-15822 | 7.5 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-15824 | 8.2 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-16111 | 7.5 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-16159 | 8.6 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-16161 | 7.5 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-16163 | 8.6 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-16164 | 7.5 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-16165 | 7.5 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-16167 | 7.5 | 2026-10-08 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throug |
| CVE-2026-91844 | 7.3 | 2026-10-08 | Unrestricted upload of file with dangerous type vulnerability in İzometri IT Services Domestic and Foreign Trade Co. Ltd |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-88779 | Citrix / NetScaler | 2026-10-04 | 2026-10-07 | Unknown |
| CVE-2026-102490 | Zammad GmbH / Zammad | 2026-10-02 | 2026-10-05 | Unknown |
| CVE-2026-102489 | Zammad GmbH / Zammad | 2026-10-02 | 2026-10-05 | Unknown |
| CVE-2026-104286 | Fortinet / FortiMail | 2026-10-01 | 2026-10-04 | Unknown |

---

*Total entries in CISA KEV catalog: 1734*