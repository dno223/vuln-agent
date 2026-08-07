# Vulnerability Intelligence Report

**Date:** 2026-08-07  
**Generated:** 2026-08-07T08:57:28Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011Cdo7P8QADyweVVrPmAJV5'}

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
| CVE-2026-55978 | 8.4 | 2026-08-06 | An improper access control vulnerability in CatchPulse could allow a non-administrative local attacker to connect to an  |
| CVE-2026-19034 | 7.2 | 2026-08-06 | A vulnerability was determined in Shibby Tomato 1.28.0000. Affected by this vulnerability is the function new_qoslimit_s |
| CVE-2026-54225 | 7.5 | 2026-08-06 | Apache CXF allows to control the maximum attachment size via the "attachment-max-size". Prior to Apache CXF 4.2.3 and 4. |
| CVE-2026-57817 | 8.1 | 2026-08-06 | The OpenID Connect Core 1.0 specification mandates that the RP MUST validate the `c_hash` parameter when operating in th |
| CVE-2026-57819 | 7.5 | 2026-08-06 | Apache CXF allows to set a limit on the number of form parameters in a JAX-RS message via the "maxFormParameterCount" co |
| CVE-2026-64958 | 7.5 | 2026-08-06 | An incomplete fix for CVE-2026-50645 means that it is still possible to perform a denial of service attack on Apache CXF |
| CVE-2026-65432 | 7.5 | 2026-08-06 | Apache CXF reads a top-level WSDL through its hardened StaxUtils path, which disables XML DTDs and external entities. Ho |
| CVE-2026-66909 | 9.8 | 2026-08-06 | Apache CXF's JMS transport deserializes the body of any inbound JMS ObjectMessage using native Java deserialization, wit |
| CVE-2025-15028 | 7.2 | 2026-08-06 | The FormGent – Next-Gen AI Form Builder for WordPress with Multi-Step, Quizzes, Payments & More plugin for WordPress is  |
| CVE-2026-19035 | 7.2 | 2026-08-06 | A vulnerability was identified in Shibby Tomato 1.28.0000. Affected by this issue is the function new_qoslimit_start of  |
| CVE-2026-57818 | 8.1 | 2026-08-06 | A race condition in JCacheCodeDataProvider allows an attacker to redeem a single authorization code multiple times via c |
| CVE-2026-61466 | 9.1 | 2026-08-06 | In Apache CXF's OAuth2 Dynamic Client Registration endpoint, the authorization server accepts and stores the `scope` val |
| CVE-2026-63687 | 9.1 | 2026-08-06 | Apache CXF's JwtRequestCodeFilter copies all claims from a signed request JWT into the authorization parameter map witho |
| CVE-2026-65583 | 9.1 | 2026-08-06 | Apache CXF’s OIDC relying-party token validation could accept self-issued ID tokens without enforcing required claim che |
| CVE-2026-68079 | 9.8 | 2026-08-06 | In Apache CXF's DefaultEncryptingCodeDataProvider, a captured authorization code can be redeemed an unlimited number of  |
| CVE-2026-68481 | 7.5 | 2026-08-06 | In Apache CXF's DefaultEncryptingOAuthDataProvider, revoked access tokens still decrypt successfully, and TokenIntrospec |
| CVE-2026-19036 | 7.2 | 2026-08-06 | A security flaw has been discovered in Shibby Tomato 1.28.0000. This affects the function sub_40F88C of the file /tmp/pp |
| CVE-2026-65551 | 7.5 | 2026-08-06 | Missing Authorization vulnerability in Soflyy Breakdance allows Exploiting Incorrectly Configured Access Control Securit |
| CVE-2026-66733 | 7.5 | 2026-08-06 | Sonic 3 A.I.R. before commit 2492d18 contains an unbounded memory allocation vulnerability in ReceivedPacketCache::enque |
| CVE-2026-12605 | 9.6 | 2026-08-06 | In Eclipse GlassFish versions 8.0.x before 8.0.4, CSRF + SSRF in DownloadServlet ContentSources leaks the admin `gfrestt |
| CVE-2026-16315 | 8.7 | 2026-08-06 | OMICRON StationGuard before version 4.10 contains a cryptographic timing side-channel vulnerability in the backend authe |
| CVE-2026-5134 | 9.8 | 2026-08-06 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Loca Software Info |
| CVE-2025-49506 | 7.5 | 2026-08-06 | APR-util versions 1.6.3 (and earlier) function apr_password_validate() was not constant-time with regards to hashes or p |
| CVE-2026-28005 | 9.8 | 2026-08-06 | Unauthenticated Privilege Escalation in Kadence WooCommerce Email Designer <= 1.5.19 versions. |
| CVE-2026-28082 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in JetEngine <= 3.8.13.1 versions. |
| CVE-2026-28111 | 8.8 | 2026-08-06 | Contributor Privilege Escalation in Forminator <= 1.56.0 versions. |
| CVE-2026-28139 | 9.8 | 2026-08-06 | Unauthenticated PHP Object Injection in Ajax Search Lite <= 4.14.4 versions. |
| CVE-2026-28140 | 7.5 | 2026-08-06 | Unauthenticated Broken Access Control in JetFormBuilder <= 3.6.4.1 versions. |
| CVE-2026-28141 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in NextGEN Gallery <= 4.2.3 versions. |
| CVE-2026-28143 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Forminator <= 1.56.0 versions. |
| CVE-2026-28172 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Request Forgery (CSRF) in Tracking Code Manager <= 2.6.0 versions. |
| CVE-2026-28177 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Popup Maker <= 1.23.0 versions. |
| CVE-2026-32327 | 9.1 | 2026-08-06 | A bug in APR-util version 1.6.3 (and earlier) allows a stack recursion attack against any library consumer which parses  |
| CVE-2026-34191 | 9.1 | 2026-08-06 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Apache Portable Ru |
| CVE-2026-34501 | 7.5 | 2026-08-06 | Heap-based Buffer Overflow vulnerability in Apache Portable Runtime Utility redis client.

This issue affects Apache Por |
| CVE-2026-34502 | 7.5 | 2026-08-06 | Heap-based Buffer Overflow vulnerability in Apache Portable Runtime Utility memcached client

This issue affects Apache  |
| CVE-2026-53975 | 9.8 | 2026-08-06 | OpenChamber 1.11.7 contains an unauthenticated remote code execution vulnerability that allows remote attackers to execu |
| CVE-2026-53976 | 9.1 | 2026-08-06 | OpenChamber 1.11.7 contains a path traversal vulnerability in the file-serving endpoints /api/fs/read, /api/fs/stat, and |
| CVE-2026-54489 | 9.1 | 2026-08-06 | Dell Virtual Storage Integrator for VMware vSphere Client, versions prior to 10.11.1.0, contain(s) a Sensitive Informati |
| CVE-2026-61961 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in EmbedPress <= 4.5.6 versions. |
| CVE-2026-61963 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Media LIbrary Assistant <= 3.38 versions. |
| CVE-2026-61964 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Ninja Tables <= 5.2.9 versions. |
| CVE-2026-61982 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in SiteGuard WP Plugin <= 1.8.6 versions. |
| CVE-2026-65504 | 7.5 | 2026-08-06 | Unauthenticated Broken Access Control in BOX NOW Delivery Croatia <= 3.3.0 versions. |
| CVE-2026-65507 | 9.8 | 2026-08-06 | Unauthenticated Privilege Escalation in AIWU <= 1.5.6 versions. |
| CVE-2026-65508 | 9.3 | 2026-08-06 | Unauthenticated SQL Injection in Simply Schedule Appointments <= 1.6.12.10 versions. |
| CVE-2026-65509 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in wpDataTables <= 7.5.1 versions. |
| CVE-2026-65513 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Simply Schedule Appointments <= 1.6.12.10 versions. |
| CVE-2026-65515 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in AffiliateWP <= 2.35.0 versions. |
| CVE-2026-65517 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Easy PayPal Buy Now Button <= 2.0.4 versions. |
| CVE-2026-65520 | 9.3 | 2026-08-06 | Unauthenticated SQL Injection in WP OAuth Server <= 6.2.0 versions. |
| CVE-2026-65523 | 7.5 | 2026-08-06 | Unauthenticated Insecure Direct Object References (IDOR) in Formidable Forms Signature Online Contract Automation <= 2.0 |
| CVE-2026-65541 | 7.3 | 2026-08-06 | Unauthenticated Broken Access Control in Staff Training <= 1.0.7 versions. |
| CVE-2026-65542 | 8.8 | 2026-08-06 | Unauthenticated Broken Authentication in Super Socializer <= 7.14.5 versions. |
| CVE-2026-65543 | 7.5 | 2026-08-06 | Subscriber Sensitive Data Exposure in Vimeo <= 1.2.2 versions. |
| CVE-2026-65544 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Super Socializer <= 7.14.5 versions. |
| CVE-2026-65545 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in AI Engine <= 3.6.8 versions. |
| CVE-2026-65546 | 9.3 | 2026-08-06 | Unauthenticated SQL Injection in Qode Tours <= 3.1.3.1 versions. |
| CVE-2026-65547 | 8.5 | 2026-08-06 | Subscriber SQL Injection in Creative Mail <= 1.6.9 versions. |
| CVE-2026-65548 | 9.9 | 2026-08-06 | Contributor Remote Code Execution (RCE) in Betheme <= 28.4.2 versions. |
| CVE-2026-65549 | 7.2 | 2026-08-06 | Author PHP Object Injection in Jeg Kit for Elementor <= 3.2.10 versions. |
| CVE-2026-65552 | 9.8 | 2026-08-06 | Subscriber PHP Object Injection in Export User Data <= 2.2.6 versions. |
| CVE-2026-65553 | 10.0 | 2026-08-06 | Unauthenticated Remote Code Execution (RCE) in Spider Analyser &#8211; WordPress搜索引擎蜘蛛分析插件 <= 2.1.3 versions. |
| CVE-2026-65554 | 7.1 | 2026-08-06 | Subscriber Broken Access Control in AnsPress – Question and answer 4.4.4 versions. |
| CVE-2026-65556 | 9.8 | 2026-08-06 | Unauthenticated PHP Object Injection in WPBruiser {no- Captcha anti-Spam} <= 3.1.43 versions. |
| CVE-2026-65559 | 7.2 | 2026-08-06 | Shop manager Privilege Escalation in Order Delivery Date for WooCommerce <= 4.6.0 versions. |
| CVE-2026-65560 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Houzez Property Feed <= 2.5.48 versions. |
| CVE-2026-65565 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Survey Maker <= 5.2.3.3 versions. |
| CVE-2026-65569 | 8.5 | 2026-08-06 | Subscriber SQL Injection in WP Job Portal <= 2.5.6 versions. |
| CVE-2026-65570 | 8.1 | 2026-08-06 | Unauthenticated Bypass Vulnerability in Login with phone number <= 1.8.70 versions. |
| CVE-2026-65571 | 9.8 | 2026-08-06 | Unauthenticated PHP Object Injection in 69 Clothing <= 1.2.11.1 versions. |
| CVE-2026-65572 | 9.8 | 2026-08-06 | Unauthenticated PHP Object Injection in A.Williams <= 1.3.1 versions. |
| CVE-2026-65573 | 9.8 | 2026-08-06 | Unauthenticated PHP Object Injection in Abelle <= 1.22 versions. |
| CVE-2026-65574 | 9.8 | 2026-08-06 | Unauthenticated PHP Object Injection in Abogado <= 1.18 versions. |
| CVE-2026-65575 | 9.8 | 2026-08-06 | Unauthenticated PHP Object Injection in Accalia <= 1.5.3 versions. |
| CVE-2026-65576 | 9.8 | 2026-08-06 | Unauthenticated PHP Object Injection in Adrena <= 1.2.14 versions. |
| CVE-2026-65577 | 9.8 | 2026-08-06 | Unauthenticated PHP Object Injection in Advice <= 1.18.0 versions. |
| CVE-2026-65578 | 9.8 | 2026-08-06 | Unauthenticated PHP Object Injection in Agora <= 1.9 versions. |
| CVE-2026-65579 | 9.8 | 2026-08-06 | Unauthenticated PHP Object Injection in Agricola <= 1.21.0 versions. |
| CVE-2026-65581 | 9.8 | 2026-08-06 | Unauthenticated PHP Object Injection in AI ANN <= 1.29.0 versions. |
| CVE-2026-66439 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Advanced AJAX Product Filters <= 3.2.0.3 versions. |
| CVE-2026-66440 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in WPIDE – File Manager & Code Editor <= 3.5.7 versions. |
| CVE-2026-66447 | 9.3 | 2026-08-06 | Unauthenticated SQL Injection in WordPress File Upload <= 5.1.7 versions. |
| CVE-2026-66457 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Events Manager <= 7.4.1 versions. |
| CVE-2026-66470 | 7.1 | 2026-08-06 | Subscriber Broken Access Control in Frontend Admin by DynamiApps <= 3.29.10 versions. |
| CVE-2026-66662 | 9.8 | 2026-08-06 | Unauthenticated Privilege Escalation in Frontend Admin by DynamiApps <= 3.29.10 versions. |
| CVE-2026-66663 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in WP Data Access <= 5.5.79 versions. |
| CVE-2026-66664 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in SEO Plugin by Squirrly SEO <= 14.2.0 versions. |
| CVE-2026-66665 | 10.0 | 2026-08-06 | Unauthenticated Arbitrary File Upload in Type Hub <= 2.0.6 versions. |
| CVE-2026-66690 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in GiveWP <= 4.16.5 versions. |
| CVE-2026-66694 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Thrive Architect <= 10.9.3.1 versions. |
| CVE-2026-66702 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Rank Math SEO <= 1.0.274.1 versions. |
| CVE-2026-66705 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Facebook for WordPress <= 5.2.1 versions. |
| CVE-2026-66707 | 7.1 | 2026-08-06 | Unauthenticated Cross Site Scripting (XSS) in Facebook for WooCommerce <= 3.7.5 versions. |
| CVE-2026-66708 | 8.2 | 2026-08-06 | Unauthenticated Broken Access Control in Total Upkeep <= 1.17.2 versions. |
| CVE-2026-66709 | 9.1 | 2026-08-06 | Shop manager Remote Code Execution (RCE) in CTX Feed <= 6.6.42 versions. |
| CVE-2026-66710 | 8.1 | 2026-08-06 | Unauthenticated Local File Inclusion in e2pdf <= 1.32.40 versions. |
| CVE-2026-66711 | 7.1 | 2026-08-06 | Subscriber Cross Site Scripting (XSS) in WooCommerce Multilingual & Multicurrency <= 5.5.6 versions. |
| CVE-2026-66712 | 7.5 | 2026-08-06 | Unauthenticated Broken Access Control in Simple Membership <= 4.7.8 versions. |
| CVE-2026-67261 | 9.8 | 2026-08-06 | Dell Virtual Storage Integrator for VMware vSphere Client, versions prior to 10.11.1.0, contain(s) an OS Command Injecti |
| CVE-2026-70646 | 7.5 | 2026-08-06 | aiosend is a synchronous and asynchronous Crypto Pay API client. Pror to version 3.0.7, `WebhookHandler.feed_update()` d |
| CVE-2026-18258 | 8.8 | 2026-08-06 | Authorization bypass in the Line, LineTranscription, VirtualCollection, tag and process API endpoints in Scripta/eScript |
| CVE-2026-18277 | 7.1 | 2026-08-06 | Missing authorization in the OcrModelRight create and delete views in Scripta eScriptorium through 26.04.1 allows a remo |
| CVE-2026-18359 | 8.5 | 2026-08-06 | Server-side request forgery in the METS and IIIF import URI handling in Scripta eScriptorium through 26.04.1 allows a re |
| CVE-2026-18427 | 7.5 | 2026-08-06 | @fastify/static before version 10.1.3 contains an incomplete fix for a previous route guard bypass. The static file hand |
| CVE-2026-3430 | 8.6 | 2026-08-06 | The Creative Mail WordPress plugin from 1.6.5 to 1.6.9 does not sanitize and escape a parameter before using in an SQL s |
| CVE-2026-43622 | 7.8 | 2026-08-06 | llama.cpp builds b1886 through b7445 contain a double free vulnerability in the LLaMA-Android JNI wrapper where new_1bat |
| CVE-2026-53977 | 7.5 | 2026-08-06 | OpenChamber 1.11.7 contains an authentication bypass vulnerability that allows unauthenticated remote attackers to termi |
| CVE-2026-53985 | 7.5 | 2026-08-06 | Ground Station prior to 0.6.0 contains an unauthenticated denial-of-service vulnerability in the Socket.IO server's serv |
| CVE-2025-14561 | 9.0 | 2026-08-06 | In multi-tenant deployments, the Publisher REST APIs fail to enforce tenant isolation correctly. This allows a user in o |
| CVE-2026-10524 | 7.5 | 2026-08-06 | The CoCart WordPress plugin before 4.9.0 does not validate a user-supplied price value against the actual product price  |
| CVE-2026-10599 | 7.5 | 2026-08-06 | The Integrate PhonePe with WooCommerce WordPress plugin through 1.2.1 does not validate that a verified payment transact |
| CVE-2026-11803 | 7.8 | 2026-08-06 | A maliciously crafted PDF file, when parsed through Autodesk Revit, can force an Out-of-Bounds Read vulnerability. A mal |
| CVE-2026-11976 | 10.0 | 2026-08-06 | The official MonsterInsights Pro update distribution bucket (`monster-insights.s3.amazonaws.com`) was compromised. Both  |
| CVE-2026-12584 | 7.5 | 2026-08-06 | The Payment Gateway for Redsys & WooCommerce Lite WordPress plugin before 7.0.2 does not verify the authenticity of inco |
| CVE-2026-13399 | 7.5 | 2026-08-06 | The Payment Plugins for PayPal WooCommerce WordPress plugin before 2.0.20 does not have proper authorization checks on a |
| CVE-2026-14812 | 10.0 | 2026-08-06 | The Premium SEO WordPress plugin is malicious: it ships an unauthenticated backdoor that creates a hidden administrator  |
| CVE-2026-16619 | 7.5 | 2026-08-06 | The miniOrange 2FA WordPress plugin before 6.2.8 does not correctly limit the number of second-factor verification attem |
| CVE-2026-16620 | 7.5 | 2026-08-06 | The WPC Name Your Price for WooCommerce WordPress plugin before 2.2.5 does not enforce its server-side price allowlist f |
| CVE-2026-17032 | 9.8 | 2026-08-06 | Multiple Supsystic Pro plugins were distributed with malicious code through the vendor's compromised update server, allo |
| CVE-2026-18367 | 9.3 | 2026-08-06 | A privilege escalation vulnerability allows local users to execute arbitrary code as root via Sophos Endpoint for macOS  |
| CVE-2026-19062 | 7.3 | 2026-08-06 | A vulnerability has been found in chiuwingyan house up to dea6bcceaebe2b364a5a209747f48ecc2b2dc670. This affects an unkn |
| CVE-2026-19111 | 8.1 | 2026-08-06 | Insecure direct object reference in the mongodb_memory, elasticsearch_memory, and mem0_memory tools in Amazon Strands Ag |
| CVE-2026-19137 | 8.3 | 2026-08-06 | Use after free in WebGL in Google Chrome on Android prior to 151.0.7922.109 allowed a remote attacker who had compromise |
| CVE-2026-19138 | 8.3 | 2026-08-06 | Heap buffer overflow in CrashReporting in Google Chrome prior to 151.0.7922.109 allowed a remote attacker who had compro |
| CVE-2026-19139 | 7.4 | 2026-08-06 | Race in CredentialProvider in Google Chrome on Windows prior to 151.0.7922.109 allowed a local attacker to perform OS-le |
| CVE-2026-19140 | 8.3 | 2026-08-06 | Use after free in GPU in Google Chrome prior to 151.0.7922.109 allowed a remote attacker who had compromised the rendere |
| CVE-2026-19145 | 8.8 | 2026-08-06 | Use after free in Translate in Google Chrome prior to 151.0.7922.109 allowed a remote attacker to execute arbitrary code |
| CVE-2026-19149 | 9.6 | 2026-08-06 | Use after free in Aura in Google Chrome on Linux prior to 151.0.7922.109 allowed a remote attacker to potentially perfor |
| CVE-2026-19150 | 8.8 | 2026-08-06 | Inappropriate implementation in V8 in Google Chrome prior to 151.0.7922.109 allowed a remote attacker to execute arbitra |
| CVE-2026-19151 | 8.8 | 2026-08-06 | Use after free in V8 in Google Chrome prior to 151.0.7922.109 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-19154 | 8.3 | 2026-08-06 | Use after free in Skia in Google Chrome on Android prior to 151.0.7922.109 allowed a remote attacker who had compromised |
| CVE-2026-19155 | 8.3 | 2026-08-06 | Use after free in Payments in Google Chrome prior to 151.0.7922.109 allowed a remote attacker who had compromised the re |
| CVE-2026-19162 | 8.8 | 2026-08-06 | Out of bounds write in V8 in Google Chrome prior to 151.0.7922.109 allowed a remote attacker to execute arbitrary code i |
| CVE-2026-19163 | 8.3 | 2026-08-06 | Use after free in Media in Google Chrome on Windows prior to 151.0.7922.109 allowed a remote attacker who had compromise |
| CVE-2026-19165 | 7.5 | 2026-08-06 | Use after free in Extensions in Google Chrome prior to 151.0.7922.109 allowed an attacker who convinced a user to instal |
| CVE-2026-19168 | 8.8 | 2026-08-06 | Inappropriate implementation in V8 in Google Chrome prior to 151.0.7922.109 allowed a remote attacker to execute arbitra |
| CVE-2026-19169 | 8.8 | 2026-08-06 | Insufficient validation of untrusted input in Contextual Tasks in Google Chrome prior to 151.0.7922.109 allowed a remote |
| CVE-2026-19170 | 9.6 | 2026-08-06 | Use after free in WebGL in Google Chrome on Android prior to 151.0.7922.109 allowed a remote attacker to potentially per |
| CVE-2026-19172 | 8.3 | 2026-08-06 | Use after free in Views in Google Chrome prior to 151.0.7922.109 allowed a remote attacker who had compromised the rende |
| CVE-2026-19174 | 8.8 | 2026-08-06 | Integer overflow in V8 in Google Chrome prior to 151.0.7922.109 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-19176 | 7.5 | 2026-08-06 | Use after free in Skia in Google Chrome prior to 151.0.7922.109 allowed a remote attacker who had compromised the render |
| CVE-2026-19177 | 8.3 | 2026-08-06 | Insufficient validation of untrusted input in UI in Google Chrome prior to 151.0.7922.109 allowed a remote attacker who  |
| CVE-2026-1289 | 7.8 | 2026-08-06 | A maliciously crafted PDF file, when parsed through Autodesk Revit, can force a Use-After-Free vulnerability. A maliciou |
| CVE-2026-3415 | 8.7 | 2026-08-06 | The XML and schema validation functionalities within the SchemaValidator Mediator process XML input as part of validatio |
| CVE-2026-3418 | 9.1 | 2026-08-06 | The System REST API accepts user-supplied file uploads without enforcing sufficient validation on the file type or desti |
| CVE-2026-43627 | 7.8 | 2026-08-06 | llama.cpp builds b1283 through b9058 contain an integer overflow vulnerability in the llama_batch_init() function where  |
| CVE-2026-43628 | 7.8 | 2026-08-06 | llama.cpp builds b3978 through b9058 contain an integer underflow and out-of-bounds read vulnerability in the DRY sample |
| CVE-2026-43629 | 8.1 | 2026-08-06 | llama.cpp builds b4882 through b9058 contain a heap buffer overflow vulnerability in the KV cache state restore path whe |
| CVE-2026-43631 | 8.1 | 2026-08-06 | llama.cpp builds b7492 through the latest b9060 contains a use-after-free vulnerability in the vocab pointer of llama-se |
| CVE-2026-43632 | 8.1 | 2026-08-06 | llama.cpp builds b7492 through the latest b9060 contains a use-after-free vulnerability in llama-server affecting six to |
| CVE-2026-45378 | 7.5 | 2026-08-06 | Decidim is a participatory democracy framework. Prior to 0.30.9, from 0.31.0 before 0.31.5, and in 0.32.0.rc1 before 0.3 |
| CVE-2026-45414 | 8.5 | 2026-08-06 | Decidim is a participatory democracy framework. Prior to 0.31.5 and in 0.32.0.rc1 before 0.32.0.rc2, JWT-backed API auth |
| CVE-2026-48054 | 8.8 | 2026-08-06 | OpenZeppelin Contracts Wizardis a web application to interactively build a contract out of components from OpenZeppelin  |
| CVE-2026-48079 | 7.4 | 2026-08-06 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to ver |
| CVE-2026-48080 | 8.0 | 2026-08-06 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to ver |
| CVE-2026-48081 | 8.1 | 2026-08-06 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to ver |
| CVE-2026-48084 | 7.4 | 2026-08-06 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Versions pri |
| CVE-2026-48085 | 9.8 | 2026-08-06 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to ver |
| CVE-2026-48086 | 9.9 | 2026-08-06 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to ver |
| CVE-2026-48087 | 9.8 | 2026-08-06 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to ver |
| CVE-2026-48088 | 9.4 | 2026-08-06 | OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to ver |
| CVE-2026-53983 | 8.6 | 2026-08-06 | Ground Station prior to 0.6.0 contains an unauthenticated blind server-side request forgery vulnerability in the orbital |
| CVE-2026-53984 | 9.1 | 2026-08-06 | Ground Station prior to 0.6.0 contains an unauthenticated database-destruction and arbitrary-data-injection vulnerabilit |
| CVE-2026-5855 | 7.5 | 2026-08-06 | Contiki-NG's LwM2M TLV parser lwm2m_tlv_read() in os/services/lwm2m/lwm2m-tlv.c ignores its caller-supplied buffer lengt |
| CVE-2026-5856 | 7.1 | 2026-08-06 | Contiki-NG's DNS/mDNS resolver skip_name() in os/services/resolv/resolv.c walks DNS wire-format name labels with no pack |
| CVE-2026-5857 | 8.1 | 2026-08-06 | Contiki-NG's MQTT client parse_publish_vhdr() in os/net/app-layer/mqtt/mqtt.c sets topic_len_received=1 before checking  |
| CVE-2026-63637 | 8.6 | 2026-08-06 | Dgraph is an open source distributed GraphQL database. Prior to 25.3.8, maybeQuoteArg in graphql/resolve/query_rewriter. |
| CVE-2026-63725 | 7.2 | 2026-08-06 | sysPass's FileBackupService::doBackupFiles() in lib/SP/Services/Backup/FileBackupService.php around line 388 builds a ta |
| CVE-2026-64665 | 8.1 | 2026-08-06 | Statamic is a Laravel and Git powered content management system (CMS). Prior to 5.74.1 and 6.24.0, when OAuth login was  |
| CVE-2026-65400 | 7.1 | 2026-08-06 | An authentication issue was addressed with improved state management. This issue is fixed in macOS Sequoia 15.7.9, macOS |
| CVE-2026-67422 | 7.5 | 2026-08-06 | pymdown-extensions is a collection of extensions for the Python Markdown library. In versions up to and including 11.0,  |
| CVE-2026-67621 | 7.6 | 2026-08-06 | Flowise through 3.1.4 contains a missing authorization vulnerability that allows authenticated workspace members to perf |
| CVE-2026-67622 | 9.9 | 2026-08-06 | Flowise through 3.1.4 contains an insecure direct object reference vulnerability in the OpenAI Assistants integration th |
| CVE-2026-70558 | 9.8 | 2026-08-06 | Dinky's POST /download/uploadFromRsByLocal handler passes the caller-supplied path parameter directly to new File(path)  |
| CVE-2026-70559 | 7.5 | 2026-08-06 | Dinky's SysConfigController.getAll() handler for GET /api/sysConfig/getAll carries a method-level @SaIgnore annotation t |
| CVE-2026-70628 | 7.8 | 2026-08-06 | FFmpeg versions from 0.5 up to, but not including, 9.0 contain a signed integer overflow vulnerability in the DVB subtit |
| CVE-2026-70632 | 7.8 | 2026-08-06 | FFmpeg versions from 4.4 up to, but not including, 9.0 contain an out-of-bounds heap write vulnerability in the native G |
| CVE-2026-70634 | 8.1 | 2026-08-06 | TimescaleDB through 2.29.1, fixed in commit 517c13e, contains an out-of-bounds read in the Dictionary compression revers |
| CVE-2026-70635 | 7.1 | 2026-08-06 | TimescaleDB through 2.29.1, fixed in commit 517c13e, contains an out-of-bounds read vulnerability that allows authentica |
| CVE-2026-70636 | 7.5 | 2026-08-06 | Flowise through 3.1.4 contains an authentication bypass vulnerability that allows unauthenticated attackers to access th |
| CVE-2026-70638 | 7.8 | 2026-08-06 | llama.cpp builds b1886 through b7445 contain an integer overflow vulnerability in the LLaMA-Android JNI wrapper where th |
| CVE-2026-70640 | 7.0 | 2026-08-06 | llama.cpp builds b1886 through b7445 contain a race condition use-after-free vulnerability in the LLaMA-Android JNI wrap |
| CVE-2026-71488 | 7.5 | 2026-08-06 | league/commonmark is a PHP library for parsing and rendering CommonMark Markdown. From 0.6.0 until 2.9.0, specially craf |
| CVE-2026-7406 | 7.8 | 2026-08-06 | A maliciously crafted BMP file, when parsed through certain Autodesk products, can force a Untrusted Pointer Dereference |
| CVE-2026-7867 | 7.8 | 2026-08-06 | A flaw was found in udisks2. A local attacker with an active console session can exploit insufficient authorization chec |
| CVE-2026-8325 | 7.8 | 2026-08-06 | A maliciously crafted PDF file, when parsed through Autodesk Revit, can force an Out-of-Bounds Write vulnerability. A ma |
| CVE-2026-49163 | 8.8 | 2026-08-07 | Improper limitation of a pathname to a restricted directory ('path traversal') in Application Insights Profiler allows a |
| CVE-2026-50481 | 9.9 | 2026-08-07 | Modification of assumed-immutable data (maid) in Azure Active Directory allows an authorized attacker to elevate privile |
| CVE-2026-50515 | 9.9 | 2026-08-07 | Deserialization of untrusted data in Azure Service Bus allows an authorized attacker to execute code over a network. |
| CVE-2026-56161 | 9.6 | 2026-08-07 | Improper access control in Azure Logic Apps allows an authorized attacker to disclose information over a network. |
| CVE-2026-56162 | 10.0 | 2026-08-07 | Improper authentication in Azure SQL Database allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-59115 | 9.9 | 2026-08-07 | '.../...//' in Microsoft Entra Provisioning Service (SyncFabric) allows an authorized attacker to elevate privileges ove |
| CVE-2026-59118 | 9.3 | 2026-08-07 | Improper authorization in Microsoft Power Apps allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-62830 | 9.9 | 2026-08-07 | Missing authorization in Azure SRE Agent allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-62836 | 8.7 | 2026-08-07 | Improper restriction of communication channel to intended endpoints in Azure SQL Managed Instance allows an unauthorized |
| CVE-2026-62873 | 9.8 | 2026-08-07 | Improper verification of cryptographic signature in Microsoft 365 Admin Center allows an unauthorized attacker to elevat |
| CVE-2026-62896 | 9.6 | 2026-08-07 | Improper authentication in Microsoft Teams allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-62918 | 7.5 | 2026-08-07 | Improper verification of cryptographic signature in Microsoft Teams allows an unauthorized attacker to perform spoofing  |
| CVE-2026-63508 | 10.0 | 2026-08-07 | Missing authentication for critical function in Microsoft Planetary Computer Pro allows an unauthorized attacker to elev |
| CVE-2026-65667 | 10.0 | 2026-08-07 | Missing authorization in Microsoft Teams allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-65668 | 8.8 | 2026-08-07 | Improper access control in Microsoft Purview eDiscovery allows an authorized attacker to elevate privileges over a netwo |
| CVE-2026-68823 | 9.1 | 2026-08-07 | Exposed dangerous method or function in Azure Confidential Ledger allows an authorized attacker to execute code over a n |
| CVE-2026-70332 | 9.6 | 2026-08-07 | Server-side request forgery (ssrf) in Microsoft Office SharePoint allows an unauthorized attacker to perform spoofing ov |
| CVE-2026-19189 | 7.8 | 2026-08-07 | A security flaw has been discovered in Power Sofware PowerISO 9.3.0.0. Affected by this issue is some unknown functional |
| CVE-2026-19190 | 7.8 | 2026-08-07 | A weakness has been identified in StableBit Scanner 2.6.13.4088. This affects an unknown part of the file C:\Program Fil |
| CVE-2026-14364 | 9.8 | 2026-08-07 | The TrueBooker – Appointment Booking and Scheduler System plugin for WordPress is vulnerable to account takeover via imp |
| CVE-2026-14365 | 9.8 | 2026-08-07 | The TrueBooker – Appointment Booking and Scheduler System plugin for WordPress is vulnerable to authorization bypass in  |
| CVE-2026-19191 | 7.8 | 2026-08-07 | A security vulnerability has been detected in StableBit DrivePool 2.3.13.1687. This vulnerability affects unknown code o |
| CVE-2026-19192 | 7.8 | 2026-08-07 | A vulnerability was detected in DeepCool DisplayService 1.2.12. This issue affects some unknown processing of the file C |
| CVE-2026-19193 | 7.8 | 2026-08-07 | A flaw has been found in Jiangmin Antivirus 21. Impacted is the function MessageNotifyCallback in the library kvcore.sys |
| CVE-2026-19195 | 7.8 | 2026-08-07 | A vulnerability has been found in V-Secure Jingyun Antivirus 2.4.2.39. The affected element is an unknown function in th |
| CVE-2026-19196 | 7.3 | 2026-08-07 | A vulnerability was found in SourceCodester Photo Share Website 1.0. The impacted element is an unknown function of the  |
| CVE-2026-49007 | 7.5 | 2026-08-07 | By accessing unencrypted information in the device firmware, an attacker can obtain the initial login credentials for th |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-63077 | JetBrains / TeamCity | 2026-08-05 | 2026-08-08 | Unknown |
| CVE-2026-18556 | N-able / N-central | 2026-08-04 | 2026-08-07 | Unknown |
| CVE-2026-34486 | Apache / Tomcat | 2026-08-04 | 2026-08-07 | Unknown |
| CVE-2026-9198 | IBM / Langflow | 2026-08-04 | 2026-08-07 | Unknown |
| CVE-2026-18577 | N-able / N-central | 2026-08-03 | 2026-08-06 | Unknown |

---

*Total entries in CISA KEV catalog: 1661*