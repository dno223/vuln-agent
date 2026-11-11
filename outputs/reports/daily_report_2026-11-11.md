# Vulnerability Intelligence Report

**Date:** 2026-11-11  
**Generated:** 2026-11-11T15:52:16Z  

---

## Executive Summary

Our environment faces critical exposure across 1,056 high-severity vulnerabilities, with the most urgent threats including unauthenticated remote code execution in Ivanti Endpoint Manager (CVSS 9.8), privilege escalation in Zoom Workplace (CVSS 9.6), and missing authentication in Ivanti Cloud Services (CVSS 9.4). Twelve new CISA Known Exploited Vulnerabilities were added this week, and one monitored CVE — a Google Chromium use-after-free — is actively exploited with a federal remediation deadline of November 24, 2026. Immediate prioritization of patch deployment and network controls is essential to prevent ransomware, data exfiltration, and system compromise.

---

## Risk Narrative

Threat actors are actively exploiting vulnerabilities in widely deployed enterprise platforms including Ivanti, Zoom, Microsoft Office, Barracuda, and Cisco BroadWorks. The concentration of unauthenticated remote code execution and privilege escalation flaws creates high-probability attack paths for ransomware deployment, credential theft, and lateral movement. The CISA KEV additions confirm active in-the-wild exploitation, elevating organizational risk beyond theoretical exposure. With 1,056 high-severity CVEs outstanding, the attack surface is broad and prioritization is critical. Failure to act swiftly — particularly on the Chromium KEV deadline — risks regulatory non-compliance, operational disruption, and significant reputational damage.

---

## Prioritized Action Items

