# Vulnerability Intelligence Report

**Date:** 2026-06-11  
**Generated:** 2026-06-11T12:09:24Z  

---

## Executive Summary

Our environment faces 93 high-severity vulnerabilities with CISA adding 6 new Known Exploited Vulnerabilities this week. Critical concerns include multiple Ghidra security flaws (SQL injection, command injection, unsafe deserialization), Slate Digital privilege escalation vulnerabilities, and Node.js denial-of-service risks. The addition of Chromium V8, Cisco SD-WAN, and Check Point gateway vulnerabilities to the KEV catalog indicates active exploitation in the wild. Immediate patching is essential to prevent system compromise, data theft, and service disruption.

---

## Risk Narrative

The threat landscape shows active exploitation of infrastructure components with 6 new KEV entries targeting widely-used enterprise systems. Attackers are focusing on privilege escalation, remote code execution, and authentication bypass techniques. The Ghidra vulnerabilities are particularly concerning as they affect reverse engineering tools used by security teams, potentially compromising analysis environments. Network infrastructure remains a prime target with Cisco and Check Point vulnerabilities enabling lateral movement. The combination of web application flaws and system-level exploits creates multiple attack vectors for ransomware deployment and data exfiltration campaigns.

---

## Prioritized Action Items

1. Patch all Ghidra installations to version 12.1 immediately due to multiple critical vulnerabilities including SQL injection and RCE.
2. Update Slate Digital Connect on all macOS systems to address privileged helper tool exploitation risks.
3. Review and update image-size Node.js library dependencies to versions above 2.0.2 across all applications.
4. Prioritize patching of Chromium V8, Cisco SD-WAN Manager, and Check Point Security Gateway systems within 72 hours.
5. Implement additional monitoring for XSS attempts targeting WPZOOM Portfolio and similar web applications.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-24066 | 8.4 | 2026-06-10 | Slate Digital Connect 1.37.0 for macOS installs a privileged helper tool, com.slatedigital.connect.privileged.helper.too |
| CVE-2026-24067 | 8.4 | 2026-06-10 | Slate Digital Connect 1.37.0 for macOS installs a privileged helper tool, com.slatedigital.connect.privileged.helper.too |
| CVE-2025-71329 | 7.5 | 2026-06-10 | image-size through 2.0.2 contains a denial of service vulnerability that allows remote attackers to permanently block th |
| CVE-2025-71330 | 7.5 | 2026-06-10 | image-size through 2.0.2 contains a denial of service vulnerability that allows remote attackers to permanently block th |
| CVE-2026-49069 | 7.1 | 2026-06-10 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WPZOOM Portfolio a |
| CVE-2026-49498 | 8.8 | 2026-06-10 | Ghidra 11.0 before 12.1 contains a SQL injection vulnerability in the changePassword() method of PostgresFunctionDatabas |
| CVE-2026-52750 | 7.8 | 2026-06-10 | Ghidra before 12.1 contains a command injection vulnerability in URL annotation handling on Windows where cmd.exe metach |
| CVE-2026-52751 | 8.8 | 2026-06-10 | Ghidra before 12.1 contains an unsafe deserialization vulnerability in client-side Shared-Project RMI connection code th |
| CVE-2026-52752 | 7.8 | 2026-06-10 | Ghidra before 12.0.2 contains a path traversal vulnerability in the extension installer that fails to validate ZIP entry |
| CVE-2026-52754 | 8.8 | 2026-06-10 | Ghidra before 12.1 contains an authentication bypass vulnerability in PKIAuthenticationModule.authenticate() that allows |
| CVE-2026-52755 | 7.8 | 2026-06-10 | Ghidra before 12.0.4 contains a path traversal vulnerability in the theme import functionality that allows attackers to  |
| CVE-2026-52758 | 8.8 | 2026-06-10 | Ghidra before 12.1 contains a SQL injection vulnerability in BSim filter types that concatenate user-supplied values dir |
| CVE-2026-53435 | 8.8 | 2026-06-10 | In Jenkins 2.567 and earlier, LTS 2.555.2 and earlier, it is possible for attackers to have Jenkins deserialize arbitrar |
| CVE-2026-9758 | 7.3 | 2026-06-10 | Improper comparison with the certificates trusted list in S2OPC allows an attacker well-formed untrusted certificate to  |
| CVE-2026-45549 | 8.5 | 2026-06-10 | Roxy-WI is a web interface for managing Haproxy, Nginx, Apache and Keepalived servers. In versions 8.2.6.4 and prior, ag |
| CVE-2026-45550 | 9.1 | 2026-06-10 | Roxy-WI is a web interface for managing Haproxy, Nginx, Apache and Keepalived servers. In versions 8.2.6.4 and prior, PU |
| CVE-2026-45552 | 9.9 | 2026-06-10 | Roxy-WI is a web interface for managing Haproxy, Nginx, Apache and Keepalived servers. In versions 8.2.6.4 and prior, th |
| CVE-2026-45556 | 9.9 | 2026-06-10 | Roxy-WI is a web interface for managing Haproxy, Nginx, Apache and Keepalived servers. In versions 8.2.6.4 and prior, PO |
| CVE-2026-45558 | 9.9 | 2026-06-10 | Roxy-WI is a web interface for managing Haproxy, Nginx, Apache and Keepalived servers. In versions 8.2.6.4 and prior, th |
| CVE-2026-45564 | 8.8 | 2026-06-10 | Roxy-WI is a web interface for managing Haproxy, Nginx, Apache and Keepalived servers. In versions 8.2.6.4 and prior, PO |
| CVE-2026-53469 | 9.1 | 2026-06-10 | A flaw was found in migration-planner. An authenticated user can exploit this vulnerability by sending a DELETE request  |
| CVE-2026-53470 | 9.6 | 2026-06-10 | A flaw was found in migration-planner. An authenticated attacker could exploit an improper access control vulnerability  |
| CVE-2026-53471 | 9.6 | 2026-06-10 | A flaw was found in migration-planner. The agent-API middleware processes JSON Web Tokens (JWTs) for authentication, but |
| CVE-2026-53473 | 7.3 | 2026-06-10 | A flaw was found in migration-planner-ui-app. An attacker can register a malicious discovery agent with a specially craf |
| CVE-2026-53474 | 9.6 | 2026-06-10 | A flaw was found in migration-planner. A remote authenticated attacker could exploit this vulnerability by uploading a s |
| CVE-2026-53475 | 9.3 | 2026-06-10 | A flaw was found in assisted-migration-agent. The application hardcodes insecure Transport Layer Security (TLS) connecti |
| CVE-2026-53476 | 9.6 | 2026-06-10 | A flaw was found in assisted-migration-agent. An unauthenticated attacker, located on the same local area network (LAN), |
| CVE-2026-53689 | 7.1 | 2026-06-10 | libnfs through 6.0.2 before 55c18ea does not validate a string size, leading to an integer overflow during a connection  |
| CVE-2026-6090 | 7.0 | 2026-06-10 | A potential authentication bypass was reported in Lenovo Smart Connect for Windows that could allow a local authenticate |
| CVE-2026-8637 | 7.8 | 2026-06-10 | A potential uncontrolled search path vulnerability was reported in the LanSchool Classic client application that could a |
| CVE-2026-9045 | 7.8 | 2026-06-10 | During an internal security assessment, a potential vulnerability was discovered in Lenovo Accessories and Display Manag |
| CVE-2026-25700 | 7.2 | 2026-06-10 | Improper Restriction of Security Token Assignment vulnerability in Apache Answer.

