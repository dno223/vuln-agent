# Vulnerability Intelligence Report

**Date:** 2026-09-26  
**Generated:** 2026-09-26T12:40:44Z  

---

## Executive Summary

Our environment faces significant exposure across 95 high-severity CVEs, including a critical Linux kernel flaw (CVSS 9.8) and multiple IBM Guardium Data Protection vulnerabilities affecting data integrity and confidentiality. Ten new CISA Known Exploited Vulnerabilities were added this week targeting MikroTik, Microsoft SharePoint, WordPress, WSO2, and Adobe Commerce — all platforms commonly present in enterprise environments. While no monitored CVEs currently appear in the KEV catalog, the volume and severity of active threats demand immediate prioritization and remediation action.

---

## Risk Narrative

The current threat landscape combines critical infrastructure vulnerabilities with actively exploited flaws across widely deployed platforms. The CVSS 9.8 Linux kernel flaw represents a potential systemic risk if unpatched. IBM Guardium vulnerabilities threaten sensitive data governance capabilities. CISA KEV additions confirm real-world exploitation of network devices, content management systems, and enterprise commerce platforms. Successful exploitation could result in data breaches, regulatory penalties, operational disruption, and reputational damage. Organizations should treat this week's KEV additions as high-probability threats requiring urgent response.

---

## Prioritized Action Items

1. Patch the Linux kernel RDMA/srpt vulnerability (CVE-2026-100075, CVSS 9.8) immediately across all affected systems as it poses critical remote exploitation risk.
2. Apply all available IBM Guardium Data Protection 12.2 patches addressing command injection, SQL injection, and plaintext password storage vulnerabilities.
3. Audit and patch Microsoft SharePoint and WordPress Core installations against newly added CISA KEV entries within the required remediation window.
4. Remediate MikroTik RouterOS, WSO2, and Adobe Commerce/Magento vulnerabilities flagged in the CISA KEV catalog before the mandated deadline.
5. Restrict web interface access and apply firmware updates for D-Link DAP-2610 devices to mitigate the authenticated command injection vulnerability (CVE-2025-51457).

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2025-51457 | 8.8 | 2026-09-25 | D-Link DAP-2610 up to 2.06B08r099 contains an authenticated command injection vulnerability within the web interface at  |
| CVE-2026-51773 | 8.1 | 2026-09-25 | An issue in the VMware datastore driver of OpenStack glance_store. When an authenticated attacker provides a maliciously |
| CVE-2026-52622 | 7.5 | 2026-09-25 | An issue in Wellav Technologies Co., Ltd Wellav WES Emergency Broadcast Terminal WES100, WES270, WES280, and WES290 befo |
| CVE-2026-79153 | 7.8 | 2026-09-25 | Seclore FileSecure Desktop Client before 3.25.1.0 contains improper access control vulnerability in the kernel-mode driv |
| CVE-2026-88421 | 7.5 | 2026-09-25 | Incorrect access control in the BlogPage.get_entries() component of APSL puput v1.2.1 through v2.2.0 allows unauthentica |
| CVE-2026-100075 | 9.8 | 2026-09-25 | In the Linux kernel, the following vulnerability has been resolved:

