# Vulnerability Intelligence Report

**Date:** 2026-10-27  
**Generated:** 2026-10-27T14:00:29Z  

---

## Executive Summary

Our environment faces significant exposure from 142 high-severity vulnerabilities, including critical flaws in Fortinet FortiSandbox, Mautic, NexoPOS, and MacCMS. Top concerns include authentication bypasses, unrestricted file uploads, and remote code execution vectors with CVSS scores reaching 9.9. Additionally, 10 new entries were added to the CISA Known Exploited Vulnerabilities catalog this week, signaling active threat actor interest in similar platforms. Immediate remediation and enhanced monitoring are required to prevent potential breaches, data exfiltration, or full system compromise.

---

## Risk Narrative

The current threat landscape reflects a surge in exploitation of web application and network security platforms. Authentication bypasses and remote code execution vulnerabilities in widely deployed tools like Fortinet FortiSandbox and Mautic represent immediate business risks, including unauthorized access to sensitive data, full system compromise, and operational disruption. The addition of 10 CVEs to the CISA KEV catalog within seven days underscores active exploitation in the wild. Organizations running PHP-based applications or Arista network infrastructure face heightened urgency. Failure to act swiftly could expose customer data, violate compliance obligations, and result in significant financial and reputational harm.

---

## Prioritized Action Items

1. Patch Fortinet FortiSandbox immediately across all affected versions (4.4.0–5.0.6) to remediate the critical authentication bypass vulnerability (CVE-2026-107656).
2. Remediate all critical Mautic vulnerabilities (CVE-2026-115188 through CVE-2026-115193), prioritizing the CVSS 9.9 unrestricted file upload flaw enabling remote code execution.
3. Apply available patches or mitigations for NexoPOS v6.2.4 and MacCMS v10 to address directory traversal and authentication bypass vulnerabilities rated CVSS 9.8 and 9.1.
4. Audit and restrict API access for Dolibarr ERP CRM and review all authenticated user permissions to limit SQL injection exposure (CVE-2026-116218).
5. Review the 10 newly added CISA KEV entries, particularly PHP Group PHP and Arista VeloCloud CVEs, and confirm whether any affected products exist in the environment.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-107092 | 9.8 | 2026-10-26 | NexoPOS v6.2.4 is vulnerable to Directory Traversal via the api/update endpoint. |
| CVE-2026-107656 | 9.8 | 2026-10-26 | An authentication bypass using an alternate path or channel vulnerability in Fortinet FortiSandbox 5.0.0 through 5.0.6,  |
| CVE-2026-115188 | 9.9 | 2026-10-26 | An unrestricted file upload vulnerability exists in the campaign import feature of Mautic 7. When processing an uploaded |
| CVE-2026-115189 | 8.8 | 2026-10-26 | A server-side template injection vulnerability exists in the Twig theme rendering sandbox of Mautic. The sandbox introdu |
| CVE-2026-115190 | 8.0 | 2026-10-26 | An insecure deserialization (PHP object injection) vulnerability exists in Mautic's handling of segment filters and cust |
| CVE-2026-115191 | 7.1 | 2026-10-26 | A SQL injection vulnerability exists in a contact lookup AJAX endpoint of the Mautic administration interface (/s/ajax). |
| CVE-2026-115192 | 7.1 | 2026-10-26 | An SQL Injection vulnerability exists in the dashboard widget data API endpoint (/api/data/{type}). Chart filter paramet |
| CVE-2026-115193 | 8.2 | 2026-10-26 | A stored Cross-Site Scripting (XSS) vulnerability exists in the contact detail view of Mautic 7. Values of HTML-type cus |
| CVE-2026-116214 | 9.1 | 2026-10-26 | MacCMS v10 before 2026.1000.4054 contains an authentication bypass vulnerability that allows unauthenticated attackers t |
| CVE-2026-116218 | 7.6 | 2026-10-26 | Dolibarr ERP CRM 19.0.0 before 23.0.4 contains an SQL injection vulnerability that allows authenticated API users to inj |
| CVE-2026-116219 | 7.2 | 2026-10-26 | Dolibarr ERP CRM before 24.0.0 contains an OS command injection vulnerability in htdocs/admin/tools/export.php that lets |
| CVE-2026-116485 | 9.8 | 2026-10-26 | danmu_api before 1.21.7 contains an authentication bypass vulnerability that allows unauthenticated attackers to modify  |
| CVE-2026-59106 | 9.8 | 2026-10-26 | A security vulnerability has been identified in the WolfProt interface implementation. Insufficient neutralization of us |
| CVE-2026-59107 | 9.8 | 2026-10-26 | A security vulnerability has been identified in the vSolution Matrix file sharing feature. A shared cryptographic trust  |
| CVE-2026-112345 | 8.1 | 2026-10-26 | TTLock Android application before v9.8.260718 and associated smart-lock firmware contain a hardcoded static AES key vuln |
| CVE-2026-116339 | 7.3 | 2026-10-26 | A vulnerability was determined in iFlytek astron-agent up to 1.1.2. This affects an unknown function of the file core/me |
| CVE-2026-65184 | 9.8 | 2026-10-26 | The root-privileged `wsserver` terminal-bridge daemon builds a shell command from client-supplied WebSocket fields and p |
| CVE-2026-90885 | 7.5 | 2026-10-26 | Improper Restriction of XML External Entity Reference vulnerability in Apache Camel Saxon component.



