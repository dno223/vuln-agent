# Vulnerability Intelligence Report

**Date:** 2026-11-07  
**Generated:** 2026-11-07T14:40:57Z  

---

## Executive Summary

Our environment faces critical exposure across multiple platforms. Ten high-severity CVEs have been identified, including a CVSS 9.8 unauthenticated SQL injection in Craft CMS and multiple additional injection and privilege escalation flaws. Most urgently, CVE-2026-19868 affecting SonicWall SonicOS SSLVPN is actively exploited in the wild and listed in CISA's Known Exploited Vulnerabilities catalog with a remediation deadline of November 20, 2026. Additional KEV entries for Apple and WordPress products signal an escalating threat environment requiring immediate prioritization and coordinated patch management.

---

## Risk Narrative

The organization faces a converging threat from actively exploited vulnerabilities and a broad set of high-severity flaws spanning web CMS platforms, VPN infrastructure, and system utilities. The CISA KEV designation for SonicWall SSLVPN confirms active exploitation by threat actors, posing immediate risk of network perimeter compromise. Craft CMS vulnerabilities expose databases to both authenticated and unauthenticated attackers, risking data theft and full application takeover. Usermin flaws enable remote file writes and command execution. Skyvern and Fluxbox vulnerabilities add further code execution risk. Collectively, these findings indicate significant exposure to ransomware, data exfiltration, and lateral movement if left unaddressed.

---

## Prioritized Action Items

