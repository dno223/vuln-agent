# Vulnerability Intelligence Report

**Date:** 2026-10-03  
**Generated:** 2026-10-03T13:02:42Z  

---

## Executive Summary

Our environment faces significant exposure from 70 high-severity vulnerabilities, including two critical CVEs scoring 9.8 and 9.9 affecting WordPress and GitLab AI components that could enable privilege escalation and unauthorized access. Additionally, CISA added 7 new actively exploited vulnerabilities to its Known Exploited Vulnerabilities catalog this week, targeting Fortinet, Cisco, Apple, and Zammad products. While none of our monitored CVEs currently appear in the KEV catalog, the breadth and severity of new disclosures demand immediate prioritization. Threat actors are actively exploiting several of these vulnerability classes in the wild, elevating organizational risk.

---

## Risk Narrative

The current threat landscape reflects a surge in vulnerability disclosures targeting widely deployed platforms including WordPress plugins, GitLab AI components, IoT devices, and enterprise networking products. A CVSS 9.9 GitLab vulnerability and a 9.8 WordPress privilege escalation flaw represent near-worst-case scenarios for unauthorized access and lateral movement. CISA's KEV additions for Fortinet, Cisco, and Apple products confirm active exploitation in the wild, signaling organized threat actor interest. SQL injection and stored XSS vulnerabilities further expand the attack surface across web-facing applications. Collectively, these exposures risk data breaches, operational disruption, and reputational harm if not addressed within defined remediation windows.

---

## Prioritized Action Items

1. Immediately patch GitLab AI Gateway to version 19.2.4 or later to remediate the CVSS 9.9 remote code execution vulnerability (CVE-2026-90970).
2. Update the Divi Membership WordPress plugin to a version beyond 2.2.0 to eliminate the critical privilege escalation vulnerability (CVE-2026-19652, CVSS 9.8).
3. Apply vendor patches immediately for all CISA KEV-listed products including Fortinet FortiMail, Cisco Catalyst SD-WAN Manager, Apple products, and Zammad.
4. Audit and restrict xdg-dbus-proxy deployments by upgrading to version 0.1.9 or later to prevent message-filtering bypass attacks (CVE-2026-94422).
5. Conduct an inventory review of all IoT devices using the Meari Cloud Platform and Tenda routers, isolating or patching affected units to remediate authorization and injection flaws.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-104610 | 10.0 | 2026-10-02 | A security vulnerability has been detected in Tenda HG7, HG9 and HG10 300001138_en_xpon. This impacts the function boaGe |
| CVE-2026-104611 | 9.1 | 2026-10-02 | A vulnerability was detected in Tenda AC9 15.03.02.13. Affected is an unknown function of the file /goform/fast_setting_ |
| CVE-2026-19652 | 9.8 | 2026-10-02 | The Divi Membership plugin for WordPress is vulnerable to Privilege Escalation in versions up to, and including, 2.2.0.  |
| CVE-2026-85215 | 7.1 | 2026-10-02 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in GG Soft Software S |
| CVE-2026-93875 | 7.2 | 2026-10-02 | The JetAppointment plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'friendlyTime' parameter in |
| CVE-2026-94422 | 8.8 | 2026-10-02 | An incorrect implementation of message filtering in xdg-dbus-proxy versions before 0.1.9 allows an attacker to bypass th |
| CVE-2026-104026 | 7.8 | 2026-10-02 | In Sapling SCM prior to v0.2.20260929-102736, control characters were allowed to be embedded in Git subtree URLs. A mali |
| CVE-2026-104637 | 7.3 | 2026-10-02 | A weakness has been identified in onetwothreeneth HospitalManagementSystem up to 9ef91ed6007314b6473110ed699dff76d158f61 |
| CVE-2026-90970 | 9.9 | 2026-10-02 | GitLab has remediated a vulnerability in the GitLab AI Gateway component affecting all versions of the AI Gateway from 1 |
| CVE-2026-101104 | 7.7 | 2026-10-02 | The Meari IoT Cloud Platform OpenAPI Service is vulnerable to an authorization flaw that allows authenticated users to m |
| CVE-2026-103622 | 8.8 | 2026-10-02 | Use after free in SVG in Google Chrome prior to 154.0.8037.97 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-103625 | 8.8 | 2026-10-02 | Type confusion in V8 in Google Chrome prior to 154.0.8037.97 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-103628 | 9.6 | 2026-10-02 | Out of bounds write in WebGL in Google Chrome prior to 154.0.8037.97 allowed a remote attacker to execute arbitrary code |
| CVE-2026-103648 | 9.1 | 2026-10-02 | Path traversal in image-downloader 4.3.0 allows an attacker who can control the download URL to cause downloaded respons |
| CVE-2026-104845 | 7.5 | 2026-10-02 | Seroval facilitates JS value stringification, including complex structures beyond JSON.stringify capabilities. Prior to  |
| CVE-2026-104846 | 9.8 | 2026-10-02 | Seroval facilitates JS value stringification, including complex structures beyond JSON.stringify capabilities. From 0.12 |
| CVE-2026-51907 | 8.1 | 2026-10-02 | In TaskingAI v0.3.0 in the QR Code Generator plugin save_base64_image function, a path traversal vulnerability allows at |
| CVE-2026-51916 | 7.5 | 2026-10-02 | TransformerOptimus SuperAGI v0.0.14 contains an incorrect access control vulnerability in delete_user_knowledge in super |
| CVE-2026-67989 | 7.5 | 2026-10-02 | crmne/ruby_llm at commit fa6f279847d6d7027814539d9c0dfc3bbdfd2a83 contains a polynomial-time regular expression denial-o |
| CVE-2026-104851 | 8.8 | 2026-10-02 | fsspec is a specification and Python implementation framework for filesystem interfaces. From 0.9.0 until 2026.6.0, fssp |
| CVE-2026-102795 | 9.3 | 2026-10-02 | Improper Access Control vulnerability in Apache Traffic Server.



