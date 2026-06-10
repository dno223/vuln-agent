# Vulnerability Intelligence Report

**Date:** 2026-06-10  
**Generated:** 2026-06-10T11:38:21Z  

---

## Executive Summary

Our environment faces significant risk from 289 high-severity vulnerabilities, primarily affecting WordPress plugins with SQL injection flaws that allow unauthenticated attackers to access sensitive database information. Seven critical vulnerabilities were added to CISA's Known Exploited Vulnerabilities catalog this week, including flaws in Google Chromium, Cisco SD-WAN, and Check Point security systems. These represent active threats being exploited in the wild. The concentration of WordPress plugin vulnerabilities indicates poor security practices in web application management, while the new CISA KEV entries signal emerging threats across our technology stack.

---

## Risk Narrative

The threat landscape shows attackers increasingly targeting web applications and network infrastructure. WordPress plugin vulnerabilities dominate our high-severity findings, creating pathways for data theft and system compromise through SQL injection attacks. The recent CISA KEV additions indicate sophisticated threat actors are rapidly weaponizing vulnerabilities in critical infrastructure components including browsers, network management systems, and security appliances. Our organization faces elevated risk of data breaches, service disruptions, and lateral network movement if these vulnerabilities remain unaddressed. Immediate remediation is essential to prevent exploitation.

---

## Prioritized Action Items

