# Vulnerability Intelligence Report

**Date:** 2026-11-09  
**Generated:** 2026-11-09T18:20:31Z  

---

## Executive Summary

Our environment faces significant exposure across 90 high-severity vulnerabilities, including a critical CVSS 9.8 OS command injection in IBM Concert and multiple remote code execution and account takeover flaws. Six new CISA Known Exploited Vulnerabilities (KEVs) were added in the past seven days, including actively exploited flaws in OpenSSH and SonicWall SSLVPN, indicating heightened threat actor activity. While no monitored CVEs currently overlap with the KEV catalog, the breadth of high-severity findings—spanning identity systems, storage, and integration platforms—represents serious business risk requiring immediate prioritization and remediation action.

---

## Risk Narrative

Threat actors are actively exploiting vulnerabilities in widely deployed infrastructure components including OpenSSH, SonicWall VPN, and Apple products, as confirmed by recent CISA KEV additions. The presence of a CVSS 9.8 command injection flaw alongside multiple CVSS 8+ authentication and session vulnerabilities significantly elevates the risk of full system compromise, data exfiltration, and lateral movement. Identity and access management platforms under threat amplify the blast radius of any breach. Organizations in this landscape face elevated risk of ransomware, espionage, and operational disruption, particularly if patch cycles are delayed or legacy systems remain unmitigated.

---

## Prioritized Action Items

