# Vulnerability Intelligence Report

**Date:** 2026-09-29  
**Generated:** 2026-09-29T14:37:48Z  

---

## Executive Summary

Our environment faces critical exposure across multiple fronts. Netcore NR289-GE router firmware contains five vulnerabilities, three rated CVSS 10.0, enabling unauthenticated remote code execution. SailPoint IdentityIQ and SUSE Rancher carry critical flaws allowing RCE and cross-tenant access. Twelve new CISA Known Exploited Vulnerabilities were added this week, including actively exploited flaws in Apple, Citrix NetScaler, MikroTik, and Microsoft SharePoint. One monitored CVE, CVE-2026-86950 affecting Apple products, is confirmed exploited in the wild with a federal remediation deadline of October 2, 2026. Immediate prioritization of patching and compensating controls is essential to reduce exposure.

---

## Risk Narrative

The current threat landscape reflects a convergence of critical infrastructure vulnerabilities and active exploitation by threat actors. Three CVSS 10.0 flaws in widely deployed router firmware provide trivial remote footholds, while identity and management platform vulnerabilities in SailPoint and Rancher threaten lateral movement and privilege escalation across organizational boundaries. The CISA KEV additions signal that adversaries are actively weaponizing flaws in Apple, Citrix, MikroTik, and Microsoft products. Confirmed exploitation of CVE-2026-86950 in federal environments indicates sophisticated actors are targeting endpoint and productivity platforms. Collectively, these vulnerabilities elevate risk of data breach, ransomware deployment, and supply chain compromise, with potential regulatory and reputational consequences if left unaddressed.

---

## Prioritized Action Items

