# Vulnerability Intelligence Report

**Date:** 2026-08-19  
**Generated:** 2026-08-19T08:35:13Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011CeBoPwW6NrPvv8By4ziCt'}

---

## Executive Summary

_No summary available._

---

## Risk Narrative

_No risk narrative available._

---

## Prioritized Action Items

_No action items available._

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-75626 | 9.3 | 2026-08-18 | SpiderFoot fails to HTML-escape correlation titles built from external scan data sources including server banners and me |
| CVE-2026-75627 | 9.8 | 2026-08-18 | Bastillion fails to properly validate request URI paths in its controller dispatcher, allowing unauthenticated attackers |
| CVE-2026-15585 | 7.5 | 2026-08-18 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in AKIN Software Computer I |
| CVE-2026-74902 | 8.6 | 2026-08-18 | SiYuan before v3.7.4 contains a cross-site scripting vulnerability in the file upload validation flow that fails to esca |
| CVE-2026-74904 | 7.5 | 2026-08-18 | SiYuan before v3.7.4 is missing authorization checks in 17 block metadata/content endpoints in kernel/api/block.go (incl |
| CVE-2026-74905 | 7.1 | 2026-08-18 | SiYuan before v3.7.4 contains a server-side request forgery (SSRF) vulnerability in the isPrivateIP function in kernel/u |
| CVE-2026-74906 | 7.5 | 2026-08-18 | SiYuan before v3.7.4 contains an incorrect authorization vulnerability in eight publish-mode reader-facing endpoints tha |
| CVE-2026-75827 | 8.8 | 2026-08-18 | Grav before 2.0.15 contains an arbitrary file write vulnerability in the Blueprint dynamic-data bare-function validation |
| CVE-2026-75828 | 8.7 | 2026-08-18 | Grav before 2.0.15 contains a stored cross-site scripting vulnerability in the detectXss() function where unpaired quote |
| CVE-2026-75829 | 8.1 | 2026-08-18 | grav-plugin-api versions before 1.0.15 fail to validate Twig content in the translate() endpoint, allowing attackers wit |
| CVE-2026-75830 | 7.1 | 2026-08-18 | grav-plugin-api (getgrav/grav-plugin-api) versions >= 1.0.0-beta.10 and <= 1.0.14 contain a path traversal vulnerability |
| CVE-2026-75831 | 7.6 | 2026-08-18 | Grav before 2.0.15 contains a stored cross-site scripting vulnerability in the audio and video media rendering through t |
| CVE-2026-75836 | 8.8 | 2026-08-18 | The Grav API plugin (getgrav/grav-plugin-api, bundled with Grav's admin-next/API stack) before 1.0.14 fails to enforce t |
| CVE-2026-75837 | 9.1 | 2026-08-18 | Grav before 2.0.14 fails to guard the access field in the core group blueprint with the required security@: admin.super  |
| CVE-2026-75840 | 7.5 | 2026-08-18 | ArcadeDB before 26.8.1 contains an arbitrary file read vulnerability in the GraalVM JavaScript sandbox allowlist enforce |
| CVE-2026-75842 | 7.7 | 2026-08-18 | ArcadeDB versions before 26.8.1 contain an arbitrary file read vulnerability in the OpenCypher LOAD CSV FROM clause that |
| CVE-2026-75843 | 9.9 | 2026-08-18 | ArcadeDB before 26.8.1 fails to bind the authenticated principal on the gRPC transaction executor thread in beginTransac |
| CVE-2026-75844 | 7.1 | 2026-08-18 | ArcadeDB versions before 26.8.1 contain a server-side request forgery vulnerability in the IMPORT DATABASE command where |
| CVE-2026-75846 | 7.1 | 2026-08-18 | ArcadeDB before 26.8.1 (affected versions <= 26.7.3) contains a missing authorization vulnerability in the DELETE FUNCTI |
| CVE-2026-75851 | 9.9 | 2026-08-18 | ArcadeDB server (com.arcadedb:arcadedb-server) in versions 26.7.3 and earlier fails to propagate the authenticated princ |
| CVE-2026-75852 | 9.8 | 2026-08-18 | ArcadeDB versions before 26.8.1 fail to enforce SASL authentication on data commands in the MongoDB wire-protocol plugin |
| CVE-2026-75853 | 8.8 | 2026-08-18 | ArcadeDB's Gremlin wire-protocol plugin (com.arcadedb:arcadedb-gremlin) in versions <= 26.7.3 enforces authentication (S |
| CVE-2026-75854 | 9.8 | 2026-08-18 | ArcadeDB versions before 26.8.1 contain a missing authentication vulnerability in the Redis wire-protocol plugin that al |
| CVE-2026-75855 | 8.7 | 2026-08-18 | ArcadeDB versions before 26.8.1 fail to sanitize database names in the POST /api/v1/server endpoint's create database an |
| CVE-2026-74935 | 8.8 | 2026-08-18 | Privilege escalation in the DOM: Networking component. This vulnerability was fixed in Firefox 154, Firefox ESR 115.39,  |
| CVE-2026-74937 | 8.8 | 2026-08-18 | Use-after-free in the JavaScript: GC component. This vulnerability was fixed in Firefox 154, Firefox ESR 153.1, Thunderb |
| CVE-2026-74938 | 9.1 | 2026-08-18 | Mitigation bypass in the JavaScript: GC component. This vulnerability was fixed in Firefox 154, Firefox ESR 153.1, Thund |
| CVE-2026-74939 | 8.8 | 2026-08-18 | Privilege escalation in the DOM: Navigation component. This vulnerability was fixed in Firefox 154, Firefox ESR 115.39,  |
| CVE-2026-74941 | 8.8 | 2026-08-18 | Privilege escalation in the Graphics: CanvasWebGL component. This vulnerability was fixed in Firefox 154, Firefox ESR 14 |
| CVE-2026-74942 | 8.8 | 2026-08-18 | Privilege escalation in the Remote Settings Client component. This vulnerability was fixed in Firefox 154, Firefox ESR 1 |
| CVE-2026-74946 | 8.8 | 2026-08-18 | Privilege escalation due to incorrect boundary conditions in the Graphics: CanvasWebGL component. This vulnerability was |
| CVE-2026-74947 | 8.8 | 2026-08-18 | Privilege escalation due to invalid pointer in the Graphics component. This vulnerability was fixed in Firefox 154, Fire |
| CVE-2026-74949 | 8.8 | 2026-08-18 | Privilege escalation due to use-after-free in the Graphics: Canvas2D component. This vulnerability was fixed in Firefox  |
| CVE-2026-74950 | 8.8 | 2026-08-18 | Privilege escalation in the Downloads API component. This vulnerability was fixed in Firefox 154, Firefox ESR 153.1, Thu |
| CVE-2026-74952 | 8.8 | 2026-08-18 | Privilege escalation in the Application Update component. This vulnerability was fixed in Firefox 154 and Thunderbird 15 |
| CVE-2026-74953 | 8.8 | 2026-08-18 | Privilege escalation in the Networking: Cookies component. This vulnerability was fixed in Firefox 154, Firefox ESR 140. |
| CVE-2026-74954 | 7.5 | 2026-08-18 | Information disclosure due to side-channel in the Storage: Cache API component. This vulnerability was fixed in Firefox  |
| CVE-2026-74955 | 8.8 | 2026-08-18 | Privilege escalation in the Request Handling component. This vulnerability was fixed in Firefox 154, Firefox ESR 153.1,  |
| CVE-2026-74956 | 9.1 | 2026-08-18 | Same-origin policy bypass in the DOM: Service Workers component. This vulnerability was fixed in Firefox 154, Firefox ES |
| CVE-2026-74958 | 7.5 | 2026-08-18 | Information disclosure in the WebRTC component. This vulnerability was fixed in Firefox 154, Firefox ESR 153.1, Thunderb |
| CVE-2026-74965 | 8.8 | 2026-08-18 | Privilege escalation in the Shell Integration component. This vulnerability was fixed in Firefox 154, Firefox ESR 140.14 |
| CVE-2026-74977 | 7.5 | 2026-08-18 | Integer overflow in the Graphics component. This vulnerability was fixed in Firefox 154, Firefox ESR 153.1, Thunderbird  |
| CVE-2026-74978 | 8.1 | 2026-08-18 | Clickjacking issue in the Widget component. This vulnerability was fixed in Firefox 154, Firefox ESR 153.1, Thunderbird  |
| CVE-2026-74979 | 9.8 | 2026-08-18 | Mitigation bypass in the Add-ons Manager component. This vulnerability was fixed in Firefox 154, Firefox ESR 153.1, Thun |
| CVE-2026-74990 | 9.8 | 2026-08-18 | Internally found bugs present in Thunderbird ESR 140.13, Thunderbird ESR 153.0 and Thunderbird 153. Some of these bugs s |
| CVE-2026-75778 | 7.3 | 2026-08-18 | A vulnerability was identified in code-projects Task Management System 1.0. This affects the function Operation::select_ |
| CVE-2026-75783 | 9.6 | 2026-08-18 | A security vulnerability has been detected in TRENDnet TEW-WLC100P 12.07b01. Affected by this vulnerability is an unknow |
| CVE-2026-75874 | 10.0 | 2026-08-18 | Sandbox escape in the Remote Settings Client component. This vulnerability was fixed in Firefox 154 and Thunderbird 154. |
| CVE-2026-24301 | 8.8 | 2026-08-18 | Improper neutralization of special elements used in a command ('command injection') in Microsoft Copilot allows an unaut |
| CVE-2026-28191 | 8.8 | 2026-08-18 | Subscriber Privilege Escalation in The Grid <= 2.7.9.1 versions. |
| CVE-2026-28192 | 9.6 | 2026-08-18 | Unauthenticated Arbitrary File Upload in Piotnet Addons For Elementor Pro <= 7.1.67 versions. |
| CVE-2026-28567 | 7.5 | 2026-08-18 | Unauthenticated Broken Access Control in WP Sort Order <= 1.3.5 versions. |
| CVE-2026-28568 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Quill Forms <= 5.7.1 versions. |
| CVE-2026-28569 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in SSL Zen <= 4.7.43 versions. |
| CVE-2026-28570 | 8.1 | 2026-08-18 | Unauthenticated Local File Inclusion in Vavo Core <= 2.3.0 versions. |
| CVE-2026-28571 | 7.5 | 2026-08-18 | Unauthenticated Broken Access Control in FormyChat <= 2.15.7 versions. |
| CVE-2026-32333 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Mayosis Core <= 5.4.7 versions. |
| CVE-2026-32444 | 9.9 | 2026-08-18 | Contributor Remote Code Execution (RCE) in Cwicly <= 1.4.4 versions. |
| CVE-2026-32463 | 9.9 | 2026-08-18 | Contributor Arbitrary File Upload in Sync Post With Other Site <= 1.9.3 versions. |
| CVE-2026-32464 | 8.1 | 2026-08-18 | Unauthenticated Local File Inclusion in Theme Test Drive <= 2.9.1 versions. |
| CVE-2026-32465 | 8.8 | 2026-08-18 | Customer PHP Object Injection in Essential Real Estate <= 5.3.3 versions. |
| CVE-2026-32466 | 8.5 | 2026-08-18 | Subscriber SQL Injection in Gravity Forms Bookings premium <= 2.1 versions. |
| CVE-2026-32468 | 7.5 | 2026-08-18 | Unauthenticated Sensitive Data Exposure in Duitku Payment Gateway <= 2.11.14 versions. |
| CVE-2026-50575 | 7.7 | 2026-08-18 | BetterDesk is a remote desktop management solution. BetterDesk versions through 2.3.0 improperly invalidate deleted devi |
| CVE-2026-18534 | 7.4 | 2026-08-18 | ArcSearch for iOS versions prior to 1.48.0 could keep the address bar hidden after a page-initiated scroll, allowing att |
| CVE-2026-32470 | 9.8 | 2026-08-18 | Unauthenticated PHP Object Injection in FundEngine <= 1.7.9 versions. |
| CVE-2026-32472 | 7.5 | 2026-08-18 | Unauthenticated Broken Access Control in Online Contact Widget <= 1.3.0 versions. |
| CVE-2026-32473 | 7.2 | 2026-08-18 | Unauthenticated Server Side Request Forgery (SSRF) in PDF Smart Viewer for Elementor <= 1.0.4 versions. |
| CVE-2026-32474 | 9.9 | 2026-08-18 | Contributor Arbitrary File Upload in Templatiq <= 0.2.5 versions. |
| CVE-2026-32481 | 7.5 | 2026-08-18 | Unauthenticated Broken Authentication in Ezoic <= 2.22.11 versions. |
| CVE-2026-32547 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in BP Better Messages <= 2.15.22 versions. |
| CVE-2026-32549 | 7.5 | 2026-08-18 | Unauthenticated Broken Access Control in ThumbPress < 6.5 versions. |
| CVE-2026-32553 | 7.2 | 2026-08-18 | Unauthenticated Server Side Request Forgery (SSRF) in OttoKit <= 1.1.35 versions. |
| CVE-2026-45733 | 8.3 | 2026-08-18 | Trilium Notes is a cross-platform, hierarchical note taking application focused on building large personal knowledge bas |
| CVE-2026-48798 | 7.1 | 2026-08-18 | SSH.NET is a Secure Shell (SSH) library for .NET. In 2025.1.0 and earlier, ScpClient.Download(string directoryName, Dire |
| CVE-2026-50138 | 8.1 | 2026-08-18 | goshs is a SimpleHTTPServer written in Go. Prior to version 2.1.0, when `goshs` is launched with WebDAV enabled (`-w`),  |
| CVE-2026-50187 | 8.8 | 2026-08-18 | Oh My Zsh is a community-driven framework for managing Zsh configuration. Prior to 2026-05-28, the dotenv plugin in plug |
| CVE-2026-56684 | 7.5 | 2026-08-18 | Valkey is a distributed key-value database. Prior to 7.2.14, 8.0.10, 8.1.9, 9.0.5, and 9.1.1, Valkey's tlsProcessPending |
| CVE-2026-59825 | 7.4 | 2026-08-18 | Mastodon is a free, open-source social network server based on ActivityPub. Prior to 4.4.19 and from 4.5.0 until 4.5.12, |
| CVE-2026-59940 | 9.8 | 2026-08-18 | Seroval facilitates JS value stringification, including complex structures beyond JSON.stringify capabilities. Prior to  |
| CVE-2026-61407 | 8.8 | 2026-08-18 | Dell Watchdog Timer Driver versions prior to 2.0.0.1 contain an Exposed IOCTL with Insufficient Access Control vulnerabi |
| CVE-2026-63639 | 8.8 | 2026-08-18 | Valkey is a distributed key-value database. Prior to 7.2.14, 8.0.10, 8.1.9, 9.0.5, and 9.1.1, Valkey's RESTORE command a |
| CVE-2026-66046 | 7.5 | 2026-08-18 | Expat through 2.8.3 contains a denial of service vulnerability caused by quadratic algorithmic complexity in the storeAt |
| CVE-2026-66620 | 7.2 | 2026-08-18 | Editor PHP Object Injection in OptionTree <= 2.7.3 versions. |
| CVE-2026-66621 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Ultimate Dashboard <= 3.11.2 versions. |
| CVE-2026-66622 | 7.5 | 2026-08-18 | Unauthenticated SQL Injection in Depicter Slider <= 4.8.0 versions. |
| CVE-2026-66627 | 9.9 | 2026-08-18 | Contributor Arbitrary File Upload in GP Premium <= 2.5.5 versions. |
| CVE-2026-66629 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Kirki <= 6.2.3 versions. |
| CVE-2026-66633 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Fluent Forms Pro Add On Pack < 6.2.12 versions. |
| CVE-2026-66635 | 7.4 | 2026-08-18 | Unauthenticated Cross Site Request Forgery (CSRF) in Slider by 10Web <= 1.2.62 versions. |
| CVE-2026-66667 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Templately <= 3.7.1 versions. |
| CVE-2026-66793 | 8.8 | 2026-08-18 | A flaw was found in the governance-policy-addon-controller component of Red Hat Advanced Cluster Management for Kubernet |
| CVE-2026-68567 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Convert Pro <= 1.0.1 versions. |
| CVE-2026-69189 | 7.6 | 2026-08-18 | Hoppscotch is an open source API development ecosystem. Prior to 2026.6.0, the team, teamMembers.user, RESTHistory, GQLH |
| CVE-2026-73181 | 7.5 | 2026-08-18 | Unauthenticated Arbitrary File Download in Extra Product Options & Add-Ons for WooCommerce < 7.6 versions. |
| CVE-2026-73187 | 9.3 | 2026-08-18 | Unauthenticated SQL Injection in Sticky Chat Widget <= 1.4.2 versions. |
| CVE-2026-73190 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in WPDM – Premium Packages <= 7.0.5 versions. |
| CVE-2026-73338 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Autopay <= 5.0.0 versions. |
| CVE-2026-73339 | 9.3 | 2026-08-18 | Unauthenticated SQL Injection in Modern Events Calendar < 7.35.0 versions. |
| CVE-2026-73341 | 9.8 | 2026-08-18 | Unauthenticated PHP Object Injection in RegistrationMagic <= 6.0.9.7 versions. |
| CVE-2026-73342 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in WP Multilang <= 2.4.31 versions. |
| CVE-2026-73343 | 10.0 | 2026-08-18 | Unauthenticated Remote Code Execution (RCE) in WP Compress < 7.20.01 versions. |
| CVE-2026-73345 | 7.1 | 2026-08-18 | Customer SQL Injection in License Manager for WooCommerce <= 3.0.18 versions. |
| CVE-2026-73350 | 8.2 | 2026-08-18 | Unauthenticated Broken Authentication in SupportCandy <= 3.5.1 versions. |
| CVE-2026-73351 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in WordPress Social Login and Register <= 7.8.1 versions. |
| CVE-2026-73355 | 9.3 | 2026-08-18 | Unauthenticated SQL Injection in Affiliates Manager <= 2.9.53 versions. |
| CVE-2026-73356 | 8.2 | 2026-08-18 | Unauthenticated Arbitrary Content Deletion in Breeze <= 2.5.12 versions. |
| CVE-2026-73358 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Affiliates Manager <= 2.9.53 versions. |
| CVE-2026-73360 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Chaty Pro <= 3.5.8 versions. |
| CVE-2026-73361 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Recipe Card Blocks for Gutenberg & Elementor <= 3.4.18 versions. |
| CVE-2026-73362 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in URL Shortify <= 2.5.0 versions. |
| CVE-2026-73365 | 9.3 | 2026-08-18 | Unauthenticated SQL Injection in JetAppointment <= 2.5.2 versions. |
| CVE-2026-73366 | 9.8 | 2026-08-18 | Unauthenticated PHP Object Injection in Easy Google Maps <= 1.13.0 versions. |
| CVE-2026-73367 | 7.2 | 2026-08-18 | Unauthenticated Remote File Inclusion in Easy Google Maps < 1.14.2 versions. |
| CVE-2026-73375 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Ultimate Maps by Supsystic < 1.5.0 versions. |
| CVE-2026-73376 | 9.8 | 2026-08-18 | Unauthenticated PHP Object Injection in Ultimate Maps by Supsystic < 1.5.0 versions. |
| CVE-2026-73377 | 7.5 | 2026-08-18 | Unauthenticated Broken Access Control in Ultimate Maps by Supsystic < 1.5.0 versions. |
| CVE-2026-73378 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Contact Form by Supsystic < 1.10.0 versions. |
| CVE-2026-73380 | 9.8 | 2026-08-18 | Unauthenticated PHP Object Injection in Popup by Supsystic <= 1.13.0 versions. |
| CVE-2026-73381 | 9.1 | 2026-08-18 | Unauthenticated Broken Authentication in Popup by Supsystic <= 1.13.0 versions. |
| CVE-2026-73382 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Site Reviews <= 8.2.0 versions. |
| CVE-2026-73392 | 9.3 | 2026-08-18 | Unauthenticated SQL Injection in Super Store Finder <= 7.8 versions. |
| CVE-2026-73393 | 7.1 | 2026-08-18 | Unauthenticated Cross Site Scripting (XSS) in Subscribe2 <= 10.46 versions. |
| CVE-2026-73396 | 7.1 | 2026-08-18 | Subscriber Broken Authentication in MWB HubSpot for WooCommerce <= 1.6.7 versions. |
| CVE-2026-73397 | 9.8 | 2026-08-18 | Unauthenticated Deserialization of untrusted data in Youzify <= 1.3.7 versions. |
| CVE-2026-73400 | 8.1 | 2026-08-18 | Unauthenticated Local File Inclusion in Restaurant Menu by MotoPress <= 2.4.11 versions. |
| CVE-2026-73994 | 7.5 | 2026-08-18 | Unauthenticated Broken Access Control in Charitable <= 1.8.11.3 versions. |
| CVE-2026-73996 | 9.8 | 2026-08-18 | Unauthenticated Arbitrary File Upload in Masteriyo - LMS <= 2.3.2 versions. |
| CVE-2026-73997 | 7.5 | 2026-08-18 | Unauthenticated Denial of Service Attack in Starter Templates by Kadence WP <= 2.3.3 versions. |
| CVE-2026-74012 | 8.8 | 2026-08-18 | Editor PHP Object Injection in TaxoPress <= 3.51.0 versions. |
| CVE-2026-74015 | 9.3 | 2026-08-18 | Unauthenticated SQL Injection in Readabler < 2.0.18 versions. |
| CVE-2026-75784 | 10.0 | 2026-08-18 | A vulnerability was detected in TRENDnet TEW-WLC100 1v2.07b01. Affected by this issue is the function FUN_0040da4c of th |
| CVE-2026-75898 | 8.5 | 2026-08-18 | RAGFlow before 0.26.3 contains a server-side request forgery vulnerability in the agent workflow "Invoke" component (age |
| CVE-2026-12564 | 9.6 | 2026-08-18 | A flaw was found in the AAP Controller's HashiCorp Vault credential plugin. The kubernetes_auth() function in awx_plugin |
| CVE-2026-19500 | 7.5 | 2026-08-18 | The Entries component in Brainstorm Force SureForms version, less than 2.1.3, does not enforce adequate limits on user-c |
| CVE-2026-45115 | 8.7 | 2026-08-18 | MyBB is free and open source forum software. Prior to 1.8.40, the Buddy/Ignore component does not sanitize usernames cor |
| CVE-2026-45116 | 8.7 | 2026-08-18 | MyBB is free and open source forum software. Prior to 1.8.40, the user datahandler does not properly validate checkbox a |
| CVE-2026-45117 | 9.8 | 2026-08-18 | MyBB is free and open source forum software. From 1.8.13 until 1.8.40, the installer module does not properly escape use |
| CVE-2026-45118 | 9.3 | 2026-08-18 | MyBB is free and open source forum software. Prior to 1.8.40, the Contact module does not validate a redirect URL or pro |
| CVE-2026-49221 | 8.8 | 2026-08-18 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to 1.0.8.4 |
| CVE-2026-49226 | 8.3 | 2026-08-18 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to 1.0.8.4 |
| CVE-2026-49227 | 7.6 | 2026-08-18 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to 1.0.8.4 |
| CVE-2026-55839 | 8.7 | 2026-08-18 | Kestra is an open-source, event-driven orchestration platform. Prior to 1.3.24, Kestra's custom Markdown parser in ui/sr |
| CVE-2026-71365 | 7.7 | 2026-08-18 | A server-side request forgery (SSRF) vulnerability was found in AWX's webhook status callback mechanism. When processing |
| CVE-2026-75856 | 8.6 | 2026-08-18 | CodeWhale before 0.8.64 contains a server-side request forgery bypass vulnerability in DNS pinning logic that fails to p |
| CVE-2026-75857 | 7.0 | 2026-08-18 | CodeWhale versions >= 0.8.41 and < 0.8.64 contain a vulnerability in the exec_shell_interact (alias exec_interact) tool, |
| CVE-2026-75858 | 7.8 | 2026-08-18 | CodeWhale (packages codewhale / codewhale-tui) versions >= 0.8.41 and < 0.8.64 contain a remote code execution vulnerabi |
| CVE-2026-75859 | 7.5 | 2026-08-18 | CodeWhale versions before 0.8.64 fail to validate file paths in the project config instructions field, allowing attacker |
| CVE-2026-75911 | 7.8 | 2026-08-18 | CodeWhale versions before 0.8.64 fail to properly validate the allow_shell configuration parameter from project config f |
| CVE-2026-75912 | 7.4 | 2026-08-18 | CodeWhale versions before 0.8.64 contain an argument injection vulnerability in the git_blame tool that allows attackers |
| CVE-2026-75913 | 9.3 | 2026-08-18 | CodeWhale (codewhale / codewhale-tui) versions >= 0.8.41 and < 0.8.64 contain an argument injection vulnerability in the |
| CVE-2026-75914 | 7.5 | 2026-08-18 | CodeWhale versions before 0.8.64 contain a path traversal vulnerability in the image_analyze tool that fails to canonica |
| CVE-2026-75915 | 7.5 | 2026-08-18 | CodeWhale versions before 0.8.64 contain an environment variable exposure vulnerability in the js_execution tool that fa |
| CVE-2026-75926 | 8.6 | 2026-08-18 | Hugo 0.161.0 placed the Node asset pipelines behind the Node.js permission model so that code running through PostCSS, B |
| CVE-2026-18963 | 9.1 | 2026-08-18 | A flaw was found in the reset-credentials flow of the keycloak-services component, which is the core engine for identity |
| CVE-2026-49222 | 7.6 | 2026-08-18 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to 1.0.8.4 |
| CVE-2026-49223 | 7.6 | 2026-08-18 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to 1.0.8.4 |
| CVE-2026-49224 | 8.3 | 2026-08-18 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to 1.0.8.4 |
| CVE-2026-49225 | 8.3 | 2026-08-18 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to 1.0.8.4 |
| CVE-2026-49228 | 8.8 | 2026-08-18 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to 1.0.8.4 |
| CVE-2026-50577 | 7.4 | 2026-08-18 | ePA 3.x Integration implements the authorization workflow and writes Medical Information Objects to Germany's electronic |
| CVE-2026-50578 | 7.5 | 2026-08-18 | ePA 3.x Integration implements the authorization workflow and writes Medical Information Objects to Germany's electronic |
| CVE-2026-52723 | 9.1 | 2026-08-18 | ePA 3.x Integration implements the authorization workflow and writes Medical Information Objects to Germany's electronic |
| CVE-2026-61574 | 8.8 | 2026-08-18 | authentik is an open-source identity provider. Prior to 2026.2.6 and 2026.5.5, the Remote Access Control endpoint list r |
| CVE-2026-66782 | 7.8 | 2026-08-18 | A flaw was found in the Submariner operator. This vulnerability allows for the exposure of a long-lived broker service a |
| CVE-2026-66783 | 8.2 | 2026-08-18 | A flaw was found in the `submariner-operator` component of Red Hat Advanced Cluster Management for Kubernetes. This vuln |
| CVE-2026-67271 | 9.8 | 2026-08-18 | Dell PowerStore SDNAS, contains an Out-of-bounds Write vulnerability in the SMB/CIFS. An unauthenticated attacker with r |
| CVE-2026-70415 | 8.1 | 2026-08-18 | Dell PowerStore SDNAS contains a Buffer Copy without Checking Size of Input vulnerability in the NFS/RPC. An unauthentic |
| CVE-2026-75897 | 7.5 | 2026-08-18 | Improper input validation in the capabilities route handler in OpenSearch Dashboards - the size of the request payload i |
| CVE-2026-75924 | 8.7 | 2026-08-18 | A flaw was found in managed-serviceaccount. A compromised addon-manager pod, due to its ClusterRole granting excessive p |
| CVE-2026-32657 | 7.3 | 2026-08-18 | Dell AppSync Version 4.6.0.0, Dell Metro Node Version 8.0.0, Dell UCC Edge Version 3.0.1, Dell VxRail Version 8.0.322, D |
| CVE-2026-44472 | 8.1 | 2026-08-18 | Saleor is an e-commerce platform. From 2.10.0rc1 until 3.21.67, 3.22.63, and 3.23.22, the account activation flow treats |
| CVE-2026-48508 | 8.8 | 2026-08-18 | Lemur manages TLS certificate creation. Prior to 1.9.1, StrictRolePermission and AuthorityCreatorPermission in lemur/aut |
| CVE-2026-50143 | 8.1 | 2026-08-18 | The Apify MCP server enables AI agents to extract data from websites using ready-made scrapers, crawlers, and automation |
| CVE-2026-54552 | 7.9 | 2026-08-18 | sh provides Python process launching. Prior to 2.2.4, the _uid option in sh.py performs an incomplete privilege drop on  |
| CVE-2026-66780 | 9.9 | 2026-08-18 | A flaw was found in the submariner-operator component. The `submariner-k8s-broker-cluster` Role, which is assigned to jo |
| CVE-2026-67262 | 8.1 | 2026-08-18 | Dell PowerStore contains a Missing Authorization vulnerability. An attacker with access to a mapped host could exploit t |
| CVE-2026-71551 | 7.8 | 2026-08-18 | Super Productivity is an advanced todo list app with integrated timeboxing and time tracking capabilities. Prior to 18.1 |
| CVE-2026-74038 | 7.1 | 2026-08-18 | Wazuh 4.0.0 before 4.14.6 contains a path traversal vulnerability that allows unauthenticated remote attackers to cause  |
| CVE-2026-75130 | 9.0 | 2026-08-18 | Context7 through 2.1.2 contains a prompt injection vulnerability that allows attackers to execute malicious instructions |
| CVE-2026-75625 | 9.0 | 2026-08-18 | Kraken agents fail to verify peer-to-peer downloaded blobs against their requested SHA-256 digest before committing to t |
| CVE-2025-9210 | 8.1 | 2026-08-18 | Missing signature validation in JSON Web Tokens in Otalio Ship Property Management System versions before 2.22.0 allows  |
| CVE-2026-24183 | 7.8 | 2026-08-18 | NVIDIA Cumulus Linux contains a vulnerability in the user management component, where an unprivileged user could use imp |
| CVE-2026-24184 | 7.5 | 2026-08-18 | NVIDIA Cumulus Linux contains a vulnerability in the Link Layer Discovery Protocol (LLDP) daemon component, where an una |
| CVE-2026-24185 | 7.1 | 2026-08-18 | NVIDIA NVOS for network switches contains a vulnerability in the secure shell (SSH) server configuration component while |
| CVE-2026-47627 | 9.8 | 2026-08-18 | NVIDIA Triton Inference Server for Linux contains a vulnerability where an attacker could cause path traversal. A succes |
| CVE-2026-47628 | 7.5 | 2026-08-18 | NVIDIA Triton Inference Server for Linux contains a vulnerability where an attacker could cause an allocation of resourc |
| CVE-2026-47629 | 7.5 | 2026-08-18 | NVIDIA Triton Inference Server for Linux contains a vulnerability where an attacker could cause improper input validatio |
| CVE-2026-55166 | 9.9 | 2026-08-18 | Lemur manages TLS certificate creation. Prior to 1.9.2, authenticated users could influence an ACME authority acme_url w |
| CVE-2026-47719 | 8.2 | 2026-08-18 | FUXA is a web-based Process Visualization (SCADA/HMI/Dashboard) software. Prior to 1.3.2, the DEVICE_WEBAPI_REQUEST and  |
| CVE-2026-52829 | 7.5 | 2026-08-18 | ZEBRA is a Zcash node written entirely in Rust. Prior to 4.5.0, an unauthenticated IPv4 peer can deterministically termi |
| CVE-2026-59915 | 7.3 | 2026-08-18 | Dell Alienware Command Center (AWCC), versions prior to 6.14.20.0, contain a Least Privilege Violation vulnerability. A  |
| CVE-2026-70666 | 7.4 | 2026-08-18 | Lemur manages TLS certificate creation. Prior to 1.9.3, an authority-role member could update acme_url through PUT /api/ |
| CVE-2026-71303 | 7.7 | 2026-08-18 | Lemur manages TLS certificate creation. Prior to 1.9.3, _validate_acme_url enforced ACME_DIRECTORY_HOST_ALLOWLIST when a |
| CVE-2026-71307 | 7.7 | 2026-08-18 | Lemur manages TLS certificate creation. Prior to 1.9.3, GET /api/1/destinations and GET /api/1/destinations/ relied only |
| CVE-2026-71308 | 8.1 | 2026-08-18 | Lemur manages TLS certificate creation. From 0.5.0 until 1.9.3, certificate create, upload, and edit requests accepted r |
| CVE-2026-71417 | 7.3 | 2026-08-18 | Lemur manages TLS certificate creation. Prior to 1.9.3, POST /api/1/certificates/upload allowed a non-read-only user to  |
| CVE-2026-75877 | 9.9 | 2026-08-18 | A flaw has been found in TRENDnet TV-IP751WIC 11.03.03. This vulnerability affects the function SystemNetworkChanged/Sys |
| CVE-2026-75935 | 7.5 | 2026-08-18 | Uncontrolled memory allocation in the binary Ion stream cursor in Amazon ion-java before 1.12.0 might allow remote actor |
| CVE-2026-75936 | 7.5 | 2026-08-18 | Improper handling of highly compressed data in the GZIP auto-decompression handler in Amazon ion-java before 1.12.0 migh |
| CVE-2026-15571 | 7.3 | 2026-08-18 | A flaw was found in the legacy client-initiated account-linking endpoint of Keycloak, a widely used open-source identity |
| CVE-2026-52793 | 8.1 | 2026-08-18 | Froxlor is open source server administration software. Prior to 2.3.7, the API authentication path in lib/Froxlor/Api/Fr |
| CVE-2026-54347 | 8.7 | 2026-08-18 | Froxlor is open source server administration software. Prior to 2.3.8, DNS TXT record content accepted by lib/Froxlor/Ap |
| CVE-2026-54348 | 7.2 | 2026-08-18 | Froxlor is open source server administration software. Prior to 2.3.8, the Admins.add and Admins.update endpoints in lib |
| CVE-2026-55426 | 7.8 | 2026-08-18 | linuxfabrik-lib provides Python modules for database access, caching, shell execution, and API integrations, and Linuxfa |
| CVE-2026-60391 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Reporting product of Oracle Hyperion (component: Server).   The supported |
| CVE-2026-60392 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Outside In Technology product of Oracle Fusion Middleware (component: Outside In PDF Export  |
| CVE-2026-60393 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Lifecycle Manageme |
| CVE-2026-60412 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Outside In Technology product of Oracle Fusion Middleware (component: Outside In Core).   Th |
| CVE-2026-60413 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Outside In Technology product of Oracle Fusion Middleware (component: Outside In Core).   Th |
| CVE-2026-60414 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Outside In Technology product of Oracle Fusion Middleware (component: Outside In Core).   Th |
| CVE-2026-60415 | 8.1 | 2026-08-18 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions t |
| CVE-2026-60590 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hospitality Simphony product of Oracle Food and Beverage Applications (component: POS).  Sup |
| CVE-2026-60591 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Hospitality Simphony product of Oracle Food and Beverage Applications (component: POS).  Sup |
| CVE-2026-60592 | 8.2 | 2026-08-18 | Vulnerability in the MySQL Cluster product of Oracle MySQL (component: Cluster: NDB Operator).  Supported versions that  |
| CVE-2026-60672 | 9.8 | 2026-08-18 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions t |
| CVE-2026-60679 | 7.5 | 2026-08-18 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions t |
| CVE-2026-60680 | 8.1 | 2026-08-18 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions t |
| CVE-2026-60693 | 7.1 | 2026-08-18 | Vulnerability in the Oracle General Ledger product of Oracle E-Business Suite (component: Internal Operations).  Support |
| CVE-2026-60696 | 9.8 | 2026-08-18 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions t |
| CVE-2026-60698 | 9.8 | 2026-08-18 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions t |
| CVE-2026-60699 | 8.6 | 2026-08-18 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions t |
| CVE-2026-60702 | 9.9 | 2026-08-18 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions t |
| CVE-2026-60707 | 8.7 | 2026-08-18 | Vulnerability in the Oracle Identity Manager product of Oracle Fusion Middleware (component: Security).  Supported versi |
| CVE-2026-60715 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Identity Manager product of Oracle Fusion Middleware (component: OIM Legacy UI).  Supported  |
| CVE-2026-60716 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Identity Manager product of Oracle Fusion Middleware (component: OIM Legacy UI).  Supported  |
| CVE-2026-60720 | 9.9 | 2026-08-18 | Vulnerability in the Oracle Identity Manager product of Oracle Fusion Middleware (component: OIM Legacy UI).  Supported  |
| CVE-2026-60721 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Identity Manager product of Oracle Fusion Middleware (component: OIM Legacy UI).  Supported  |
| CVE-2026-60722 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Identity Manager product of Oracle Fusion Middleware (component: OIM Legacy UI).  Supported  |
| CVE-2026-60726 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine).  Supp |
| CVE-2026-60727 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Identity Manager product of Oracle Fusion Middleware (component: OIM Legacy UI).  Supported  |
| CVE-2026-60728 | 9.1 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Portlet Services).  Support |
| CVE-2026-60729 | 8.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Composer).  Supported versi |
| CVE-2026-60730 | 9.9 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Composer).  Supported versi |
| CVE-2026-60731 | 8.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Composer).  Supported versi |
| CVE-2026-60733 | 7.7 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Composer).  Supported versi |
| CVE-2026-60737 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Web Services Manager product of Oracle Fusion Middleware (component: Web Services Security). |
| CVE-2026-60742 | 8.1 | 2026-08-18 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: PIA Core Technology).  S |
| CVE-2026-60748 | 7.6 | 2026-08-18 | Vulnerability in the Oracle General Ledger product of Oracle E-Business Suite (component: Internal Operations).  Support |
| CVE-2026-60751 | 8.8 | 2026-08-18 | Vulnerability in the Siebel Apps - Marketing product of Oracle Siebel CRM (component: Marketing).  Supported versions th |
| CVE-2026-60752 | 7.1 | 2026-08-18 | Vulnerability in the Siebel Apps - Marketing product of Oracle Siebel CRM (component: Marketing).  Supported versions th |
| CVE-2026-60753 | 7.8 | 2026-08-18 | Vulnerability in the Siebel CRM Deployment product of Oracle Siebel CRM (component: Installation).  Supported versions t |
| CVE-2026-60754 | 9.1 | 2026-08-18 | Vulnerability in the Siebel Apps - Marketing product of Oracle Siebel CRM (component: Marketing).  Supported versions th |
| CVE-2026-60757 | 8.1 | 2026-08-18 | Vulnerability in the Siebel CRM End User product of Oracle Siebel CRM (component: Search).  Supported versions that are  |
| CVE-2026-60758 | 8.5 | 2026-08-18 | Vulnerability in the Siebel Artificial Intelligence product of Oracle Siebel CRM (component: AI).  Supported versions th |
| CVE-2026-60759 | 7.4 | 2026-08-18 | Vulnerability in the Oracle Internet Procurement Connector product of Oracle E-Business Suite (component: Internal Opera |
| CVE-2026-60765 | 7.5 | 2026-08-18 | Vulnerability in the Siebel Apps - Marketing product of Oracle Siebel CRM (component: Marketing).  Supported versions th |
| CVE-2026-60766 | 7.4 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: REST).  Supported versions that are |
| CVE-2026-60767 | 8.8 | 2026-08-18 | Vulnerability in the Siebel Apps - Marketing product of Oracle Siebel CRM (component: Marketing).  Supported versions th |
| CVE-2026-60769 | 7.5 | 2026-08-18 | Vulnerability in the Oracle General Ledger product of Oracle E-Business Suite (component: Internal Operations).  Support |
| CVE-2026-60779 | 8.1 | 2026-08-18 | Vulnerability in the Siebel Apps - Marketing product of Oracle Siebel CRM (component: Marketing).  Supported versions th |
| CVE-2026-60781 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Payments product of Oracle E-Business Suite (component: File Transmission).  Supported versi |
| CVE-2026-60782 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Payments product of Oracle E-Business Suite (component: File Transmission).  Supported versi |
| CVE-2026-60791 | 8.1 | 2026-08-18 | Vulnerability in the Siebel CRM Deployment product of Oracle Siebel CRM (component: Application Interface).  Supported v |
| CVE-2026-60792 | 7.4 | 2026-08-18 | Vulnerability in the Siebel CRM Deployment product of Oracle Siebel CRM (component: Server Infrastructure).  Supported v |
| CVE-2026-60796 | 8.2 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: REST).  Supported versions that are |
| CVE-2026-60797 | 7.4 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: REST).  Supported versions that are |
| CVE-2026-60798 | 8.5 | 2026-08-18 | Vulnerability in the Siebel CRM Deployment product of Oracle Siebel CRM (component: Migration).  Supported versions that |
| CVE-2026-60803 | 7.4 | 2026-08-18 | Vulnerability in the Siebel Apps - Marketing product of Oracle Siebel CRM (component: Marketing).  Supported versions th |
| CVE-2026-60808 | 7.5 | 2026-08-18 | Vulnerability in the Siebel Apps - Marketing product of Oracle Siebel CRM (component: Email Marketing).  Supported versi |
| CVE-2026-60820 | 7.4 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: REST).  Supported versions that are |
| CVE-2026-60821 | 9.8 | 2026-08-18 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Business Interlink).  Su |
| CVE-2026-60822 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Enterprise Manager for Systems Infrastructure product of Oracle Enterprise Manager (componen |
| CVE-2026-60831 | 8.1 | 2026-08-18 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Integration Broker).  Su |
| CVE-2026-60841 | 8.5 | 2026-08-18 | Vulnerability in the Oracle Unified Directory product of Oracle Fusion Middleware (component: OUD Core).  Supported vers |
| CVE-2026-60849 | 8.5 | 2026-08-18 | Vulnerability in the Oracle Unified Directory product of Oracle Fusion Middleware (component: OUD Core).  Supported vers |
| CVE-2026-60850 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Unified Directory product of Oracle Fusion Middleware (component: OUD Core).  Supported vers |
| CVE-2026-60856 | 7.4 | 2026-08-18 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Install and Packaging).  |
| CVE-2026-60858 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-60860 | 8.7 | 2026-08-18 | Vulnerability in the Service Delivery Platform product of Oracle Fusion Middleware (component: Messaging Enabler).  Supp |
| CVE-2026-60861 | 9.6 | 2026-08-18 | Vulnerability in the Service Delivery Platform product of Oracle Fusion Middleware (component: Messaging Enabler).  Supp |
| CVE-2026-60873 | 7.2 | 2026-08-18 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Data Mover).  Supported  |
| CVE-2026-60879 | 8.8 | 2026-08-18 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Configuration Manager).  |
| CVE-2026-60883 | 7.2 | 2026-08-18 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: PeopleCode).  Supported  |
| CVE-2026-60889 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Unified Directory product of Oracle Fusion Middleware (component: OUD Core).  Supported vers |
| CVE-2026-60902 | 7.0 | 2026-08-18 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Tuxedo).  Supported vers |
| CVE-2026-60903 | 8.7 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60905 | 9.6 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60906 | 7.5 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60909 | 7.6 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60914 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Unified Directory product of Oracle Fusion Middleware (component: OUD Core).  Supported vers |
| CVE-2026-60915 | 7.4 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-60916 | 9.9 | 2026-08-18 | Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). |
| CVE-2026-60921 | 9.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). |
| CVE-2026-60928 | 8.4 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).   The sup |
| CVE-2026-60933 | 7.4 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60934 | 8.7 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60935 | 8.7 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60944 | 8.2 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60946 | 9.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). |
| CVE-2026-60947 | 9.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). |
| CVE-2026-60949 | 7.1 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60954 | 8.7 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60955 | 8.2 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60956 | 7.5 | 2026-08-18 | Vulnerability in the JD Edwards EnterpriseOne US Payroll product of Oracle JD Edwards (component: Payroll).   The suppor |
| CVE-2026-60958 | 9.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). |
| CVE-2026-60961 | 8.0 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60967 | 8.8 | 2026-08-18 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: nVision).  Supported ver |
| CVE-2026-60969 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Unified Directory product of Oracle Fusion Middleware (component: OUD Core).  Supported vers |
| CVE-2026-60970 | 9.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). |
| CVE-2026-60971 | 9.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Enterprise Capture product of Oracle Fusion Middleware (component: Client Bundle). |
| CVE-2026-60975 | 7.5 | 2026-08-18 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Security).  Supported ve |
| CVE-2026-60976 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Scripting product of Oracle E-Business Suite (component: Internal Operations).  Supported ve |
| CVE-2026-60977 | 9.8 | 2026-08-18 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: WLS Core Components).  Suppo |
| CVE-2026-60980 | 8.7 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60981 | 8.7 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60983 | 7.7 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-60990 | 9.9 | 2026-08-18 | Vulnerability in the Oracle Identity Manager Connector product of Oracle Fusion Middleware (component: Core).  Supported |
| CVE-2026-60991 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Identity Manager Connector product of Oracle Fusion Middleware (component: Core).  Supported |
| CVE-2026-60992 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Identity Manager Connector product of Oracle Fusion Middleware (component: Core).  Supported |
| CVE-2026-60993 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Identity Manager Connector product of Oracle Fusion Middleware (component: Core).  Supported |
| CVE-2026-60994 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Identity Manager Connector product of Oracle Fusion Middleware (component: Core).  Supported |
| CVE-2026-60995 | 9.9 | 2026-08-18 | Vulnerability in the Oracle Identity Manager Connector product of Oracle Fusion Middleware (component: Core).  Supported |
| CVE-2026-60996 | 8.7 | 2026-08-18 | Vulnerability in the Oracle Identity Manager Connector product of Oracle Fusion Middleware (component: Connectors and Co |
| CVE-2026-60998 | 8.0 | 2026-08-18 | Vulnerability in the Oracle Identity Manager Connector product of Oracle Fusion Middleware (component: Microsoft Active  |
| CVE-2026-61001 | 9.6 | 2026-08-18 | Vulnerability in the Oracle Web Services Manager product of Oracle Fusion Middleware (component: Web Services Security). |
| CVE-2026-61002 | 8.8 | 2026-08-18 | Vulnerability in the Oracle SOA Suite product of Oracle Fusion Middleware (component: B2B Engine).  Supported versions t |
| CVE-2026-61003 | 9.9 | 2026-08-18 | Vulnerability in the Oracle Managed File Transfer product of Oracle Fusion Middleware (component: MFT Runtime Server).   |
| CVE-2026-61007 | 7.5 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61008 | 9.1 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61011 | 8.2 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61016 | 8.2 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61017 | 8.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61018 | 9.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61021 | 9.9 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61022 | 8.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61029 | 9.0 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61032 | 8.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61033 | 8.6 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61034 | 9.1 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61038 | 8.2 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61040 | 8.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61042 | 8.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61045 | 8.6 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61054 | 8.2 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61058 | 8.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).  Supported |
| CVE-2026-61066 | 9.9 | 2026-08-18 | Vulnerability in the Oracle Identity Manager product of Oracle Fusion Middleware (component: OIM Legacy UI).  Supported  |
| CVE-2026-61118 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Identity Manager product of Oracle Fusion Middleware (component: OIM Legacy UI).  Supported  |
| CVE-2026-61124 | 7.1 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).  Supported  |
| CVE-2026-61177 | 8.1 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).  Supported  |
| CVE-2026-61193 | 8.7 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).  Supported  |
| CVE-2026-61199 | 7.7 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).   The suppo |
| CVE-2026-61206 | 9.9 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-61208 | 7.6 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).  Supported  |
| CVE-2026-61212 | 8.5 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).  Supported  |
| CVE-2026-61213 | 8.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).  Supported  |
| CVE-2026-61215 | 8.7 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).  Supported  |
| CVE-2026-61219 | 8.7 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).  Supported  |
| CVE-2026-61222 | 8.2 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).  Supported  |
| CVE-2026-61227 | 7.6 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).  Supported  |
| CVE-2026-61228 | 8.6 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).  Supported  |
| CVE-2026-61229 | 8.1 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).  Supported  |
| CVE-2026-61230 | 8.6 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).  Supported  |
| CVE-2026-61231 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Virtual Directory product of Oracle Fusion Middleware (component: Virtual Directory Server). |
| CVE-2026-61241 | 10.0 | 2026-08-18 | Vulnerability in the Oracle Internet Directory product of Oracle Fusion Middleware (component: OID LDAP Server).  Suppor |
| CVE-2026-61248 | 9.9 | 2026-08-18 | Vulnerability in the Oracle Internet Directory product of Oracle Fusion Middleware (component: OID LDAP Server).  Suppor |
| CVE-2026-61258 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Internet Directory product of Oracle Fusion Middleware (component: OID LDAP Server).  Suppor |
| CVE-2026-61259 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-61265 | 8.1 | 2026-08-18 | Vulnerability in the JD Edwards EnterpriseOne Orchestrator product of Oracle JD Edwards (component: E1 IOT Orchestrator  |
| CVE-2026-61268 | 8.1 | 2026-08-18 | Vulnerability in the JD Edwards EnterpriseOne Tools product of Oracle JD Edwards (component: Business Logic Infra SEC).  |
| CVE-2026-61270 | 8.1 | 2026-08-18 | Vulnerability in the JD Edwards EnterpriseOne Orchestrator product of Oracle JD Edwards (component: E1 IOT Orchestrator  |
| CVE-2026-61272 | 9.8 | 2026-08-18 | Vulnerability in the JD Edwards EnterpriseOne Tools product of Oracle JD Edwards (component: Web Runtime SEC).  Supporte |
| CVE-2026-61273 | 8.8 | 2026-08-18 | Vulnerability in the JD Edwards EnterpriseOne Tools product of Oracle JD Edwards (component: Installation Security).  Su |
| CVE-2026-61276 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-61281 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-61284 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Enterprise Manager Base Platform product of Oracle Enterprise Manager (component: Applicatio |
| CVE-2026-61286 | 8.6 | 2026-08-18 | Vulnerability in the Oracle Enterprise Manager Base Platform product of Oracle Enterprise Manager (component: Event Mana |
| CVE-2026-61288 | 7.1 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-61290 | 7.1 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-61291 | 7.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-61293 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-61295 | 7.1 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-61296 | 7.6 | 2026-08-18 | Vulnerability in the Oracle Enterprise Asset Management product of Oracle E-Business Suite (component: Linear Asset Mana |
| CVE-2026-61300 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Enterprise Manager Base Platform product of Oracle Enterprise Manager (component: Agent Next |
| CVE-2026-61302 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Pod Admin). |
| CVE-2026-61305 | 8.3 | 2026-08-18 | Vulnerability in the Oracle BI Publisher product of Oracle Analytics (component: BI Platform Security).  Supported versi |
| CVE-2026-61306 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Complex Maintenance, Repair and Overhaul product of Oracle E-Business Suite (component: Prod |
| CVE-2026-61307 | 8.1 | 2026-08-18 | Vulnerability in the PeopleSoft Enterprise CC Common Application Objects product of Oracle PeopleSoft (component: Common |
| CVE-2026-61317 | 9.9 | 2026-08-18 | Vulnerability in the Siebel CRM Cloud Applications product of Oracle Siebel CRM (component: Siebel Cloud Manager).  Supp |
| CVE-2026-61318 | 9.8 | 2026-08-18 | Vulnerability in the Siebel CRM Cloud Applications product of Oracle Siebel CRM (component: Siebel Cloud Manager).  Supp |
| CVE-2026-61319 | 8.8 | 2026-08-18 | Vulnerability in the Oracle U.S. Federal Financials product of Oracle E-Business Suite (component: Internal Operations). |
| CVE-2026-61321 | 8.1 | 2026-08-18 | Vulnerability in the Siebel CRM Cloud Applications product of Oracle Siebel CRM (component: Siebel Cloud Manager).  Supp |
| CVE-2026-61326 | 8.5 | 2026-08-18 | Vulnerability in the Siebel CRM Cloud Applications product of Oracle Siebel CRM (component: Siebel Cloud Manager).  Supp |
| CVE-2026-61330 | 8.8 | 2026-08-18 | Vulnerability in the Siebel CRM Cloud Applications product of Oracle Siebel CRM (component: Siebel Cloud Manager).  Supp |
| CVE-2026-61331 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Financials Common Modules product of Oracle E-Business Suite (component: Common Components). |
| CVE-2026-61332 | 8.7 | 2026-08-18 | Vulnerability in the Siebel CRM Cloud Applications product of Oracle Siebel CRM (component: Siebel Cloud Manager).  Supp |
| CVE-2026-61339 | 7.3 | 2026-08-18 | Vulnerability in the Siebel CRM Cloud Applications product of Oracle Siebel CRM (component: Siebel Cloud Manager).  Supp |
| CVE-2026-61340 | 8.2 | 2026-08-18 | Vulnerability in the Oracle MES for Process Manufacturing product of Oracle E-Business Suite (component: Internal Operat |
| CVE-2026-61341 | 8.8 | 2026-08-18 | Vulnerability in the Siebel CRM Cloud Applications product of Oracle Siebel CRM (component: Siebel Cloud Manager).  Supp |
| CVE-2026-62442 | 8.1 | 2026-08-18 | Vulnerability in the Siebel CRM Cloud Applications product of Oracle Siebel CRM (component: Siebel Cloud Manager).  Supp |
| CVE-2026-62448 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Email Center product of Oracle E-Business Suite (component: Message Component).  Supported v |
| CVE-2026-62449 | 7.0 | 2026-08-18 | Vulnerability in the Oracle Work in Process product of Oracle E-Business Suite (component: Internal Operations).  Suppor |
| CVE-2026-62450 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Flow Manufacturing product of Oracle E-Business Suite (component: Internal Operations).  Sup |
| CVE-2026-62452 | 9.9 | 2026-08-18 | Vulnerability in the Siebel CRM Cloud Applications product of Oracle Siebel CRM (component: Siebel Cloud Manager).  Supp |
| CVE-2026-62454 | 7.8 | 2026-08-18 | Vulnerability in the Siebel CRM Cloud Applications product of Oracle Siebel CRM (component: Siebel Cloud Manager).  Supp |
| CVE-2026-62455 | 8.3 | 2026-08-18 | Vulnerability in the Siebel CRM Cloud Applications product of Oracle Siebel CRM (component: Siebel Cloud Manager).  Supp |
| CVE-2026-62457 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Events).    |
| CVE-2026-62458 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Work in Process product of Oracle E-Business Suite (component: Internal Operations).  Suppor |
| CVE-2026-62459 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-62462 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Work in Process product of Oracle E-Business Suite (component: Internal Operations).  Suppor |
| CVE-2026-62463 | 9.6 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Lifecycle Manageme |
| CVE-2026-62467 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Events).    |
| CVE-2026-62471 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Events).    |
| CVE-2026-62477 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Security).  |
| CVE-2026-62481 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Events).    |
| CVE-2026-62485 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Events).    |
| CVE-2026-62491 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Purchasing product of Oracle E-Business Suite (component: Internal Operations).  Supported v |
| CVE-2026-62492 | 7.4 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Security).  |
| CVE-2026-62500 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Events).    |
| CVE-2026-62501 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Events).    |
| CVE-2026-62502 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Events).    |
| CVE-2026-62512 | 9.9 | 2026-08-18 | Vulnerability in the Siebel CRM Cloud Applications product of Oracle Siebel CRM (component: Siebel Cloud Manager).  Supp |
| CVE-2026-62522 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Security).  |
| CVE-2026-62531 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Lifecycle Manageme |
| CVE-2026-62535 | 8.6 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-62536 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-62537 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-62538 | 7.4 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-62539 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-62540 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Cost Management product of Oracle E-Business Suite (component: Cost Planning).  Supported ve |
| CVE-2026-62541 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-62543 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-62544 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-62545 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-62550 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-62551 | 7.3 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-62552 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-62554 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-62571 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-62581 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-62582 | 9.6 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-62585 | 9.8 | 2026-08-18 | Vulnerability in the Siebel CRM Administration product of Oracle Siebel CRM (component: Data Archival).  Supported versi |
| CVE-2026-62586 | 8.6 | 2026-08-18 | Vulnerability in the Siebel CRM Administration product of Oracle Siebel CRM (component: Data Archival).  Supported versi |
| CVE-2026-62587 | 7.1 | 2026-08-18 | Vulnerability in the Siebel CRM Administration product of Oracle Siebel CRM (component: Data Archival).  Supported versi |
| CVE-2026-62588 | 9.9 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: Open Integration).  Supported versi |
| CVE-2026-62589 | 8.7 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: Open Integration).  Supported versi |
| CVE-2026-62590 | 8.5 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: Open Integration).  Supported versi |
| CVE-2026-62591 | 8.1 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: Open Integration).  Supported versi |
| CVE-2026-62592 | 9.8 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: Open Integration).  Supported versi |
| CVE-2026-62593 | 7.7 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: Open Integration).  Supported versi |
| CVE-2026-62594 | 7.7 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: Open Integration).  Supported versi |
| CVE-2026-62595 | 8.1 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: Open Integration).  Supported versi |
| CVE-2026-62596 | 8.5 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: Open Integration).  Supported versi |
| CVE-2026-62598 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-62599 | 8.6 | 2026-08-18 | Vulnerability in the Oracle Trading Community product of Oracle E-Business Suite (component: Third Party Data Integratio |
| CVE-2026-62600 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Sales product of Oracle E-Business Suite (component: Internal Operations).  Supported versio |
| CVE-2026-62601 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Sales product of Oracle E-Business Suite (component: Internal Operations).  Supported versio |
| CVE-2026-62602 | 8.0 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-62605 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Partner Management product of Oracle E-Business Suite (component: Internal Operations).  Sup |
| CVE-2026-62607 | 8.7 | 2026-08-18 | Vulnerability in the Oracle Customer Care product of Oracle E-Business Suite (component: Internal Operations).  Supporte |
| CVE-2026-62608 | 9.9 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62609 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62610 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62611 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62612 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62613 | 9.3 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62614 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62615 | 8.5 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62616 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62617 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62618 | 9.3 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62619 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62620 | 8.6 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62621 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62622 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62623 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62624 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62625 | 8.6 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62626 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62627 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62628 | 8.6 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62629 | 9.4 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62630 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62631 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62632 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62633 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62634 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62635 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62636 | 8.6 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62637 | 9.3 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62638 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62639 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62640 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-62988 | 9.0 | 2026-08-18 | Froxlor is open source server administration software. From 2.3.7 until 2.3.8, the Customers.get, Customers.listing, Adm |
| CVE-2026-70668 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-70669 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-70670 | 9.6 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-70671 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-70672 | 7.4 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-70673 | 9.3 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-70674 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-70675 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Reports Developer product of Oracle Fusion Middleware (component: Security and Authenticatio |
| CVE-2026-70676 | 7.0 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-70678 | 7.6 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-70680 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Applications DBA product of Oracle E-Business Suite (component: Internal Operations).  Suppo |
| CVE-2026-70681 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Applications DBA product of Oracle E-Business Suite (component: JRI and other Java utils).   |
| CVE-2026-70684 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Enterprise Manager Base Platform product of Oracle Enterprise Manager (component: Agent Next |
| CVE-2026-70685 | 7.9 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-70686 | 8.8 | 2026-08-18 | Vulnerability in the Oracle General Ledger product of Oracle E-Business Suite (component: Internal Operations).  Support |
| CVE-2026-70687 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Marketing product of Oracle E-Business Suite (component: Audience).  Supported versions that |
| CVE-2026-70688 | 8.8 | 2026-08-18 | Vulnerability in Oracle Essbase (component: Calculator).   The supported version that is affected is 21.8.1.0.0. Easily  |
| CVE-2026-70689 | 9.8 | 2026-08-18 | Vulnerability in Oracle Essbase (component: Infrastructure).   The supported version that is affected is 21.8.1.0.0. Eas |
| CVE-2026-70690 | 8.0 | 2026-08-18 | Vulnerability in the Oracle HRMS (US) product of Oracle E-Business Suite (component: US Payroll - General).  Supported v |
| CVE-2026-70691 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Agile Engineering Data Management product of Oracle Supply Chain (component: Engineering Com |
| CVE-2026-70692 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Marketing Encyclopedia System product of Oracle E-Business Suite (component: Internal Operat |
| CVE-2026-70694 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Payments product of Oracle E-Business Suite (component: File Transmission).  Supported versi |
| CVE-2026-70695 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Payments product of Oracle E-Business Suite (component: File Transmission).  Supported versi |
| CVE-2026-70696 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Payments product of Oracle E-Business Suite (component: File Transmission).  Supported versi |
| CVE-2026-70697 | 7.0 | 2026-08-18 | Vulnerability in the Oracle Agile Engineering Data Management product of Oracle Supply Chain (component: Engineering Com |
| CVE-2026-70699 | 7.4 | 2026-08-18 | Vulnerability in the Oracle Payments product of Oracle E-Business Suite (component: File Transmission).  Supported versi |
| CVE-2026-70700 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Payables product of Oracle E-Business Suite (component: Internal Operations).  Supported ver |
| CVE-2026-70701 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Payables product of Oracle E-Business Suite (component: Internal Operations).  Supported ver |
| CVE-2026-70702 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Payments product of Oracle E-Business Suite (component: File Transmission).  Supported versi |
| CVE-2026-70703 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Agile Engineering Data Management product of Oracle Supply Chain (component: Engineering Com |
| CVE-2026-70704 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Trading Community product of Oracle E-Business Suite (component: Party Search UI).  Supporte |
| CVE-2026-70705 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Calculation Manager product of Oracle Hyperion (component: Security).   The support |
| CVE-2026-70706 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Sales product of Oracle E-Business Suite (component: Internal Operations).  Supported versio |
| CVE-2026-70707 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Sales for Handhelds product of Oracle E-Business Suite (component: Internal Operations).  Su |
| CVE-2026-70708 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Sales Foundation product of Oracle E-Business Suite (component: Security API).  Supported ve |
| CVE-2026-70710 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Sales Foundation product of Oracle E-Business Suite (component: Security API).  Supported ve |
| CVE-2026-70713 | 7.5 | 2026-08-18 | Vulnerability in the Oracle iSetup product of Oracle E-Business Suite (component: General Ledger Update Transform, Repor |
| CVE-2026-70715 | 8.8 | 2026-08-18 | Vulnerability in Oracle Autonomous Health Framework (component: Trace File Analyzer).  Supported versions that are affec |
| CVE-2026-70717 | 7.7 | 2026-08-18 | Vulnerability in Oracle Autonomous Health Framework (component: Cluster Health Analyzer).  Supported versions that are a |
| CVE-2026-70718 | 8.5 | 2026-08-18 | Vulnerability in the Oracle Bills of Material product of Oracle E-Business Suite (component: Internal Operations).  Supp |
| CVE-2026-70721 | 8.6 | 2026-08-18 | Vulnerability in the Oracle Hyperion Profitability and Cost Management product of Oracle Hyperion (component: Deployment |
| CVE-2026-70722 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Advanced Inbound Telephony product of Oracle E-Business Suite (component: Internal Operation |
| CVE-2026-70723 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Hyperion Profitability and Cost Management product of Oracle Hyperion (component: Deployment |
| CVE-2026-70724 | 7.5 | 2026-08-18 | Vulnerability in the MySQL Cluster product of Oracle MySQL (component: Cluster: General).  Supported versions that are a |
| CVE-2026-70725 | 7.6 | 2026-08-18 | Vulnerability in the Oracle Advanced Inbound Telephony product of Oracle E-Business Suite (component: Internal Operation |
| CVE-2026-70728 | 8.5 | 2026-08-18 | Vulnerability in Oracle Autonomous Health Framework (component: Trace File Analyzer).  Supported versions that are affec |
| CVE-2026-70729 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Teleservice product of Oracle E-Business Suite (component: Service Request Form).  Supported |
| CVE-2026-70730 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Profitability and Cost Management product of Oracle Hyperion (component: Deployment |
| CVE-2026-70731 | 8.4 | 2026-08-18 | Vulnerability in Oracle Autonomous Health Framework (component: Trace File Analyzer).  Supported versions that are affec |
| CVE-2026-70733 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Profitability and Cost Management product of Oracle Hyperion (component: Deployment |
| CVE-2026-70734 | 7.4 | 2026-08-18 | Vulnerability in Oracle Autonomous Health Framework (component: Trace File Analyzer).  Supported versions that are affec |
| CVE-2026-70735 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Profitability and Cost Management product of Oracle Hyperion (component: Deployment |
| CVE-2026-70736 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Profitability and Cost Management product of Oracle Hyperion (component: Deployment |
| CVE-2026-70737 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Enterprise Manager for Systems Infrastructure product of Oracle Enterprise Manager (componen |
| CVE-2026-70738 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Profitability and Cost Management product of Oracle Hyperion (component: Deployment |
| CVE-2026-70739 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Reporting product of Oracle Hyperion (component: Server).   The supported |
| CVE-2026-70740 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Reporting product of Oracle Hyperion (component: Server).   The supported |
| CVE-2026-70741 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Reporting product of Oracle Hyperion (component: Server).   The supported |
| CVE-2026-70742 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Reporting product of Oracle Hyperion (component: Server).   The supported |
| CVE-2026-70743 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Reporting product of Oracle Hyperion (component: Server).   The supported |
| CVE-2026-70744 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Reporting product of Oracle Hyperion (component: Server).   The supported |
| CVE-2026-70745 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Reporting product of Oracle Hyperion (component: Server).   The supported |
| CVE-2026-70746 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Reporting product of Oracle Hyperion (component: Server).   The supported |
| CVE-2026-70747 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Customers Online product of Oracle E-Business Suite (component: Customer Tab).  Supported ve |
| CVE-2026-70749 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Reporting product of Oracle Hyperion (component: Server).   The supported |
| CVE-2026-70750 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Reporting product of Oracle Hyperion (component: Server).   The supported |
| CVE-2026-70752 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Reporting product of Oracle Hyperion (component: Server).   The supported |
| CVE-2026-70760 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Order Management product of Oracle E-Business Suite (component: Product Diagnostic Tools).   |
| CVE-2026-70761 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Risk Management product of Oracle E-Business Suite (component: Internal Operations).  Suppor |
| CVE-2026-70762 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Risk Management product of Oracle E-Business Suite (component: Internal Operations).  Suppor |
| CVE-2026-70763 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Operations Intelligence product of Oracle E-Business Suite (component: Daily Business Intell |
| CVE-2026-70764 | 7.6 | 2026-08-18 | Vulnerability in the Oracle General Ledger product of Oracle E-Business Suite (component: Internal Operations).  Support |
| CVE-2026-70770 | 8.3 | 2026-08-18 | Vulnerability in the Oracle Warehouse Management product of Oracle E-Business Suite (component: Internal Operations).  S |
| CVE-2026-70771 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Warehouse Management product of Oracle E-Business Suite (component: Internal Operations).  S |
| CVE-2026-70772 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Warehouse Management product of Oracle E-Business Suite (component: Internal Operations).  S |
| CVE-2026-70773 | 8.2 | 2026-08-18 | Vulnerability in the Oracle HCM Common Architecture product of Oracle E-Business Suite (component: Knowledge Integration |
| CVE-2026-70774 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Warehouse Management product of Oracle E-Business Suite (component: Internal Operations).  S |
| CVE-2026-70777 | 7.5 | 2026-08-18 | Vulnerability in the Oracle iSupplier Portal product of Oracle E-Business Suite (component: Internal Operations).  Suppo |
| CVE-2026-70778 | 8.7 | 2026-08-18 | Vulnerability in the Oracle Customer Care product of Oracle E-Business Suite (component: Internal Operations).  Supporte |
| CVE-2026-70779 | 7.4 | 2026-08-18 | Vulnerability in the Oracle iSupplier Portal product of Oracle E-Business Suite (component: Internal Operations).  Suppo |
| CVE-2026-70781 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Proposals product of Oracle E-Business Suite (component: Internal Operations).  Supported ve |
| CVE-2026-70782 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Labor Distribution product of Oracle E-Business Suite (component: Internal Operations).  Sup |
| CVE-2026-70783 | 7.4 | 2026-08-18 | Vulnerability in the Oracle Service Contracts product of Oracle E-Business Suite (component: Internal Operations).  Supp |
| CVE-2026-70786 | 7.6 | 2026-08-18 | Vulnerability in the Oracle Service Fulfillment Manager product of Oracle E-Business Suite (component: Fulfillment Engin |
| CVE-2026-70787 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Reporting product of Oracle Hyperion (component: Server).   The supported |
| CVE-2026-70790 | 7.4 | 2026-08-18 | Vulnerability in the Oracle Telecommunications Billing Integrator product of Oracle E-Business Suite (component: Interna |
| CVE-2026-70791 | 7.6 | 2026-08-18 | Vulnerability in the Oracle Transportation Execution product of Oracle E-Business Suite (component: Internal Operations) |
| CVE-2026-70792 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Yard Management product of Oracle E-Business Suite (component: Internal Operations).  Suppor |
| CVE-2026-70795 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Applications Platform Engineering product of Oracle E-Business Suite (component: Valid Sessi |
| CVE-2026-70796 | 7.2 | 2026-08-18 | Vulnerability in the Oracle General Ledger product of Oracle E-Business Suite (component: Internal Operations).  Support |
| CVE-2026-70797 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Purchasing product of Oracle E-Business Suite (component: Internal Operations).  Supported v |
| CVE-2026-70798 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Purchasing product of Oracle E-Business Suite (component: Internal Operations).  Supported v |
| CVE-2026-70799 | 7.5 | 2026-08-18 | Vulnerability in the Oracle SDP Number Portability product of Oracle E-Business Suite (component: Internal Operations).  |
| CVE-2026-70800 | 7.3 | 2026-08-18 | Vulnerability in the Oracle SDP Number Portability product of Oracle E-Business Suite (component: Internal Operations).  |
| CVE-2026-70801 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Flow Manufacturing product of Oracle E-Business Suite (component: Internal Operations).  Sup |
| CVE-2026-70802 | 8.0 | 2026-08-18 | Vulnerability in the Oracle Public Sector Human Resources product of Oracle E-Business Suite (component: Regression Test |
| CVE-2026-70803 | 7.6 | 2026-08-18 | Vulnerability in the Oracle General Ledger product of Oracle E-Business Suite (component: Internal Operations).  Support |
| CVE-2026-70804 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Public Sector Human Resources product of Oracle E-Business Suite (component: Regression Test |
| CVE-2026-70805 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Project Planning and Control product of Oracle E-Business Suite (component: Change Managemen |
| CVE-2026-70806 | 7.1 | 2026-08-18 | Vulnerability in the Oracle E-Business Tax product of Oracle E-Business Suite (component: Internal Operations).  Support |
| CVE-2026-70807 | 8.5 | 2026-08-18 | Vulnerability in the Oracle Call Center Technology product of Oracle E-Business Suite (component: Internal Operations).  |
| CVE-2026-70808 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Scripting product of Oracle E-Business Suite (component: Internal Operations).  Supported ve |
| CVE-2026-70809 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Scripting product of Oracle E-Business Suite (component: Internal Operations).  Supported ve |
| CVE-2026-70810 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Scripting product of Oracle E-Business Suite (component: Internal Operations).  Supported ve |
| CVE-2026-70811 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Purchasing product of Oracle E-Business Suite (component: Internal Operations).  Supported v |
| CVE-2026-70812 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Call Center Technology product of Oracle E-Business Suite (component: Internal Operations).  |
| CVE-2026-70813 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Call Center Technology product of Oracle E-Business Suite (component: Internal Operations).  |
| CVE-2026-70814 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Call Center Technology product of Oracle E-Business Suite (component: Internal Operations).  |
| CVE-2026-70815 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Internet Procurement Connector product of Oracle E-Business Suite (component: Internal Opera |
| CVE-2026-70816 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Financials for EMEA product of Oracle E-Business Suite (component: Internal Operations).  Su |
| CVE-2026-70817 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70818 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70819 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70820 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Call Center Technology product of Oracle E-Business Suite (component: Internal Operations).  |
| CVE-2026-70821 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70822 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70823 | 7.4 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70827 | 7.7 | 2026-08-18 | Vulnerability in the Oracle MES for Process Manufacturing product of Oracle E-Business Suite (component: Internal Operat |
| CVE-2026-70828 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70829 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Process Manufacturing Systems product of Oracle E-Business Suite (component: Internal Operat |
| CVE-2026-70830 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Process Manufacturing Systems product of Oracle E-Business Suite (component: Internal Operat |
| CVE-2026-70832 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70833 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Landed Cost Management product of Oracle E-Business Suite (component: Internal Operations).  |
| CVE-2026-70834 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70835 | 8.1 | 2026-08-18 | Vulnerability in the Oracle iRecruitment product of Oracle E-Business Suite (component: Internal Operations).  Supported |
| CVE-2026-70837 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Financials for Asia/Pacific product of Oracle E-Business Suite (component: Internal Operatio |
| CVE-2026-70839 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Financials for EMEA product of Oracle E-Business Suite (component: Internal Operations).  Su |
| CVE-2026-70840 | 8.4 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70842 | 8.4 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70844 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Loans product of Oracle E-Business Suite (component: Internal Operations).  Supported versio |
| CVE-2026-70845 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Loans product of Oracle E-Business Suite (component: Internal Operations).  Supported versio |
| CVE-2026-70846 | 9.6 | 2026-08-18 | Vulnerability in the Oracle Demand Planning product of Oracle Supply Chain (component: Internal Operations).  Supported  |
| CVE-2026-70852 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Demand Planning product of Oracle Supply Chain (component: Internal Operations).  Supported  |
| CVE-2026-70854 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70855 | 9.3 | 2026-08-18 | Vulnerability in the Siebel Apps - Self Service product of Oracle Siebel CRM (component: Helpdesk/Training).  Supported  |
| CVE-2026-70856 | 7.5 | 2026-08-18 | Vulnerability in the Siebel CRM Deployment product of Oracle Siebel CRM (component: Migration).  Supported versions that |
| CVE-2026-70857 | 7.7 | 2026-08-18 | Vulnerability in the Siebel CRM End User product of Oracle Siebel CRM (component: Open UI).  Supported versions that are |
| CVE-2026-70858 | 7.1 | 2026-08-18 | Vulnerability in the Oracle WebCenter Content product of Oracle Fusion Middleware (component: Content Server).  Supporte |
| CVE-2026-70859 | 8.5 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: REST).  Supported versions that are |
| CVE-2026-70861 | 7.2 | 2026-08-18 | Vulnerability in the PeopleSoft Enterprise FIN Common Objects Brazil product of Oracle PeopleSoft (component: Common Obj |
| CVE-2026-70862 | 9.1 | 2026-08-18 | Vulnerability in Oracle Application Testing Suite.   The supported version that is affected is 13.3.0.1. Easily exploita |
| CVE-2026-70863 | 8.8 | 2026-08-18 | Vulnerability in Oracle Application Testing Suite.   The supported version that is affected is 13.3.0.1. Easily exploita |
| CVE-2026-70864 | 7.6 | 2026-08-18 | Vulnerability in Oracle Application Testing Suite.   The supported version that is affected is 13.3.0.1. Easily exploita |
| CVE-2026-70865 | 7.5 | 2026-08-18 | Vulnerability in Oracle Application Testing Suite.   The supported version that is affected is 13.3.0.1. Difficult to ex |
| CVE-2026-70866 | 7.8 | 2026-08-18 | Vulnerability in Oracle Application Testing Suite.   The supported version that is affected is 13.3.0.1. Easily exploita |
| CVE-2026-70867 | 7.1 | 2026-08-18 | Vulnerability in Oracle Application Testing Suite.   The supported version that is affected is 13.3.0.1. Easily exploita |
| CVE-2026-70868 | 8.1 | 2026-08-18 | Vulnerability in Oracle Application Testing Suite.   The supported version that is affected is 13.3.0.1. Difficult to ex |
| CVE-2026-70870 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Web Client - Un |
| CVE-2026-70871 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70872 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70873 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70874 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70875 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70876 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70877 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70878 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70879 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70880 | 10.0 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70881 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70882 | 8.7 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70883 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70884 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70885 | 8.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70886 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70887 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70889 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70890 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70891 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70892 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70893 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70894 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70896 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70897 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70898 | 7.4 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70899 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70900 | 8.7 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70901 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70902 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70903 | 8.7 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70904 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Data Relationship Management product of Oracle Hyperion (component: Access and secu |
| CVE-2026-70905 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Agent infrastructure).  Suppo |
| CVE-2026-70906 | 7.5 | 2026-08-18 | Vulnerability in Oracle Java SE (component: 2D).  Supported versions that are affected are Oracle Java SE: 25.0.4 and  2 |
| CVE-2026-70908 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-70909 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70910 | 7.5 | 2026-08-18 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: REST).  Supported versions that are |
| CVE-2026-70914 | 7.0 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70918 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Product Hub product of Oracle E-Business Suite (component: Outbound Data).  Supported versio |
| CVE-2026-70920 | 9.9 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70921 | 10.0 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70922 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Financial Services Enterprise Case Management product of Oracle Financial Services Applicati |
| CVE-2026-70924 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Web Services Manager product of Oracle Fusion Middleware (component: Web Services Security). |
| CVE-2026-70925 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70926 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Workflow product of Oracle E-Business Suite (component: Workflow Notification Mailer).  Supp |
| CVE-2026-70927 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Workflow product of Oracle E-Business Suite (component: Workflow Notification Mailer).  Supp |
| CVE-2026-70928 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70929 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70930 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Order Management product of Oracle E-Business Suite (component: Product Diagnostic Tools).   |
| CVE-2026-70931 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Workflow product of Oracle E-Business Suite (component: Workflow Notification Mailer).  Supp |
| CVE-2026-70932 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Order Management product of Oracle E-Business Suite (component: Product Diagnostic Tools).   |
| CVE-2026-70933 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70934 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70935 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70936 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70937 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70939 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70940 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70941 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Payroll product of Oracle E-Business Suite (component: Internal Operations).  Supported vers |
| CVE-2026-70942 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70943 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70944 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70945 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Payroll product of Oracle E-Business Suite (component: Internal Operations).  Supported vers |
| CVE-2026-70946 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70947 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Purchasing product of Oracle E-Business Suite (component: Other issue).  Supported versions  |
| CVE-2026-70948 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Purchasing product of Oracle E-Business Suite (component: Other issue).  Supported versions  |
| CVE-2026-70949 | 8.8 | 2026-08-18 | Vulnerability in the Siebel CRM Deployment product of Oracle Siebel CRM (component: Server Infrastructure).  Supported v |
| CVE-2026-70950 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70951 | 8.8 | 2026-08-18 | Vulnerability in the Siebel CRM End User product of Oracle Siebel CRM (component: Document Management).  Supported versi |
| CVE-2026-70952 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70953 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Commerce Platform product of Oracle Commerce (component: Dynamo Application Framework).   Th |
| CVE-2026-70954 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Commerce Platform product of Oracle Commerce (component: Dynamo Application Framework).   Th |
| CVE-2026-70955 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Commerce Platform product of Oracle Commerce (component: Dynamo Application Framework).   Th |
| CVE-2026-70956 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-70957 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-70958 | 9.6 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-70959 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-70960 | 7.6 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-70964 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-70965 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-70966 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-70967 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-70970 | 9.8 | 2026-08-18 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Runtime Tools).  Supported  |
| CVE-2026-70971 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-70973 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-70976 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70977 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70978 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70979 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70980 | 9.0 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70981 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70984 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70985 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70986 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70987 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70988 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70992 | 7.0 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70993 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70994 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70995 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70996 | 8.6 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70997 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70998 | 9.3 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-70999 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71000 | 8.7 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71002 | 8.5 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71003 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71009 | 7.4 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71010 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71012 | 7.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71014 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71015 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71016 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71018 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71020 | 7.6 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71021 | 7.6 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71022 | 7.6 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71023 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71024 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71026 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71027 | 7.6 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71028 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71030 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71032 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71034 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71035 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71036 | 9.1 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71037 | 9.3 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71038 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Commerce Guided Search / Oracle Commerce Experience Manager product of Oracle Commerce (comp |
| CVE-2026-71039 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Agile PLM product of Oracle Supply Chain (component: Application Server).   The supported ve |
| CVE-2026-71040 | 9.8 | 2026-08-18 | Vulnerability in the Oracle Agile PLM product of Oracle Supply Chain (component: Security).   The supported version that |
| CVE-2026-71041 | 7.0 | 2026-08-18 | Vulnerability in the Oracle Agile PLM product of Oracle Supply Chain (component: Gantt Chart).   The supported version t |
| CVE-2026-71042 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Agile PLM product of Oracle Supply Chain (component: PGC / Excel Plugin).   The supported ve |
| CVE-2026-71043 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Agile PLM product of Oracle Supply Chain (component: Security).   The supported version that |
| CVE-2026-71044 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Agile PLM product of Oracle Supply Chain (component: Export).   The supported version that i |
| CVE-2026-71045 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Agile PLM product of Oracle Supply Chain (component: Security).   The supported version that |
| CVE-2026-71046 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Agile PLM product of Oracle Supply Chain (component: Security).   The supported version that |
| CVE-2026-71048 | 7.6 | 2026-08-18 | Vulnerability in the Oracle Product Lifecycle Analytics product of Oracle Supply Chain (component: Installation Issues). |
| CVE-2026-71049 | 8.5 | 2026-08-18 | Vulnerability in the Oracle Product Lifecycle Analytics product of Oracle Supply Chain (component: Installation Issues). |
| CVE-2026-71050 | 8.7 | 2026-08-18 | Vulnerability in the Oracle Product Lifecycle Analytics product of Oracle Supply Chain (component: Installation Issues). |
| CVE-2026-71051 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Product Lifecycle Analytics product of Oracle Supply Chain (component: Installation Issues). |
| CVE-2026-71052 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Agile Engineering Data Management product of Oracle Supply Chain (component: Web Services Se |
| CVE-2026-71053 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Agile Engineering Data Management product of Oracle Supply Chain (component: Web Services Se |
| CVE-2026-71055 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Platform Se |
| CVE-2026-71056 | 7.7 | 2026-08-18 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: BI Search). |
| CVE-2026-71057 | 8.5 | 2026-08-18 | Vulnerability in the Oracle BI Publisher product of Oracle Analytics (component: BI Platform Security).  Supported versi |
| CVE-2026-71058 | 8.8 | 2026-08-18 | Vulnerability in the Oracle BI Publisher product of Oracle Analytics (component: Web Service API).  Supported versions t |
| CVE-2026-71059 | 9.9 | 2026-08-18 | Vulnerability in the Oracle BI Publisher product of Oracle Analytics (component: Web Service API).  Supported versions t |
| CVE-2026-71061 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: BI Platform |
| CVE-2026-71062 | 8.5 | 2026-08-18 | Vulnerability in the RDBMS component of Oracle Database Server.  Supported versions that are affected are 23.4.0-23.26.3 |
| CVE-2026-71063 | 9.6 | 2026-08-18 | Vulnerability in the Portable Clusterware component of Oracle Database Server.  Supported versions that are affected are |
| CVE-2026-71064 | 9.6 | 2026-08-18 | Vulnerability in the Portable Clusterware component of Oracle Database Server.  Supported versions that are affected are |
| CVE-2026-71065 | 9.3 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-71067 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Agile PLM MCAD Connector product of Oracle Supply Chain (component: CAX Client).   The suppo |
| CVE-2026-71068 | 8.1 | 2026-08-18 | Vulnerability in the Oracle Agile PLM MCAD Connector product of Oracle Supply Chain (component: CAX Client).   The suppo |
| CVE-2026-71069 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Agile PLM MCAD Connector product of Oracle Supply Chain (component: CAX Client).   The suppo |
| CVE-2026-71074 | 9.8 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-71092 | 7.5 | 2026-08-18 | Vulnerability in the PeopleSoft Enterprise FIN Lease Administration product of Oracle PeopleSoft (component: Lease Admin |
| CVE-2026-71094 | 7.3 | 2026-08-18 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Presentatio |
| CVE-2026-71095 | 8.3 | 2026-08-18 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: BI Platform |
| CVE-2026-71096 | 8.2 | 2026-08-18 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: BI Platform |
| CVE-2026-71097 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Platform Se |
| CVE-2026-71098 | 7.0 | 2026-08-18 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Platform Se |
| CVE-2026-71099 | 7.2 | 2026-08-18 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Analytics W |
| CVE-2026-71101 | 7.8 | 2026-08-18 | Vulnerability in the Oracle HRMS (US) product of Oracle E-Business Suite (component: US Payroll Tax Issues).  Supported  |
| CVE-2026-71102 | 9.1 | 2026-08-18 | Vulnerability in the Portable Clusterware component of Oracle Database Server.  Supported versions that are affected are |
| CVE-2026-71104 | 7.2 | 2026-08-18 | Vulnerability in the Oracle HRMS (Netherlands) product of Oracle E-Business Suite (component: Netherlands Payroll).  Sup |
| CVE-2026-71106 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hospitality OPERA 5 Property Services product of Oracle Hospitality Applications (component: |
| CVE-2026-71107 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Analytics S |
| CVE-2026-71110 | 8.1 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-71111 | 7.8 | 2026-08-18 | Vulnerability in the Oracle Identity Manager product of Oracle Fusion Middleware (component: Installer).  Supported vers |
| CVE-2026-71112 | 8.1 | 2026-08-18 | Vulnerability in the PeopleSoft Enterprise FIN Common Objects product of Oracle PeopleSoft (component: Security).   The  |
| CVE-2026-71113 | 7.5 | 2026-08-18 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-71116 | 7.5 | 2026-08-18 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-71117 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-71122 | 8.0 | 2026-08-18 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Platform Se |
| CVE-2026-71126 | 7.8 | 2026-08-18 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-71129 | 8.2 | 2026-08-18 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-71130 | 8.2 | 2026-08-18 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-71131 | 8.6 | 2026-08-18 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-71136 | 7.3 | 2026-08-18 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-71138 | 7.3 | 2026-08-18 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-71141 | 7.7 | 2026-08-18 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-71142 | 7.5 | 2026-08-18 | Vulnerability in the Oracle Communications Unified Inventory Management product of Oracle Communications (component: Sec |
| CVE-2026-71143 | 7.4 | 2026-08-18 | Vulnerability in the Oracle Communications Unified Inventory Management product of Oracle Communications (component: Thi |
| CVE-2026-71150 | 8.8 | 2026-08-18 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-71152 | 9.8 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-71153 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-71155 | 8.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-71158 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-71159 | 8.2 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-71160 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-71164 | 9.8 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-71166 | 9.4 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-71167 | 9.4 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73865 | 9.1 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73866 | 9.1 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73875 | 7.2 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73876 | 7.2 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73878 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73879 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73882 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73883 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73884 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73885 | 7.2 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73886 | 7.2 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73887 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73890 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73891 | 7.3 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73894 | 7.3 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73902 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73903 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73905 | 9.8 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73907 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73908 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73912 | 9.8 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73915 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73916 | 9.1 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73917 | 9.1 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73918 | 7.3 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73920 | 9.4 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73921 | 9.8 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73922 | 9.1 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73924 | 9.1 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73925 | 8.2 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73927 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73928 | 7.2 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73929 | 8.3 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73930 | 9.9 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73931 | 8.3 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73933 | 7.3 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73934 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73935 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73936 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73937 | 8.2 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73938 | 7.5 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-73939 | 8.6 | 2026-08-18 | Vulnerability in the Helidon product of Oracle Fusion Middleware (component: Imperative Web Server).   The supported ver |
| CVE-2026-50142 | 7.5 | 2026-08-18 | libheif is a HEIF and AVIF file format decoder and encoder. From 1.19.0 until 1.23.0, a crafted HEIF sequence accepted b |
| CVE-2026-50186 | 8.8 | 2026-08-18 | 4gaBoards is a boards system for realtime project management. Prior to 3.3.8, 4gaBoards allows an authenticated project  |
| CVE-2026-50191 | 8.8 | 2026-08-18 | 4gaBoards is a boards system for realtime project management. Prior to 3.3.8, 4gaBoards is vulnerable to pre-account tak |
| CVE-2026-52854 | 8.6 | 2026-08-18 | Maps is a MediaWiki extension that enables visualization of geographic data through dynamic embedded maps. Prior to vers |
| CVE-2026-52872 | 8.8 | 2026-08-18 | Streambert is a cross-platform Electron Desktop App to stream and download video content. Prior to 2.5.0, the downloadSu |
| CVE-2026-52876 | 8.8 | 2026-08-18 | Streambert is a cross-platform Electron Desktop App to stream and download video content. Prior to version 2.6.0, the op |
| CVE-2026-52877 | 8.3 | 2026-08-18 | Streambert is a cross-platform Electron Desktop App to stream and download video content. Prior to version 2.6.0, the op |
| CVE-2026-53958 | 7.6 | 2026-08-18 | 4gaBoards is a boards system for realtime project management. Prior to 3.3.9, 4gaBoards allows an authenticated user to  |
| CVE-2026-66602 | 8.8 | 2026-08-18 | Cross-Site Request Forgery (CSRF) vulnerability in DevItems HashBar – WordPress Notification Bar allows Cross Site Reque |
| CVE-2026-75976 | 9.9 | 2026-08-19 | A weakness has been identified in TRENDnet TEW-823DRU 1.1.02b01. Impacted is the function strcpy of the file /cgi-bin/wa |
| CVE-2026-75984 | 7.4 | 2026-08-19 | A vulnerability was detected in TRENDnet TEW-823DRU 1.1.02b01. Impacted is an unknown function of the file /cgi-bin/admi |
| CVE-2026-75985 | 7.4 | 2026-08-19 | A flaw has been found in TRENDnet Router 1.1.02b01. The affected element is an unknown function of the file /cgi-bin/pin |
| CVE-2026-75986 | 7.3 | 2026-08-19 | A vulnerability has been found in code-projects Online Job Portal System 1.0. The impacted element is an unknown functio |
| CVE-2026-75987 | 7.3 | 2026-08-19 | A vulnerability was found in SPLWare esProc up to 20260507. This affects the function ObjectInputStream.readUnshared of  |
| CVE-2026-76003 | 9.9 | 2026-08-19 | A weakness has been identified in UTT HiPER 1200GW up to 2.5.3-170306. Affected is the function strcpy of the file /gofo |
| CVE-2026-76004 | 9.9 | 2026-08-19 | A security vulnerability has been detected in UTT HiPER 1250GW up to 3.2.7-210907-180535. Affected by this vulnerability |
| CVE-2026-76008 | 10.0 | 2026-08-19 | A flaw has been found in Comfast CF-N1-S 2.6.0.1. This affects the function get_para_from_uri of the file /cgi-bin/mbox- |
| CVE-2026-76048 | 7.3 | 2026-08-19 | A flaw has been found in SourceCodester Simple Online Food Ordering System 1.0. The impacted element is an unknown funct |
| CVE-2026-76049 | 7.3 | 2026-08-19 | A vulnerability has been found in SourceCodester Simple Online Food Ordering System 1.0. This affects an unknown functio |
| CVE-2026-76050 | 7.3 | 2026-08-19 | A vulnerability was found in SourceCodester Simple Online Food Ordering System 1.0. This impacts an unknown function of  |
| CVE-2026-19942 | 8.1 | 2026-08-19 | The Atarim – AI Agency for WordPress: Edit Pages, Fix Code, Update Plugins, SEO & Client Feedback plugin for WordPress i |
| CVE-2026-70408 | 8.8 | 2026-08-19 | An incorrect authorization vulnerability exists in acmailer, which may allow a user to create a sub-account that has adm |
| CVE-2026-15780 | 7.2 | 2026-08-19 | The WP Statistics – Simple, privacy-friendly Google Analytics alternative plugin for WordPress is vulnerable to Stored C |
| CVE-2026-75981 | 7.2 | 2026-08-19 | The TranslatePress – Translate Multilingual sites with AI Translation plugin for WordPress is vulnerable to unauthentica |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-33824 | Microsoft / Internet Key Exchange (IKE) Service Extensions | 2026-08-18 | 2026-08-21 | Unknown |
| CVE-2026-59310 | Broadcom / VMware vCenter | 2026-08-18 | 2026-08-21 | Unknown |
| CVE-2026-55040 | Microsoft / SharePoint | 2026-08-18 | 2026-08-21 | Unknown |
| CVE-2026-65400 | Apple / macOS | 2026-08-18 | 2026-08-21 | Unknown |
| CVE-2025-62593 | Ray-Project / Ray | 2026-08-17 | 2026-08-20 | Unknown |

---

*Total entries in CISA KEV catalog: 1670*