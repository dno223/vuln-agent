# Vulnerability Intelligence Report

**Date:** 2026-11-02  
**Generated:** 2026-11-02T17:50:05Z  

---

## Executive Summary

Our environment faces significant exposure from 101 high-severity CVEs, including five critical CVSS 10.0 vulnerabilities in WAVLINK network devices with remote code execution potential. Additionally, 10 new entries were added to the CISA Known Exploited Vulnerabilities catalog this week, targeting widely deployed platforms including Ivanti Connect Secure, GitLab, Cisco Firewall, and VMware ESX. While no monitored CVEs currently match the KEV catalog, the breadth of critical network device vulnerabilities and active exploitation of enterprise infrastructure products represents an urgent and escalating threat to business operations.

---

## Risk Narrative

The current threat landscape reflects active exploitation of critical enterprise infrastructure by sophisticated threat actors. WAVLINK device vulnerabilities with maximum CVSS scores expose network perimeters to unauthenticated remote compromise. Simultaneously, CISA's addition of Ivanti, Cisco, VMware, and GitLab vulnerabilities to the KEV catalog confirms real-world exploitation is underway. These platforms are foundational to remote access, network security, virtualization, and software development pipelines. A successful attack on any of these could result in full network takeover, data exfiltration, ransomware deployment, or supply chain compromise, posing severe financial, operational, and reputational risk to the organization.

---

## Prioritized Action Items