This issue affects Apache Answer: thr |
| CVE-2026-45565 | 8.1 | 2026-06-10 | Roxy-WI is a web interface for managing Haproxy, Nginx, Apache and Keepalived servers. In versions 8.2.6.4 and prior, Es |
| CVE-2026-45567 | 8.3 | 2026-06-10 | Roxy-WI is a web interface for managing Haproxy, Nginx, Apache and Keepalived servers. In versions 8.2.6.4 and prior, th |
| CVE-2026-45569 | 8.1 | 2026-06-10 | Roxy-WI is a web interface for managing Haproxy, Nginx, Apache and Keepalived servers. In versions 8.2.6.4 and prior, om |
| CVE-2026-46558 | 8.3 | 2026-06-10 | Plane is an open-source project management tool. Prior to version 1.3.1, there is a cross-workspace asset authorization  |
| CVE-2026-11417 | 7.3 | 2026-06-10 | OS command injection in the NodejsFunction local bundling pipeline in aws-cdk-lib before 2.245.0 (2.246.0 on Windows) mi |
| CVE-2026-20251 | 8.8 | 2026-06-10 | In Splunk Enterprise versions below 10.2.4, 10.0.7, 9.4.12, and 9.3.13, Splunk Cloud Platform versions below 10.3.2512.1 |
| CVE-2026-20252 | 7.6 | 2026-06-10 | In Splunk Enterprise versions below 10.2.4, 10.0.7, 9.4.12, and 9.3.13, and Splunk Cloud Platform versions below 10.4.26 |
| CVE-2026-20253 | 9.8 | 2026-06-10 | In Splunk Enterprise versions below 10.2.4 and 10.0.7, and Splunk Cloud Platform versions below 10.4.2604.3 and 10.2.251 |
| CVE-2026-20258 | 7.1 | 2026-06-10 | In Splunk Enterprise versions below 10.2.4, 10.0.7, 9.4.12, and 9.3.13, and Splunk Cloud Platform versions below 10.3.25 |
| CVE-2026-45062 | 8.1 | 2026-06-10 | FrankenPHP is a modern application server for PHP. From version 1.11.2 to before version 1.12.3, the splitPos() function |
| CVE-2026-46612 | 8.8 | 2026-06-10 | Fission is an open-source, Kubernetes-native serverless framework that simplifies the deployment of functions and applic |
| CVE-2026-46614 | 9.8 | 2026-06-10 | Fission is an open-source, Kubernetes-native serverless framework that simplifies the deployment of functions and applic |
| CVE-2026-49821 | 7.7 | 2026-06-10 | Fission is an open-source, Kubernetes-native serverless framework that simplifies the deployment of functions and applic |
| CVE-2026-49822 | 7.7 | 2026-06-10 | Fission is an open-source, Kubernetes-native serverless framework that simplifies the deployment of functions and applic |
| CVE-2026-49823 | 7.7 | 2026-06-10 | Fission is an open-source, Kubernetes-native serverless framework that simplifies the deployment of functions and applic |
| CVE-2026-49824 | 8.5 | 2026-06-10 | Fission is an open-source, Kubernetes-native serverless framework that simplifies the deployment of functions and applic |
| CVE-2026-50545 | 9.9 | 2026-06-10 | Fission is an open-source, Kubernetes-native serverless framework that simplifies the deployment of functions and applic |
| CVE-2026-50563 | 9.9 | 2026-06-10 | Fission is an open-source, Kubernetes-native serverless framework that simplifies the deployment of functions and applic |
| CVE-2026-50564 | 9.9 | 2026-06-10 | Fission is an open-source, Kubernetes-native serverless framework that simplifies the deployment of functions and applic |
| CVE-2026-50566 | 9.9 | 2026-06-10 | Fission is an open-source, Kubernetes-native serverless framework that simplifies the deployment of functions and applic |
| CVE-2026-50567 | 7.7 | 2026-06-10 | Fission is an open-source, Kubernetes-native serverless framework that simplifies the deployment of functions and applic |
| CVE-2026-50570 | 8.5 | 2026-06-10 | Fission is an open-source, Kubernetes-native serverless framework that simplifies the deployment of functions and applic |
| CVE-2026-1220 | 7.5 | 2026-06-10 | Race in V8 in Google Chrome prior to 144.0.7559.99 allowed a remote attacker to potentially exploit type confusion via a |
| CVE-2026-6893 | 8.8 | 2026-06-10 | A flaw was found in dracut. A remote attacker on the adjacent network can exploit this vulnerability by providing specia |
| CVE-2022-26758 | 7.1 | 2026-06-10 | A malicious application may cause unexpected changes in memory shared between processes. A memory corruption issue was a |
| CVE-2026-10142 | 7.5 | 2026-06-10 | kafka-python prior to 2.3.2 contains a denial-of-service vulnerability in the protocol parser that allows a malicious br |
| CVE-2026-10143 | 7.5 | 2026-06-10 | kafka-python prior to 2.3.2 contains a denial-of-service vulnerability in SCRAM authentication handling that allows a ma |
| CVE-2026-2049 | 7.8 | 2026-06-10 | GIMP HDR File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote a |
| CVE-2026-42462 | 7.0 | 2026-06-10 | Fedify is a TypeScript library for building federated server apps powered by ActivityPub. Prior to versions 1.9.11, 1.10 |
| CVE-2026-42542 | 7.5 | 2026-06-10 | TDengine is an open source, time-series database optimized for Internet of Things devices. In versions 3.4.0.0 through 3 |
| CVE-2026-44692 | 7.7 | 2026-06-10 | Sharp is a content management framework built for Laravel as a package. Prior to version 9.22.0, Sharp exposes a generic |
| CVE-2026-45783 | 7.5 | 2026-06-10 | libp2p is a JavaScript Implementation of libp2p networking stack. Prior to version 16.2.6, an unauthenticated remote pee |
| CVE-2026-46520 | 7.5 | 2026-06-10 | ImageMagick is free and open-source software used for editing and manipulating digital images. Prior to versions 6.9.13- |
| CVE-2026-46522 | 7.5 | 2026-06-10 | ImageMagick is free and open-source software used for editing and manipulating digital images. Prior to versions 7.1.2.2 |
| CVE-2026-46625 | 7.5 | 2026-06-10 | JavaScript Cookie is a JavaScript API for handling cookies, client-side. Prior to version 3.0.7, js-cookie's internal as |
| CVE-2026-46673 | 7.5 | 2026-06-10 | Russh is a Rust SSH client & server library. Prior to version 0.60.3, CryptoVec used unchecked capacity growth, unchecke |
| CVE-2026-46679 | 7.5 | 2026-06-10 | libp2p is a JavaScript Implementation of libp2p networking stack. Prior to version 15.0.23, three cooperating omissions  |
| CVE-2026-46702 | 7.5 | 2026-06-10 | Russh is a Rust SSH client & server library. From version 0.34.0 to before version 0.61.1, when SSH compression is enabl |
| CVE-2026-48110 | 7.5 | 2026-06-10 | Russh is a Rust SSH client & server library. From version 0.34.0 to before version 0.61.0, several russh client and serv |
| CVE-2026-50131 | 8.6 | 2026-06-10 | Fedify is a TypeScript library for building federated server apps powered by ActivityPub. Fedify previously addressed SS |
| CVE-2026-53738 | 8.1 | 2026-06-10 | Copy & Delete Posts through 1.5.4 lets any plugin-enabled non-admin role invoke every operation in the cdp_action_handli |
| CVE-2026-42305 | 8.8 | 2026-06-10 | Dulwich is a pure-Python implementation of the Git file formats and protocols. Versions starting with 0.10.0 and prior t |
| CVE-2026-42558 | 7.6 | 2026-06-10 | Xibo is an open source digital signage platform with a web content management system and Windows display player software |
| CVE-2026-44693 | 8.8 | 2026-06-10 | Pi-hole FTL is the core engine of the Pi-hole network-level advertisement and tracker blocker. Prior to version 6.6.1, P |
| CVE-2026-46695 | 10.0 | 2026-06-10 | Boxlite is a sandbox service that allows users to create lightweight virtual machines (Boxes) and launch OCI containers  |
| CVE-2026-46703 | 9.6 | 2026-06-10 | Boxlite is a sandbox service that allows users to create lightweight virtual machines (Boxes) and launch OCI containers  |
| CVE-2026-49218 | 7.5 | 2026-06-10 | ImageMagick is free and open-source software used for editing and manipulating digital images. Prior to versions 6.9.13- |
| CVE-2026-52726 | 7.5 | 2026-06-10 | Dulwich is a pure-Python implementation of the Git file formats and protocols. Starting in version 0.23.2 and prior to v |
| CVE-2026-53460 | 7.5 | 2026-06-10 | ImageMagick is free and open-source software used for editing and manipulating digital images. Prior to versions 6.9.13- |
| CVE-2026-53461 | 7.5 | 2026-06-10 | ImageMagick is free and open-source software used for editing and manipulating digital images. Prior to versions 6.9.13- |
| CVE-2026-35273 | 9.8 | 2026-06-11 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Updates Environment Mana |
| CVE-2026-10795 | 8.1 | 2026-06-11 | The UpdraftPlus: WP Backup & Migration Plugin plugin for WordPress is vulnerable to Authentication Bypass in all version |
| CVE-2026-40987 | 7.1 | 2026-06-11 | A malicious or compromised FTP/SFTP/SMB server can write arbitrary files anywhere on the client filesystem (outside the  |
| CVE-2026-40994 | 8.2 | 2026-06-11 | Wss4jSecurityInterceptor initialized its BSP (WS-I Basic Security Profile) compliance flag so that inbound validation di |
| CVE-2026-40998 | 8.2 | 2026-06-11 | Jaxp13XPathTemplate evaluated XPath expressions for StreamSource and SAXSource inputs using a code path that parsed atta |
| CVE-2026-40999 | 8.6 | 2026-06-11 | When WS-Addressing is used with non-anonymous ReplyTo or FaultTo addresses, Spring WS may initiate outbound connections  |
| CVE-2026-41699 | 8.1 | 2026-06-11 | Spring for GraphQL applications are vulnerable to Unsafe Deserialization when processing paginated GraphQL queries. An a |
| CVE-2026-41700 | 8.1 | 2026-06-11 | Spring for GraphQL applications that have enabled the WebSocket transport are vulnerable to Cross-Site WebSocket Hijacki |
| CVE-2026-41856 | 7.5 | 2026-06-11 | The Spring GraphQL annotation detection mechanism for @Controller data fetchers may not correctly resolve annotations on |
| CVE-2023-33999 | 7.1 | 2026-06-11 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in WPVibes WP Mail Lo |
| CVE-2026-5497 | 7.5 | 2026-06-11 | vLLM versions 0.8.0 and later are vulnerable to an Out-of-Memory (OOM) Denial of Service (DoS) attack due to unbounded f |

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

---

*Total entries in CISA KEV catalog: 1617*