RDMA/srpt: Fix srpt_alloc_rw_ctxs() unwind counters |
| CVE-2026-84884 | 7.5 | 2026-09-25 | IBM Guardium Data Protection 12.2 stores internal REST service-account passwords in a reversible plaintext-equivalent fo |
| CVE-2026-84893 | 7.6 | 2026-09-25 | IBM Guardium Data Protection 12.2 is vulnerable to SQL injection in the PESI service. An authenticated attacker could ex |
| CVE-2026-85029 | 7.5 | 2026-09-25 | IBM Guardium Data Protection 12.2 could allow a remote attacker to obtain sensitive information, delete arbitrary files, |
| CVE-2026-85542 | 8.8 | 2026-09-25 | IBM Guardium Data Protection 12.2 is affected by a command injection vulnerability in the GIM bundle import functionalit |
| CVE-2026-85750 | 7.2 | 2026-09-25 | Piwigo before v16.4.0 is vulnerable to arbitrary file read and remote code execution in image upload handling when using |
| CVE-2026-93641 | 9.3 | 2026-09-25 | An unauthenticated sender can forge a share notification that triggers stored XSS when a signed-in Zimbra Classic recipi |
| CVE-2026-93642 | 9.3 | 2026-09-25 | An unauthenticated sender can forge a share notification that triggers stored XSS when a signed-in Zimbra Modern recipie |
| CVE-2026-93643 | 9.8 | 2026-09-25 | When OnlyOffice/Document Editing is available, an unauthenticated remote attacker with access to an existing supported p |
| CVE-2026-93647 | 9.3 | 2026-09-25 | An unauthenticated calendar sender can place active markup in a COUNTER message's RFC From address. Selecting the messag |
| CVE-2026-93834 | 8.8 | 2026-09-25 | A use-after-free vulnerability was found in QEMU's 9pfs subsystem. A race condition between the main thread and a worker |
| CVE-2026-97865 | 7.3 | 2026-09-25 | A security flaw has been discovered in Open-Web-Analytics up to 1.8.1. Affected is the function Event::loadFromArray of  |
| CVE-2026-84862 | 7.2 | 2026-09-25 | IBM Guardium Data Protection 12.2 is vulnerable to insecure deserialization in the Quartz JDBC job store. An authenticat |
| CVE-2026-84882 | 7.5 | 2026-09-25 | IBM Guardium Data Protection 12.2 is vulnerable to path traversal in the Universal Connector Oracle Wallet upload compon |
| CVE-2026-93306 | 7.1 | 2026-09-25 | IBM Server Firmware FW1120.00 through FW1120.01, FW1110.00 through FW1110.31, FW1060.00 through FW1060.81, and FW950.00  |
| CVE-2026-33639 | 7.2 | 2026-09-25 | InvoicePlane is a self-hosted open source application for managing invoices, clients, and payments. Prior to 1.7.2, Invo |
| CVE-2026-39353 | 9.1 | 2026-09-25 | InvoicePlane is a self-hosted open source application for managing invoices, clients, and payments. Prior to 1.7.2-rc-1, |
| CVE-2026-42322 | 9.1 | 2026-09-25 | Piwigo is a full featured open source photo gallery application for the web. Prior to 16.4.0, admin/themes_standard_page |
| CVE-2026-42323 | 7.2 | 2026-09-25 | Piwigo is a full featured open source photo gallery application for the web. Prior to 16.4.0, admin/batch_manager.php ac |
| CVE-2026-42324 | 7.2 | 2026-09-25 | Piwigo is a full featured open source photo gallery application for the web. Prior to 16.4.0, admin/element_set_ranks.ph |
| CVE-2026-44642 | 8.1 | 2026-09-25 | Piwigo is a full featured open source photo gallery application for the web. Prior to 16.4.0, check_upgrade_access_right |
| CVE-2026-49850 | 7.5 | 2026-09-25 | InvoicePlane is a self-hosted open source application for managing invoices, clients, and payments. Prior to 1.7.2, Invo |
| CVE-2026-50547 | 7.5 | 2026-09-25 | InvoicePlane is a self-hosted open source application for managing invoices, clients, and payments. Prior to 1.7.2, Invo |
| CVE-2026-62262 | 9.1 | 2026-09-25 | Piwigo is a full featured open source photo gallery application for the web. In 17.0.0beta1 and earlier, when rating is  |
| CVE-2026-92161 | 9.8 | 2026-09-25 | FriendsOfFlarum OAuth allows users to log in to Flarum with GitHub, Twitter, Facebook, and other providers. Prior to 1.7 |
| CVE-2026-89032 | 7.7 | 2026-09-25 | BerriAI LiteLLM before 1.101.0-rc.1 contains a tenant isolation bypass vulnerability in the semantic cache layer that al |
| CVE-2026-91837 | 7.8 | 2026-09-25 | A flaw was found in NetworkManager-iodine, the iodine VPN plugin for NetworkManager. A local unprivileged user can explo |
| CVE-2026-94445 | 8.8 | 2026-09-25 | A malicious txtar could escape the intended execution context and force arbitrary writes to the playground host's truste |
| CVE-2026-97871 | 7.3 | 2026-09-25 | A vulnerability has been found in Zhonglun CloudPos up to 3.0.1.76. This issue affects the function OpenLocalBrowser of  |
| CVE-2026-97877 | 7.3 | 2026-09-25 | A vulnerability was determined in zhistaredu StarTraining up to 3.8.1. This issue affects the function UserLoginService. |
| CVE-2026-97878 | 7.3 | 2026-09-25 | A vulnerability was identified in zhistaredu StarTraining up to 3.8.1. Impacted is the function anonymous of the file /d |
| CVE-2026-91838 | 7.8 | 2026-09-25 | A flaw was found in NetworkManager-sstp, the SSTP VPN plugin for NetworkManager. A local unprivileged user can exploit t |
| CVE-2026-91839 | 7.8 | 2026-09-25 | A flaw was found in NetworkManager-fortisslvpn, the FortiSSLVPN plugin for NetworkManager. The nm-fortisslvpn-service im |
| CVE-2026-91840 | 7.8 | 2026-09-25 | A flaw was found in NetworkManager-vpnc. This vulnerability allows a local unprivileged user to escalate privileges to r |
| CVE-2026-91841 | 7.8 | 2026-09-25 | A flaw was found in NetworkManager-vpnc, a VPN plugin for NetworkManager. A local unprivileged user can exploit this vul |
| CVE-2026-97882 | 7.3 | 2026-09-25 | A weakness has been identified in mathurvishal CloudClassroom-PHP-Project up to 5dadec098bfbbf3300d60c3494db3fb95b66e7be |
| CVE-2026-97883 | 7.3 | 2026-09-25 | A security vulnerability has been detected in mathurvishal CloudClassroom-PHP-Project up to 5dadec098bfbbf3300d60c3494db |
| CVE-2026-97885 | 7.3 | 2026-09-25 | A flaw has been found in mathurvishal CloudClassroom-PHP-Project up to 5dadec098bfbbf3300d60c3494db3fb95b66e7be. Affecte |
| CVE-2026-97060 | 7.2 | 2026-09-25 | X-SpringBoot through 6.0 lacks object-level authorization in user management endpoints, allowing sub-administrators to m |
| CVE-2026-97063 | 9.1 | 2026-09-25 | X-SpringBoot through 6.0 returns login verification codes in HTTP responses from unauthenticated endpoints GET /sys/mobi |
| CVE-2026-97064 | 9.1 | 2026-09-25 | X-SpringBoot through 6.0 ships with a hardcoded static master login verification code 172839 enabled by default in the d |
| CVE-2026-100208 | 7.5 | 2026-09-25 | Integer overflow or wraparound in Microsoft Office Outlook allows an unauthorized attacker to execute code over a networ |
| CVE-2026-100310 | 7.0 | 2026-09-25 | GNU libextractor before 1.16 loads plugins from an untrusted search path specified by the LIBEXTRACTOR_PREFIX environmen |
| CVE-2026-100368 | 8.4 | 2026-09-25 | CliInvoke is a .NET library for invoking command-line programs, and its `CliInvoke.Specializations` packages provide spe |
| CVE-2026-100372 | 7.2 | 2026-09-25 | ClipBucket v5 before 5.5.3-#197 contains a path traversal vulnerability in the admin template editor that allows authent |
| CVE-2026-5267 | 7.5 | 2026-09-25 | Ciena Navigator Network
Control Suite (NCS) contains an information exposure vulnerability in an
event-streaming API tha |
| CVE-2026-100369 | 8.4 | 2026-09-25 | CliInvoke and its formerly named `AlastairLundy.CliInvoke` package are .NET libraries for invoking command-line programs |
| CVE-2026-100387 | 8.1 | 2026-09-25 | pgPointcloud through 1.2.5 contains a heap out-of-bounds read vulnerability in dimensional patch WKB deserialization tha |
| CVE-2026-100389 | 8.1 | 2026-09-25 | GestSup versions before 3.2.61 contain a remote code execution vulnerability in the basic IMAP connector's attachment ha |
| CVE-2026-100390 | 7.4 | 2026-09-25 | Zoraxy versions 3.2.3 through 3.3.4 fail to properly parse IPv6 addresses in the RemoteAddr field when setting forwarded |
| CVE-2026-100391 | 8.2 | 2026-09-25 | MediaFlow Proxy through 2.4.9 contains a server-side request forgery vulnerability in the /proxy routes due to missing a |
| CVE-2026-10758 | 7.5 | 2026-09-25 | Esri LERC is an open-source image or raster format which supports rapid encoding and decoding for any pixel type. A Heap |
| CVE-2026-57443 | 7.5 | 2026-09-25 | SCBE-AETHERMOORE is a geometric AI governance and evaluation framework. Starting in version 4.0.2 and prior to version 4 |
| CVE-2026-91765 | 7.5 | 2026-09-25 | cleanup_xml_node() in the SOAP XML parser recurses once per XML nesting level with no depth limit. An unauthenticated at |
| CVE-2026-100419 | 7.0 | 2026-09-25 | gitoxide gix-fs before 0.23.0 contains a path validation bypass vulnerability in the worktree checkout mechanism that al |
| CVE-2026-96795 | 8.8 | 2026-09-25 | Horilla is an HR and CRM software. Prior to 2.0.0, HorillaListView.export_data in horilla_views/generic/cbv/views.py acc |
| CVE-2026-100504 | 7.0 | 2026-09-26 | Ghidra versions through 12.1.4 contain a stack-based out-of-bounds write vulnerability in the decompiler's leftshift128  |
| CVE-2026-100520 | 8.8 | 2026-09-26 | Laranode versions before 1.2.1 contain a path traversal vulnerability in the POST /filemanager/upload-file endpoint that |
| CVE-2026-100530 | 7.3 | 2026-09-26 | OpenClaw versions before 2026.8.1 fail to bind working directory context to reusable exec approvals, allowing approved c |
| CVE-2026-100532 | 8.1 | 2026-09-26 | @openclaw/whatsapp (npm) before 2026.8.1 exposes the WhatsApp login tool through the generic channel-tool path without p |
| CVE-2026-100535 | 7.5 | 2026-09-26 | OpenClaw (npm package 'openclaw') versions >= 2026.4.5 and < 2026.8.1 can lose the originating requester's restrictions  |
| CVE-2026-100541 | 7.5 | 2026-09-26 | OpenClaw's Matrix integration (npm package @openclaw/matrix) versions >= 2026.2.2 and < 2026.8.1 lowercase complete Matr |
| CVE-2026-100543 | 7.5 | 2026-09-26 | OpenClaw (npm package openclaw) before 2026.8.1 could include deterministic hashes computed over the original, unredacte |
| CVE-2026-100544 | 8.8 | 2026-09-26 | openclaw's @openclaw/voice-call package before 2026.8.1 launches the configured agent for classic inbound voice calls wi |
| CVE-2026-100551 | 8.3 | 2026-09-26 | OpenClaw for iOS versions >= 2026.7.1 and < 2026.8.11 do not enforce saved Gateway TLS pins in the Control UI. While nat |
| CVE-2026-100552 | 8.8 | 2026-09-26 | OpenClaw (npm package 'openclaw') before 2026.8.1 does not correctly enforce per-chat tool policies for Codex app-server |
| CVE-2026-100555 | 7.1 | 2026-09-26 | OpenClaw is an npm-distributed gateway application. In versions >= 2026.7.1 and < 2026.8.1, Synology Chat attachment del |
| CVE-2026-100557 | 8.3 | 2026-09-26 | OpenClaw versions before 2026.8.1 contain an authorization bypass vulnerability in skill tool dispatch that fails to car |
| CVE-2026-100558 | 7.5 | 2026-09-26 | OpenClaw versions before 2026.8.1 contain a resource exhaustion vulnerability in the Gateway listener that allows unauth |
| CVE-2026-100559 | 8.0 | 2026-09-26 | OpenClaw versions before 2026.8.1 contain a command parser vulnerability where escaped newlines confuse exec allowlist p |
| CVE-2026-100560 | 7.5 | 2026-09-26 | OpenClaw versions before 2026.8.1 contain an authorization bypass vulnerability where Allow Always approvals for exact c |
| CVE-2026-100561 | 8.0 | 2026-09-26 | OpenClaw (npm package 'openclaw') versions >= 2026.3.22 and < 2026.8.1 contain an approval-bypass flaw in the exec appro |
| CVE-2026-100567 | 8.2 | 2026-09-26 | OpenClaw is an agent gateway distributed as the npm package 'openclaw'. In versions >= 2026.4.5 and < 2026.8.1, the Gate |
| CVE-2026-100568 | 8.3 | 2026-09-26 | OpenClaw versions before 2026.8.1 fail to properly restrict access to operator command cron jobs, allowing model-visible |
| CVE-2026-100570 | 7.8 | 2026-09-26 | OpenClaw (npm package 'openclaw') versions >= 2026.3.28 and < 2026.8.1 allow an untrusted workspace .env file to set the |
| CVE-2026-100575 | 8.8 | 2026-09-26 | OpenClaw Slack versions before 2026.8.1 fail to properly enforce sender allowlists in multi-person direct messages. Disa |
| CVE-2026-100578 | 7.6 | 2026-09-26 | OpenClaw (npm package `openclaw`) before 2026.7.1 fails to restrict owner-only infrastructure tools exposed through the  |
| CVE-2026-100579 | 7.6 | 2026-09-26 | OpenClaw (npm package 'openclaw') before 2026.7.1 incorrectly trusts requester provenance in message.action. In identity |
| CVE-2026-100580 | 8.8 | 2026-09-26 | OpenClaw (npm package 'openclaw') before 2026.7.1 improperly handles case sensitivity in the model-facing cron tool: a m |
| CVE-2026-100585 | 8.0 | 2026-09-26 | OpenClaw (npm package `openclaw`) before 2026.7.1 fails to enforce the owner-only authorization requirement for Claude C |
| CVE-2026-100586 | 8.8 | 2026-09-26 | OpenClaw Codex before 2026.7.1 fails to properly enforce owner authorization when creating native conversation bindings. |
| CVE-2026-100587 | 8.8 | 2026-09-26 | OpenClaw versions before 2026.7.1 fail to properly validate owner authorization in the Codex computer-use installation c |
| CVE-2026-100588 | 8.3 | 2026-09-26 | OpenClaw (npm package 'openclaw') before 2026.7.1 does not enforce the administrator scope requirement on browser contro |
| CVE-2026-100589 | 8.3 | 2026-09-26 | OpenClaw versions before 2026.7.1 contain a sandbox bypass vulnerability in the browser tool that allows sandboxed sessi |
| CVE-2026-100596 | 8.8 | 2026-09-26 | OpenClaw versions before 2026.7.1 fail to properly authorize non-owner users executing MCP configuration changes through |
| CVE-2026-100597 | 7.8 | 2026-09-26 | OpenClaw (npm package 'openclaw') before 2026.7.1 is vulnerable to a time-of-check time-of-use race condition in OpenShe |
| CVE-2026-100598 | 7.1 | 2026-09-26 | OpenClaw (npm package openclaw) before 2026.7.1 incorrectly binds Signal approval reactions. In affected versions, a rea |
| CVE-2026-100599 | 8.8 | 2026-09-26 | OpenClaw versions 2026.5.1 through 2026.7.0 fail to apply the configured exec approval path to Google Meet node commands |
| CVE-2026-18143 | 9.8 | 2026-09-26 | The Request a Quote for WooCommerce plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, a |
| CVE-2026-100314 | 7.3 | 2026-09-26 | A security vulnerability has been detected in mathurvishal CloudClassroom-PHP-Project up to 5dadec098bfbbf3300d60c3494db |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-67279 | MikroTik / RouterOS | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-65660 | Microsoft / SharePoint | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-87902 | WordPress / Core | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-5430 | WSO2 / Multiple Products | 2026-09-24 | 2026-09-27 | Unknown |
| CVE-2026-71362 | Adobe / Commerce and Magento  | 2026-09-24 | 2026-09-27 | Unknown |
| CVE-2026-93952 | Arista / VeloCloud Orchestrator | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-94127 | F5 / BIG-IP APM | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-93616 | Check Point / Multiple Products | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-85102 | Check Point / Multiple Products | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-7273 | Zyxel / GS1900 Series Switches | 2026-09-21 | 2026-09-24 | Unknown |

---

*Total entries in CISA KEV catalog: 1726*