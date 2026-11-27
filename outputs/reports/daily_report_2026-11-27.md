# Vulnerability Intelligence Report

**Date:** 2026-11-27  
**Generated:** 2026-11-27T17:51:09Z  

---

## Executive Summary

Our environment faces significant exposure from 147 high-severity CVEs alongside 19 newly added CISA Known Exploited Vulnerabilities (KEVs) catalogued in the past seven days. Key risks include SQL injection flaws in web applications, stored cross-site scripting vulnerabilities across multiple WordPress plugins, missing authorization controls, and actively exploited vulnerabilities in HPE Juniper networking infrastructure, Vates Xen Orchestra, and Danfoss industrial control systems. While no monitored CVEs currently overlap with the KEV catalog, the volume and diversity of high-severity findings indicate a broad attack surface requiring immediate prioritization and remediation.

---

## Risk Narrative

The current threat landscape reflects a convergence of opportunistic web application attacks and targeted exploitation of enterprise and industrial infrastructure. Actively exploited vulnerabilities in HPE Juniper networking equipment and Vates Xen Orchestra present immediate risk of network-level compromise and lateral movement. Danfoss industrial control system vulnerabilities introduce operational technology risk, potentially impacting physical processes and safety systems. The 147 high-severity CVEs, concentrated in web application frameworks and WordPress plugins, expand the attack surface for data theft, session hijacking, and privilege escalation. Collectively, these exposures risk business disruption, regulatory penalties, reputational damage, and potential safety incidents if industrial systems are compromised.

---

## Prioritized Action Items