1. Patch CVE-2026-125350 (Google Chromium use-after-free) across all endpoints before the CISA KEV deadline of November 24, 2026.
2. Immediately remediate CVE-2026-121653 (Ivanti EPM SQL injection, CVSS 9.8) by upgrading to version 2024 SU8 or later to eliminate unauthenticated RCE risk.
3. Apply emergency patches for CVE-2026-121683 (Ivanti Cloud Services missing authentication, CVSS 9.4) and CVE-2026-108186 (Zoom privilege escalation, CVSS 9.6) on all affected systems.
4. Audit and restrict network access to all systems affected by the 12 newly added CISA KEV entries, prioritizing Microsoft Office, Barracuda ESG, and Cisco BroadWorks vulnerabilities.
5. Conduct a full vulnerability inventory review to triage and schedule remediation for the remaining 1,046 high-severity CVEs based on asset criticality and exploitability.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-105425 | 7.2 | 2026-11-10 | OS command injection in Ivanti Sentry before versions 11.0.0, 10.8.3, and 10.7.4 as well as in Ivanti EPMM before versio |
| CVE-2026-108186 | 9.6 | 2026-11-10 | Improper Input Validation in Zoom Workplace for Windows may allow an unauthenticated user to conduct an escalation of pr |
| CVE-2026-108187 | 8.1 | 2026-11-10 | Origin Validation Error in Zoom Workplace for Windows may allow an unauthenticated user to conduct an escalation of priv |
| CVE-2026-11316 | 8.8 | 2026-11-10 | A out-of-bounds write vulnerability exists in the dr_wav drwav__read_cue_to_metadata_obj functionality of dr_libs (versi |
| CVE-2026-121653 | 9.8 | 2026-11-10 | SQL injection in the Core of Ivanti Endpoint Manager before version 2024 SU8 allows a remote unauthenticated attacker to |
| CVE-2026-121683 | 9.4 | 2026-11-10 | Missing authentication in Ivanti Cloud Services Application version 5.0.8 allows a remote unauthenticated attacker to ad |
| CVE-2026-124036 | 7.1 | 2026-11-10 | Missing authorization checks in the visual alert feature of FlockOS, Flock's hosted public safety platform, prior to 202 |
| CVE-2026-125750 | 7.1 | 2026-11-10 | Firekylin through 2.18.1 contains an improper authorization vulnerability that allows editor-role users to read administ |
| CVE-2026-125754 | 7.1 | 2026-11-10 | Dolibarr 20.0.0 through 23.0.4 and 24.x before 24.0.2 contains an insecure direct object reference vulnerability in api_ |
| CVE-2026-125757 | 9.1 | 2026-11-10 | mailcow: dockerized before 2026-11 contains a server-side template injection vulnerability that allows domain administra |
| CVE-2026-125758 | 7.4 | 2026-11-10 | Aptabase before commit 61d4c01 contains an authentication bypass vulnerability that allows unauthenticated attackers to  |
| CVE-2026-125759 | 7.5 | 2026-11-10 | Nango before 0.71.3 contains an sql injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2026-123180 | 8.8 | 2026-11-10 | A missing authentication vulnerability in the listed NETGEAR RAX models allows an network adjacent attacker who has auth |
| CVE-2026-124251 | 8.8 | 2026-11-10 | Cross-Site Request Forgery (CSRF) vulnerability in XplodedThemes WPIDE – File Manager & Code Editor wpide allows Cross S |
| CVE-2026-125271 | 7.8 | 2026-11-10 | Incorrect normalization of operation names in the custom security policy enforcement in awslabs aws-api-mcp-server befor |
| CVE-2026-126042 | 7.0 | 2026-11-10 | VNote 3.11.0 before 4.12.0 contains an OS command injection vulnerability in its Tasks feature: magic variables such as  |
| CVE-2026-126050 | 7.8 | 2026-11-10 | apitrace 2.0 through 14.0 contains a heap-based buffer overflow in SnappyFile::flushReadCache() that allows attackers to |
| CVE-2026-59986 | 7.4 | 2026-11-10 | rabbitmq-c is a C-language AMQP client library for RabbitMQ. Prior to version 0.17.0, the bounds check (*offset = o + le |
| CVE-2026-61547 | 9.8 | 2026-11-10 | rabbitmq-c is a C-language AMQP client library for RabbitMQ. Prior to version 0.17.0, a heap buffer overflow exists in r |
| CVE-2026-125323 | 7.8 | 2026-11-10 | pgEdge Control Plane is a distributed application for managing and orchestrating Postgres databases across multiple host |
| CVE-2026-125343 | 8.3 | 2026-11-10 | Buffer overflow in Compositing in Google Chrome prior to 157.0.8103.50 allowed a remote attacker who had compromised the |
| CVE-2026-125344 | 8.8 | 2026-11-10 | Type confusion in V8 in Google Chrome prior to 157.0.8103.50 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-125346 | 8.8 | 2026-11-10 | Use after free in XML in Google Chrome prior to 157.0.8103.50 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-125347 | 9.6 | 2026-11-10 | Incorrect authorization in FileSystem in Google Chrome prior to 157.0.8103.50 allowed a remote attacker leveraging socia |
| CVE-2026-125348 | 8.8 | 2026-11-10 | Out of bounds write in GPU in Google Chrome prior to 157.0.8103.50 allowed a remote attacker to potentially execute arbi |
| CVE-2026-125350 | 8.8 | 2026-11-10 | Use after free in XML in Google Chrome prior to 157.0.8103.50 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-100204 | 7.0 | 2026-11-10 | Use after free in HEIF Image Extensions allows an unauthorized attacker to execute code locally. |
| CVE-2026-100223 | 7.8 | 2026-11-10 | An elevation of privilege vulnerability exists when reparse points are created by sandboxed processes allowing sandbox e |
| CVE-2026-102219 | 8.1 | 2026-11-10 | Inadequate encryption strength in Windows Modern Device Management (MDM) allows an unauthorized attacker to execute code |
| CVE-2026-102224 | 8.4 | 2026-11-10 | Improper neutralization of special elements used in an os command ('os command injection') in Azure CycleCloud allows an |
| CVE-2026-102230 | 7.4 | 2026-11-10 | Missing authorization in Visual Studio Code allows an unauthorized attacker to disclose information over a network. |
| CVE-2026-102236 | 8.6 | 2026-11-10 | Improper restriction of rendered ui layers or frames in Visual Studio Code allows an unauthorized attacker to bypass a s |
| CVE-2026-103571 | 7.0 | 2026-11-10 | An elevation of privilege vulnerability exists when the Windows Cryptography Next Generation (CNG) Key Isolation service |
| CVE-2026-105017 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Volume Shadow Cop |
| CVE-2026-105020 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-105021 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-105022 | 7.8 | 2026-11-10 | Use after free in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105023 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-105024 | 7.0 | 2026-11-10 | Use after free in Windows Storage Spaces Controller allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105025 | 7.8 | 2026-11-10 | Double free in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105026 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-105028 | 7.8 | 2026-11-10 | Out-of-bounds read in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105437 | 7.5 | 2026-11-10 | Affected versions of Git have a heap buffer overflow in the three-way merge
code (xdiff), which an attacker can trigger  |
| CVE-2026-105490 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileg |
| CVE-2026-105491 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-105493 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileg |
| CVE-2026-105494 | 7.8 | 2026-11-10 | Untrusted search path in Azure NFS mount helper (aznfs) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105495 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-105496 | 8.8 | 2026-11-10 | Double free in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105497 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-105498 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-105499 | 8.8 | 2026-11-10 | Out-of-bounds read in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileges locall |
| CVE-2026-105501 | 7.8 | 2026-11-10 | Incorrect authorization in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105503 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Management Instrumentation allows an authorized attacker to elevate privileges loc |
| CVE-2026-105504 | 7.0 | 2026-11-10 | An elevation of privilege vulnerability exists in the way that the Windows Kernel handles objects in memory. An attacker |
| CVE-2026-105505 | 7.8 | 2026-11-10 | Relative path traversal in Microsoft Input Method Editor (IME) allows an authorized attacker to elevate privileges local |
| CVE-2026-105507 | 7.8 | 2026-11-10 | An elevation of privilege vulnerability exists in the Windows Installer when the Windows Installer fails to properly san |
| CVE-2026-105509 | 7.0 | 2026-11-10 | Use after free in Windows Resilient File System (ReFS) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105510 | 7.0 | 2026-11-10 | Use after free in Windows Secure Socket Tunneling Protocol (SSTP) allows an authorized attacker to elevate privileges lo |
| CVE-2026-105511 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Point-to-Point Pr |
| CVE-2026-105512 | 7.5 | 2026-11-10 | Integer underflow (wrap or wraparound) in Microsoft QUIC allows an unauthorized attacker to deny service over a network. |
| CVE-2026-105513 | 7.0 | 2026-11-10 | An elevation of privilege vulnerability exists in the way that the Windows Kernel handles objects in memory. An attacker |
| CVE-2026-105515 | 7.5 | 2026-11-10 | Buffer over-read in Windows Message Queuing allows an unauthorized attacker to deny service over a network. |
| CVE-2026-105518 | 8.8 | 2026-11-10 | Use after free in Windows iSCSI allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105520 | 7.2 | 2026-11-10 | Improper link resolution before file access ('link following') in Windows DNS allows an authorized attacker to elevate p |
| CVE-2026-105522 | 7.0 | 2026-11-10 | Use after free in Winlogon allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105524 | 7.8 | 2026-11-10 | Weak authentication in Windows Management Instrumentation allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105525 | 7.0 | 2026-11-10 | Integer overflow or wraparound in Windows Network Connection Broker allows an authorized attacker to elevate privileges  |
| CVE-2026-105526 | 7.0 | 2026-11-10 | Double free in Winsock allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105528 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Desktop Window Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105529 | 7.0 | 2026-11-10 | Weak authentication in Windows Storage allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105532 | 7.8 | 2026-11-10 | Improper link resolution before file access ('link following') in Windows Installer allows an authorized attacker to ele |
| CVE-2026-105533 | 7.0 | 2026-11-10 | Release of invalid pointer or reference in Windows COM allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105534 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Storage allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105540 | 7.0 | 2026-11-10 | Incorrect resource transfer between spheres in Windows Error Reporting allows an authorized attacker to elevate privileg |
| CVE-2026-105541 | 7.8 | 2026-11-10 | Use of out-of-range pointer offset in Windows Audio Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105542 | 8.8 | 2026-11-10 | Untrusted pointer dereference in Windows NTFS allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105543 | 7.8 | 2026-11-10 | Null pointer dereference in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105544 | 7.5 | 2026-11-10 | Improper access control in .NET allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105545 | 7.0 | 2026-11-10 | An elevation of privilege vulnerability exists in the Windows Installer when the Windows Installer fails to properly san |
| CVE-2026-105546 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Management Instru |
| CVE-2026-105547 | 7.0 | 2026-11-10 | Double free in Windows Setup and Deployment allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105551 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Windows NetBIOS allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-105553 | 7.0 | 2026-11-10 | Stack-based buffer overflow in Windows Filtering Platform (WFP) allows an authorized attacker to elevate privileges loca |
| CVE-2026-105554 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Background Intelligent Transfer Service (BITS) allows an authorized attacker to el |
| CVE-2026-105558 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Windows Deployment Services allows an authorized attacker to execute code over a network. |
| CVE-2026-105560 | 7.2 | 2026-11-10 | Release of invalid pointer or reference in Windows DHCP Server allows an authorized attacker to execute code over a netw |
| CVE-2026-105561 | 7.5 | 2026-11-10 | Uncontrolled resource consumption in Windows Secure Socket Tunneling Protocol (SSTP) allows an unauthorized attacker to  |
| CVE-2026-105565 | 7.0 | 2026-11-10 | Use after free in Windows MIDI Service Module allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105566 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Kernel allows an  |
| CVE-2026-105567 | 7.0 | 2026-11-10 | Use after free in Windows Print Spooler Components allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105569 | 7.8 | 2026-11-10 | Out-of-bounds read in Windows Cloud Files Mini Filter Driver allows an authorized attacker to elevate privileges locally |
| CVE-2026-105574 | 7.0 | 2026-11-10 | Use after free in Windows MIDI Service Module allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105575 | 7.8 | 2026-11-10 | Access of resource using incompatible type ('type confusion') in Windows DWM Core Library allows an authorized attacker  |
| CVE-2026-105578 | 7.5 | 2026-11-10 | Integer overflow or wraparound in Microsoft JScript allows an unauthorized attacker to execute code over a network. |
| CVE-2026-105579 | 7.5 | 2026-11-10 | Integer overflow or wraparound in Windows DNS allows an unauthorized attacker to disclose information over a network. |
| CVE-2026-105580 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Management Instrumentation allows an unauthorized attacker to execute code locally |
| CVE-2026-105581 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Desktop Window Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105582 | 7.0 | 2026-11-10 | Release of invalid pointer or reference in Windows DWM Core Library allows an authorized attacker to elevate privileges  |
| CVE-2026-105583 | 7.0 | 2026-11-10 | Release of invalid pointer or reference in Windows DWM Core Library allows an authorized attacker to elevate privileges  |
| CVE-2026-105586 | 7.0 | 2026-11-10 | Null pointer dereference in Microsoft Windows SCSI Class System File allows an authorized attacker to elevate privileges |
| CVE-2026-105587 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows OLE DB allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105589 | 7.0 | 2026-11-10 | Use after free in Windows Wireless Networking allows an authorized attacker to elevate privileges locally. |
| CVE-2026-105734 | 7.0 | 2026-11-10 | Incorrect permission assignment for critical resource in Azure Local allows an authorized attacker to elevate privileges |
| CVE-2026-108401 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Remote Desktop Services allows an authorized attacker to execute code over a netwo |
| CVE-2026-108403 | 7.8 | 2026-11-10 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-108405 | 7.8 | 2026-11-10 | Integer overflow or wraparound in Windows CD-ROM Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-108406 | 7.0 | 2026-11-10 | Use after free in Windows Network Connection Broker allows an authorized attacker to elevate privileges locally. |
| CVE-2026-108407 | 7.8 | 2026-11-10 | Out-of-bounds read in Windows GDI allows an authorized attacker to elevate privileges locally. |
| CVE-2026-108411 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows ODBC Driver allows an unauthorized attacker to execute code over a network. |
| CVE-2026-108412 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Redirected Drive Buffering allows an authorized attacker to elevate privileges loc |
| CVE-2026-108413 | 7.0 | 2026-11-10 | Use after free in Windows Telephony Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-108414 | 7.0 | 2026-11-10 | Use after free in Windows Projected File System Filter Driver allows an authorized attacker to elevate privileges locall |
| CVE-2026-108421 | 7.5 | 2026-11-10 | Out-of-bounds read in Windows File Server Resource Management Service allows an unauthorized attacker to elevate privile |
| CVE-2026-109454 | 9.0 | 2026-11-10 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-109457 | 8.0 | 2026-11-10 | Improper neutralization of special elements used in an os command ('os command injection') in Azure CLI allows an author |
| CVE-2026-109459 | 8.1 | 2026-11-10 | Heap-based buffer overflow in Windows Message Queuing Queue Manager allows an unauthorized attacker to execute code over |
| CVE-2026-109463 | 8.8 | 2026-11-10 | Deserialization of untrusted data in Windows DNS allows an unauthorized attacker to execute code over a network. |
| CVE-2026-109464 | 8.8 | 2026-11-10 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-109466 | 8.0 | 2026-11-10 | Missing authorization in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over an adjacen |
| CVE-2026-109467 | 9.9 | 2026-11-10 | Improper authentication in Azure DevOps allows an authorized attacker to execute code over a network. |
| CVE-2026-109472 | 8.8 | 2026-11-10 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-109473 | 7.8 | 2026-11-10 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-109475 | 7.5 | 2026-11-10 | Stack-based buffer overflow in .NET allows an unauthorized attacker to deny service over a network. |
| CVE-2026-109478 | 7.5 | 2026-11-10 | Inefficient algorithmic complexity in ASP.NET Core allows an unauthorized attacker to deny service over a network. |
| CVE-2026-109481 | 7.5 | 2026-11-10 | Cross-site request forgery (csrf) in ASP.NET Core allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-109487 | 7.5 | 2026-11-10 | Use after free in Microsoft Office PowerPoint allows an unauthorized attacker to execute code over a network. |
| CVE-2026-109491 | 7.5 | 2026-11-10 | Use after free in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-109492 | 8.8 | 2026-11-10 | Authorization bypass through user-controlled key in Microsoft MCP Gateway allows an authorized attacker to elevate privi |
| CVE-2026-109493 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-109494 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Visio allows an unauthorized attacker to execute code over a network. |
| CVE-2026-109496 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Visio allows an unauthorized attacker to execute code over a network. |
| CVE-2026-109497 | 7.3 | 2026-11-10 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-109498 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-109499 | 8.8 | 2026-11-10 | Access of resource using incompatible type ('type confusion') in Microsoft Office SharePoint allows an authorized attack |
| CVE-2026-109500 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-109501 | 8.8 | 2026-11-10 | Out-of-bounds read in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-109502 | 8.8 | 2026-11-10 | Server-side request forgery (ssrf) in Microsoft Office SharePoint allows an authorized attacker to elevate privileges ov |
| CVE-2026-109503 | 8.8 | 2026-11-10 | Double free in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-109504 | 7.3 | 2026-11-10 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-109505 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110043 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110044 | 8.8 | 2026-11-10 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-110045 | 7.3 | 2026-11-10 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-110047 | 8.8 | 2026-11-10 | Use after free in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110048 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110049 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-110050 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110052 | 7.5 | 2026-11-10 | Use after free in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110053 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110054 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110055 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110056 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-110058 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110059 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110060 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110061 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110062 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110064 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110065 | 7.3 | 2026-11-10 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-110067 | 8.8 | 2026-11-10 | Use after free in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-110068 | 8.8 | 2026-11-10 | Use after free in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111285 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111286 | 7.5 | 2026-11-10 | Use after free in Microsoft Office allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111287 | 7.5 | 2026-11-10 | Stack-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111289 | 8.8 | 2026-11-10 | Use after free in Microsoft Office allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111290 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111294 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111295 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111296 | 8.0 | 2026-11-10 | Server-side request forgery (ssrf) in Microsoft Office SharePoint allows an authorized attacker to elevate privileges ov |
| CVE-2026-111297 | 8.0 | 2026-11-10 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-111298 | 8.8 | 2026-11-10 | Out-of-bounds read in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111299 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111300 | 7.3 | 2026-11-10 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-111301 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111302 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-111303 | 7.3 | 2026-11-10 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-111304 | 8.8 | 2026-11-10 | Use after free in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111305 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Access allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111306 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111307 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111308 | 8.8 | 2026-11-10 | Numeric truncation error in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-111309 | 8.8 | 2026-11-10 | Release of invalid pointer or reference in Microsoft Office Outlook allows an unauthorized attacker to execute code over |
| CVE-2026-111310 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112714 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112715 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112716 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112717 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112718 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112719 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112721 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112722 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112723 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112724 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112726 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112727 | 8.8 | 2026-11-10 | Untrusted pointer dereference in DNS Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112728 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112729 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112730 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112733 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112734 | 8.8 | 2026-11-10 | Use after free in Microsoft Office PowerPoint allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112735 | 8.8 | 2026-11-10 | Use after free in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112737 | 8.8 | 2026-11-10 | Use after free in Microsoft Office PowerPoint allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112739 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112741 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112743 | 7.8 | 2026-11-10 | Untrusted pointer dereference in Windows Device Association Service allows an authorized attacker to elevate privileges  |
| CVE-2026-112751 | 7.8 | 2026-11-10 | Use after free in Windows Remote Assistance allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112752 | 7.8 | 2026-11-10 | Improper access control in Windows Print Spooler Components allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112753 | 7.0 | 2026-11-10 | Access of resource using incompatible type ('type confusion') in Windows Container Isolation FS Filter Driver (unionfs.s |
| CVE-2026-112756 | 7.0 | 2026-11-10 | Use after free in Windows Filtering Platform (WFP) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112758 | 7.8 | 2026-11-10 | Double free in Windows Defender Firewall Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112759 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Task Scheduler allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112760 | 7.8 | 2026-11-10 | Integer overflow or wraparound in Windows Overlay Filter allows an unauthorized attacker to elevate privileges locally. |
| CVE-2026-112761 | 7.0 | 2026-11-10 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112762 | 8.8 | 2026-11-10 | Relative path traversal in Windows Print Spooler Components allows an unauthorized attacker to elevate privileges over a |
| CVE-2026-112763 | 7.0 | 2026-11-10 | Use after free in Windows Cloud Files Mini Filter Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112764 | 7.0 | 2026-11-10 | Use after free in Windows USB Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112765 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Print Spooler Components allows an authorized attacker to elevate privileges local |
| CVE-2026-112766 | 7.0 | 2026-11-10 | Use after free in Windows exFAT File System allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112790 | 7.0 | 2026-11-10 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112791 | 7.0 | 2026-11-10 | Time-of-check time-of-use (toctou) race condition in Windows Print Spooler Components allows an authorized attacker to e |
| CVE-2026-112792 | 7.0 | 2026-11-10 | Use after free in Windows Print Spooler Components allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112793 | 7.5 | 2026-11-10 | Use after free in Windows Event Collector Service allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-112794 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Smart Card allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112796 | 7.0 | 2026-11-10 | Double free in Windows Event Collector Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112797 | 7.0 | 2026-11-10 | Use after free in Windows Print Spooler Components allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112798 | 7.0 | 2026-11-10 | Use after free in Windows NetBIOS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112799 | 7.8 | 2026-11-10 | Stack-based buffer overflow in Windows Projected File System allows an authorized attacker to elevate privileges locally |
| CVE-2026-112800 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Diagnostic Policy Service allows an authorized attacker to elevate privileges loca |
| CVE-2026-112801 | 7.8 | 2026-11-10 | Insufficiently protected credentials in Windows eSCL Scanner allows an authorized attacker to elevate privileges locally |
| CVE-2026-112802 | 7.8 | 2026-11-10 | Missing authorization in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112804 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows exFAT File System allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112805 | 8.8 | 2026-11-10 | Untrusted pointer dereference in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112810 | 7.0 | 2026-11-10 | Time-of-check time-of-use (toctou) race condition in Windows Cloud Files Mini Filter Driver allows an authorized attacke |
| CVE-2026-112811 | 7.8 | 2026-11-10 | Stack-based buffer overflow in Windows Print Spooler Components allows an authorized attacker to elevate privileges loca |
| CVE-2026-112812 | 7.0 | 2026-11-10 | Use after free in Windows SMB Client allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112966 | 7.5 | 2026-11-10 | Uncontrolled resource consumption in Windows Security Account Manager allows an unauthorized attacker to deny service ov |
| CVE-2026-112967 | 9.8 | 2026-11-10 | Heap-based buffer overflow in Windows Xbox Live Networking Service allows an unauthorized attacker to execute code over  |
| CVE-2026-112968 | 7.0 | 2026-11-10 | Use after free in Windows COM allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112970 | 7.0 | 2026-11-10 | Use after free in Windows SMB Client allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112971 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows SMB Client allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112972 | 7.5 | 2026-11-10 | Integer overflow or wraparound in Windows SMB Server allows an authorized attacker to execute code over a network. |
| CVE-2026-112973 | 7.1 | 2026-11-10 | Improper access control in Windows Kernel allows an authorized attacker to bypass a security feature locally. |
| CVE-2026-112976 | 7.0 | 2026-11-10 | Use after free in Windows Print Spooler Components allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112978 | 7.8 | 2026-11-10 | Use after free in Windows Print Spooler Components allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112981 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Print Spooler Components allows an authorized attacker to elevate privileges local |
| CVE-2026-112985 | 7.5 | 2026-11-10 | Integer overflow or wraparound in Microsoft JScript allows an unauthorized attacker to execute code over a network. |
| CVE-2026-112986 | 7.0 | 2026-11-10 | No cwe for this issue in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-112987 | 7.0 | 2026-11-10 | Integer overflow or wraparound in Windows Modern Device Management (MDM) allows an authorized attacker to elevate privil |
| CVE-2026-112989 | 7.0 | 2026-11-10 | Untrusted pointer dereference in Servicing Stack Updates allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113748 | 7.8 | 2026-11-10 | Stack-based buffer overflow in Software Protection Platform (SPP) allows an authorized attacker to elevate privileges lo |
| CVE-2026-113749 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Microsoft Windows Codecs Library allows an unauthorized attacker to execute code over a ne |
| CVE-2026-113750 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Device Inventory allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113751 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Fast FAT Driver a |
| CVE-2026-113752 | 7.5 | 2026-11-10 | Use after free in Windows Print Spooler Components allows an unauthorized attacker to execute code over an adjacent netw |
| CVE-2026-113753 | 8.2 | 2026-11-10 | Untrusted pointer dereference in Windows Hyper-V allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113755 | 7.0 | 2026-11-10 | Use after free in Windows Filter Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113758 | 7.8 | 2026-11-10 | Out-of-bounds read in Desktop Window Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113759 | 7.8 | 2026-11-10 | Use after free in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-113760 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows XWizard Framework allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113761 | 7.0 | 2026-11-10 | Untrusted pointer dereference in Windows Container Isolation FS Filter Driver (unionfs.sys) allows an authorized attacke |
| CVE-2026-113762 | 7.0 | 2026-11-10 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113765 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows File Server Resource Management Service allows an authorized attacker to elevate p |
| CVE-2026-113767 | 7.8 | 2026-11-10 | Inclusion of functionality from untrusted control sphere in Windows COM+ Event System Service allows an authorized attac |
| CVE-2026-113768 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Windows Performance Counters allows an unauthorized attacker to execute code over a networ |
| CVE-2026-113769 | 7.0 | 2026-11-10 | Use after free in Windows COM+ Event System Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113770 | 7.0 | 2026-11-10 | Untrusted pointer dereference in Windows Print Spooler Components allows an authorized attacker to elevate privileges lo |
| CVE-2026-113814 | 8.8 | 2026-11-10 | Untrusted pointer dereference in Windows Storage Spaces Controller allows an unauthorized attacker to execute code over  |
| CVE-2026-113819 | 7.0 | 2026-11-10 | Use after free in Desktop Window Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113820 | 7.0 | 2026-11-10 | Use after free in Windows Modern Device Management (MDM) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113823 | 7.5 | 2026-11-10 | Improper limitation of a pathname to a restricted directory ('path traversal') in Azure CycleCloud allows an unauthorize |
| CVE-2026-113825 | 7.5 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows SMB Server Networ |
| CVE-2026-113842 | 7.0 | 2026-11-10 | Use after free in Windows Security Center allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113843 | 7.8 | 2026-11-10 | Improper authentication in Windows Remote Access Connection Manager allows an authorized attacker to elevate privileges  |
| CVE-2026-113847 | 7.8 | 2026-11-10 | Integer overflow or wraparound in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113848 | 7.8 | 2026-11-10 | Null pointer dereference in Windows NTFS allows an unauthorized attacker to execute code locally. |
| CVE-2026-113855 | 7.5 | 2026-11-10 | Use of uninitialized resource in Windows DNS allows an unauthorized attacker to execute code over an adjacent network. |
| CVE-2026-113856 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Hyper-V allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113859 | 7.5 | 2026-11-10 | Use after free in Windows TCP/IP allows an unauthorized attacker to execute code over an adjacent network. |
| CVE-2026-113860 | 7.0 | 2026-11-10 | Use after free in Windows Hyper-V allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113861 | 7.5 | 2026-11-10 | Use after free in Windows Hyper-V allows an authorized attacker to elevate privileges locally. |
| CVE-2026-113862 | 8.1 | 2026-11-10 | Use after free in Windows Network Address Translation (NAT) allows an unauthorized attacker to execute code over a netwo |
| CVE-2026-113863 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows DHCP Client allows an unauthorized attacker to elevate privileges over an adjacent |
| CVE-2026-113865 | 7.8 | 2026-11-10 | Time-of-check time-of-use (toctou) race condition in Windows Hyper-V allows an authorized attacker to elevate privileges |
| CVE-2026-114146 | 9.0 | 2026-11-10 | Incorrect authorization in ASP.NET Core allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-114147 | 7.5 | 2026-11-10 | Missing release of memory after effective lifetime in ASP.NET Core allows an unauthorized attacker to deny service over  |
| CVE-2026-114149 | 7.5 | 2026-11-10 | Uncontrolled resource consumption in ASP.NET Core allows an unauthorized attacker to deny service over a network. |
| CVE-2026-114151 | 8.8 | 2026-11-10 | Deserialization of untrusted data in Visual Studio allows an unauthorized attacker to execute code over a network. |
| CVE-2026-114152 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Visual Studio allows an unauthorized attacker to execute code over a network. |
| CVE-2026-114154 | 7.5 | 2026-11-10 | Uncontrolled resource consumption in ASP.NET Core allows an unauthorized attacker to deny service over a network. |
| CVE-2026-114155 | 7.5 | 2026-11-10 | Time-of-check time-of-use (toctou) race condition in .NET allows an authorized attacker to elevate privileges locally. |
| CVE-2026-114157 | 7.5 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in ASP.NET Core allows an au |
| CVE-2026-114158 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Visual Studio allows an unauthorized attacker to execute code over a network. |
| CVE-2026-114159 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Visual Studio allows an unauthorized attacker to execute code over a network. |
| CVE-2026-114160 | 9.8 | 2026-11-10 | Server-side request forgery (ssrf) in Azure Managed Grafana allows an unauthorized attacker to elevate privileges over a |
| CVE-2026-114161 | 7.8 | 2026-11-10 | Improper limitation of a pathname to a restricted directory ('path traversal') in Azure CycleCloud allows an authorized  |
| CVE-2026-114162 | 9.1 | 2026-11-10 | Incorrect authorization in Microsoft Graph allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-114164 | 8.8 | 2026-11-10 | Integer underflow (wrap or wraparound) in Microsoft Windows Codecs Library allows an unauthorized attacker to execute co |
| CVE-2026-114165 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Windows Codecs Library allows an unauthorized attacker to execute code locally. |
| CVE-2026-114167 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Windows Codecs Library allows an unauthorized attacker to execute code locally. |
| CVE-2026-114169 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Raw Image Extension allows an unauthorized attacker to execute code over a network |
| CVE-2026-114170 | 7.8 | 2026-11-10 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-114171 | 8.8 | 2026-11-10 | User interface (ui) misrepresentation of critical information in Visual Studio Code allows an unauthorized attacker to b |
| CVE-2026-116698 | 7.5 | 2026-11-10 | Use after free in Microsoft WDAC OLE DB provider for SQL allows an unauthorized attacker to execute code over a network. |
| CVE-2026-116706 | 7.5 | 2026-11-10 | Use after free in Windows Link Layer Topology Discovery Protocol allows an unauthorized attacker to execute code over an |
| CVE-2026-116707 | 7.0 | 2026-11-10 | Use after free in Windows Link Layer Topology Discovery Protocol allows an authorized attacker to elevate privileges loc |
| CVE-2026-116710 | 8.1 | 2026-11-10 | Heap-based buffer overflow in Windows Message Queuing allows an unauthorized attacker to execute code over a network. |
| CVE-2026-116714 | 7.8 | 2026-11-10 | Incorrect authorization in Windows AppX Deployment Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-116717 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code over a network. |
| CVE-2026-116718 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-116719 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-116720 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-116722 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-116923 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-116925 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-116926 | 7.5 | 2026-11-10 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Teams allows an unauth |
| CVE-2026-116927 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-116928 | 9.8 | 2026-11-10 | Out-of-bounds write in Microsoft Windows Search Component allows an unauthorized attacker to execute code over a network |
| CVE-2026-116929 | 7.5 | 2026-11-10 | Execution with unnecessary privileges in SQL Server allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-116930 | 8.8 | 2026-11-10 | Improper neutralization of special elements used in a command ('command injection') in SQL Server allows an unauthorized |
| CVE-2026-116931 | 7.5 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-116933 | 7.2 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-116934 | 8.8 | 2026-11-10 | Untrusted pointer dereference in SQL Server allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-116936 | 7.2 | 2026-11-10 | Stack-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-116937 | 7.5 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-116938 | 7.5 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-116941 | 8.8 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-116942 | 8.8 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-116943 | 7.5 | 2026-11-10 | Buffer over-read in SQL Server allows an unauthorized attacker to disclose information over a network. |
| CVE-2026-116944 | 7.2 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-116945 | 9.8 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-116946 | 8.8 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-116947 | 7.5 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-118105 | 8.8 | 2026-11-10 | Improper neutralization of special elements used in an sql command ('sql injection') in SQL Server allows an authorized  |
| CVE-2026-118106 | 8.1 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118108 | 7.5 | 2026-11-10 | Improper authorization in SQL Server allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-118109 | 8.8 | 2026-11-10 | Improper neutralization of special elements used in an sql command ('sql injection') in SQL Server allows an authorized  |
| CVE-2026-118110 | 8.8 | 2026-11-10 | Improper neutralization of special elements used in an sql command ('sql injection') in SQL Server allows an authorized  |
| CVE-2026-118111 | 8.0 | 2026-11-10 | Origin validation error in SQL Server allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-118112 | 8.0 | 2026-11-10 | Improper control of generation of code ('code injection') in SQL Server allows an authorized attacker to elevate privile |
| CVE-2026-118113 | 8.0 | 2026-11-10 | Improper neutralization of special elements used in an sql command ('sql injection') in SQL Server allows an authorized  |
| CVE-2026-118114 | 7.5 | 2026-11-10 | Improper neutralization of special elements used in an sql command ('sql injection') in SQL Server allows an authorized  |
| CVE-2026-118115 | 7.5 | 2026-11-10 | Improper neutralization of special elements used in an sql command ('sql injection') in SQL Server allows an authorized  |
| CVE-2026-118116 | 7.0 | 2026-11-10 | Improper neutralization of special elements used in an sql command ('sql injection') in SQL Server allows an authorized  |
| CVE-2026-118117 | 8.0 | 2026-11-10 | Improper neutralization of special elements used in an sql command ('sql injection') in SQL Server allows an authorized  |
| CVE-2026-118118 | 8.0 | 2026-11-10 | Improper neutralization of special elements used in an sql command ('sql injection') in SQL Server allows an authorized  |
| CVE-2026-118119 | 8.0 | 2026-11-10 | Improper neutralization of special elements used in an sql command ('sql injection') in SQL Server allows an authorized  |
| CVE-2026-118120 | 8.8 | 2026-11-10 | Improper neutralization of special elements used in an sql command ('sql injection') in SQL Server allows an authorized  |
| CVE-2026-118123 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Point-to-Point Pr |
| CVE-2026-118124 | 7.0 | 2026-11-10 | Out-of-bounds read in Windows Internet Connection Sharing (ICS) allows an authorized attacker to elevate privileges loca |
| CVE-2026-118125 | 7.0 | 2026-11-10 | Use after free in Windows Message Queuing allows an authorized attacker to elevate privileges locally. |
| CVE-2026-118126 | 7.8 | 2026-11-10 | Use after free in Windows Message Queuing allows an authorized attacker to elevate privileges locally. |
| CVE-2026-118137 | 7.8 | 2026-11-10 | Improper authorization in Windows FTP Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-118138 | 7.8 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Client for NFS al |
| CVE-2026-118141 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Windows Client for NFS allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118142 | 7.8 | 2026-11-10 | Out-of-bounds read in Windows Distributed File System (DFS) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-118145 | 7.5 | 2026-11-10 | Use after free in Windows Function Discovery SSDP Provider allows an unauthorized attacker to execute code over an adjac |
| CVE-2026-118146 | 8.8 | 2026-11-10 | Incorrect authorization in Active Directory Domain Services allows an authorized attacker to execute code over a network |
| CVE-2026-118148 | 7.5 | 2026-11-10 | Improper authentication in Active Directory Domain Services allows an authorized attacker to elevate privileges over a n |
| CVE-2026-118149 | 8.8 | 2026-11-10 | Improper control of generation of code ('code injection') in Microsoft Exchange Server allows an authorized attacker to  |
| CVE-2026-118150 | 8.8 | 2026-11-10 | Authorization bypass through user-controlled key in Microsoft Exchange Server allows an authorized attacker to elevate p |
| CVE-2026-118151 | 7.2 | 2026-11-10 | External control of file name or path in Microsoft Exchange Server allows an authorized attacker to elevate privileges o |
| CVE-2026-118153 | 7.5 | 2026-11-10 | Inefficient algorithmic complexity in Microsoft Exchange Server allows an unauthorized attacker to deny service over a n |
| CVE-2026-118154 | 8.8 | 2026-11-10 | Reliance on untrusted inputs in a security decision in Microsoft Exchange Server allows an authorized attacker to elevat |
| CVE-2026-118157 | 7.2 | 2026-11-10 | Weak authentication in Microsoft Exchange Server allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-118207 | 8.8 | 2026-11-10 | Improper input validation in Microsoft Exchange Server allows an authorized attacker to execute code over a network. |
| CVE-2026-118208 | 7.1 | 2026-11-10 | Improper access control in Microsoft Exchange Server allows an authorized attacker to perform spoofing over a network. |
| CVE-2026-118215 | 7.8 | 2026-11-10 | Use after free in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileges locally. |
| CVE-2026-118216 | 8.8 | 2026-11-10 | Use after free in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileges locally. |
| CVE-2026-118217 | 8.8 | 2026-11-10 | Use after free in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileges locally. |
| CVE-2026-118218 | 8.8 | 2026-11-10 | Use after free in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileges locally. |
| CVE-2026-118219 | 8.8 | 2026-11-10 | Use after free in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileges locally. |
| CVE-2026-118220 | 7.8 | 2026-11-10 | Double free in Windows Multiple Provider Router allows an authorized attacker to elevate privileges locally. |
| CVE-2026-118221 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-118222 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-118223 | 7.8 | 2026-11-10 | Use after free in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileges locally. |
| CVE-2026-118224 | 7.8 | 2026-11-10 | Use after free in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileges locally. |
| CVE-2026-118225 | 8.8 | 2026-11-10 | Inclusion of functionality from untrusted control sphere in Windows Advanced Rasterization Platform allows an authorized |
| CVE-2026-118226 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileg |
| CVE-2026-118227 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-118228 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-118229 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-118232 | 8.8 | 2026-11-10 | Out-of-bounds read in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileges locall |
| CVE-2026-118277 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-118278 | 8.8 | 2026-11-10 | Out-of-bounds read in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileges locall |
| CVE-2026-118279 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-118280 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-118283 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privileg |
| CVE-2026-118288 | 7.0 | 2026-11-10 | Incorrect permission assignment for critical resource in Azure File Sync allows an authorized attacker to elevate privil |
| CVE-2026-118292 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118293 | 8.8 | 2026-11-10 | Out-of-bounds read in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118294 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118295 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118296 | 8.8 | 2026-11-10 | Double free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118297 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118298 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118299 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118301 | 7.5 | 2026-11-10 | Use of uninitialized resource in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118302 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118700 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118701 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118702 | 8.8 | 2026-11-10 | Double free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118703 | 8.8 | 2026-11-10 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118704 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118705 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118706 | 8.8 | 2026-11-10 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118707 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118708 | 8.8 | 2026-11-10 | Release of invalid pointer or reference in Microsoft Office Excel allows an unauthorized attacker to execute code over a |
| CVE-2026-118709 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118710 | 8.8 | 2026-11-10 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118711 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118712 | 8.8 | 2026-11-10 | Integer underflow (wrap or wraparound) in Microsoft Office Excel allows an unauthorized attacker to execute code over a  |
| CVE-2026-118713 | 8.8 | 2026-11-10 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118714 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118715 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to elevate privileges over a networ |
| CVE-2026-118716 | 8.8 | 2026-11-10 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118717 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118718 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118719 | 8.8 | 2026-11-10 | Double free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118720 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118721 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118722 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118723 | 7.8 | 2026-11-10 | Untrusted pointer dereference in Microsoft Office Excel allows an unauthorized attacker to execute code locally. |
| CVE-2026-118724 | 8.8 | 2026-11-10 | Untrusted pointer dereference in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118725 | 8.8 | 2026-11-10 | Out-of-bounds read in Microsoft Office Excel allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-118726 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118729 | 8.8 | 2026-11-10 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118730 | 8.8 | 2026-11-10 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118731 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118732 | 8.8 | 2026-11-10 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118735 | 7.5 | 2026-11-10 | Weak authentication in Active Directory Domain Services allows an authorized attacker to elevate privileges over a netwo |
| CVE-2026-118737 | 8.1 | 2026-11-10 | Improper verification of cryptographic signature in Windows Remote Procedure Call Runtime allows an unauthorized attacke |
| CVE-2026-118740 | 9.1 | 2026-11-10 | Missing authorization in Aspire allows an unauthorized attacker to bypass a security feature over a network. |
| CVE-2026-118741 | 8.1 | 2026-11-10 | Improper authentication in ASP.NET Core allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-118742 | 8.6 | 2026-11-10 | Incorrect permission assignment for critical resource in Azure Front Door (AFD) allows an unauthorized attacker to eleva |
| CVE-2026-118745 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Visual Studio allows an unauthorized attacker to execute code over a network. |
| CVE-2026-118747 | 7.5 | 2026-11-10 | Inefficient algorithmic complexity in .NET allows an unauthorized attacker to deny service over a network. |
| CVE-2026-118748 | 7.5 | 2026-11-10 | Allocation of resources without limits or throttling in ASP.NET Core allows an unauthorized attacker to deny service ove |
| CVE-2026-118749 | 7.5 | 2026-11-10 | Inefficient algorithmic complexity in ASP.NET Core allows an unauthorized attacker to deny service over a network. |
| CVE-2026-118750 | 7.5 | 2026-11-10 | Allocation of resources without limits or throttling in ASP.NET Core allows an unauthorized attacker to deny service ove |
| CVE-2026-119382 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows TPM allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119386 | 7.0 | 2026-11-10 | Use after free in Windows Resilient File System (ReFS) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119387 | 7.0 | 2026-11-10 | Use after free in Quality Windows Audio/Video Experience (QWAVE) service allows an authorized attacker to elevate privil |
| CVE-2026-119388 | 7.0 | 2026-11-10 | Use after free in Quality Windows Audio/Video Experience (QWAVE) service allows an authorized attacker to elevate privil |
| CVE-2026-119389 | 7.0 | 2026-11-10 | Use after free in Windows Storage allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119390 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Remote Desktop Client allows an authorized attacker to execute code locally. |
| CVE-2026-119391 | 7.8 | 2026-11-10 | Use after free in Windows Hyper-V allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119392 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Storage Spaces Controller allows an unauthorized attacker to elevate privileges ov |
| CVE-2026-119393 | 7.8 | 2026-11-10 | Stack-based buffer overflow in Windows Credential Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119397 | 7.0 | 2026-11-10 | Use after free in Kernel Transaction Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119398 | 7.0 | 2026-11-10 | Improper access control in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119399 | 7.0 | 2026-11-10 | Double free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119401 | 7.0 | 2026-11-10 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119402 | 7.0 | 2026-11-10 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119403 | 7.0 | 2026-11-10 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119405 | 7.0 | 2026-11-10 | Use after free in Windows Backup Engine allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119816 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Microsoft Account Sign-in Assistant allows an authorized attacker to elevate privi |
| CVE-2026-119817 | 7.8 | 2026-11-10 | Double free in Windows Shell allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119818 | 7.8 | 2026-11-10 | Incorrect authorization in Windows Text Services Framework allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119821 | 7.8 | 2026-11-10 | Improper authorization in Windows Network Connection Broker allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119822 | 7.0 | 2026-11-10 | Exposure of sensitive system information to an unauthorized control sphere in Windows Overlay Filter allows an authorize |
| CVE-2026-119824 | 8.8 | 2026-11-10 | Missing authentication for critical function in Remote Desktop Client allows an unauthorized attacker to perform tamperi |
| CVE-2026-119826 | 7.8 | 2026-11-10 | Use after free in Windows Hyper-V allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119827 | 7.0 | 2026-11-10 | Missing authorization in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119831 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119833 | 7.0 | 2026-11-10 | Untrusted pointer dereference in Windows Message Queuing allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119834 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Subsystem for Linux allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119835 | 7.0 | 2026-11-10 | Use after free in Windows Smart Card allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119837 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Windows Universal Disk Format File System Driver (UDFS) allows an authorized attacker to e |
| CVE-2026-119839 | 8.8 | 2026-11-10 | Untrusted search path in Remote Desktop Client allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-119844 | 7.0 | 2026-11-10 | Use after free in Windows Device Association Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119846 | 7.8 | 2026-11-10 | Out-of-bounds read in Windows Subsystem for Linux allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119847 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Kerberos allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119849 | 7.0 | 2026-11-10 | Stack-based buffer overflow in Virtual Hard Disk (VHD) Miniport Driver allows an authorized attacker to execute code loc |
| CVE-2026-119851 | 7.0 | 2026-11-10 | Time-of-check time-of-use (toctou) race condition in Windows Storage Spaces Controller allows an authorized attacker to  |
| CVE-2026-119853 | 7.8 | 2026-11-10 | Untrusted search path in Windows Remote Access API allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119858 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119859 | 7.0 | 2026-11-10 | Use after free in Windows Internet Connection Sharing (ICS) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119860 | 7.0 | 2026-11-10 | Use after free in Windows Internet Connection Sharing (ICS) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119861 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Internet Connection Sharing (ICS) allows an authorized attacker to elevate privile |
| CVE-2026-119862 | 8.8 | 2026-11-10 | Out-of-bounds read in Windows Input System allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119865 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Installer allows  |
| CVE-2026-119866 | 7.0 | 2026-11-10 | Use after free in Windows Device Association Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119868 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Kernel allows an  |
| CVE-2026-119870 | 7.0 | 2026-11-10 | Untrusted pointer dereference in Windows SMB Client allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119873 | 7.0 | 2026-11-10 | Use after free in Windows NetBIOS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119874 | 7.0 | 2026-11-10 | Use after free in Windows Device Association Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119876 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows USB Scanner Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119880 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Microsoft XPS Document Converter allows an unauthorized attacker to execute code over a ne |
| CVE-2026-119881 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft XPS Document Converter allows an unauthorized attacker to elevate privileges ove |
| CVE-2026-119886 | 7.8 | 2026-11-10 | Missing authentication for critical function in Windows Telephony Service allows an authorized attacker to elevate privi |
| CVE-2026-119888 | 7.0 | 2026-11-10 | Use after free in Windows Audio Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119892 | 7.8 | 2026-11-10 | Incorrect authorization in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119893 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Audio Service all |
| CVE-2026-119894 | 7.0 | 2026-11-10 | Use after free in Windows Audio Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119895 | 7.0 | 2026-11-10 | Use after free in Windows Audio Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119898 | 7.0 | 2026-11-10 | Null pointer dereference in Windows PrintWorkflowUserSvc allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119899 | 7.8 | 2026-11-10 | Improper access control in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119900 | 7.3 | 2026-11-10 | Out-of-bounds read in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119903 | 7.8 | 2026-11-10 | Improper access control in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119904 | 7.8 | 2026-11-10 | Improper control of generation of code ('code injection') in Microsoft Windows Speech allows an authorized attacker to e |
| CVE-2026-119906 | 7.8 | 2026-11-10 | Improper neutralization of special elements used in an os command ('os command injection') in Windows Sandbox allows an  |
| CVE-2026-119907 | 7.8 | 2026-11-10 | Untrusted pointer dereference in Windows Function Discovery Resource Publication allows an authorized attacker to elevat |
| CVE-2026-119908 | 8.8 | 2026-11-10 | Integer underflow (wrap or wraparound) in Windows Storage Spaces Controller allows an unauthorized attacker to execute c |
| CVE-2026-119913 | 7.0 | 2026-11-10 | Improper link resolution before file access ('link following') in Windows Print Spooler Components allows an authorized  |
| CVE-2026-119916 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Input System allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119917 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Distributed Transaction Coordinator allows an authorized attacker to elevate privi |
| CVE-2026-119919 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Distributed Transaction Coordinator allows an authorized attacker to elevate privi |
| CVE-2026-119921 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Microsoft Account Sign-in Assistant allows an authorized attacker to elevate privi |
| CVE-2026-119925 | 8.8 | 2026-11-10 | Out-of-bounds read in Windows Text Services Framework allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119928 | 7.0 | 2026-11-10 | Use after free in Windows PrintWorkflowUserSvc allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119929 | 7.8 | 2026-11-10 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119931 | 7.0 | 2026-11-10 | Time-of-check time-of-use (toctou) race condition in Windows Text Services Framework allows an authorized attacker to el |
| CVE-2026-119932 | 7.5 | 2026-11-10 | Null pointer dereference in Windows Remote Desktop allows an unauthorized attacker to deny service over a network. |
| CVE-2026-119933 | 7.8 | 2026-11-10 | Use of uninitialized resource in Windows NTFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119934 | 8.8 | 2026-11-10 | Double free in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119938 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Windows Shell allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119939 | 7.8 | 2026-11-10 | Improper privilege management in Windows Print Spooler Components allows an authorized attacker to elevate privileges lo |
| CVE-2026-119941 | 7.8 | 2026-11-10 | Untrusted pointer dereference in Windows Volume Shadow Copy allows an unauthorized attacker to elevate privileges locall |
| CVE-2026-119943 | 7.8 | 2026-11-10 | Buffer over-read in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119944 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Windows Mobile Device Management allows an unauthorized attacker to elevate privileges ove |
| CVE-2026-119945 | 8.1 | 2026-11-10 | Use after free in Windows Modern Device Management (MDM) allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119947 | 7.5 | 2026-11-10 | Use after free in Windows Hyper-V allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119948 | 7.5 | 2026-11-10 | Stack-based buffer overflow in Windows Active Directory allows an authorized attacker to execute code over a network. |
| CVE-2026-119950 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Print Spooler Components allows an unauthorized attacker to elevate privileges ove |
| CVE-2026-119951 | 8.1 | 2026-11-10 | Use after free in Windows Deployment Services allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119952 | 8.1 | 2026-11-10 | Observable timing discrepancy in Windows Schannel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119953 | 7.8 | 2026-11-10 | Use after free in Windows DNS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119954 | 7.8 | 2026-11-10 | Absolute path traversal in Microsoft Windows Search Component allows an authorized attacker to elevate privileges locall |
| CVE-2026-119957 | 7.8 | 2026-11-10 | Double free in Windows Remote Desktop Services allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119958 | 9.8 | 2026-11-10 | Out-of-bounds write in Windows LDAP - Lightweight Directory Access Protocol allows an unauthorized attacker to execute c |
| CVE-2026-119960 | 7.5 | 2026-11-10 | Use of uninitialized resource in Windows Hyper-V allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119961 | 8.1 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Internet Informat |
| CVE-2026-119962 | 8.1 | 2026-11-10 | Double free in Windows Cred SSProvider Protocol allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119963 | 8.1 | 2026-11-10 | Double free in Windows Message Queuing allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119964 | 8.1 | 2026-11-10 | Double free in Windows Message Queuing allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119966 | 7.5 | 2026-11-10 | Integer overflow or wraparound in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119967 | 8.1 | 2026-11-10 | Use after free in Windows Message Queuing Queue Manager allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119969 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Graphic Fonts allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119974 | 7.0 | 2026-11-10 | Time-of-check time-of-use (toctou) race condition in Windows Cloud Files Mini Filter Driver allows an authorized attacke |
| CVE-2026-119975 | 8.8 | 2026-11-10 | Improper neutralization of input during web page generation ('cross-site scripting') in Visual Studio Code allows an una |
| CVE-2026-119981 | 7.0 | 2026-11-10 | Missing authentication for critical function in Visual Studio Code allows an authorized attacker to elevate privileges l |
| CVE-2026-119983 | 8.8 | 2026-11-10 | Server-side request forgery (ssrf) in Visual Studio Code allows an unauthorized attacker to bypass a security feature ov |
| CVE-2026-119985 | 8.3 | 2026-11-10 | Incorrect authorization in Visual Studio Code allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119986 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119987 | 7.8 | 2026-11-10 | Untrusted search path in Microsoft Windows App Store allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119988 | 7.1 | 2026-11-10 | Numeric truncation error in Windows SMB allows an authorized attacker to execute code over a network. |
| CVE-2026-119989 | 8.2 | 2026-11-10 | Improper neutralization of special elements used in a command ('command injection') in Azure Pipelines allows an authori |
| CVE-2026-119990 | 9.8 | 2026-11-10 | Missing authentication for critical function in Azure OpenAI allows an unauthorized attacker to elevate privileges over  |
| CVE-2026-119992 | 7.0 | 2026-11-10 | Double free in Windows HTTP.sys allows an authorized attacker to elevate privileges locally. |
| CVE-2026-119995 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119996 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-119997 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code locally. |
| CVE-2026-120000 | 7.5 | 2026-11-10 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-120001 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office PowerPoint allows an unauthorized attacker to execute code over a network |
| CVE-2026-120002 | 9.9 | 2026-11-10 | Incorrect authorization in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over a networ |
| CVE-2026-120003 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code over a network. |
| CVE-2026-120005 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office PowerPoint allows an unauthorized attacker to execute code over a network |
| CVE-2026-120006 | 7.5 | 2026-11-10 | Insertion of sensitive information into sent data in .NET Aspire allows an authorized attacker to elevate privileges loc |
| CVE-2026-120778 | 7.3 | 2026-11-10 | Creation of temporary file in directory with insecure permissions in .NET Aspire allows an authorized attacker to elevat |
| CVE-2026-120779 | 9.6 | 2026-11-10 | Improper control of generation of code ('code injection') in Visual Studio Code allows an unauthorized attacker to execu |
| CVE-2026-120780 | 8.3 | 2026-11-10 | Improper access control in Visual Studio Code allows an unauthorized attacker to execute code over a network. |
| CVE-2026-120782 | 7.8 | 2026-11-10 | Improper control of generation of code ('code injection') in Visual Studio Code allows an unauthorized attacker to bypas |
| CVE-2026-120785 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-120786 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-120788 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-120789 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-120790 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-120791 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-120792 | 7.3 | 2026-11-10 | Insertion of sensitive information into log file in Aspire allows an authorized attacker to disclose information locally |
| CVE-2026-121660 | 7.5 | 2026-11-10 | Incomplete list of disallowed inputs in Visual Studio Code allows an unauthorized attacker to bypass a security feature  |
| CVE-2026-121661 | 7.8 | 2026-11-10 | Incomplete list of disallowed inputs in Visual Studio Code allows an unauthorized attacker to bypass a security feature  |
| CVE-2026-121662 | 8.6 | 2026-11-10 | Improper neutralization of special elements used in a command ('command injection') in Visual Studio Code allows an unau |
| CVE-2026-121663 | 8.8 | 2026-11-10 | Incomplete list of disallowed inputs in Visual Studio Code allows an unauthorized attacker to bypass a security feature  |
| CVE-2026-121664 | 8.3 | 2026-11-10 | Improper neutralization of input during web page generation ('cross-site scripting') in Visual Studio Code allows an una |
| CVE-2026-121665 | 8.8 | 2026-11-10 | Trust boundary violation in Visual Studio Code allows an unauthorized attacker to bypass a security feature over a netwo |
| CVE-2026-121668 | 7.7 | 2026-11-10 | Missing authorization in Azure Confidential Clean Rooms allows an authorized attacker to perform tampering over a networ |
| CVE-2026-121670 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Overlay Filter al |
| CVE-2026-121671 | 7.0 | 2026-11-10 | Use after free in Windows Audio Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-121673 | 7.8 | 2026-11-10 | Use after free in Windows Filter Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-121680 | 7.5 | 2026-11-10 | Exposure of sensitive information to an unauthorized actor in Windows NTLM allows an unauthorized attacker to perform sp |
| CVE-2026-121681 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Trace Data Helper allows an authorized attacker to elevate privileges locally. |
| CVE-2026-122163 | 7.5 | 2026-11-10 | Double free in Windows Image Acquisition allows an unauthorized attacker to execute code over a network. |
| CVE-2026-122164 | 8.0 | 2026-11-10 | Weak authentication in Windows Kerberos allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-122165 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Client for NFS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-122166 | 7.8 | 2026-11-10 | Stack-based buffer overflow in Windows Remote Desktop Services allows an authorized attacker to elevate privileges local |
| CVE-2026-122168 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Windows Media Foundation allows an authorized attacker to elevate privileges loc |
| CVE-2026-122169 | 7.5 | 2026-11-10 | Insufficient granularity of access control in Windows IKE Extension allows an authorized attacker to perform spoofing lo |
| CVE-2026-122170 | 7.0 | 2026-11-10 | Use after free in Windows Win32K allows an authorized attacker to elevate privileges locally. |
| CVE-2026-122171 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft XPS Document Converter allows an unauthorized attacker to execute code over a ne |
| CVE-2026-122172 | 7.8 | 2026-11-10 | Use after free in Microsoft Trace Data Helper allows an authorized attacker to elevate privileges locally. |
| CVE-2026-122174 | 7.0 | 2026-11-10 | Improper link resolution before file access ('link following') in Windows Task Scheduler allows an authorized attacker t |
| CVE-2026-122175 | 7.0 | 2026-11-10 | Use after free in Windows Autopilot allows an authorized attacker to elevate privileges locally. |
| CVE-2026-122176 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows SMB allows an authorized attacker to execute code over a network. |
| CVE-2026-122177 | 7.5 | 2026-11-10 | Improper link resolution before file access ('link following') in Windows iSCSI allows an unauthorized attacker to eleva |
| CVE-2026-122179 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Internet Connection Sharing (ICS) allows an authorized attacker to elevate privile |
| CVE-2026-122182 | 7.0 | 2026-11-10 | Improper link resolution before file access ('link following') in Windows Maps allows an authorized attacker to elevate  |
| CVE-2026-122183 | 7.8 | 2026-11-10 | Out-of-bounds read in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-122194 | 8.8 | 2026-11-10 | Null pointer dereference in Microsoft Defender allows an unauthorized attacker to execute code over a network. |
| CVE-2026-122198 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code over a network. |
| CVE-2026-122475 | 8.8 | 2026-11-10 | Untrusted pointer dereference in Windows Storage Spaces Controller allows an unauthorized attacker to execute code over  |
| CVE-2026-122979 | 8.1 | 2026-11-10 | Improper control of generation of code ('code injection') in Microsoft Teams for Android allows an unauthorized attacker |
| CVE-2026-122984 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Universal Disk Format File System Driver (UDFS) allows an authorized attacker to e |
| CVE-2026-122986 | 7.8 | 2026-11-10 | Improper privilege management in Microsoft Azure Kubernetes Service allows an authorized attacker to elevate privileges  |
| CVE-2026-122988 | 8.0 | 2026-11-10 | Improper authorization in Windows Admin Center allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-123375 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-123376 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-123377 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-123378 | 7.5 | 2026-11-10 | Integer overflow or wraparound in Microsoft Office Outlook allows an unauthorized attacker to execute code over a networ |
| CVE-2026-123379 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-123380 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-123381 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-123382 | 8.8 | 2026-11-10 | Untrusted pointer dereference in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network |
| CVE-2026-123383 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-123384 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network. |
| CVE-2026-123385 | 8.8 | 2026-11-10 | Stack-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-123387 | 8.0 | 2026-11-10 | Improper neutralization of special elements used in a command ('command injection') in Windows Active Directory allows a |
| CVE-2026-123388 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Program Compatibility Assistant Service allows an authorized attacker to elevate p |
| CVE-2026-123389 | 7.0 | 2026-11-10 | Use after free in Quality Windows Audio/Video Experience (QWAVE) service allows an authorized attacker to elevate privil |
| CVE-2026-123390 | 8.8 | 2026-11-10 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-123391 | 8.8 | 2026-11-10 | Incorrect authorization in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over a networ |
| CVE-2026-123394 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-124170 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-124174 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-124176 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-124185 | 7.5 | 2026-11-10 | Use of uninitialized resource in Microsoft Office Word allows an unauthorized attacker to execute code over a network. |
| CVE-2026-124187 | 8.8 | 2026-11-10 | Use after free in Microsoft Office Excel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-124224 | 7.0 | 2026-11-10 | Improper link resolution before file access ('link following') in Windows PowerShell allows an authorized attacker to el |
| CVE-2026-124225 | 7.8 | 2026-11-10 | Improper control of generation of code ('code injection') in Windows PowerShell allows an unauthorized attacker to execu |
| CVE-2026-124226 | 8.8 | 2026-11-10 | Execution with unnecessary privileges in Windows PowerShell allows an authorized attacker to bypass a security feature l |
| CVE-2026-124227 | 7.5 | 2026-11-10 | Use of uninitialized resource in Microsoft Office Outlook allows an unauthorized attacker to execute code over a network |
| CVE-2026-124228 | 8.8 | 2026-11-10 | Improper limitation of a pathname to a restricted directory ('path traversal') in Microsoft Office Outlook allows an aut |
| CVE-2026-125134 | 7.5 | 2026-11-10 | Use after free in Windows Function Discovery Resource Publication allows an unauthorized attacker to execute code over a |
| CVE-2026-125136 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Network Connected Devices Auto-Setup Service allows an unauthorized attacker to ex |
| CVE-2026-125137 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-125327 | 7.5 | 2026-11-10 | pgEdge RAG Server is an API server for retrieval-augmented generation over PostgreSQL content using pgvector. Prior to 2 |
| CVE-2026-125330 | 7.5 | 2026-11-10 | HarnessRouter is a self-hosted unified API for agent harnesses. From version 0.4.2 until 0.31.7, routes that accept a se |
| CVE-2026-125331 | 9.1 | 2026-11-10 | HarnessRouter is a self-hosted unified API for running agent harnesses with sessions, streaming, files, cancellation, an |
| CVE-2026-125336 | 7.4 | 2026-11-10 | Forge (also called node-forge) is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.3, pki |
| CVE-2026-126087 | 8.8 | 2026-11-10 | Untrusted search path in the cross-user process launcher in Open Job Description (OpenJD) Sessions for Python before 0.1 |
| CVE-2026-40275 | 8.4 | 2026-11-10 | Heap-based Buffer Overflow in the DCMD_PROC_EVENT handler of the procnto could allow an attacker with local access to ca |
| CVE-2026-54436 | 7.4 | 2026-11-10 | Heap-based Buffer
Overflow in the io-char library's DCMD_CHR_WAITINFO devctl() handler could
allow an attacker with loca |
| CVE-2026-62903 | 7.4 | 2026-11-10 | Authentication bypass by capture-replay in SQL Server allows an unauthorized attacker to disclose information over a net |
| CVE-2026-66801 | 9.8 | 2026-11-10 | Heap-based buffer overflow in Xbox allows an unauthorized attacker to execute code over a network. |
| CVE-2026-66813 | 8.1 | 2026-11-10 | Out-of-bounds read in SQL Server allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-67372 | 8.8 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-67374 | 8.8 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-67375 | 8.8 | 2026-11-10 | Stack-based buffer overflow in SQL Server allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-67387 | 8.8 | 2026-11-10 | Untrusted pointer dereference in SQL Server allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-67391 | 8.8 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-67632 | 8.8 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-67637 | 8.8 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-67646 | 8.8 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-69327 | 7.4 | 2026-11-10 | Use after free in Remote Desktop Gateway Service allows an unauthorized attacker to execute code locally. |
| CVE-2026-69565 | 7.0 | 2026-11-10 | Use after free in Remote Desktop Gateway Service allows an authorized attacker to execute code locally. |
| CVE-2026-69901 | 7.5 | 2026-11-10 | Origin validation error in Microsoft Teams for Android allows an unauthorized attacker to perform spoofing over a networ |
| CVE-2026-70003 | 8.7 | 2026-11-10 | Improper verification of cryptographic signature in JDBC Driver for SQL Server allows an unauthorized attacker to bypass |
| CVE-2026-70094 | 8.8 | 2026-11-10 | Untrusted search path in Visual Studio Code allows an unauthorized attacker to execute code over a network. |
| CVE-2026-70120 | 7.0 | 2026-11-10 | Use after free in Microsoft Bluetooth Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70182 | 7.8 | 2026-11-10 | Weak authentication in Windows Bind Filter Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-70231 | 7.0 | 2026-11-10 | Use after free in Windows Local Security Authority Subsystem Service (LSASS) allows an authorized attacker to elevate pr |
| CVE-2026-70240 | 7.5 | 2026-11-10 | Missing release of memory after effective lifetime in Windows Kerberos allows an unauthorized attacker to deny service o |
| CVE-2026-72998 | 8.1 | 2026-11-10 | Use after free in Windows DHCP Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-80094 | 7.5 | 2026-11-10 | Use after free in Remote Desktop Gateway Service allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-80095 | 9.0 | 2026-11-10 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-81384 | 8.1 | 2026-11-10 | Heap-based buffer overflow in DNS Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-83563 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Winlogon allows an authorized attacker to elevate privileges locally. |
| CVE-2026-83684 | 7.5 | 2026-11-10 | Buffer over-read in Windows iSCSI Target Service allows an unauthorized attacker to disclose information over a network. |
| CVE-2026-83894 | 7.0 | 2026-11-10 | Use after free in RPC Runtime allows an authorized attacker to elevate privileges locally. |
| CVE-2026-84010 | 7.5 | 2026-11-10 | Exposed dangerous method or function in SQL Server allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-85801 | 7.8 | 2026-11-10 | Use after free in Windows Local Security Authority Subsystem Service (LSASS) allows an authorized attacker to elevate pr |
| CVE-2026-85838 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft WDAC OLE DB provider for SQL allows an unauthorized attacker to execute code ove |
| CVE-2026-85839 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft WDAC OLE DB provider for SQL allows an unauthorized attacker to execute code ove |
| CVE-2026-85844 | 9.8 | 2026-11-10 | Authentication bypass using an alternate path or channel in Windows Kerberos allows an unauthorized attacker to elevate  |
| CVE-2026-85862 | 7.0 | 2026-11-10 | Double free in Windows Error Reporting allows an authorized attacker to elevate privileges locally. |
| CVE-2026-85923 | 8.8 | 2026-11-10 | Authorization bypass through user-controlled key in Azure DevOps Server allows an authorized attacker to elevate privile |
| CVE-2026-85929 | 7.8 | 2026-11-10 | Incorrect permission assignment for critical resource in Windows Brokering File System allows an authorized attacker to  |
| CVE-2026-85942 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Camera Frame Server Monitor allows an authorized attacker to elevate privileges lo |
| CVE-2026-88111 | 7.5 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-88176 | 8.8 | 2026-11-10 | Missing authorization in Microsoft Office SharePoint allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-88187 | 8.0 | 2026-11-10 | Heap-based buffer overflow in Windows Bluetooth A2DP driver allows an authorized attacker to elevate privileges over an  |
| CVE-2026-88212 | 7.5 | 2026-11-10 | Use after free in Windows Network Address Translation (NAT) allows an unauthorized attacker to execute code over an adja |
| CVE-2026-88213 | 7.8 | 2026-11-10 | Numeric truncation error in Windows Bluetooth Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88216 | 7.5 | 2026-11-10 | Time-of-check time-of-use (toctou) race condition in Windows DHCP Server allows an authorized attacker to execute code o |
| CVE-2026-88218 | 9.8 | 2026-11-10 | Double free in Windows DNS allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88221 | 7.0 | 2026-11-10 | Use after free in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88222 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft WDAC OLE DB provider for SQL allows an unauthorized attacker to execute code ove |
| CVE-2026-88224 | 7.0 | 2026-11-10 | Improper link resolution before file access ('link following') in Windows AppX Deployment Service allows an authorized a |
| CVE-2026-88227 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Local Security Authority Subsystem Service (LSASS) allows an authorized attacker t |
| CVE-2026-88228 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Local Security Authority Subsystem Service (LSASS) allows an authorized attacker t |
| CVE-2026-88229 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Media Player allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88230 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows LUAFV allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88232 | 7.8 | 2026-11-10 | Use after free in Windows Camera Frame Server Monitor allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88233 | 7.8 | 2026-11-10 | Improper authorization in Windows Task Scheduler allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88234 | 9.8 | 2026-11-10 | Release of invalid pointer or reference in Windows iSCSI allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88235 | 7.8 | 2026-11-10 | Unintended proxy or intermediary ('confused deputy') in Servicing Stack Updates allows an authorized attacker to elevate |
| CVE-2026-88236 | 7.5 | 2026-11-10 | Null pointer dereference in Microsoft QUIC allows an unauthorized attacker to deny service over a network. |
| CVE-2026-88237 | 7.0 | 2026-11-10 | Use after free in Windows Subsystem for Linux allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88238 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Camera Frame Server Monitor allows an authorized attacker to elevate privileges lo |
| CVE-2026-88239 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Biometric Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88240 | 8.0 | 2026-11-10 | Heap-based buffer overflow in Windows DHCP Client allows an authorized attacker to elevate privileges over an adjacent n |
| CVE-2026-88241 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Sensor Data Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-88242 | 7.0 | 2026-11-10 | Use after free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges loca |
| CVE-2026-88243 | 9.8 | 2026-11-10 | Out-of-bounds read in Windows DHCP Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-88244 | 7.5 | 2026-11-10 | Use after free in Windows Link Layer Topology Discovery Protocol allows an unauthorized attacker to execute code over an |
| CVE-2026-88245 | 7.8 | 2026-11-10 | Missing authentication for critical function in Windows Brokering File System allows an authorized attacker to elevate p |
| CVE-2026-88249 | 8.8 | 2026-11-10 | Use after free in Windows Client for NFS allows an unauthorized attacker to execute code over a network. |
| CVE-2026-94507 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows DirectX allows an authorized attacker to elevate privileges locally. |
| CVE-2026-94511 | 8.8 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to execute code over a network. |
| CVE-2026-94513 | 8.0 | 2026-11-10 | Heap-based buffer overflow in SQL Server allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-94514 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Kernel allows an  |
| CVE-2026-94515 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Advanced Rasterization Platform allows an authorized attacker to elevate privilege |
| CVE-2026-94519 | 7.0 | 2026-11-10 | Use after free in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-94522 | 7.0 | 2026-11-10 | Use after free in Kernel Transaction Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-94525 | 7.0 | 2026-11-10 | An elevation of privilege vulnerability exists in Windows Error Reporting (WER) when WER handles and executes files. The |
| CVE-2026-94527 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows GDI allows an authorized attacker to elevate privileges locally. |
| CVE-2026-94529 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges loc |
| CVE-2026-94531 | 7.8 | 2026-11-10 | Stack-based buffer overflow in Windows COM allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95871 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Broadcast DVR User Service allows an authorized attacker to elevate privileges loc |
| CVE-2026-95872 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows USB Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95874 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Xbox allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95876 | 7.0 | 2026-11-10 | Use after free in Windows Local Session Manager (LSM) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95877 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Biometric Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95879 | 7.8 | 2026-11-10 | Out-of-bounds read in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95881 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Push Notifications allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95882 | 9.8 | 2026-11-10 | Stack-based buffer overflow in Windows Microsoft DirectMusic allows an unauthorized attacker to execute code over a netw |
| CVE-2026-95885 | 8.1 | 2026-11-10 | Use after free in Windows Client for NFS allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-95888 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95891 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Microsoft DirectMusic allows an authorized attacker to execute code locally. |
| CVE-2026-95894 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Task Scheduler allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95895 | 7.8 | 2026-11-10 | Use after free in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95896 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Microsoft DirectMusic allows an authorized attacker to execute code locally. |
| CVE-2026-95898 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows iSCSI allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95901 | 9.8 | 2026-11-10 | Double free in Windows Microsoft DirectMusic allows an unauthorized attacker to execute code over a network. |
| CVE-2026-95902 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows USB Hub Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95906 | 7.0 | 2026-11-10 | Out-of-bounds read in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95909 | 7.8 | 2026-11-10 | Out-of-bounds read in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95920 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Management Instrumentation allows an authorized attacker to elevate privileges loc |
| CVE-2026-95922 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95923 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows HTTP.sys allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95932 | 7.8 | 2026-11-10 | Inclusion of functionality from untrusted control sphere in Windows Graphics Kernel allows an authorized attacker to ele |
| CVE-2026-95933 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows OLE allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95934 | 7.8 | 2026-11-10 | Double free in Windows Diagnostic Policy Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95935 | 7.8 | 2026-11-10 | Integer overflow or wraparound in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95938 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95942 | 7.8 | 2026-11-10 | Out-of-bounds read in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95947 | 7.8 | 2026-11-10 | An elevation of privilege vulnerability exists in Windows Error Reporting (WER) when WER handles and executes files. The |
| CVE-2026-95948 | 7.8 | 2026-11-10 | Stack-based buffer overflow in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95950 | 7.0 | 2026-11-10 | Out-of-bounds read in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95951 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95953 | 7.8 | 2026-11-10 | Out-of-bounds read in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95956 | 8.1 | 2026-11-10 | Use after free in Windows eSCL Scanner allows an unauthorized attacker to execute code over a network. |
| CVE-2026-95960 | 8.8 | 2026-11-10 | Access of resource using incompatible type ('type confusion') in Windows Advanced Rasterization Platform allows an autho |
| CVE-2026-95961 | 7.0 | 2026-11-10 | Double free in Windows USB Video Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95962 | 9.0 | 2026-11-10 | Use after free in Windows Virtual Filtering Platform (VFP) allows an unauthorized attacker to execute code over a networ |
| CVE-2026-95963 | 7.8 | 2026-11-10 | Improper link resolution before file access ('link following') in Data Sharing Service Client allows an authorized attac |
| CVE-2026-95964 | 7.5 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Remote Desktop Client all |
| CVE-2026-95965 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows USB Video Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95966 | 7.0 | 2026-11-10 | Use after free in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95968 | 7.0 | 2026-11-10 | Use after free in Windows Smart Card allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95971 | 7.0 | 2026-11-10 | Untrusted pointer dereference in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95973 | 7.0 | 2026-11-10 | Untrusted pointer dereference in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95974 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95975 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Performance Counters allows an unauthorized attacker to execute code over a networ |
| CVE-2026-95976 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Diagnostic Policy |
| CVE-2026-95979 | 7.0 | 2026-11-10 | Use after free in Windows Brokering File System allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95983 | 7.8 | 2026-11-10 | Untrusted pointer dereference in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95987 | 7.0 | 2026-11-10 | Use after free in Windows User Manager Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95988 | 7.8 | 2026-11-10 | Incorrect authorization in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95989 | 7.0 | 2026-11-10 | Use after free in vhdmp.sys allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95991 | 7.8 | 2026-11-10 | Use after free in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95996 | 8.8 | 2026-11-10 | Integer underflow (wrap or wraparound) in Windows Bluetooth Port Driver allows an authorized attacker to elevate privile |
| CVE-2026-95997 | 7.8 | 2026-11-10 | Use after free in Windows Event Logging Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-95999 | 7.8 | 2026-11-10 | Out-of-bounds read in Windows USB Hub Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96002 | 8.8 | 2026-11-10 | Heap-based buffer overflow in DNS Server allows an authorized attacker to execute code over a network. |
| CVE-2026-96004 | 7.0 | 2026-11-10 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96005 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows USB Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96007 | 7.0 | 2026-11-10 | Use after free in Connected Devices Platform Service (Cdpsvc) allows an authorized attacker to elevate privileges locall |
| CVE-2026-96008 | 7.0 | 2026-11-10 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96010 | 8.8 | 2026-11-10 | Integer underflow (wrap or wraparound) in HID Parser Library allows an authorized attacker to elevate privileges over a  |
| CVE-2026-96016 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Local Security Authority Subsystem Service (LSASS) allows an authorized attacker t |
| CVE-2026-96019 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Installer allows  |
| CVE-2026-96020 | 8.8 | 2026-11-10 | Out-of-bounds write in DNS Server allows an authorized attacker to execute code over a network. |
| CVE-2026-96023 | 7.8 | 2026-11-10 | Use after free in Windows Push Notification Core allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96026 | 7.0 | 2026-11-10 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96027 | 7.0 | 2026-11-10 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96028 | 7.8 | 2026-11-10 | Access of resource using incompatible type ('type confusion') in Windows Installer allows an authorized attacker to elev |
| CVE-2026-96029 | 7.8 | 2026-11-10 | Improper access control in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96031 | 7.8 | 2026-11-10 | Out-of-bounds write in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96035 | 7.0 | 2026-11-10 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96036 | 7.8 | 2026-11-10 | Integer overflow or wraparound in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96037 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows User Manager Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96038 | 7.8 | 2026-11-10 | Inclusion of functionality from untrusted control sphere in Windows Audio Service allows an authorized attacker to eleva |
| CVE-2026-96042 | 7.0 | 2026-11-10 | Use after free in Windows Connection Manager Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96043 | 7.0 | 2026-11-10 | Use after free in Windows Connection Manager Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96046 | 7.0 | 2026-11-10 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96047 | 7.0 | 2026-11-10 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96051 | 7.0 | 2026-11-10 | Out-of-bounds read in Windows USB Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96052 | 7.8 | 2026-11-10 | Integer underflow (wrap or wraparound) in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96053 | 7.8 | 2026-11-10 | Improper neutralization of special elements used in a command ('command injection') in Windows Task Scheduler allows an  |
| CVE-2026-96054 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Microsoft Color Management allows an unauthorized attacker to execute code locally. |
| CVE-2026-96055 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows USB Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96056 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows USB Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96057 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows USB Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96060 | 7.8 | 2026-11-10 | Out-of-bounds read in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96061 | 7.0 | 2026-11-10 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96062 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96064 | 8.8 | 2026-11-10 | Heap-based buffer overflow in DNS Server allows an authorized attacker to execute code over a network. |
| CVE-2026-96066 | 7.8 | 2026-11-10 | Stack-based buffer overflow in Windows Local Security Authority Subsystem Service (LSASS) allows an authorized attacker  |
| CVE-2026-96067 | 9.8 | 2026-11-10 | Integer overflow or wraparound in Microsoft Color Management allows an unauthorized attacker to execute code over a netw |
| CVE-2026-96072 | 7.0 | 2026-11-10 | Use after free in Windows Connected User Experiences and Telemetry allows an authorized attacker to elevate privileges l |
| CVE-2026-96073 | 7.0 | 2026-11-10 | Use after free in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96074 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows AppX Package Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96075 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Feedback Hub allo |
| CVE-2026-96076 | 7.8 | 2026-11-10 | Use after free in Windows DIAL Client allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96077 | 7.5 | 2026-11-10 | Null pointer dereference in Windows TCP/IP allows an unauthorized attacker to deny service over a network. |
| CVE-2026-96078 | 9.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Color Management allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96081 | 7.5 | 2026-11-10 | Heap-based buffer overflow in Windows Rich Text Edit Control allows an unauthorized attacker to execute code over a netw |
| CVE-2026-96084 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Graphic Fonts allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96085 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96088 | 7.0 | 2026-11-10 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Connected User Ex |
| CVE-2026-96092 | 8.1 | 2026-11-10 | Use after free in DNS Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96097 | 7.0 | 2026-11-10 | Release of invalid pointer or reference in Windows Brokering File System allows an authorized attacker to elevate privil |
| CVE-2026-96102 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows TCP/IP allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96103 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Desktop Window Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96107 | 7.0 | 2026-11-10 | Null pointer dereference in Windows Phone Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96115 | 8.0 | 2026-11-10 | Double free in Windows DHCP Client allows an authorized attacker to elevate privileges over an adjacent network. |
| CVE-2026-96117 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows LUAFV allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96122 | 7.8 | 2026-11-10 | Untrusted pointer dereference in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96124 | 7.0 | 2026-11-10 | Use after free in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96126 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96127 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Biometric Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96129 | 7.8 | 2026-11-10 | Inclusion of functionality from untrusted control sphere in Windows Kernel allows an authorized attacker to elevate priv |
| CVE-2026-96134 | 7.5 | 2026-11-10 | Uncontrolled resource consumption in Windows DHCP Server allows an unauthorized attacker to deny service over a network. |
| CVE-2026-96139 | 7.0 | 2026-11-10 | Untrusted pointer dereference in Windows Kernel-Mode Drivers allows an authorized attacker to elevate privileges locally |
| CVE-2026-96152 | 7.8 | 2026-11-10 | Stack-based buffer overflow in Windows Installer allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96153 | 7.0 | 2026-11-10 | Heap-based buffer overflow in Windows Error Reporting allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96155 | 7.0 | 2026-11-10 | Use after free in Windows Audio Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96157 | 9.8 | 2026-11-10 | Heap-based buffer overflow in Microsoft Windows Media Foundation allows an unauthorized attacker to execute code over a  |
| CVE-2026-96158 | 7.0 | 2026-11-10 | Use of uninitialized resource in Microsoft ActiveX Installer Service allows an authorized attacker to elevate privileges |
| CVE-2026-96160 | 7.8 | 2026-11-10 | Out-of-bounds read in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96162 | 7.8 | 2026-11-10 | Incorrect authorization in Windows Clipboard Virtual Channel Extension allows an authorized attacker to elevate privileg |
| CVE-2026-96164 | 8.8 | 2026-11-10 | Heap-based buffer overflow in Windows Imaging Component allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96168 | 7.0 | 2026-11-10 | Untrusted pointer dereference in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96171 | 7.0 | 2026-11-10 | Use after free in Windows Graphics Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96172 | 7.8 | 2026-11-10 | No cwe for this issue in Desktop Window Manager allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96174 | 7.8 | 2026-11-10 | Release of invalid pointer or reference in Desktop Window Manager allows an authorized attacker to elevate privileges lo |
| CVE-2026-96175 | 7.8 | 2026-11-10 | Release of invalid pointer or reference in Desktop Window Manager allows an authorized attacker to elevate privileges lo |
| CVE-2026-96176 | 7.5 | 2026-11-10 | Missing release of memory after effective lifetime in Windows DNS allows an unauthorized attacker to deny service over a |
| CVE-2026-96177 | 8.1 | 2026-11-10 | Use after free in DNS Server allows an unauthorized attacker to execute code over a network. |
| CVE-2026-96184 | 7.8 | 2026-11-10 | Heap-based buffer overflow in Windows Modern Device Management (MDM) allows an authorized attacker to elevate privileges |
| CVE-2026-96845 | 7.8 | 2026-11-10 | Improper authorization in Windows Task Scheduler allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96969 | 7.0 | 2026-11-10 | Double free in Windows TCP/IP allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96971 | 7.0 | 2026-11-10 | Use after free in Windows NetBIOS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96972 | 7.5 | 2026-11-10 | Out-of-bounds read in Windows DNS allows an unauthorized attacker to disclose information over a network. |
| CVE-2026-96973 | 7.0 | 2026-11-10 | Use after free in Windows Encrypting File System (EFS) allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96978 | 7.0 | 2026-11-10 | Use after free in Windows Credential User Interface allows an authorized attacker to elevate privileges locally. |
| CVE-2026-96993 | 7.5 | 2026-11-10 | Release of invalid pointer or reference in Windows Performance Monitor allows an unauthorized attacker to execute code o |
| CVE-2026-96994 | 7.0 | 2026-11-10 | Use after free in Winsock allows an authorized attacker to elevate privileges locally. |
| CVE-2026-97000 | 7.0 | 2026-11-10 | Null pointer dereference in Windows USM Communication Manager allows an authorized attacker to elevate privileges locall |
| CVE-2026-97002 | 7.5 | 2026-11-10 | Out-of-bounds read in Windows VMSwitch allows an authorized attacker to elevate privileges locally. |
| CVE-2026-97013 | 7.8 | 2026-11-10 | Access of resource using incompatible type ('type confusion') in Windows Shell allows an authorized attacker to elevate  |
| CVE-2025-61625 | 8.1 | 2026-11-10 | An improper limitation of a pathname to a restricted directory ('path traversal') vulnerability in Fortinet FortiAnalyze |
| CVE-2026-102166 | 8.8 | 2026-11-10 | Arista C-260 and C-250 access points ship with fleet-wide static cryptographic keys used for firmware image verification |
| CVE-2026-115483 | 7.5 | 2026-11-10 | The Everest Forms plugin for WordPress is vulnerable to Arbitrary File Read in all versions up to, and including, 3.6.3  |
| CVE-2026-120803 | 7.1 | 2026-11-10 | A use-after-free issue exists in MongoDB’s SBE (Slot-Based Execution) implementation of a window function accumulator us |
| CVE-2026-120804 | 7.5 | 2026-11-10 | A flaw exists in the server-side SSPI Kerberos authentication handler on Windows Enterprise builds of MongoDB. When proc |
| CVE-2026-120808 | 7.4 | 2026-11-10 | An issue exists in MongoDB's macOS TLS client implementation where certificate chain-of-trust validation is bypassed for |
| CVE-2026-120814 | 7.2 | 2026-11-10 | An improper privilege management issue in the sharding subsystem of MongoDB Server may allow a user holding certain shar |
| CVE-2026-120815 | 8.4 | 2026-11-10 | An incorrect authorization check in the MongoDB Server authorization subsystem may allow an unauthenticated party with l |
| CVE-2026-120977 | 8.2 | 2026-11-10 | On affected platforms running Arista EOS with 802.1X with Dynamic Host Configuration Protocol (DHCP) device profiling en |
| CVE-2026-120979 | 8.1 | 2026-11-10 | This vulnerability affects customers using Arista Pathfinder for WAN path selection with Border Gateway Protocol-Link St |
| CVE-2026-120982 | 7.5 | 2026-11-10 | On affected platforms running Arista EOS with Border Gateway Protocol (BGP) configured, An unauthenticated attacker who  |
| CVE-2026-120983 | 7.6 | 2026-11-10 | On affected EOS platforms where 802.1x is configured in multi-host authenticated mode and the device is configured with  |
| CVE-2026-121287 | 8.8 | 2026-11-10 | An unauthenticated attacker on an adjacent network segment can send crafted RIPv2 packets to a RIP-enabled interface on  |
| CVE-2026-121288 | 8.1 | 2026-11-10 | An unauthenticated attacker on an adjacent network segment can bypass MD5 authentication and have unauthorized RIP route |
| CVE-2026-121289 | 9.8 | 2026-11-10 | On affected platforms running Arista EOS with BGP configured, a specially crafted packet can cause the BGP agent to cras |
| CVE-2026-121290 | 8.2 | 2026-11-10 | On affected platforms running Arista EOS with Border Gateway Protocol (BGP) changing the BGP listen port from its defaul |
| CVE-2026-121291 | 8.2 | 2026-11-10 | A crafted Error Report can leave EOS stuck believing that a cache reset is in progress, preventing ROA publication, with |
| CVE-2026-121292 | 8.2 | 2026-11-10 | A malformed Error Report can cause EOS to read beyond packet boundaries, potentially terminating the RPKI agent or expos |
| CVE-2026-121295 | 8.6 | 2026-11-10 | On affected platforms running Arista EOS configured as S-BFD peers, an unauthenticated attacker could send a crafted S-B |
| CVE-2026-121367 | 9.6 | 2026-11-10 | On affected Arista EOS platforms with Routing Information Protocol version 2 (RIPv2) configured, under certain condition |
| CVE-2026-121368 | 8.6 | 2026-11-10 | On affected platforms running Arista EOS with Bidirectional Forwarding Detection (BFD) configured to use keyed MD5 or ke |
| CVE-2026-121370 | 8.6 | 2026-11-10 | On affected platforms running Arista EOS with Precision Time Protocol (PTP) configured, an unauthenticated attacker with |
| CVE-2026-121371 | 7.5 | 2026-11-10 | On affected EOS versions with the eAPI service enabled, a specially crafted HTTP request can allow an unauthenticated, r |
| CVE-2026-121529 | 9.6 | 2026-11-10 | A origin validation error vulnerability in Fortinet FortiClientMac 7.4.0 through 7.4.7, FortiClientWindows 7.4.0 through |
| CVE-2026-125337 | 8.3 | 2026-11-10 | Winter CMS is a content management system built on the Laravel PHP framework. Prior to 1.2.14, the ImportExportControlle |
| CVE-2026-26248 | 8.8 | 2026-11-10 | A improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Fortinet FortiSa |
| CVE-2026-50077 | 7.7 | 2026-11-10 | Invalid Memory Access via the MSI-X table in QVM could allow an attacker in the guest to execute arbitrary code in the Q |
| CVE-2026-58789 | 7.5 | 2026-11-10 | In s_gen_tile_param of multiple files, there is a possible way to trigger an out of bounds write in tile parameter array |
| CVE-2026-58807 | 7.5 | 2026-11-10 | In Retry_MtsMessageInPending of MtsMessageController.cpp, there is a possible way to trigger memory exhaustion via leake |
| CVE-2026-59582 | 7.5 | 2026-11-10 | In StartTimer of UcePublishManager.cpp, there is a possible way to trigger a process abort during timer calculation due  |
| CVE-2026-59585 | 7.5 | 2026-11-10 | In SetDisplayName of RegInfoContact.cpp, there is a possible denial of service due to a missing null check. This could l |
| CVE-2026-59595 | 7.5 | 2026-11-10 | In DecodeHeaderComponent of SipStack.cpp, there is a possible way to trigger stack exhaustion via unbounded mutual recur |
| CVE-2026-59603 | 7.5 | 2026-11-10 | In RespondReceivedMessage of MtsMessageController.cpp, there is a possible way to trigger a double free and process abor |
| CVE-2026-59611 | 7.5 | 2026-11-10 | In multiple locations, there is a possible way to trigger a temporary denial of service via an integer overflow trap due |
| CVE-2026-59613 | 7.5 | 2026-11-10 | In multiple locations, there is a possible way to trigger an out of bounds read and temporary denial of service due to i |
| CVE-2026-59623 | 7.5 | 2026-11-10 | In CompareTelUris of SipAddress.cpp, there is a possible way to trigger an unhandled out of range exception and process  |
| CVE-2026-59632 | 7.5 | 2026-11-10 | In RespondReceivedMessage of MtsMessageController.cpp, there is a possible way to trigger memory exhaustion via an undra |
| CVE-2026-95780 | 8.1 | 2026-11-10 | A vulnerability exists in the authentication and session-management mechanisms that may result in access not being fully |
| CVE-2026-95781 | 7.5 | 2026-11-10 | A security vulnerability exists in AthonetOS that may allow an unauthorized party to affect service operation or gain ac |
| CVE-2026-95782 | 7.5 | 2026-11-10 | A vulnerability exists in a monitoring component that may, under certain conditions, allow security controls to be circu |
| CVE-2026-95783 | 7.5 | 2026-11-10 | A vulnerability exists in a network-facing component that may, under certain conditions, result in service disruption. S |
| CVE-2026-95784 | 7.5 | 2026-11-10 | A vulnerability exists in a system component that may, under certain conditions, disrupt the availability of affected se |
| CVE-2026-95785 | 7.2 | 2026-11-10 | A vulnerability exists in a system component that may, under certain conditions, allow an authorized user to make unauth |
| CVE-2026-104352 | 7.8 | 2026-11-10 | Premiere Pro is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the co |
| CVE-2026-110085 | 7.8 | 2026-11-10 | Premiere Pro is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the co |
| CVE-2026-110086 | 7.8 | 2026-11-10 | Premiere Pro is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the co |
| CVE-2026-110088 | 7.8 | 2026-11-10 | Premiere Pro is affected by a Buffer Overflow vulnerability that could result in arbitrary code execution in the context |
| CVE-2026-110089 | 7.8 | 2026-11-10 | Premiere Pro is affected by a Buffer Underwrite ('Buffer Underflow') vulnerability that could result in arbitrary code e |
| CVE-2026-110090 | 7.1 | 2026-11-10 | Premiere Pro is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerabil |
| CVE-2026-110091 | 7.1 | 2026-11-10 | Premiere Pro is affected by a Missing Authentication for Critical Function vulnerability that could result in a Security |
| CVE-2026-113512 | 7.8 | 2026-11-10 | After Effects is affected by a Stack-based Buffer Overflow vulnerability that could result in arbitrary code execution i |
| CVE-2026-113516 | 7.8 | 2026-11-10 | After Effects is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the c |
| CVE-2026-113517 | 7.8 | 2026-11-10 | After Effects is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the c |
| CVE-2026-113523 | 7.8 | 2026-11-10 | After Effects is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the c |
| CVE-2026-113525 | 7.8 | 2026-11-10 | After Effects is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the c |
| CVE-2026-113526 | 8.6 | 2026-11-10 | After Effects is affected by a Violation of Secure Design Principles vulnerability that could result in arbitrary code e |
| CVE-2026-113528 | 7.8 | 2026-11-10 | After Effects is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the c |
| CVE-2026-113530 | 7.8 | 2026-11-10 | After Effects is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the c |
| CVE-2026-113532 | 8.6 | 2026-11-10 | After Effects is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerabi |
| CVE-2026-113534 | 8.6 | 2026-11-10 | After Effects is affected by an Improper Input Validation vulnerability that could result in arbitrary code execution in |
| CVE-2026-113536 | 7.8 | 2026-11-10 | After Effects is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the c |
| CVE-2026-113538 | 7.8 | 2026-11-10 | After Effects is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the c |
| CVE-2026-113541 | 7.8 | 2026-11-10 | Media Encoder is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the c |
| CVE-2026-113543 | 7.8 | 2026-11-10 | Media Encoder is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the c |
| CVE-2026-113545 | 7.8 | 2026-11-10 | Media Encoder is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the c |
| CVE-2026-113547 | 7.8 | 2026-11-10 | Media Encoder is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the c |
| CVE-2026-113551 | 8.7 | 2026-11-10 | Audition is affected by a Violation of Secure Design Principles vulnerability that could result in privilege escalation. |
| CVE-2026-113553 | 7.8 | 2026-11-10 | Audition is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the contex |
| CVE-2026-113555 | 7.8 | 2026-11-10 | Audition is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the contex |
| CVE-2026-113557 | 8.6 | 2026-11-10 | Audition is affected by an Improper Input Validation vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-113558 | 8.6 | 2026-11-10 | Audition is affected by an Improper Input Validation vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-113560 | 7.7 | 2026-11-10 | Audition is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the co |
| CVE-2026-113562 | 7.7 | 2026-11-10 | Audition is affected by an Improper Input Validation vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-113563 | 8.6 | 2026-11-10 | Audition is affected by a Violation of Secure Design Principles vulnerability that could result in arbitrary code execut |
| CVE-2026-113565 | 7.8 | 2026-11-10 | Audition is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the contex |
| CVE-2026-113567 | 7.8 | 2026-11-10 | Audition is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the contex |
| CVE-2026-113575 | 7.8 | 2026-11-10 | Photoshop Desktop is affected by a Heap-based Buffer Overflow vulnerability that could result in arbitrary code executio |
| CVE-2026-116003 | 7.8 | 2026-11-10 | Photoshop Desktop is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-116480 | 7.8 | 2026-11-10 | Photoshop Desktop is affected by a Heap-based Buffer Overflow vulnerability that could result in arbitrary code executio |
| CVE-2026-117546 | 7.8 | 2026-11-10 | Photoshop Desktop is affected by a Use After Free vulnerability that could result in arbitrary code execution in the con |
| CVE-2026-117547 | 7.8 | 2026-11-10 | Photoshop Desktop is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in t |
| CVE-2026-118383 | 9.0 | 2026-11-10 | A use-after-free in the replication component of MongoDB Server can occur when a newly elected replica set primary compl |
| CVE-2026-120818 | 7.1 | 2026-11-10 | A use-after-free weakness in MongoDB Server's server-side JavaScript support for aggregation may allow a stale reference |
| CVE-2026-120824 | 8.8 | 2026-11-10 | A use-after-free in the time-series collection component of MongoDB Server can occur when the server validates a time-se |
| CVE-2026-120828 | 7.5 | 2026-11-10 | A replica-set database server node does not limit or reclaim internal wait records created while handling a client-suppl |
| CVE-2026-123263 | 7.8 | 2026-11-10 | After Effects is affected by a Heap-based Buffer Overflow vulnerability that could result in arbitrary code execution in |
| CVE-2026-126065 | 9.8 | 2026-11-10 | OpenObserve is a cloud-native observability platform. Prior to 1.1.0, the shared authentication validator in src/api/com |
| CVE-2026-126080 | 7.5 | 2026-11-10 | Active Support is a collection of utility classes and standard library extensions used by Rails and other Ruby projects. |
| CVE-2026-126081 | 7.5 | 2026-11-10 | Action Pack is a framework for handling and responding to web requests. Prior to 8.1.4.1 and 8.0.5.2, ActionController:: |
| CVE-2026-126082 | 9.8 | 2026-11-10 | Active Storage makes it simple to upload and reference files in cloud services and attach those files to Active Record o |
| CVE-2026-126083 | 7.4 | 2026-11-10 | Action Pack is a framework for handling and responding to web requests. From 8.1 until 8.1.4.1, Since Rails 8.1.0, Actio |
| CVE-2026-48402 | 7.8 | 2026-11-10 | Premiere Pro is affected by an Untrusted Search Path vulnerability that could result in arbitrary code execution in the  |
| CVE-2026-82002 | 7.7 | 2026-11-10 | Media Encoder is affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in t |
| CVE-2026-82012 | 7.8 | 2026-11-10 | Premiere Pro is affected by an out-of-bounds write vulnerability that could result in arbitrary code execution in the co |
| CVE-2026-107356 | 8.8 | 2026-11-10 | U.S. Geological Survey Area Species Management Research Program (ARMI) accepts any uploaded file and stores the file und |
| CVE-2026-113579 | 9.9 | 2026-11-10 | Adobe Experience Manager is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that  |
| CVE-2026-113580 | 9.9 | 2026-11-10 | Adobe Experience Manager is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that  |
| CVE-2026-114371 | 9.9 | 2026-11-10 | Adobe Experience Manager is affected by an Incorrect Authorization vulnerability that could result in arbitrary code exe |
| CVE-2026-118483 | 8.2 | 2026-11-10 | Dimension is affected by an Improper Input Validation vulnerability that could result in arbitrary code execution in the |
| CVE-2026-119017 | 9.9 | 2026-11-10 | Adobe Experience Manager is affected by an Incorrect Authorization vulnerability that could result in arbitrary code exe |
| CVE-2026-121349 | 9.6 | 2026-11-10 | Adobe Connect is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerabi |
| CVE-2026-121350 | 7.7 | 2026-11-10 | Adobe Connect is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vul |
| CVE-2026-121351 | 10.0 | 2026-11-10 | Adobe Connect is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerabi |
| CVE-2026-121352 | 10.0 | 2026-11-10 | Adobe Connect is affected by an Incorrect Authorization vulnerability that could result in privilege escalation. An atta |
| CVE-2026-121353 | 10.0 | 2026-11-10 | Adobe Connect is affected by an Improper Neutralization of CRLF Sequences ('CRLF Injection') vulnerability that could re |
| CVE-2026-121354 | 9.9 | 2026-11-10 | Adobe Connect is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerabi |
| CVE-2026-121355 | 9.1 | 2026-11-10 | Adobe Connect is affected by an Incorrect Authorization vulnerability that could result in privilege escalation. An atta |
| CVE-2026-121356 | 10.0 | 2026-11-10 | Adobe Connect is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalatio |
| CVE-2026-121887 | 9.9 | 2026-11-10 | Adobe Connect is affected by an Improper Restriction of XML External Entity Reference ('XXE') vulnerability that could r |
| CVE-2026-121889 | 10.0 | 2026-11-10 | Adobe Connect is affected by a Server-Side Request Forgery (SSRF) vulnerability that could result in privilege escalatio |
| CVE-2026-121890 | 7.7 | 2026-11-10 | Adobe Connect is affected by an Improper Restriction of XML External Entity Reference ('XXE') vulnerability that could l |
| CVE-2026-121892 | 9.9 | 2026-11-10 | Adobe Connect is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that could resul |
| CVE-2026-121894 | 9.9 | 2026-11-10 | Adobe Connect is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vul |
| CVE-2026-121896 | 9.9 | 2026-11-10 | Adobe Connect is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vul |
| CVE-2026-121898 | 9.9 | 2026-11-10 | Adobe Connect is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vul |
| CVE-2026-121900 | 8.3 | 2026-11-10 | Adobe Connect is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vul |
| CVE-2026-121902 | 9.4 | 2026-11-10 | Adobe Connect is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vul |
| CVE-2026-121904 | 9.6 | 2026-11-10 | Adobe Connect is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by a low-privileged  |
| CVE-2026-121906 | 9.9 | 2026-11-10 | Adobe Connect is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerabi |
| CVE-2026-121908 | 9.9 | 2026-11-10 | Adobe Connect is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vul |
| CVE-2026-121913 | 8.8 | 2026-11-10 | Adobe Connect is affected by an Incorrect Authorization vulnerability that could result in privilege escalation. A low-p |
| CVE-2026-122102 | 8.7 | 2026-11-10 | Adobe Connect is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by a low-privileged  |
| CVE-2026-125297 | 9.8 | 2026-11-10 | AsiaInfo Business Support System (BSS) 9.2.0 through 9.2.40 accepts unauthenticated requests via the management API '/bs |
| CVE-2026-125298 | 9.8 | 2026-11-10 | AsiaInfo Business Support System (BSS) 9.2.0 through 9.2.40 does not correctly verify cryptographic signatures for JSON  |
| CVE-2026-126186 | 8.8 | 2026-11-10 | Active Storage makes it simple to upload and reference files in cloud services and attach those files to Active Record o |
| CVE-2026-77685 | 8.3 | 2026-11-10 | The RFCOMM multiplexer control-channel handler in subsys/bluetooth/host/classic/rfcomm.c computed the echo length for a  |
| CVE-2026-82391 | 9.1 | 2026-11-10 | The HTTP/2 front-end of the Zephyr HTTP server aliased connection receive state as a scratch output. In subsys/net/lib/h |
| CVE-2026-89324 | 9.8 | 2026-11-10 | The Basel Post Types plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including, 1 |
| CVE-2026-90833 | 7.8 | 2026-11-10 | The simulated EEPROM driver validated access ranges in eeprom_range_is_valid() (drivers/eeprom/eeprom_simulator.c) with  |
| CVE-2026-126261 | 9.8 | 2026-11-10 | A improper authorization vulnerability in Fortinet FortiManager 8.0.0, FortiManager 7.6.0 through 7.6.7, FortiManager 7. |
| CVE-2026-126497 | 7.8 | 2026-11-11 | LibreCAD through 2.2.1.6 contains a heap-based out-of-bounds write vulnerability in the bundled libdxfrw dwgReader18::pa |
| CVE-2026-126499 | 7.4 | 2026-11-11 | Jellyfin before 12.0 contains a path traversal vulnerability in the DELETE /Library/VirtualFolders and POST /Library/Vir |
| CVE-2026-126539 | 8.1 | 2026-11-11 | Directus before 12.1.0 contains an authorization bypass vulnerability that allows unauthenticated attackers to skip perm |
| CVE-2026-126541 | 8.1 | 2026-11-11 | WWBN AVideo through 29.7.1 contains a missing authorization vulnerability in Live plugin restream endpoints that allows  |
| CVE-2026-126542 | 9.8 | 2026-11-11 | WWBN AVideo 6.5 through 29.7.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to  |
| CVE-2026-126543 | 7.5 | 2026-11-11 | WWBN AVideo through 29.7.1 contains an improper payment verification vulnerability in plugin/PayPalYPT/ipnV2.php that cr |
| CVE-2026-126561 | 7.1 | 2026-11-11 | Semantic MediaWiki 2.5.0 before 7.4.1 contains a missing authorization vulnerability that allows editors without the edi |
| CVE-2026-126566 | 7.1 | 2026-11-11 | Semantic MediaWiki 7.3.1 before 7.4.1 contains an incorrect authorization vulnerability in EditProtectionUpdater::userMa |
| CVE-2026-126570 | 7.6 | 2026-11-11 | Padloc 4.0.0 before 4.3.1 contains a prototype pollution vulnerability that allows SCIM token holders to modify Object.p |
| CVE-2026-63660 | 8.1 | 2026-11-11 | node-fontnik is a library that delivers a range of glyphs rendered as SDFs (signed distance fields) in a protocol buffer |
| CVE-2026-64666 | 7.1 | 2026-11-11 | pam_usb provides hardware authentication for Linux using removable media. Prior to version 0.9.3, src/local.c reads XRDP |
| CVE-2026-64668 | 7.4 | 2026-11-11 | pam_usb provides hardware authentication for Linux using removable media. From version 0.8.0 to before version 0.9.3, th |
| CVE-2026-64669 | 7.4 | 2026-11-11 | pam_usb provides hardware authentication for Linux using removable media. From version 0.8.0 to before version 0.9.3, th |
| CVE-2026-64670 | 9.3 | 2026-11-11 | Waline is a comment system with backend support. In versions 3.15.2 and prior, @waline/client renders the comment editor |
| CVE-2026-64671 | 7.2 | 2026-11-11 | Waline is a comment system with backend support. In versions 3.15.2 and prior, the @waline/client UserList widget builds |
| CVE-2026-64678 | 9.8 | 2026-11-11 | NOsql Object (NO2 a.k.a Nitrite) database is an open source nosql embedded document store. Prior to version 4.4.1, when  |
| CVE-2026-64682 | 9.8 | 2026-11-11 | AstroBlocks is a block-first CMS for Astro projects. Prior to version 3.4.0, admin session tokens can be forged due to a |
| CVE-2026-109870 | 8.1 | 2026-11-11 | The User Registration & Membership  WordPress plugin before 5.3.2 does not verify that a discount coupon applied to a pa |
| CVE-2026-111579 | 8.1 | 2026-11-11 | The Forminator Forms  WordPress plugin before 1.58.4 does not enforce payment on the server side when a form's configure |
| CVE-2026-115733 | 9.1 | 2026-11-11 | The Printaura-Woocommerce WordPress plugin through 4.0.2 does not properly restrict access to the WooCommerce REST API,  |
| CVE-2026-115734 | 9.6 | 2026-11-11 | The Pay with a tweet WordPress plugin through 1.0.5 does not validate a file path before deleting it, nor does it restri |
| CVE-2026-115735 | 9.6 | 2026-11-11 | The Somatic Framework WordPress plugin through 1.8.14 does not perform an authorization check or validate a user-supplie |
| CVE-2026-118041 | 8.8 | 2026-11-11 | The Contest Gallery  WordPress plugin before 34.0.3 does not sanitise the name of files uploaded through its e-commerce  |
| CVE-2026-121497 | 9.8 | 2026-11-11 | The AskAny  WordPress plugin before 2.2.0 does not validate the extension or content of files attached to chat messages, |
| CVE-2026-121862 | 8.8 | 2026-11-11 | The Knowledge Building WordPress plugin before 0.7.3 does not sanitise and escape comments submitted through its reply f |
| CVE-2026-121863 | 7.1 | 2026-11-11 | The Knowledge Building WordPress plugin before 0.7.3 does not escape several user-supplied values before echoing them ba |
| CVE-2026-121870 | 7.5 | 2026-11-11 | The Simpler Checkout WordPress plugin before 1.5.4 does not properly restrict who can create orders and checks its autom |
| CVE-2026-121998 | 8.8 | 2026-11-11 | The iChart  WordPress plugin before 2.2.4 does not perform capability or ownership checks in several of its AJAX actions |
| CVE-2026-123134 | 8.8 | 2026-11-11 | The Smoove abandoned cart trigger for WooCommerce WordPress plugin before 4.3.6 does not sanitise and escape abandoned-c |
| CVE-2026-123695 | 9.8 | 2026-11-11 | The Security For WooCommerce WordPress plugin through 1.0.16 does not restrict access to several of its REST API routes, |
| CVE-2026-123696 | 7.5 | 2026-11-11 | The Security For WooCommerce WordPress plugin through 1.0.16 does not check that the requester is authorised before rese |
| CVE-2026-123697 | 7.5 | 2026-11-11 | The Security For WooCommerce WordPress plugin through 1.0.16 does not restrict who can request a user's current two-fact |
| CVE-2026-123700 | 7.5 | 2026-11-11 | The Security For WooCommerce WordPress plugin through 1.0.16 does not check that the requester is authorised before runn |
| CVE-2026-111190 | 8.1 | 2026-11-11 | The ARForms plugin for WordPress is vulnerable to arbitrary file upload in all versions up to, and including, 7.2.4 via  |
| CVE-2026-12062 | 8.8 | 2026-11-11 | Zoho Corporation ManageEngine ADAudit Plus versions below 8703 are vulnerable to an authenticated SQL injection vulnerab |
| CVE-2026-12424 | 7.2 | 2026-11-11 | The ARforms plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Referer Header in all versions up to,  |
| CVE-2026-12427 | 7.2 | 2026-11-11 | The ARforms plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'description' parameter in all ver |
| CVE-2026-76981 | 8.8 | 2026-11-11 | Zoho Corporation ManageEngine ADAudit Plus versions below 8711 are vulnerable to an authenticated second order SQL injec |
| CVE-2026-126607 | 7.8 | 2026-11-11 | Progressive Robot hMailServer 6.2.3 through 6.3.7 on Windows, with a MySQL or MariaDB database, hands the bundled MariaD |
| CVE-2026-126609 | 7.5 | 2026-11-11 | Progressive Robot hMailServer 6.2.25 through 6.3.7 on Windows, with a PostgreSQL database, the connection's sslmode requ |
| CVE-2026-126610 | 7.4 | 2026-11-11 | Progressive Robot hMailServer 6.3.4 through 6.3.7, with a MySQL or MariaDB database and TlsMode=verify-full, does not ha |
| CVE-2026-126611 | 7.0 | 2026-11-11 | Progressive Robot hMailServer 6.3.4 through 6.3.7, with a MySQL or MariaDB database, TlsMode=verify-full and no TlsCaFil |
| CVE-2026-126612 | 7.8 | 2026-11-11 | Improper link resolution in the Windows installer of Progressive Robot hMailServer 6.0.0 through 6.3.7 allows a local au |
| CVE-2026-126613 | 7.5 | 2026-11-11 | Allocation of resources without limits in the JSON reader of Progressive Robot hMailServer 6.3.2 through 6.3.7 allows a  |
| CVE-2026-126617 | 8.8 | 2026-11-11 | SQL injection in the database layer of Progressive Robot hMailServer 6.0.0-B1 through 6.2.18, when the server uses MySQL |
| CVE-2026-126621 | 7.5 | 2026-11-11 | Progressive Robot hMailServer 6.0.0-B1 through 6.3.7 on Windows hands OpenSSL the names of its own TLS files - the liste |
| CVE-2026-126622 | 7.3 | 2026-11-11 | Incorrect default permissions in the Windows installer of Progressive Robot hMailServer 6.3.7 allow a local authenticate |
| CVE-2026-126623 | 7.5 | 2026-11-11 | Inefficient algorithmic complexity in the JSON reader of Progressive Robot hMailServer 6.3.6 and 6.3.7 allows a remote a |
| CVE-2026-126624 | 7.3 | 2026-11-11 | Unverified ownership in the Windows installer of Progressive Robot hMailServer 6.3.7 allows a local authenticated user t |
| CVE-2026-18767 | 7.8 | 2026-11-11 | A local low privileged attacker or process can access I/O ports via TcRouter.sys because of exposed IOCTL function calls |
| CVE-2026-18768 | 7.8 | 2026-11-11 | A local low privileged attacker can access arbitrary physical memory or define its mapping via TcRouter.sys because of e |
| CVE-2026-18769 | 7.8 | 2026-11-11 | A local low privileged attacker can move arbitrary physical memory content via TcRouter.sys because of exposed IOCTL fun |
| CVE-2026-124250 | 7.1 | 2026-11-11 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in AyeCode Ltd GeoDir |
| CVE-2026-124737 | 7.5 | 2026-11-11 | A flaw was found in BusyBox. When the TFTP (Trivial File Transfer Protocol) client requests a custom small block size an |
| CVE-2026-123478 | 7.1 | 2026-11-11 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Meow Apps AI Engin |
| CVE-2026-124253 | 7.1 | 2026-11-11 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in codepeople Calcula |
| CVE-2026-124739 | 7.5 | 2026-11-11 | A flaw was found in BusyBox. When the httpd web server processes subdirectory configuration files, an overly long index  |
| CVE-2026-124741 | 7.6 | 2026-11-11 | A flaw was found in BusyBox. The udhcpc6 DHCPv6 client does not properly validate the size of network options sent by a  |
| CVE-2026-78287 | 10.0 | 2026-11-11 | Improper Control of Generation of Code ('Code Injection') vulnerability in Staggs STAGGS staggs allows Remote Code Inclu |
| CVE-2026-103883 | 8.8 | 2026-11-11 | The 6Storage Rentals plugin for WordPress is vulnerable to Authentication Bypass leading to Administrator Account Takeov |
| CVE-2026-119615 | 8.8 | 2026-11-11 | The Reset Database plugin for WordPress is vulnerable to privilege escalation in versions up to, and including, 1.1.3. T |
| CVE-2026-125784 | 8.8 | 2026-11-11 | Cross-Site Request Forgery (CSRF) vulnerability in Magnigenie RestroPress restropress allows Cross Site Request Forgery. |
| CVE-2026-105153 | 7.7 | 2026-11-11 | Improper Restriction of XML External Entity Reference in Apache Roller 4.0 through 6.1.6 allows an authenticated user wi |
| CVE-2026-118411 | 8.8 | 2026-11-11 | Cross-Site Request Forgery (CSRF) in Apache Roller 5.0.1 through 6.1.6 allows an unauthenticated attacker to create an a |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
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
| CVE-2026-19868 | SonicWall / SonicOS SSLVPN | 2026-11-06 | 2026-11-20 | Unknown |
| CVE-2024-27834 | Apple / Multiple Products | 2026-11-04 | 2026-11-18 | Unknown |

---

*Total entries in CISA KEV catalog: 1779*