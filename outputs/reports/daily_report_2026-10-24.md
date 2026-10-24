# Vulnerability Intelligence Report

**Date:** 2026-10-24  
**Generated:** 2026-10-24T12:27:25Z  

---

## Executive Summary

Our environment faces significant exposure from 95 high-severity CVEs, predominantly critical deserialization vulnerabilities (CVSS 9.8) in WordPress themes that enable remote object injection and potential full system compromise. Eight new entries were added to CISA's Known Exploited Vulnerabilities catalog this week, including actively exploited flaws in Arista VeloCloud, Collabora Online, Plex Media Server, and SiteGuard Server Edition. These KEV additions confirm threat actors are actively leveraging similar classes of vulnerabilities in production environments. Immediate remediation prioritization is required to reduce organizational risk exposure across web infrastructure and third-party software components.

---

## Risk Narrative

The current threat landscape is characterized by aggressive exploitation of deserialization vulnerabilities in widely deployed WordPress themes, enabling unauthenticated attackers to achieve remote code execution and full system takeover. The concentration of CVSS 9.8-scored flaws across multiple vendor themes amplifies supply chain risk. Simultaneously, CISA's addition of eight KEV entries within seven days signals elevated adversary interest in network orchestration platforms, media servers, and collaboration tools. Successful exploitation could result in data exfiltration, ransomware deployment, or lateral movement across enterprise networks. Business risks include regulatory penalties, reputational damage, and operational disruption if these vulnerabilities remain unaddressed.

---

## Prioritized Action Items