1. Immediately patch IBM Concert (CVE-2026-6715, CVSS 9.8) to eliminate the critical OS command injection vulnerability allowing unauthenticated remote code execution.
2. Apply emergency mitigations or patches for SonicWall SSLVPN and OpenSSH KEV entries, as these are confirmed actively exploited in the wild.
3. Remediate session fixation and authentication bypass vulnerabilities in IBM Security Verify Directory and IBM webMethods Integration Server to prevent unauthorized access and privilege escalation.
4. Address remote code execution risks in IBM Bob and IBM Langflow OSS by updating to vendor-patched versions and restricting write permissions on affected service accounts.
5. Establish a continuous KEV monitoring process to automatically alert when any internal asset CVEs appear in the CISA catalog, reducing response lag to under 24 hours.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-18893 | 7.1 | 2026-11-08 | IBM CockroachDB PostgreSQL for IBM VPC 26.2.0 through 26.2.3, 25.4.0 through 25.4.12, and 25.2.0 through 25.2.20 is vuln |
| CVE-2026-19133 | 8.1 | 2026-11-08 | IBM Storage TS4500 Library 1.1.1.6 through 1.12.0.3 could allow a remote authenticated attacker to perform unauthorized  |
| CVE-2026-6715 | 9.8 | 2026-11-08 | IBM Concert 1.0 through 3.0.1.1 allows an attacker can supply crafted input that is incorporated into an operating syste |
| CVE-2026-8639 | 8.8 | 2026-11-08 | IBM Security Verify Directory 10.0.0 through 10.0.4 and IBM Verify Directory 11.0.0 is vulnerable to session fixation. A |
| CVE-2026-93879 | 7.5 | 2026-11-08 | Hibernate Validator could allow a remote attacker to cause a denial of service due to uncontrolled resource consumption  |
| CVE-2026-97677 | 8.1 | 2026-11-08 | IBM Langflow OSS 1.0.0 through 1.12.2 An authenticated flow author could write attacker-controlled file content into any |
| CVE-2026-9764 | 8.8 | 2026-11-08 | IBM Bob 1.0.4 through 2.0.1 could allow a remote attacker to inject arbitrary code on the system, due to the improper co |
| CVE-2026-118904 | 8.1 | 2026-11-08 | IBM webMethods Integration Server 12.1 could allow a remote authenticated attacker to bypass security restrictions due t |
| CVE-2026-96146 | 7.5 | 2026-11-08 | IBM SevOne Network Performance Management 7.0.0 through 8.2.2 could allow a remote attacker to cause a denial of service |
| CVE-2026-124501 | 7.3 | 2026-11-09 | A weakness has been identified in Tidelift moto up to 5.2.4. Affected is an unknown function of the file moto/batch/mode |
| CVE-2026-119506 | 9.1 | 2026-11-09 | Incorrect Privilege Assignment vulnerability in DynamiApps Frontend Admin by DynamiApps acf-frontend-form-element allows |
| CVE-2026-124509 | 7.3 | 2026-11-09 | A vulnerability was identified in floci-io Floci up to 2.1.0. The affected element is the function S3Destination.bucketN |
| CVE-2026-124554 | 7.3 | 2026-11-09 | A security flaw has been discovered in JeecgBoot 3.9.5. This affects an unknown part of the file /jeecg-boot/drag/onlDra |
| CVE-2026-124557 | 7.3 | 2026-11-09 | A vulnerability was detected in OtterMind Chat2DB up to 5.3.8. Impacted is the function DbMybatisGenerateServiceImpl.gen |
| CVE-2026-124558 | 7.3 | 2026-11-09 | A vulnerability has been found in DataLinkDC Dinky up to 1.2.5. The impacted element is the function SqlGateway.onOpen o |
| CVE-2026-124560 | 9.8 | 2026-11-09 | A vulnerability was found in D-Link DIR-878 1.20B05. This affects the function GetCAPTCHAsetting of the file bin/prog.cg |
| CVE-2026-124561 | 7.5 | 2026-11-09 | A vulnerability was determined in D-Link DIR-878 1.20B05. This impacts the function SetVLANSettings of the file prog.cgi |
| CVE-2026-124562 | 7.5 | 2026-11-09 | A vulnerability was identified in D-Link DIR-878 1.20B05. Affected is the function SetWanSettings of the component HNAP  |
| CVE-2026-124563 | 7.5 | 2026-11-09 | A security flaw has been discovered in D-Link DIR-878 1.20B05. Affected by this vulnerability is the function SetWanSett |
| CVE-2026-115204 | 8.8 | 2026-11-09 | The AZEXO Store Locator WordPress plugin through 1.4 does not perform capability or nonce checks on its AJAX actions and |
| CVE-2026-115212 | 8.8 | 2026-11-09 | The mView 豆瓣电影 WordPress plugin through 1.0.3 does not validate the type, name, or source of a remotely fetched file, no |
| CVE-2026-115213 | 9.8 | 2026-11-09 | The EASY-JS-WPAPI Client HANDLE for the WordPress REST-API WordPress plugin through 2.0 does not prevent the administrat |
| CVE-2026-115237 | 9.8 | 2026-11-09 | The Grand Job WordPress plugin through 1.2.1 does not correctly verify the password reset code before updating a user's  |
| CVE-2026-115256 | 7.5 | 2026-11-09 | The Mail Debug for WooCommerce WordPress plugin through 1.3.0 does not perform any capability, authentication, or nonce  |
| CVE-2026-118201 | 7.5 | 2026-11-09 | The Limit Login Attempts Security  WordPress plugin before 3.4.1 does not enforce its two-factor authentication on every |
| CVE-2026-118202 | 7.5 | 2026-11-09 | The Limit Login Attempts Security  WordPress plugin before 3.4.1 does not confirm that its two-factor authentication ste |
| CVE-2026-121874 | 7.2 | 2026-11-09 | The Post Duplicator WordPress plugin before 3.0.18 does not restrict settings saves to its own options, allowing a site  |
| CVE-2026-121875 | 7.2 | 2026-11-09 | The Post Duplicator WordPress plugin before 3.0.18 does not validate the capabilities assigned to roles through its perm |
| CVE-2026-123064 | 8.8 | 2026-11-09 | The WP BASE Booking of Appointments, Services and Events WordPress plugin before 6.5.1 does not properly restrict access |
| CVE-2026-123091 | 7.5 | 2026-11-09 | The Vigilant  WordPress plugin before 2.11.0 does not enforce its two-factor authentication on login forms other than th |
| CVE-2026-123751 | 9.8 | 2026-11-09 | The WP Duplicate  WordPress plugin through 1.1.11 does not properly verify a request authentication value and does not v |
| CVE-2026-124573 | 7.3 | 2026-11-09 | A vulnerability was found in logseq 2.0.1/2.0.2. This affects the function validate-auth-token of the file src/electron/ |
| CVE-2026-124576 | 7.3 | 2026-11-09 | A security flaw has been discovered in BeikeShop up to 2.0.0.31. Impacted is the function OrderRepo::getOrderByNumber of |
| CVE-2026-124577 | 9.8 | 2026-11-09 | A weakness has been identified in Intelbras SG 2404 PoE L2+ 1.00.70/1.00.72. The affected element is an unknown function |
| CVE-2026-124579 | 7.4 | 2026-11-09 | A vulnerability was determined in aaPanel BillionMail up to 4.9. Affected by this issue is some unknown functionality of |
| CVE-2026-124580 | 10.0 | 2026-11-09 | A vulnerability was found in Chengdu Feiyuxing Technology VW2100 and VEC10GP 1.0 B-MB3W202-210825-r11775. This impacts t |
| CVE-2026-124581 | 7.3 | 2026-11-09 | A vulnerability was determined in itsourcecode Airline Reservation System 1.0. Affected is an unknown function of the fi |
| CVE-2026-124585 | 9.9 | 2026-11-09 | A vulnerability was found in Chengdu Feiyuxing Technology VW2100 and VEC10GP 1.0 B-MB3W202-210825-r11775. This issue aff |
| CVE-2026-94249 | 8.1 | 2026-11-09 | Missing Authorization vulnerability in TÜBİTAK BİLGEM Software Technologies Research Institute Liderahenk allows Privile |
| CVE-2026-111403 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Inventory WP In |
| CVE-2026-111421 | 8.8 | 2026-11-09 | Apache Airflow's Task Execution API stored XCom values written by a task without the reserved-key check applied elsewher |
| CVE-2026-119483 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in 10Web Form Maker b |
| CVE-2026-119504 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in DynamiApps Fronten |
| CVE-2026-119505 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Welcart Welcart e- |
| CVE-2026-121760 | 7.5 | 2026-11-09 | Missing Authorization vulnerability in weDevs weDocs wedocs allows Exploiting Incorrectly Configured Access Control Secu |
| CVE-2026-121764 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in FolioVision FV Flo |
| CVE-2026-121780 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Gijo Varghese Flyi |
| CVE-2026-123463 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Wham Checkout F |
| CVE-2026-123465 | 7.5 | 2026-11-09 | Exposure of Sensitive System Information to an Unauthorized Control Sphere vulnerability in myCred myCred mycred allows  |
| CVE-2026-123484 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Crocoblock JetForm |
| CVE-2026-124586 | 7.3 | 2026-11-09 | A vulnerability was determined in Tencent RapidJSON 1.1.0. Impacted is the function GetCachedPowerByIndex in the library |
| CVE-2026-54863 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Mamunur Rashid Rev |
| CVE-2026-106466 | 7.5 | 2026-11-09 | The JWT Auth WordPress plugin through 3.0.2 does not invalidate previously issued refresh tokens when a user changes or  |
| CVE-2026-115252 | 10.0 | 2026-11-09 | The Confection WordPress Cable WordPress plugin from 0.4.0 to 0.4.7 does not perform any capability or nonce checks befo |
| CVE-2026-120367 | 7.5 | 2026-11-09 | Allocation of Resources Without Limits or Throttling vulnerability in Apache Axis2/Java. The JSON message builders, incl |
| CVE-2026-121570 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Chill RSVP and  |
| CVE-2026-121722 | 7.5 | 2026-11-09 | Missing Authorization vulnerability in WP E-Signature Formidable Forms Signature Online Contract Automation forms-signat |
| CVE-2026-121782 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in If-So Dynamic Cont |
| CVE-2026-122666 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Kitae Park Mang Bo |
| CVE-2026-123460 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Nickboss WordPress |
| CVE-2026-123475 | 7.5 | 2026-11-09 | Missing Authorization vulnerability in PT Norther Lights Production MapSVG mapsvg-lite-interactive-vector-maps allows Ex |
| CVE-2026-123476 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in fifu.app Featured  |
| CVE-2026-124590 | 7.3 | 2026-11-09 | A security vulnerability has been detected in zhangbw409 library_manager_system f6c9d9c96bf5d2a32ef741daeaa29d80e6db166b |
| CVE-2026-124621 | 7.4 | 2026-11-09 | A vulnerability was determined in kongxin-github Java_Library_Management_System up to 70a6eb6b96fe64575d8051f1a59055bfc5 |
| CVE-2026-121629 | 7.5 | 2026-11-09 | A flaw was found in GStreamer's adaptive streaming demuxers (HLS, DASH, MSS). When processing a media playlist or manife |
| CVE-2026-119610 | 8.2 | 2026-11-09 | A flaw was found in GStreamer's gst-plugins-good, specifically in the H.264 RTP depayloader element. When processing MTA |
| CVE-2026-120854 | 7.5 | 2026-11-09 | Allocation of Resources Without Limits or Throttling vulnerability in iubenda iubenda iubenda-cookie-law-solution allows |
| CVE-2026-120856 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Rymera Web Co Invo |
| CVE-2026-124079 | 9.8 | 2026-11-09 | rConfig Core 8.0.0 before 8.2.19 and rConfig Pro before 8.4.1 contain a deserialization of untrusted data vulnerability  |
| CVE-2026-94434 | 8.8 | 2026-11-09 | Improper neutralization of special elements used in an OS command ('OS command injection') vulnerability in TÜBİTAK BİLG |
| CVE-2026-95648 | 8.1 | 2026-11-09 | Improperly controlled modification of Dynamically-Determined object attributes vulnerability in C-Prot Inc. C-Prot AppDe |
| CVE-2026-121842 | 8.8 | 2026-11-09 | Privilege escalation in the Reader View component in Firefox for iOS. This vulnerability was fixed in Firefox for iOS 16 |
| CVE-2026-121843 | 8.8 | 2026-11-09 | Privilege escalation in Firefox for iOS. This vulnerability was fixed in Firefox for iOS 160.0. |
| CVE-2026-16283 | 8.8 | 2026-11-09 | Improper neutralization of special elements used in an OS command ('OS command injection') vulnerability in Osbil Techno |
| CVE-2026-95778 | 8.8 | 2026-11-09 | A remote code execution vulnerability exists in HPE Morpheus Software. |
| CVE-2026-95779 | 8.8 | 2026-11-09 | An exposure of the appliance’s confidential certificate  information 
vulnerability exists in HPE Morpheus manager softw |
| CVE-2026-119474 | 7.8 | 2026-11-09 | Incorrect Permission Assignment for Critical Resource vulnerability in HAVELSAN Inc. Liman Render Engine allows Privileg |
| CVE-2026-115338 | 8.1 | 2026-11-09 | Insufficient protection of communications in Progress WS_FTP Server versions prior to 2025.0.5 could allow a network att |
| CVE-2026-115339 | 7.5 | 2026-11-09 | Insufficient resource limits in Progress Software WS_FTP Server releases prior to 2025.0.5 on Windows could allow an una |
| CVE-2026-115340 | 7.1 | 2026-11-09 | Progress Software WS_FTP Server versions prior to 2025.0.5 on Windows may write sensitive user credential and session da |
| CVE-2026-115341 | 7.7 | 2026-11-09 | Improper access restrictions in the Thin Client Web Transfer component of Progress Software WS_FTP Server versions prior |
| CVE-2026-121576 | 8.8 | 2026-11-09 | Incorrect Privilege Assignment vulnerability in AtlasAiDev MCP Server for WordPress ai-workflow-automation-ai-agent-hub  |
| CVE-2026-122664 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in VideoWhisper.com B |
| CVE-2026-123482 | 7.1 | 2026-11-09 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Crocoblock JetForm |
| CVE-2026-119755 | 7.5 | 2026-11-09 | Tasmota through 16.0.0, fixed in commit 1cb7ebc, contains a cross-site request forgery vulnerability that allows unauthe |
| CVE-2026-119756 | 9.8 | 2026-11-09 | Tasmota through 16.0.0, fixed in commit e97e1e4, contains a heap out-of-bounds write vulnerability in SendReceiveDeviceG |
| CVE-2026-123270 | 9.8 | 2026-11-09 | Redpanda Connect versions 4.39 to 4.110 contain a missing authentication vulnerability that enables unauthenticated remo |
| CVE-2026-123367 | 7.4 | 2026-11-09 | Thor Vector Graphics (ThorVG) is a production-ready vector graphics engine. Prior to 1.1.2, the bundled jpgd JPEG decode |
| CVE-2026-123797 | 7.5 | 2026-11-09 | SuperTokens Core is an open source authentication server. Prior to 11.3.6, 11.4.6, and 12.0.8, app-specific management r |
| CVE-2026-19706 | 8.3 | 2026-11-09 | During ABI bootstrap, the bootstrap node's approve-csr.service approves and signs every CSR without identity validation. |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-102895 | GPUStack / GPUStack | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-123158 | OpenBSD / OpenSSH | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-116779 | SignalWire / FreeSwitch | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-19868 | SonicWall / SonicOS SSLVPN | 2026-11-06 | 2026-11-20 | Unknown |
| CVE-2024-27834 | Apple / Multiple Products | 2026-11-04 | 2026-11-18 | Unknown |
| CVE-2026-119977 | WordPress / WordPress Core | 2026-11-03 | 2026-11-06 | Unknown |

---

*Total entries in CISA KEV catalog: 1772*