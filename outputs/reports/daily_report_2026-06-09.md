# Vulnerability Intelligence Report

**Date:** 2026-06-09  
**Generated:** 2026-06-09T11:14:06Z  

---

## Executive Summary

Our organization faces significant cybersecurity exposure with 107 high-severity vulnerabilities identified, including critical CVSS 9.3 rated flaws. A Check Point Security Gateway vulnerability (CVE-2026-50751) has been added to CISA's Known Exploited Vulnerabilities catalog with a June 11 remediation deadline, indicating active exploitation. The vulnerability landscape shows heavy concentration in network infrastructure devices from vendors like Tenda, UTT, and Check Point, with authentication bypass and buffer overflow vulnerabilities predominating. Immediate action is required to prevent potential network compromise and data breaches.

---

## Risk Narrative

The threat landscape reveals active targeting of network infrastructure with government-mandated patching deadlines indicating real-world exploitation. Authentication bypass vulnerabilities in security gateways pose severe risks of network perimeter compromise. Buffer overflow vulnerabilities in widely-deployed network devices create pathways for remote code execution and lateral movement. The concentration of high-CVSS vulnerabilities in network infrastructure suggests coordinated efforts to exploit foundational network security controls. Business operations face disruption risk from potential network outages and compliance violations if CISA deadlines are missed.

---

## Prioritized Action Items

1. Patch CVE-2026-50751 in all Check Point Security Gateways before June 11, 2026 CISA deadline.
2. Conduct emergency security assessment of all Tenda network devices for multiple buffer overflow vulnerabilities.
3. Implement network segmentation to isolate vulnerable infrastructure devices from critical systems.
4. Deploy additional monitoring for authentication bypass attempts on network appliances.
5. Schedule immediate firmware updates for UTT HiPER and other affected network equipment.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-11504 | 8.8 | 2026-06-08 | A vulnerability was detected in Tenda CX12L 16.03.53.12. The impacted element is the function setSchedWifi of the file / |
| CVE-2026-50751 | 9.3 | 2026-06-08 | A logic flow weakness in Remote Access and Mobile Access certificate validation in deprecated IKEv1 key exchange allows  |
| CVE-2026-50752 | 7.4 | 2026-06-08 | A weakness in the certificate validation logic of the deprecated IKEv1 key exchange may allow an unauthenticated attacke |
| CVE-2026-11577 | 7.2 | 2026-06-08 | A flaw was found in Keycloak. A limited administrator can exploit an improper access control vulnerability in the POST / |
| CVE-2026-11517 | 8.8 | 2026-06-08 | A vulnerability was determined in UTT HiPER 2610G up to 3.0.0-171107. This impacts the function strcpy of the file /gofo |
| CVE-2026-36789 | 7.5 | 2026-06-08 | Shenzhen Tenda Technology Co., Ltd Tenda AC1206 v15.03.06.23 was discovered to contain multiple stack overflows in the f |
| CVE-2026-11522 | 8.8 | 2026-06-08 | A vulnerability was detected in Tenda W20E 15.11.0.6. This vulnerability affects the function formSetPortMirror of the f |
| CVE-2026-11523 | 8.8 | 2026-06-08 | A flaw has been found in Tenda W20E 15.11.0.6. This issue affects the function formPortalAuth of the file /goform/Portal |
| CVE-2026-11524 | 8.8 | 2026-06-08 | A vulnerability has been found in Tenda W20E 15.11.0.6. Impacted is the function modifyWifiFilterRules of the file /gofo |
| CVE-2026-11528 | 8.8 | 2026-06-08 | A vulnerability was found in Tenda AC18 15.03.05.05. The affected element is the function sub_45304 of the file /goform/ |
| CVE-2026-22164 | 7.5 | 2026-06-08 | Software installed and run as a non-privileged user may conduct improper GPU system calls to corrupt kernel heap memory. |
| CVE-2026-34194 | 7.1 | 2026-06-08 | Software installed and run as a non-privileged user may conduct improper GPU system calls to cause mismanagement of a ma |
| CVE-2026-34355 | 7.5 | 2026-06-08 | A buffer overflow in mod_proxy_html in Apache HTTP Server 2.4.67 and earlier allows an attack by an untrusted backend.
U |
| CVE-2026-34356 | 7.5 | 2026-06-08 | Heap-based Buffer Overflow vulnerability in Apache HTTP Server with malicious backend servers and ProxyPassReverseCookie |
| CVE-2026-36786 | 7.5 | 2026-06-08 | Shenzhen Tenda Technology Co., Ltd Tenda FH451 V1.0.0.9 was discovered to contain a stack overflow in the list1 paramete |
| CVE-2026-42536 | 7.5 | 2026-06-08 | Heap-based Buffer Overflow vulnerability in Apache HTTP Server with mod_xml2enc, xml2StartParse, and untrusted content

 |