1. Immediately audit all WordPress installations for affected ThemeREX, AivahThemes, and axiomthemes plugins and apply vendor patches or remove unused themes within 48 hours.
2. Patch or isolate all instances of Arista VeloCloud Orchestrator, Plex Media Server, and SiteGuard Server Edition in line with CISA KEV remediation deadlines.
3. Conduct an emergency inventory of PHP-based web applications to identify exposure to Remote File Inclusion vulnerabilities, particularly the AncoraThemes Your Dress flaw (CVE-2026-112850).
4. Implement web application firewall rules to detect and block deserialization attack payloads targeting vulnerable WordPress theme endpoints while patches are applied.
5. Establish a recurring 72-hour patch cycle for all CISA KEV additions and enforce automated alerting when monitored CVEs appear in the KEV catalog.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-112846 | 9.8 | 2026-10-23 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Save Life save-life allows Object Injection.This issue |
| CVE-2026-112847 | 9.8 | 2026-10-23 | Deserialization of Untrusted Data vulnerability in ThemeREX ZenSoul zensoul allows Object Injection.This issue affects Z |
| CVE-2026-112848 | 9.8 | 2026-10-23 | Deserialization of Untrusted Data vulnerability in AivahThemes Hostme v2 hostmev2 allows Object Injection.This issue aff |
| CVE-2026-112849 | 7.1 | 2026-10-23 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in AivahThemes Hostme |
| CVE-2026-112850 | 8.1 | 2026-10-23 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2026-112851 | 9.8 | 2026-10-23 | Deserialization of Untrusted Data vulnerability in ThemeREX Group HotLock hotlock allows Object Injection.This issue aff |
| CVE-2026-112852 | 8.1 | 2026-10-23 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Helion helion allows Object Injection.This issue affec |
| CVE-2026-112853 | 9.8 | 2026-10-23 | Deserialization of Untrusted Data vulnerability in axiomthemes Hallelujah hallelujah allows Object Injection.This issue  |
| CVE-2026-112854 | 9.8 | 2026-10-23 | Deserialization of Untrusted Data vulnerability in axiomthemes Holistic Center holistic-center allows Object Injection.T |
| CVE-2026-112855 | 9.8 | 2026-10-23 | Deserialization of Untrusted Data vulnerability in axiomthemes Redy redy allows Object Injection.This issue affects Redy |
| CVE-2026-112856 | 9.8 | 2026-10-23 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Vagabonds vagabonds allows Object Injection.This issue |
| CVE-2026-112857 | 9.8 | 2026-10-23 | Deserialization of Untrusted Data vulnerability in axiomthemes Reprizo reprizo allows Object Injection.This issue affect |
| CVE-2026-112858 | 9.8 | 2026-10-23 | Deserialization of Untrusted Data vulnerability in axiomthemes Rhodos rhodos allows Object Injection.This issue affects  |
| CVE-2026-112859 | 9.8 | 2026-10-23 | Deserialization of Untrusted Data vulnerability in ThemeREX Group Little Birdies little-birdies allows Object Injection. |
| CVE-2026-112863 | 7.1 | 2026-10-23 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Hogash KALLYAS kal |
| CVE-2026-115728 | 7.5 | 2026-10-23 | @hapi/content from 6.0.1 before 6.0.3 contains a regular expression denial of service vulnerability in Content.dispositi |
| CVE-2026-57113 | 8.1 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 2.6.0 to before version 4.6.59, PraisonAI's template loader accept |
| CVE-2026-57114 | 7.2 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 4.5.126 to before version 4.6.59, PraisonAI's Async Jobs API valid |
| CVE-2026-57116 | 9.8 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 4.2.1 to before version 4.6.59, PraisonAI's AgentOS FastAPI deploy |
| CVE-2026-57117 | 8.8 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 4.6.10 to before version 4.6.59, LocalManagedAgent / SandboxedAgen |
| CVE-2026-57121 | 8.1 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 0.1.4 to before version 0.1.5 in praisonai-platform, a workspace m |
| CVE-2026-57142 | 7.8 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 4.5.87 to before version 4.6.61, PraisonAI recipe execution has a  |
| CVE-2026-57144 | 8.8 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 4.5.110 to before version 4.6.61, praisonai.sandbox.SandlockSandbo |
| CVE-2026-57146 | 7.5 | 2026-10-23 | PraisonAI is a multi-agent teams system. From version 4.5.115 to before version 4.6.61, the published A2U advisory GHSA- |
| CVE-2026-63120 | 8.4 | 2026-10-23 | pghoard is a PostgreSQL backup daemon and restore tooling that stores backup data in cloud object stores. Prior to versi |
| CVE-2026-10632 | 8.7 | 2026-10-23 | A reflected cross-site scripting vulnerability in the Classic Web Client of Zimbra Collaboration Suite (ZCS) allows an a |
| CVE-2026-114621 | 8.8 | 2026-10-23 | baserCMS is a website development framework. In versions 5.0.0 before 5.3.2 and 5.4.0 before 5.4.2, list and detail acti |
| CVE-2026-114622 | 7.2 | 2026-10-23 | baserCMS is a website development framework. In versions 5.2.3 before 5.3.2 and 5.4.0 before 5.4.2, the optional BcTheme |
| CVE-2026-114624 | 7.2 | 2026-10-23 | baserCMS is a website development framework. In versions 5.0.0 before 5.3.2 and 5.4.0 before 5.4.2, the widget-area enti |
| CVE-2026-115457 | 7.1 | 2026-10-23 | baserCMS is a website development framework. In versions 5.0.0 before 5.3.2 and 5.4.0 before 5.4.2, global shortcode exp |
| CVE-2026-50053 | 8.7 | 2026-10-23 | A request attribute override vulnerability in Zimbra Collaboration Suite (ZCS) allows unauthenticated requests to /h/* t |
| CVE-2026-50056 | 7.8 | 2026-10-23 | A local privilege escalation vulnerability in the zmmailboxdmgr launcher of Zimbra Collaboration Suite (ZCS) allows the  |
| CVE-2026-50057 | 7.8 | 2026-10-23 | A local privilege escalation vulnerability in the Zimbra Collaboration Suite (ZCS) MTA package allows the Unix zimbra ac |
| CVE-2026-53921 | 9.8 | 2026-10-23 | odhcpd is the DHCPv6, DHCPv4, and router-advertisement server used by OpenWrt. Prior to version 25.12, odhcpd's DHCPv6 I |
| CVE-2026-93631 | 7.1 | 2026-10-23 | A cross-site request forgery vulnerability in the OAuth extension of Zimbra Collaboration Suite (ZCS) Network Edition al |
| CVE-2026-93639 | 8.7 | 2026-10-23 | A missing authorization vulnerability in Zimbra Collaboration Suite (ZCS) allows a delegated administrator with no expli |
| CVE-2026-93640 | 7.8 | 2026-10-23 | A local privilege escalation vulnerability in the optional dnscache package of Zimbra Collaboration Suite (ZCS) allows t |
| CVE-2026-106763 | 7.5 | 2026-10-23 | An issue in @justice8096/sagemath-mcp-server 1.0.1 allows a remote attacker to execute arbitrary code via the escapeShel |
| CVE-2026-106764 | 7.5 | 2026-10-23 | An issue in @rog0x/mcp-git-tools 1.0.1 allows a remote attacker to execute arbitrary code via the resolveBaseBranch func |
| CVE-2026-106765 | 7.5 | 2026-10-23 | An issue in @rog0x/mcp-docker-tools 1.0.1 allows a remote attacker to execute arbitrary code via the handleImageList fun |
| CVE-2026-39902 | 7.2 | 2026-10-23 | Cacti is an open source performance and fault management framework. Prior to version 1.2.31, the prior blocklist ([;&\| ` |
| CVE-2026-46651 | 9.8 | 2026-10-23 | The Goobi viewer is a web application that allows digitised material to be displayed in a web browser. From version 24.0 |
| CVE-2026-46652 | 9.8 | 2026-10-23 | The Goobi viewer is a web application that allows digitised material to be displayed in a web browser. From version 24.0 |
| CVE-2026-53942 | 9.9 | 2026-10-23 | Conda Organization Infrastructure is a centralized location for infrastructure codes. Prior to commit 9c0f238, a GitHub  |
| CVE-2026-55457 | 7.4 | 2026-10-23 | The Goobi viewer is a web application that allows digitised material to be displayed in a web browser. Prior to version  |
| CVE-2026-55459 | 7.4 | 2026-10-23 | The Goobi viewer is a web application that allows digitised material to be displayed in a web browser. From version 25.0 |
| CVE-2026-55486 | 9.3 | 2026-10-23 | The Goobi viewer is a web application that allows digitised material to be displayed in a web browser. From version 25.0 |
| CVE-2026-57845 | 8.8 | 2026-10-23 | Hugging Face Datasets through 5.1.0 contains an insecure deserialization vulnerability that allows attackers to execute  |
| CVE-2026-105482 | 7.4 | 2026-10-23 | A flaw in Node.js DNS resolution allows hostnames containing a NUL byte to be silently truncated by the dns.resolve*() f |
| CVE-2026-105483 | 7.4 | 2026-10-23 | A flaw in Node.js TLS hostname verification allows a certificate without a matching IP address SAN to authenticate a con |
| CVE-2026-106069 | 7.4 | 2026-10-23 | A flaw in Node.js TLS hostname verification can cause a server certificate to be validated against a different IP addres |
| CVE-2026-115810 | 7.7 | 2026-10-23 | Tandoor Recipes before 2.7.0 contains a server-side request forgery vulnerability in the Pestle importer that allows aut |
| CVE-2026-87901 | 8.3 | 2026-10-23 | Improper sanitization in the registration module allows reflected Cross-Site Scripting. |
| CVE-2026-110975 | 7.4 | 2026-10-23 | A flaw was found in Kruize Autotune. Its REST API ships without an authentication layer, and the endpoints that return d |
| CVE-2026-115812 | 9.8 | 2026-10-23 | Relative path traversal during model archive extraction in Amazon Web Services Multi Model Server 1.1.11 and earlier mig |
| CVE-2026-115863 | 7.6 | 2026-10-23 | ConnMan through 2.0 has a stack-based buffer overflow via a DHCPv6 Reply message. This occurs in get_domains in gdhcp/cl |
| CVE-2026-112342 | 7.1 | 2026-10-23 | Tandoor Recipes before 2.7.0 contains an improper cache-key design in cookbook/helper/permission_helper.py that allows a |
| CVE-2026-115570 | 7.4 | 2026-10-23 | Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 42.11.1 |
| CVE-2026-19741 | 7.5 | 2026-10-23 | Zephyr's OpenThread integration defined CONFIG_OPENTHREAD_JOINER_PSKD with default "J01NME" in modules/openthread/Kconfi |
| CVE-2026-79977 | 8.2 | 2026-10-23 | The WireGuard VPN service in subsys/net/lib/wireguard/wg.c updated the peer endpoint from a message it could not authent |
| CVE-2026-79979 | 7.8 | 2026-10-23 | The arm64 MMU backend invalidates a single virtual address from the TLB with invalidate_tlb_page() in arch/arm64/core/mm |
| CVE-2026-79982 | 8.8 | 2026-10-23 | The Bluetooth HCI USB transport class of the new USB device stack, subsys/usb/device_next/class/bt_hci.c, copies every c |
| CVE-2026-115776 | 7.5 | 2026-10-23 | Twisted is an event-based framework for internet applications, supporting Python 3.6+. Prior to 26.10.0rc1, twisted.word |
| CVE-2026-115778 | 7.5 | 2026-10-23 | Twisted is an event-based framework for internet applications, supporting Python 3.6+. Prior to 26.10.0rc1, twisted.conc |
| CVE-2026-58202 | 8.3 | 2026-10-23 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to ver |
| CVE-2026-65824 | 7.4 | 2026-10-23 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to ver |
| CVE-2026-65825 | 7.5 | 2026-10-23 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. In versions  |
| CVE-2026-115887 | 7.5 | 2026-10-23 | GraphQL Scalars is a library of custom GraphQL scalars for creating precise type-safe GraphQL schemas. From 1.24.1 until |
| CVE-2026-115889 | 9.9 | 2026-10-23 | Wasmtime is a runtime for WebAssembly. Prior to 36.0.19 and 43.0.0, the Cranelift compiler backend bit-packs SSA value i |
| CVE-2026-115893 | 9.9 | 2026-10-23 | Wasmtime is a runtime for WebAssembly. Prior to 36.0.19, 48.0.7, and 49.0.4, the Cranelift compiler backend on aarch64 c |
| CVE-2026-115895 | 8.8 | 2026-10-23 | Happy DOM is a JavaScript implementation of a web browser without its graphical user interface. From 17.0.0 until 21.0.4 |
| CVE-2026-115935 | 8.8 | 2026-10-23 | The app/process-api-response-headers action accepts fake Craft API response headers from any authenticated control panel |
| CVE-2026-115937 | 7.5 | 2026-10-23 | The Mollie webhook endpoint accepts two independent, attacker-controlled parameters and never verifies that they belong  |
| CVE-2026-115938 | 8.8 | 2026-10-23 | Craft CMS allows any authenticated control panel user to submit an element-search condition whose element selector is ev |
| CVE-2026-115931 | 9.9 | 2026-10-23 | Postiz lets a signed-in user ask the backend to run a function on one of their connected channels. The backend did not r |
| CVE-2026-115806 | 9.8 | 2026-10-24 | The Prime Mover – Backup and Migration plugin for WordPress is vulnerable to PHP Object Injection in all versions up to, |
| CVE-2026-115807 | 7.1 | 2026-10-24 | The User Profile Builder – Beautiful User Registration Forms, User Profiles & User Role Editor plugin for WordPress is v |
| CVE-2026-111402 | 9.3 | 2026-10-24 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Tribulant Software |
| CVE-2026-112844 | 7.1 | 2026-10-24 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Arraytics WP Event |
| CVE-2026-112866 | 9.3 | 2026-10-24 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in WPFactory Product  |
| CVE-2026-112869 | 7.1 | 2026-10-24 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Noah Hearle We’re  |
| CVE-2026-114178 | 7.1 | 2026-10-24 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Bold Grid W3 Total |
| CVE-2026-114179 | 7.1 | 2026-10-24 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in wordplus BP Better |
| CVE-2026-114196 | 9.8 | 2026-10-24 | Deserialization of Untrusted Data vulnerability in paytiumsupport Paytium paytium allows Object Injection.This issue aff |
| CVE-2026-114694 | 7.1 | 2026-10-24 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Pixelite Events Ma |
| CVE-2026-114695 | 7.1 | 2026-10-24 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Infomaniak Network |
| CVE-2026-114697 | 7.1 | 2026-10-24 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in QuarkA QA Analytic |
| CVE-2026-115975 | 7.1 | 2026-10-24 | Broken access control in JiraController in Cervantes version v1.3-beta could allow an attacker to create, edit, or delet |
| CVE-2026-94075 | 9.8 | 2026-10-24 | Deserialization of Untrusted Data vulnerability in Tribulant Software Newsletters newsletters-lite allows Object Injecti |
| CVE-2026-110018 | 8.8 | 2026-10-24 | The aBlocks – Gutenberg Blocks, User Dashboard Builder, Popup Builder, Form Builder & Animation Builder plugin for WordP |
| CVE-2026-116009 | 8.8 | 2026-10-24 | Camaleon CMS before 2.9.3 contains a path traversal vulnerability that allows users with only the media permission to wr |
| CVE-2026-116011 | 7.5 | 2026-10-24 | Crow before 1.3.4 contains an uncontrolled recursion vulnerability in crow::json::load() that allows remote unauthentica |
| CVE-2026-116014 | 8.1 | 2026-10-24 | open62541 1.5.0 before 1.5.7 contains an integer overflow in UA_DataType_fromStructureDescription() that wraps the 16-bi |
| CVE-2026-116016 | 7.1 | 2026-10-24 | yudao-cloud through 2026.09 contains an authorization bypass vulnerability that allows authenticated users to evade row- |
| CVE-2026-116019 | 8.8 | 2026-10-24 | Grav 2.0.15 before 2.2.13 contains an allowlist bypass vulnerability that allows page editors to invoke arbitrary public |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-114625 | Arista / VeloCloud Orchestrator | 2026-10-23 | 2026-10-26 | Unknown |
| CVE-2026-110447 | Collabora / Collabora Online – Built-in CODE Server | 2026-10-23 | 2026-10-26 | Unknown |
| CVE-2026-106931 | EG Secure Solutions / SiteGuard Server Edition | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96656 | Plex / Media Server | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96655 | Plex / Media Server | 2026-10-20 | 2026-11-03 | Unknown |
| CVE-2026-96654 | Plex / Media Server | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96652 | Plex / Media Server | 2026-10-20 | 2026-11-03 | Unknown |
| CVE-2026-110936 | Siemens / Software Center | 2026-10-20 | 2026-11-03 | Unknown |

---

*Total entries in CISA KEV catalog: 1756*