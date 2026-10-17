# Vulnerability Intelligence Report

**Date:** 2026-10-17  
**Generated:** 2026-10-17T11:58:45Z  

---

## Executive Summary

Our environment faces significant exposure across 123 high-severity vulnerabilities, including a critical CVSS 9.8 hard-coded credential flaw in EseeCloud devices enabling full unauthorized access. Additional high-risk issues include remote code execution in SGLang, SQL injection in MapSVG, and CSRF vulnerabilities in WordPress plugins. Nine new CISA Known Exploited Vulnerabilities were added this week affecting BeyondTrust, Fortinet, Atlassian, Cisco, and Ahsay products, signaling active threat actor exploitation in the wild. Immediate prioritization and remediation of the most critical findings is required to reduce organizational risk.

---

## Risk Narrative

Threat actors are actively exploiting vulnerabilities across enterprise platforms including Fortinet, Atlassian, Cisco, and BeyondTrust, as confirmed by nine new CISA KEV additions this week. The presence of a CVSS 9.8 hard-coded credential flaw represents an immediate takeover risk with minimal attacker skill required. Remote code execution, SQL injection, and CSRF vulnerabilities across web platforms expand the attack surface significantly, enabling data theft, lateral movement, and privilege escalation. Unpatched virtualization and resource exhaustion flaws could destabilize critical infrastructure. The combination of actively exploited known vulnerabilities and a large backlog of high-severity CVEs creates compounding business risk including operational disruption, regulatory exposure, and potential data breach.

---

## Prioritized Action Items

