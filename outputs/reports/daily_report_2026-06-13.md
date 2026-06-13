# Vulnerability Intelligence Report

**Date:** 2026-06-13  
**Generated:** 2026-06-13T10:28:11Z  

---

## Executive Summary

The organization faces critical security exposure with 99 high-severity vulnerabilities, including multiple maximum-severity (CVSS 10.0) hardcoded credential flaws. Seven new CISA Known Exploited Vulnerabilities were added this week, indicating active threat actor targeting. Critical vulnerabilities affect network infrastructure (Netty framework), industrial systems (IEI), content management platforms, and virtualization technologies. The prevalence of hardcoded credentials and authentication bypass vulnerabilities creates immediate risk of unauthorized system access and potential lateral movement across the network.

---

## Risk Narrative

The threat landscape shows sophisticated attackers actively exploiting known vulnerabilities, with CISA's emergency additions indicating imminent exploitation risk. Hardcoded credentials in multiple systems create persistent backdoors that cannot be easily remediated through standard patching. The combination of network framework vulnerabilities and industrial control system exposures suggests potential for supply chain attacks and critical infrastructure targeting. Business continuity faces immediate risk from potential system compromises, data breaches, and operational disruptions across multiple technology stacks.

---

## Prioritized Action Items

1. Immediately patch or isolate systems with CVE-2026-47131 (CVSS 10.0) vm2 sandbox bypass vulnerability.
2. Replace or disable IEI Remote Management systems affected by CVE-2026-11849 hardcoded credentials vulnerability.
3. Update all Netty framework implementations to versions 4.1.135.Final or 4.2.15.Final to address multiple high-severity flaws.
4. Patch Oracle PeopleSoft, Ivanti Sentry, and Cisco SD-WAN systems per CISA emergency directive requirements.
5. Conduct emergency credential audit to identify and remediate any additional hardcoded authentication mechanisms.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-11849 | 9.8 | 2026-06-12 | The 
iRM-IEI Remote Management developed by IEI Integration Corp has a Hardcoded Credentials vulnerability, allowing una |
| CVE-2026-12066 | 7.3 | 2026-06-12 | A security flaw has been discovered in PbootCMS up to 3.2.12. This vulnerability affects the function retrieve of the fi |
| CVE-2026-10557 | 9.8 | 2026-06-12 | The Yarbo Android and iOS applications contain hard-coded MQTT broker credentials that are identical for all users and a |
| CVE-2026-44893 | 7.5 | 2026-06-12 | Netty is a network application framework for development of protocol servers and clients. In netty-codec-haproxy prior t |
| CVE-2026-44894 | 7.5 | 2026-06-12 | Netty is a network application framework for development of protocol servers and clients. NoQuicTokenHandler is the toke |
| CVE-2026-45416 | 7.5 | 2026-06-12 | Netty is a network application framework for development of protocol servers and clients. Prior to versions 4.1.135.Fina |
| CVE-2026-45674 | 8.7 | 2026-06-12 | Netty is a network application framework for development of protocol servers and clients. Prior to versions 4.1.135.Fina |
| CVE-2026-46340 | 7.5 | 2026-06-12 | Netty is a network application framework for development of protocol servers and clients. In versions of netty-transport |
| CVE-2026-47131 | 10.0 | 2026-06-12 | vm2 is an open source vm/sandbox for Node.js. Prior to version 3.11.4, by combining Buffer.call.call({}.__lookupGetter__ |
| CVE-2026-47135 | 8.7 | 2026-06-12 | vm2 is an open source vm/sandbox for Node.js. Prior to version 3.11.4, Symbol.for override in setup-sandbox.js only inte |
| CVE-2026-47137 | 10.0 | 2026-06-12 | vm2 is an open source vm/sandbox for Node.js. Prior to version 3.11.4, the fix for GHSA-8hg8-63c5-gwmx (CVE-2023-37903)  |
| CVE-2026-47139 | 8.6 | 2026-06-12 | vm2 is an open source vm/sandbox for Node.js. Prior to version 3.11.4, NodeVM supports excluding public network builtins |
| CVE-2026-47140 | 10.0 | 2026-06-12 | vm2 is an open source vm/sandbox for Node.js. Prior to version 3.11.4, NodeVM blocks several dangerous Node.js builtins  |
| CVE-2026-47208 | 10.0 | 2026-06-12 | vm2 is an open source vm/sandbox for Node.js. Prior to version 3.11.4, VM2 suffers from a sandbox breakout vulnerability |
| CVE-2026-47209 | 8.6 | 2026-06-12 | vm2 is an open source vm/sandbox for Node.js. Prior to version 3.11.4, the BaseHandler.set trap in bridge.js (line 1231) |
| CVE-2026-47210 | 9.8 | 2026-06-12 | vm2 is an open source vm/sandbox for Node.js. Prior to version 3.11.4, a sandbox escape vulnerability in vm2 allows arbi |
| CVE-2026-53787 | 9.8 | 2026-06-12 | Amasty Order Attributes for Magento 2 before version 4.0.0 contains an unauthenticated arbitrary file upload vulnerabili |
| CVE-2026-54133 | 9.8 | 2026-06-12 | jmespath.php allows users to use JMESPath, software for declaratively specifying how to extract elements from a JSON doc |
| CVE-2026-6211 | 8.7 | 2026-06-12 | Unrestricted upload of file with dangerous type vulnerability in Global IT Informatics Services Inc. WEOLL allows Access |
| CVE-2026-6853 | 9.8 | 2026-06-12 | Improper restriction of excessive authentication attempts vulnerability in Başbelen Group Food Cafe Businesses Industry  |
| CVE-2026-7368 | 8.1 | 2026-06-12 | The Yarbo cloud does not enforce per-device or per-user authorization. Any client possessing valid credentials, whether  |
| CVE-2026-47691 | 8.7 | 2026-06-12 | Netty is a network application framework for development of protocol servers and clients. Prior to versions 4.1.135.Fina |
| CVE-2026-48748 | 7.5 | 2026-06-12 | Netty is a network application framework for development of protocol servers and clients. Prior to version 4.2.15.Final, |
| CVE-2026-50010 | 7.5 | 2026-06-12 | Netty is a network application framework for development of protocol servers and clients. Prior to versions 4.1.135.Fina |
| CVE-2026-50011 | 7.5 | 2026-06-12 | Netty is a network application framework for development of protocol servers and clients. Prior to versions 4.1.135.Fina |
| CVE-2026-50083 | 9.1 | 2026-06-12 | The Aqara IAM/SSO Gateway (gw-builder.aqara.com) used a hardcoded OAuth client credential, which is an instance of "CWE- |
| CVE-2026-50084 | 9.6 | 2026-06-12 | The Aqara Cloud Production API (open-cn.aqara.com/v3.0/open/api) would authorize any valid developer token for access to |
| CVE-2026-50085 | 8.6 | 2026-06-12 | The Aqara Board service (op-test.aqara.com) accepts arbitrary MQTT command payloads, and forwards them to the platfom's  |
| CVE-2026-50086 | 10.0 | 2026-06-12 | The Aqara IAM/SSO gateway (gw-builder.aqara.com) exposes bidirectional AES round-trups against the platform's signing ke |
| CVE-2026-50087 | 8.2 | 2026-06-12 | The Aqara IAM/SSO gateway (gw-builder.aqara.com) exhibits a cross-origin request sharing vulnerability, which is an inst |
| CVE-2026-50088 | 8.2 | 2026-06-12 | The Aqara Developer Portal (developer.aqara.com) and shared test environments (developer-test.aqara.com, aiot-test.aqara |
| CVE-2026-50090 | 9.3 | 2026-06-12 | The Aqara Cloud OAuth Authorization Endpoint (open-cn.aqara.com/oauth/authorize) is vulnerable to a redirect bypass due  |
| CVE-2026-50091 | 9.1 | 2026-06-12 | Aqara Home Android (com.lumiunited.aqarahome) 6.0.0 (and white-label clients embedding the same liblumidevsdk.so) uses h |
| CVE-2026-9638 | 7.5 | 2026-06-12 | Crypt::PBKDF2 versions before 0.261630 for Perl generate insecure random values for salts.

These versions use the built |
| CVE-2026-3840 | 7.1 | 2026-06-12 | A vulnerability in Kedro version 1.2.0 allows an attacker to exploit path traversal by providing a crafted version strin |
| CVE-2026-53981 | 7.6 | 2026-06-12 | Cap-go prior to 12.128.2 contains an account takeover vulnerability in its email change mechanism that allows an attacke |
| CVE-2026-6961 | 7.6 | 2026-06-12 | Mattermost versions 11.6.x <= 11.6.1, 11.5.x <= 11.5.4, 10.11.x <= 10.11.15, 10.11.x <= 10.11.16 Mattermost fails to san |
| CVE-2026-7387 | 8.8 | 2026-06-12 | Mattermost versions 11.6.x <= 11.6.1, 11.5.x <= 11.5.4, 10.11.x <= 10.11.15, 10.11.x <= 10.11.16 Mattermost fails to req |
| CVE-2026-44168 | 8.0 | 2026-06-12 | MariaDB server is a community developed fork of MySQL server. From versions 10.6.1 to before 10.6.26, 10.11.1 to before  |
| CVE-2026-47965 | 7.8 | 2026-06-12 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by an out-of-bounds write vulnerability that |
| CVE-2026-48163 | 8.0 | 2026-06-12 | MariaDB server is a community developed fork of MySQL server. From versions 10.6.1 to before 10.6.27, 10.11.1 to before  |
| CVE-2026-48165 | 8.0 | 2026-06-12 | MariaDB server is a community developed fork of MySQL server. From versions 10.6.1 to before 10.6.27, 10.11.1 to before  |
| CVE-2026-48558 | 10.0 | 2026-06-12 | SimpleHelp versions 5.5.15 and prior and 6.0 pre-release versions contain an authentication bypass vulnerability in the  |
| CVE-2026-53406 | 7.8 | 2026-06-12 | Insufficient Verification of Data Authenticity in Remote Control for Zoom Contact Center for Windows before version 7.0. |
| CVE-2026-12043 | 8.8 | 2026-06-12 | Improper handling of HPACK dynamic table size updates in the AWS Common Runtime aws-c-http library might allow a remote  |
| CVE-2026-12143 | 7.5 | 2026-06-12 | form-data is a library for creating readable multipart/form-data streams. In versions through 4.0.5, the `field` argumen |
| CVE-2026-28742 | 9.8 | 2026-06-12 | Naxclow devices use a uniform request-signing scheme based on a hard-coded, platform-wide salt embedded in every firmwar |
| CVE-2026-42306 | 7.2 | 2026-06-12 | Moby is an open source container framework. In Docker Engine prior to version 29.5.1, Docker Daemon versions 28.5.2 and  |
| CVE-2026-42947 | 8.8 | 2026-06-12 | A flaw in Naxclow's platform’s onboarding workflow allows an attacker to replay a confirm-then-bind sequence to silently |
| CVE-2026-50101 | 8.1 | 2026-06-12 | Naxclow devices use a server-side, per-device relay credential that never rotates and is re-issued to the device on each |
| CVE-2026-50108 | 7.5 | 2026-06-12 | The Naxclow platform API that returns device relay registration details exposes a persistent credential without verifyin |
| CVE-2026-53407 | 8.1 | 2026-06-12 | Improper Authorization in Handler for Custom URL Scheme in Zoom Workplace before version 7.0.4 for Android and before 7. |
| CVE-2026-53408 | 8.1 | 2026-06-12 | Improper Authorization in Handler for Custom URL Scheme in Zoom Workplace before version 7.0.4 for Android and before 7. |
| CVE-2026-42851 | 7.8 | 2026-06-12 | Kitty is a cross-platform GPU based terminal. In versions prior to 0.47.0, a program able to write bytes to a kitty term |
| CVE-2026-47260 | 7.7 | 2026-06-12 | Koel is a free, open-source music streaming solution. Prior to version 9.3.5, Koel validates the podcast feed URL via th |
| CVE-2026-44786 | 7.5 | 2026-06-12 | Discourse is an open-source discussion platform. From versions 2026.1.0-latest to before 2026.1.4, 2026.3.0-latest to be |
| CVE-2026-44990 | 9.3 | 2026-06-12 | ApostropheCMS is an open-source Node.js content management system, and sanitize-html provides a simple HTML sanitizer wi |
| CVE-2026-45011 | 7.3 | 2026-06-12 | ApostropheCMS is an open-source Node.js content management system. Version 4.29.0 has a stored cross-site scripting vuln |
| CVE-2026-45012 | 7.6 | 2026-06-12 | ApostropheCMS is an open-source Node.js content management system. Versions up to and including 4.29.0 contain an authen |
| CVE-2026-45013 | 8.1 | 2026-06-12 | ApostropheCMS is an open-source Node.js content management system. Versions up to and including 4.29.0 have a password r |
| CVE-2026-4870 | 7.5 | 2026-06-12 | IBM Qiskit SDK 0.43.0 through 2.5.0 could allow an attacker to trigger a segmentation fault leading to a denial of servi |
| CVE-2026-54056 | 7.6 | 2026-06-12 | Kitty is a cross-platform GPU based terminal. In versions 0.47.0 and 0.47.1, `kitten dnd` can allow a malicious remote d |
| CVE-2025-7002 | 7.8 | 2026-06-12 | Heap buffer out-of-bounds read vulnerability in Avira Antivirus engine when scanning a malformed PDF file may allow Loca |
| CVE-2025-7003 | 7.8 | 2026-06-12 | Heap buffer out-of-bounds read vulnerability in Avira Antivirus engine when scanning a malformed PDF file may allow Loca |
| CVE-2025-7004 | 7.8 | 2026-06-12 | Heap buffer out-of-bounds write vulnerability in Avast Antivirus when scanning a malformed Windows PE file may allow Loc |
| CVE-2025-7008 | 7.8 | 2026-06-12 | Heap buffer out-of-bounds read vulnerability in Avast Antivirus when scanning a malformed Windows PE file with .NET meta |
| CVE-2025-7009 | 7.8 | 2026-06-12 | Heap buffer out-of-bounds read vulnerability in Avast Antivirus when scanning a malformed Windows PE file may allow Loca |
| CVE-2025-7011 | 7.8 | 2026-06-12 | Heap out-of-bounds read vulnerability in Avast Antivirus when scanning a malformed zip file containing XML may allow Loc |
| CVE-2025-7017 | 7.8 | 2026-06-12 | Heap buffer out-of-bounds read vulnerability in Avira Antivirus engine when scanning a malformed Windows MSI file may al |
| CVE-2026-46716 | 9.9 | 2026-06-12 | Nezha Monitoring is a self-hostable, lightweight, servers and websites monitoring and O&M tool. From version 1.4.0 to be |
| CVE-2026-46717 | 7.7 | 2026-06-12 | Nezha Monitoring is a self-hostable, lightweight, servers and websites monitoring and O&M tool. From version 1.4.0 to be |
| CVE-2026-47120 | 7.1 | 2026-06-12 | Nezha Monitoring is a self-hostable, lightweight, servers and websites monitoring and O&M tool. From version 1.4.0 to be |
| CVE-2026-48119 | 7.1 | 2026-06-12 | Nezha Monitoring is a self-hostable, lightweight, servers and websites monitoring and O&M tool. From version 0.20.0 to b |
| CVE-2026-49396 | 7.1 | 2026-06-12 | Nezha Monitoring is a self-hostable, lightweight, servers and websites monitoring and O&M tool. From version 1.0.0 to be |
| CVE-2026-53519 | 9.1 | 2026-06-12 | Nezha Monitoring is a self-hostable, lightweight, servers and websites monitoring and O&M tool. Prior to version 2.0.13, |
| CVE-2026-53608 | 8.7 | 2026-06-12 | ApostropheCMS is an open-source Node.js content management system. Versions up to and including 1.4.2 of the `@apostroph |
| CVE-2026-53609 | 9.1 | 2026-06-12 | ApostropheCMS is an open-source Node.js content management system. In versions up to and including 4.30.0, `apos.util.se |
| CVE-2026-53821 | 8.8 | 2026-06-12 | OpenClaw before 2026.5.18 accepts WebSocket client-declared operator scopes before binding to server-approved pairing or |
| CVE-2026-53822 | 8.8 | 2026-06-12 | OpenClaw before 2026.5.18 contains a command injection vulnerability where shell wrapper argv could change between appro |
| CVE-2026-53823 | 8.1 | 2026-06-12 | OpenClaw before 2026.5.3 contains a privilege escalation vulnerability in the allowFrom feature that binds to mutable Sl |
| CVE-2026-53828 | 8.8 | 2026-06-12 | OpenClaw before 2026.5.6 contains an authorization bypass vulnerability in native command handling that allows authentic |
| CVE-2026-53829 | 8.0 | 2026-06-12 | OpenClaw before 2026.5.18 contains an approval display truncation vulnerability allowing authenticated users to hide com |
| CVE-2026-53831 | 8.3 | 2026-06-12 | OpenClaw before 2026.5.18 contains a policy enforcement vulnerability in system.run safe-bin allowlist validation that a |
| CVE-2026-53832 | 7.7 | 2026-06-12 | OpenClaw before 2026.5.18 contains an identity header validation vulnerability allowing local same-host callers to forge |
| CVE-2026-53833 | 7.7 | 2026-06-12 | OpenClaw before 2026.4.29 contains an authorization bypass vulnerability in the QQBot streaming command that allows auth |
| CVE-2026-53834 | 7.5 | 2026-06-12 | OpenClaw before 2026.4.27 contains an authorization bypass vulnerability in QQBot pre-dispatch slash commands that allow |
| CVE-2026-53836 | 8.8 | 2026-06-12 | OpenClaw before 2026.5.12 contains an allowlist bypass vulnerability in PowerShell encoded-command handling that allows  |
| CVE-2026-53838 | 9.8 | 2026-06-12 | OpenClaw before 2026.5.27 contains a state mutation vulnerability in node pairing reconnection that allows paired nodes  |
| CVE-2026-53868 | 7.5 | 2026-06-12 | Capgo before 12.128.2 contains a denial of service vulnerability allowing attackers to register accounts using arbitrary |
| CVE-2025-14098 | 7.8 | 2026-06-12 | Heap buffer out-of-bounds write vulnerability due to integer overflow in Avira Antivirus engine when scanning a malforme |
| CVE-2025-9032 | 7.8 | 2026-06-12 | Heap buffer out-of-bounds read vulnerability in Avira Antivirus engine when scanning a malformed Windows PE file may all |
| CVE-2025-9033 | 7.8 | 2026-06-12 | Heap buffer out-of-bounds read vulnerability in Avira Antivirus engine when scanning a malformed PDF file may allow Loca |
| CVE-2026-12068 | 7.4 | 2026-06-12 | Information disclosure vulnerability in Avira Password Manager when used with Mozilla Firefox may allow a remote attacke |
| CVE-2026-6676 | 7.8 | 2026-06-12 | Heap buffer out-of-bounds write vulnerability in Avira Antivirus engine when scanning a malformed POSIX tar archive may  |
| CVE-2026-54228 | 7.8 | 2026-06-13 | A time-of-check time-of-use (TOCTOU) race condition was found in the abrt-dbus D-Bus service's SetElement method. Betwee |
| CVE-2026-54229 | 7.0 | 2026-06-13 | A race condition was found in the abrt-dbus D-Bus service's ChownProblemDir method. ChownProblemDir opens the dump direc |
| CVE-2026-54230 | 7.0 | 2026-06-13 | A symlink following vulnerability was found in the ABRT post-create event handler scripts in libreport. Event scripts wr |
| CVE-2026-9848 | 7.5 | 2026-06-13 | The WP Ticket plugin for WordPress is vulnerable to SQL Injection via the WordPress search query parameter (`s`) in vers |
| CVE-2026-9109 | 7.2 | 2026-06-13 | The GPTranslate – Multilingual AI Translation for WordPress: Automatically Translate Websites plugin for WordPress is vu |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-35273 | Oracle /  PeopleSoft Enterprise PeopleTools | 2026-06-12 | 2026-06-15 | Known |
| CVE-2026-10520 | Ivanti / Sentry | 2026-06-11 | 2026-06-14 | Unknown |
| CVE-2026-11645 | Google / Chromium V8 | 2026-06-09 | 2026-06-23 | Unknown |
| CVE-2026-7473 | Arista / Extensible Operating System | 2026-06-09 | 2026-06-23 | Unknown |
| CVE-2026-20245 | Cisco / Catalyst SD-WAN Manager | 2026-06-09 | 2026-06-23 | Unknown |
| CVE-2026-42271 | BerriAI / LiteLLM | 2026-06-08 | 2026-06-22 | Unknown |
| CVE-2026-50751 | Check Point / Security Gateway | 2026-06-08 | 2026-06-11 | Known |

---

*Total entries in CISA KEV catalog: 1619*