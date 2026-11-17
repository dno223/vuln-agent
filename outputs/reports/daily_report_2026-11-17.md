# Vulnerability Intelligence Report

**Date:** 2026-11-17  
**Generated:** 2026-11-17T17:23:17Z  

---

## Executive Summary

Our environment faces significant exposure from 82 high-severity vulnerabilities, including critical flaws in Microsoft Office SharePoint and OneNote enabling remote code execution, privilege escalation risks in Autodesk Installer, and multiple email parsing vulnerabilities. Eight new CISA Known Exploited Vulnerabilities were added this week affecting Cisco, Microsoft, and Check Point products, signaling active exploitation in the wild. Immediate patching and compensating controls are required to reduce organizational risk and prevent potential data breaches or system compromise.

---

## Risk Narrative

The current threat landscape reflects a surge in actively exploited vulnerabilities across widely deployed enterprise software. CISA's addition of eight KEVs in seven days indicates threat actors are actively weaponizing flaws in network infrastructure, email platforms, and productivity tools. Remote code execution vulnerabilities in Microsoft Office products represent the highest business risk, potentially enabling attackers to exfiltrate sensitive data, deploy ransomware, or establish persistent footholds. Email parsing flaws introduce supply chain risk, while kernel-level driver vulnerabilities threaten endpoint integrity. Organizations failing to act swiftly face regulatory exposure, operational disruption, and reputational damage.

---

## Prioritized Action Items