This issue affects Apache Traffic Server: from 9.0.0  |
| CVE-2026-104861 | 7.5 | 2026-10-02 | probe-image-size gets image dimensions without downloading the entire file. Prior to 7.4.0, lib/parse_sync/svg.js and li |
| CVE-2014-125130 | 7.5 | 2026-10-02 | CodeArt Google MP3 Audio Player plugin (google-mp3-audio-player) for WordPress through 1.0.11 contains an unauthenticate |
| CVE-2020-37278 | 7.5 | 2026-10-02 | Weaver e-Bridge contains an unauthenticated arbitrary file read vulnerability that allows remote attackers to access arb |
| CVE-2023-54405 | 9.8 | 2026-10-02 | H3C CVM, the Cloud Virtualization Management component of the H3C CAS cloud platform, contains an unauthenticated arbitr |
| CVE-2026-103956 | 10.0 | 2026-10-02 | Missing authentication for critical function in the authentication dependency in Loom for AWS before 1.6.1 allowed remot |
| CVE-2026-103958 | 7.6 | 2026-10-02 | Server-side request forgery in the tool server and remote agent connection handling in Loom for AWS before 1.7.0 might a |
| CVE-2026-96940 | 8.8 | 2026-10-02 | Weak authorization in Microsoft Exchange Server allows an authenticated attacker to elevate privileges over a network. |
| CVE-2026-104019 | 9.0 | 2026-10-02 | OS command injection in the Studio Space startup validation script in Amazon SageMaker Distribution 2.x before 2.14.12,  |
| CVE-2026-104988 | 8.1 | 2026-10-02 | A flaw was found in Dogtag PKI (pki-core). The CMCAuthForEST authentication plugin fails open when an EST fullcmc enroll |
| CVE-2026-104991 | 7.1 | 2026-10-02 | Phproject before 1.8.7 contains a missing object-level authorization vulnerability in the REST API issue endpoints (sing |
| CVE-2026-39718 | 8.8 | 2026-10-02 | Cross-Site Request Forgery (CSRF) vulnerability in Webriti Wallstreet wallstreet allows Cross Site Request Forgery.This  |
| CVE-2026-82039 | 8.8 | 2026-10-02 | UTMStack before 11.2.16 contains a SQL injection vulnerability in UtmAssetGroupService.searchQueryBuilder() that allows  |
| CVE-2026-82041 | 9.9 | 2026-10-02 | UTMStack before 11.2.16 contains a missing authorization vulnerability in UTMIncidentCommandWebsocket.processCommand(),  |
| CVE-2026-82042 | 9.8 | 2026-10-02 | UTMStack before 11.2.16 contains an authentication bypass vulnerability that allows remote attackers to gain full admini |
| CVE-2026-82044 | 7.7 | 2026-10-02 | UTMStack before 11.2.16 contains a server-side request forgery vulnerability that allows authenticated attackers to make |
| CVE-2026-94591 | 8.4 | 2026-10-02 | Armatura One stores database and message-broker credentials in an install configuration file, encrypting them with AES-1 |
| CVE-2026-94592 | 8.4 | 2026-10-02 | Armatura One's database initialization routine assigns a fixed, vendor-defined password to the database superuser accoun |
| CVE-2026-94593 | 7.8 | 2026-10-02 | Armatura One's backup and restore routine records the full database connection command, including the superuser password |
| CVE-2026-95102 | 9.4 | 2026-10-02 | WebSocket endpoints lack proper authentication mechanisms, enabling attackers to impersonate charging stations. As a res |
| CVE-2026-97212 | 7.3 | 2026-10-02 | The WebSocket backend uses charging station identifiers to uniquely associate sessions but allows multiple endpoints to  |
| CVE-2026-97363 | 7.5 | 2026-10-02 | The WebSocket Application Programming Interface lacks restrictions on the number of authentication requests. This absenc |
| CVE-2026-84411 | 9.8 | 2026-10-02 | The web management service in affected RouterOS versions contains an integer underflow in its HTTP request body handling |
| CVE-2026-104433 | 7.5 | 2026-10-03 | Mooncake transfer engine before 0.3.12 contains an out-of-bounds read vulnerability in the readString function of includ |
| CVE-2026-104478 | 7.1 | 2026-10-03 | Formwork before 2.3.13 contains a path traversal vulnerability in BackupController that allows authenticated panel users |
| CVE-2026-105080 | 9.9 | 2026-10-03 | In ConvertX before 0.19.0, converters/calibre.ts does not block recipe files, and instead passes them to the ebook-conve |
| CVE-2026-93428 | 7.5 | 2026-10-03 | The Ultimate Member – User Profile, Registration, Login, Member Directory, Content Restriction & Membership Plugin plugi |
| CVE-2026-96270 | 7.2 | 2026-10-03 | The Ultimate Member – User Profile, Registration, Login, Member Directory, Content Restriction & Membership Plugin plugi |
| CVE-2026-92536 | 8.8 | 2026-10-03 | The Paid Membership Plugin, Ecommerce, User Registration Form, Login Form, User Profile & Restrict Content – ProfilePres |
| CVE-2026-92977 | 7.2 | 2026-10-03 | The Real Cookie Banner: GDPR & ePrivacy Cookie Consent plugin for WordPress is vulnerable to Stored Cross-Site Scripting |
| CVE-2026-97644 | 8.8 | 2026-10-03 | The Groundhogg — CRM, Newsletters, and Marketing Automation plugin for WordPress is vulnerable to Privilege Escalation v |
| CVE-2026-101923 | 8.1 | 2026-10-03 | The Photo Reviews for WooCommerce plugin for WordPress is vulnerable to Arbitrary Content Deletion in versions up to, an |
| CVE-2026-101928 | 7.2 | 2026-10-03 | The Magic Tooltips For Contact Form 7 plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'author' |
| CVE-2026-103913 | 7.5 | 2026-10-03 | The GeoDirectory plugin for WordPress is vulnerable to SQL Injection via the stored latitude/longitude coordinates of a  |
| CVE-2026-87091 | 7.2 | 2026-10-03 | The Welcart e-Commerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Settlement Notification Par |
| CVE-2026-93430 | 7.2 | 2026-10-03 | The GD Rating System plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'title' and 'url' Render Args |
| CVE-2026-96564 | 7.2 | 2026-10-03 | The SEOPress – AI SEO Plugin & On-site SEO plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Author  |
| CVE-2026-96575 | 7.2 | 2026-10-03 | The Transliterator – Multilingual and Multi-script Text Conversion plugin for WordPress is vulnerable to Stored Cross-Si |
| CVE-2026-96650 | 7.2 | 2026-10-03 | The Strong Testimonials plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'platform_user_photo' Cust |
| CVE-2026-97337 | 7.5 | 2026-10-03 | The Simple Membership plugin for WordPress is vulnerable to unauthorized modification of data and sensitive information  |
| CVE-2026-97341 | 7.2 | 2026-10-03 | The Visitor Traffic Real Time Statistics plugin for WordPress is vulnerable to Stored DOM-Based Cross-Site Scripting via |
| CVE-2026-18443 | 8.8 | 2026-10-03 | The Smart Manager – Advanced WooCommerce Bulk Edit & Inventory Management plugin for WordPress is vulnerable to generic  |
| CVE-2026-75028 | 7.5 | 2026-10-03 | The WPCafe – Restaurant Menu, Online Food Ordering & Table Booking System plugin for WordPress is vulnerable to Local Fi |
| CVE-2026-87115 | 9.1 | 2026-10-03 | The VikAppointments Services Booking Calendar plugin for WordPress is vulnerable to arbitrary file deletion due to insuf |
| CVE-2026-93889 | 7.2 | 2026-10-03 | The Mail logging – WP Mail Catcher plugin for WordPress is vulnerable to Stored Cross-Site Scripting via PHPMailer 'wp_m |
| CVE-2026-94505 | 8.1 | 2026-10-03 | The Nelio Content – Editorial Calendar & Social Media Auto-Posting plugin for WordPress is vulnerable to authorization b |
| CVE-2026-96267 | 7.5 | 2026-10-03 | The WP Visitor Statistics (Real Time Traffic) plugin for WordPress is vulnerable to generic SQL Injection via the 'fullR |
| CVE-2026-97660 | 7.2 | 2026-10-03 | The WPC Product Options for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via wpcpo-* Ar |
| CVE-2026-92084 | 9.1 | 2026-10-03 | The The Beaver Builder Page Builder – Drag and Drop Website Builder plugin for WordPress is vulnerable to arbitrary shor |
| CVE-2026-105105 | 9.8 | 2026-10-03 | CWE-306: Missing Authentication for Critical Function in the ait.core.server telemetry and command broker (ait-server) i |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-102490 | Zammad GmbH / Zammad | 2026-10-02 | 2026-10-05 | Unknown |
| CVE-2026-102489 | Zammad GmbH / Zammad | 2026-10-02 | 2026-10-05 | Unknown |
| CVE-2026-104286 | Fortinet / FortiMail | 2026-10-01 | 2026-10-04 | Unknown |
| CVE-2026-76504 | Cisco / Catalyst SD-WAN Manager | 2026-09-30 | 2026-10-03 | Unknown |
| CVE-2026-86950 | Apple / Multiple Products | 2026-09-29 | 2026-10-02 | Unknown |
| CVE-2026-88772 | Citrix / NetScaler | 2026-09-27 | 2026-09-30 | Unknown |
| CVE-2026-88771 | Citrix / NetScaler | 2026-09-27 | 2026-09-30 | Unknown |

---

*Total entries in CISA KEV catalog: 1733*