1. Immediately patch or isolate systems running HPE Juniper Session Smart Router/Conductor and Vates Xen Orchestra, as these are confirmed actively exploited per CISA KEV.
2. Apply available vendor patches or implement compensating controls for all three Danfoss AK-SM 800A Series CVEs (CVE-2025-41450, CVE-2023-25914, CVE-2023-25915) given their active exploitation status.
3. Audit and remediate missing authorization vulnerabilities in Radius Booking and RepairBuddy plugins (CVE-2026-134488, CVE-2026-134714) to prevent unauthorized access to sensitive functions.
4. Remediate SQL injection vulnerabilities in projectworlds Online Jewellery Shopping System and itsourcecode Event Management System to protect against data exfiltration and system compromise.
5. Conduct a full inventory and patching sweep of all WordPress plugins affected by stored XSS vulnerabilities, prioritizing customer-facing and authenticated user environments.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-137412 | 7.3 | 2026-11-26 | A vulnerability was determined in projectworlds Online Jewellery Shopping System 1.0. The affected element is the functi |
| CVE-2026-137414 | 7.3 | 2026-11-26 | A vulnerability was identified in itsourcecode Event Management System 1.0. The impacted element is an unknown function  |
| CVE-2026-137415 | 7.3 | 2026-11-26 | A security flaw has been discovered in Tencent RapidJSON up to 1.1.0. This affects the function Writer::WriteString in t |
| CVE-2026-134470 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Host.it Fastcache  |
| CVE-2026-134488 | 7.5 | 2026-11-26 | Missing Authorization vulnerability in Mamunur Rashid Radius Booking — Booking Calendar for Appointments &amp; Services  |
| CVE-2026-134712 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in DevItems ShopLento |
| CVE-2026-134713 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in INTINITUM FORM Tra |
| CVE-2026-134714 | 7.5 | 2026-11-26 | Missing Authorization vulnerability in Webful Creations RepairBuddy computer-repair-shop allows Exploiting Incorrectly C |
| CVE-2026-134955 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in tychesoftwares Pro |
| CVE-2026-135037 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Mohammed Kaludi AM |
| CVE-2026-135038 | 7.5 | 2026-11-26 | Missing Authorization vulnerability in weDevs WP ERP erp allows Exploiting Incorrectly Configured Access Control Securit |
| CVE-2026-135039 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Liquid Web / Stell |
| CVE-2026-137436 | 7.3 | 2026-11-26 | A vulnerability was found in SourceCodester Basic Hotel Online Reservation System 1.0. The affected element is an unknow |
| CVE-2026-137437 | 7.3 | 2026-11-26 | A vulnerability was determined in SourceCodester Basic Hotel Online Reservation System 1.0. The impacted element is an u |
| CVE-2026-134489 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Themeum Kirki kirk |
| CVE-2026-134705 | 8.8 | 2026-11-26 | Incorrect Privilege Assignment vulnerability in miniOrange miniorange otp verification miniorange-otp-verification allow |
| CVE-2026-134720 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Webful Creations R |
| CVE-2026-134991 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in IdeaBox Creations  |
| CVE-2026-134997 | 7.1 | 2026-11-26 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in KAP ASIAs LottieFi |
| CVE-2026-137506 | 7.8 | 2026-11-26 | ezdxf through 1.4.5 contains a code injection vulnerability in the dxf2code add-on that allows attackers to inject Pytho |
| CVE-2026-137518 | 7.8 | 2026-11-26 | pyfda through 0.9.5 contains an insecure deserialization vulnerability in load_filter() that allows attackers to execute |
| CVE-2026-137529 | 7.8 | 2026-11-26 | JAL (Just Another Ledger) through 2026.11.3 contains an arbitrary file overwrite vulnerability in backup restore that al |
| CVE-2026-137539 | 8.8 | 2026-11-26 | lastversion before 3.6.20 contains a path traversal vulnerability in extract_tar() that allows attackers to write files  |
| CVE-2026-137657 | 7.5 | 2026-11-26 | InternLM LMDeploy 0.9.0 through 0.18.0 contains an unbounded resource allocation vulnerability in the DistServe proxy /d |
| CVE-2026-137660 | 7.3 | 2026-11-26 | A vulnerability has been found in stylefeng Guns up to 2.2. Affected by this issue is the function TokenAndPermissionInt |
| CVE-2026-137677 | 7.3 | 2026-11-27 | A vulnerability has been found in code-projects Simple Laundry System 1.0. This affects an unknown function of the file  |
| CVE-2026-106125 | 9.8 | 2026-11-27 | The Sneeit Framework plugin for WordPress is vulnerable to Remote Code Execution in versions up to, and including, 8.7 v |
| CVE-2026-113774 | 8.8 | 2026-11-27 | The Schema & Structured Data for WP & AMP plugin for WordPress is vulnerable to PHP Object Injection in versions up to,  |
| CVE-2026-115867 | 9.8 | 2026-11-27 | The Database for Contact Form 7, WPforms, Elementor forms plugin for WordPress is vulnerable to Arbitrary File Upload in |
| CVE-2026-126717 | 7.2 | 2026-11-27 | The Translate WordPress with Weglot 2.0 – Multilingual AI Translation plugin for WordPress is vulnerable to Stored Cross |
| CVE-2026-135616 | 7.5 | 2026-11-27 | The W3 Total Cache plugin for WordPress is vulnerable to PHP Object Injection in all versions up to, and including, 2.11 |
| CVE-2026-137702 | 8.1 | 2026-11-27 | Exim before 4.100.2 allows attackers to send SMTP traffic that triggers a heap out-of-bounds write in expansion code run |
| CVE-2026-137041 | 7.2 | 2026-11-27 | The E2Pdf – Export Pdf Tool for WordPress plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'you |
| CVE-2026-137678 | 7.3 | 2026-11-27 | A security vulnerability has been detected in code-projects Online Job Portal 1.0. Affected by this issue is some unknow |
| CVE-2026-137704 | 8.8 | 2026-11-27 | D-Link DWM-222W developed by D-Link Corporation has a Use of Hard-coded Credentials vulnerability. Unauthenticated adjac |
| CVE-2026-137705 | 7.5 | 2026-11-27 | Smart Portal developed by Direk Tech has an Arbitrary File Read vulnerability.Unauthenticated remote attackers can explo |
| CVE-2026-137706 | 9.9 | 2026-11-27 | Smart Portal developed by Direk Tech has a Missing Authorization vulnerability. Authenticated remote attackers can add a |
| CVE-2026-135626 | 7.5 | 2026-11-27 | The Simple Membership plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 4 |
| CVE-2026-135627 | 7.5 | 2026-11-27 | The Simple Membership plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 4 |
| CVE-2026-137679 | 7.3 | 2026-11-27 | A vulnerability was detected in code-projects Online Job Portal 1.0. This affects the function GetSQLValueString of the  |
| CVE-2026-105917 | 8.8 | 2026-11-27 | File Permission Vulnerability in RV3000 Log Monitor for VMware.