1. Immediately isolate or patch EseeCloud devices affected by the CVSS 9.8 hard-coded credential vulnerability CVE-2026-107617 to prevent unauthorized access.
2. Assess and patch all systems running BeyondTrust, Fortinet, Atlassian, Cisco, and Ahsay products newly listed in the CISA KEV catalog within 24-48 hours.
3. Remediate the SGLang remote code execution vulnerability CVE-2026-111391 and the SQL injection flaw CVE-2026-111399 on all affected servers immediately.
4. Apply patches or mitigations for the spice-server memory bounds vulnerabilities CVE-2026-105958 and CVE-2026-105959 to prevent potential exploitation in virtualized environments.
5. Audit and harden all WordPress plugin configurations, prioritizing removal or patching of plugins affected by XSS, CSRF, and authorization bypass vulnerabilities.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-105959 | 7.5 | 2026-10-16 | A flaw was found in spice-server. The GLZ encoder dictionary restore path truncates a size_t allocation size to int when |
| CVE-2026-107648 | 7.2 | 2026-10-16 | The WP Sessions Time Monitoring Full Automatic plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the |
| CVE-2026-111391 | 8.1 | 2026-10-16 | SGLang 0.5.10 through 0.5.22 contains a code injection vulnerability in _evaluate_filter() that allows remote attackers  |
| CVE-2026-105958 | 7.5 | 2026-10-16 | A flaw was found in spice-server. Multiple migration data handlers use client-supplied offsets from SPICE_MSGC_MIGRATE_D |
| CVE-2026-107564 | 7.5 | 2026-10-16 | An unauthenticated remote attacker may use an allocation of resources without limits or throttling weakness in the affec |
| CVE-2026-111396 | 7.1 | 2026-10-16 | Missing Authorization vulnerability in Liquid Web / StellarWP Advanced Post Manager advanced-post-manager allows Exploit |
| CVE-2026-111399 | 8.5 | 2026-10-16 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in PT Norther Lights  |
| CVE-2026-63618 | 7.5 | 2026-10-16 | Exposure of Sensitive Information (system level configuration info) to an Unauthorized Actor vulnerability in Apache Kyl |
| CVE-2026-107617 | 9.8 | 2026-10-16 | An attacker can use a hard-coded credential to log in to EseeCloud devices. |
| CVE-2026-111413 | 8.8 | 2026-10-16 | Cross-Site Request Forgery (CSRF) vulnerability in aThemeArt aThemeArt Theme Helper athemeart-theme-helper allows Cross  |
| CVE-2026-18516 | 9.6 | 2026-10-16 | An output escaping vulnerability in the Audit Logs component of Crafty Controller allows a remote, unauthenticated attac |
| CVE-2026-101021 | 7.5 | 2026-10-16 | MultipartInputStream performs inefficient boundary matching and unnecessary buffer copying. Crafted multipart input can  |
| CVE-2026-105273 | 7.5 | 2026-10-16 | MP4Parser does not adequately validate MP4 box sizes. A malformed box can cause parsing to make no forward progress and  |
| CVE-2026-105279 | 9.1 | 2026-10-16 | In the default configuration, the archive accepts DICOM associations from an unregistered calling AE. A remote peer can  |
| CVE-2026-105667 | 7.5 | 2026-10-16 | In the default configuration, the HL7 listener accepts ADT^A40 patient-merge messages without authenticating the sending |
| CVE-2026-106705 | 8.8 | 2026-10-16 | ELADMIN (eladmin-mp) up to 2.7 contains an improper access control vulnerability in the role management module. The endp |
| CVE-2026-107621 | 7.5 | 2026-10-16 | JPEGParser can enter an infinite loop while parsing a specially crafted or truncated stream. |
| CVE-2026-88755 | 7.8 | 2026-10-16 | Z.ai ZCode v3.11.2.6792 was discovered to automatically establish connections with MCP servers declared inside a reposit |
| CVE-2026-95182 | 10.0 | 2026-10-16 | An untrusted search path in DeepSeek Harness (dsh) commit c291e796 allows attackers to execute arbitrary code via supply |
| CVE-2026-97851 | 9.1 | 2026-10-16 | The storage status-change REST service allows location records still associated with DICOM instances to be changed to de |
| CVE-2026-102941 | 7.5 | 2026-10-16 | The package github.com/gomarkdown/markdown is a Go library for parsing Markdown text and rendering as HTML. Prior to 0.0 |
| CVE-2026-41582 | 7.5 | 2026-10-16 | countly-server is the server-side part of Countly, a product analytics solution. Prior to 24.05.50 and 25.03.44, public  |
| CVE-2026-42269 | 8.1 | 2026-10-16 | countly-server is the server-side part of Countly, a product analytics solution. Prior to 24.05.50 and 25.03.44, the aut |
| CVE-2026-42270 | 7.5 | 2026-10-16 | countly-server is the server-side part of Countly, a product analytics solution. Prior to 24.05.50 and 25.03.44, star-ra |
| CVE-2026-44977 | 9.0 | 2026-10-16 | countly-server is the server-side part of Countly, a product analytics solution. Prior to 24.05.50 and 25.03.44, plugins |
| CVE-2026-46472 | 7.5 | 2026-10-16 | An issue was discovered in GStreamer gst-plugins-good before 1.28.2. While parsing an MP4 file, the isomp4 plugin's qtde |
| CVE-2026-48503 | 7.5 | 2026-10-16 | libIEC61850 is an open-source implementation of IEC 61850 client and server protocols including MMS, GOOSE, Sampled Valu |
| CVE-2026-48741 | 7.5 | 2026-10-16 | libIEC61850 is an open-source implementation of IEC 61850 client and server protocols including MMS, GOOSE, Sampled Valu |
| CVE-2026-57486 | 7.5 | 2026-10-16 | pupnp is an SDK for development of UPnP device and control point applications. Prior to 2.0.2, ixmlNode_compare in ixml/ |
| CVE-2026-57487 | 7.5 | 2026-10-16 | pupnp is an SDK for development of UPnP device and control point applications. Prior to 2.0.2, Transfer-Encoding: chunke |
| CVE-2026-57488 | 7.1 | 2026-10-16 | pupnp is an SDK for development of UPnP device and control point applications. Prior to 2.0.2, raw_to_int in upnp/src/ge |
| CVE-2026-77630 | 7.5 | 2026-10-16 | pupnp is an SDK for development of UPnP device and control point applications. Prior to 22.0.4, parse_hostport in upnp/s |
| CVE-2026-92263 | 7.2 | 2026-10-16 | SparkyFitness is a self-hosted, AI-powered health and fitness tracker for families. Prior to 1.6.0, the api/admin/backup |
| CVE-2026-96424 | 7.8 | 2026-10-16 | Incorrect DBus policy for lomiri-upload-manager (part of lomiri-download-manager) allows arbitrary user to read arbitrar |
| CVE-2026-102692 | 9.1 | 2026-10-16 | RIOT is an open-source microcontroller operating system designed for Internet of Things devices and other embedded syste |
| CVE-2026-102693 | 9.6 | 2026-10-16 | RIOT is an open-source microcontroller operating system designed for Internet of Things devices and other embedded syste |
| CVE-2026-49868 | 9.8 | 2026-10-16 | RIOT is an open-source microcontroller operating system designed for Internet of Things devices and other embedded syste |
| CVE-2026-57169 | 9.6 | 2026-10-16 | Dockhand is a Docker management application. Prior to 1.0.34, the in-browser container terminal endpoint /api/containers |
| CVE-2026-77474 | 7.1 | 2026-10-16 | destructive_command_guard (dcg) is a command-line safety tool that blocks destructive shell commands before AI coding ag |
| CVE-2026-85746 | 9.9 | 2026-10-16 | MariaDB server is a community developed fork of MySQL server. From 10.6.1 until 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3 |
| CVE-2026-85748 | 9.9 | 2026-10-16 | MariaDB server is a community developed fork of MySQL server. From 12.3.1 until 12.3.3 and 13.0.2, SYS_REFCURSOR handlin |
| CVE-2026-86008 | 7.2 | 2026-10-16 | Mailu is a mail server distributed as a set of Docker images. Prior to 8577c929b4ade04d3cd4210cf036601abd793556, a domai |
| CVE-2026-86047 | 7.7 | 2026-10-16 | MariaDB server is a community developed fork of MySQL server. From 10.6.1 until 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3 |
| CVE-2026-92262 | 9.9 | 2026-10-16 | MariaDB server is a community developed fork of MySQL server. From 10.6.1 until 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3 |
| CVE-2026-97380 | 8.8 | 2026-10-16 | MariaDB server is a community developed fork of MySQL server. From 10.6.1 until 10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3 |
| CVE-2026-102551 | 7.7 | 2026-10-16 | Improper verification of the source of a communication channel in the IPv6 Router Advertisement handler in Amazon FreeRT |
| CVE-2026-109587 | 8.8 | 2026-10-16 | Incorrect authorization in the Arm Cortex-R82 (Armv8-R AArch64) MPU port in FreeRTOS-Kernel V11.3.0 and V11.3.1 might al |
| CVE-2026-109588 | 8.8 | 2026-10-16 | Numeric truncation of the buffer length in the MPU buffer authorization check in FreeRTOS-Kernel V11.3.0 and V11.3.1 on  |
| CVE-2026-111605 | 8.1 | 2026-10-16 | Jpom through 2.11.12 contains an authorization bypass vulnerability in SshFileController that allows authenticated works |
| CVE-2026-111606 | 8.1 | 2026-10-16 | Huly Platform through 0.7.432 contains a missing authorization vulnerability that allows any authenticated user to merge |
| CVE-2026-111607 | 7.1 | 2026-10-16 | Jeepay through 3.2.9 contains an insecure direct object reference vulnerability that allows authenticated merchant users |
| CVE-2026-111612 | 7.5 | 2026-10-16 | netdisk-fast-download through 0.4.8 contains an information disclosure vulnerability that allows unauthenticated attacke |
| CVE-2026-111613 | 7.5 | 2026-10-16 | AllData through 0.7.1 contains an unauthenticated JDBC injection vulnerability that allows remote attackers to open arbi |
| CVE-2026-111626 | 9.8 | 2026-10-16 | Webreaper Damselfly through 4.5.3 contains an authentication bypass vulnerability that allows unauthenticated attackers  |
| CVE-2026-111627 | 7.2 | 2026-10-16 | HestiaCP before 1.10.5 contains an authorization bypass vulnerability that allows non-ROOT_USER administrators to perfor |
| CVE-2026-111633 | 8.6 | 2026-10-16 | ZKEACMS through 4.4 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge REST  |
| CVE-2026-111634 | 8.1 | 2026-10-16 | Helical Insight through 7.0.0 contains an sql injection vulnerability that allows authenticated viewers to inject SQL th |
| CVE-2026-111636 | 8.1 | 2026-10-16 | OpenBMB StaffDeck through 0.5.6 contains an authentication bypass vulnerability that allows unauthenticated attackers to |
| CVE-2026-111638 | 7.7 | 2026-10-16 | sshportal through 1.19.5 contains a missing authorization vulnerability in the management shell 'key show' command that  |
| CVE-2026-111639 | 8.1 | 2026-10-16 | bbs-go through 4.4.6 contains an authentication bypass vulnerability in the /api/login/google_one_tap endpoint that allo |
| CVE-2026-111641 | 9.8 | 2026-10-16 | FastapiAdmin through 3.0 contains an authentication bypass vulnerability that allows unauthenticated attackers to obtain |
| CVE-2026-111642 | 8.8 | 2026-10-16 | FastapiAdmin through 3.0 contains a hard-coded JWT signing secret in backend/app/config/setting.py that allows low-privi |
| CVE-2026-111643 | 9.8 | 2026-10-16 | Misaka Danmu Server through 2.8.9 contains an authentication bypass vulnerability that allows unauthenticated attackers  |
| CVE-2026-111644 | 7.3 | 2026-10-16 | Misaka Danmu Server through 2.8.9 contains a missing authentication vulnerability that allows unauthenticated attackers  |
| CVE-2026-111650 | 8.6 | 2026-10-16 | ChronoFrame through 1.0.0 contains a missing authentication vulnerability in the server/api/wizard/ handlers that allows |
| CVE-2026-111663 | 8.6 | 2026-10-16 | Chaskiq through 2.0.3 contains a server-side request forgery vulnerability that allows unauthenticated attackers to fetc |
| CVE-2026-111671 | 7.1 | 2026-10-16 | Cube-studio through 2026.09.01 contains an insecure direct object reference vulnerability that allows authenticated user |
| CVE-2026-111673 | 9.8 | 2026-10-16 | IceCMS through 4.1.5 contains a missing authentication vulnerability that allows unauthenticated attackers to modify, de |
| CVE-2026-111675 | 7.4 | 2026-10-16 | Course-tencent-cloud through 2.0.1 contains an improper restriction of authentication attempts vulnerability that allows |
| CVE-2026-111680 | 8.3 | 2026-10-16 | APIPark through 1.9.7-beta contains an authorization bypass vulnerability that allows authenticated team managers to acc |
| CVE-2026-111681 | 8.8 | 2026-10-16 | EFAK through 5.1.0 contains a missing authorization vulnerability that allows authenticated low-privilege users to manag |
| CVE-2026-111684 | 8.3 | 2026-10-16 | Magistrala through 1.0.0 contains an authorization bypass vulnerability that allows authenticated workspace members to v |
| CVE-2026-111685 | 7.5 | 2026-10-16 | IceCMS through 4.1.5 contains an unauthenticated sql injection vulnerability that allows remote attackers to inject SQL  |
| CVE-2026-111686 | 7.5 | 2026-10-16 | IceCMS through 4.1.5 contains an unauthenticated sql injection vulnerability that allows remote attackers to inject SQL  |
| CVE-2026-111687 | 9.8 | 2026-10-16 | WeRSS (we-mp-rss) through 1.5.3 contains a remote code execution vulnerability that allows unauthenticated attackers to  |
| CVE-2026-111690 | 9.8 | 2026-10-16 | Simple Admin Core through 1.8.7 contains an authentication bypass vulnerability that allows unauthenticated attackers to |
| CVE-2026-111691 | 7.4 | 2026-10-16 | WIMOOR through commit ec86736 contains an authentication bypass vulnerability that allows attackers to impersonate any t |
| CVE-2026-111692 | 9.8 | 2026-10-16 | DataBuff ai-apm-web through 0.1.10 contains an authentication bypass vulnerability that allows unauthenticated attackers |
| CVE-2026-111693 | 9.8 | 2026-10-16 | DataBuff ai-apm-web through 0.1.10 contains a hard-coded default credentials vulnerability that allows unauthenticated a |
| CVE-2026-111695 | 7.1 | 2026-10-16 | Shaiwz data-platform-open through commit efeacd3 contains an insecure direct object reference vulnerability that allows  |
| CVE-2026-111700 | 7.1 | 2026-10-16 | WebVella ERP through 1.8.8 contains an sql injection vulnerability that allows any authenticated user to inject SQL thro |
| CVE-2026-111701 | 7.0 | 2026-10-16 | OtterMind Nubase through 0.1.4 contains a missing authentication vulnerability that allows unauthenticated attackers to  |
| CVE-2026-111702 | 7.5 | 2026-10-16 | ChatOllama through commit 96c3ce5 contains an insecure direct object reference vulnerability that allows remote attacker |
| CVE-2026-111704 | 9.8 | 2026-10-16 | LangChat through commit 2a6285a contains a missing authentication vulnerability that allows unauthenticated remote attac |
| CVE-2026-111706 | 7.5 | 2026-10-16 | 99AI through 4.3.0 contains a missing authentication vulnerability in the POST /api/chatLog/exportExcel route that allow |
| CVE-2026-111708 | 9.8 | 2026-10-16 | WhaTicket Community through commit cf04795 contains an authentication bypass vulnerability that allows unauthenticated a |
| CVE-2026-111710 | 7.5 | 2026-10-16 | Netcore NR256CN through 1.5.140116 contains a NULL pointer dereference vulnerability in the Boa web server's user_auth() |
| CVE-2026-111711 | 9.8 | 2026-10-16 | Netcore NR256CN through 1.5.140116 contains a pre-authentication stack overflow vulnerability in the Boa web server's us |
| CVE-2026-111722 | 8.1 | 2026-10-16 | LingGuo-Drama through commit 8a6924a contains an insecure direct object reference vulnerability that allows registered u |
| CVE-2026-111723 | 8.8 | 2026-10-16 | LingGuo-Drama through commit 8a6924a contains a missing authorization vulnerability that allows any registered user to m |
| CVE-2026-81452 | 7.0 | 2026-10-16 | Dell Alienware Command Center (AWCC), versions prior to 6.14.54.0, contain a Least Privilege Violation vulnerability. A  |
| CVE-2026-102917 | 7.8 | 2026-10-16 | IBM i 7.3, 7.4, 7.5, and 7.6 is vulnerable to an authenticated attacker elevating their privilege. A bad actor could exp |
| CVE-2026-102607 | 8.8 | 2026-10-16 | ZoneMinder is a free, open source closed-circuit television software application. Prior to 1.38.3, the exportEvents() fu |
| CVE-2026-102608 | 9.0 | 2026-10-16 | ZoneMinder is a free, open source closed-circuit television software application. Prior to 1.38.3, downloadEvents() manu |
| CVE-2026-102834 | 7.5 | 2026-10-16 | JavaCV provides Java interfaces to OpenCV, FFmpeg, and other multimedia libraries. Prior to 1.5.14, IPCameraFrameGrabber |
| CVE-2026-30971 | 8.8 | 2026-10-16 | ZoneMinder is a free, open source closed-circuit television software application. Prior to 1.39.2, 1.38.2, and 1.36.40,  |
| CVE-2026-59963 | 7.1 | 2026-10-16 | Tandoor Recipes is an application for managing recipes, planning meals, and building shopping lists. Prior to 2.6.10, re |
| CVE-2026-59970 | 7.7 | 2026-10-16 | Tandoor Recipes is an application for managing recipes, planning meals, and building shopping lists. Prior to 2.6.10, pa |
| CVE-2026-61726 | 8.1 | 2026-10-16 | Tandoor Recipes is an application for managing recipes, planning meals, and building shopping lists. Prior to 2.6.12, St |
| CVE-2026-108374 | 7.7 | 2026-10-16 | ERPNext is a free and open source Enterprise Resource Planning tool. Prior to 15.121.0 and 16.34.0, certain endpoints fo |
| CVE-2026-111044 | 7.6 | 2026-10-16 | Sunshine is a self-hosted game stream host for Moonlight. From 2026.329.165800 until 2026.906.222525, Sunshine accepted  |
| CVE-2026-49410 | 8.1 | 2026-10-16 | OpenHuman is an open-source agent harness available as a desktop application and Rust library. Versions before 0.56.0 al |
| CVE-2026-62439 | 7.0 | 2026-10-16 | A flaw was found in GIMP. An integer overflow occurs in the file-pvr plug-in when calculating memory buffer sizes for im |
| CVE-2026-68498 | 7.5 | 2026-10-16 | StreamReadConstraints.maxNameLength (default 50,000 characters) is intended to bound how much memory a single JSON Objec |
| CVE-2026-96626 | 8.5 | 2026-10-16 | Arcane is an interface for managing Docker containers, images, networks, and volumes. Prior to 2.5.0, UpdateRegistry and |
| CVE-2026-96627 | 8.8 | 2026-10-16 | Arcane is an interface for managing Docker containers, images, networks, and volumes. Prior to 2.6.0, UpdateUser in back |
| CVE-2026-111823 | 9.8 | 2026-10-17 | Mage OSS through 0.9.80 before 76c4f46 can proceed with session creation upon encountering an unknown OAuth provider. |
| CVE-2026-111853 | 8.8 | 2026-10-17 | An issue was discovered on Tektronix 3 Series MDO devices before 1.21.1. An OS command injection vulnerability exists in |
| CVE-2026-111854 | 8.1 | 2026-10-17 | An issue was discovered on Tektronix 3 Series MDO devices before 1.21.1. A path traversal vulnerability in the SCPI FILE |
| CVE-2026-111855 | 7.5 | 2026-10-17 | An issue was discovered on Tektronix 3 Series MDO devices before 1.21.1. A path traversal vulnerability exists in the we |
| CVE-2026-104734 | 7.2 | 2026-10-17 | The Kirki – Freeform Page Builder, Website Builder & Customizer plugin for WordPress is vulnerable to PHP Object Injecti |
| CVE-2026-107762 | 7.5 | 2026-10-17 | The Kirki – Freeform Page Builder, Website Builder & Customizer plugin for WordPress is vulnerable to Insecure Direct Ob |
| CVE-2026-109208 | 7.2 | 2026-10-17 | The LearnPress – WordPress LMS Plugin for Create and Sell Online Courses plugin for WordPress is vulnerable to Stored Cr |
| CVE-2026-110653 | 9.1 | 2026-10-17 | The Appointment Booking Plugin – LatePoint \| Calendar & Scheduling for WordPress plugin for WordPress is vulnerable to A |
| CVE-2026-103899 | 7.2 | 2026-10-17 | The EU VAT Assistant for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'vat_numb |
| CVE-2026-104736 | 9.8 | 2026-10-17 | The LearnPress plugin for WordPress is vulnerable to PHP Object Injection in versions up to, and including, 4.4.10 via d |
| CVE-2026-108123 | 7.5 | 2026-10-17 | The WP Booking System – Booking Calendar plugin for WordPress is vulnerable to authorization bypass in all versions up t |
| CVE-2026-92798 | 8.1 | 2026-10-17 | The User Registration & Membership plugin for WordPress is vulnerable to Arbitrary Shortcode Execution in versions up to |
| CVE-2026-96660 | 7.2 | 2026-10-17 | The User Registration & Membership – Free & Paid Memberships, Subscriptions, Content Restriction, User Profile, Custom U |
| CVE-2026-110384 | 7.1 | 2026-10-17 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Heateor Support Fa |
| CVE-2026-100316 | 7.2 | 2026-10-17 | The European VAT Compliance Assistant for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting  |
| CVE-2026-111110 | 7.2 | 2026-10-17 | The Payment forms, Buy now buttons, and Invoicing System \| GetPaid plugin for WordPress is vulnerable to Stored Cross-Si |
| CVE-2026-110889 | 7.5 | 2026-10-17 | Generation of Error Message Containing Sensitive Information vulnerability in Gantry Gantry 5 Framework gantry5 allows R |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-102764 | BeyondTrust / Remote Support | 2026-10-16 | 2026-10-19 | Unknown |
| CVE-2025-61624 | Fortinet / Multiple Products | 2026-10-16 | 2026-10-19 | Unknown |
| CVE-2026-21589 | Atlassian / Multiple Products | 2026-10-15 | 2026-10-18 | Unknown |
| CVE-2026-105134 | Ahsay / AhsayCBS | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-76519 | Cisco / Secure Email Gateway | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-105133 | Ahsay / AhsayCBS | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-0322 | Palo Alto Networks / PAN-OS | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-104935 | Ivanti / Connect Secure | 2026-10-13 | 2026-10-16 | Unknown |
| CVE-2026-96951 | Microsoft / Windows | 2026-10-13 | 2026-10-16 | Unknown |

---

*Total entries in CISA KEV catalog: 1748*