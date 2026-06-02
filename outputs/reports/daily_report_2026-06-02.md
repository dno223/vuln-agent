# Vulnerability Intelligence Report

**Date:** 2026-06-02  
**Generated:** 2026-06-02T12:04:14Z  

---

## Executive Summary

Our environment faces significant cybersecurity exposure with 116 high-severity vulnerabilities requiring immediate attention. The threat landscape includes critical web application vulnerabilities in rental and job portal systems, network equipment flaws, and infrastructure management tools. Six new CISA Known Exploited Vulnerabilities were added recently, including Oracle WebLogic Server and Palo Alto Networks PAN-OS vulnerabilities. These vulnerabilities present substantial risk through potential unauthorized access, data breaches, and system compromise. The concentration of web application vulnerabilities suggests systemic security gaps in our application portfolio that demand coordinated remediation efforts.

---

## Risk Narrative

The current threat environment presents elevated risk through multiple attack vectors. Web applications represent the primary exposure with numerous SQL injection and authentication bypass vulnerabilities affecting customer-facing systems. Network infrastructure vulnerabilities in H3C equipment and management tools create potential lateral movement opportunities for attackers. The addition of six new CISA KEV entries indicates active exploitation in the wild, requiring urgent attention. Business impact includes potential data breaches, service disruption, regulatory compliance violations, and reputational damage. The high volume of vulnerabilities suggests inadequate security controls in development and deployment processes, necessitating comprehensive security program enhancement.

---

## Prioritized Action Items

1. Immediately patch Oracle WebLogic Server instances affected by CVE-2024-21182 within 48 hours per CISA KEV requirements.
2. Apply emergency patches to all Palo Alto Networks PAN-OS systems for CVE-2026-0257 to prevent network compromise.
3. Conduct security assessment of all itsourcecode Online House Rental System deployments and implement input validation controls.
4. Review and harden all CodeAstro Online Job Portal instances against SQL injection and authentication bypass vulnerabilities.
5. Establish weekly vulnerability monitoring process to track new CISA KEV additions and prioritize remediation accordingly.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-10251 | 7.3 | 2026-06-01 | A weakness has been identified in itsourcecode Online House Rental System 1.0. The impacted element is an unknown functi |
| CVE-2026-10252 | 7.3 | 2026-06-01 | A security vulnerability has been detected in itsourcecode Online House Rental System 1.0. This affects an unknown funct |
| CVE-2026-10253 | 7.3 | 2026-06-01 | A vulnerability was detected in itsourcecode Online House Rental System 1.0. This impacts an unknown function of the fil |
| CVE-2024-40646 | 8.6 | 2026-06-01 | Vertex is a management tool for PT (Private Tracker) users to manage streaming and watching videos. Versions prior to co |
| CVE-2026-10259 | 8.8 | 2026-06-01 | A security vulnerability has been detected in H3C Magic B0 up to 100R002. The affected element is the function SetMobile |
| CVE-2026-10260 | 7.3 | 2026-06-01 | A vulnerability was detected in CodeAstro Online Job Portal 1.0. The impacted element is an unknown function of the file |
| CVE-2026-10261 | 7.3 | 2026-06-01 | A flaw has been found in CodeAstro Online Job Portal 1.0. This affects an unknown function of the file /users/applicatio |
| CVE-2026-10262 | 7.3 | 2026-06-01 | A vulnerability has been found in code-projects Real State Services 1.0. This impacts an unknown function of the file /l |
| CVE-2026-10263 | 7.3 | 2026-06-01 | A vulnerability was found in SourceCodester Computer Repair Shop Management System up to 1.0. Affected is an unknown fun |
| CVE-2026-37220 | 7.5 | 2026-06-01 | FlexRIC v2.0.0 crashes when an SCTP association is closed before an E2_SETUP_REQUEST is sent. The near-RT RIC assumes a  |
| CVE-2026-37221 | 7.5 | 2026-06-01 | FlexRIC v2.0.0 crashes when receiving a RIC_SUBSCRIPTION_RESPONSE with an unknown ric_id that has no corresponding pendi |
| CVE-2026-42680 | 9.8 | 2026-06-01 | Incorrect Privilege Assignment vulnerability in Wasiliy Strecker / ContestGallery developer Contest Gallery Pro allows P |
| CVE-2026-42681 | 7.1 | 2026-06-01 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in E2Pdf.Com e2pdf al |
| CVE-2026-42682 | 9.1 | 2026-06-01 | Missing Authorization vulnerability in Tomdever wpForo Forum allows Exploiting Incorrectly Configured Access Control Sec |
| CVE-2026-42683 | 7.1 | 2026-06-01 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in e4jvikwp VikBookin |
| CVE-2026-48839 | 7.1 | 2026-06-01 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in VeronaLabs WP Stat |
| CVE-2026-48865 | 7.1 | 2026-06-01 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in ThimPress LearnPre |
| CVE-2026-48866 | 9.6 | 2026-06-01 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Rocketgenius Inc. Gravit |
| CVE-2026-48879 | 9.8 | 2026-06-01 | Incorrect Privilege Assignment vulnerability in Sergey AIWU allows Privilege Escalation.

