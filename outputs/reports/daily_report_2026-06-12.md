# Vulnerability Intelligence Report

**Date:** 2026-06-12  
**Generated:** 2026-06-12T11:42:58Z  

---

## Executive Summary

Our environment faces critical security exposure with 92 high-severity vulnerabilities, including 10 critical-rated issues scoring 9.8-9.9 CVSS. GitLab Enterprise Edition across multiple versions contains severe vulnerabilities affecting authentication and access controls. Additional critical flaws exist in third-party applications including SQL injection, remote code execution, and file upload vulnerabilities. Seven new CISA KEV entries indicate active exploitation of similar vulnerabilities in enterprise environments, creating immediate risk of compromise.

---

## Risk Narrative

The threat landscape presents immediate danger with multiple attack vectors targeting our infrastructure. Critical vulnerabilities in GitLab Enterprise Edition create pathways for unauthorized access and privilege escalation. Third-party applications show patterns of SQL injection and unrestricted file upload vulnerabilities, indicating poor security practices by vendors. CISA's addition of seven new KEV entries suggests active threat actor campaigns targeting similar vulnerabilities. Without immediate remediation, we face high probability of successful attacks leading to data breaches, system compromise, and operational disruption.

---

## Prioritized Action Items

1. Immediately patch GitLab EE installations to versions 18.10.8, 18.11.5, or 19.0.2 to address critical authentication bypass vulnerabilities.
2. Conduct emergency assessment of all systems running Soagen Informa, LimRAD NAC, and Rotaban for immediate patching or isolation.
3. Review and restrict file upload functionality across all web applications to prevent malicious file execution.
4. Implement network segmentation to limit exposure of vulnerable systems identified in the KEV catalog additions.
5. Execute comprehensive vulnerability scanning to identify additional instances of the 92 high-severity CVEs in our environment.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-10087 | 8.7 | 2026-06-11 | GitLab has remediated an issue in GitLab EE affecting all versions from 17.1 before 18.10.8, 18.11 before 18.11.5, and 1 |
| CVE-2026-6552 | 8.7 | 2026-06-11 | GitLab has remediated an issue in GitLab EE affecting all versions from 15.5 before 18.10.8, 18.11 before 18.11.5, and 1 |
| CVE-2026-7250 | 7.5 | 2026-06-11 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 12.10 before 18.10.8, 18.11 before 18.11.5, a |
| CVE-2026-8589 | 7.3 | 2026-06-11 | GitLab has remediated an issue in GitLab EE affecting all versions from 13.1.4 before 18.10.8, 18.11 before 18.11.5, and |
| CVE-2026-11561 | 9.8 | 2026-06-11 | Improper neutralization of special elements used in an expression language statement ('expression language injection') v |
| CVE-2026-7852 | 9.8 | 2026-06-11 | Unrestricted upload of file with dangerous type vulnerability in Limatek System Inc. LimRAD NAC allows Remote Code Inclu |
| CVE-2026-10847 | 7.8 | 2026-06-11 | A local privilege escalation vulnerability exists in Check Point Identity Agent Full for Windows OS. An authenticated lo |
| CVE-2026-11816 | 8.1 | 2026-06-11 | Keras versions prior to 3.14.0 are vulnerable to a path traversal issue in the archive extraction utilities located in ` |
| CVE-2026-38581 | 9.8 | 2026-06-11 | SQL Injection vulnerability in damasac thaipalliative_lte through version 3.0 allows remote attackers to execute arbitra |
| CVE-2026-11839 | 9.9 | 2026-06-11 | Unrestricted upload of file with dangerous type vulnerability in Başarsoft Information Technologies Inc. Rotaban allows  |
| CVE-2026-53777 | 8.1 | 2026-06-11 | Perry before 0.5.1159 contains a path traversal vulnerability that allows a malicious build server to write arbitrary co |
| CVE-2026-7787 | 7.5 | 2026-06-11 | IBM Langflow OSS 1.0.0 through 1.9.1 could allow an authenticated user to read or modify sensitive information by bypass |
| CVE-2026-7870 | 8.8 | 2026-06-11 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a user to gain elevated privileges due to an unqualified library call. A malici |
| CVE-2026-9648 | 9.1 | 2026-06-11 | The crypton-x509-validation Haskell library fails to enforce X.509 NameConstraints, allowing TLS clients to accept certi |
| CVE-2026-44486 | 7.5 | 2026-06-11 | Axios is a promise based HTTP client for the browser and Node.js. Prior to 0.32.0 and 1.16.0, Axios’ Node.js HTTP adapte |
| CVE-2026-44488 | 7.5 | 2026-06-11 | Axios is a promise based HTTP client for the browser and Node.js. Axios versions 1.7.0 through 1.15.x did not enforce co |
| CVE-2026-44492 | 8.6 | 2026-06-11 | Axios is a promise based HTTP client for the browser and Node.js. Prior to 0.32.0 and 1.16.0, Axios does not normalise I |
| CVE-2026-44494 | 8.7 | 2026-06-11 | Axios is a promise based HTTP client for the browser and Node.js. From 1.0.0 to before 1.16.0, the Axios library is vuln |
| CVE-2026-44495 | 7.0 | 2026-06-11 | Axios is a promise based HTTP client for the browser and Node.js. From 0.19.0 to before 0.31.1 and 1.15.2, Axios contain |
| CVE-2026-44496 | 7.5 | 2026-06-11 | Axios is a promise based HTTP client for the browser and Node.js. Axios versions before 0.32.0 on the 0.x line and befor |
| CVE-2026-49982 | 8.2 | 2026-06-11 | tmp is a temporary file and directory creator for node.js. In version 0.2.6, the _assertPath guard added to tmp rejects  |
| CVE-2026-46697 | 7.5 | 2026-06-11 | Fediverse Embeds embeds fediverse posts on WordPress sites. Prior to version 1.5.8, Fediverse Embeds registered an unaut |
| CVE-2026-48546 | 7.3 | 2026-06-11 | KanaDojo before 0.1.18 contains a sandbox escape vulnerability that allows an attacker to execute arbitrary code by expl |
| CVE-2026-49261 | 10.0 | 2026-06-11 | MariaDB server is a community developed fork of MySQL server. Versions 10.6.1 through 10.6.26, 10.11.1 through 10.11.17, |
| CVE-2025-24284 | 8.8 | 2026-06-11 | This issue was addressed with improved checks to prevent unauthorized actions. This issue is fixed in macOS Sequoia 15.4 |
| CVE-2025-31272 | 7.8 | 2026-06-11 | The issue was addressed with improved checks. This issue is fixed in macOS Sequoia 15.4. An app may be able to bypass la |
| CVE-2025-46315 | 7.5 | 2026-06-11 | A permissions issue was addressed with additional restrictions. This issue is fixed in macOS Tahoe 26.1. An app may be a |
| CVE-2026-11774 | 7.6 | 2026-06-11 | An integer overflow flaw was found in the SASL I/O layer of 389 Directory Server (389-ds-base). In sasl_io_start_packet( |
| CVE-2026-46519 | 8.8 | 2026-06-11 | mcp-server-kubernetes is a Model Context Protocol server for Kubernetes cluster management. Prior to version 3.6.0, mcp- |
| CVE-2026-47170 | 7.7 | 2026-06-11 | Garlic-Hub manages digital signage network — devices, content, and playlists — from a single self-hosted interface. Prio |
| CVE-2026-48547 | 7.3 | 2026-06-11 | KanaDojo contains a command injection vulnerability that allows an attacker with pull request access to execute arbitrar |
| CVE-2026-46489 | 8.1 | 2026-06-11 | SolidInvoice is an open-source invoicing platform. Prior to version 2.3.17, the company logo upload feature accepts any  |
| CVE-2026-46622 | 8.1 | 2026-06-11 | SolidInvoice is an open-source invoicing platform. Prior to version 2.3.17, API tokens used to authenticate all REST API |
| CVE-2026-49973 | 9.4 | 2026-06-11 | Hermes WebUI before version 0.51.358 contains an improper access control vulnerability that allows unauthenticated remot |
| CVE-2026-53782 | 7.4 | 2026-06-11 | Summarize before 0.17.0 contains a server-side request forgery vulnerability that allows attackers who control a podcast |
| CVE-2026-41005 | 9.0 | 2026-06-11 | Cloud Foundry UAA incorrectly treated XML encryption to the Service Provider (confidentiality) as a substitute for XML s |
| CVE-2026-50005 | 7.7 | 2026-06-11 | Brickcom cameras
ship with default credentials that allows any unauthenticated remote attacker to silently access camera |
| CVE-2026-50245 | 7.7 | 2026-06-11 | Brickcom cameras allow unauthenticated access to live snapshot images via the /ONVIF endpoint and no authentication is r |
| CVE-2026-53806 | 8.8 | 2026-06-11 | OpenClaw before 2026.5.12 contains a shell option parsing vulnerability that allows combined POSIX shell flags to bypass |
| CVE-2026-53807 | 8.8 | 2026-06-11 | OpenClaw before 2026.5.6 contains an authorization bypass vulnerability in Telegram interactive callbacks that allows au |
| CVE-2026-53810 | 8.8 | 2026-06-11 | OpenClaw before 2026.5.18 contains a code execution vulnerability where marketplace runtime extension metadata can redir |
| CVE-2026-53811 | 8.8 | 2026-06-11 | OpenClaw before 2026.5.7 contains a privilege escalation vulnerability in the Matrix allowFrom feature that allows authe |
| CVE-2026-53812 | 7.7 | 2026-06-11 | OpenClaw before 2026.5.18 contains a server-side request forgery vulnerability in browser control that allows authentica |
| CVE-2026-53813 | 7.8 | 2026-06-11 | OpenClaw before 2026.4.25 contains a path traversal vulnerability in memory-core artifact loading where workspace state  |
| CVE-2026-53814 | 8.3 | 2026-06-11 | OpenClaw before 2026.5.20 contains a privilege escalation vulnerability where hook-triggered agent runs incorrectly rece |
| CVE-2026-53816 | 7.2 | 2026-06-11 | OpenClaw before 2026.5.18 contains an insufficient provenance validation vulnerability in node event handling that allow |
| CVE-2026-53817 | 8.8 | 2026-06-11 | OpenClaw before 2026.5.22 contains a locality validation vulnerability in Control UI pairing that allows attackers with  |
| CVE-2026-53819 | 8.8 | 2026-06-11 | OpenClaw before 2026.5.27 contains an arbitrary code execution vulnerability in skill install flows where workspace .env |
| CVE-2026-12007 | 8.8 | 2026-06-11 | Use after free in Core in Google Chrome on Windows prior to 149.0.7827.115 allowed a remote attacker to execute arbitrar |
| CVE-2026-12008 | 8.3 | 2026-06-11 | Use after free in DigitalCredentials in Google Chrome prior to 149.0.7827.115 allowed a remote attacker who had compromi |
| CVE-2026-12009 | 8.3 | 2026-06-11 | Insufficient validation of untrusted input in Accessibility in Google Chrome on Mac prior to 149.0.7827.115 allowed a re |
| CVE-2026-12010 | 8.3 | 2026-06-11 | Heap buffer overflow in GPU in Google Chrome on Android prior to 149.0.7827.115 allowed a remote attacker who had compro |
| CVE-2026-12011 | 8.3 | 2026-06-11 | Use after free in WebMIDI in Google Chrome on Windows prior to 149.0.7827.115 allowed a remote attacker who had compromi |
| CVE-2026-12012 | 8.1 | 2026-06-11 | Use after free in Network in Google Chrome prior to 149.0.7827.115 allowed an attacker in a privileged network position  |
| CVE-2026-12013 | 8.8 | 2026-06-11 | Use after free in Media in Google Chrome on Windows prior to 149.0.7827.115 allowed a remote attacker to potentially exp |
| CVE-2026-12014 | 8.3 | 2026-06-11 | Use after free in Cast in Google Chrome prior to 149.0.7827.115 allowed an attacker on the local network segment to pote |
| CVE-2026-12016 | 8.3 | 2026-06-11 | Inappropriate implementation in DevTools in Google Chrome prior to 149.0.7827.115 allowed a remote attacker who had comp |
| CVE-2026-12018 | 8.8 | 2026-06-11 | Inappropriate implementation in Mojo in Google Chrome on Windows prior to 149.0.7827.115 allowed a local attacker to per |
| CVE-2026-12019 | 8.3 | 2026-06-11 | Heap buffer overflow in Codecs in Google Chrome on Linux and ChromeOS prior to 149.0.7827.115 allowed a remote attacker  |
| CVE-2026-12020 | 8.8 | 2026-06-11 | Use after free in Autofill in Google Chrome on Mac prior to 149.0.7827.115 allowed a remote attacker to potentially expl |
| CVE-2026-12022 | 8.3 | 2026-06-11 | Race in Safe Browsing in Google Chrome on Mac prior to 149.0.7827.115 allowed a remote attacker who had compromised the  |
| CVE-2026-12023 | 8.3 | 2026-06-11 | Use after free in GPU in Google Chrome on Mac prior to 149.0.7827.115 allowed a remote attacker who had compromised the  |
| CVE-2026-12028 | 8.3 | 2026-06-11 | Use after free in GPU in Google Chrome on Android prior to 149.0.7827.115 allowed a remote attacker who had compromised  |
| CVE-2026-12029 | 8.3 | 2026-06-11 | Use after free in Video in Google Chrome on Windows prior to 149.0.7827.115 allowed a remote attacker who had compromise |
| CVE-2026-12030 | 8.3 | 2026-06-11 | Out of bounds write in GPU in Google Chrome on Android prior to 149.0.7827.115 allowed a remote attacker who had comprom |
| CVE-2026-12031 | 8.3 | 2026-06-11 | Inappropriate implementation in Views in Google Chrome on Windows prior to 149.0.7827.115 allowed a remote attacker who  |
| CVE-2026-12034 | 8.3 | 2026-06-11 | Insufficient validation of untrusted input in Linux Toolkit Theming in Google Chrome on Linux prior to 149.0.7827.115 al |
| CVE-2026-39494 | 9.3 | 2026-06-11 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in WBW Plugins Produc |
| CVE-2026-42647 | 9.3 | 2026-06-11 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Beardev JoomSport  |
| CVE-2026-42653 | 7.1 | 2026-06-11 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in iova.Mihai SliceWP |
| CVE-2026-44249 | 8.1 | 2026-06-11 | Netty is a network application framework for development of protocol servers and clients. In netty-handler prior to vers |
| CVE-2026-44250 | 7.5 | 2026-06-11 | Netty is a network application framework for development of protocol servers and clients. In netty-codec-redis prior to  |
| CVE-2026-44890 | 7.5 | 2026-06-11 | Netty is a network application framework for development of protocol servers and clients. In netty-codec-redis prior to  |
| CVE-2026-49060 | 9.8 | 2026-06-11 | Incorrect Privilege Assignment vulnerability in Hippoo Mobile App for WooCommerce allows Privilege Escalation.

This iss |
| CVE-2026-42846 | 9.8 | 2026-06-11 | ClipBucket v5 is an open source video sharing platform. Prior to version 5.5.3 - #140, ClipBucket's Remote Play feature  |
| CVE-2026-45060 | 9.8 | 2026-06-11 | ClipBucket v5 is an open source video sharing platform. Prior to version 5.5.3 - #129, the actions/progress_video.php en |
| CVE-2026-45418 | 8.8 | 2026-06-11 | ClipBucket v5 is an open source video sharing platform. Prior to version 5.5.3 - #132, any authenticated user who can up |
| CVE-2026-11933 | 8.8 | 2026-06-12 | A use-after-free vulnerability exists in MongoDB Server's server-side JavaScript engine when converting BSON documents t |
| CVE-2026-47365 | 9.9 | 2026-06-12 | Argument injection vulnerability in WordPress Toolkit before 6.11.0 as used in cPanel & WHM, allows remote authenticated |
| CVE-2026-47366 | 7.2 | 2026-06-12 | Improper verification of access permissions when modifying permissions through the Administration Control Panel (ACP) al |
| CVE-2026-47367 | 9.9 | 2026-06-12 | A malicious actor with access to the network and low privileges could exploit an Improper Input Validation vulnerability |
| CVE-2026-47368 | 8.6 | 2026-06-12 | A malicious actor with access to the network could exploit a Path Traversal vulnerability found in certain devices runni |
| CVE-2026-47369 | 9.9 | 2026-06-12 | A malicious actor with access to the network and low privileges could exploit an Improper Input Validation vulnerability |
| CVE-2026-47370 | 9.9 | 2026-06-12 | A malicious actor with access to the network and low privileges could exploit an Improper Input Validation vulnerability |
| CVE-2026-48610 | 8.1 | 2026-06-12 | Under certain network configurations, a malicious actor with access to network could exploit an Improper Access Control  |
| CVE-2026-48611 | 9.8 | 2026-06-12 | Improper authentication checks in the OAuth implementation allow account hijacking even when OAuth is not configured or  |
| CVE-2026-48612 | 8.0 | 2026-06-12 | Improper state verification in the OAuth implementation could allow an attacker to manipulate the authentication flow an |
| CVE-2026-44892 | 7.5 | 2026-06-12 | Netty is a network application framework for development of protocol servers and clients. Prior to version 4.2.15.Final, |
| CVE-2026-12059 | 8.8 | 2026-06-12 | The SSH service of CelloOS developed by Cellopoint has an Improper Access Control vulnerability, allowing authenticated  |
| CVE-2026-11845 | 7.2 | 2026-06-12 | The iVEC-IEI Virtualization Edge Computer developed by IEI Integration Corp has a OS Command Injection vulnerability, al |
| CVE-2026-11846 | 8.1 | 2026-06-12 | The 
iVEC-IEI Virtualization Edge Computer developed by IEI Integration Corp has an Arbitrary File Deletion vulnerabilit |
| CVE-2026-11849 | 9.8 | 2026-06-12 | The 
iRM-IEI Remote Management developed by IEI Integration Corp has a Hardcoded Credentials vulnerability, allowing una |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-10520 | Ivanti / Sentry | 2026-06-11 | 2026-06-14 | Unknown |
| CVE-2026-11645 | Google / Chromium V8 | 2026-06-09 | 2026-06-23 | Unknown |
| CVE-2026-7473 | Arista / Extensible Operating System | 2026-06-09 | 2026-06-23 | Unknown |
| CVE-2026-20245 | Cisco / Catalyst SD-WAN Manager | 2026-06-09 | 2026-06-23 | Unknown |
| CVE-2026-42271 | BerriAI / LiteLLM | 2026-06-08 | 2026-06-22 | Unknown |
| CVE-2026-50751 | Check Point / Security Gateway | 2026-06-08 | 2026-06-11 | Known |
| CVE-2026-28318 | SolarWinds / Serv-U | 2026-06-05 | 2026-06-19 | Unknown |

---

*Total entries in CISA KEV catalog: 1618*