1. Patch or mitigate CVE-2026-19868 (SonicWall SonicOS SSLVPN) immediately to meet the CISA KEV remediation deadline of November 20, 2026.
2. Apply emergency patches for CVE-2026-123488 (CVSS 9.8 unauthenticated SQL injection in Craft CMS) to prevent full database compromise without authentication.
3. Upgrade Craft CMS to versions 4.18.9 or 5.11.2 to simultaneously remediate CVE-2026-123489, CVE-2026-123490, and CVE-2026-123491 covering SQL injection and privilege escalation flaws.
4. Remediate KEV-listed vulnerabilities in Apple and WordPress products (CVE-2024-27834 and CVE-2026-119977) in accordance with CISA guidance.
5. Patch Usermin through 2.570 to address unauthenticated path traversal (CVE-2026-123621) and authenticated OS command injection (CVE-2026-123620) vulnerabilities.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-112340 | 8.2 | 2026-11-06 | Wazuh dashboard plugins from 4.9.0 before 4.14.9 contain an authorization bypass vulnerability that allows authenticated |
| CVE-2026-123487 | 7.5 | 2026-11-06 | Parse Server before 8.6.115 and 9.0.0 before 9.10.7-alpha.1 validates user email address format with a regular expressio |
| CVE-2026-123488 | 9.8 | 2026-11-06 | Craft CMS 4.0.0 before 4.18.9 and 5.0.0 before 5.11.2 contains an unauthenticated SQL injection vulnerability in the ele |
| CVE-2026-123489 | 7.1 | 2026-11-06 | Craft CMS 4.0.0 before 4.18.9 and 5.0.0 before 5.11.2 contains a blind SQL injection vulnerability because the sandbox-e |
| CVE-2026-123490 | 8.8 | 2026-11-06 | Craft CMS from 5.8.17 before 5.11.2 contains a privilege escalation vulnerability because getOwners() applies caller cri |
| CVE-2026-123491 | 8.2 | 2026-11-06 | Craft CMS 4.0.0 before 4.18.9 and 5.0.0 before 5.11.2 contains an SQL injection vulnerability in GraphQL eager-loading:  |
| CVE-2026-123620 | 7.5 | 2026-11-06 | Usermin through 2.570 contains an OS command injection vulnerability in the Read Mail module that allows authenticated u |
| CVE-2026-123621 | 8.8 | 2026-11-06 | Usermin through 2.570 contains a path traversal vulnerability in mailbox/detachall.cgi that allows remote unauthenticate |
| CVE-2026-123783 | 8.8 | 2026-11-06 | Skyvern through 1.0.56 contains a sandbox bypass vulnerability that allows authenticated users to execute code by recons |
| CVE-2026-123784 | 7.8 | 2026-11-06 | Fluxbox through 1.3.7 contains an OS command injection vulnerability in RootTheme::reconfigTheme() that allows attackers |
| CVE-2026-123786 | 8.5 | 2026-11-06 | Agenta before 0.122.5 contains a server-side request forgery vulnerability that allows workspace members with workflow e |
| CVE-2026-53980 | 8.1 | 2026-11-06 | Charmbracelet wish before 2.0.5 contains a path traversal vulnerability in the git middleware (charm.land/wish/v2) that  |
| CVE-2026-59105 | 9.8 | 2026-11-06 | Jumis (formerly Tildes Jumis) creates and uses a Microsoft SQL Server login named ##Tilde_JumisAdmin## whose password is |
| CVE-2026-87045 | 7.5 | 2026-11-06 | The HTTP/2 server in subsys/net/lib/http/http_server_http2.c clears the connection's stream binding at the start of ever |
| CVE-2026-123675 | 8.3 | 2026-11-06 | A flaw has been found in OpenBMB Internet of Agents up to 9d78e88e47160eb42ee1ee8538c05e1c2c47877a. This affects the fun |
| CVE-2026-58141 | 7.6 | 2026-11-06 | Dify before 1.15.0 contains a server-side request forgery vulnerability that allows any authenticated console user to by |
| CVE-2026-103985 | 7.1 | 2026-11-06 | FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.231, the profile form exposes the only_assigned_ti |
| CVE-2026-104656 | 7.3 | 2026-11-06 | Improper neutralization of input in the sessions grid in Progress Telerik Fiddler Everywhere 8.3.0 and earlier allows an |
| CVE-2026-104657 | 7.5 | 2026-11-06 | Missing integrity verification in the Progress Software Fiddler Download and Setup Skill on Linux, macOS, and Windows wh |
| CVE-2026-122193 | 9.9 | 2026-11-06 | OS command injection in the example SSM document provisioning script in Trusted Remote Execution (REX) before 2026-07-28 |
| CVE-2026-123831 | 9.6 | 2026-11-06 | In JetBrains CLion before 2026.2, 
2026.1.4 code execution was possible in Safe Mode via Meson project settings |
| CVE-2026-123832 | 9.6 | 2026-11-06 | In JetBrains CLion before 2026.2 code execution was possible in Safe Mode via JSON compilation database |
| CVE-2026-123834 | 7.5 | 2026-11-06 | In JetBrains Datalore before 2026.4 improper scope validation in database tasks allowed using another workspace's servic |
| CVE-2026-123836 | 8.8 | 2026-11-06 | In JetBrains Datalore before 2026.4 workspace collaborators could obtain the owner's SSH private key via Git backup |
| CVE-2026-123837 | 7.8 | 2026-11-06 | In JetBrains IntelliJ IDEA before 2026.3, 
2026.2.1 command injection was possible in untrusted projects via Tomcat run  |
| CVE-2026-123838 | 7.8 | 2026-11-06 | In JetBrains IntelliJ IDEA before 2026.3 code execution was possible in Safe Mode via UI Designer form file |
| CVE-2026-123841 | 7.8 | 2026-11-06 | In JetBrains IntelliJ IDEA before 2026.3 code execution was possible via symlinks in an imported settings archive |
| CVE-2026-123842 | 7.1 | 2026-11-06 | In JetBrains IntelliJ IDEA before 2026.3 arbitrary file write was possible via symlinks when extracting plugin archives |
| CVE-2026-123848 | 7.4 | 2026-11-06 | In JetBrains IntelliJ IDEA before 2026.3 host name verification was missing for server TLS certificates |
| CVE-2026-123849 | 7.0 | 2026-11-06 | In JetBrains IntelliJ IDEA before 2026.3 code execution was possible in untrusted projects via the Terraform File Watche |
| CVE-2026-123852 | 7.4 | 2026-11-06 | In JetBrains Junie GitHub Action before 1.8.0 code execution with workflow credentials was possible via fork updates |
| CVE-2026-123853 | 7.8 | 2026-11-06 | In JetBrains IntelliJ IDEA before 2026.3, 
2026.2.2 code execution was possible in Safe Mode via project-controlled JVM  |
| CVE-2026-123855 | 7.5 | 2026-11-06 | In JetBrains Toolbox App before 3.6.1 command injection was possible via enterprise configuration URLs |
| CVE-2026-123859 | 8.1 | 2026-11-06 | When identifier escaping is disabled through a non-default configuration, the write_pandas() data-loading functionality  |
| CVE-2026-123962 | 8.4 | 2026-11-06 | In FreedomBox before 26.15, unprivileged user accounts can read/write files for which they lack permissions by setting t |
| CVE-2026-62854 | 7.6 | 2026-11-06 | FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.225, a user who can edit a mailbox signature can c |
| CVE-2026-62856 | 7.7 | 2026-11-06 | FreeScout is a self-hosted help desk and shared mailbox application. Prior to version 1.8.226, the  polycast/receive  en |
| CVE-2026-85743 | 8.2 | 2026-11-06 | FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.230, multiple outbound paths in Helper::downloadRe |
| CVE-2026-102359 | 7.5 | 2026-11-06 | Kroki creates diagrams from textual descriptions. Prior to 0.31.2, the TikZ backend's tikz/tikz2svg guard used when KROK |
| CVE-2026-102650 | 7.5 | 2026-11-06 | Nuxt Content is the file-based CMS for Nuxt applications, powered by Markdown and Vue components. From 3.0.0 until 3.15. |
| CVE-2026-118670 | 8.8 | 2026-11-06 | OHIF Viewers is a zero-footprint DICOM viewer with shared extension packages. From 3.5.0-beta.0 until 3.12.15, 3.13.7, a |
| CVE-2026-62344 | 7.5 | 2026-11-06 | Wanderer is a self-hosted trail database for saving and sharing adventures. Prior to 0.19.3, the unauthenticated GET /ac |
| CVE-2026-85742 | 7.5 | 2026-11-06 | FreeScout is a self-hosted help desk and shared mailbox. Prior to 1.8.230, a pre-authenticated attacker can place HTML i |
| CVE-2026-89017 | 7.5 | 2026-11-06 | Skyline DataMiner BrokerGateway contains an embedded API key vulnerability that allows unauthenticated attackers to retr |
| CVE-2026-107154 | 8.8 | 2026-11-06 | A session validation vulnerability has been identified in the SonicOS management interface, which in specific conditions |
| CVE-2026-107155 | 8.8 | 2026-11-06 | A permissive cross-domain policy vulnerability has been identified in the SonicOS management interface, which in specifi |
| CVE-2026-119923 | 9.8 | 2026-11-06 | A heap-based buffer overflow in the TDS prelogin parser in the Babelfish for PostgreSQL extension versions 1.0-1.5, 2.1- |
| CVE-2026-119924 | 8.1 | 2026-11-06 | An out-of-bounds read in the TDS RPC procedure-name parser in the Babelfish for PostgreSQL extension versions 1.0-1.5, 2 |
| CVE-2026-123356 | 7.5 | 2026-11-06 | GROBID is machine learning software for extracting information from scholarly documents. Prior to 0.9.1, the unauthentic |
| CVE-2026-123993 | 8.8 | 2026-11-06 | Hisense VIDAA Smart TV firmware V0000.01.00a.P0220 contains an unauthenticated access vulnerability where a QA build of  |
| CVE-2026-123998 | 8.3 | 2026-11-06 | Hisense VIDAA Smart TV firmware V0000.01.00a.P0220 contains an authentication bypass vulnerability in its remote-control |
| CVE-2026-19868 | 7.5 | 2026-11-06 | An authentication enforcement vulnerability in SonicOS SSLVPN service may allow a user with valid credentials for an alt |
| CVE-2026-62345 | 7.6 | 2026-11-06 | Wanderer is a self-hosted trail database for saving and sharing adventures. Prior to 0.19.3, an authenticated user can s |
| CVE-2026-62346 | 7.6 | 2026-11-06 | Wanderer is a self-hosted trail database for saving and sharing adventures. Prior to 0.19.3, an authenticated local user |
| CVE-2026-71495 | 10.0 | 2026-11-06 | Wanderer is a self-hosted trail database for saving and sharing adventures. Prior to 0.20.0, when PUBLIC_PRIVATE_INSTANC |
| CVE-2026-82308 | 7.5 | 2026-11-06 | A pre-authentication heap-based buffer overflow vulnerability has been identified in the SonicOS SSL-VPN service, which  |
| CVE-2026-123974 | 7.8 | 2026-11-06 | In all versions of PyTorch's TorchServe, a predictable extraction directory in /tmp lets a local user swap the model han |
| CVE-2026-124027 | 7.5 | 2026-11-06 | ChatWiki before 2.10.0 contains a missing authentication vulnerability in the GET /manage/getLibRawFileOnePage route tha |
| CVE-2026-124040 | 8.1 | 2026-11-06 | CivetWeb through 1.16, when built with USE_HTTP2 and enable_http2 on, contains a use-after-free vulnerability in handle_ |
| CVE-2026-33050 | 8.8 | 2026-11-06 | GeoNode is a geospatial content management system, a platform for the management and publication of geospatial data. Pri |
| CVE-2026-58490 | 9.8 | 2026-11-06 | Tracecat is an open-source security automation platform for teams and AI agents. From version 0.37.0 until 1.0.0-beta.49 |
| CVE-2026-65960 | 8.8 | 2026-11-06 | Tetragon is an eBPF-based security observability and runtime enforcement project. Versions before 1.7.0 can use a Helm d |
| CVE-2026-102344 | 8.1 | 2026-11-06 | Lavish is the new editor for your HTML artifacts. Prior to 0.1.43, the lavish-axi loopback HTTP server did not authentic |
| CVE-2026-102657 | 7.5 | 2026-11-06 | esm.sh is a no-build content delivery network (CDN) for web development. Prior to server version 137_7, the documented w |
| CVE-2026-124078 | 7.5 | 2026-11-06 | plist.js (npm package 'plist') before 5.0.1 contains an uncontrolled resource consumption vulnerability in the binary pr |
| CVE-2026-54349 | 9.8 | 2026-11-06 | Chartbrew is an open-source web application that can connect directly to databases and APIs and use the data to create c |
| CVE-2026-63438 | 9.8 | 2026-11-06 | 2FAuth is a web app to manage Two-Factor Authentication (2FA) accounts and generate their security codes. Prior to 8.0.0 |
| CVE-2026-63439 | 9.8 | 2026-11-06 | 2FAuth is a web app to manage Two-Factor Authentication (2FA) accounts and generate their security codes. Prior to 8.0.0 |
| CVE-2026-85295 | 9.8 | 2026-11-06 | Chartbrew is an open-source web application that can connect directly to databases and APIs and use the data to create c |
| CVE-2026-85708 | 7.5 | 2026-11-06 | Chartbrew is an open-source web application that can connect directly to databases and APIs and use the data to create c |
| CVE-2026-85712 | 8.8 | 2026-11-06 | Chartbrew is an open-source web application that can connect directly to databases and APIs and use the data to create c |
| CVE-2026-85726 | 7.5 | 2026-11-06 | Chartbrew is an open-source web application that can connect directly to databases and APIs and use the data to create c |
| CVE-2026-85736 | 8.1 | 2026-11-06 | Chartbrew is an open-source web application that can connect directly to databases and APIs and use the data to create c |
| CVE-2026-86044 | 9.6 | 2026-11-06 | JupyterLab Desktop is the cross-platform desktop application for JupyterLab. Prior to 4.6.2-1, JupyterLab Desktop expose |
| CVE-2026-123791 | 7.3 | 2026-11-06 | A vulnerability was detected in OpenBMB Internet of Agents up to 9d78e88e47160eb42ee1ee8538c05e1c2c47877a. This affects  |
| CVE-2026-50240 | 8.8 | 2026-11-06 | A flaw was found in OpenShift Pipelines-as-Code (PAC). PAC does not verify whether the creator of a Repository custom re |
| CVE-2026-59104 | 9.8 | 2026-11-06 | UgCS server before 6.2 contains an authentication bypass in the HCI protocol login handler (LoginHandler) exposed on TCP |
| CVE-2026-68933 | 7.5 | 2026-11-06 | Chartbrew is an open-source web application that can connect directly to databases and APIs and use the data to create c |
| CVE-2026-68935 | 9.1 | 2026-11-06 | Chartbrew is an open-source web application for creating charts from databases and APIs. In versions 4.8.5 through 5.2.2 |
| CVE-2026-109469 | 10.0 | 2026-11-06 | Authorization bypass through user-controlled key in Entra Device Registration allows an unauthorized attacker to elevate |
| CVE-2026-104913 | 8.8 | 2026-11-07 | The Interactive Real Estate – Floor Plan & Building Visualizer plugin for WordPress is vulnerable to Arbitrary File Uplo |
| CVE-2026-119070 | 7.2 | 2026-11-07 | The Optimole – Optimize Images \| Convert WebP & AVIF \| CDN & Lazy Load \| Image Optimization plugin for WordPress is vuln |
| CVE-2026-119175 | 7.2 | 2026-11-07 | The Flying Images: Optimize and Lazy Load Images for Faster Page Speed plugin for WordPress is vulnerable to Stored Cros |
| CVE-2026-120082 | 7.2 | 2026-11-07 | The GeoDirectory – WP Business Directory Plugin and Classified Listings Directory plugin for WordPress is vulnerable to  |
| CVE-2026-120512 | 7.2 | 2026-11-07 | The Form Maker by 10Web – Mobile-Friendly Drag & Drop Contact Form Builder plugin for WordPress is vulnerable to Stored  |
| CVE-2026-120540 | 7.2 | 2026-11-07 | The iubenda \| All-in-one Compliance for GDPR / CCPA Cookie Consent + more plugin for WordPress is vulnerable to Stored C |
| CVE-2026-93754 | 9.8 | 2026-11-07 | The payever – WooCommerce Gateway plugin for WordPress is vulnerable to arbitrary file upload leading to remote code exe |
| CVE-2026-119158 | 7.2 | 2026-11-07 | The Pie Register – User Registration, Profiles & Content Restriction plugin for WordPress is vulnerable to Stored Cross- |
| CVE-2026-120677 | 7.2 | 2026-11-07 | The Optimole – Optimize Images \| Convert WebP & AVIF \| CDN & Lazy Load \| Image Optimization plugin for WordPress is vuln |
| CVE-2026-120739 | 7.2 | 2026-11-07 | The Optimole – Optimize Images \| Convert WebP & AVIF \| CDN & Lazy Load \| Image Optimization plugin for WordPress is vuln |
| CVE-2026-123218 | 9.8 | 2026-11-07 | IBM Aspera Faspex 5.0.0 through 5.0.19 could allow an authorized user to craft a specific message to bypass user authori |
| CVE-2026-17362 | 9.8 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to create, modify, or delete tenants due to miss |
| CVE-2026-19803 | 9.8 | 2026-11-07 | The Printcart Store – Web to Print Product Designer for WooCommerce plugin for WordPress is vulnerable to Arbitrary File |
| CVE-2026-105002 | 7.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow arbitrary code to be executed by th |
| CVE-2026-119167 | 7.2 | 2026-11-07 | The TranslatePress – Translate Multilingual sites with AI Translation plugin for WordPress is vulnerable to Stored Cross |
| CVE-2026-120043 | 7.5 | 2026-11-07 | The Affiliate Program Suite — SliceWP Affiliates plugin for WordPress is vulnerable to generic SQL Injection via the 'em |
| CVE-2026-16709 | 8.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-16712 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-16714 | 7.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to overwrite arbi |
| CVE-2026-16715 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-16716 | 8.8 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-16717 | 7.7 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information du |
| CVE-2026-16718 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-16720 | 9.8 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain valid a |
| CVE-2026-16854 | 7.7 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information be |
| CVE-2026-16880 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-16884 | 9.9 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information due to an XML ex |
| CVE-2026-16912 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-16918 | 9.3 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to access interna |
| CVE-2026-16920 | 9.9 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to bypass security restrictions du |
| CVE-2026-17049 | 9.9 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information an |
| CVE-2026-17066 | 9.1 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information an |
| CVE-2026-17108 | 8.5 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information du |
| CVE-2026-17112 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17117 | 9.9 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17129 | 7.6 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information an |
| CVE-2026-17131 | 9.3 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information due to server-si |
| CVE-2026-17132 | 9.9 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary SQL commands  |
| CVE-2026-17134 | 9.9 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary SQL commands  |
| CVE-2026-17146 | 9.9 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17147 | 9.9 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17150 | 9.9 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17158 | 9.9 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17172 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17187 | 8.5 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information du |
| CVE-2026-17188 | 8.5 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information du |
| CVE-2026-17190 | 8.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17228 | 8.5 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information du |
| CVE-2026-17239 | 9.9 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary code due to a |
| CVE-2026-17244 | 7.4 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17278 | 9.8 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to gain unauthorized access to sensitive API cat |
| CVE-2026-17279 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17280 | 8.9 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to perform unauth |
| CVE-2026-17281 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17282 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17283 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17284 | 7.1 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17285 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17287 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17288 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17289 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17290 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17291 | 8.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17292 | 9.1 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17293 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17294 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17295 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17296 | 9.6 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17297 | 9.6 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to perform an acc |
| CVE-2026-17298 | 9.9 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17299 | 9.6 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17301 | 9.8 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow an unauthenticated attacker to bypa |
| CVE-2026-17309 | 8.0 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information and tamper with  |
| CVE-2026-17311 | 7.1 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to modify application API subscrip |
| CVE-2026-17313 | 9.8 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information and take control |
| CVE-2026-17316 | 7.2 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to perform server-side request forgery due to im |
| CVE-2026-17318 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17319 | 7.1 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to modify tool configuration and c |
| CVE-2026-17320 | 7.7 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information du |
| CVE-2026-17321 | 8.1 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to delete or overwrite arbitrary c |
| CVE-2026-17322 | 7.1 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a local attacker to obtain sensitiv |
| CVE-2026-17323 | 8.2 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information due to XML exter |
| CVE-2026-17324 | 8.3 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to access sensitive configuration data and perfo |
| CVE-2026-17325 | 8.5 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information du |
| CVE-2026-17326 | 8.1 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17327 | 8.5 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information du |
| CVE-2026-17328 | 8.5 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information du |
| CVE-2026-17329 | 9.3 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information due to improper  |
| CVE-2026-17330 | 8.5 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information du |
| CVE-2026-17331 | 7.5 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to read arbitrary files on the server due to ext |
| CVE-2026-17332 | 8.7 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to bypass security restrictions due to improper  |
| CVE-2026-17333 | 8.0 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to bypass authent |
| CVE-2026-17334 | 8.5 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information du |
| CVE-2026-17335 | 8.8 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary code due to p |
| CVE-2026-17336 | 9.9 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to execute arbitrary SQL commands  |
| CVE-2026-17337 | 7.4 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to bypass authentication due to im |
| CVE-2026-17338 | 9.1 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information du |
| CVE-2026-17339 | 9.1 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to access or delete resources belo |
| CVE-2026-17340 | 9.8 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to execute arbitrary code due to a path traversa |
| CVE-2026-17341 | 7.2 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to perform server-side request forgery and relay |
| CVE-2026-17342 | 9.9 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17343 | 8.1 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to bypass authorization checks to  |
| CVE-2026-17344 | 9.3 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information due to server-si |
| CVE-2026-17345 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17352 | 8.5 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information du |
| CVE-2026-17353 | 9.6 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information an |
| CVE-2026-17354 | 9.9 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to perform arbitrary file writes d |
| CVE-2026-17355 | 8.2 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information fr |
| CVE-2026-17356 | 8.7 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a local attacker to obtain sensitive information due to the use of |
| CVE-2026-17357 | 7.6 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17358 | 8.2 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17359 | 9.9 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17360 | 9.8 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to gain full administrative control due to the u |
| CVE-2026-17361 | 7.7 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to obtain sensitive information du |
| CVE-2026-17363 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17365 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17373 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17374 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17375 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17376 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17378 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17379 | 7.4 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to bypass authent |
| CVE-2026-17380 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17381 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17382 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17383 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17384 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 could allow a remote authenticated attacker to obtain sensitive information d |
| CVE-2026-17385 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17386 | 8.1 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 could allow a remote attacker to gain full administrative control due to the  |
| CVE-2026-17387 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17388 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17392 | 9.9 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17394 | 9.6 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17396 | 9.6 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17397 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17398 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17399 | 9.9 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17400 | 7.7 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17401 | 7.2 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17402 | 9.9 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17403 | 9.0 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to gain full admi |
| CVE-2026-17404 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17405 | 8.8 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17406 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17407 | 8.5 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17408 | 9.8 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to execute arbitr |
| CVE-2026-17409 | 9.4 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to execute unauth |
| CVE-2026-17410 | 9.9 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote authenticated attacker to  |
| CVE-2026-17411 | 7.6 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow an authenticated attacker to view,  |
| CVE-2026-18535 | 9.6 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 are vulnerable to a Regular Expression Denial o |
| CVE-2026-18836 | 9.3 | 2026-11-07 | IBM API Connect 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensiti |
| CVE-2026-18838 | 9.4 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to obtain sensitive information and modify API c |
| CVE-2026-19121 | 8.3 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow an authenticated attacker to gain unauthorized access due to impro |
| CVE-2026-19128 | 7.5 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow an authenticated attacker to send unauthorized requests from the s |
| CVE-2026-75590 | 7.2 | 2026-11-07 | IBM API Connect 12.1.0.0 through 12.1.1.2 could allow a remote attacker to access internal network resources and obtain  |
| CVE-2026-115811 | 7.2 | 2026-11-07 | The Strong Testimonials plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'star_rating' paramete |
| CVE-2026-116558 | 7.2 | 2026-11-07 | The Unlimited Elements for Elementor plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the '<title>/ |
| CVE-2026-120537 | 7.2 | 2026-11-07 | The TranslatePress – Translate Multilingual sites with AI Translation plugin for WordPress is vulnerable to Stored Cross |
| CVE-2026-122037 | 7.2 | 2026-11-07 | The AgenWebsite Shipping – Plugin Ongkos Kirim & Generate Resi Otomatis Semua Kurir Indonesia plugin for WordPress is vu |
| CVE-2026-87112 | 8.8 | 2026-11-07 | The QA Assistants – Driven by data plugin for WordPress is vulnerable to PHP Object Injection in all versions up to, and |
| CVE-2026-123881 | 7.3 | 2026-11-07 | A vulnerability was found in OpenBMB Internet of Agents up to 9d78e88e47160eb42ee1ee8538c05e1c2c47877a. This issue affec |
| CVE-2026-104738 | 8.1 | 2026-11-07 | The Advanced Form Integration — Connect Forms to 300+ Apps plugin for WordPress is vulnerable to PHP Object Injection in |
| CVE-2026-123957 | 9.9 | 2026-11-07 | A vulnerability was determined in TOTOLINK CA300-PoE 6.2c.884. Impacted is the function setIpQosRules of the file /cgi-b |
| CVE-2026-123958 | 9.9 | 2026-11-07 | A vulnerability was identified in TOTOLINK CA300-PoE 6.2c.884. The affected element is the function setLanConfig of the  |
| CVE-2026-66669 | 8.8 | 2026-11-07 | Cross-Site Request Forgery (CSRF) vulnerability in Suplugins Superb Addons: Blocks, Patterns &amp; Theme Designer superb |
| CVE-2026-103900 | 8.1 | 2026-11-07 | The WPJAM Basic plugin for WordPress is vulnerable to Privilege Escalation in versions up to, and including, 7.1 This is |
| CVE-2026-107616 | 7.5 | 2026-11-07 | The Amelia plugin for WordPress is vulnerable to unauthorized access of attendee data due to a missing authorization che |
| CVE-2026-119155 | 7.5 | 2026-11-07 | The wpForo Forum plugin for WordPress is vulnerable to time-based SQL Injection via the 'href[locale]' parameter in all  |
| CVE-2026-119164 | 7.5 | 2026-11-07 | The wpForo Forum plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 3.2.2  |
| CVE-2026-121762 | 8.8 | 2026-11-07 | Cross-Site Request Forgery (CSRF) vulnerability in Blubrry Podcasting PowerPress Podcasting powerpress allows Cross Site |
| CVE-2026-123959 | 9.1 | 2026-11-07 | A security flaw has been discovered in TOTOLINK CA300-PoE 6.2c.884. The impacted element is the function setLanguageCfg  |
| CVE-2026-123960 | 9.9 | 2026-11-07 | A weakness has been identified in TOTOLINK CA300-PoE 6.2c.884. This affects the function setWanConfig of the file /cgi-b |
| CVE-2026-95870 | 7.5 | 2026-11-07 | The wpForo Forum plugin for WordPress is vulnerable to generic SQL Injection via the 'data' parameter in all versions up |
| CVE-2026-123961 | 9.9 | 2026-11-07 | A security vulnerability has been detected in TOTOLINK CA300-PoE 6.2c.884. This impacts the function setWiFiBasicConfig  |
| CVE-2026-104014 | 9.8 | 2026-11-07 | The Naimur Email OTP Verification for WooCommerce plugin for WordPress is vulnerable to authentication bypass in version |
| CVE-2026-104746 | 8.1 | 2026-11-07 | The Motors – Car Dealership & Classified Listings Plugin plugin for WordPress is vulnerable to arbitrary file deletion d |
| CVE-2026-104768 | 7.5 | 2026-11-07 | The AutomatorWP – No-Code Workflow Automation, Integration & Webhooks Plugin, now with AI plugin for WordPress is vulner |
| CVE-2026-109214 | 7.2 | 2026-11-07 | The User Frontend – Membership, User Registration, User Profile, User Directory & Content Restriction with Frontend Post |
| CVE-2026-109230 | 7.2 | 2026-11-07 | The WP Visitor Statistics (Real Time Traffic) plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the  |
| CVE-2026-109991 | 7.5 | 2026-11-07 | The FunnelKit Payment Gateway for Stripe WooCommerce plugin for WordPress is vulnerable to Insecure Direct Object Refere |
| CVE-2026-111317 | 7.2 | 2026-11-07 | The JetFormBuilder — Dynamic Blocks Form Builder plugin for WordPress is vulnerable to Stored Cross-Site Scripting via t |
| CVE-2026-111370 | 7.2 | 2026-11-07 | The WP Visitor Statistics (Real Time Traffic) plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the  |
| CVE-2026-115548 | 7.2 | 2026-11-07 | The Quttera ThreatSign – Web Malware Scanner for WordPress plugin for WordPress is vulnerable to Stored Cross-Site Scrip |
| CVE-2026-116537 | 7.2 | 2026-11-07 | The Link Library plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'link_description' parameter  |
| CVE-2026-116751 | 7.5 | 2026-11-07 | The Booking for Appointments and Events Calendar – Amelia Pro plugin for WordPress is vulnerable to time-based SQL Injec |
| CVE-2026-118066 | 9.1 | 2026-11-07 | The Appointment Booking Plugin – LatePoint \| Calendar & Scheduling for WordPress plugin for WordPress is vulnerable to A |
| CVE-2026-118267 | 8.1 | 2026-11-07 | The WP Data Access – App Builder for Tables, Forms, Dashboards, Charts & Maps plugin for WordPress is vulnerable to Inco |
| CVE-2026-119075 | 9.8 | 2026-11-07 | The Registration Form for WooCommerce plugin for WordPress is vulnerable to privilege escalation due to a missing allow- |
| CVE-2026-119183 | 7.2 | 2026-11-07 | The JetFormBuilder — Dynamic Blocks Form Builder plugin for WordPress is vulnerable to Stored Cross-Site Scripting via t |
| CVE-2026-121765 | 7.1 | 2026-11-07 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Cozmoslabs Transla |
| CVE-2026-122231 | 7.2 | 2026-11-07 | The WS Form LITE – Drag & Drop Contact Form Builder plugin for WordPress is vulnerable to Stored Cross-Site Scripting vi |
| CVE-2026-123418 | 7.2 | 2026-11-07 | The Church Admin plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'lat' parameter in all versio |
| CVE-2026-93429 | 7.2 | 2026-11-07 | The VikBooking Hotel Booking Engine & PMS plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'guests[ |
| CVE-2026-93755 | 7.2 | 2026-11-07 | The Happyforms plugin for WordPress is vulnerable to Stored Cross-Site Scripting via spoofable client IP headers in vers |
| CVE-2026-93766 | 7.2 | 2026-11-07 | The Happyforms Pro plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'happyforms_client_referer' |
| CVE-2026-119156 | 7.2 | 2026-11-07 | The Download Manager plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'wpdm_reg[first_name], wp |
| CVE-2026-120839 | 8.8 | 2026-11-07 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2026-120841 | 8.8 | 2026-11-07 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2026-122041 | 9.1 | 2026-11-07 | The Checkout Field Editor for WooCommerce (Pro) plugin for WordPress is vulnerable to unauthorized deletion of arbitrary |
| CVE-2026-123963 | 7.3 | 2026-11-07 | A security vulnerability has been detected in OpenBMB Internet of Agents up to 9d78e88e47160eb42ee1ee8538c05e1c2c47877a. |
| CVE-2026-120984 | 9.1 | 2026-11-07 | A flaw was found in the Keycloak server's client management component. When a client is created or imported with authori |
| CVE-2026-123966 | 10.0 | 2026-11-07 | A vulnerability was determined in Tenda AC19 16.03.10.07. Affected by this issue is the function saveParentControlInfo o |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-19868 | SonicWall / SonicOS SSLVPN | 2026-11-06 | 2026-11-20 | Unknown |
| CVE-2024-27834 | Apple / Multiple Products | 2026-11-04 | 2026-11-18 | Unknown |
| CVE-2026-119977 | WordPress / WordPress Core | 2026-11-03 | 2026-11-06 | Unknown |

---

*Total entries in CISA KEV catalog: 1769*