1. Immediately patch Microsoft Office SharePoint (CVE-2026-124223, CVSS 8.8) and OneNote (CVE-2026-126526, CVSS 8.8) to eliminate active remote code execution exposure.
2. Apply all vendor updates for the five newly added CISA KEV entries, prioritizing Cisco BroadWorks, Check Point, and Microsoft Office due to confirmed active exploitation.
3. Remediate the Autodesk Installer DLL hijacking vulnerability (CVE-2026-101327, CVSS 7.8) by restricting write permissions on temporary directories used during installation.
4. Update mail-parser and Amazon DJL libraries to their patched versions to close path traversal and email parsing vulnerabilities affecting multiple systems.
5. Audit and patch VB-Audio VB-CABLE kernel driver (CVE-2026-124019, CVSS 7.8) on all endpoints to prevent privilege escalation via out-of-bounds memory exploitation.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-129295 | 7.5 | 2026-11-16 | mail-parser is a tool that parses emails by enhancing the Python standard library and extracting message details into a  |
| CVE-2026-129297 | 7.5 | 2026-11-16 | mail-parser is a tool that parses emails by enhancing the Python standard library and extracting message details into a  |
| CVE-2026-101327 | 7.8 | 2026-11-16 | A maliciously crafted DLL placed in a predictable, attacker-writable temporary directory used by the Autodesk Installer  |
| CVE-2026-127218 | 7.5 | 2026-11-16 | Axigen Mail Server 10.3.3.67 through 10.3.3.x, 10.4.42 through 10.4.x, 10.5.29 through 10.5.x, 10.6.x before 10.6.41, an |
| CVE-2026-129266 | 7.5 | 2026-11-16 | External control of a file path in Amazon Deep Java Library (DJL) versions 0.7.0 through 0.38.0 might allow a remote una |
| CVE-2026-83816 | 8.1 | 2026-11-16 | CodeWhale is a DeepSeek and MiMo coding agent for the terminal. Prior to 0.9.0, the ExecShellTool::approval_requirement_ |
| CVE-2026-83817 | 7.5 | 2026-11-16 | CodeWhale is a DeepSeek and MiMo coding agent for the terminal. Prior to 0.9.0, DEFAULT_AUTOMATION_AUTO_APPROVE caused A |
| CVE-2026-124019 | 7.8 | 2026-11-16 | VB-Audio VB-CABLE virtual audio device kernel streaming driver (vbaudio_cable64_win10.sys 10.0.10011.16384) contains out |
| CVE-2026-124223 | 8.8 | 2026-11-16 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-126526 | 8.8 | 2026-11-16 | Heap-based buffer overflow in Microsoft Office OneNote allows an unauthorized attacker to execute code over a network. |
| CVE-2026-129302 | 7.5 | 2026-11-16 | Guard Core is an API security core engine for the FastAPI-Guard, FlaskAPI Guard, and DjAPI Guard adapters. From 3.5.0 un |
| CVE-2026-53998 | 10.0 | 2026-11-16 | Phoenix is an AI observability and evaluation platform. From 13.0.0 until 15.7.0, the applyChatTemplate GraphQL query pa |
| CVE-2026-111760 | 8.0 | 2026-11-16 | Git is a fast, scalable, distributed revision control system with an unusually rich command set that provides both high- |
| CVE-2026-115563 | 7.5 | 2026-11-16 | The Model Context Protocol Python SDK is the official Python SDK for Model Context Protocol servers and clients. From 1. |
| CVE-2026-121708 | 8.1 | 2026-11-16 | OpenCTI is an open source platform for managing cyber threat intelligence knowledge and observables. Prior to 7.260513.0 |
| CVE-2026-63477 | 8.8 | 2026-11-16 | OpenCTI is an open source platform for managing cyber threat intelligence knowledge and observables. Prior to 7.260624.0 |
| CVE-2026-110339 | 7.5 | 2026-11-16 | The Libreswan pluto daemon dereferences a NULL pointer when a CERT payload is received with an empty PKCS#7 payload, cau |
| CVE-2026-120697 | 8.7 | 2026-11-16 | Wiki.js is an open source wiki app built on Node.js. Prior to 2.5.315, an authenticated user with write:pages can store  |
| CVE-2026-120698 | 8.8 | 2026-11-16 | Wiki.js is an open source wiki app built on Node.js. Prior to 2.5.315, an authenticated account with only manage:users c |
| CVE-2026-130067 | 7.8 | 2026-11-16 | 7-Zip File Manager before 26.03 fails to detect archive entry names padded with Unicode space characters, allowing attac |
| CVE-2026-130070 | 9.1 | 2026-11-16 | Ghost by muneeb141 on the main branch from commit c731cdf through commit 672dfec contains an authentication bypass vulne |
| CVE-2026-130071 | 9.8 | 2026-11-16 | TridotsTech go1cms master branch through commit 7f68d05 and version-3 branch before commit ead8da3 contains a missing au |
| CVE-2026-130072 | 9.1 | 2026-11-16 | Cloud Commander (cloudcmd) before 19.21.4 contains an authentication bypass and path traversal vulnerability that allows |
| CVE-2026-130073 | 8.3 | 2026-11-16 | CBoard before commit 7bd8180 contains a missing authorization vulnerability that allows any authenticated user to reach  |
| CVE-2026-130074 | 8.1 | 2026-11-16 | free5GC WebConsole through 1.4.6 contains an authorization flaw in the ChangePasswordInfo handler that allows authentica |
| CVE-2026-130081 | 7.5 | 2026-11-16 | B3log Solo through 4.4.0 contains an information disclosure vulnerability that allows unauthenticated attackers to obtai |
| CVE-2026-130082 | 8.8 | 2026-11-16 | django-tenants 3.4.8 before 4.0.1 contains an SQL injection vulnerability in its PostgreSQL backend that allows attacker |
| CVE-2026-130290 | 7.9 | 2026-11-16 | In Open Object Rexx (ooRexx) before 5.2.0, RXAPI has a heap buffer over-read in a QueueManager DataQueue::addmethod. In  |
| CVE-2026-69154 | 7.8 | 2026-11-16 | The Coder VS Code extension opens Coder workspaces in VS Code with a single click. From 0.1.20 until 1.14.6, a malicious |
| CVE-2026-130320 | 9.3 | 2026-11-16 | In Open Object Rexx (ooRexx) before 5.2.0, RXAPI mishandles nameArg and userid bounds checking, possibly leading to arbi |
| CVE-2026-130327 | 9.3 | 2026-11-16 | In Open Object Rexx (ooRexx) before 5.2.0, RXAPI relies on a world-writable /tmp file unless XDG_RUNTIME_DIR is set, or  |
| CVE-2026-12487 | 7.5 | 2026-11-17 | An incorrect authorization vulnerability in the SNMP parameter of Zyxel EE5301-00 customized firmware version 5.63(ACLD. |
| CVE-2026-130351 | 7.2 | 2026-11-17 | phpMyFAQ from 4.2.0-alpha before 4.2.0-RC.2 contains an authorization bypass vulnerability in the multisite Redis config |
| CVE-2026-130361 | 8.8 | 2026-11-17 | AdminNeo before 5.9.1 contains a parameter injection vulnerability in its ClickHouse driver that allows attackers to inj |
| CVE-2026-130366 | 8.1 | 2026-11-17 | AdminNeo before 5.9.1 contains an authentication bypass vulnerability in the ClickHouse driver that allows remote attack |
| CVE-2026-130369 | 8.1 | 2026-11-17 | phpMyFAQ 4.1.9 before 4.1.12 and 4.2.0-alpha before 4.2.0-RC.2 contains an authorization bypass vulnerability in multisi |
| CVE-2026-130371 | 8.1 | 2026-11-17 | phpMyFAQ before 4.1.12 and 4.2.0-alpha before 4.2.0-RC.2 contains an authentication bypass vulnerability because the web |
| CVE-2026-130374 | 7.5 | 2026-11-17 | AdminNeo before 5.9.1 contains an sql injection vulnerability that allows remote attackers to inject SQL by supplying cr |
| CVE-2026-130375 | 7.2 | 2026-11-17 | AdminNeo before 5.9.1 contains a remote code execution vulnerability that allows authenticated SQLite users to bypass th |
| CVE-2026-130380 | 8.1 | 2026-11-17 | AdminNeo before 5.9.1 contains an authentication bypass vulnerability in the sqlsrv-based MS SQL driver that allows unau |
| CVE-2026-130382 | 8.8 | 2026-11-17 | AdminNeo before 5.9.1 contains an authentication bypass vulnerability in OtpLoginPlugin that allows attackers knowing th |
| CVE-2026-79614 | 9.8 | 2026-11-17 | An out-of-bounds write vulnerability in “libclinkc.so” in Zyxel DX3301-T0/EX3301-T0 firmware versions through 5.50(ABVY. |
| CVE-2026-86676 | 7.2 | 2026-11-17 | A post-authentication command injection vulnerability in the “Description” parameter of a CGI program  in Zyxel DX3300-T |
| CVE-2026-107901 | 7.1 | 2026-11-17 | TELLUS and TELLUS Lite provided by FUJI ELECTRIC CO., LTD. contain an out-of-bounds read vulnerability. Opening a specia |
| CVE-2026-107902 | 7.8 | 2026-11-17 | TELLUS and TELLUS Lite provided by FUJI ELECTRIC CO., LTD. contain a use after free vulnerability. Opening a specially c |
| CVE-2026-105739 | 8.7 | 2026-11-17 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 17.2 before 19.3.9, 19.4 before 19.4.8, and 1 |
| CVE-2026-108153 | 8.7 | 2026-11-17 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 16.1 before 19.3.9, 19.4 before 19.4.8, and 1 |
| CVE-2026-121684 | 8.1 | 2026-11-17 | The Soledad theme for WordPress is vulnerable to unauthenticated Remote Code Execution in versions up to, and including, |
| CVE-2026-18241 | 8.2 | 2026-11-17 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 9.3 before 19.3.9, 19.4 before 19.4.8, and 19 |
| CVE-2026-97187 | 7.6 | 2026-11-17 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 17.6 before 19.3.9, 19.4 before 19.4.8, and 1 |
| CVE-2026-107904 | 9.8 | 2026-11-17 | Joomla Extension - valorapps.com - Unauthenticated Remote Code Execution in Easy File Uploader < 2.9.7 - An unauthentica |
| CVE-2026-107493 | 7.7 | 2026-11-17 | Issue summary: When an application passes a stack to
PEM_X509_INFO_read_bio_ex() to add entries to, and reading fails,
O |
| CVE-2026-119643 | 7.2 | 2026-11-17 | The MembershipWorks - Membership, Events & Directory plugin for WordPress is vulnerable to Stored Cross-Site Scripting i |
| CVE-2026-121864 | 8.5 | 2026-11-17 | In nanobot, when sandboxed exec is enabled, the shell executable used to run commands can be selected by the caller and  |
| CVE-2026-121865 | 7.6 | 2026-11-17 | In nanobot, the WebSocket gateway allows a standard client holding a valid client token to select an existing directory  |
| CVE-2026-124709 | 7.5 | 2026-11-17 | Issue summary: A QUIC server that rejects a stream opened by the peer may
retain that stream's state for the lifetime of |
| CVE-2026-118496 | 7.5 | 2026-11-17 | The affected products process a server-supplied URL without sufficient validation. An unauthenticated remote attacker co |
| CVE-2026-118498 | 7.5 | 2026-11-17 | The CODESYS Automation Server Connector uses server-supplied file names without sufficient path traversal checks. An una |
| CVE-2026-129448 | 9.8 | 2026-11-17 | Deserialization of Untrusted Data in Apache Roller versions 4.0.0 through 6.1.4 allows an unauthenticated remote attacke |
| CVE-2026-12239 | 8.8 | 2026-11-17 | The WP Abstracts plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 2.7.6. |
| CVE-2026-130583 | 9.3 | 2026-11-17 | Rootways Authorize.net CIM Pro extension for Magento 2 before 4.1.5 contains an unauthenticated server-side request forg |
| CVE-2026-130584 | 8.3 | 2026-11-17 | Xibo CMS before 4.5.3 contains an insecure direct object reference vulnerability that allows authenticated users to acce |
| CVE-2026-130587 | 9.9 | 2026-11-17 | OpenFunction through 1.2.0 contains a privilege escalation vulnerability that allows namespace tenants to create privile |
| CVE-2026-130589 | 8.1 | 2026-11-17 | Emitter through 3.1 contains a privilege escalation vulnerability that allows any channel key holder to forge a master k |
| CVE-2026-130591 | 7.5 | 2026-11-17 | 53AIHub before 0.5.5 contains a missing authentication vulnerability that allows unauthenticated attackers to read files |
| CVE-2026-130615 | 7.1 | 2026-11-17 | Flowise through 3.1.4 contains a server-side request forgery vulnerability that allows authenticated users to reach inte |
| CVE-2026-82025 | 7.2 | 2026-11-17 | WP File Manager before 8.0.7 contains a file upload restriction bypass vulnerability that allows authenticated administr |
| CVE-2026-130626 | 7.5 | 2026-11-17 | The core JDK HTTP client (a2a-java-sdk-http-client) applies the GHSA-9rhm redirect-neutralization only to the POST path. |
| CVE-2026-130627 | 7.5 | 2026-11-17 | The Vert.x HTTP client transport (a2a-java-sdk-http-client-vertx) hand-rolls a POST redirect follower that, when the doc |
| CVE-2026-77224 | 7.5 | 2026-11-17 | Camunda 7.24.0 before 7.24.14 and 7.23.0 before 7.23.17 contains an XML External Entity (XXE) injection vulnerability in |
| CVE-2026-100963 | 8.1 | 2026-11-17 | NVIDIA TensorRT for Linux contains a vulnerability where a user could cause an integer overflow issue. A successful expl |
| CVE-2026-100971 | 8.4 | 2026-11-17 | NVIDIA OpenShell for Linux contains a vulnerability in the L7 path allowlist enforcement component where a local attacke |
| CVE-2026-100972 | 8.1 | 2026-11-17 | NVIDIA OpenShell for Linux contains a vulnerability in resource-level authorization for create, read, update, and delete |
| CVE-2026-100975 | 7.6 | 2026-11-17 | NVIDIA OpenShell for Linux contains a vulnerability in the Kubernetes sandbox SSH authentication configuration where a l |
| CVE-2026-100977 | 7.5 | 2026-11-17 | NVIDIA OpenShell for Linux contains a vulnerability in L7 REST policy enforcement where a local attacker with low privil |
| CVE-2026-100980 | 7.5 | 2026-11-17 | NVIDIA OpenShell for Linux contains a vulnerability in its command-line diagnostic interface where an attacker could cau |
| CVE-2026-65106 | 7.8 | 2026-11-17 | NVIDIA Transformer Engine for Linux contains a vulnerability where a user could cause deserialization by loading  untrus |
| CVE-2026-100967 | 7.8 | 2026-11-17 | NVIDIA Megatron-LM contains a vulnerability where an attacker could cause deserialization of untrusted data. A successfu |
| CVE-2026-100968 | 7.8 | 2026-11-17 | NVIDIA Megatron-LM contains a vulnerability in dataset loading where an attacker could cause deserialization of untruste |
| CVE-2026-129246 | 7.8 | 2026-11-17 | Due to a Debian-specific patch, the directory used to share data between the
LightDM and the users logging in was writab |
| CVE-2026-65132 | 7.8 | 2026-11-17 | NVIDIA Megatron-LM contains a vulnerability in checkpoint loading where an attacker could cause deserialization of untru |
| CVE-2026-67455 | 8.8 | 2026-11-17 | NVIDIA Model Optimizer for Linux and Windows contains a vulnerability where an attacker could cause a deserialization of |

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

---

*Total entries in CISA KEV catalog: 1781*