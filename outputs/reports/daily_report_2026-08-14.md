# Vulnerability Intelligence Report

**Date:** 2026-08-14  
**Generated:** 2026-08-14T09:05:42Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011Ce2NgEakqAMA2fMMBu9yQ'}

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
| CVE-2026-15413 | 10.0 | 2026-08-13 | The Link Factory WordPress plugin is a backdoor. Distributed as a "homepage sentence publisher", it exposes an operator- |
| CVE-2026-19481 | 7.5 | 2026-08-13 | @fastify/busboy is a multipart form-data parser. In versions 1.0.0 through 3.2.0, an attacker who can submit multipart f |
| CVE-2026-19484 | 7.5 | 2026-08-13 | @fastify/busboy is a multipart form-data parser. In versions 3.1.0 through 3.2.0, a remote unauthenticated attacker can  |
| CVE-2026-59499 | 8.6 | 2026-08-13 | CWE-200: Exposure of Sensitive
Information to an Unauthorized Actor |
| CVE-2026-59500 | 10.0 | 2026-08-13 | CWE-287: Improper Authentication |
| CVE-2026-59501 | 8.2 | 2026-08-13 | CWE-284: Improper Access Control |
| CVE-2026-59503 | 9.1 | 2026-08-13 | CWE-200: Exposure of Sensitive Information to an Unauthorized Actor CWE-359: Exposure of Private Personal Information to |
| CVE-2026-59504 | 9.1 | 2026-08-13 | CWE-602: Client-Side Enforcement of Server-Side Security |
| CVE-2026-59505 | 8.6 | 2026-08-13 | CWE-284: Improper Access Control |
| CVE-2026-59506 | 9.3 | 2026-08-13 | CWE-306: Missing Authentication for Critical Function |
| CVE-2026-59507 | 9.3 | 2026-08-13 | CWE-798: Use of Hard-coded Credentials CWE-200: Exposure of Sensitive Information to an Unauthorized Actor CWE-284: Impr |
| CVE-2026-12263 | 8.8 | 2026-08-13 | Zohocorp ManageEngine Password Manager Pro versions before 13232 and PAM360 versions before 8551 are vulnerable to an au |
| CVE-2026-73608 | 8.6 | 2026-08-13 | SiYuan's development branch (endpoint introduced by commit 9b8e8956f, not present in v3.7.3 or master, patched in v3.7.4 |
| CVE-2026-73612 | 8.1 | 2026-08-13 | File Browser before v2.63.22 fails to validate access rules for descendants during recursive copy, rename, and delete op |
| CVE-2026-73613 | 8.2 | 2026-08-13 | filebrowser versions before 2.63.19 contain an out-of-scope file deletion vulnerability in the TUS upload cache eviction |
| CVE-2026-73614 | 8.8 | 2026-08-13 | Network-AI ClaudeHookBridge before 5.15.1 truncates the target string to 500 characters before evaluating denyPatterns,  |
| CVE-2026-73615 | 8.8 | 2026-08-13 | Network-AI versions before 5.15.1 contain a security matcher bypass vulnerability where SandboxPolicy evaluates raw comm |
| CVE-2026-73617 | 7.1 | 2026-08-13 | Budibase before 3.40.0 contains a NoSQL injection vulnerability in the MongoDB datasource integration where user-supplie |
| CVE-2026-73618 | 8.3 | 2026-08-13 | Budibase Server before 3.40.0 contains a NoSQL injection vulnerability in the MongoDB query execution endpoint where use |
| CVE-2026-73620 | 8.1 | 2026-08-13 | GitPython before 3.1.57 fails to guard git option forwarding in IndexFile.checkout() and TagReference.create(), allowing |
| CVE-2026-73622 | 7.5 | 2026-08-13 | GitPython before 3.1.55 fails to disable environment variable expansion in Remote.create() and Submodule.add() URL handl |
| CVE-2026-73623 | 7.5 | 2026-08-13 | GitPython before 3.1.54 contains an incomplete denylist in unsafe_git_clone_options that omits --template, allowing atta |
| CVE-2026-73624 | 8.1 | 2026-08-13 | GitPython versions before 3.1.54 contain an arbitrary file overwrite vulnerability in the Diffable.diff method that fail |
| CVE-2026-73625 | 8.8 | 2026-08-13 | GitPython versions before 3.1.54 contain a remote code execution vulnerability in the check_unsafe_options guard that ca |
| CVE-2026-73629 | 8.5 | 2026-08-13 | Serendipity before 2.6.0 contains a server-side request forgery vulnerability in the serendipity_url_allowed() filter th |
| CVE-2026-14662 | 8.8 | 2026-08-13 | Integer wraparound in PostgreSQL tsvector and tsquery data type functions allows an unprivileged database user to cause  |
| CVE-2026-14664 | 8.8 | 2026-08-13 | Heap buffer overflow in PostgreSQL regexp allows the query author to execute arbitrary code as the operating system user |
| CVE-2026-14668 | 8.1 | 2026-08-13 | Type confusion regarding input of PostgreSQL ctid data type selectivity estimator allows an object creator to view a cal |
| CVE-2026-14669 | 8.8 | 2026-08-13 | Heap buffer overflow in PostgreSQL to_char(timestamptz) allows the party choosing the timezone to execute arbitrary code |
| CVE-2026-14670 | 8.8 | 2026-08-13 | Heap buffer overflow in PostgreSQL plperl return of a tied hash allows the function owner to execute arbitrary code as t |
| CVE-2026-14671 | 8.8 | 2026-08-13 | Type confusion in PostgreSQL module "refint" allows an object creator to execute arbitrary code as the operating system  |
| CVE-2026-14676 | 8.8 | 2026-08-13 | Heap buffer overflow in PostgreSQL pg_stat_statements allows the query author to execute arbitrary code as the operating |
| CVE-2026-14677 | 8.8 | 2026-08-13 | Integer wraparound in PostgreSQL 32-bit builds of pltcl and plperl allows an object creator to cause the server to under |
| CVE-2026-14679 | 8.2 | 2026-08-13 | Stack buffer overflow in PostgreSQL argument name matching allows an object creator to achieve unknown impacts via OUT p |
| CVE-2026-14680 | 8.8 | 2026-08-13 | Type confusion with PostgreSQL "internal" data type arguments allows any user to execute arbitrary code as the operating |
| CVE-2026-15741 | 8.8 | 2026-08-13 | SQL injection in PostgreSQL EXTRACT() deparse allows an object owner to execute arbitrary SQL as a superuser via a hosti |
| CVE-2026-15742 | 8.8 | 2026-08-13 | Integer wraparound in PostgreSQL fuzzystrmatch allows a user to direct writes to a huge range of addresses, executing ar |
| CVE-2026-16238 | 8.8 | 2026-08-13 | Type confusion in PostgreSQL pg_restore_attribute_stats() allows an object creator to execute arbitrary code as the oper |
| CVE-2026-16239 | 8.8 | 2026-08-13 | Type confusion in PostgreSQL "portal"/cursor lifecycle allows a user to execute arbitrary code as the operating system u |
| CVE-2026-18408 | 8.8 | 2026-08-13 | Untrusted data inclusion in pg_dump in PostgreSQL allows a malicious superuser of the origin server to inject arbitrary  |
| CVE-2026-19385 | 8.8 | 2026-08-13 | Heap buffer overflow in PostgreSQL pg_dump of long function transform lists allows an object creator to execute arbitrar |
| CVE-2026-49478 | 8.7 | 2026-08-13 | Fulcio is a certificate authority for issuing code signing certificates for an OpenID Connect (OIDC) identity. Versions  |
| CVE-2026-49827 | 9.8 | 2026-08-13 | WebErpMesv2 is a Resource Management and Manufacturing execution system Web for industry. Versions 1.19 and prior allow  |
| CVE-2026-6464 | 8.1 | 2026-08-13 | Untrusted data inclusion in PostgreSQL psql COPY may allow a server administrator to elicit execution of data lines as p |
| CVE-2026-6471 | 7.2 | 2026-08-13 | Missing authorization in PostgreSQL logical decoding allows a non-superuser holding REPLICATION privilege to dlopen any  |
| CVE-2026-27345 | 7.5 | 2026-08-13 | Unauthenticated Broken Access Control in Taxi Booking Manager for WooCommerce <= 2.0.3 versions. |
| CVE-2026-27380 | 7.2 | 2026-08-13 | Editor PHP Object Injection in Car Rental Manager <= 1.3.9 versions. |
| CVE-2026-27535 | 7.1 | 2026-08-13 | Subscriber Broken Access Control in Solace Extra <= 1.6.0 versions. |
| CVE-2026-27536 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in MailChimp Subscribe Forms  <= 4.3.3 versions. |
| CVE-2026-27538 | 7.5 | 2026-08-13 | Unauthenticated SQL Injection in WP Directory Kit <= 1.5.4 versions. |
| CVE-2026-27539 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in Welcart e-Commerce <= 2.11.31 versions. |
| CVE-2026-27543 | 8.1 | 2026-08-13 | Unauthenticated Privilege Escalation in MStore API <= 4.20.0 versions. |
| CVE-2026-27544 | 10.0 | 2026-08-13 | Unauthenticated Remote Code Execution (RCE) in QA Analytics <= 5.2.0.0 versions. |
| CVE-2026-28001 | 9.3 | 2026-08-13 | Unauthenticated SQL Injection in WP Directory Kit <= 1.5.4 versions. |
| CVE-2026-28002 | 8.5 | 2026-08-13 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Arraytics Booktics |
| CVE-2026-28003 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in Maspik – Spam blacklist <= 2.9.1 versions. |
| CVE-2026-28004 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in Business Directory <= 6.4.25 versions. |
| CVE-2026-28008 | 9.8 | 2026-08-13 | Unauthenticated Broken Authentication in OAuth Single Sign On – SSO (OAuth Client) <= 7.0.0 versions. |
| CVE-2026-28142 | 9.3 | 2026-08-13 | Unauthenticated SQL Injection in Web Directory Free <= 1.7.13 versions. |
| CVE-2026-28148 | 9.8 | 2026-08-13 | Unauthenticated Bypass Vulnerability in Headless Single Sign On <= 1.6 versions. |
| CVE-2026-28149 | 9.8 | 2026-08-13 | Unauthenticated PHP Object Injection in Headless Single Sign On <= 1.6 versions. |
| CVE-2026-28156 | 8.5 | 2026-08-13 | Subscriber SQL Injection in Do Lasso <= 358 versions. |
| CVE-2026-28157 | 7.5 | 2026-08-13 | Subscriber Path Traversal in Do Lasso <= 358 versions. |
| CVE-2026-28158 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in Do Lasso <= 358 versions. |
| CVE-2026-28161 | 8.8 | 2026-08-13 | Subscriber Privilege Escalation in Service Finder Booking <= 6.2 versions. |
| CVE-2026-28168 | 8.5 | 2026-08-13 | Subscriber SQL Injection in CubeWP <= 1.1.30 versions. |
| CVE-2026-28170 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in Blog Floating Button <= 1.4.20 versions. |
| CVE-2026-28173 | 7.1 | 2026-08-13 | Customer Arbitrary Content Deletion in WP Event SOlution <= 4.1.19 versions. |
| CVE-2026-28175 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in Visitors Traffic Real Time Statistics <= 8.11 versions. |
| CVE-2026-28176 | 8.8 | 2026-08-13 | Unauthenticated PHP Object Injection in Booking Activities <= 1.18.4 versions. |
| CVE-2026-28185 | 9.8 | 2026-08-13 | Unauthenticated Broken Authentication in Log in with Google <= 1.4.2 versions. |
| CVE-2026-28186 | 8.1 | 2026-08-13 | Subscriber Broken Access Control in Travelfic Toolkit <= 1.5.1 versions. |
| CVE-2026-28187 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in Knowledge Base for Documentation, FAQs with AI Assistance <= 17.211.0 vers |
| CVE-2026-28188 | 7.3 | 2026-08-13 | Unauthenticated Broken Access Control in Hydra Booking <= 1.2.2 versions. |
| CVE-2026-28189 | 7.4 | 2026-08-13 | Unauthenticated Arbitrary File Deletion in Participants Database <= 2.7.8.4 versions. |
| CVE-2026-48702 | 7.5 | 2026-08-13 | Rekor is a software supply chain transparency log. Starting in version 0.3.0 and prior to version 1.5.2, the `Package.Un |
| CVE-2026-61960 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in WP Full Stripe Free <= 8.5.0 versions. |
| CVE-2026-61962 | 10.0 | 2026-08-13 | Unauthenticated Arbitrary Code Execution in WP BASE Booking <= 6.3.0 versions. |
| CVE-2026-61965 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in GeekyBot <= 1.2.6 versions. |
| CVE-2026-61966 | 9.3 | 2026-08-13 | Subscriber SQL Injection in WPJAM Basic <= 7.0.1 versions. |
| CVE-2026-61967 | 9.8 | 2026-08-13 | Unauthenticated Privilege Escalation in miniorange otp verification <= 5.5.1 versions. |
| CVE-2026-61969 | 9.3 | 2026-08-13 | Unauthenticated SQL Injection in Listdom <= 5.6.0 versions. |
| CVE-2026-61974 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in Mang Board WP <= 2.3.4 versions. |
| CVE-2026-61979 | 8.1 | 2026-08-13 | Unauthenticated Privilege Escalation in SAML SP Single Sign On <= 5.4.3 versions. |
| CVE-2026-61980 | 7.5 | 2026-08-13 | Unauthenticated Arbitrary File Download in OMGF Pro <= 5.2.7 versions. |
| CVE-2026-61984 | 7.5 | 2026-08-13 | Unauthenticated Broken Access Control in WPMobile.App <= 11.77 versions. |
| CVE-2026-65580 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in Agrion <= 1.0.0 versions. |
| CVE-2026-65582 | 7.7 | 2026-08-13 | Subscriber Arbitrary File Download in AI Hub <= 1.3.10 versions. |
| CVE-2026-66424 | 9.8 | 2026-08-13 | Unauthenticated Privilege Escalation in SMS Alert Order Notifications <= 3.9.7 versions. |
| CVE-2026-66426 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in WP-Stats <= 2.56 versions. |
| CVE-2026-66429 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in Visitor Traffic Real Time Statistics Pro <= 11.10 versions. |
| CVE-2026-66430 | 8.5 | 2026-08-13 | Subscriber SQL Injection in Visitor Traffic Real Time Statistics Pro <= 11.10 versions. |
| CVE-2026-66431 | 7.5 | 2026-08-13 | Unauthenticated Broken Access Control in Bitcoin Lightning Payment Gateway for WooCommerce (via CLINK) <= 1.0.7 versions |
| CVE-2026-66432 | 7.5 | 2026-08-13 | Subscriber Sensitive Data Exposure in WPJAM Basic <= 7.0.2.1 versions. |
| CVE-2026-66436 | 9.3 | 2026-08-13 | Unauthenticated SQL Injection in Active Products Tables for WooCommerce <= 1.1.1 versions. |
| CVE-2026-66441 | 7.5 | 2026-08-13 | Unauthenticated Broken Access Control in MultiVendorX <= 5.0.10 versions. |
| CVE-2026-66443 | 7.5 | 2026-08-13 | Unauthenticated Sensitive Data Exposure in REST API Log <= 1.7.1 versions. |
| CVE-2026-66446 | 9.3 | 2026-08-13 | Subscriber SQL Injection in If-So Dynamic Content Personalization <= 1.10 versions. |
| CVE-2026-66449 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in  Geo Mashup <= 1.13.18 versions. |
| CVE-2026-66450 | 8.1 | 2026-08-13 | Unauthenticated Local File Inclusion in  Geo Mashup <= 1.13.18 versions. |
| CVE-2026-66453 | 9.8 | 2026-08-13 | Unauthenticated Broken Authentication in Salon booking system <= 10.30.26 versions. |
| CVE-2026-66458 | 9.3 | 2026-08-13 | Unauthenticated SQL Injection in RealPress <= 1.1.2 versions. |
| CVE-2026-66461 | 7.5 | 2026-08-13 | Unauthenticated Broken Access Control in SMEPay: UPI Gateway for WooCommerce <= 1.0.5 versions. |
| CVE-2026-66462 | 7.5 | 2026-08-13 | Unauthenticated Sensitive Data Exposure in WooCommerce Appointments <= 5.3.8 versions. |
| CVE-2026-66463 | 7.5 | 2026-08-13 | Unauthenticated Sensitive Data Exposure in iCARRY <= 2.9 versions. |
| CVE-2026-66465 | 9.8 | 2026-08-13 | Unauthenticated Broken Authentication in Cartify <= 1.3.0.1 versions. |
| CVE-2026-66466 | 7.5 | 2026-08-13 | Unauthenticated Broken Access Control in StoreGrowth: Smart Sales Booster for WooCommerce \| BOGO, Upsells, Direct Checko |
| CVE-2026-66468 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in Local Delivery Drivers for WooCommerce <= 3.0.0 versions. |
| CVE-2026-66469 | 7.5 | 2026-08-13 | Unauthenticated Broken Access Control in Arvow AI SEO Writer <= 1.5.3 versions. |
| CVE-2026-66472 | 9.3 | 2026-08-13 | Unauthenticated SQL Injection in Everest Backup <= 2.3.12 versions. |
| CVE-2026-66478 | 9.3 | 2026-08-13 | Unauthenticated SQL Injection in Church Admin <= 5.1.1 versions. |
| CVE-2026-66653 | 8.1 | 2026-08-13 | Unauthenticated Local File Inclusion in Barista <= 2.5.1 versions. |
| CVE-2026-66655 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in MultiParcels Shipping For WooCommerce <= 1.30.36 versions. |
| CVE-2026-66656 | 8.1 | 2026-08-13 | Unauthenticated Local File Inclusion in Foton Core <= 1.1.1 versions. |
| CVE-2026-66657 | 8.1 | 2026-08-13 | Unauthenticated Local File Inclusion in Biagiotti Core <= 2.1.1 versions. |
| CVE-2026-66658 | 8.5 | 2026-08-13 | Subscriber SQL Injection in Reviewer <= 3.14.2 versions. |
| CVE-2026-66661 | 7.7 | 2026-08-13 | Subscriber Privilege Escalation in Directories Pro <= 2.0.5 versions. |
| CVE-2026-66691 | 9.8 | 2026-08-13 | Unauthenticated Broken Access Control in Nokri <= 1.6.6 versions. |
| CVE-2026-66697 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in Colissimo Officiel : Méthodes de livraison pour WooCommerce <= 2.10.0 vers |
| CVE-2026-66698 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in SureDash <= 1.10.1 versions. |
| CVE-2026-66700 | 7.1 | 2026-08-13 | Unauthenticated Cross Site Scripting (XSS) in Smart Online Order for Clover <= 1.6.1 versions. |
| CVE-2026-66704 | 7.2 | 2026-08-13 | Unauthenticated Server Side Request Forgery (SSRF) in Gutenverse Companion <= 2.5.1 versions. |
| CVE-2026-67986 | 8.4 | 2026-08-13 | amazing-print/amazing_print at commit dc890dfafdf07088ea901df53c19c2710e5c5234 contains a Ruby code injection condition  |
| CVE-2026-67991 | 7.5 | 2026-08-13 | crmne/ruby_llm at commit fa6f279847d6d7027814539d9c0dfc3bbdfd2a83 contains a polynomial-time regular expression denial-o |
| CVE-2026-73188 | 7.5 | 2026-08-13 | Unauthenticated Sensitive Data Exposure in KiviCare <= 4.5.1 versions. |
| CVE-2026-73346 | 7.6 | 2026-08-13 | Administrator SQL Injection in MailChimp For WooCommerce < 6.2 versions. |
| CVE-2026-12036 | 7.1 | 2026-08-13 | An improper link following vulnerability was reported in the VantageCoreAddin for Lenovo Vantage and Lenovo Commercial V |
| CVE-2026-14456 | 7.5 | 2026-08-13 | Issue summary: When an OpenSSL QUIC server (Listener SSL object) processes
valid QUIC Initial packets for unknown destin |
| CVE-2026-15994 | 7.0 | 2026-08-13 | During an internal security assessment, an improper link following vulnerability was identified in Lenovo Vantage and Le |
| CVE-2026-16101 | 8.8 | 2026-08-13 | Spoofing an already bonded device can force either RS9116W or SiWx917 to re-pair/bond with a rogue device. See V1 in BLE |
| CVE-2026-19291 | 8.8 | 2026-08-13 | Bluetooth re-pairing with an existing device can use a lower security level. RS9116W and SiWx91x impacted. See V3 in the |
| CVE-2026-19292 | 8.8 | 2026-08-13 | Re-pairing with a legitimate device can use a lower security level than
previous making brute-forcing the LTK easier. Se |
| CVE-2026-19293 | 8.8 | 2026-08-13 | SMP security request (from peripheral) does not include the maximum
encryption key size supported. Using a key with less |
| CVE-2026-28154 | 7.1 | 2026-08-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in snstheme Samex - C |
| CVE-2026-49857 | 7.4 | 2026-08-13 | auth-fetch-mcp is an MCP server that lets AI assistants fetch content from authenticated web pages. Version 3.0.1 implem |
| CVE-2026-53783 | 8.1 | 2026-08-13 | rsync before 3.5.0 contains a time-of-check to time-of-use (TOCTOU) race condition vulnerability in the rrsync restricte |
| CVE-2026-53784 | 7.1 | 2026-08-13 | rsync before 3.5.0 contains a path traversal vulnerability that allows remote clients to access files outside the intend |
| CVE-2026-53785 | 7.1 | 2026-08-13 | rsync before 3.5.0 contains a path traversal vulnerability that allows a malicious sender to write files outside the int |
| CVE-2026-53790 | 8.1 | 2026-08-13 | rsync before 3.5.0 contains multiple command and argument injection vulnerabilities that allow attackers to execute arbi |
| CVE-2026-53791 | 9.1 | 2026-08-13 | rsync daemon before 3.5.0 contains an IP address spoofing vulnerability that allows unauthenticated remote attackers to  |
| CVE-2026-53793 | 7.4 | 2026-08-13 | rsync before 3.5.0 contains a path confinement bypass vulnerability that allows remote clients to escape the intended in |
| CVE-2026-53795 | 8.1 | 2026-08-13 | rsync before 3.5.0 contains an arbitrary file write vulnerability that allows attackers to write files outside the inten |
| CVE-2026-53802 | 7.1 | 2026-08-13 | rsync before 3.5.0 contains an arbitrary file read vulnerability that allows attackers to read files accessible to the r |
| CVE-2026-53803 | 7.8 | 2026-08-13 | rsync before 3.5.0 contains a symlink following vulnerability that allows local attackers to overwrite arbitrary files b |
| CVE-2026-63423 | 7.8 | 2026-08-13 | During an internal security assessment, a potential vulnerability was discovered in Lenovo Accessories and Display Manag |
| CVE-2026-63424 | 7.3 | 2026-08-13 | During an internal security assessment, an improperly protected key was discovered in Lenovo Dock Manager that could all |
| CVE-2026-63425 | 7.8 | 2026-08-13 | During an internal security assessment, a potential improper permissions vulnerability was discovered in Lenovo Dock Man |
| CVE-2026-63426 | 7.1 | 2026-08-13 | During an internal security assessment, a potential vulnerability was discovered in Lenovo Dock Manager that could allow |
| CVE-2026-66256 | 7.2 | 2026-08-13 | ** UNSUPPORTED WHEN ASSIGNED ** Deserialization of Untrusted Data vulnerability in Apache Shindig.

This issue affects A |
| CVE-2026-68451 | 7.8 | 2026-08-13 | In the Linux kernel, the following vulnerability has been resolved:

s390/zcrypt: Validate length for CCA ECC private ke |
| CVE-2026-68452 | 7.8 | 2026-08-13 | In the Linux kernel, the following vulnerability has been resolved:

s390/zcrypt: Validate length for CCA AES cipher key |
| CVE-2026-68453 | 7.1 | 2026-08-13 | In the Linux kernel, the following vulnerability has been resolved:

s390/zcrypt: Fix buffer over-read in cca_cipher2pro |
| CVE-2026-68454 | 8.8 | 2026-08-13 | In the Linux kernel, the following vulnerability has been resolved:

KVM: s390: pci: Fix handling of AIF enable without  |
| CVE-2026-6387 | 7.0 | 2026-08-13 | A potential authentication bypass vulnerability was reported in Lenovo System Update that could allow a local authentica |
| CVE-2026-70452 | 7.4 | 2026-08-13 | rsync 3.1.0 before 3.5.0 contains an access control bypass vulnerability that allows remote attackers to circumvent host |
| CVE-2026-70453 | 7.5 | 2026-08-13 | rsync before 3.5.0 contains an algorithmic complexity vulnerability in the hash_search() function that allows a remote a |
| CVE-2026-70454 | 8.0 | 2026-08-13 | rsync 3.2.0 through 3.2.3 (openssl mode) and rsync-ssl through 3.4.4 (stunnel mode) contain a TLS certificate validation |
| CVE-2026-70455 | 7.5 | 2026-08-13 | rsync 3.4.2 before 3.5.0 contains a denial of service vulnerability that allows a remote sender to exhaust system resour |
| CVE-2026-70456 | 8.2 | 2026-08-13 | rsync 3.0.1 before 3.5.0 contains an out-of-bounds write vulnerability in the read_args() function that allows a malicio |
| CVE-2026-70458 | 8.2 | 2026-08-13 | rsync 3.0.0 before 3.5.0 contains an out-of-bounds write vulnerability that allows attackers to corrupt memory by trigge |
| CVE-2026-70460 | 8.1 | 2026-08-13 | rsync 2.3.3 before 3.5.0 contains a path traversal vulnerability that allows a malicious sender to escape the module roo |
| CVE-2026-70461 | 8.2 | 2026-08-13 | rsync 3.2.5 before 3.5.0 contains a heap out-of-bounds write vulnerability that allows remote unauthenticated attackers  |
| CVE-2026-70463 | 8.1 | 2026-08-13 | rsync 3.1.0 before 3.5.0 contains an authorization bypass in auth users directive parsing. The auth users parser uses co |
| CVE-2026-70464 | 7.5 | 2026-08-13 | rsync daemon 2.0.0 before 3.5.0 contains a denial of service vulnerability that allows unauthenticated remote attackers  |
| CVE-2026-73505 | 7.8 | 2026-08-13 | Oh My Posh is the most customisable and low-latency cross platform/shell prompt renderer. Prior to 29.35.1, the setStyle |
| CVE-2026-73507 | 7.5 | 2026-08-13 | Netty is an asynchronous, event-driven network application framework. Prior to 4.1.136.Final and 4.2.16.Final, io.netty. |
| CVE-2026-73509 | 7.6 | 2026-08-13 | OpenList a file list program that supports multiple storage. Prior to 4.2.4, the authenticated /api/fs/batch_rename hand |
| CVE-2026-19710 | 7.3 | 2026-08-13 | A vulnerability was found in SourceCodester Simple Student Information System. Affected by this vulnerability is an unkn |
| CVE-2026-73514 | 8.8 | 2026-08-13 | The address_standardizer extension for PostGIS through 3.7.0, fixed in commit 423570b, contains an out-of-bounds write v |
| CVE-2026-73515 | 8.1 | 2026-08-13 | PostGIS before 3.7.0beta2 contains an out-of-bounds read vulnerability that allows attackers to cause memory disclosure  |
| CVE-2026-73532 | 9.8 | 2026-08-13 | Fluent Forms Pro 6.2.7 contains an embedded malicious code vulnerability introduced via a tampered plugin build served t |
| CVE-2026-73533 | 9.8 | 2026-08-13 | Ninja Tables Pro 5.2.11 contains an embedded malicious code vulnerability introduced via a tampered plugin build served  |
| CVE-2026-73570 | 8.9 | 2026-08-13 | A remote code execution vulnerability exists in Zimbra Collaboration (ZCS) before 10.1.20 when the optional zimbra-snmp  |
| CVE-2026-73670 | 7.2 | 2026-08-13 | A CMS contains a SQL injection vulnerability in admin/db_data.php at line 509 that allows authenticated administrators t |
| CVE-2026-24791 | 8.1 | 2026-08-13 | Public-only tokens bypass private-resource restrictions on `/api/v1/user` self routes |
| CVE-2026-58416 | 7.1 | 2026-08-13 | Fork-PR Actions task can read a third private repository via the collaborative-owner branch (missing fork-PR guard) |
| CVE-2026-59109 | 8.8 | 2026-08-13 | SQL injection in the Zalktis accounting application via
trading-partner-controlled text fields in received electronic in |
| CVE-2026-73266 | 7.1 | 2026-08-13 | A flaw was found in the clusterclaims-controller component of Multicluster Engine (MCE). An authenticated tenant can exp |
| CVE-2019-25765 | 7.5 | 2026-08-13 | ASP-CMS contains a SQL injection vulnerability in the commentList.asp endpoint that allows unauthenticated remote attack |
| CVE-2024-58374 | 7.5 | 2026-08-13 | Hongjing e-HR contains an unauthenticated SQL injection vulnerability in the getSdutyTree servlet endpoint that allows r |
| CVE-2026-18428 | 8.8 | 2026-08-13 | A SQL query validation bypass in the Flint extension query handler in the OpenSearch SQL plugin allows a remote authenti |
| CVE-2026-67614 | 9.8 | 2026-08-13 | CyberPanel before 3.0.0 contains a hard-coded JWT secret vulnerability in the WebTerminal FastAPI SSH service that allow |
| CVE-2026-72741 | 8.1 | 2026-08-13 | Rainbond through 6.9.7 contains a broken access control vulnerability in the CheckToken function that allows authenticat |
| CVE-2026-73561 | 7.5 | 2026-08-13 | Hub is a Node.js WebSocket server and client with added features. Prior to 0.2.16, every incoming unauthenticated WebSoc |
| CVE-2026-73566 | 7.5 | 2026-08-13 | node-tar is a tar archive manipulation library for Node.js. Prior to 7.5.21, node-tar's filesFilter in src/list.ts uses  |
| CVE-2026-73567 | 9.1 | 2026-08-13 | sm-crypto provides JavaScript implementations of the Chinese cryptographic algorithms SM2, SM3, and SM4. Prior to 0.5.0, |
| CVE-2026-73568 | 7.5 | 2026-08-13 | py-libp2p is the Python implementation of the libp2p networking stack. In 0.7.0 and earlier, the yamux handle_incoming() |
| CVE-2026-73643 | 7.5 | 2026-08-13 | js-yaml is a JavaScript YAML parser and dumper. From 5.0.0 until 5.2.2, parsing a small YAML document can take exponenti |
| CVE-2026-73644 | 9.6 | 2026-08-13 | OpenDJ is an LDAPv3 compliant directory service. Prior to 5.1.2, the SASL PLAIN authorization identity path in opendj-se |
| CVE-2026-73649 | 9.8 | 2026-08-13 | Velocity.js is a JavaScript implementation of the Apache Velocity template engine. Prior to 2.1.7, the earlier fix for C |
| CVE-2026-17197 | 8.1 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to bypass security restrictions due to improper validation of |
| CVE-2026-17220 | 8.2 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to cause a denial of service and modify authentication metada |
| CVE-2026-18071 | 7.8 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a local attacker to gain elevated privileges due to improper privilege manageme |
| CVE-2026-72777 | 8.6 | 2026-08-13 | Next AI Draw.io through 0.4.16 contains a server-side request forgery vulnerability in the POST /api/parse-url endpoint  |
| CVE-2026-73482 | 8.1 | 2026-08-13 | phpList before 3.7.0-RC5 contains a cross-site request forgery (CSRF) vulnerability in lists/admin/admins.php. The admin |
| CVE-2026-73650 | 8.2 | 2026-08-13 | SVGO, short for SVG Optimizer, is a Node.js library and command-line application for optimizing SVG files. From version  |
| CVE-2026-73653 | 9.4 | 2026-08-13 | Vitest is a testing framework powered by Vite. Prior to versions 3.2.7, 4.1.10, and 5.0.0-beta.6, Browser Mode provider  |
| CVE-2026-13365 | 7.1 | 2026-08-13 | IBM Planning Analytics 2.0, and 2.1 Local is vulnerable to cross-site request forgery which could allow an attacker to e |
| CVE-2026-13460 | 7.5 | 2026-08-13 | IBM Storage Scale 5.2.3.0 through 5.2.3.8, and 6.0.0.0 through 6.0.1.0 GUI contains a hardcoded token in the source code |
| CVE-2026-14525 | 9.4 | 2026-08-13 | IBM WebSphere Application Server - Liberty 17.0.0.3 through 26.0.0.8 IBM WebSphere Application Server Liberty is vulnera |
| CVE-2026-14875 | 7.3 | 2026-08-13 | IBM i Access Client Solutions 1.1.2.0 through 1.1.9.13 is vulnerable to arbitrary code execution on Windows when install |
| CVE-2026-16674 | 8.8 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote authenticated attacker to execute arbitrary code due to an untrusted s |
| CVE-2026-16722 | 8.8 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote authenticated attacker to obtain unauthorized privileges due to improp |
| CVE-2026-16815 | 8.6 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to cause a denial of service and potentially obtain sensitive |
| CVE-2026-16867 | 8.1 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to access server resources with the privileges of an authenti |
| CVE-2026-16868 | 8.1 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to cause a denial of service due to the use of uninitialized  |
| CVE-2026-16887 | 7.5 | 2026-08-13 | IBM i 7.6 could allow a remote attacker to cause a denial of service due to an out-of-bounds write. |
| CVE-2026-16896 | 7.1 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a local authenticated attacker to obtain unauthorized access to files due to a  |
| CVE-2026-16898 | 7.8 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a local authenticated attacker to change the ownership of arbitrary files due t |
| CVE-2026-16908 | 8.5 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote authenticated attacker to gain unauthorized access to arbitrary object |
| CVE-2026-16961 | 7.6 | 2026-08-13 | IBM i 7.6, 7.5, and 7.4 s vulnerable to SQL injection. A remote attacker could send specially crafted SQL statements, wh |
| CVE-2026-16967 | 8.5 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote authenticated attacker to gain unauthorized access to system objects d |
| CVE-2026-16975 | 8.8 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote authenticated attacker to execute arbitrary code due to a heap-based b |
| CVE-2026-16982 | 7.5 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to cause a denial of service due to a heap buffer overflow. |
| CVE-2026-16987 | 8.8 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a local attacker to gain elevated privileges due to improper validation of the  |
| CVE-2026-17004 | 7.5 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to cause a denial of service due to an infinite loop. |
| CVE-2026-17029 | 8.8 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a local attacker to execute arbitrary code due to an out-of-bounds write. |
| CVE-2026-17045 | 8.1 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote authenticated attacker to perform unauthorized operations and access s |
| CVE-2026-17069 | 8.1 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote authenticated attacker to bypass security restrictions due to improper |
| CVE-2026-17199 | 7.5 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to cause a denial of service due to unbounded resource alloca |
| CVE-2026-17206 | 8.1 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to execute arbitrary code due to a buffer overflow. |
| CVE-2026-17223 | 8.8 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote authenticated attacker to execute arbitrary code due to a buffer overf |
| CVE-2026-17229 | 7.5 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to cause a denial of service due to an infinite loop. |
| CVE-2026-18164 | 8.1 | 2026-08-13 | An undocumented hard-coded credential, shared by all device units, is authorized to bypass authentication. This allows a |
| CVE-2026-18846 | 7.5 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 s vulnerable to a buffer overflow from improperly validating client data. By sending malfor |
| CVE-2026-19747 | 9.8 | 2026-08-13 | A weakness has been identified in Tenda CH7, CH7G, CH10, CP3, CP3 Pro, CP7, TC3B14C, TC3B15C, TC3T14C and TC3T15C up to  |
| CVE-2026-48099 | 7.1 | 2026-08-13 | WsgiDAV is a generic and extendable WebDAV server based on WSGI. WsgiDAV 4.3.3 and prior can allow a WebDAV request path |
| CVE-2026-59714 | 7.1 | 2026-08-13 | Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform. From 0.9.5 before 0.10.0, any auth |
| CVE-2026-72629 | 7.1 | 2026-08-13 | Authorization Bypass Through User-Controlled Key (CWE-639) in Kibana can lead to unauthorized cross-space access via Acc |
| CVE-2026-72630 | 7.1 | 2026-08-13 | Incorrect Authorization (CWE-863) in Kibana Fleet can lead to privilege escalation via Privilege Abuse (CAPEC-122). Flee |
| CVE-2026-72632 | 7.1 | 2026-08-13 | Observable Discrepancy (CWE-203) in Kibana Fleet can lead to information disclosure via Excavation (CAPEC-116). Fleet re |
| CVE-2026-72642 | 8.8 | 2026-08-13 | The native inference process that Elasticsearch uses to evaluate uploaded machine learning models accepts a model operat |
| CVE-2026-72643 | 7.1 | 2026-08-13 | Kibana Agent Builder determines whether a caller owns a private agent by comparing a stable user identifier when one is  |
| CVE-2026-72658 | 7.3 | 2026-08-13 | Cross-Site Request Forgery (CWE-352) in Kibana can lead to privilege escalation via Cross Site Request Forgery (CAPEC-62 |
| CVE-2026-72665 | 8.1 | 2026-08-13 | Missing Authorization (CWE-862) in Kibana can lead to unauthorized execution of Osquery and Elastic Defend response acti |
| CVE-2026-72669 | 7.6 | 2026-08-13 | The state that Kibana stores for an Observability Onboarding flow is not bound to the user who created the flow, and the |
| CVE-2026-72670 | 7.7 | 2026-08-13 | A lower privileged user who holds only the privilege to read agent policies can read the entire configuration of a confi |
| CVE-2026-72672 | 7.7 | 2026-08-13 | The Elastic Security capability that suggests existing field values while a user authors endpoint policy artifacts queri |
| CVE-2026-72675 | 7.1 | 2026-08-13 | Missing Authorization (CWE-862) in Kibana can lead to cross-space information disclosure and unauthorized data modificat |
| CVE-2026-72677 | 7.3 | 2026-08-13 | Relative Path Traversal (CWE-23) in Kibana can lead to the unauthorized deletion of Kibana resources via Relative Path T |
| CVE-2026-73530 | 7.7 | 2026-08-13 | Flyto2 Core before 2.28.0 contains a server-side request forgery guard bypass vulnerability that allows attackers to rea |
| CVE-2026-73654 | 8.5 | 2026-08-13 | Trigger.dev is a platform for building and deploying fully managed AI agents and workflows. From 3.3.8 until 4.5.6, the  |
| CVE-2026-73655 | 7.4 | 2026-08-13 | Trigger.dev is a platform for building and deploying fully managed AI agents and workflows. Prior to 4.5.2, addGoogleStr |
| CVE-2026-73656 | 9.9 | 2026-08-13 | Trigger.dev is a platform for building and deploying fully managed AI agents and workflows. Prior to 4.5.6, POST /api/v1 |
| CVE-2026-17099 | 7.3 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to obtain sensitive information due to improper authenticatio |
| CVE-2026-17101 | 8.3 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to execute arbitrary code or obtain sensitive information due |
| CVE-2026-17272 | 8.2 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to cause a denial of service due to a buffer overflow. |
| CVE-2026-17473 | 7.5 | 2026-08-13 | IBM Documentation Offline 1.0.0 through 1.4.1 could allow a remote attacker to read arbitrary files due to improper limi |
| CVE-2026-17481 | 8.8 | 2026-08-13 | IBM Documentation Offline 1.0.0 through 1.4.1 could allow a remote attacker to execute arbitrary code due to improper ou |
| CVE-2026-17482 | 9.8 | 2026-08-13 | IBM Documentation Offline 1.0.0 through 1.4.1 could allow a remote attacker to execute arbitrary code due to improper co |
| CVE-2026-17502 | 8.6 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to cause a denial of service due to an out-of-bounds write. |
| CVE-2026-18077 | 7.5 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to cause a denial of service due to a stack-based buffer over |
| CVE-2026-18101 | 8.8 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a local attacker to gain elevated privileges due to improper management of thre |
| CVE-2026-18193 | 8.9 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to bypass security restrictions due to improper validation of |
| CVE-2026-18249 | 8.4 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote authenticated attacker to gain elevated privileges due to improper val |
| CVE-2026-18509 | 8.2 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a local authenticated attacker to gain privilege escalation via the Navigator f |
| CVE-2026-18511 | 7.3 | 2026-08-13 | IBM i 7.6, 7.5, 7.4, and 7.3 could allow a local authenticated attacker to generate a stack-based buffer overflow in the |
| CVE-2026-19297 | 9.1 | 2026-08-13 | IBM Langflow OSS 1.0.0 through 1.9.6 could allow a remote attacker to obtain unauthorized access to user accounts due to |
| CVE-2026-19483 | 7.1 | 2026-08-13 | IBM Storage Scale 5.2.3.0 through 5.2.3.8, and 6.0.0.0 through 6.0.1.0 Secrets may be disclosed in log files in IBM Stor |
| CVE-2026-8715 | 9.6 | 2026-08-13 | Vault Secrets Operator 1.3.0 up to 1.4.1 is vulnerable to an arbitrary file read and credential exfiltration issue in th |
| CVE-2026-19750 | 8.1 | 2026-08-13 | A flaw has been found in Tenda CH, CP and TX3 V21.x/V22.x/V25.x/V26.x/V27.x. Affected by this issue is some unknown func |
| CVE-2026-72776 | 9.8 | 2026-08-13 | AgenticSeek (commit fc242c7) contains an unauthenticated remote code execution vulnerability that allows any network-adj |
| CVE-2026-72839 | 9.8 | 2026-08-13 | filebrowser through 2.63.16 fails to properly restrict scope and permissions when self-signup is enabled with default Cr |
| CVE-2026-72840 | 8.8 | 2026-08-13 | OpenWrt LuCI contains an overly permissive ACL definition in luci-mod-system-mounts that grants write access to /etc/cro |
| CVE-2026-72841 | 9.9 | 2026-08-13 | luci-app-openvpn fails to properly validate the instance_name2 parameter during file upload, allowing authenticated user |
| CVE-2026-72842 | 9.9 | 2026-08-13 | luci-app-lxc contains an ACL inconsistency vulnerability that allows low-privileged authenticated LuCI users to access b |
| CVE-2026-72849 | 7.7 | 2026-08-13 | Budibase before 3.40.0 contains a cross-site request forgery vulnerability in the chat-link handoff endpoint that allows |
| CVE-2026-72850 | 9.1 | 2026-08-13 | Budibase before 3.40.0 fails to properly sanitize S3 object keys, allowing authenticated builders to upload files with t |
| CVE-2026-72851 | 10.0 | 2026-08-13 | Budibase before 3.40.0 contains an unauthenticated SQL injection vulnerability in webhook-triggered automations with EXE |
| CVE-2026-72853 | 7.6 | 2026-08-13 | Budibase before 3.40.0 contains a SQL injection vulnerability in the Oracle datasource connector's post-write row lookup |
| CVE-2026-72855 | 8.5 | 2026-08-13 | Budibase before 3.40.0 contains server-side request forgery vulnerabilities in OpenAPI query import and REST query execu |
| CVE-2026-72856 | 8.1 | 2026-08-13 | Budibase versions before 3.40.0 contain an authorization/authentication bypass in the PUT /api/global/users/tenant/owner |
| CVE-2026-72857 | 7.7 | 2026-08-13 | Budibase before 3.40.0 fails to redact datasource credentials stored in STRING typed fields, allowing authenticated user |
| CVE-2026-73305 | 8.8 | 2026-08-13 | Budibase is an open-source low-code platform. Prior to 3.39.24, POST /api/public/v1/roles/assign called validateGlobalRo |
| CVE-2026-73408 | 7.6 | 2026-08-13 | Budibase is an open-source low-code platform. Prior to 3.39.18, packages/server/src/integrations/mysql.ts enabled multip |
| CVE-2026-73658 | 8.2 | 2026-08-13 | Trigger.dev is a platform for building and deploying fully managed AI agents and workflows. From 4.4.2 until 4.5.0-rc.5, |
| CVE-2026-73659 | 8.1 | 2026-08-13 | Trigger.dev is the open-source platform for building AI workflows in TypeScript. From 4.4.2 until 4.5.0, the packet pres |
| CVE-2026-73666 | 8.2 | 2026-08-13 | OpenChoreo is a developer platform for Kubernetes. Prior to 1.0.4, 1.1.4, and 1.2.1, the OpenChoreo Backstage backend ha |
| CVE-2026-73667 | 8.8 | 2026-08-13 | OpenChoreo is a complete, open-source developer platform for Kubernetes. Prior to 1.0.4, 1.1.4, and 1.2.0-rc.2, OpenChor |
| CVE-2026-73841 | 8.8 | 2026-08-13 | OpenChoreo is a complete, open-source developer platform for Kubernetes. From 1.2.0-rc.1 until 1.2.0, internal/openchore |
| CVE-2026-73842 | 9.0 | 2026-08-13 | OpenChoreo is a complete, open-source developer platform for Kubernetes. Prior to 1.0.3, 1.1.3, and 1.2.0-rc.2, internal |
| CVE-2026-73843 | 9.6 | 2026-08-13 | OpenChoreo is a complete, open-source developer platform for Kubernetes. Prior to 1.0.2 and 1.1.2, internal/cluster-gate |
| CVE-2026-19753 | 7.3 | 2026-08-13 | A vulnerability was detected in Model Context Protocol mcp-rdf-explorer 1.0.0. Affected is the function explore_url of t |
| CVE-2026-19757 | 7.3 | 2026-08-14 | A vulnerability was found in Dromara lamp-cloud up to 5.10.0. This vulnerability affects unknown code of the file FileAn |
| CVE-2026-19758 | 7.3 | 2026-08-14 | A vulnerability was determined in dromara lamp-cloud up to 5.10.0. This issue affects some unknown processing of the fil |
| CVE-2026-19762 | 7.3 | 2026-08-14 | A vulnerability was found in DTStack Taier 1.4.0. Affected by this vulnerability is the function Paths.ge of the file Fi |
| CVE-2026-19764 | 7.3 | 2026-08-14 | A vulnerability was identified in Raisecom Communication Command and Dispatch Management Platform up to 7.6.5. This affe |
| CVE-2026-19771 | 7.2 | 2026-08-14 | A vulnerability was identified in Baicells EG3661M BaiCE_BQ6_2.0.5.3_NA. This impacts an unknown function of the file /c |
| CVE-2026-18109 | 7.2 | 2026-08-14 | The W3 Total Cache plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comment Author Name in all vers |
| CVE-2026-19788 | 8.8 | 2026-08-14 | A vulnerability was found in Tenda AC1206 15.03.06.23_multi_TD01. This affects the function set_device_name of the file  |
| CVE-2026-19789 | 8.8 | 2026-08-14 | A vulnerability was determined in Tenda AC1206 15.03.06.23_multi_TD01. This vulnerability affects the function set_wl_gu |
| CVE-2026-19790 | 8.8 | 2026-08-14 | A vulnerability was identified in Tenda G0 up to 20260625. This issue affects the function formSetPortMirror of the file |
| CVE-2026-19791 | 8.8 | 2026-08-14 | A weakness has been identified in Tenda G0 up to 20260625. The affected element is the function addStaticRoute of the fi |
| CVE-2026-19792 | 8.8 | 2026-08-14 | A security flaw has been discovered in Tenda G0 up to 20260625. Impacted is the function setPortMapping of the file /gof |
| CVE-2026-12949 | 9.8 | 2026-08-14 | The Wishlist Member plugin for WordPress is vulnerable to Account Takeover via Insufficient Verification of Data Authent |
| CVE-2026-19811 | 8.8 | 2026-08-14 | A security flaw has been discovered in TOTOLINK A800R 4.1.2cu.5137_B20200730. The impacted element is the function setIp |
| CVE-2026-19794 | 7.2 | 2026-08-14 | The WP-Stats plugin for WordPress is vulnerable to Stored Cross-Site Scripting in all versions up to, and including, 2.5 |
| CVE-2026-19812 | 8.8 | 2026-08-14 | A weakness has been identified in TOTOLINK A800R 4.1.2cu.5137_B20200730. This affects the function UploadCustomModule of |
| CVE-2026-19813 | 8.8 | 2026-08-14 | A security vulnerability has been detected in TOTOLINK A800R 4.1.2cu.5137_B20200730. This impacts the function setMacFil |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-20349 | Cisco / Secure Firewall Adaptive Security Appliance (ASA) and Secure Firewall Threat Defense (FTD)  | 2026-08-11 | 2026-08-14 | Unknown |
| CVE-2026-68820 | Microsoft / Windows Ancillary Function Driver for WinSock  | 2026-08-11 | 2026-08-25 | Unknown |
| CVE-2026-72898 | Metabase / Metabase | 2026-08-11 | 2026-08-14 | Unknown |
| CVE-2026-8037 | Progress / LoadMaster | 2026-08-07 | 2026-08-10 | Unknown |

---

*Total entries in CISA KEV catalog: 1665*