1. Immediately audit your environment for WAVLINK WN536AX6-A and WN553X1-B devices and isolate or patch them due to CVSS 10.0 remote code execution vulnerabilities.
2. Verify and apply emergency patches for Ivanti Connect Secure following two KEV additions on 2026-10-30 that indicate active exploitation in the wild.
3. Assess and patch Cisco Secure Firewall ASA and FTD Software per the CISA KEV entry added 2026-10-29 to prevent perimeter compromise.
4. Patch VMware ESX environments immediately in response to the Broadcom VMware KEV entry, as hypervisor exploitation can compromise entire virtualized infrastructure.
5. Audit GitLab Community and Enterprise Edition instances for the KEV-listed vulnerability and apply available patches to protect source code and CI/CD pipelines.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-120238 | 9.9 | 2026-11-01 | A vulnerability has been found in WAVLINK WN553X1-B 260403_2.0.0. This affects the function sub_4162A8 of the file /bin/ |
| CVE-2026-120239 | 9.9 | 2026-11-01 | A vulnerability was found in WAVLINK WN553X1-B V260403_2.0.0. This vulnerability affects the function sub_419DA8 of the  |
| CVE-2026-120240 | 9.9 | 2026-11-01 | A vulnerability was determined in WAVLINK WN553X1-B V260403_2.0.0. This issue affects the function sub_41A748 of the fil |
| CVE-2026-120241 | 7.5 | 2026-11-01 | A vulnerability was identified in Ruijie RG-ES205GC, RG-ES206GC-P, RG-ES208GC, RG-ES210GC-LP and RG-ES210GS-P ESW_1.0(1) |
| CVE-2026-120276 | 10.0 | 2026-11-02 | A weakness has been identified in WAVLINK WN536AX6-A V260507_2.0.0. This vulnerability affects the function sub_416760 o |
| CVE-2026-120277 | 10.0 | 2026-11-02 | A security vulnerability has been detected in WAVLINK WN536AX6-A V260507_2.0.0. This issue affects the function sub_41a1 |
| CVE-2026-120279 | 10.0 | 2026-11-02 | A flaw has been found in WAVLINK WN536AX6-A V260507. The affected element is an unknown function of the file /protocol.c |
| CVE-2026-120280 | 10.0 | 2026-11-02 | A vulnerability has been found in WAVLINK WN536AX6-A V260507. The impacted element is the function wireguard_cli_group h |
| CVE-2026-120281 | 10.0 | 2026-11-02 | A vulnerability was found in WAVLINK WN536AX6-A V260507. This affects the function strcpy of the file /protocol.csp of t |
| CVE-2026-120282 | 9.9 | 2026-11-02 | A vulnerability was determined in WAVLINK WN536AX6-A V260507. This impacts the function host_black of the file /protocol |
| CVE-2026-120283 | 10.0 | 2026-11-02 | A vulnerability was identified in Linksys E8450 1.2.00.360516. Affected is the function strcpy of the file /www/cgi-bin/ |
| CVE-2026-120322 | 9.9 | 2026-11-02 | A vulnerability was identified in Termix-SSH Termix up to 2.9.2. This issue affects some unknown processing of the file  |
| CVE-2026-120311 | 8.8 | 2026-11-02 | Network-AI from 5.13.4 before 5.15.5 contains a path traversal vulnerability in FileJobStore that allows attackers to re |
| CVE-2026-120312 | 8.8 | 2026-11-02 | Network-AI from 5.13.4 before 5.15.5 contains a path traversal vulnerability in AgentVCR that allows attackers controlli |
| CVE-2026-120313 | 7.5 | 2026-11-02 | Network-AI before 5.15.5 contains a path traversal vulnerability in InputSanitizer.sanitizePath() that allows attackers  |
| CVE-2026-120314 | 7.3 | 2026-11-02 | Network-AI from 5.14.0 before 5.15.5 contains a missing authentication vulnerability in the A2AServer class that allows  |
| CVE-2026-120315 | 8.8 | 2026-11-02 | LobeHub Chat from 1.84.26 before 2.1.49 contains a path traversal vulnerability that allows authenticated users to write |
| CVE-2026-120324 | 8.3 | 2026-11-02 | A weakness has been identified in Aklivity Zilla up to 1.3.4/2.4.7/2.5.0-rc2. The affected element is the function Path. |
| CVE-2026-20499 | 7.5 | 2026-11-02 | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation of |
| CVE-2026-20545 | 7.5 | 2026-11-02 | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation of |
| CVE-2026-20546 | 7.5 | 2026-11-02 | In Modem, there is a possible out of bounds write due to an incorrect bounds check. This could lead to remote escalation |
| CVE-2026-20547 | 7.5 | 2026-11-02 | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation of |
| CVE-2026-20548 | 7.5 | 2026-11-02 | In Modem, there is a possible out of bounds write due to an integer overflow. This could lead to remote escalation of pr |
| CVE-2026-20549 | 7.5 | 2026-11-02 | In Modem, there is a possible out of bounds write due to improper input validation. This could lead to remote escalation |
| CVE-2026-20554 | 7.1 | 2026-11-02 | In Modem, there is a possible system crash due to a missing bounds check. This could lead to remote escalation of privil |
| CVE-2026-20556 | 7.5 | 2026-11-02 | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation of |
| CVE-2026-20557 | 7.5 | 2026-11-02 | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation of |
| CVE-2026-20558 | 8.4 | 2026-11-02 | In GPU pdma, there is a possible escalation of privilege due to use after free. This could lead to local escalation of p |
| CVE-2026-20559 | 7.8 | 2026-11-02 | In GPU pdma, there is a possible memory corruption due to use after free. This could lead to local escalation of privile |
| CVE-2026-20565 | 8.4 | 2026-11-02 | In Modem, there is a possible out of bounds write due to an incorrect bounds check. This could lead to local escalation  |
| CVE-2026-20585 | 7.5 | 2026-11-02 | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation of |
| CVE-2026-20591 | 8.4 | 2026-11-02 | In GPU pdma, there is a possible escalation of privilege due to a missing permission check. This could lead to local esc |
| CVE-2026-120336 | 7.3 | 2026-11-02 | A vulnerability was found in VStarcam O-KAM Client 1.3.3.32. Affected by this vulnerability is the function FUN_10003EA0 |
| CVE-2026-120337 | 7.3 | 2026-11-02 | A vulnerability was determined in VStarcam O-KAM SuperIPCam 1.3.3.32. Affected by this issue is the function FUN_005a2d4 |
| CVE-2026-120341 | 7.3 | 2026-11-02 | A security vulnerability has been detected in mathurvishal CloudClassroom-PHP-Project. Impacted is an unknown function o |
| CVE-2026-120342 | 7.3 | 2026-11-02 | A vulnerability was detected in mathurvishal CloudClassroom-PHP-Project. The affected element is an unknown function of  |
| CVE-2026-120344 | 10.0 | 2026-11-02 | A vulnerability has been found in WAVLINK WN551X3-A M51X3_V251020-WO-182e965. This affects the function system of the fi |
| CVE-2025-11969 | 9.4 | 2026-11-02 | The System REST APIs do not correctly enforce access control mechanisms, allowing users with lower privilege roles to ex |
| CVE-2026-120345 | 10.0 | 2026-11-02 | A vulnerability was found in WAVLINK WN551X3-A M51X3_V251020-WO-182e965. This impacts the function sub_41a430 of the fil |
| CVE-2026-120347 | 7.3 | 2026-11-02 | A vulnerability was determined in dayrui XunRuiCMS up to 4.7.4. Affected is the function View of the file dayrui/Fcms/Co |
| CVE-2026-120348 | 7.3 | 2026-11-02 | A vulnerability was identified in dayrui XunRuiCMS up to 4.7.4. Affected by this vulnerability is the function _get_tpl_ |
| CVE-2026-101176 | 7.1 | 2026-11-02 | Permission control vulnerability in the event notification management module.
Impact: Successful exploitation of this vu |
| CVE-2026-101186 | 7.5 | 2026-11-02 | DoS vulnerability in the window module.
Impact: Successful exploitation of this vulnerability may affect availability. |
| CVE-2026-120349 | 7.3 | 2026-11-02 | A security flaw has been discovered in dayrui XunRuiCMS up to 4.7.4. Affected by this issue is the function str_replace  |
| CVE-2026-18199 | 8.8 | 2026-11-02 | Zohocorp ManageEngine Password Manager Pro versions before 13236 and PAM360 versions before 8601 are vulnerable to an au |
| CVE-2026-117518 | 8.2 | 2026-11-02 | @fastify/reply-from is a Fastify plugin that forwards requests to an upstream HTTP server. In versions up to and includi |
| CVE-2026-120213 | 9.1 | 2026-11-02 | @fastify/http-proxy is a Fastify plugin that proxies HTTP requests to an upstream server under a configured prefix. In v |
| CVE-2026-2613 | 8.7 | 2026-11-02 | The Admin REST API accepts user-supplied input without adequately sanitizing it, allowing it to be included in the struc |
| CVE-2026-8923 | 8.7 | 2026-11-02 | Zohocorp ManageEngine Eventlog Analyzer and ManageEngine Log360 versions before 13062 are vulnerable to Authenticated Re |
| CVE-2026-92886 | 7.8 | 2026-11-02 | Missing Authorization vulnerability in TÜBİTAK BİLGEM Software Technologies Research Institute eta-register allows Privi |
| CVE-2026-94349 | 8.0 | 2026-11-02 | Dell OpenManage Enterprise, versions prior to 4.8.0, contains an Improper Neutralization of Special Elements used in an  |
| CVE-2026-74993 | 7.5 | 2026-11-02 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Starnet Computer a |
| CVE-2026-120318 | 7.2 | 2026-11-02 | Product Gallery Slider & Additional Variation Images for WooCommerce 2.3.23 before 2.3.26 contains a missing authorizati |
| CVE-2026-120426 | 7.5 | 2026-11-02 | OpenCSG CSGHub through v2.6.0-ce contains an authorization bypass vulnerability in the unauthenticated file resolve rout |
| CVE-2026-120429 | 7.1 | 2026-11-02 | Camaleon CMS before 2.9.2 contains a missing authorization vulnerability in Admin::MediaController that allows low-privi |
| CVE-2026-120431 | 7.8 | 2026-11-02 | Netpbm before 10.86.51, 11.x before 11.02.29, and 11.03 before 11.15.07 contains a heap-based buffer overflow in sgitopn |
| CVE-2026-120432 | 7.8 | 2026-11-02 | Netpbm before 10.86.51, 11.02.30, and 11.15.08 contains an integer overflow vulnerability in winicontopam that allows at |
| CVE-2026-120433 | 7.8 | 2026-11-02 | Netpbm before 10.86.51, 11.x before 11.02.30, and 11.03 before 11.15.08 contains a stack-based buffer overflow in the pi |
| CVE-2026-120434 | 7.8 | 2026-11-02 | Netpbm before 10.86.51, 11.x before 11.02.30, and 11.03 before 11.15.08 contains a stack-based buffer overflow in pictto |
| CVE-2026-120435 | 7.8 | 2026-11-02 | Netpbm before 10.86.51, 11.x before 11.02.30, and 11.03 before 11.15.08 contains a heap buffer overflow in xpmtoppm caus |
| CVE-2026-120436 | 7.8 | 2026-11-02 | Netpbm before 10.86.51, 11.x before 11.02.30, and 11.03 before 11.15.08 contains an integer overflow in jbigtopnm that c |
| CVE-2026-120438 | 7.8 | 2026-11-02 | QuickJS-NG before 0.16.0 contains an integer overflow in js_proxy_get_own_property_names() in quickjs.c that causes a he |
| CVE-2026-120439 | 7.0 | 2026-11-02 | QuickJS-NG before 0.16.0 contains an integer overflow in js_typed_array_sort() in quickjs.c that allows attackers to cau |
| CVE-2026-120442 | 9.8 | 2026-11-02 | ape-volo-admin before 3.6.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to for |
| CVE-2026-120444 | 8.1 | 2026-11-02 | GoFound through 1.4.1 contains a path traversal vulnerability that allows unauthenticated attackers to delete arbitrary  |
| CVE-2026-120445 | 8.8 | 2026-11-02 | madong-admin-saas through 5.1.4 contains an incorrect authorization vulnerability in AccessTokenMiddleware that allows a |
| CVE-2026-120446 | 9.4 | 2026-11-02 | madong-admin-saas through 5.1.4 contains a missing authentication vulnerability in the platform tenant management API be |
| CVE-2026-120447 | 8.1 | 2026-11-02 | HotGo through 2.15.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to choose the |
| CVE-2026-120448 | 8.1 | 2026-11-02 | DoraCMS through 3.1.0 contains a mass assignment vulnerability in the PUT /api/v1/user/api-keys/:id endpoint that allows |
| CVE-2026-120459 | 7.4 | 2026-11-02 | python-jose through 3.5.0 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge |
| CVE-2026-120460 | 8.8 | 2026-11-02 | Jpom through 2.11.12 contains a cross-workspace authorization bypass vulnerability that allows authenticated users to ma |
| CVE-2026-120461 | 8.8 | 2026-11-02 | Jpom through 2.11.12 contains a cross-workspace authorization bypass in POST /node/ssh_command/batch that resolves comma |
| CVE-2026-120487 | 7.2 | 2026-11-02 | LaraDashboard before 1.4.5 contains an incorrect authorization vulnerability in SettingPolicy::manageCoreUpgrades() that |
| CVE-2026-73695 | 8.8 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.16 contains a path traversal vulnerability in services/users/index.php |
| CVE-2026-73696 | 9.1 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.12 contains an execution after redirect vulnerability in the user pane |
| CVE-2026-73697 | 8.8 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.16 contains an arbitrary file write and OS command injection vulnerabi |
| CVE-2026-104080 | 8.4 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.30 contains an OS command injection vulnerability in the loopback API  |
| CVE-2026-109140 | 8.4 | 2026-11-02 | The vulnerability is that Krill encrypts every login-session token with a nonce built from a counter that is reset to 0  |
| CVE-2026-109141 | 8.4 | 2026-11-02 | The vulnerability gives a role that is restricted to a list of CAs (cas = [...]) its full permission set for every reque |
| CVE-2026-109142 | 8.4 | 2026-11-02 | When a CA's parent lives on the same Krill server: instead of building and verifying a signed CMS message, it runs the R |
| CVE-2026-77876 | 9.8 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.16 contains an OS command injection vulnerability in the protected_dir |
| CVE-2026-77877 | 8.4 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.30 contains a missing authentication vulnerability that allows attacke |
| CVE-2026-77878 | 8.4 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.30 contains an OS command injection vulnerability in the loopback API  |
| CVE-2026-77879 | 7.7 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.16 contains a SQL injection vulnerability in the loopback API authenti |
| CVE-2026-77880 | 8.4 | 2026-11-02 | Control Web Panel (CWP) before webpanel_version 1.16 contains an OS command injection vulnerability in the loopback API  |
| CVE-2026-88809 | 7.6 | 2026-11-02 | A security vulnerability exists in the SUSE Rancher Manager meta proxy endpoint (/meta/proxy). This endpoint is intended |
| CVE-2026-94290 | 9.1 | 2026-11-02 | SUSE Rancher Fleet clusters reference a kubeconfig secret that the controller uses to install and manage a Fleet agent o |
| CVE-2026-99218 | 7.0 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