This issue affec |
| CVE-2026-112343 | 8.1 | 2026-10-26 | Syncplify Server! before 8.8.0 contains an access control bypass vulnerability that allows authenticated SFTP users to e |
| CVE-2026-112346 | 9.8 | 2026-10-26 | OpenHands Software Agent SDK before 1.52.0 contains an unauthenticated remote code execution vulnerability where the Doc |
| CVE-2026-115721 | 7.5 | 2026-10-26 | **UNSUPPORTED WHEN ASSIGNED**  Unbounded allocation in XML parsing in Apache Vysper; all versions, may lead to an out of |
| CVE-2026-115748 | 8.8 | 2026-10-26 | **UNSUPPORTED WHEN ASSIGNED**  Authorization bypass in Apache Vysper, all versions.




Apache Vysper is an XMPP (Jabber |
| CVE-2026-116368 | 7.3 | 2026-10-26 | A vulnerability was determined in DeepSeek Harness up to 0.2.0-rc.2. This issue affects some unknown processing of the f |
| CVE-2026-116489 | 7.5 | 2026-10-26 | Timescale pgvectorscale before 0.9.1 contains a type confusion vulnerability that allows low-privileged database users t |
| CVE-2026-116543 | 7.5 | 2026-10-26 | Open5GS 1.3.0 through 2.8.0 contains a heap out-of-bounds write vulnerability in parse_multipart() that allows unauthent |
| CVE-2026-115418 | 7.3 | 2026-10-26 | SQL injection in the database-query custom resource handlers in the Amazon Web Services (AWS) Cloud Development Kit (CDK |
| CVE-2026-115907 | 7.5 | 2026-10-26 | zip is a zip library for Rust that supports reading and writing simple ZIP files. From 5.1.0 until 9.0.0, applications b |
| CVE-2026-115908 | 7.4 | 2026-10-26 | zip is a zip library for Rust that supports reading and writing simple ZIP files. From 7.2.0 until 9.0.0, ZipArchive::ex |
| CVE-2026-115909 | 7.5 | 2026-10-26 | zip is a zip library for Rust that supports reading and writing simple ZIP files. From 1.3.0 until 9.0.0, ZipArchive::ex |
| CVE-2026-115912 | 7.5 | 2026-10-26 | vLLM is an inference and serving engine for large language models. Prior to 0.32.0, an authenticated caller can place fo |
| CVE-2026-116612 | 7.8 | 2026-10-26 | A flaw was found in GStreamer Editing Services (gst-editing-services). A GES project file can embed an arbitrary GStream |
| CVE-2026-81038 | 7.1 | 2026-10-26 | The Object Transfer Service server builds its Object Action Control Point (OACP) response indication in oacp_ind_send()  |
| CVE-2026-102649 | 9.9 | 2026-10-26 | Burrito is a Terraform Automation Collaboration Software (TACoS) Kubernetes operator. Prior to 0.13.0, `POST /api/webhoo |
| CVE-2026-105608 | 8.8 | 2026-10-26 | HashiCorp Consul and Consul Enterprise are vulnerable to an authorization bypass in service mesh proxy registration. Thi |
| CVE-2026-105626 | 7.5 | 2026-10-26 | HashiCorp Consul and Consul Enterprise are vulnerable to a denial of service in the HTTP API that may allow an unauthent |
| CVE-2026-105765 | 7.5 | 2026-10-26 | HashiCorp Consul and Consul Enterprise 1.17.0 up to 2.0.4 are vulnerable to an authorization bypass in the agent's servi |
| CVE-2026-10757 | 9.8 | 2026-10-26 | There is a SQL injection vulnerability in Esri ArcGIS Server versions 12.1 and earlier on Windows and Linux that may all |
| CVE-2026-115915 | 8.1 | 2026-10-26 | vLLM is an inference and serving engine for large language models. Prior to 0.32.0, ImageMediaIO passes attacker-control |
| CVE-2026-33521 | 7.5 | 2026-10-26 | There is s denial of service vulnerability in Esri ArcGIS Server versions 12.0 and prior that may allow a remote, unauth |
| CVE-2026-72753 | 8.2 | 2026-10-26 | When Routinator encounters an RRDP notification file with gaps in the delta entries, it is still accepted and parsed, po |
| CVE-2026-72754 | 7.5 | 2026-10-26 | When Routinator encounters a CRL with many entries, it may hang or run out of memory. If Routinator encounters a CRL fil |
| CVE-2026-72756 | 7.5 | 2026-10-26 | Routinator exits when an rsync URI for a file obtained over RRDP contains a path that cannot be stored on disk, such as  |
| CVE-2026-72758 | 7.5 | 2026-10-26 | When parsing an AS range in Routinator, if the maximum value of the range is smaller than the minimum value of the range |
| CVE-2026-110720 | 9.9 | 2026-10-26 | Consul-k8s versions 0.42.0 and later are vulnerable to a cross-namespace authorization bypass in component ACL binding r |
| CVE-2014-125135 | 7.3 | 2026-10-26 | A security vulnerability has been detected in OctoPrint 1.0.0/1.1.0. Affected is an unknown function of the component Fl |
| CVE-2026-115924 | 8.6 | 2026-10-26 | Rembg is a tool to remove images background. Prior to 2.0.82, the public /api/remove endpoint passes attacker-controlled |
| CVE-2026-112427 | 8.1 | 2026-10-26 | An authentication issue was addressed with improved state management. This issue is fixed in macOS Golden Gate 27.2. A r |
| CVE-2026-112438 | 8.8 | 2026-10-26 | A logic issue was addressed with improved state management. This issue is fixed in macOS Golden Gate 27.2, macOS Sequoia |
| CVE-2026-112457 | 7.1 | 2026-10-26 | A double free issue was addressed with improved memory management. This issue is fixed in macOS Golden Gate 27.2, macOS  |
| CVE-2026-112484 | 7.8 | 2026-10-26 | This issue was addressed with improved file handling. This issue is fixed in macOS Golden Gate 27.2, macOS Sequoia 15.8. |
| CVE-2026-112623 | 8.8 | 2026-10-26 | A use-after-free issue was addressed with improved memory management. This issue is fixed in Safari 27.2, iOS 26.7.2 and |
| CVE-2026-112626 | 8.8 | 2026-10-26 | A use-after-free issue was addressed with improved memory management. This issue is fixed in Safari 27.2, iOS 26.7.2 and |
| CVE-2026-112637 | 8.8 | 2026-10-26 | A use-after-free issue was addressed with improved memory management. This issue is fixed in Safari 27.2, iOS 27.2 and i |
| CVE-2026-112651 | 8.8 | 2026-10-26 | A use-after-free issue was addressed with improved memory management. This issue is fixed in Safari 27.2, iOS 26.7.2 and |
| CVE-2026-112655 | 8.8 | 2026-10-26 | A use-after-free issue was addressed with improved memory management. This issue is fixed in Safari 27.2, iOS 26.7.2 and |
| CVE-2026-112659 | 8.8 | 2026-10-26 | A type confusion issue was addressed with improved memory handling. This issue is fixed in Safari 27.2, iOS 26.7.2 and i |
| CVE-2026-112688 | 8.8 | 2026-10-26 | A memory corruption issue was addressed with improved memory handling. This issue is fixed in iOS 26.7 and iPadOS 26.7,  |
| CVE-2026-113947 | 8.8 | 2026-10-26 | This issue was addressed with improved access restrictions. This issue is fixed in macOS Golden Gate 27.2. Unpacking a m |
| CVE-2026-116504 | 9.9 | 2026-10-26 | A vulnerability has been found in TOTOLINK A950RG 4.1.2cu.5268_B20221104. This affects the function setCloudUpgradeFW of |
| CVE-2026-116505 | 9.1 | 2026-10-26 | A vulnerability was found in TOTOLINK A950RG 4.1.2cu.5268_B20221104. This impacts the function getDeviceInfo of the file |
| CVE-2026-116506 | 9.9 | 2026-10-26 | A vulnerability was determined in TOTOLINK A950RG 4.1.2cu.5268_B20221104. Affected is the function apmib_set of the file |
| CVE-2026-116576 | 7.8 | 2026-10-26 | systeminformation is a System and OS information library for node.js. Prior to 5.33.16, services() in lib/processes.js i |
| CVE-2026-116580 | 7.3 | 2026-10-26 | Seroval facilitates JavaScript value stringification, including complex structures beyond JSON.stringify capabilities. P |
| CVE-2026-116581 | 7.5 | 2026-10-26 | Seroval facilitates JavaScript value stringification, including complex structures beyond JSON.stringify capabilities. P |
| CVE-2026-116584 | 7.5 | 2026-10-26 | Seroval facilitates JavaScript value stringification, including complex structures beyond JSON.stringify capabilities. F |
| CVE-2026-64759 | 8.8 | 2026-10-26 | An integer overflow was addressed with improved input validation. This issue is fixed in iOS 26.7.2 and iPadOS 26.7.2, i |
| CVE-2026-65327 | 8.4 | 2026-10-26 | A logic issue was addressed with improved checks. This issue is fixed in macOS Golden Gate 27.2, macOS Sequoia 15.8.2, m |
| CVE-2026-86916 | 7.8 | 2026-10-26 | A use after free issue was addressed with improved memory management. This issue is fixed in iOS 26.7 and iPadOS 26.7, i |
| CVE-2026-86929 | 8.8 | 2026-10-26 | An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in macOS Golden Gate 27, m |
| CVE-2026-116508 | 10.0 | 2026-10-26 | A security flaw has been discovered in TOTOLINK A950RG 4.1.2cu.5268_B20221104. Affected by this issue is the function su |
| CVE-2026-116587 | 7.5 | 2026-10-26 | Go JOSE provides an implementation of the Javascript Object Signing and Encryption set of standards in Go, including sup |
| CVE-2026-116723 | 7.8 | 2026-10-26 | FLTK through 1.4.5 contains a stack-based buffer overflow vulnerability in Fl_BMP_Image::load_bmp_() that allows attacke |
| CVE-2026-116724 | 7.8 | 2026-10-26 | FLTK through 1.4.5 contains an integer overflow vulnerability in Fl_BMP_Image::load_bmp_() that causes undersized pixel  |
| CVE-2026-116738 | 8.8 | 2026-10-26 | VMime through 0.9.2 contains an integer underflow in the uuEncoder::decode function that allows remote attackers to trig |
| CVE-2026-116747 | 8.1 | 2026-10-26 | Kener 3.0.0 before 4.1.10 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge |
| CVE-2026-116748 | 8.8 | 2026-10-26 | Transmission 4.0.0 before 4.1.3 contains a permissive CORS vulnerability in handle_request() in rpc-server.cc that expos |
| CVE-2026-116808 | 7.2 | 2026-10-27 | OpenPanel before 3.0.0 contains an sql injection vulnerability that allows authenticated users to read cross-tenant data |
| CVE-2026-116811 | 8.8 | 2026-10-27 | OpenPanel before 3.0.0 contains a sandbox escape vulnerability in the js-runtime validator that allows a project member  |
| CVE-2026-116818 | 8.2 | 2026-10-27 | OpenPanel before 3.0.0 contains an unauthenticated ClickHouse sql injection vulnerability that allows remote attackers t |
| CVE-2026-116819 | 8.5 | 2026-10-27 | OpenPanel before 3.0.0 contains an information disclosure vulnerability that allows read-level project members to obtain |
| CVE-2024-58400 | 8.2 | 2026-10-27 | llama.cpp before b3701 contains an out-of-bounds read vulnerability in llama_decode_internal and llama_encode_internal t |
| CVE-2026-116620 | 7.3 | 2026-10-27 | A security vulnerability has been detected in Tencent RapidJSON up to 1.1.0. This issue affects the function GenericStri |
| CVE-2026-116623 | 7.3 | 2026-10-27 | A vulnerability was detected in code-projects Simple Content Management System 1.0. Impacted is an unknown function of t |
| CVE-2026-116816 | 7.8 | 2026-10-27 | llama.cpp b5899 before b10261 contains a heap out-of-bounds write vulnerability in llm_tokenizer_plamo2::build that allo |
| CVE-2026-116836 | 8.8 | 2026-10-27 | A malicious actor with access to the adjacent network and under certain conditions could exploit a Stored Cross-Site Scr |
| CVE-2026-116837 | 8.8 | 2026-10-27 | A malicious actor with access to the adjacent network could exploit a Heap-based Buffer Overflow vulnerability found in  |
| CVE-2026-116838 | 8.8 | 2026-10-27 | A malicious actor who lures an authenticated user to a malicious page could exploit a Cross-Site Request Forgery (CSRF)  |
| CVE-2026-116839 | 7.1 | 2026-10-27 | A malicious actor who lures an authenticated user to a malicious page could exploit a Cross-Site Request Forgery (CSRF)  |
| CVE-2026-116843 | 8.8 | 2026-10-27 | Mistral Vibe before 3.0.3 contains a remote code execution vulnerability that allows attackers to run commands by defini |
| CVE-2026-111820 | 7.2 | 2026-10-27 | The Analytics Insights – Google Analytics Dashboard for WordPress plugin for WordPress is vulnerable to Stored Cross-Sit |
| CVE-2026-106174 | 7.5 | 2026-10-27 | A improper locking vulnerability in Fortinet FortiOS 8.0.0, FortiOS 7.6.4 through 7.6.6 may allow an unauthenticated att |
| CVE-2026-75891 | 8.8 | 2026-10-27 | The Kirki plugin for WordPress is vulnerable to Privilege Escalation via PHP Object Injection in all versions up to, and |
| CVE-2026-16521 | 7.2 | 2026-10-27 | An OS command injection vulnerability exists because of insufficient input filtering. An attacker can inject a command p |
| CVE-2026-18449 | 7.5 | 2026-10-27 | The BMC does not correctly enforce integrity and encryption requirements for IPMI commands. An attacker may be able to c |
| CVE-2026-18450 | 9.8 | 2026-10-27 | The BMC does not correctly enforce integrity and encryption requirements for IPMI commands. An attacker may be able to c |
| CVE-2026-65219 | 7.4 | 2026-10-27 | A flaw in the BMC RAKP+ implementation may allow an attacker to send a request followed by a specially crafted RAKP mess |
| CVE-2026-65220 | 8.8 | 2026-10-27 | A logic flaw in the BMC IPMI implementation may allow an attacker to send specially crafted RAKP+ messages and escalate  |
| CVE-2026-65211 | 7.2 | 2026-10-27 | This issue may allow an authenticated IPMI Administrator to read and write arbitrary BMC physical memory and thereby exe |
| CVE-2026-92885 | 9.8 | 2026-10-27 | The Qode Membership plugin for WordPress is vulnerable to Authentication Bypass leading to Account Takeover in all versi |
| CVE-2026-76932 | 9.4 | 2026-10-27 | Stack-based Buffer Overflow Vulnerability in JP1/Automatic Job Management System 3.

This issue affects JP1/Automatic Jo |
| CVE-2026-76933 | 9.4 | 2026-10-27 | Heap-based Buffer Overflow Vulnerability in JP1/Automatic Job Management System 3.

This issue affects JP1/Automatic Job |
| CVE-2026-76934 | 9.8 | 2026-10-27 | Stack-based Buffer Overflow Vulnerability in JP1/Automatic Job Management System 3.

This issue affects JP1/Automatic Jo |
| CVE-2026-76935 | 9.4 | 2026-10-27 | Stack-based Buffer Overflow Vulnerability in JP1/Automatic Job Management System 3.


This issue affects JP1/Automatic J |
| CVE-2026-76936 | 9.4 | 2026-10-27 | Stack-based Buffer Overflow Vulnerability in JP1/Automatic Job Management System 3.


This issue affects JP1/Automatic J |
| CVE-2026-76937 | 9.4 | 2026-10-27 | Heap-based Buffer Overflow Vulnerability in JP1/Automatic Job Management System 3.


This issue affects JP1/Automatic Jo |
| CVE-2026-76938 | 9.8 | 2026-10-27 | Authentication Bypass Vulnerability in JP1/Automatic Job Management System 3.


This issue affects JP1/Automatic Job Man |
| CVE-2026-76939 | 9.8 | 2026-10-27 | Heap-based Buffer Overflow Vulnerability in JP1/Automatic Job Management System 3.

This issue affects JP1/Automatic Job |
| CVE-2026-82116 | 9.8 | 2026-10-27 | Missing Authentication for Critical Function Vulnerability in HiRDB.


This issue affects HiRDB Server Version 10: from  |
| CVE-2026-82117 | 9.8 | 2026-10-27 | Authentication Bypass by Spoofing Vulnerability in HiRDB.

This issue affects HiRDB Server Version 10: from 10-00 before |
| CVE-2026-82118 | 9.8 | 2026-10-27 | Stack-based Buffer Overflow Vulnerability in HiRDB.


This issue affects HiRDB Server Version 10: from 10-00 before 10-1 |
| CVE-2026-82119 | 9.8 | 2026-10-27 | OS Command Injection Vulnerability in HiRDB.


This issue affects HiRDB Server Version 10: from 10-00 before 10-12-01; H |
| CVE-2026-82120 | 9.8 | 2026-10-27 | Heap-based Buffer Overflow Vulnerability in HiRDB.


This issue affects HiRDB Server Version 10: from 10-00 before 10-12 |
| CVE-2026-82121 | 7.5 | 2026-10-27 | Origin Validation Error Vulnerability in HiRDB.


This issue affects HiRDB Server Version 10: from 10-00 before 10-12-01 |
| CVE-2026-82122 | 9.4 | 2026-10-27 | Stack-based Buffer Overflow Vulnerability in HiRDB.


This issue affects HiRDB Server Version 10: from 10-00 before 10-1 |
| CVE-2026-86574 | 9.8 | 2026-10-27 | Heap-based Buffer Overflow Vulnerability in JP1/Base.

This issue affects JP1/Base: from 11-00 before 12-50-54. |
| CVE-2026-86575 | 9.4 | 2026-10-27 | Stack-based Buffer Overflow Vulnerability in JP1 Products.

This issue affects JP1/Integrated Management 3 - Manager: fr |
| CVE-2026-86576 | 9.4 | 2026-10-27 | Heap-based Buffer Overflow Vulnerability in JP1 Products.

This issue affects JP1/Integrated Management 3 - Manager: fro |
| CVE-2026-86577 | 9.4 | 2026-10-27 | Out-of-bounds Write Vulnerability in JP1 Products.

This issue affects JP1/Integrated Management 3 - Manager: from 13-00 |
| CVE-2026-116871 | 7.5 | 2026-10-27 | Semantic MediaWiki 3.0.0 before 7.3.1 contains an uncontrolled recursion vulnerability in LegacyParser::getSubqueryDescr |
| CVE-2026-116872 | 7.5 | 2026-10-27 | Semantic MediaWiki from 3.0.0 before 7.3.1 contains an algorithmic complexity vulnerability in TermParser::normalize_com |
| CVE-2026-116873 | 7.3 | 2026-10-27 | Semantic MediaWiki from 7.3.0 before 7.3.1 contains a missing authorization vulnerability in the smwtask API module that |
| CVE-2026-116876 | 7.1 | 2026-10-27 | Semantic MediaWiki from 2.5.0 before 7.3.1 contains an improper authorization vulnerability that allows ordinary editors |
| CVE-2026-116878 | 7.5 | 2026-10-27 | Semantic MediaWiki from 2.5.0 before 7.3.1 contains an uncontrolled resource consumption vulnerability that allows anony |
| CVE-2026-116880 | 7.1 | 2026-10-27 | Semantic MediaWiki from 3.0.0 before 7.3.1 contains a cross-site request forgery vulnerability in Special:SMWAdmin becau |
| CVE-2026-116890 | 7.3 | 2026-10-27 | Semantic MediaWiki from 3.0.0 before 7.3.0 contains a missing authorization vulnerability in the api.php smwtask module  |
| CVE-2026-116896 | 7.5 | 2026-10-27 | REDAXO before 5.21.5 contains a missing authorization vulnerability in the backup addon export that accepts any database |
| CVE-2026-116898 | 7.1 | 2026-10-27 | REDAXO before 5.21.4 contains a missing authorization vulnerability in the media pool bulk move that checks only target  |
| CVE-2026-117532 | 9.8 | 2026-10-27 | REDAXO core from 5.3.0 before 5.21.4 contains an authentication bypass vulnerability in the structure/history plugin tha |
| CVE-2026-117536 | 8.8 | 2026-10-27 | REDAXO before 5.21.3 contains a cross-site request forgery vulnerability in the backend user administration page (users/ |
| CVE-2026-117540 | 7.5 | 2026-10-27 | svg-sanitizer from 0.5.3 before 1.1.0 contains a denial of service vulnerability in Sanitizer::sanitize() that repeatedl |
| CVE-2026-109995 | 7.2 | 2026-10-27 | The Advanced Views – Display Framework for Gutenberg & Elementor plugin for WordPress is vulnerable to Stored Cross-Site |
| CVE-2026-112362 | 9.1 | 2026-10-27 | @fastify/express is a Fastify plugin that runs Express middleware inside Fastify. In versions 4.0.5 through 4.0.8, when  |
| CVE-2026-41020 | 7.5 | 2026-10-27 | Eaton easyE4 uses a static nonce during authentication, which could allow an unauthenticated attacker with access to cap |
| CVE-2026-41021 | 7.5 | 2026-10-27 | Eaton easyE4 uses an insufficiently strong password policy. An attacker who obtains a password hash, including through C |
| CVE-2026-100164 | 7.5 | 2026-10-27 | Observable response discrepancy vulnerability in Rolantis Information Technologies Tourism Industry and Trade Co. Ltd. A |
| CVE-2026-24269 | 7.1 | 2026-10-27 | NVIDIA TensorRT-LLM contains a vulnerability where an attacker could cause a server-side request forgery. A successful e |
| CVE-2026-47486 | 7.8 | 2026-10-27 | NVIDIA PhysX for all platforms contains a vulnerability where an attacker could cause an out-of-bounds write. A successf |
| CVE-2026-65119 | 8.4 | 2026-10-27 | NVIDIA TensorRT-LLM for any platform contains a vulnerability in KvCacheAwareRouter tokenizer loading, where an attacker |
| CVE-2026-65120 | 7.1 | 2026-10-27 | NVIDIA TensorRT-LLM contains a vulnerability where an attacker could cause a server-side request forgery. A successful e |
| CVE-2026-65145 | 10.0 | 2026-10-27 | NVIDIA NeMo Agent Toolkit contains a vulnerability where a attacker could cause a missing authentication issue. This vul |
| CVE-2026-65151 | 8.4 | 2026-10-27 | NVIDIA NeMo Agent Toolkit contains vulnerability where an attacker could cause a SQL injection issue. A successful explo |
| CVE-2026-92546 | 7.5 | 2026-10-27 | Authentication bypass by spoofing vulnerability in Keepnet Labs Cybersecurity Inc. Agentic AI / Agentic Ally allows Auth |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-109618 | PHP Group / PHP | 2026-10-26 | 2026-10-29 | Unknown |
| CVE-2026-109619 | PHP Group / PHP | 2026-10-26 | 2026-10-29 | Unknown |
| CVE-2026-114625 | Arista / VeloCloud Orchestrator | 2026-10-23 | 2026-10-26 | Unknown |
| CVE-2026-110447 | Collabora / Collabora Online – Built-in CODE Server | 2026-10-23 | 2026-10-26 | Unknown |
| CVE-2026-106931 | EG Secure Solutions / SiteGuard Server Edition | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96656 | Plex / Media Server | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96655 | Plex / Media Server | 2026-10-20 | 2026-11-03 | Unknown |
| CVE-2026-96654 | Plex / Media Server | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96652 | Plex / Media Server | 2026-10-20 | 2026-11-03 | Unknown |
| CVE-2026-110936 | Siemens / Software Center | 2026-10-20 | 2026-11-03 | Unknown |

---

*Total entries in CISA KEV catalog: 1758*