1. Immediately patch or disable all affected WordPress plugins, prioritizing those with CVSS scores above 8.0 that allow unauthenticated SQL injection attacks.
2. Apply security updates for Google Chromium V8 engine across all browser deployments to address CVE-2026-11645.
3. Update Cisco Catalyst SD-WAN Manager systems to address CVE-2026-20245 and prevent potential network compromise.
4. Review and harden Check Point Security Gateway configurations while applying patches for CVE-2026-50751.
5. Conduct comprehensive vulnerability assessment of all WordPress installations and implement web application firewall rules.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2016-20062 | 8.2 | 2026-06-09 | Simply Poll 1.4.1 plugin for WordPress contains an SQL injection vulnerability that allows unauthenticated attackers to  |
| CVE-2016-20063 | 7.1 | 2026-06-09 | Single Personal Message 1.0.3 contains an SQL injection vulnerability that allows authenticated users to execute arbitra |
| CVE-2016-20065 | 8.2 | 2026-06-09 | Product Catalog 8 1.2 plugin for WordPress contains an SQL injection vulnerability that allows unauthenticated attackers |
| CVE-2017-20243 | 8.2 | 2026-06-09 | WordPress Car Park Booking Plugin version 13 October 17 contains a time-based SQL injection vulnerability that allows un |
| CVE-2017-20244 | 8.2 | 2026-06-09 | Wow Forms WordPress Plugin version 2.1 contains an SQL injection vulnerability that allows unauthenticated attackers to  |
| CVE-2017-20245 | 8.2 | 2026-06-09 | Wow Viral Signups 2.1 WordPress plugin contains an SQL injection vulnerability that allows unauthenticated attackers to  |
| CVE-2017-20246 | 8.2 | 2026-06-09 | KittyCatfish 2.2 plugin for WordPress contains an SQL injection vulnerability that allows unauthenticated attackers to r |
| CVE-2017-20247 | 8.2 | 2026-06-09 | WordPress Plugin PICA Photo Gallery 1.0 contains an SQL injection vulnerability that allows unauthenticated attackers to |
| CVE-2017-20248 | 7.5 | 2026-06-09 | Apptha Slider Gallery 1.0 contains a path traversal vulnerability that allows unauthenticated attackers to download arbi |
| CVE-2017-20249 | 8.2 | 2026-06-09 | Apptha Slider Gallery 1.0 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbit |
| CVE-2017-20250 | 7.5 | 2026-06-09 | Mac Photo Gallery 3.0 contains a path traversal vulnerability that allows unauthenticated attackers to download arbitrar |
| CVE-2017-20251 | 9.8 | 2026-06-09 | WordPress Insert PHP plugin versions before 3.3.1 contain a PHP code injection vulnerability that allows unauthenticated |
| CVE-2026-7486 | 9.8 | 2026-06-09 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Netcad Software In |
| CVE-2026-10520 | 10.0 | 2026-06-09 | An OS Command Injection vulnerability in Ivanti Sentry before the R10.5.2, R10.6.2 and R10.7.1 versions allows a remote  |
| CVE-2026-10523 | 9.9 | 2026-06-09 | An Authentication Bypass vulnerability (CWE-288) in Ivanti Sentry before the R10.5.2, R10.6.2 and R10.7.1 versions allow |
| CVE-2026-10727 | 7.2 | 2026-06-09 | An OS command injection vulnerability in Ivanti EPMM before 12.9.0.1, 12.8.0.3 and 12.7.0.2 versions allows a remote aut |
| CVE-2026-24065 | 8.1 | 2026-06-09 | Waves Central for macOS versions 13.0.9 through 16.5.5 contain a local privilege escalation vulnerability in the privile |
| CVE-2026-25089 | 9.8 | 2026-06-09 | A improper neutralization of special elements used in an os command ('os command injection') vulnerability in Fortinet F |
| CVE-2026-49948 | 8.1 | 2026-06-09 | Mem0 versions through 0.2.8, fixed in commit ae7f406, contain a missing authorization vulnerability in the self-hosted s |
| CVE-2026-8025 | 9.8 | 2026-06-09 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in MOSK Information T |
| CVE-2026-22926 | 7.8 | 2026-06-09 | Omnissa Workspace ONE® Assist for macOS contains a Local Privilege Escalation   Vulnerability. |
| CVE-2026-24180 | 7.3 | 2026-06-09 | NVIDIA DALI contains a vulnerability in a component where an attacker could cause a heap-based buffer overflow. A succes |
| CVE-2026-24181 | 7.3 | 2026-06-09 | NVIDIA DALI contains a vulnerability in a component where an attacker could cause an improper index validation. A succes |
| CVE-2026-26142 | 9.8 | 2026-06-09 | Deserialization of untrusted data in Nuance PowerScribe allows an unauthorized attacker to execute code over a network. |
| CVE-2026-32193 | 8.8 | 2026-06-09 | Improper limitation of a pathname to a restricted directory ('path traversal') in Microsoft Azure Kubernetes Service all |
| CVE-2026-33828 | 7.8 | 2026-06-09 | Trust boundary violation in Windows Attestation allows an authorized attacker to elevate privileges locally. |
| CVE-2026-34180 | 7.5 | 2026-06-09 | Issue summary: Parsing a crafted DER-encoded ASN.1 structure with a primitive
element whose content exceeds 2 gigabytes  |
| CVE-2026-34335 | 7.0 | 2026-06-09 | Use after free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges loca |
| CVE-2026-40371 | 8.8 | 2026-06-09 | Improper handling of insufficient permissions or privileges in Microsoft Dynamics 365 (on-premises) allows an authorized |
| CVE-2026-40376 | 7.5 | 2026-06-09 | Improper input validation in Visual Studio Code allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-40404 | 7.8 | 2026-06-09 | Windows Universal Disk Format File System Driver (UDFS) Elevation of Privilege Vulnerability |
| CVE-2026-40409 | 7.8 | 2026-06-09 | Windows Universal Disk Format File System Driver (UDFS) Elevation of Privilege Vulnerability |
| CVE-2026-41092 | 7.8 | 2026-06-09 | Improper access control in Microsoft Kinect allows an authorized attacker to elevate privileges locally. |
| CVE-2026-41098 | 8.4 | 2026-06-09 | Improper neutralization of input during web page generation ('cross-site scripting') in Azure Stack Edge allows an autho |
| CVE-2026-41108 | 7.0 | 2026-06-09 | Heap-based buffer overflow in Microsoft Windows DNS allows an authorized attacker to elevate privileges locally. |
| CVE-2026-42570 | 7.5 | 2026-06-09 | Svelte devalue is a JavaScript library that serializes values into strings when JSON.stringify isn't sufficient for the  |
| CVE-2026-42764 | 7.5 | 2026-06-09 | Issue summary: Receiving a QUIC initial packet with an invalid token may
trigger a NULL pointer dereference in the OpenS |
| CVE-2026-42765 | 7.5 | 2026-06-09 | Issue summary: When a partial-chain certificate verification is enabled
together with OCSP response checking for the who |
| CVE-2026-42828 | 7.8 | 2026-06-09 | Buffer over-read in Windows Projected File System Filter Driver allows an authorized attacker to elevate privileges loca |
| CVE-2026-42829 | 7.8 | 2026-06-09 | Improper access control in Windows Administrator Protection allows an authorized attacker to bypass a security feature l |
| CVE-2026-42835 | 8.1 | 2026-06-09 | Improper neutralization of special elements in output used by a downstream component ('injection') in Microsoft Teams fo |
| CVE-2026-42836 | 7.0 | 2026-06-09 | Concurrent execution using shared resource with improper synchronization ('race condition') in Function Discovery Servic |
| CVE-2026-42837 | 7.8 | 2026-06-09 | Buffer over-read in Windows Projected File System Filter Driver allows an authorized attacker to elevate privileges loca |
| CVE-2026-42902 | 7.8 | 2026-06-09 | Improper authorization in Microsoft PowerToys allows an authorized attacker to elevate privileges locally. |
| CVE-2026-42904 | 9.6 | 2026-06-09 | Heap-based buffer overflow in Windows TCP/IP allows an unauthorized attacker to elevate privileges over an adjacent netw |
| CVE-2026-42905 | 7.8 | 2026-06-09 | Use after free in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-42908 | 7.5 | 2026-06-09 | Out-of-bounds read in Windows RDP allows an unauthorized attacker to disclose information over a network. |
| CVE-2026-42909 | 7.5 | 2026-06-09 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-42910 | 7.8 | 2026-06-09 | Out-of-bounds write in Windows Hotpatch Monitoring Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-42911 | 7.0 | 2026-06-09 | Use after free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges loca |
| CVE-2026-42912 | 7.0 | 2026-06-09 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Telephony Service |
| CVE-2026-42913 | 7.5 | 2026-06-09 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-42916 | 7.8 | 2026-06-09 | Integer underflow (wrap or wraparound) in Windows NT OS Kernel allows an authorized attacker to elevate privileges local |
| CVE-2026-42974 | 8.1 | 2026-06-09 | Integer underflow (wrap or wraparound) in Windows Performance Monitor allows an unauthorized attacker to execute code ov |
| CVE-2026-42977 | 7.8 | 2026-06-09 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Push Notification |
| CVE-2026-42978 | 7.8 | 2026-06-09 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Push Notification |
| CVE-2026-42979 | 7.8 | 2026-06-09 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Push Notification |
| CVE-2026-42980 | 7.8 | 2026-06-09 | Integer underflow (wrap or wraparound) in Windows NT OS Kernel allows an authorized attacker to elevate privileges local |
| CVE-2026-42981 | 8.1 | 2026-06-09 | Integer underflow (wrap or wraparound) in Windows Performance Monitor allows an unauthorized attacker to execute code ov |
| CVE-2026-42983 | 7.8 | 2026-06-09 | Use after free in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-42984 | 7.0 | 2026-06-09 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-42985 | 8.8 | 2026-06-09 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-42986 | 7.8 | 2026-06-09 | Use after free in Microsoft Graphics Component allows an authorized attacker to elevate privileges locally. |
| CVE-2026-42987 | 8.1 | 2026-06-09 | Use after free in Windows Deployment Services allows an unauthorized attacker to execute code over a network. |
| CVE-2026-42989 | 7.8 | 2026-06-09 | Improper link resolution before file access ('link following') in Winlogon allows an authorized attacker to elevate priv |
| CVE-2026-42991 | 7.8 | 2026-06-09 | Concurrent execution using shared resource with improper synchronization ('race condition') in Windows Push Notification |
| CVE-2026-42992 | 7.5 | 2026-06-09 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-42993 | 7.5 | 2026-06-09 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-44799 | 7.5 | 2026-06-09 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-44801 | 7.5 | 2026-06-09 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-44802 | 7.8 | 2026-06-09 | Use after free in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-44803 | 7.8 | 2026-06-09 | Integer overflow or wraparound in Windows Win32K - GRFX allows an unauthorized attacker to execute code locally. |
| CVE-2026-44804 | 7.8 | 2026-06-09 | Use after free in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-44807 | 7.8 | 2026-06-09 | Use after free in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-44808 | 7.8 | 2026-06-09 | Use after free in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-44809 | 7.8 | 2026-06-09 | Use after free in Windows Common Log File System Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-44810 | 8.4 | 2026-06-09 | Improper authentication in Windows Cryptographic Services allows an unauthorized attacker to elevate privileges locally. |
| CVE-2026-44811 | 7.8 | 2026-06-09 | Use after free in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-44812 | 7.8 | 2026-06-09 | Integer overflow or wraparound in Windows Win32K - GRFX allows an unauthorized attacker to execute code locally. |
| CVE-2026-44813 | 7.8 | 2026-06-09 | Use after free in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-44815 | 9.8 | 2026-06-09 | Stack-based buffer overflow in Windows DHCP Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-44817 | 7.8 | 2026-06-09 | Integer underflow (wrap or wraparound) in Microsoft Office Excel allows an unauthorized attacker to execute code locally |
| CVE-2026-44818 | 7.0 | 2026-06-09 | Integer underflow (wrap or wraparound) in Microsoft Office Excel allows an unauthorized attacker to execute code locally |
| CVE-2026-44819 | 7.8 | 2026-06-09 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-44820 | 7.8 | 2026-06-09 | Integer underflow (wrap or wraparound) in Microsoft Office Excel allows an unauthorized attacker to execute code locally |
| CVE-2026-44822 | 8.2 | 2026-06-09 | Out-of-bounds read in Microsoft Office Excel allows an unauthorized attacker to disclose information over a network. |
| CVE-2026-44823 | 7.8 | 2026-06-09 | Integer underflow (wrap or wraparound) in Microsoft Office Excel allows an unauthorized attacker to execute code locally |
| CVE-2026-44824 | 7.8 | 2026-06-09 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-45445 | 7.5 | 2026-06-09 | Issue summary: When an application drives an AES-OCB context through the
public EVP_Cipher() one-shot interface, the app |
| CVE-2026-45447 | 9.8 | 2026-06-09 | Issue summary: A specially crafted PKCS#7 or S/MIME signed message could
trigger a use-after-free during PKCS#7 signatur |
| CVE-2026-45456 | 8.4 | 2026-06-09 | Access of resource using incompatible type ('type confusion') in Microsoft Office allows an unauthorized attacker to exe |
| CVE-2026-45457 | 7.8 | 2026-06-09 | Untrusted pointer dereference in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-45458 | 8.4 | 2026-06-09 | Access of resource using incompatible type ('type confusion') in Microsoft Office allows an unauthorized attacker to exe |
| CVE-2026-45461 | 8.4 | 2026-06-09 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-45463 | 8.4 | 2026-06-09 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-45469 | 7.8 | 2026-06-09 | Integer underflow (wrap or wraparound) in Microsoft Office Excel allows an unauthorized attacker to execute code locally |
| CVE-2026-45471 | 7.8 | 2026-06-09 | Untrusted pointer dereference in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-45472 | 8.4 | 2026-06-09 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-45474 | 8.4 | 2026-06-09 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-45475 | 7.8 | 2026-06-09 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-45476 | 8.2 | 2026-06-09 | Use after free in Linux MANA Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-45481 | 7.3 | 2026-06-09 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-45482 | 8.4 | 2026-06-09 | Improper limitation of a pathname to a restricted directory ('path traversal') in GitHub Copilot and Visual Studio Code  |
| CVE-2026-45484 | 8.8 | 2026-06-09 | Deserialization of untrusted data in Microsoft Office SharePoint allows an authorized attacker to elevate privileges ove |
| CVE-2026-45486 | 7.8 | 2026-06-09 | Untrusted pointer dereference in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-45487 | 7.8 | 2026-06-09 | Time-of-check time-of-use (TOCTOU) race condition in Program Compatibility Assistant Service allows an authorized attack |
| CVE-2026-45490 | 7.8 | 2026-06-09 | Improper authorization in .NET allows an authorized attacker to elevate privileges locally. |
| CVE-2026-45503 | 8.1 | 2026-06-09 | Server-side request forgery (ssrf) in Microsoft Exchange Server allows an authorized attacker to disclose information ov |
| CVE-2026-45504 | 8.8 | 2026-06-09 | Server-side request forgery (ssrf) in Microsoft Exchange Server allows an authorized attacker to elevate privileges over |
| CVE-2026-45583 | 7.5 | 2026-06-09 | Improper control of generation of code ('code injection') in Microsoft Exchange Server allows an unauthorized attacker t |
| CVE-2026-45586 | 7.8 | 2026-06-09 | Improper link resolution before file access ('link following') in Windows Collaborative Translation Framework allows an  |
| CVE-2026-45588 | 7.9 | 2026-06-09 | Protection mechanism failure in Windows Secure Boot allows an authorized attacker to bypass a security feature locally. |
| CVE-2026-45591 | 7.5 | 2026-06-09 | Uncontrolled resource consumption in ASP.NET Core allows an unauthorized attacker to deny service over a network. |
| CVE-2026-45592 | 7.8 | 2026-06-09 | Integer overflow or wraparound in Windows Internet (wininet.dll) allows an authorized attacker to elevate privileges loc |
| CVE-2026-45593 | 7.8 | 2026-06-09 | Use after free in Windows SDK allows an authorized attacker to elevate privileges locally. |
| CVE-2026-45596 | 7.0 | 2026-06-09 | Use after free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges loca |
| CVE-2026-45597 | 7.0 | 2026-06-09 | Concurrent execution using shared resource with improper synchronization ('race condition') in UI Automation Manager (ui |
| CVE-2026-45598 | 7.0 | 2026-06-09 | Use after free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges loca |
| CVE-2026-45599 | 8.1 | 2026-06-09 | Use after free in Universal Plug and Play (upnp.dll) allows an unauthorized attacker to execute code over a network. |
| CVE-2026-45600 | 7.8 | 2026-06-09 | Access of resource using incompatible type ('type confusion') in Windows Kernel-Mode Drivers allows an authorized attack |
| CVE-2026-45601 | 7.0 | 2026-06-09 | Use after free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges loca |
| CVE-2026-45602 | 9.1 | 2026-06-09 | No cwe for this issue in Windows DHCP Server allows an unauthorized attacker to perform tampering over a network. |
| CVE-2026-45603 | 7.0 | 2026-06-09 | Use after free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges loca |
| CVE-2026-45605 | 7.8 | 2026-06-09 | Use after free in Windows Bluetooth Service allows an authorized attacker to elevate privileges locally. |
| CVE-2026-45607 | 8.4 | 2026-06-09 | Out-of-bounds read in Windows Hyper-V allows an unauthorized attacker to execute code locally. |
| CVE-2026-45635 | 8.1 | 2026-06-09 | Use after free in Universal Plug and Play (upnp.dll) allows an unauthorized attacker to execute code over a network. |
| CVE-2026-45636 | 7.8 | 2026-06-09 | Heap-based buffer overflow in Windows NTFS allows an unauthorized attacker to execute code locally. |
| CVE-2026-45637 | 7.8 | 2026-06-09 | Use after free in Windows DWM Core Library allows an authorized attacker to elevate privileges locally. |
| CVE-2026-45638 | 7.8 | 2026-06-09 | Use after free in Windows Ancillary Function Driver for WinSock allows an authorized attacker to elevate privileges loca |
| CVE-2026-45639 | 7.5 | 2026-06-09 | Out-of-bounds read in Windows RDP allows an unauthorized attacker to disclose information over a network. |
| CVE-2026-45640 | 7.0 | 2026-06-09 | Use after free in Windows Bluetooth Port Driver allows an authorized attacker to elevate privileges locally. |
| CVE-2026-45641 | 8.4 | 2026-06-09 | Out-of-bounds read in Windows Hyper-V allows an unauthorized attacker to execute code locally. |
| CVE-2026-45643 | 7.8 | 2026-06-09 | Untrusted pointer dereference in Microsoft Office Word allows an unauthorized attacker to execute code locally. |
| CVE-2026-45644 | 8.0 | 2026-06-09 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Live Share Canvas SDK  |
| CVE-2026-45645 | 7.8 | 2026-06-09 | Heap-based buffer overflow in Microsoft Office allows an unauthorized attacker to execute code locally. |
| CVE-2026-45648 | 8.8 | 2026-06-09 | Stack-based buffer overflow in Active Directory Domain Services allows an authorized attacker to execute code over a net |
| CVE-2026-45649 | 7.1 | 2026-06-09 | Improper access control in Office for Android allows an unauthorized attacker to perform spoofing locally. |
| CVE-2026-45653 | 7.0 | 2026-06-09 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-45654 | 7.9 | 2026-06-09 | Protection mechanism failure in Windows Secure Boot allows an authorized attacker to bypass a security feature locally. |
| CVE-2026-45656 | 7.8 | 2026-06-09 | Protection mechanism failure in Windows UEFI allows an authorized attacker to bypass a security feature locally. |
| CVE-2026-45657 | 9.8 | 2026-06-09 | Use after free in Windows Kernel allows an unauthorized attacker to execute code over a network. |
| CVE-2026-45658 | 7.8 | 2026-06-09 | Protection mechanism failure in Windows BitLocker allows an unauthorized attacker to bypass a security feature with a ph |
| CVE-2026-45771 | 7.5 | 2026-06-09 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-46492 | 7.2 | 2026-06-09 | md-fileserver allows for local viewing of markdown files in a browser. Prior to version 1.10.3, a cross-site scripting ( |
| CVE-2026-47281 | 9.6 | 2026-06-09 | Improper input validation in Visual Studio Code allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-47288 | 7.1 | 2026-06-09 | Integer overflow or wraparound in Windows Kerberos allows an authorized attacker to execute code over an adjacent networ |
| CVE-2026-47289 | 8.8 | 2026-06-09 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-47291 | 9.8 | 2026-06-09 | Integer overflow or wraparound in Windows HTTP.sys allows an unauthorized attacker to execute code over a network. |
| CVE-2026-47292 | 7.8 | 2026-06-09 | Inclusion of functionality from untrusted control sphere in Visual Studio Code allows an unauthorized attacker to elevat |
| CVE-2026-47293 | 7.0 | 2026-06-09 | Use after free in Microsoft Office Click-To-Run allows an authorized attacker to elevate privileges locally. |
| CVE-2026-47298 | 8.0 | 2026-06-09 | Improper authorization in Microsoft Office SharePoint allows an authorized attacker to execute code over a network. |
| CVE-2026-47631 | 8.1 | 2026-06-09 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Exchange Server allows |
| CVE-2026-47634 | 7.3 | 2026-06-09 | Improper neutralization of input during web page generation ('cross-site scripting') in Microsoft Office SharePoint allo |
| CVE-2026-47635 | 8.4 | 2026-06-09 | Access of resource using incompatible type ('type confusion') in Microsoft Office allows an unauthorized attacker to exe |
| CVE-2026-47643 | 9.8 | 2026-06-09 | External control of file name or path in Azure Stack Edge allows an unauthorized attacker to execute code over a network |
| CVE-2026-47648 | 7.0 | 2026-06-09 | Untrusted search path in Windows Storage allows an authorized attacker to elevate privileges locally. |
| CVE-2026-47652 | 8.2 | 2026-06-09 | Out-of-bounds read in Windows Hyper-V allows an unauthorized attacker to execute code locally. |
| CVE-2026-47653 | 8.8 | 2026-06-09 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-47654 | 7.5 | 2026-06-09 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-47656 | 7.9 | 2026-06-09 | Protection mechanism failure in Windows Boot Manager allows an authorized attacker to bypass a security feature locally. |
| CVE-2026-48563 | 7.5 | 2026-06-09 | Heap-based buffer overflow in Remote Desktop Client allows an unauthorized attacker to execute code over a network. |
| CVE-2026-48565 | 7.8 | 2026-06-09 | Untrusted search path in Windows Narrator Braille allows an authorized attacker to elevate privileges locally. |
| CVE-2026-48568 | 7.9 | 2026-06-09 | Protection mechanism failure in Windows Secure Boot allows an authorized attacker to bypass a security feature locally. |
| CVE-2026-48569 | 7.1 | 2026-06-09 | Improper input validation in Visual Studio Code allows an unauthorized attacker to bypass a security feature locally. |
| CVE-2026-48570 | 7.9 | 2026-06-09 | Protection mechanism failure in Windows Secure Boot allows an authorized attacker to bypass a security feature locally. |
| CVE-2026-48573 | 7.9 | 2026-06-09 | Protection mechanism failure in Windows Secure Boot allows an authorized attacker to bypass a security feature locally. |
| CVE-2026-48574 | 7.8 | 2026-06-09 | Heap-based buffer overflow in Windows Media allows an unauthorized attacker to execute code locally. |
| CVE-2026-48575 | 7.9 | 2026-06-09 | Protection mechanism failure in Windows Secure Boot allows an authorized attacker to bypass a security feature locally. |
| CVE-2026-48576 | 7.9 | 2026-06-09 | Protection mechanism failure in Windows Secure Boot allows an authorized attacker to bypass a security feature locally. |
| CVE-2026-48578 | 7.9 | 2026-06-09 | Protection mechanism failure in Windows Secure Boot allows an authorized attacker to bypass a security feature locally. |
| CVE-2026-48583 | 7.8 | 2026-06-09 | Use after free in Windows Kernel allows an authorized attacker to elevate privileges locally. |
| CVE-2026-49160 | 7.5 | 2026-06-09 | Uncontrolled resource consumption in HTTP/2 allows an unauthorized attacker to deny service over a network. |
| CVE-2026-49161 | 7.8 | 2026-06-09 | Improper access control in Microsoft PC Manager allows an authorized attacker to bypass a security feature locally. |
| CVE-2026-49475 | 7.5 | 2026-06-09 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-49840 | 9.1 | 2026-06-09 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-49841 | 9.8 | 2026-06-09 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-49842 | 7.5 | 2026-06-09 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-49847 | 7.5 | 2026-06-09 | FreeSWITCH is a Software Defined Telecom Stack enabling the digital transformation from proprietary telecom switches to  |
| CVE-2026-49957 | 7.7 | 2026-06-09 | Hermes WebUI before version 0.51.269 contains a workspace boundary bypass vulnerability that allows authenticated attack |
| CVE-2026-49959 | 8.8 | 2026-06-09 | Hermes WebUI before version 0.51.311 contains a remote code execution vulnerability that allows authenticated attackers  |
| CVE-2026-7383 | 8.1 | 2026-06-09 | Issue summary: A signed integer overflow when sizing the destination
buffer for Unicode output in ASN1_mbstring_ncopy()  |
| CVE-2026-9076 | 7.5 | 2026-06-09 | Issue summary: When CMS password-based decryption (RFC 3211 / PWRI key unwrap)
processes attacker-supplied CMS data, an  |
| CVE-2026-34691 | 9.3 | 2026-06-09 | Adobe Experience Manager Forms JEE versions LTS SP1, 6.5.24.0 and earlier are affected by a stored Cross-Site Scripting  |
| CVE-2026-34693 | 8.0 | 2026-06-09 | Adobe Experience Manager Forms JEE versions LTS SP1, 6.5.24.0 and earlier are affected by a reflected Cross-Site Scripti |
| CVE-2026-34695 | 7.8 | 2026-06-09 | InDesign Desktop versions 21.3, 20.5.3 and earlier are affected by a Stack-based Buffer Overflow vulnerability that coul |
| CVE-2026-34696 | 7.8 | 2026-06-09 | InDesign Desktop versions 21.3, 20.5.3 and earlier are affected by a Use After Free vulnerability that could result in a |
| CVE-2026-34697 | 7.8 | 2026-06-09 | InDesign Desktop versions 21.3, 20.5.3 and earlier are affected by a Stack-based Buffer Overflow vulnerability that coul |
| CVE-2026-34698 | 7.8 | 2026-06-09 | InDesign Desktop versions 21.3, 20.5.3 and earlier are affected by a Heap-based Buffer Overflow vulnerability that could |
| CVE-2026-34699 | 7.8 | 2026-06-09 | InDesign Desktop versions 21.3, 20.5.3 and earlier are affected by a Heap-based Buffer Overflow vulnerability that could |
| CVE-2026-34700 | 7.8 | 2026-06-09 | InDesign Desktop versions 21.3, 20.5.3 and earlier are affected by an out-of-bounds write vulnerability that could resul |
| CVE-2026-34701 | 7.8 | 2026-06-09 | InDesign Desktop versions 21.3, 20.5.3 and earlier are affected by a Heap-based Buffer Overflow vulnerability that could |
| CVE-2026-34702 | 7.8 | 2026-06-09 | InDesign Desktop versions 21.3, 20.5.3 and earlier are affected by a Stack-based Buffer Overflow vulnerability that coul |
| CVE-2026-34706 | 7.8 | 2026-06-09 | InCopy versions 21.3, 20.5.3 and earlier are affected by an out-of-bounds write vulnerability that could result in arbit |
| CVE-2026-34707 | 7.8 | 2026-06-09 | InCopy versions 21.3, 20.5.3 and earlier are affected by a Heap-based Buffer Overflow vulnerability that could result in |
| CVE-2026-34708 | 7.8 | 2026-06-09 | InCopy versions 21.3, 20.5.3 and earlier are affected by a Stack-based Buffer Overflow vulnerability that could result i |
| CVE-2026-48293 | 7.8 | 2026-06-09 | InDesign Desktop versions 21.3, 20.5.3 and earlier are affected by an out-of-bounds write vulnerability that could resul |
| CVE-2026-50511 | 7.8 | 2026-06-09 | Improper link resolution before file access ('link following') in Microsoft PC Manager allows an authorized attacker to  |
| CVE-2026-50512 | 7.8 | 2026-06-09 | Improper link resolution before file access ('link following') in Microsoft PC Manager allows an authorized attacker to  |
| CVE-2026-50635 | 8.8 | 2026-06-09 | LimeSurvey constructs account password-reset links from the client-supplied HTTP Host header without validating it. The  |
| CVE-2026-50636 | 8.8 | 2026-06-09 | The RemoteControl API methods invite_participants and remind_participants pass a caller-supplied token-ID array into Tok |
| CVE-2023-29146 | 8.2 | 2026-06-09 | The utility functions used by Malwarebytes EDR 1.0.11 on Linux for calculating a cryptographic hash of data bytes trunca |
| CVE-2023-43688 | 7.5 | 2026-06-09 | An issue was discovered in Malwarebytes 4.x and 5.x (and Nebula 2020-10-21 and later). There is a Heap buffer overflow i |
| CVE-2025-52292 | 7.5 | 2026-06-09 | A stack buffer overflow in the filein_process function (in_file.c) of GPAC MP4Box v2.4 allows attackers to cause a Denia |
| CVE-2025-52293 | 7.5 | 2026-06-09 | A segmentation violaton in the gf_hevc_read_sps_bs_internal function (media_tools/av_parsers.c) of GPAC MP4Box v2.4 allo |
| CVE-2025-55657 | 7.5 | 2026-06-09 | A NULL pointer dereference in the gf_odf_vvc_cfg_write_bs function (odf/descriptors.c) of GPAC MP4Box v2.4 allows attack |
| CVE-2026-10045 | 9.8 | 2026-06-09 | Shenzhen Kangda Xin Intelligent Network Technology Company's router, model DR300, version 2.1.2.121, contains hardcoded  |
| CVE-2026-30141 | 9.8 | 2026-06-09 | An issue was discovered in bitbank2 AnimatedGIF v2.2.0. A buffer overflow in the DecodeLZW function allows remote attack |
| CVE-2026-36720 | 8.1 | 2026-06-09 | Insecure permissions in bookcars v8.3 allows authenticated attackers to escalate privileges from user to admin via modif |
| CVE-2026-36770 | 7.5 | 2026-06-09 | Shenzhen Tenda Technology Co., Ltd Tenda US_W3V1.0BR v1.0.0.3 was discovered to contain a stack overflow in the Go param |
| CVE-2026-36771 | 7.5 | 2026-06-09 | Shenzhen Tenda Technology Co., Ltd Tenda W3 Wireless Router v1.0.0.3(2204) was discovered to contain a stack overflow in |
| CVE-2026-36819 | 7.5 | 2026-06-09 | Shenzhen Tenda Technology Co., Ltd Tenda W20E v15.11.0.6 was discovered to contain a buffer overflow in the bindMACAddr  |
| CVE-2026-36820 | 7.5 | 2026-06-09 | Shenzhen Tenda Technology Co., Ltd Tenda W20E v15.11.0.6 was discovered to contain a buffer overflow in the webAuthWhite |
| CVE-2026-36821 | 7.5 | 2026-06-09 | Shenzhen Tenda Technology Co., Ltd Tenda W20E v15.11.0.6 was discovered to contain a buffer overflow in the picCropName  |
| CVE-2026-36822 | 7.5 | 2026-06-09 | Shenzhen Tenda Technology Co., Ltd Tenda W20E v15.11.0.6 was discovered to contain a buffer overflow in the macAddr para |
| CVE-2026-36823 | 7.5 | 2026-06-09 | Shenzhen Tenda Technology Co., Ltd Tenda W20E v15.11.0.6 was discovered to contain a buffer overflow in the webAuthUserI |
| CVE-2026-39169 | 7.5 | 2026-06-09 | SEMCMS 5.0 is vulnerable to unauthorized access in SEMCMS_copy.php. |
| CVE-2026-8863 | 7.8 | 2026-06-09 | Multiple Microsoft-sigend UEFI SHIM bootloaders are vulnerable to SecureBoot bypass. An attacker with administrative pri |
| CVE-2026-11822 | 7.8 | 2026-06-09 | SQLite before 3.53.2 contains memory corruption vulnerabilities in the FTS5 full-text search extension that allow attack |
| CVE-2026-11824 | 7.8 | 2026-06-09 | SQLite before 3.53.2 contains a heap-based buffer overflow vulnerability in the FTS5 full-text search extension that all |
| CVE-2026-34709 | 7.8 | 2026-06-09 | Substance3D - Sampler versions 6.0.0 and earlier are affected by an out-of-bounds write vulnerability that could result  |
| CVE-2026-34710 | 7.8 | 2026-06-09 | Substance3D - Sampler versions 6.0.0 and earlier are affected by an out-of-bounds write vulnerability that could result  |
| CVE-2026-47906 | 8.6 | 2026-06-09 | Dreamweaver Desktop versions 21.7 and earlier are affected by a Dependency on Vulnerable Third-Party Component vulnerabi |
| CVE-2026-47907 | 8.2 | 2026-06-09 | Dreamweaver Desktop versions 21.7 and earlier are affected by an Improper Access Control vulnerability that could lead t |
| CVE-2026-47908 | 7.8 | 2026-06-09 | Dreamweaver Desktop versions 21.7 and earlier are affected by an Access of Uninitialized Pointer vulnerability that coul |
| CVE-2026-48305 | 7.8 | 2026-06-09 | Substance3D - Sampler versions 6.0.0 and earlier are affected by an out-of-bounds write vulnerability that could result  |
| CVE-2026-48306 | 7.8 | 2026-06-09 | Substance3D - Sampler versions 6.0.0 and earlier are affected by an out-of-bounds write vulnerability that could result  |
| CVE-2025-71319 | 7.5 | 2026-06-09 | image-size 1.1.0 before 1.2.1 and 2.0.0 before 2.0.2 contain a denial of service vulnerability in the findBox function w |
| CVE-2026-47911 | 7.8 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by an out-of-bounds write vulnerability that |
| CVE-2026-47912 | 7.8 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by a Use After Free vulnerability that could |
| CVE-2026-47913 | 7.8 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by a Use After Free vulnerability that could |
| CVE-2026-47914 | 7.8 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by a Use After Free vulnerability that could |
| CVE-2026-47915 | 7.8 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by a Use After Free vulnerability that could |
| CVE-2026-47916 | 7.8 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by a Use After Free vulnerability that could |
| CVE-2026-47917 | 7.8 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by a Use After Free vulnerability that could |
| CVE-2026-47918 | 7.8 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by a Use After Free vulnerability that could |
| CVE-2026-47919 | 7.8 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by a Use After Free vulnerability that could |
| CVE-2026-47920 | 7.8 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by a Use After Free vulnerability that could |
| CVE-2026-47921 | 7.8 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by a Use After Free vulnerability that could |
| CVE-2026-47928 | 9.6 | 2026-06-09 | ColdFusion versions 2023.19, 2025.8 and earlier are affected by an Improper Input Validation vulnerability that could re |
| CVE-2026-47929 | 8.4 | 2026-06-09 | ColdFusion versions 2023.19, 2025.8 and earlier are affected by an Incorrect Authorization vulnerability that could resu |
| CVE-2026-47930 | 8.1 | 2026-06-09 | ColdFusion versions 2023.19, 2025.8 and earlier are affected by an Improper Input Validation vulnerability that could re |
| CVE-2026-47931 | 8.4 | 2026-06-09 | ColdFusion versions 2023.19, 2025.8 and earlier are affected by an Improper Input Validation vulnerability that could re |
| CVE-2026-47932 | 8.8 | 2026-06-09 | ColdFusion versions 2023.19, 2025.8 and earlier are affected by an Improper Limitation of a Pathname to a Restricted Dir |
| CVE-2026-47937 | 7.4 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by an Uncontrolled Search Path Element vulne |
| CVE-2026-47938 | 10.0 | 2026-06-09 | Adobe Campaign Classic (ACC) versions 7.4.3 build 9394 and earlier are affected by a Server-Side Request Forgery (SSRF)  |
| CVE-2026-47952 | 7.8 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by a Heap-based Buffer Overflow vulnerabilit |
| CVE-2026-47955 | 7.8 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by a Use After Free vulnerability that could |
| CVE-2026-47959 | 7.8 | 2026-06-09 | Acrobat Reader versions 24.001.30365, 26.001.21651 and earlier are affected by a Stack-based Buffer Overflow vulnerabili |
| CVE-2026-47960 | 7.4 | 2026-06-09 | ColdFusion versions 2023.19, 2025.8 and earlier are affected by an Improper Restriction of XML External Entity Reference |
| CVE-2026-48291 | 7.8 | 2026-06-09 | Format Plugins versions 1.1.2 and earlier are affected by a Heap-based Buffer Overflow vulnerability that could result i |
| CVE-2026-48292 | 7.8 | 2026-06-09 | Format Plugins versions 1.1.2 and earlier are affected by a Heap-based Buffer Overflow vulnerability that could result i |
| CVE-2026-48303 | 10.0 | 2026-06-09 | Adobe Campaign Classic (ACC) versions 7.4.3 build 9394 and earlier are affected by an Incorrect Authorization vulnerabil |
| CVE-2026-34711 | 7.5 | 2026-06-09 | CAI Content Credentials versions c2pa-web@0.7.1, c2pa-v0.80.1 and earlier are affected by an Integer Overflow or Wraparo |
| CVE-2026-34712 | 7.5 | 2026-06-09 | CAI Content Credentials versions c2pa-web@0.7.1, c2pa-v0.80.1 and earlier are affected by an Improper Input Validation v |
| CVE-2026-34713 | 7.5 | 2026-06-09 | CAI Content Credentials versions c2pa-web@0.7.1, c2pa-v0.80.1 and earlier are affected by an Uncontrolled Resource Consu |
| CVE-2026-46373 | 7.5 | 2026-06-09 | SQLFluff is a modular SQL linter and auto-formatter with support for multiple dialects and templated code. Prior to vers |
| CVE-2026-46374 | 7.5 | 2026-06-09 | SQLFluff is a modular SQL linter and auto-formatter with support for multiple dialects and templated code. Prior to vers |
| CVE-2026-9740 | 7.5 | 2026-06-09 | A vulnerability in MongoDB Server's BSON validation logic allows an unauthenticated user to crash the mongod process by  |
| CVE-2026-9742 | 7.5 | 2026-06-09 | When OIDC authentication is enabled in configuration, clients may set specific values in the "mechanism" parameter of th |
| CVE-2026-9753 | 8.1 | 2026-06-09 | The $_internalApplyOplogUpdate aggregation pipeline stage can be used to execute a document diff containing a malformed  |
| CVE-2026-40988 | 7.5 | 2026-06-10 | An application using spring-security-saml2-service-provider and the REDIRECT binding for SAML 2.0 Login or Logout may be |
| CVE-2026-40993 | 7.3 | 2026-06-10 | An attacker with write permissions to the database table managed by JdbcAssertingPartyMetadataRepository (saml2_assertin |
| CVE-2026-41003 | 7.6 | 2026-06-10 | An attacker able to influence values in RelyingPartyRegistration may be able to run arbitrary code on HTML forms generat |
| CVE-2026-41695 | 7.5 | 2026-06-10 | Spring Data Commons applications may be vulnerable to denial of service through resource exhaustion when attacker-contro |
| CVE-2026-41716 | 7.5 | 2026-06-10 | Spring Data's internal property-lookup cache accepts and permanently retains attacker-supplied strings as cache keys, al |
| CVE-2026-41717 | 8.1 | 2026-06-10 | Spring Data MongoDB contains a SpEL (Spring Expression Language) expression injection vulnerability. The issue occurs du |
| CVE-2026-41728 | 7.5 | 2026-06-10 | Spring Data REST's JSON Patch (application/json-patch+json) implementation does not apply the write-access filter to int |
| CVE-2026-41729 | 8.1 | 2026-06-10 | Spring Data REST is vulnerable to SpEL expression injection through map-typed properties when processing JSON Patch (app |
| CVE-2026-41731 | 8.1 | 2026-06-10 | JsonKafkaHeaderMapper and the deprecated DefaultKafkaHeaderMapper matched type headers against trusted packages using a  |
| CVE-2026-41732 | 8.1 | 2026-06-10 | JsonPulsarHeaderMapper matched type headers against trusted packages using a prefix check, meaning that trusting any pac |
| CVE-2026-44716 | 7.5 | 2026-06-10 | Pipecat is an open-source Python framework for building real-time voice and multimodal conversational agents. From versi |
| CVE-2026-46432 | 7.8 | 2026-06-10 | LMDeploy is a toolkit for compressing, deploying, and serving large language models. In versions 0.12.3 and prior, LMDep |
| CVE-2026-46491 | 8.6 | 2026-06-10 | SimpleSAMLphp-casserver is a CAS 1.0 and 2.0 compliant CAS server in the form of a SimpleSAMLphp module. Prior to versio |
| CVE-2026-46517 | 7.8 | 2026-06-10 | LMDeploy is a toolkit for compressing, deploying, and serving large language models. In versions 0.12.3 and prior, hardc |
| CVE-2026-46518 | 7.7 | 2026-06-10 | OpenEMR is a free and open source electronic health records and medical practice management application. Prior to versio |
| CVE-2026-46541 | 7.5 | 2026-06-10 | Nimiq is a Rust implementation of the Nimiq Proof-of-Stake protocol based on the Albatross consensus algorithm. Prior to |
| CVE-2026-46545 | 7.5 | 2026-06-10 | Nimiq is a Rust implementation of the Nimiq Proof-of-Stake protocol based on the Albatross consensus algorithm. Prior to |
| CVE-2026-53673 | 8.1 | 2026-06-10 | BuddyPress 14.4.0 contains an insecure direct object reference vulnerability in the messages REST API that allows authen |
| CVE-2026-53674 | 7.1 | 2026-06-10 | BuddyPress 14.4.0 contains a regular expression injection vulnerability in the activity mention resolver that, when user |
| CVE-2026-45328 | 9.3 | 2026-06-10 | ESF-IDF is the Espressif Internet of Things (IOT) Development Framework. In versions 5.5.4 and 6.0, the esp_tee componen |
| CVE-2026-45329 | 7.1 | 2026-06-10 | ESF-IDF is the Espressif Internet of Things (IOT) Development Framework. In versions 5.5.4 and 6.0, several ESP-TEE secu |
| CVE-2026-45541 | 7.5 | 2026-06-10 | ESF-IDF is the Espressif Internet of Things (IOT) Development Framework. In versions 5.2.6, 5.3.5, 5.4.4, 5.5.4, and 6.0 |
| CVE-2026-45542 | 7.1 | 2026-06-10 | ESF-IDF is the Espressif Internet of Things (IOT) Development Framework. In versions 5.2.6, 5.3.5, 5.4.4, 5.5.4, and 6.0 |
| CVE-2026-11837 | 7.3 | 2026-06-10 | A local privilege escalation vulnerability was found in the ansible.posix authorized_key module. The module's keyfile()  |
| CVE-2026-3326 | 8.6 | 2026-06-10 | The Xstore WordPress theme before 9.7.3 does not properly sanitise and escape a parameter before using it in a SQL state |
| CVE-2026-8071 | 8.8 | 2026-06-10 | The Anti-Spam by CleanTalk. Spam protection WordPress plugin before 6.79 does not properly sanitize content within a cus |
| CVE-2026-9067 | 9.1 | 2026-06-10 | The Schema & Structured Data for WP & AMP WordPress plugin before 1.60 does not check user capabilities on its frontend  |
| CVE-2025-6254 | 9.8 | 2026-06-10 | The Doctreat Core plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 1.6.8 |
| CVE-2026-3018 | 7.5 | 2026-06-10 | The Newsletters plugin for WordPress is vulnerable to time-based SQL Injection via the ‘wpmlsubscriber_id’ parameter in  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-11645 | Google / Chromium V8 | 2026-06-09 | 2026-06-23 | Unknown |
| CVE-2026-7473 | Arista / Extensible Operating System | 2026-06-09 | 2026-06-23 | Unknown |
| CVE-2026-20245 | Cisco / Catalyst SD-WAN Manager | 2026-06-09 | 2026-06-23 | Unknown |
| CVE-2026-42271 | BerriAI / LiteLLM | 2026-06-08 | 2026-06-22 | Unknown |
| CVE-2026-50751 | Check Point / Security Gateway | 2026-06-08 | 2026-06-11 | Known |
| CVE-2026-28318 | SolarWinds / Serv-U | 2026-06-05 | 2026-06-19 | Unknown |
| CVE-2026-45247 | Mirasvit / Mirasvit Full Page Cache Warmer | 2026-06-03 | 2026-06-06 | Unknown |

---

*Total entries in CISA KEV catalog: 1617*