coredump: hold RCU while releasing parked threads

 |
| CVE-2026-99224 | 7.0 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

keys: Protect the type name while describing a key
 |
| CVE-2026-99227 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

io_uring/waitid: prevent cancel reference wrap

io_ |
| CVE-2026-99231 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

io_uring/waitid: own the request before clearing -> |
| CVE-2026-99233 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

tracing/histograms: Verify event_call identity when |
| CVE-2026-99235 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

tracing: Save the event file instead of the compati |
| CVE-2026-99236 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

tracing: Reject incomplete event filter expressions |
| CVE-2026-99237 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

tracing: Hold trace_types_lock when resetting last  |
| CVE-2026-99238 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

tracing: Hold trace_types_lock when updating module |
| CVE-2026-99239 | 7.8 | 2026-11-02 | In the Linux kernel, the following vulnerability has been resolved:

Bluetooth: L2CAP: refuse __l2cap_chan_add if chan a |
| CVE-2026-105769 | 9.3 | 2026-11-02 | kaniko before 1.25.20 can send a Microsoft Entra ID (Azure AD) access token for Azure Resource Manager to an attacker-co |
| CVE-2026-119301 | 7.9 | 2026-11-02 | Improper neutralization of quoting syntax in SQL identifier construction in the Apache Iceberg write component in AWS SD |
| CVE-2026-88810 | 7.2 | 2026-11-02 | A privilege escalation issue was discovered in Rancher Manager's role-based access control. The inheritedNamespacedRules |
| CVE-2026-88811 | 9.1 | 2026-11-02 | Missing filtering in the SUSE Rancher Manager meta proxy could cause passed in rancher credentials to be leaked to cloud |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-118527 | Ivanti / Connect Secure | 2026-10-30 | 2026-11-13 | Unknown |
| CVE-2026-111357 | Ivanti / Connect Secure | 2026-10-30 | 2026-11-02 | Unknown |
| CVE-2026-97229 | GitLab / Community Edition and Enterprise Edition | 2026-10-29 | 2026-11-01 | Unknown |
| CVE-2026-76418 | Cisco / Secure Firewall ASA Software and Cisco Secure FTD Software | 2026-10-29 | 2026-11-01 | Unknown |
| CVE-2026-41709 | Broadcom / VMware ESX | 2026-10-28 | 2026-11-11 | Unknown |
| CVE-2026-46300 | Linux / Kernel | 2026-10-28 | 2026-10-31 | Unknown |
| CVE-2026-48356 | Adobe / Commerce and Magento | 2026-10-27 | 2026-11-10 | Unknown |
| CVE-2026-111497 | Google / Brotli | 2026-10-27 | 2026-11-10 | Unknown |
| CVE-2026-109618 | PHP Group / PHP | 2026-10-26 | 2026-10-29 | Unknown |
| CVE-2026-109619 | PHP Group / PHP | 2026-10-26 | 2026-10-29 | Unknown |

---

*Total entries in CISA KEV catalog: 1766*