This issue affects RV3000 Log Monitor for VMware(CIM):  |
| CVE-2026-115283 | 8.8 | 2026-11-27 | Missing authentication vulnerability in BS2500/BS500 Virtage Firmware.


This issue affects BladeSymphony BS2500: from 0 |
| CVE-2026-115284 | 8.4 | 2026-11-27 | Missing authentication vulnerability in BS2500/BS500 Virtage Firmware.

This issue affects BladeSymphony BS2500: from 02 |
| CVE-2026-115285 | 7.6 | 2026-11-27 | DoS vulnerability in BS2500/BS500 Virtage Firmware.

This issue affects BladeSymphony BS2500: from 02-02 through 02-76;  |
| CVE-2026-115286 | 7.3 | 2026-11-27 | DoS vulnerability in BS2500/BS500 Virtage Firmware.

This issue affects BladeSymphony BS2500: from 02-02 through 02-76;  |
| CVE-2026-115287 | 7.3 | 2026-11-27 | DoS vulnerability in BS2500/BS500 Virtage Firmware.

This issue affects BladeSymphony BS2500: from 02-02 through 02-76;  |
| CVE-2026-115288 | 8.4 | 2026-11-27 | Missing authentication vulnerability in BS2500/BS500 Virtage Firmware.

This issue affects BladeSymphony BS2500: from 02 |
| CVE-2026-119071 | 8.1 | 2026-11-27 | The W3 Total Cache plugin for WordPress is vulnerable to unauthorized File Deletion in all versions up to, and including |
| CVE-2026-136995 | 7.2 | 2026-11-27 | The Upsell Funnel Builder for WooCommerce – Create Upsells, Cross-Sells, Order Bumps, Frequently Bought, and Popups. plu |
| CVE-2026-137721 | 10.0 | 2026-11-27 | A vulnerability in the Platform component of Mitel OpenScape 4000 and OpenScape 4000 Manager could allow an attacker to  |
| CVE-2026-137723 | 9.6 | 2026-11-27 | A vulnerability in the Platform component of Mitel OpenScape 4000 and OpenScape 4000 Manager could allow an attacker to  |
| CVE-2026-137724 | 10.0 | 2026-11-27 | A vulnerability in the Platform component of Mitel OpenScape 4000, and OpenScape 4000 Manager could allow an unauthentic |
| CVE-2026-137738 | 9.8 | 2026-11-27 | In RealVNC Server before 7.19.1, UDP-based connections could potentially be exploited without authentication to execute  |
| CVE-2026-133842 | 8.2 | 2026-11-27 | A flaw was found in Flatpak’s flatpak-system-helper. When a system-wide app, runtime, or extension uses the extra-data m |
| CVE-2026-133845 | 7.3 | 2026-11-27 | A flaw was found in Flatpak’s flatpak-portal. When a sandboxed application invokes Spawn() and maps two different file d |
| CVE-2026-133938 | 9.3 | 2026-11-27 | The backend language switch action (quick_change_language) of the JTL-Shop administration backend is executed without a  |
| CVE-2026-133939 | 9.3 | 2026-11-27 | The OPC (OnPage Composer) start menu, which JTL-Shop shows to logged-in backend users on storefront pages, writes the cu |
| CVE-2026-133941 | 9.3 | 2026-11-27 | The country manager page of the JTL-Shop administration backend (/admin/countries) writes the request parameter activeSo |
| CVE-2026-59103 | 9.8 | 2026-11-27 | MONEO ERP exposes the Ping method of its _slave JSON-RPC service over WebSocket as @rpc.openpublic, so it can be called  |
| CVE-2026-80268 | 7.8 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Exposure of Resource to Wrong S |
| CVE-2026-80448 | 7.7 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Server-Side Request Forgery (SSR |
| CVE-2026-80450 | 7.7 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Certificate Validation |
| CVE-2026-80451 | 7.8 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Use of Hard-coded Cryptographic  |
| CVE-2026-80453 | 8.4 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Download of Code Without Integri |
| CVE-2026-80457 | 7.8 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Incorrect Permission Assignment |
| CVE-2026-80459 | 7.3 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Insecure Temporary File vulnera |
| CVE-2026-80472 | 8.1 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Neutralization of Spec |
| CVE-2026-80475 | 7.7 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Server-Side Request Forgery (SSR |
| CVE-2026-80477 | 8.4 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Neutralization of Spec |
| CVE-2026-129052 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Greg Winiarski WPA |
| CVE-2026-135941 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Booking Activities |
| CVE-2026-135942 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Themeum Tutor LMS  |
| CVE-2026-135949 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Themeisle MPG mult |
| CVE-2026-135951 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Designinvento Dire |
| CVE-2026-135958 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in jgwhite33 WP Revie |
| CVE-2026-135961 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Nks Continuous Ima |
| CVE-2026-133720 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Socio WP Telegr |
| CVE-2026-134717 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in wp.insider Simple  |
| CVE-2026-134939 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in David Lingren Medi |
| CVE-2026-134957 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Chill Image Pho |
| CVE-2026-134963 | 9.9 | 2026-11-27 | Improper Control of Generation of Code ('Code Injection') vulnerability in Webdeclic WPMasterToolKit wpmastertoolkit all |
| CVE-2026-135911 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in PI Web Solution Pr |
| CVE-2026-135930 | 9.1 | 2026-11-27 | Authentication Bypass by Spoofing vulnerability in TMS Amelia ameliabooking allows Identity Spoofing.This issue affects  |
| CVE-2026-135933 | 9.8 | 2026-11-27 | Incorrect Privilege Assignment vulnerability in Tobias WebinarIgnition webinar-ignition allows Privilege Escalation.This |
| CVE-2026-135948 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Themeisle MPG mult |
| CVE-2026-135950 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in fifu.app Featured  |
| CVE-2026-137746 | 7.5 | 2026-11-27 | A flaw has been found in Free5GC 4.3.0. This vulnerability affects unknown code of the component SMF. This manipulation  |
| CVE-2026-137907 | 7.8 | 2026-11-27 | FFmpeg 3.0 before 8.1.3 contains a heap buffer overflow vulnerability in libavfilter/vf_boxblur.c because query_formats( |
| CVE-2026-123757 | 7.4 | 2026-11-27 | An attacker can send a notify request that causes the root zone to be added as a secondary domain to be added to the bin |
| CVE-2026-123761 | 8.2 | 2026-11-27 | Various logic errors in view processing can cause incorrect cached results to be returned. |
| CVE-2026-123762 | 7.6 | 2026-11-27 | A catalog zone update introducing a new zone which already exists, but in a different backend than the one storing the c |
| CVE-2026-123764 | 7.5 | 2026-11-27 | Incorrect sanitization of received data during zone AXFR to Bind backend can cause wrong or invalid data to be serialize |
| CVE-2026-124728 | 7.5 | 2026-11-27 | Incomplete GSS negotiation, as well as TKEY context deletion while a pending operation will need to be signed with that  |
| CVE-2026-124981 | 8.7 | 2026-11-27 | A vulnerability has been identified in Mendix OIDC Provider (Mendix 10 compatible) (All versions < V6.0.0), Mendix OIDC  |
| CVE-2026-134708 | 8.6 | 2026-11-27 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in VideoWhisper.com Video S |
| CVE-2026-134982 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Amauri.IO WPMobile |
| CVE-2026-134983 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Muralidharan Ramas |
| CVE-2026-134987 | 8.6 | 2026-11-27 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Nickboss WordPress File  |
| CVE-2026-134993 | 7.5 | 2026-11-27 | Path Traversal: '.../...//' vulnerability in Seraphinite Solutions Seraphinite Accelerator seraphinite-accelerator allow |
| CVE-2026-134994 | 9.8 | 2026-11-27 | Deserialization of Untrusted Data vulnerability in Nitramix Revertix &#8211; Backup, Migration, Staging &amp; Clone reve |
| CVE-2026-135009 | 9.3 | 2026-11-27 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in David Lingren Medi |
| CVE-2026-135032 | 7.5 | 2026-11-27 | Missing Authorization vulnerability in Everest Forms Everest Forms everest-forms allows Exploiting Incorrectly Configure |
| CVE-2026-135048 | 8.8 | 2026-11-27 | Incorrect Privilege Assignment vulnerability in weDevs WP ERP erp allows Privilege Escalation.This issue affects WP ERP: |
| CVE-2026-135923 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WPTasty AWP Classi |
| CVE-2026-135953 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WS Form WS Form LI |
| CVE-2026-137938 | 7.0 | 2026-11-27 | Sparkle before 2.9.6 contains a time-of-check time-of-use race condition in the installer's SPUInstallationData handling |
| CVE-2026-137939 | 7.8 | 2026-11-27 | Sparkle 2.2.0 before 2.9.6 contains a link following vulnerability in -submitInstallerAtPath: in SUInstallerLauncher.m t |
| CVE-2026-80483 | 7.3 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Off-by-one Error vulnerability. |
| CVE-2026-80485 | 8.4 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Neutralization of Spec |
| CVE-2026-80498 | 7.8 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Use of Hard-coded Cryptographic  |
| CVE-2026-80500 | 7.7 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Authentication vulnera |
| CVE-2026-80501 | 7.8 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Incorrect Permission Assignment |
| CVE-2026-4641 | 7.4 | 2026-11-27 | Incorrect Authorization vulnerability in ABB Relion Protection Relays REX610, ABB Relion Protection Relays RE_611 IEC/CN |
| CVE-2026-80505 | 7.3 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Access Control vulnera |
| CVE-2026-80507 | 8.4 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Heap-based Buffer Overflow vulne |
| CVE-2026-134483 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Lab WP-Lister L |
| CVE-2026-134992 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in megamenu Max Mega  |
| CVE-2026-135019 | 7.5 | 2026-11-27 | Missing Authorization vulnerability in Ahmad WP Job Portal wp-job-portal allows Exploiting Incorrectly Configured Access |
| CVE-2026-135024 | 7.5 | 2026-11-27 | Missing Authorization vulnerability in Ahmad WP Job Portal wp-job-portal allows Exploiting Incorrectly Configured Access |
| CVE-2026-135926 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Nks Photo Gallery  |
| CVE-2026-135939 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in flexmls Flexmls® I |
| CVE-2026-135945 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Themeum Tutor LMS  |
| CVE-2026-135957 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in bgermann CformsII  |
| CVE-2026-135962 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Qode Interactive Q |
| CVE-2026-135968 | 8.6 | 2026-11-27 | Unrestricted Upload of File with Dangerous Type vulnerability in theMarketer theMarketer themarketer allows Using Malici |
| CVE-2026-135974 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WPManageNinja Flue |
| CVE-2026-135979 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Premmerce Premmerc |
| CVE-2026-135983 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in themeansar Newsup  |
| CVE-2026-136118 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Seerox WP Dynamic  |
| CVE-2026-136119 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in InfornWeb News & B |
| CVE-2026-137952 | 7.5 | 2026-11-27 | svglib before 2.5.0 contains a denial of service vulnerability in SvgRenderer.renderNode() that recursively renders inte |
| CVE-2026-137953 | 8.6 | 2026-11-27 | Pydantic Deep 0.2.18 before 0.4.0 contains a missing authentication vulnerability in the bundled DeepResearch FastAPI ap |
| CVE-2026-137954 | 7.5 | 2026-11-27 | Pydantic Deep 0.2.18 before 0.4.0 contains a server-side request forgery and local file read vulnerability in the DeepRe |
| CVE-2026-137957 | 8.2 | 2026-11-27 | n8n before 1.123.96, 2.47.6, 2.48.3, and 3.2.2 contains a path traversal vulnerability in integration nodes that build A |
| CVE-2026-137959 | 8.2 | 2026-11-27 | n8n before 1.123.96, 2.x before 2.47.6, 2.48.x before 2.48.3, and 3.x before 3.2.2 does not verify that the user activat |
| CVE-2026-137963 | 7.5 | 2026-11-27 | ToolJet before 3.21.96-LTS contains a hard-coded credentials vulnerability where the Helm chart values.yaml sets secret_ |
| CVE-2026-137964 | 9.8 | 2026-11-27 | ToolJet before 3.21.96-LTS contains a command injection vulnerability in its GitHub Actions release workflow, which inte |
| CVE-2026-137977 | 7.5 | 2026-11-27 | Nmap before 7.992 contains a use-after-free vulnerability in DNS::ResolverImpl::handle_write in libnetutil/massdns.cc th |
| CVE-2026-137978 | 7.5 | 2026-11-27 | Nmap before 7.992 contains a use-after-free vulnerability in DNS::ResolverImpl::process_request in libnetutil/massdns.cc |
| CVE-2026-80510 | 7.7 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Authorization Bypass Through Us |
| CVE-2026-137684 | 7.3 | 2026-11-27 | A security flaw has been discovered in eosphoros-ai DB-GPT up to 0.8.3. This affects the function editor_sql_run of the  |
| CVE-2026-137992 | 7.5 | 2026-11-27 | libexpat through 2.11.0 contains a denial of service vulnerability in defineAttribute() of lib/xmlparse.c that fails to  |
| CVE-2026-137994 | 7.8 | 2026-11-27 | Leo through 6.8.10 contains an insecure deserialization vulnerability that allows attackers to execute code by embedding |
| CVE-2026-137997 | 7.8 | 2026-11-27 | HCIPy through 0.7.1 contains an insecure deserialization vulnerability that allows attackers to execute code by supplyin |
| CVE-2026-137998 | 7.8 | 2026-11-27 | Detoxify 0.5.3 through 0.5.4 contains an insecure deserialization vulnerability in load_checkpoint that allows attackers |
| CVE-2026-137999 | 7.8 | 2026-11-27 | JSONSchema2PoPo2 through 3.0.3 contains a code injection vulnerability that allows attackers to inject Python code by su |
| CVE-2026-81041 | 7.1 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Certificate Validation |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-103406 | Hewlett Packard Enterprise (HPE) / Juniper Session Smart Conductor and Session Smart Router | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2026-133469 | Vates / Xen Orchestra | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2025-41450 | Danfoss / AK-SM 800A Series | 2026-11-25 | 2026-12-09 | Unknown |
| CVE-2023-25914 | Danfoss / AK-SM 800A Series | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2023-25915 | Danfoss / AK-SM 800A Series | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2026-133324 | Mitel / MiCollab | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2026-133275 | Mitel / MiCollab | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2026-133311 | Mitel / MiCollab | 2026-11-25 | 2026-12-09 | Unknown |
| CVE-2026-133303 | Mitel / MiCollab | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2026-133323 | Mitel / MiCollab | 2026-11-25 | 2026-11-28 | Unknown |
| CVE-2026-132224 | Optimizely / Web Experimentation | 2026-11-24 | 2026-11-27 | Unknown |
| CVE-2026-131914 | Idunno / AntiCsrf | 2026-11-24 | 2026-11-27 | Unknown |
| CVE-2026-132165 | Drupal / Core | 2026-11-24 | 2026-11-27 | Unknown |
| CVE-2026-133968 | Project MONAI / MONAI Label | 2026-11-23 | 2026-11-26 | Unknown |
| CVE-2026-134624 | N-able / MailAssure | 2026-11-23 | 2026-11-26 | Unknown |
| CVE-2026-129448 | Apache / Roller | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2026-123890 | Broadcom / VMware vCenter | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2025-42884 | SAP / NetWeaver | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2026-76466 | Cisco / Expressway Series | 2026-11-20 | 2026-11-23 | Unknown |

---

*Total entries in CISA KEV catalog: 1805*