| CVE-2026-44185 | 7.3 | 2026-06-08 | Buffer Over-read vulnerability in Apache HTTP Server via outbound OCSP requests to an attacker controlled OCSP server

T |
| CVE-2026-44631 | 9.8 | 2026-06-08 | Buffer Underwrite vulnerability in Apache HTTP Server on crafted regular expressions in the configuration.

This issue a |
| CVE-2026-46440 | 7.5 | 2026-06-08 | Flowise is a drag & drop user interface to build a customized large language model flow. Prior to version 3.1.2, the che |
| CVE-2026-46656 | 8.8 | 2026-06-08 | Bludit is a content management system. Versions prior to 3.22.0 have a Broken Access Control flaw where active sessions  |
| CVE-2026-46657 | 7.1 | 2026-06-08 | Bludit is a content management system. Versions prior to 3.22.0 have a vulnerability in the user management logic that a |
| CVE-2026-48913 | 7.3 | 2026-06-08 | Use After Free vulnerability in Apache HTTP Server module mod_http2 when file handles are already exhausted.

This issue |
| CVE-2026-11530 | 7.3 | 2026-06-08 | A vulnerability was identified in imvks786 student_management_system up to 9599b560ad3c3b83e75d328b76bedcd489ef1f46. Thi |
| CVE-2026-11531 | 7.3 | 2026-06-08 | A security flaw has been discovered in imvks786 student_management_system up to 9599b560ad3c3b83e75d328b76bedcd489ef1f46 |
| CVE-2026-25555 | 9.8 | 2026-06-08 | OpenBullet2 through version 0.3.2 contains an authentication bypass vulnerability in the API key authentication middlewa |
| CVE-2026-25559 | 8.8 | 2026-06-08 | OpenBullet2 through version 0.3.2 contains a path traversal vulnerability in the wordlist endpoint that allows authentic |
| CVE-2026-25855 | 8.8 | 2026-06-08 | OpenBullet2 through version 0.3.2 contains a remote code execution vulnerability that allows authenticated users to exec |
| CVE-2026-25856 | 8.8 | 2026-06-08 | OpenBullet2 through version 0.3.2 contains an authenticated remote code execution vulnerability that allows authenticate |
| CVE-2026-39910 | 9.8 | 2026-06-08 | STACKIT IaaS API contains a missing authorization check vulnerability that allows authenticated, low-privileged attacker |
| CVE-2026-41448 | 9.4 | 2026-06-08 | AdGuard Home, when started with the --glinet flag, contains an authentication bypass vulnerability that allows unauthent |
| CVE-2026-46481 | 8.3 | 2026-06-08 | OpenMetadata is a unified metadata platform. Prior to version 1.12.4, a non-admin SSO user can trigger a TEST_CONNECTION |
| CVE-2026-48507 | 7.1 | 2026-06-08 | Snipe-IT is an IT asset/license management system. A vulnerability in versions prior to 8.6.0 allows a non-admin user ho |
| CVE-2026-11553 | 8.8 | 2026-06-08 | A vulnerability was found in Tenda HG7HG9 and HG10 300001138_en_xpon. This affects the function formPPPEdit of the file  |
| CVE-2026-11556 | 8.8 | 2026-06-08 | A security flaw has been discovered in Tenda F451 1.0.0.7/1.0.0.9. Impacted is the function formWriteFacMac of the file  |
| CVE-2026-11393 | 9.0 | 2026-06-08 | Improper neutralization of triple-quote characters during Python code generation in AgentCore CLI before v0.14.2 might a |
| CVE-2026-11557 | 8.8 | 2026-06-08 | A weakness has been identified in Tenda F451 1.0.0.7/1.0.0.9. The affected element is the function fromNatlimit of the f |
| CVE-2026-52778 | 9.8 | 2026-06-08 | YesWiki is a wiki system written in PHP. Prior to version 4.6.6, an unsafe execution vulnerability exists in the Bazar f |
| CVE-2026-11582 | 7.3 | 2026-06-08 | A flaw has been found in CodeAstro Student Attendance Management System 1.0. The impacted element is an unknown function |
| CVE-2026-40519 | 7.5 | 2026-06-08 | Nginx Proxy Manager versions 2.9.14 through 2.15.1, fixed in commit a5db5ed, contain an authenticated remote code execut |
| CVE-2026-46484 | 8.1 | 2026-06-08 | Headplane is a feature-complete Web UI for Headscale. Prior to versions 0.6.3 and 0.7.0-beta.3, Headplane was vulnerable |
| CVE-2026-49141 | 7.1 | 2026-06-08 | WACRM prior to commit 73041bf contain an authorization bypass vulnerability in the automation engine that allows authent |
| CVE-2026-11632 | 7.5 | 2026-06-09 | Use after free in TabStrip in Google Chrome prior to 149.0.7827.103 allowed a remote attacker who convinced a user to en |
| CVE-2026-11633 | 8.8 | 2026-06-09 | Use after free in Bluetooth in Google Chrome on Mac prior to 149.0.7827.103 allowed a remote attacker to execute arbitra |
| CVE-2026-11634 | 9.6 | 2026-06-09 | Use after free in Gamepad in Google Chrome on Windows prior to 149.0.7827.103 allowed a remote attacker to potentially p |
| CVE-2026-11635 | 8.3 | 2026-06-09 | Use after free in Bluetooth in Google Chrome on Mac prior to 149.0.7827.103 allowed a remote attacker who had compromise |
| CVE-2026-11637 | 8.8 | 2026-06-09 | Use after free in Views in Google Chrome on Mac prior to 149.0.7827.103 allowed a remote attacker to execute arbitrary c |
| CVE-2026-11638 | 9.6 | 2026-06-09 | Use after free in Printing in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to potentially perform a s |
| CVE-2026-11639 | 7.5 | 2026-06-09 | Use after free in Compositing in Google Chrome on Mac prior to 149.0.7827.103 allowed a remote attacker to execute arbit |
| CVE-2026-11641 | 7.5 | 2026-06-09 | Use after free in Bluetooth in Google Chrome on Windows prior to 149.0.7827.103 allowed a remote attacker who convinced  |
| CVE-2026-11642 | 8.3 | 2026-06-09 | Use after free in Web Apps in Google Chrome prior to 149.0.7827.103 allowed a remote attacker who had compromised the re |
| CVE-2026-11643 | 8.1 | 2026-06-09 | Use after free in Proxy in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to execute arbitrary code via |
| CVE-2026-11644 | 7.5 | 2026-06-09 | Use after free in Views in Google Chrome on Linux prior to 149.0.7827.103 allowed an attacker who convinced a user to in |
| CVE-2026-11645 | 8.8 | 2026-06-09 | Out of bounds read and write in V8 in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to execute arbitra |
| CVE-2026-11646 | 8.8 | 2026-06-09 | Use after free in ViewTransitions in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to execute arbitrar |
| CVE-2026-11647 | 8.3 | 2026-06-09 | Use after free in Printing in Google Chrome on Android prior to 149.0.7827.103 allowed a remote attacker who had comprom |
| CVE-2026-11649 | 8.8 | 2026-06-09 | Use after free in V8 in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-11650 | 8.8 | 2026-06-09 | Use after free in V8 in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-11651 | 9.6 | 2026-06-09 | Use after free in Network in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to execute arbitrary code i |
| CVE-2026-11652 | 8.3 | 2026-06-09 | Use after free in Extensions in Google Chrome prior to 149.0.7827.103 allowed a remote attacker who had compromised the  |
| CVE-2026-11656 | 8.3 | 2026-06-09 | Use after free in ServiceWorker in Google Chrome prior to 149.0.7827.103 allowed an attacker who convinced a user to ins |
| CVE-2026-11657 | 8.8 | 2026-06-09 | Use after free in Payments in Google Chrome on Mac prior to 149.0.7827.103 allowed a remote attacker to execute arbitrar |
| CVE-2026-11662 | 8.8 | 2026-06-09 | Type Confusion in Bindings in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to execute arbitrary code  |
| CVE-2026-11663 | 8.3 | 2026-06-09 | Use after free in Skia in Google Chrome prior to 149.0.7827.103 allowed a remote attacker who had compromised the render |
| CVE-2026-11670 | 8.8 | 2026-06-09 | Use after free in PDF in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to execute arbitrary code insid |
| CVE-2026-11671 | 9.6 | 2026-06-09 | Use after free in Navigation in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to potentially perform a |
| CVE-2026-11673 | 8.8 | 2026-06-09 | Use after free in InterestGroups in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to execute arbitrary |
| CVE-2026-11674 | 8.8 | 2026-06-09 | Use after free in Guest View in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to execute arbitrary cod |
| CVE-2026-11679 | 8.3 | 2026-06-09 | Use after free in Codecs in Google Chrome on Windows prior to 149.0.7827.103 allowed a remote attacker who had compromis |
| CVE-2026-11680 | 8.8 | 2026-06-09 | Use after free in Media in Google Chrome on Windows prior to 149.0.7827.103 allowed a remote attacker to execute arbitra |
| CVE-2026-11683 | 8.8 | 2026-06-09 | Use after free in WebCodecs in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to execute arbitrary code |
| CVE-2026-11687 | 8.8 | 2026-06-09 | Use after free in Dawn in Google Chrome on Mac prior to 149.0.7827.103 allowed a remote attacker to potentially exploit  |
| CVE-2026-11688 | 8.8 | 2026-06-09 | Inappropriate implementation in SVG in Google Chrome prior to 149.0.7827.103 allowed a remote attacker to execute arbitr |
| CVE-2026-11690 | 7.5 | 2026-06-09 | Out of bounds read and write in Media in Google Chrome on Mac prior to 149.0.7827.103 allowed a remote attacker who had  |
| CVE-2026-11692 | 8.3 | 2026-06-09 | Use after free in Read Anything in Google Chrome prior to 149.0.7827.103 allowed a remote attacker who had compromised t |
| CVE-2026-11694 | 7.5 | 2026-06-09 | Use after free in ServiceWorker in Google Chrome prior to 149.0.7827.103 allowed a remote attacker who had compromised t |
| CVE-2026-11698 | 8.8 | 2026-06-09 | Use after free in Bluetooth in Google Chrome on Mac prior to 149.0.7827.103 allowed a remote attacker to potentially exp |
| CVE-2026-11699 | 8.8 | 2026-06-09 | Use after free in Bluetooth in Google Chrome on Mac prior to 149.0.7827.103 allowed a remote attacker to potentially exp |
| CVE-2026-11700 | 8.3 | 2026-06-09 | Use after free in Tracing in Google Chrome prior to 149.0.7827.103 allowed a remote attacker who had compromised the ren |
| CVE-2026-27671 | 9.8 | 2026-06-09 | Due to improper RFC protocol validation in the SAP Kernel used by the Application Server ABAP of SAP NetWeaver and ABAP  |
| CVE-2026-40128 | 9.0 | 2026-06-09 | SAP NetWeaver Application Server Java (Web Container) allows an unauthenticated attacker to craft a malicious HTTP logon |
| CVE-2026-44748 | 9.9 | 2026-06-09 | SAP NetWeaver Application Server ABAP and ABAP Platform allows an authenticated attacker with normal privileges to obtai |
| CVE-2026-44751 | 7.1 | 2026-06-09 | Application server ABAP does not perform necessary authorization checks for an authenticated user allowing an attacker t |
| CVE-2026-8795 | 7.8 | 2026-06-09 | A YAML injection vulnerability exists in the Windows.Collectors.Remapping artifact of Rapid7 Velociraptor before version |
| CVE-2026-11618 | 7.3 | 2026-06-09 | A vulnerability was determined in DTStack Taier up to 1.4.0. The affected element is the function preHandle of the file  |
| CVE-2026-7556 | 7.2 | 2026-06-09 | The FV Flowplayer Video Player plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the comment text in |
| CVE-2026-40983 | 7.5 | 2026-06-09 | In Micrometer, it is possible for a user to provide specially crafted gRPC requests that may cause a denial-of-service ( |
| CVE-2026-40984 | 7.5 | 2026-06-09 | In Micrometer, it is possible for a user to provide specially crafted HTTP requests that may cause a denial-of-service ( |
| CVE-2026-41006 | 7.5 | 2026-06-09 | Spring HATEOAS's internal PropertyUtils.createObjectFromProperties method, used by the Collection+JSON and UBER media ty |
| CVE-2026-41007 | 7.5 | 2026-06-09 | Spring HATEOAS maintains an unbounded static cache of StringLinkRelation instances keyed on attacker-supplied strings.

 |
| CVE-2026-41720 | 7.4 | 2026-06-09 | Spring LDAP's DirContextAuthenticationStrategy implementations do not reject a bind request where a non-empty username i |
| CVE-2026-41842 | 7.5 | 2026-06-09 | Spring MVC and WebFlux applications are vulnerable to Denial of Service (DoS) attacks when resolving static resources.

 |
| CVE-2026-41845 | 7.1 | 2026-06-09 | Due to incorrect escaping, the use of JavaScriptUtils.javaScriptEscape() may lead to JavaScript code injection in the br |
| CVE-2026-41849 | 7.5 | 2026-06-09 | An integer overflow vulnerability exists in the evaluation logic of the Spring Expression Language (SpEL). An attacker c |
| CVE-2026-41850 | 7.5 | 2026-06-09 | Applications that evaluate user-supplied Spring Expression Language (SpEL) expressions are vulnerable to an Algorithmic  |
| CVE-2026-41855 | 8.1 | 2026-06-09 | In an untrusted JMS environment, org.springframework.jms.support.converter.MappingJackson2MessageConverter and org.sprin |
| CVE-2026-9185 | 7.5 | 2026-06-09 | The 6Storage Rentals plugin for WordPress is vulnerable to Authorization Bypass Through User-Controlled Key in all versi |
| CVE-2026-9662 | 8.1 | 2026-06-09 | The Recover Exit For WooCommerce plugin for WordPress is vulnerable to Local File Inclusion in all versions up to and in |
| CVE-2026-11572 | 8.8 | 2026-06-09 | Versions of the package degit before 2.8.6, from 3.0.0 and before 3.3.1 are vulnerable to Command Injection due to impro |
| CVE-2026-5067 | 9.8 | 2026-06-09 | A remote, unauthenticated attacker can trigger memory corruption in Zephyr's HTTP server WebSocket upgrade path by sendi |
| CVE-2026-5068 | 7.6 | 2026-06-09 | A remote, unauthenticated BLE peer can trigger a 2-byte out-of-bounds write in the Bluetooth host during L2CAP LE CoC SD |
| CVE-2026-11616 | 8.8 | 2026-06-09 | The Events Calendar for GeoDirectory plugin for WordPress is vulnerable to Privilege Escalation in versions up to and in |
| CVE-2026-8365 | 8.8 | 2026-06-09 | The Blocksy theme for WordPress is vulnerable to PHP Object Injection leading to Remote Code Execution via the 'blocksy_ |
| CVE-2026-24349 | 7.1 | 2026-06-09 | A vulnerability has been identified in SIMATIC WinCC Unified PC Runtime V16 (All versions), SIMATIC WinCC Unified PC Run |
| CVE-2026-41031 | 8.7 | 2026-06-09 | A Stored Cross-Site Scripting vulnerability in Vinna Process Monitor Version 4.0 Service Pack 1 (Build 63255) allows an  |
| CVE-2026-46746 | 8.8 | 2026-06-09 | A vulnerability has been identified in SINEC INS (All versions < V1.0 SP2 Update 6). The application does not properly s |
| CVE-2026-46748 | 8.8 | 2026-06-09 | A vulnerability has been identified in SINEC INS (All versions < V1.0 SP2 Update 6). The affected system includes a bina |
| CVE-2026-46749 | 7.5 | 2026-06-09 | A vulnerability has been identified in SINEC INS (All versions < V1.0 SP2 Update 6). The affected application uses a pas |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-42271 | BerriAI / LiteLLM | 2026-06-08 | 2026-06-22 | Unknown |
| CVE-2026-50751 | Check Point / Security Gateway | 2026-06-08 | 2026-06-11 | Unknown |
| CVE-2026-28318 | SolarWinds / Serv-U | 2026-06-05 | 2026-06-19 | Unknown |
| CVE-2026-45247 | Mirasvit / Mirasvit Full Page Cache Warmer | 2026-06-03 | 2026-06-06 | Unknown |
| CVE-2022-0492 | Linux / Kernel | 2026-06-02 | 2026-06-05 | Unknown |
| CVE-2025-48595 | Android / Framework | 2026-06-02 | 2026-06-05 | Unknown |

---

*Total entries in CISA KEV catalog: 1614*