1. Patch or isolate all Apple devices affected by CVE-2026-86950 immediately, as federal remediation is due by October 2, 2026, and active exploitation is confirmed.
2. Apply available patches for Citrix NetScaler (CVE-2026-88772, CVE-2026-88771) and Microsoft SharePoint (CVE-2026-65660) to address actively exploited KEV-listed vulnerabilities.
3. Isolate or replace all Netcore NR289-GE 1.4.5102 devices, as three CVSS 10.0 vulnerabilities enable unauthenticated remote code execution with no authentication required.
4. Remediate the SailPoint IdentityIQ unauthenticated RCE vulnerability (CVE-2026-12342, CVSS 9.6) by applying vendor patches or restricting network access to the IdentityIQ server.
5. Audit SUSE Rancher Fleet deployments for cross-tenant authorization exposure (CVE-2026-93538) and enforce strict cluster registration controls to prevent privilege escalation across tenants.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-101073 | 8.3 | 2026-09-28 | A security flaw has been discovered in Netcore NR289-GE 1.4.5102. Impacted is an unknown function of the file /bin/boa o |
| CVE-2026-101074 | 9.8 | 2026-09-28 | A weakness has been identified in Netcore NR289-GE 1.4.5102. The affected element is the function password-check of the  |
| CVE-2026-101075 | 10.0 | 2026-09-28 | A security vulnerability has been detected in Netcore NR289-GE 1.4.5102. The impacted element is the function system of  |
| CVE-2026-4556 | 7.8 | 2026-09-28 | Exam4 is affected by a local privilege escalation vulnerability in the com.extegrity.LogTool privileged helper, which co |
| CVE-2026-80357 | 7.0 | 2026-09-28 | Dell Boot Optimized Server Storage (BOSS), versions prior to 2.2.13.2038, contains an On-Chip Debug and Test Interface W |
| CVE-2026-93538 | 7.1 | 2026-09-28 | A cross-tenant authorization issue was discovered in SUSE Rancher Fleet. During agent-initiated cluster registration, cl |
| CVE-2026-101076 | 10.0 | 2026-09-28 | A vulnerability was detected in Netcore NR289-GE 1.4.5102. This affects the function system of the file /set_ntp_server_ |
| CVE-2026-101077 | 10.0 | 2026-09-28 | A flaw has been found in Netcore NR289-GE 1.4.5102. This impacts the function process_request of the component boa_temp  |
| CVE-2026-12342 | 9.6 | 2026-09-28 | This vulnerability
impacts all versions of IdentityIQ and allows an unauthenticated user remote
code execution on the Id |
| CVE-2026-88804 | 9.6 | 2026-09-28 | An unauthenticated update of public UI settings could be used by remote attackers to execute a stored cross-site scripti |
| CVE-2026-88805 | 8.1 | 2026-09-28 | Incorrect credential cleaning on logout could be used by remote attackers to keep access credentials even after the acco |
| CVE-2026-88808 | 8.8 | 2026-09-28 | A vulnerability has been identified within Rancher Manager where the Fleet agent wrote resources to downstream clusters  |
| CVE-2026-93348 | 8.1 | 2026-09-28 | Unsloth Zoo versions 2025.9.9 before 2026.8.14, as implemented in Unsloth 2025.9.9 through 2026.8.19, contains a code in |
| CVE-2026-101081 | 9.1 | 2026-09-28 | A security flaw has been discovered in D-Link DI-8400 16.07. This vulnerability affects the function menu_nat_more_asp o |
| CVE-2026-101894 | 9.1 | 2026-09-28 | The decompress package for Node.js extracts archives. Prior to 10.2.2 and 11.1.4, the default decompress(input, output)  |
| CVE-2026-54160 | 8.2 | 2026-09-28 | Network UPS Tools is a collection of programs which provide a common interface for monitoring and administering UPS, PDU |
| CVE-2026-55096 | 7.1 | 2026-09-28 | fast-mcp-telegram is a Telegram MCP Server. Prior to version 30.1, the send_message/send_message_to_phone MCP tools acce |
| CVE-2026-87114 | 7.1 | 2026-09-28 | A flaw was found in kube-compare. When processing a 'container://' reference path, the tool incorrectly executes an untr |
| CVE-2026-49994 | 9.1 | 2026-09-28 | Bluehood monitors local bluetooth activity. Prior to version 0.7.1, when auth_enabled is set in Bluehood, only the HTML  |
| CVE-2026-55157 | 8.4 | 2026-09-28 | Token Optimizer MCP measures token savings per AI coding agent, optimizes context, and shares a live local knowledge gra |
| CVE-2026-55160 | 7.6 | 2026-09-28 | Stringer is a self-hosted, anti-social RSS reader. Prior to commit 75cb095, an unrestricted Server-Side Request Forgery  |
| CVE-2026-102010 | 7.0 | 2026-09-28 | A flaw was found in GCC. When an application calls the erase_if function on a binary heap priority queue in libstdc++, t |
| CVE-2026-97023 | 7.1 | 2026-09-28 | A path traversal vulnerability in Flatpak's handling of the export/bin directory during app deployment allows a maliciou |
| CVE-2026-102004 | 7.8 | 2026-09-28 | Wind River VxWorks 7 prior to 26.09, specific system call arguments can result in memory corruption within the memory ma |
| CVE-2026-86950 | 8.8 | 2026-09-28 | An out-of-bounds write issue was addressed with improved bounds checking. This issue is fixed in iOS 26.7.1 and iPadOS 2 |
| CVE-2026-87741 | 8.8 | 2026-09-28 | The ConvertPlus plugin for WordPress is vulnerable to Deserialization of Untrusted Data in all versions up to, and inclu |
| CVE-2026-93355 | 8.1 | 2026-09-28 | LiteLLM contains a weak authentication vulnerability that allows an attacker holding a valid JWT from the configured ide |
| CVE-2026-101187 | 9.1 | 2026-09-28 | A weakness has been identified in Ziroom ZHOME A0101 1.0.1.0. This vulnerability affects the function pop_usb_device of  |
| CVE-2026-101916 | 7.4 | 2026-09-28 | @grpc/grpc-js implements the core functionality of gRPC purely in JavaScript, without a C++ addon. Prior to 1.13.6 and 1 |
| CVE-2026-102266 | 7.4 | 2026-09-28 | PyJWT is a Python implementation of JSON Web Token standards. From 2.13.0 until 2.14.0, HMACAlgorithm.from_jwk is affect |
| CVE-2026-102267 | 7.4 | 2026-09-28 | PyJWT is a Python implementation of JSON Web Token standards. Prior to 2.14.0, PyJWT PyJWKClient is affected because red |
| CVE-2026-102268 | 9.1 | 2026-09-28 | PyJWT is a Python implementation of JSON Web Token standards. Prior to 2.14.0, is_pem_format in jwt/utils.py is affected |
| CVE-2026-102271 | 7.4 | 2026-09-28 | PyJWT is a Python implementation of JSON Web Token standards. From 2.4.0 until 2.14.0, PyJWT HMACAlgorithm.prepare_key i |
| CVE-2026-102272 | 7.4 | 2026-09-28 | PyJWT is a Python implementation of JSON Web Token standards. From 2.13.0 until 2.14.0, HMACAlgorithm.prepare_key in jwt |
| CVE-2026-102273 | 7.4 | 2026-09-28 | PyJWT is a Python implementation of JSON Web Token standards. From 2.13.0 until 2.14.0, PyJWT HMACAlgorithm.prepare_key  |
| CVE-2026-102276 | 7.5 | 2026-09-28 | The brace-expansion library generates arbitrary strings containing a common prefix and suffix. Prior to 1.1.19, 2.1.5, 3 |
| CVE-2026-102278 | 7.5 | 2026-09-28 | The brace-expansion library generates arbitrary strings containing a common prefix and suffix. Prior to 1.1.20, 2.1.6, 3 |
| CVE-2026-16513 | 7.8 | 2026-09-28 | The userspace verifier z_vrfy_rtio_sqe_copy_in_get_handles() in subsys/rtio/rtio_syscalls.c (subsys/rtio/rtio_handlers.c |
| CVE-2026-18413 | 7.8 | 2026-09-28 | The ADC API requires each driver to reject a sampling sequence whose destination buffer is too small: the buffer_size fi |
| CVE-2026-18414 | 7.8 | 2026-09-28 | The ADC API requires each driver to reject a sampling sequence whose destination buffer is too small: the buffer_size fi |
| CVE-2024-42002 | 8.4 | 2026-09-28 | A code injection vulnerability has been discovered in the Robot Operating System 2 (ROS 2) 'ros2topic' command-line tool |
| CVE-2026-101091 | 7.1 | 2026-09-28 | SiYuan versions before v3.8.4 fail to properly validate SQL statements in block query embed blocks executed against siyu |
| CVE-2026-101188 | 8.3 | 2026-09-28 | A security vulnerability has been detected in Netcore POWER13 2.0.240730.162638. This issue affects the function routerd |
| CVE-2026-102281 | 7.5 | 2026-09-28 | Nest is a framework for building scalable Node.js server-side applications. Prior to 11.2.4 and 12.0.2, a single message |
| CVE-2026-101260 | 9.1 | 2026-09-28 | A vulnerability was detected in Ziroom ZHOME A0101 1.0.1.0. Affected by this issue is some unknown functionality of the  |
| CVE-2026-101261 | 9.1 | 2026-09-28 | A flaw has been found in Ziroom ZHOME A0101 1.0.1.0. This affects an unknown part of the file /api/ZRnetwork/firstSetup_ |
| CVE-2026-101262 | 9.1 | 2026-09-28 | A vulnerability has been found in Ziroom ZHOME A0101 1.0.1.0. This vulnerability affects unknown code of the file /api/Z |
| CVE-2026-102334 | 7.4 | 2026-09-28 | Nginx Proxy Manager through 2.16.0 lacks rate-limiting on authentication endpoints, allowing unauthenticated attackers t |
| CVE-2026-102335 | 7.1 | 2026-09-28 | Nginx Proxy Manager through 2.16.0 fails to restrict the advanced_config field to administrators, allowing non-admin use |
| CVE-2026-101263 | 9.1 | 2026-09-29 | A vulnerability was found in Ziroom ZHOME A0101 1.0.1.0. This issue affects some unknown processing of the file /api/ZRQ |
| CVE-2026-101264 | 9.1 | 2026-09-29 | A vulnerability was determined in Ziroom ZHOME A0101 1.0.1.0. Impacted is an unknown function of the file /api/ZRnetwork |
| CVE-2026-102361 | 9.1 | 2026-09-29 | mall4j through 4.0 contains a missing authentication vulnerability in the PUT /user/updatePwd endpoint that allows unaut |
| CVE-2026-101280 | 7.3 | 2026-09-29 | A vulnerability was detected in Trusted Domain Project OpenDMARC up to 1.4.2. Affected is the function opendmarc_policy_ |
| CVE-2026-101281 | 7.3 | 2026-09-29 | A flaw has been found in Trusted Domain Project OpenDMARC up to 1.4.2. Affected by this vulnerability is the function op |
| CVE-2026-101354 | 9.6 | 2026-09-29 | A security flaw has been discovered in FAST FAC1203R 20200116_2.0.4. The affected element is the function _tWlanTask of  |
| CVE-2026-101860 | 8.8 | 2026-09-29 | A vulnerability was found in RaspAP raspap-webgui up to 3.5.5. Affected by this issue is the function PluginInstaller::a |
| CVE-2026-101878 | 7.5 | 2026-09-29 | Bitwarden Server 2025.6.0 before 2026.5.0 declares the @ExternalId parameter of the User_ReadBySsoUserOrganizationIdExte |
| CVE-2026-102240 | 10.0 | 2026-09-29 | A vulnerability was found in Netcore NAP930 0.1.241010.141410. This affects the function eval of the file /www/cgi-bin/n |
| CVE-2026-96326 | 7.2 | 2026-09-29 | The HT Contact Form – Drag & Drop Form Builder for WordPress plugin for WordPress is vulnerable to Stored Cross-Site Scr |
| CVE-2026-102243 | 7.4 | 2026-09-29 | A vulnerability was identified in MODSetter SurfSense up to 2.0.3. This issue affects some unknown processing of the fil |
| CVE-2026-102245 | 7.3 | 2026-09-29 | A weakness has been identified in MODSetter SurfSense up to 2.0.3. The affected element is an unknown function of the fi |
| CVE-2026-102248 | 7.3 | 2026-09-29 | A vulnerability was identified in Rebuild up to 4.4.7/4.5.0-beta5. This affects an unknown part of the file /user/login  |
| CVE-2026-102249 | 7.3 | 2026-09-29 | A security flaw has been discovered in REBUILD up to 4.4.11. This vulnerability affects unknown code of the file /common |
| CVE-2026-102422 | 8.1 | 2026-09-29 | shell-quote's `quote()` function emits a `{ comment }` token as `#` followed by its text, which comments out the rest of |
| CVE-2026-97024 | 7.1 | 2026-09-29 | A path traversal vulnerability in Flatpak's handling of the files/etc directory during app deployment allows a malicious |
| CVE-2026-102293 | 7.3 | 2026-09-29 | A vulnerability was identified in realjerrytang tacomall 1.0.0. Impacted is the function OrgStaffServiceImpl.add of the  |
| CVE-2026-86158 | 7.7 | 2026-09-29 | Missing authentication in the local .NET backend (Fiddler.WebUi) of Progress Software Fiddler Everywhere 8.0.2 allows a  |
| CVE-2026-84154 | 9.9 | 2026-09-29 | A Code Injection vulnerability affecting GEOVIA Geospatial Data Manager from Release 3DEXPERIENCE R2024x through Release |
| CVE-2026-76718 | 8.2 | 2026-09-29 | A potential security vulnerability in HPE OneView can be exploited to allow remote session hijacking or other unauthoriz |
| CVE-2026-76719 | 8.2 | 2026-09-29 | A security vulnerability in HPE OneView may be exploited remotely to perform session hijacking, data theft or other unau |
| CVE-2026-84739 | 8.7 | 2026-09-29 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 13.11 before 19.2.7, 19.3 before 19.3.3, and  |
| CVE-2026-8065 | 9.1 | 2026-09-29 | An authentication bypass vulnerability in the firmware update endpoint of Hitachi Energy RTU500 end-of-life versions all |
| CVE-2026-8066 | 9.1 | 2026-09-29 | A directory traversal vulnerability in the file upload functionality of Hitachi Energy RTU500 end-of-life versions allow |
| CVE-2026-95387 | 8.1 | 2026-09-29 | SPDY protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| CVE-2026-95389 | 8.1 | 2026-09-29 | SCTP protocol dissector crash in 4.6.0 to 4.6.8 and 4.4.0 to 4.4.18 allows denial of service |
| CVE-2026-87748 | 8.8 | 2026-09-29 | Missing Authorization vulnerability in Interprobe Information Technologies Inc. Qorela DC allows Privilege Abuse.

This  |
| CVE-2026-95520 | 7.1 | 2026-09-29 | A heap-based buffer overflow flaw was found in rpm. Parsing a symlink entry in an untrusted RPM package whose declared R |
| CVE-2026-100761 | 8.8 | 2026-09-29 | Privilege escalation due to use-after-free in the Graphics: WebGPU component. This vulnerability was fixed in Firefox 15 |
| CVE-2026-100764 | 8.8 | 2026-09-29 | Privilege escalation due to incorrect boundary conditions in the Graphics: WebGPU component. This vulnerability was fixe |
| CVE-2026-100782 | 8.8 | 2026-09-29 | Privilege escalation due to incorrect boundary conditions in the Graphics component. This vulnerability was fixed in Fir |
| CVE-2026-100797 | 8.8 | 2026-09-29 | Privilege escalation due to use-after-free in the Graphics: WebRender component. This vulnerability was fixed in Firefox |
| CVE-2026-100801 | 8.8 | 2026-09-29 | Privilege escalation in the DLL Services component. This vulnerability was fixed in Firefox ESR 153.4, Firefox 157, and  |
| CVE-2026-100807 | 8.8 | 2026-09-29 | Privilege escalation in the DOM: Service Workers component. This vulnerability was fixed in Firefox ESR 153.4, Firefox 1 |
| CVE-2026-100818 | 9.6 | 2026-09-29 | Sandbox escape due to use-after-free in the Widget: Gtk component. This vulnerability was fixed in Firefox ESR 153.4, Fi |
| CVE-2026-100820 | 8.8 | 2026-09-29 | Privilege escalation in the Address Bar component. This vulnerability was fixed in Firefox ESR 153.4, Firefox 157, and F |
| CVE-2026-100824 | 8.8 | 2026-09-29 | Privilege escalation in the Places component. This vulnerability was fixed in Firefox ESR 153.4 and Firefox 157. |
| CVE-2026-100825 | 8.8 | 2026-09-29 | Use-after-free in the JavaScript Engine: JIT component. This vulnerability was fixed in Firefox ESR 153.4 and Firefox 15 |
| CVE-2026-100831 | 8.8 | 2026-09-29 | Use-after-free in the DOM: UI Events & Focus Handling component. This vulnerability was fixed in Firefox ESR 153.4 and F |
| CVE-2026-100832 | 8.8 | 2026-09-29 | Use-after-free in the Graphics: Canvas2D component. This vulnerability was fixed in Firefox ESR 153.4, Firefox ESR 115.4 |
| CVE-2026-102437 | 7.8 | 2026-09-29 | OS Command Injection in internal/gitcmd (git diff filter.clean/smudge invocation) in esengine DeepSeek-Reasonix (Reasoni |
| CVE-2026-73598 | 7.8 | 2026-09-29 | Dell Secure Connect Gateway (SCG) Policy Manager, versions prior to 5.34.00.16, contains an Incorrect Permission Assignm |
| CVE-2026-82973 | 9.4 | 2026-09-29 | Improper neutralization of CRLF sequences in IMAP command construction in psyb0t/docker-mailbox before 0.4.13 allows a r |
| CVE-2026-102360 | 8.6 | 2026-09-29 | A missing bounds check in the binary decoder in lib0, versions 0.2.1-0.2.117 and earlier and 1.0.0-rc.32 and earlier, le |
| CVE-2026-102521 | 8.6 | 2026-09-29 | The decoder in `readFromDataView` in lib0 before 0.2.119 can be tricked into reading more than it should from a buffer.  |
| CVE-2026-86450 | 7.5 | 2026-09-29 | Insertion of sensitive information into sent data vulnerability in Parla Auto Automotive Trading Limited Company DetaWix |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-86950 | Apple / Multiple Products | 2026-09-29 | 2026-10-02 | Unknown |
| CVE-2026-88772 | Citrix / NetScaler | 2026-09-27 | 2026-09-30 | Unknown |
| CVE-2026-88771 | Citrix / NetScaler | 2026-09-27 | 2026-09-30 | Unknown |
| CVE-2026-67279 | MikroTik / RouterOS | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-65660 | Microsoft / SharePoint | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-87902 | WordPress / Core | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-5430 | WSO2 / Multiple Products | 2026-09-24 | 2026-09-27 | Unknown |
| CVE-2026-71362 | Adobe / Commerce and Magento  | 2026-09-24 | 2026-09-27 | Unknown |
| CVE-2026-93952 | Arista / VeloCloud Orchestrator | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-94127 | F5 / BIG-IP APM | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-93616 | Check Point / Multiple Products | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-85102 | Check Point / Multiple Products | 2026-09-22 | 2026-09-25 | Unknown |

---

*Total entries in CISA KEV catalog: 1729*