# Vulnerability Intelligence Report

**Date:** 2026-11-14  
**Generated:** 2026-11-14T14:46:19Z  

---

## Executive Summary

Our environment faces significant exposure across 110 high-severity vulnerabilities, including critical flaws in Dell PowerStore, network infrastructure, and widely deployed web plugins. CISA added 12 new exploited vulnerabilities to its KEV catalog this week, targeting Microsoft Office, Cisco BroadWorks, Check Point products, and others, signaling active threat actor exploitation. The most urgent risk is a CVSS 9.8 stack-based buffer overflow in PLANET network switches, enabling unauthenticated remote code execution. Immediate prioritization of patching, network segmentation, and KEV remediation is essential to reduce breach probability and protect business operations.

---

## Risk Narrative

Threat actors are actively exploiting vulnerabilities across enterprise software, network devices, and productivity tools, as evidenced by 12 new CISA KEV additions in seven days. The presence of critical buffer overflow flaws in network switches and multiple high-severity Dell PowerStore vulnerabilities creates pathways for privilege escalation, data exfiltration, and service disruption. WordPress and WooCommerce plugin vulnerabilities expand the attack surface for web-facing systems. Active exploitation of Microsoft Office and Cisco BroadWorks by adversaries increases the likelihood of phishing-enabled breaches and unauthorized access. Without rapid remediation, the organization faces elevated risk of ransomware deployment, data loss, and regulatory non-compliance.

---

## Prioritized Action Items