This issue affects AIWU: from  |
| CVE-2026-10118 | 7.8 | 2026-06-01 | A flaw was found in Poppler's Splash backend. A remote attacker could exploit this vulnerability by crafting a malicious |
| CVE-2026-10270 | 8.8 | 2026-06-01 | A vulnerability was detected in D-Link DI-7001 MINI up to 19.09.19A1. Impacted is the function sprintf of the file /http |
| CVE-2026-10273 | 7.3 | 2026-06-01 | A vulnerability was found in php-censor up to 2.1.6. This affects an unknown function of the file src/Model/Build/GitBui |
| CVE-2026-37222 | 7.5 | 2026-06-01 | FlexRIC v2.0.0 uses hardcoded assertions to validate Information Element (IE) counts in decoded E2AP messages. A remote  |
| CVE-2026-37223 | 7.5 | 2026-06-01 | FlexRIC v2.0.0 contains a reachable assertion in the iApp message dispatcher. The dispatcher validates incoming E2AP mes |
| CVE-2026-37224 | 7.5 | 2026-06-01 | FlexRIC v2.0.0 crashes when receiving a duplicate E2_SETUP_REQUEST from the same or spoofed E2 Node. The iApp registry e |
| CVE-2026-37225 | 7.5 | 2026-06-01 | FlexRIC v2.0.0 crashes when the iApp receives an E42_RIC_SUBSCRIPTION_REQUEST with an empty ricEventTriggerDefinition fi |
| CVE-2026-37227 | 7.5 | 2026-06-01 | FlexRIC v2.0.0 contains reachable assert(0) calls in stub message handlers for whitelisted but unimplemented E2AP messag |
| CVE-2026-38950 | 7.8 | 2026-06-01 | An issue in ESA AnomalyMatch before 1.3.1 allow attackers to execute arbitrary code via crafted model checkpoint files.  |
| CVE-2026-42672 | 9.3 | 2026-06-01 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Wp Directory Kit W |
| CVE-2026-42673 | 7.5 | 2026-06-01 | Insertion of Sensitive Information Into Sent Data vulnerability in Logtivity Activity Logs Activity Logs, User Activity  |
| CVE-2026-42674 | 7.5 | 2026-06-01 | Authentication Bypass by Spoofing vulnerability in AAM Plugin Advanced Access Manager allows URL Encoding.

This issue a |
| CVE-2026-42675 | 7.3 | 2026-06-01 | Missing Authorization vulnerability in Themefic Hydra Booking allows Exploiting Incorrectly Configured Access Control Se |
| CVE-2026-42677 | 7.5 | 2026-06-01 | Missing Authorization vulnerability in Ben Balter WP Document Revisions allows Exploiting Incorrectly Configured Access  |
| CVE-2026-42678 | 7.1 | 2026-06-01 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Liquid Web / Stell |
| CVE-2026-44211 | 9.6 | 2026-06-01 | Cline is an autonomous coding agent as an SDK, IDE extension, or CLI assistant. In versions 2.13.0 and prior, there is a |
| CVE-2026-45131 | 10.0 | 2026-06-01 | CloudPirates Open Source Helm Charts is a collection of Helm charts. Prior to commit fcf9302, a GitHub Actions workflow  |
| CVE-2026-45132 | 10.0 | 2026-06-01 | CloudPirates Open Source Helm Charts is a collection of Helm charts. Prior to commit fcf9302, a GitHub Actions workflow  |
| CVE-2026-45156 | 8.1 | 2026-06-01 | Nextcloud is an open source content collaboration platform. From versions 0.3.0 to before 3.1.0, 5.0.0 to before 5.1.0,  |
| CVE-2026-46243 | 7.8 | 2026-06-01 | In the Linux kernel, the following vulnerability has been resolved:

smb: client: reject userspace cifs.spnego descripti |
| CVE-2026-8501 | 7.8 | 2026-06-01 | Improper access control in the PCTCore64.sys Windows kernel driver from PC Tools Internet Security allows user-mode proc |
| CVE-2026-10280 | 7.3 | 2026-06-01 | A security flaw has been discovered in horizon921 mcpilot 0.1.0. The impacted element is an unknown function of the file |
| CVE-2026-10281 | 7.3 | 2026-06-01 | A weakness has been identified in Enderfga claw-orchestrator up to 3.5.5. This affects the function EmbeddedServer of th |
| CVE-2026-41013 | 8.1 | 2026-06-01 | Input validation bypass in SMB volume mount handling in CloudFoundry Foundation diego-release allows low-privileged CF s |
| CVE-2026-43623 | 8.8 | 2026-06-01 | microtar through 0.1.0 contains a stack-based buffer overflow vulnerability in the raw_to_header() function in src/micro |
| CVE-2026-43624 | 8.2 | 2026-06-01 | F5-TTS through version 1.1.20 contains a path traversal vulnerability in the finetune Gradio handlers that allows unauth |
| CVE-2026-43958 | 7.8 | 2026-06-01 | A flaw was found in rrdcached, a component of rrdtool. A local attacker with access to a rrdcached socket can exploit a  |
| CVE-2026-45281 | 8.1 | 2026-06-01 | Nextcloud is an open source content collaboration platform. In Nextcloud Server from versions 32.0.0 to before 32.0.9, a |
| CVE-2026-45302 | 8.2 | 2026-06-01 | parse-nested-form-data is a tiny node module for parsing FormData by name into objects and arrays. Prior to version 1.0. |
| CVE-2026-45545 | 8.2 | 2026-06-01 | Nextcloud is an open source content collaboration platform. From versions 0.7.0 to before 0.7.7, 0.8.0 to before 0.8.10, |
| CVE-2026-45722 | 7.1 | 2026-06-01 | Nextcloud is an open source content collaboration platform. From versions 0.9.0 to before 0.9.7, and 1.0.0 to before 1.0 |
| CVE-2026-47294 | 8.0 | 2026-06-01 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to execute code over a ne |
| CVE-2026-49121 | 8.1 | 2026-06-01 | AI Tensor Engine for ROCm (AITER) through 0.1.14 contains an unauthenticated remote code execution vulnerability in the  |
| CVE-2026-7770 | 8.8 | 2026-06-01 | IBM i Access Family 1.1.5.0 through 1.1.9.12 IBM i Access Client Solutions (ACS) is vulnerable to remote code execution  |
| CVE-2026-8644 | 9.1 | 2026-06-01 | IBM WebSphere Application Server 9.0, and 8.5 is vulnerable to identity spoofing. |
| CVE-2026-9311 | 9.0 | 2026-06-01 | IBM WebSphere Application Server 9.0, and 8.5 is vulnerable to remote code execution caused by the bypass of security co |
| CVE-2026-9319 | 9.0 | 2026-06-01 | IBM WebSphere Application Server 9.0, and 8.5 is vulnerable to potential remote code execution due to deserialization of |
| CVE-2026-9330 | 8.5 | 2026-06-01 | IBM WebSphere Application Server 9.0, and 8.5 is affected by an improper validation of user-supplied data during deseria |
| CVE-2026-9614 | 8.8 | 2026-06-01 | An Improper Access Control vulnerability in Ivanti Neurons for ITSM (cloud and on-premises) allows a remote authenticate |
| CVE-2026-10287 | 7.3 | 2026-06-01 | A vulnerability was determined in SourceCodester SEO Meta Tag Extractor 1.0. This vulnerability affects the function get |
| CVE-2026-10288 | 7.3 | 2026-06-01 | A vulnerability was identified in code-projects Hotel and Tourism Reservation System 1.0. This issue affects the functio |
| CVE-2026-24751 | 8.2 | 2026-06-01 | Kiteworks is a private data network (PDN). Prior to version 9.3.0, a reflected XSS vulnerability in Kiteworks Secure Dat |
| CVE-2026-49134 | 7.1 | 2026-06-01 | CodexBar prior to 0.32.0 contains a privilege escalation vulnerability in the CLI installer that allows local attackers  |
| CVE-2026-49135 | 7.1 | 2026-06-01 | CodexBar prior to 0.32.0 contains an insecure temporary file handling vulnerability that allows local attackers to acces |
| CVE-2026-49136 | 7.5 | 2026-06-01 | Banana Slides through 0.4.0, patched in commit e8bc490, contains a path traversal vulnerability in the generate_image()  |
| CVE-2018-25427 | 9.8 | 2026-06-01 | Arm Whois 3.11 contains a stack-based buffer overflow vulnerability that allows remote attackers to execute arbitrary co |
| CVE-2018-25428 | 8.2 | 2026-06-01 | Paroiciel 11.20 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary SQL q |
| CVE-2018-25429 | 7.1 | 2026-06-01 | Paroiciel 11.20 contains an SQL injection vulnerability that allows authenticated attackers to execute arbitrary SQL que |
| CVE-2018-25430 | 7.1 | 2026-06-01 | Paroiciel 11.20 contains an SQL injection vulnerability that allows authenticated attackers to execute arbitrary SQL que |
| CVE-2018-25431 | 7.1 | 2026-06-01 | No-Cms 1.0 contains an SQL injection vulnerability in the order_by parameter of the manage_privilege export endpoint tha |
| CVE-2018-25432 | 8.4 | 2026-06-01 | Arm Whois 3.11 contains a buffer overflow vulnerability that allows local attackers to execute arbitrary code by overwri |
| CVE-2018-25433 | 8.2 | 2026-06-01 | Joomla Component JE Photo Gallery 1.1 contains an SQL injection vulnerability that allows unauthenticated attackers to e |
| CVE-2018-25434 | 8.2 | 2026-06-01 | WP AutoSuggest 0.24 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary S |
| CVE-2025-48595 | 8.4 | 2026-06-01 | In multiple locations, there is a possible way to achieve code execution due to an integer overflow. This could lead to  |
| CVE-2026-0059 | 8.0 | 2026-06-01 | In multiple functions of sdp_discovery.cc, there is a possible way to achieve code execution due to a heap buffer overfl |
| CVE-2026-0089 | 7.8 | 2026-06-01 | In multiple functions of PackageInstallerService.java, there is a possible way to install unverified apps due to a missi |
| CVE-2026-0091 | 7.8 | 2026-06-01 | In multiple locations, there is a possible way to execute code in the launcher process due to an over-privileged shell u |
| CVE-2026-0093 | 7.8 | 2026-06-01 | In multiple locations, there is a possible misleading UI due to obfuscation. This could lead to local escalation of priv |
| CVE-2026-0094 | 7.8 | 2026-06-01 | In getApplicationLabel of KeyChainActivity.java, there is a possible way to trick the user into approving access to cert |
| CVE-2026-0095 | 8.0 | 2026-06-01 | In l2c_fcr_clone_buf of l2c_fcr.cc, there is a possible way to trigger controlled heap corruption within the privileged  |
| CVE-2026-0096 | 7.8 | 2026-06-01 | In getAppLabel of ForgetDeviceDialogFragment.java, there is a possible trick the user into forgetting a device due to mi |
| CVE-2026-0097 | 8.0 | 2026-06-01 | In multiple locations, there is a possible way to bypass user interaction when pairing an LE device due to a logic error |
| CVE-2026-0098 | 7.8 | 2026-06-01 | In getCallingPackageName of Shared.java, there is a possible way to bypass activity start restrictions due to a confused |
| CVE-2026-0099 | 7.8 | 2026-06-01 | In onNullBinding of HostEmulationManager.java, there is a possible way to launch an activity from the background due to  |
| CVE-2026-0100 | 7.8 | 2026-06-01 | In Load of LoadedArsc.cpp, there is a possible out of bounds write due to a heap buffer overflow. This could lead to loc |
| CVE-2026-10290 | 7.3 | 2026-06-01 | A weakness has been identified in code-projects Hotel and Tourism Reservation System 1.0. The affected element is an unk |
| CVE-2026-10292 | 8.8 | 2026-06-01 | A vulnerability was detected in UTT HiPER 1200GW up to 2.5.3-170306. This affects the function strcpy of the file /gofor |
| CVE-2026-10293 | 8.8 | 2026-06-01 | A flaw has been found in UTT HiPER 1200GW up to 2.5.3-170306. This impacts the function strcpy of the file /goform/formF |
| CVE-2026-28577 | 7.8 | 2026-06-01 | In addWindow of WindowManagerService.java, there is a possible tapjacking issue due to a tapjacking/overlay attack. This |
| CVE-2026-28580 | 7.8 | 2026-06-01 | In multiple functions, there is a possible desync in persistence due to an incorrect bounds check. This could lead to lo |
| CVE-2026-40964 | 7.5 | 2026-06-01 | Authentication Bypass in cf-auth-proxy in Cloud Foundry Foundation all installations allows an unauthenticated remote at |
| CVE-2026-40965 | 10.0 | 2026-06-01 | Cloud Foundry UAA versions v76.12.0 through v78.12.0 are vulnerable to a private key exposure. The server contains a vul |
| CVE-2026-49491 | 8.2 | 2026-06-01 | Pixa Bank 2.0 contains an SQL injection vulnerability that allows unauthenticated attackers to extract sensitive data by |
| CVE-2019-25718 | 8.4 | 2026-06-01 | Dräger Infinity Explorer C700 contains a privilege escalation vulnerability that allows attackers to break out of kiosk  |
| CVE-2025-59604 | 7.8 | 2026-06-01 | Memory Corruption when running a memory copy operation due to invalid writes caused by a null pointer. |
| CVE-2025-59605 | 7.8 | 2026-06-01 | Memory Corruption when processing device identifier strings that exceed the expected maximum length. |
| CVE-2025-59606 | 7.8 | 2026-06-01 | Memory Corruption when writing to invalid memory locations occurs due to heap memory exhaustion during secure data initi |
| CVE-2026-24085 | 7.2 | 2026-06-01 | Memory Corruption when processing display command line information due to improper initialization of a variable. |
| CVE-2026-24087 | 7.2 | 2026-06-01 | Memory corruption while processing fastboot OEM commands. |
| CVE-2026-24088 | 8.2 | 2026-06-01 | Cryptographic Issue while processing a specific partition which allows unauthorized write access to load a customized bo |
| CVE-2026-24089 | 7.2 | 2026-06-01 | Memory corruption while processing fastboot commands with invalid input. |
| CVE-2026-24090 | 7.1 | 2026-06-01 | Cryptographic issue while processing partition table entries allows unauthorized modification of boot flow. |
| CVE-2026-24091 | 7.2 | 2026-06-01 | Memory corruption while processing fastboot commands with improperly formatted input. |
| CVE-2026-24092 | 7.2 | 2026-06-01 | Memory Corruption when processing fastboot commands to set display mode. |
| CVE-2026-24752 | 8.2 | 2026-06-01 | Kiteworks is a private data network (PDN). Prior to version 9.3.0, a reflected XSS vulnerability in Kiteworks Secure Dat |
| CVE-2026-24782 | 7.6 | 2026-06-01 | Kiteworks is a private data network (PDN). Prior to version 9.3.0,ultiple SQL Injection vulnerabilities in Kiteworks Sec |
| CVE-2026-25258 | 7.8 | 2026-06-01 | Memory corruption while processing IOCTL calls for escape operations. |
| CVE-2026-25259 | 7.8 | 2026-06-01 | Memory corruption while processing multiple IOCTL command for escape operations. |
| CVE-2026-25260 | 7.8 | 2026-06-01 | Memory Corruption when accessing shared buffers without validation of concurrent user-mode input modifications. |
| CVE-2026-25276 | 8.8 | 2026-06-01 | Memory corruption while using Strongbox due to missing bounds check. |
| CVE-2026-25277 | 8.8 | 2026-06-01 | Memory corruption while using Strongbox due to buffer overflow. |
| CVE-2026-25879 | 9.8 | 2026-06-01 | Langroid is a framework for building large-language-model-powered applications. Prior to version 0.63.0, SQLChatAgent ex |
| CVE-2026-8206 | 9.8 | 2026-06-02 | The Kirki – Freeform Page Builder, Website Builder & Customizer plugin for WordPress is vulnerable to privilege escalati |
| CVE-2026-1784 | 8.8 | 2026-06-02 | The Route OpenShift resource allows to define routes to make pods reachable at a subdomain through HAProxy. It was found |
| CVE-2026-3514 | 7.5 | 2026-06-02 | In version 3.6.19 of prefecthq/prefect, an authentication bypass vulnerability exists due to the improper handling of UR |
| CVE-2025-52759 | 7.1 | 2026-06-02 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in UnboundStudio Acco |
| CVE-2025-53209 | 9.8 | 2026-06-02 | Incorrect Privilege Assignment vulnerability in Themeisle Masteriyo LMS PRO allows Privilege Escalation.

This issue aff |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2024-21182 | Oracle / WebLogic Server | 2026-06-01 | 2026-06-04 | Unknown |
| CVE-2026-0257 | Palo Alto Networks / PAN-OS | 2026-05-29 | 2026-06-01 | Unknown |
| CVE-2026-48027 | Nx / Nx Console | 2026-05-27 | 2026-06-10 | Known |
| CVE-2026-45321 | TanStack / TanStack | 2026-05-27 | 2026-06-10 | Known |
| CVE-2026-8398 | Daemon / Daemon Tools Lite | 2026-05-27 | 2026-05-30 | Unknown |
| CVE-2026-48172 | LiteSpeed / cPanel Plugin | 2026-05-26 | 2026-05-29 | Unknown |

---

*Total entries in CISA KEV catalog: 1608*