1. Patch or isolate PLANET GS-5220-8P2T2S switches immediately due to the critical CVSS 9.8 unauthenticated remote code execution vulnerability.
2. Apply all available patches for Dell PowerStore systems to address integer overflow, improper authorization, and out-of-bounds read vulnerabilities.
3. Remediate all five newly added CISA KEV vulnerabilities affecting Microsoft Office, Cisco BroadWorks, Check Point, and UnrealIRCd within the mandated timeframe.
4. Audit and update all WooCommerce plugins, including PDF Invoices and Newsletters Lite, to eliminate deserialization and object injection risks.
5. Conduct a full asset inventory and vulnerability scan to identify any additional exposure to this week's high-severity CVEs across the environment.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-103769 | 7.2 | 2026-11-13 | Deserialization of Untrusted Data vulnerability in Acowebs PDF Invoices and Packing Slips For WooCommerce pdf-invoices-a |
| CVE-2026-107522 | 7.2 | 2026-11-13 | Dell PowerStore contains an Improper Authorization vulnerability. An authenticated user could exploit this vulnerability |
| CVE-2026-107523 | 8.7 | 2026-11-13 | Dell PowerStore contains an integer overflow vulnerability. An adjacent attacker could exploit it to bypass volume bound |
| CVE-2026-107524 | 8.8 | 2026-11-13 | Dell PowerStore contains an integer overflow vulnerability. An authenticated storage host could exploit this vulnerabili |
| CVE-2026-109092 | 7.8 | 2026-11-13 | Incorrectly handled negative sizes when processing ProcXvShmPutImage requests in the X.Org xwayland before 24.1.15 and X |
| CVE-2026-109445 | 9.8 | 2026-11-13 | PLANET GS-5220-8P2T2S (hardware version 3.0) firmware versions before 3.2412b261008 contains a stack-based buffer overfl |
| CVE-2026-111547 | 8.1 | 2026-11-13 | Dell PowerStore contains an out-of-bounds read vulnerability. An attacker could exploit this vulnerability, potentially  |
| CVE-2026-118976 | 7.5 | 2026-11-13 | In Progress® Telerik® UI for Blazor versions v11.1.0 through v14.0.0, the demo application's Chat AI Integration example |
| CVE-2026-119512 | 8.8 | 2026-11-13 | Deserialization of Untrusted Data vulnerability in Tribulant Software Newsletters newsletters-lite allows Object Injecti |
| CVE-2026-119517 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in VillaTheme Catna – |
| CVE-2026-120835 | 8.8 | 2026-11-13 | Deserialization of Untrusted Data vulnerability in VillaTheme AFFI – Affiliate Marketing for WooCommerce affi-affiliate- |
| CVE-2026-123975 | 7.5 | 2026-11-13 | Grid Community Toolkit before 6.2.20261111 (globus-gss-assist before 12.9) contains a heap out-of-bounds write in globus |
| CVE-2026-124260 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Jacob N. Breetvelt |
| CVE-2026-124265 | 8.5 | 2026-11-13 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Tribulant Software |
| CVE-2026-124267 | 7.5 | 2026-11-13 | Missing Authorization vulnerability in Noor Alam Gmail SMTP gmail-smtp allows Exploiting Incorrectly Configured Access C |
| CVE-2026-124272 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Dimitri Grassi Sal |
| CVE-2026-124410 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in wpLingua Translati |
| CVE-2026-124415 | 9.3 | 2026-11-13 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Alejandro Alex Res |
| CVE-2026-124420 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Themeisle Woody ad |
| CVE-2026-124970 | 9.3 | 2026-11-13 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in WP BASE WP BASE Bo |
| CVE-2026-125452 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Denishua WPJAM Bas |
| CVE-2026-125783 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in madalin.ungureanu  |
| CVE-2026-125811 | 8.5 | 2026-11-13 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in myCred myCred mycr |
| CVE-2026-125837 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in thethemefoundry Ma |
| CVE-2026-125851 | 9.9 | 2026-11-13 | Unrestricted Upload of File with Dangerous Type vulnerability in themagnifico52 Hotel Booking Lite hotel-booking-lite al |
| CVE-2026-125852 | 7.7 | 2026-11-13 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Realtyna Realtyna Organi |
| CVE-2026-125854 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Unbounce Unbounce  |
| CVE-2026-125855 | 9.8 | 2026-11-13 | Deserialization of Untrusted Data vulnerability in Elextensions ELEX WordPress HelpDesk & Customer Ticketing System elex |
| CVE-2026-125856 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Sarah Giles Dynami |
| CVE-2026-128908 | 8.8 | 2026-11-13 | OS command injection (CWE-78) in the network-configuration handling of the management service (uavmonitor_usbv1) of the  |
| CVE-2026-128909 | 8.8 | 2026-11-13 | Improper verification of cryptographic signature (CWE-347) in the firmware update handler of the management service (uav |
| CVE-2026-128990 | 7.8 | 2026-11-13 | xschem 2.9.9 through 3.4.7 contains a heap out-of-bounds write vulnerability in read_dataset() in src/rawtovcd.c due to  |
| CVE-2024-58406 | 7.5 | 2026-11-13 | Huatian Dynamic OA8000 collaborative office system contains an unauthenticated path traversal vulnerability in /OAapp/js |
| CVE-2026-103813 | 9.1 | 2026-11-13 | Dell PowerStore contains an OS Command Injection vulnerability. An authenticated user with limited privileges could pote |
| CVE-2026-109091 | 7.8 | 2026-11-13 | A buffer overflow in handling EDID Display-Range descriptors in X.Org xwayland before 24.1.15 and X Server before 21.1.2 |
| CVE-2026-111545 | 8.8 | 2026-11-13 | Dell PowerStore contains a SQL Injection vulnerability. An authenticated attacker could exploit this vulnerability, pote |
| CVE-2026-129099 | 7.2 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains a remote code execution vulnerability that allows authenticated administrators to run |
| CVE-2026-129100 | 7.2 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains a remote code execution vulnerability that allows authenticated administrators to exe |
| CVE-2026-129101 | 7.2 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains a mass assignment vulnerability in the vpn.set_conf App RPC method that allows authen |
| CVE-2026-129102 | 7.2 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains a command injection vulnerability that allows authenticated administrators to execute |
| CVE-2026-129103 | 7.2 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains a command injection vulnerability that allows authenticated administrators to execute |
| CVE-2026-129110 | 9.8 | 2026-11-13 | sysPass 3.0.1 through 3.2.11 contains an authentication bypass vulnerability that allows unauthenticated attackers to re |
| CVE-2026-49341 | 7.5 | 2026-11-13 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to version 1.5.1, there is a r |
| CVE-2026-49990 | 8.6 | 2026-11-13 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. From versions 1.4.2 to before 1.4.5, |
| CVE-2026-52787 | 7.5 | 2026-11-13 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.5, 1.5.1, and  |
| CVE-2026-52789 | 7.5 | 2026-11-13 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.5, 1.5.1, and  |
| CVE-2026-52790 | 7.5 | 2026-11-13 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.5, 1.5.1, and  |
| CVE-2026-58498 | 8.6 | 2026-11-13 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.5, 1.5.1, and  |
| CVE-2026-62973 | 7.5 | 2026-11-13 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.5, 1.5.1, and  |
| CVE-2026-63079 | 9.8 | 2026-11-13 | RBH Access Technologies Integra32 Security Management System 5.1.11 R5.0 contains an unauthenticated deserialization vul |
| CVE-2026-129116 | 7.5 | 2026-11-13 | C-Kermit from 7.0.197 before 11.1.515 contains an authentication bypass vulnerability in the IKSD SSL build that leaves  |
| CVE-2026-129122 | 7.5 | 2026-11-13 | C-Kermit 6.0.192 before 11.1.515 contains a buffer overflow vulnerability in tn_snenv() in ckctel.c that allows maliciou |
| CVE-2026-129123 | 8.8 | 2026-11-13 | C-Kermit 8.0.200 before 11.1.515 contains a buffer overflow vulnerability in getreply() in ckcftp.c that allows maliciou |
| CVE-2026-129124 | 8.1 | 2026-11-13 | C-Kermit before 11.1.515 contains an OS command injection vulnerability that allows remote clients to execute shell comm |
| CVE-2026-129125 | 8.1 | 2026-11-13 | C-Kermit 6.0.192 before 11.1.515 contains a remote code execution vulnerability that allows Kermit clients to run shell  |
| CVE-2026-129126 | 8.1 | 2026-11-13 | C-Kermit before 11.1.515 contains a heap buffer overflow vulnerability in putsrv() in ckcfns.c that allows malicious pee |
| CVE-2026-129128 | 7.8 | 2026-11-13 | Goose CLI 1.35.0 before 1.53.0 contains a local code execution vulnerability that allows attackers to run commands by se |
| CVE-2026-129134 | 8.1 | 2026-11-13 | MRBS before 1.13.0 contains a password reset poisoning vulnerability that allows unauthenticated attackers to redirect r |
| CVE-2026-63150 | 8.1 | 2026-11-13 | Omnispace Agora Project through 26.10.0 contains a cross-site request forgery vulnerability that allows remote attackers |
| CVE-2026-63151 | 7.5 | 2026-11-13 | Omnispace Agora Project through 26.10.0 contains a predictable token generation vulnerability that allows unauthenticate |
| CVE-2026-123177 | 8.4 | 2026-11-13 | A flaw was found in dnf5daemon-server. Unauthenticated D-Bus methods pass caller-controlled URL or .rpm path patterns in |
| CVE-2026-123965 | 9.9 | 2026-11-13 | A prompt injection vulnerability in all versions of Jet Admin Cloud Platform allows a remote attacker with a free accoun |
| CVE-2026-126091 | 7.5 | 2026-11-13 | Dental practice sites hosted with iDentalSoft send a JSON response to any user who loads certain pages containing sensit |
| CVE-2026-129139 | 8.2 | 2026-11-13 | paicoding from commit b8206b9 through commit 903adce uses predictable credentials for accounts created via ZSXQ login, b |
| CVE-2026-129143 | 7.5 | 2026-11-13 | paicoding 1.0.3 contains a missing authorization vulnerability in the ArticleRestController article detail endpoint that |
| CVE-2026-129151 | 7.5 | 2026-11-13 | SurveyKing 1.13.2 contains a missing authorization vulnerability in result lookup: the anonymous survey view leaks the l |
| CVE-2026-129153 | 7.1 | 2026-11-13 | SurveyKing 1.12.0 through 1.13.2 contains an authorization bypass in the linked survey feature that fails to verify the  |
| CVE-2026-129161 | 7.4 | 2026-11-13 | Dromara free-fs 2.0.1 through 2.3.1 contains an improper restriction of authentication attempts vulnerability that allow |
| CVE-2026-129165 | 9.1 | 2026-11-13 | Tactical RMM 0.17.0 through 1.6.1 contains an arbitrary file read in the /reporting/templates/preview/ endpoint because  |
| CVE-2026-129167 | 8.1 | 2026-11-13 | Seafile SeaDoc converter 2.0.4 before 2.0.11 and 3.0.0 before 3.0.8 contains an absolute path traversal vulnerability th |
| CVE-2026-129171 | 9.8 | 2026-11-13 | NginxPulse 1.5.0 before 1.6.26 contains an unauthenticated sql injection vulnerability that allows remote attackers to a |
| CVE-2026-100403 | 7.5 | 2026-11-13 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.6, 1.5.2, and  |
| CVE-2026-102612 | 8.1 | 2026-11-13 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.6, 1.5.2, and  |
| CVE-2026-128081 | 7.5 | 2026-11-13 | AutoMapper is a convention-based object-object mapper in .NET. Prior to 15.1.4 and from 16.0.0 until 16.3.0, AutoMapper  |
| CVE-2026-128082 | 7.5 | 2026-11-13 | AutoMapper is a convention-based object-object mapper in .NET. Prior to 15.1.4 and from 16.0.0 until 16.3.0, AutoMapper  |
| CVE-2026-82414 | 8.8 | 2026-11-13 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. From versions 1.4.0 to before 1.4.6, |
| CVE-2026-97692 | 7.7 | 2026-11-13 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.6, 1.5.2, and  |
| CVE-2026-127214 | 8.5 | 2026-11-13 | Flowise through 3.1.4 contains a server-side request forgery vulnerability that allows authenticated attackers with chat |
| CVE-2026-127215 | 8.1 | 2026-11-13 | Kanbanz by Softaculous plugin for WordPress before 1.0.3 contains a broken access control vulnerability that allows auth |
| CVE-2026-128089 | 7.5 | 2026-11-13 | dnspython is a DNS toolkit for Python. Prior to version 2.9.2, the from_text() parser for WKS records does not require t |
| CVE-2026-128118 | 7.5 | 2026-11-13 | SvelteKit is a framework for rapidly developing robust, performant web applications using Svelte. From version 3.0.0 unt |
| CVE-2026-128120 | 7.5 | 2026-11-13 | SvelteKit is a framework for rapidly developing robust, performant web applications using Svelte. From version 2.42.0 un |
| CVE-2026-68905 | 8.2 | 2026-11-13 | Hugo Blog is a tech blog site. In commit 744ca15 and prior, the AI assistant proxy exposes three HTTP endpoints (POST /a |
| CVE-2026-128128 | 7.5 | 2026-11-13 | AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.4, the C WebSocket reader  |
| CVE-2026-82504 | 9.8 | 2026-11-13 | VITEC EZ TV Platform Server before 8.5.0 contains an unrestricted file upload vulnerability in the upload handler that a |
| CVE-2026-109158 | 7.5 | 2026-11-13 | IBM App Connect Operator and IBM App Connect Enterprise Certified Containers Operands may allow the AI Agent to log sens |
| CVE-2026-110278 | 7.4 | 2026-11-13 | IBM ContextForge MCP Gateway 1.0.0 through 1.1.0 could allow an attacker to replay identity propagation claims signature |
| CVE-2026-110279 | 8.1 | 2026-11-13 | IBM ContextForge MCP Gateway 1.0.0 through 1.1.0 is vulnerable to improper credential handling because the X-Upstream-Au |
| CVE-2026-110331 | 7.8 | 2026-11-13 | A flaw was found in abrt. The completeness check introduced to mitigate CVE-2026-54228 and CVE-2026-54229 only verifies  |
| CVE-2026-115788 | 8.1 | 2026-11-13 | IBM App Connect Operator and IBM App Connect Enterprise Certified Containers Operands is vulnerable to Log Forging on a  |
| CVE-2026-123628 | 7.5 | 2026-11-13 | IBM webMethods Integration Server 10.15 and 11.1 could allow a remote attacker to obtain sensitive information due to an |
| CVE-2026-124020 | 8.1 | 2026-11-13 | Control Web Panel (CWP) before webpanel_version 1.30.6 contains a host header injection vulnerability that allows unauth |
| CVE-2026-124021 | 8.1 | 2026-11-13 | Control Web Panel (CWP) before webpanel_version 1.30.6 contains an authorization bypass vulnerability in the validate()  |
| CVE-2026-91869 | 8.1 | 2026-11-13 | IBM Security QRadar EDR 3.12 through 3.12.26 could allow a remote authenticated attacker to bypass security restrictions |
| CVE-2026-9661 | 7.0 | 2026-11-13 | Poste Italiane Postecert FIRMAOK! 1.6.29 on Windows contains a local privilege escalation vulnerability caused by an unc |
| CVE-2026-128134 | 7.8 | 2026-11-13 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research a |
| CVE-2026-129180 | 7.3 | 2026-11-13 | A flaw has been found in projectworlds Visitor Management System 1.0. This vulnerability affects the function mysqli_que |
| CVE-2026-71519 | 8.1 | 2026-11-13 | PrestaShop before 8.2.9 and 9.2.1 contains a broken access control vulnerability that allows an authenticated Webservice |
| CVE-2026-71531 | 8.1 | 2026-11-13 | PrestaShop before 8.2.9 and 9.2.1 contains an authorization flaw in the Webservice API that allows an attacker holding a |
| CVE-2026-124969 | 7.1 | 2026-11-14 | The Optimole – Optimize Images \| Convert WebP & AVIF \| CDN & Lazy Load \| Image Optimization plugin for WordPress is vuln |
| CVE-2026-126173 | 9.8 | 2026-11-14 | The AutomatorWP Pro plugin for WordPress' webhook addon is vulnerable to authorization bypass in all versions up to, and |
| CVE-2026-129181 | 7.3 | 2026-11-14 | A vulnerability has been found in projectworlds Visitor Management System 1.0. This issue affects the function mysqli_qu |
| CVE-2026-129250 | 9.9 | 2026-11-14 | A security vulnerability has been detected in Edimax BR6478ACV2 1.23. The impacted element is the function formPPTPSetup |
| CVE-2026-129427 | 8.7 | 2026-11-14 | Stored XSS via avatar upload chained with an authentication bypass in /Attachments leads to ATO
in Cervantes version v1. |
| CVE-2026-120522 | 9.8 | 2026-11-14 | The Cloud Storage Manager for Fluent Forms – Google Drive, Dropbox, OneDrive, S3 Uploads plugin for WordPress is vulnera |
| CVE-2026-129255 | 8.8 | 2026-11-14 | A vulnerability was identified in CoolerMaster MASTERPLUS+ 1.9.6. This affects the function sub_11504 in the library Win |
| CVE-2026-129429 | 7.1 | 2026-11-14 | Frappe india-payroll before 16.0.4 contains a missing authorization vulnerability in the get_employee_details, compute_t |
| CVE-2026-129433 | 9.9 | 2026-11-14 | Dokploy before 0.31.1 contains an OS command injection vulnerability in getComposeContainerCommand() that allows authent |
| CVE-2026-18053 | 8.8 | 2026-11-14 | The MemberDash plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 1.8.7. T |
| CVE-2026-19907 | 9.8 | 2026-11-14 | The Shipo plugin for WordPress is vulnerable to Authentication Bypass in versions 1.6 through 1.8.0. This is due to the  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-114713 | UnrealIRCd / UnrealIRCd | 2026-11-13 | 2026-11-16 | Unknown |
| CVE-2026-123039 | Check Point / Multiple Products | 2026-11-13 | 2026-11-16 | Unknown |
| CVE-2026-124194 | Microsoft / Office | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-111793 | Openwave Messaging Limited / Webtop Media Transcoder | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-20320 | Cisco / BroadWorks | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-111560 | Barracuda Networks / Multiple Products | 2026-11-10 | 2026-11-13 | Unknown |
| CVE-2026-116606 | Barracuda Networks / Barracuda Email Security Gateway (ESG) | 2026-11-10 | 2026-11-13 | Unknown |
| CVE-2026-125350 | Google / Chromium | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-102895 | GPUStack / GPUStack | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-123158 | OpenBSD / OpenSSH | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-116779 | SignalWire / FreeSwitch | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-123218 | IBM / Aspera Faspex | 2026-11-09 | 2026-11-12 | Unknown |

---

*Total entries in CISA KEV catalog: 1781*