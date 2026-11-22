# Vulnerability Intelligence Report

**Date:** 2026-11-22  
**Generated:** 2026-11-22T15:55:59Z  

---

## Executive Summary

Our environment faces significant exposure from 94 high-severity vulnerabilities, including multiple critical flaws in the Fastify web framework ecosystem (CVSS up to 9.1) affecting middleware routing and request handling. TRENDnet router firmware and SiYuan note-taking platform also carry high-severity weaknesses. Additionally, 9 new entries were added to CISA's Known Exploited Vulnerabilities catalog this week, targeting widely deployed platforms including VMware vCenter, Apache Roller, SAP NetWeaver, Cisco Expressway, and Synology DSM. These KEV additions indicate active exploitation in the wild and require immediate attention regardless of internal patch timelines.

---

## Risk Narrative

The current threat landscape reflects active exploitation of enterprise and open-source platforms by sophisticated threat actors. CISA's addition of VMware vCenter, SAP NetWeaver, and Cisco Expressway to its KEV catalog signals real-world attacks targeting infrastructure widely used in corporate environments. The cluster of Fastify middleware vulnerabilities introduces supply-chain risk for any organization running Node.js web services, potentially enabling request smuggling, authentication bypass, or privilege escalation. SiYuan vulnerabilities pose data exfiltration risks for teams using the platform for sensitive documentation. Collectively, these exposures threaten data confidentiality, service availability, and regulatory compliance, and could serve as initial footholds for ransomware or persistent intrusion campaigns.

---

## Prioritized Action Items

1. Immediately audit all environments running VMware vCenter, Apache Roller, SAP NetWeaver, Cisco Expressway, and Synology DSM and apply vendor patches for the five newly catalogued CISA KEV entries.
2. Upgrade @fastify/express to version 4.0.10 or later and @fastify/middie to a patched release to remediate the five critical CVSS 9.1 middleware vulnerabilities.
3. Isolate or replace TRENDnet TEW-657BRM devices running firmware 1.00.1 until a patched firmware version is available and can be deployed.
4. Update all SiYuan installations to version 3.8.10 or later to close the three unauthorized access vulnerabilities exposing indexed assets and block data.
5. Implement compensating controls—such as WAF rules, network segmentation, and enhanced monitoring—for all vulnerable systems where immediate patching is not feasible.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-133985 | 8.8 | 2026-11-21 | A flaw has been found in TRENDnet TEW-657BRM 1.00.1. Affected by this issue is some unknown functionality of the file /u |
| CVE-2026-124626 | 9.1 | 2026-11-21 | @fastify/express is a compatibility layer that lets Express middleware run inside the Fastify web framework. In versions |
| CVE-2026-129504 | 9.1 | 2026-11-21 | @fastify/express is a compatibility layer that lets Express middleware run inside the Fastify web framework. In versions |
| CVE-2026-129850 | 7.4 | 2026-11-21 | @fastify/express is a compatibility layer that lets Express middleware run inside the Fastify web framework. In versions |
| CVE-2026-133120 | 9.1 | 2026-11-21 | @fastify/express is a compatibility layer that lets Express middleware run inside the Fastify web framework. In versions |
| CVE-2026-133250 | 9.1 | 2026-11-21 | @fastify/middie is the middleware engine for the Fastify web framework. In versions up to and including 9.3.7, middie ma |
| CVE-2026-133867 | 9.1 | 2026-11-21 | @fastify/express is a compatibility layer that lets Express middleware run inside the Fastify web framework. In versions |
| CVE-2026-134245 | 7.5 | 2026-11-21 | SiYuan 3.8.0 before 3.8.10 contains an incorrect authorization vulnerability in the serveAssets route that allows unauth |
| CVE-2026-134246 | 7.5 | 2026-11-21 | SiYuan 3.6.0 before 3.6.2 and 3.7.3 before 3.8.10 contains a missing authorization vulnerability in the /api/block/getDO |
| CVE-2026-134247 | 7.5 | 2026-11-21 | SiYuan 3.8.0 before 3.8.10 contains an incorrect authorization vulnerability that allows anonymous attackers to read ind |
| CVE-2026-134248 | 7.7 | 2026-11-21 | SiYuan 3.6.0 before 3.8.10 contains an information disclosure vulnerability that allows authenticated Readers to read pr |
| CVE-2026-134249 | 7.5 | 2026-11-21 | SiYuan before 3.8.10 contains an authentication bypass vulnerability that allows unauthenticated attackers to gain Admin |
| CVE-2026-134250 | 8.0 | 2026-11-21 | Grav Form plugin 1.1.0 before 9.1.40 contains a stored cross-site scripting vulnerability in Form::uploadFiles(), which  |
| CVE-2026-134253 | 8.8 | 2026-11-21 | Grav API plugin from 1.0.0 before 1.1.4 contains a remote code execution vulnerability that allows publishers with media |
| CVE-2026-134254 | 7.1 | 2026-11-21 | Admidio from 5.0.0 before 5.0.18 contains a path traversal vulnerability in DocumentsService::renameFile() that allows a |
| CVE-2026-134258 | 8.7 | 2026-11-21 | Admidio 5.0.0 before 5.0.18 contains a path traversal vulnerability in the Documents & Files renameFile() action that al |
| CVE-2026-134262 | 8.1 | 2026-11-21 | Admidio 5.0.0 before 5.0.18 contains a stored cross-site scripting vulnerability that allows role administrators to inje |
| CVE-2026-134268 | 7.1 | 2026-11-21 | Vikunja from 0.21.0 before 2.8.0 contains a resource exhaustion vulnerability that allows authenticated users to trigger |
| CVE-2026-134282 | 8.1 | 2026-11-21 | Vikunja from 0.14.0 before 2.8.0 contains a mass assignment vulnerability that allows authenticated users to set json-hi |
| CVE-2026-134284 | 7.5 | 2026-11-21 | Vikunja from 1.0.0 before 2.8.0 contains an account takeover vulnerability that allows attackers to hijack SSO identitie |
| CVE-2026-134287 | 7.7 | 2026-11-21 | OpenRemote core before 1.34.0 contains an authentication bypass vulnerability in UserAssetProvisioningMQTTHandler that a |
| CVE-2026-134291 | 7.5 | 2026-11-21 | SurrealDB 3.0.0 before 4.0.0 contains a path traversal vulnerability in its filesystem storage bucket that only canonica |
| CVE-2026-134292 | 9.8 | 2026-11-21 | SurrealDB 1.0.0 before 4.0.0 contains a capability check bypass in its embedded JavaScript scripting engine, where the s |
| CVE-2026-134293 | 8.2 | 2026-11-21 | SurrealDB 3.1.0 before 4.0.0 contains an SQL injection vulnerability in its Model Context Protocol (MCP) server because  |
| CVE-2026-134294 | 7.5 | 2026-11-21 | SurrealDB 3.0.0 before 4.0.0 contains a path traversal vulnerability in its bucket storage layer on Windows, where Objec |
| CVE-2026-134295 | 8.8 | 2026-11-21 | SurrealDB 3.0.0 before 4.0.0 contains a path traversal vulnerability in direct filesystem buckets because BucketControll |
| CVE-2026-134299 | 7.5 | 2026-11-21 | SurrealDB 3.0.4 before 4.0.0 does not apply operator-configured WebSocket frame, message, and buffer size limits to the  |
| CVE-2026-134300 | 8.1 | 2026-11-21 | SurrealDB from 2.2.0 before 4.0.0 contains an authorization bypass vulnerability in Document::purge_references that lets |
| CVE-2026-134303 | 7.9 | 2026-11-21 | SurrealKV before 1.1.0 contains an out-of-bounds read vulnerability in the safe InternalKeyRef::from_encoded constructor |
| CVE-2026-134309 | 8.8 | 2026-11-21 | SurrealDB 1.0.0 before 4.0.0 contains an authorization bypass vulnerability that allows authenticated users to shadow pr |
| CVE-2026-134316 | 8.1 | 2026-11-21 | @better-auth/electron 1.5.0-beta.12 before 1.7.16 and 1.8.0-beta.0 before 1.8.0-beta.5 accepts any validly signed value  |
| CVE-2026-134322 | 8.1 | 2026-11-21 | better-auth 0.4.12-beta.7 before 1.7.16 and 1.8.0-beta.0 before 1.8.0-beta.5 contains an improper authentication vulnera |
| CVE-2026-134325 | 7.5 | 2026-11-21 | ArcadeDB before 26.11.1 contains a denial of service vulnerability in the Redis protocol handler, which neither replies  |
| CVE-2026-134337 | 8.8 | 2026-11-21 | ArcadeDB native-image server builds 26.8.1 before 26.11.1 contain an authorization bypass vulnerability that allows auth |
| CVE-2026-134338 | 8.8 | 2026-11-21 | ArcadeDB 25.8.1 before 26.11.1 contains an incorrect authorization vulnerability because per-type ACLs are keyed by type |
| CVE-2026-134339 | 8.8 | 2026-11-21 | ArcadeDB from 26.11.1-SNAPSHOT before 26.11.1 contains an authorization bypass vulnerability that allows authenticated u |
| CVE-2026-134341 | 7.5 | 2026-11-21 | actix-http 3.0.0 before 3.20.3 contains a denial of service vulnerability that allows unauthenticated remote attackers t |
| CVE-2026-134347 | 7.5 | 2026-11-21 | actix-files before 0.7.4 contains an information disclosure vulnerability that allows remote unauthenticated attackers t |
| CVE-2026-134352 | 8.1 | 2026-11-21 | Rclone from 1.51.0 before 1.76.0 contains an authentication bypass vulnerability in serve sftp --auth-proxy because the  |
| CVE-2026-134359 | 8.8 | 2026-11-21 | AzuraCast before 0.24.1 fails to escape backslashes in Liquidsoap annotation values, allowing media managers to break ou |
| CVE-2026-134364 | 7.5 | 2026-11-21 | pypdf 3.7.1 before 7.0.0 contains an information disclosure vulnerability that allows attackers to guess placeholders in |
| CVE-2026-134366 | 7.5 | 2026-11-21 | pypdf before 7.0.0 contains a resource exhaustion vulnerability that allows attackers to cause large memory usage by sup |
| CVE-2026-134367 | 7.5 | 2026-11-21 | pypdf 2.4.2 before 7.0.0 contains a resource exhaustion vulnerability in its handling of XFA forms that allows attackers |
| CVE-2026-134370 | 7.7 | 2026-11-21 | Frappe Framework before 15.120.1 and 16.x before 16.33.1 contains a path traversal vulnerability in file attachment hand |
| CVE-2026-134372 | 7.7 | 2026-11-21 | Frappe ERPNext 4.3.0 before 15.121.6 and 16.x before 16.37.0 contains an SQL injection vulnerability in an endpoint of t |
| CVE-2026-134389 | 8.5 | 2026-11-21 | Frappe ERPNext 6.18.0 before 15.124.0 and 16.x before 16.52.0 contains a missing authorization vulnerability in Payment  |
| CVE-2026-134393 | 7.7 | 2026-11-21 | Frappe ERPNext 10.1.41 before 15.122.0 and 16.x before 16.50.0 contains a missing authorization vulnerability in a Manuf |
| CVE-2026-134399 | 7.7 | 2026-11-21 | Frappe ERPNext 8.11.1 before 15.124.0 and 16.x before 16.52.0 is missing an authorization check in print and portal view |
| CVE-2026-134404 | 7.7 | 2026-11-21 | Frappe ERPNext 6.3.0 before 15.124.0 and 16.x before 16.52.0 contains a missing authorization vulnerability in the custo |
| CVE-2026-134411 | 7.7 | 2026-11-21 | Frappe ERPNext 11.1.7 before 15.121.4 and 16.x before 16.36.0 contains a missing authorization vulnerability in a Region |
| CVE-2026-134417 | 7.7 | 2026-11-21 | Frappe ERPNext 13.0.0 before 15.121.4 and 16.x before 16.36.0 contains a missing authorization vulnerability in an Accou |
| CVE-2026-134418 | 7.7 | 2026-11-21 | Frappe ERPNext 4.0.0 before 15.122.0 and 16.x before 16.50.0 contains a missing authorization vulnerability in an Accoun |
| CVE-2026-134428 | 7.7 | 2026-11-21 | Frappe ERPNext 13.0.0 before 15.121.4 and 16.x before 16.36.0 contains a missing authorization vulnerability in a Stock  |
| CVE-2026-134429 | 8.5 | 2026-11-21 | Frappe ERPNext before 15.121.4 and 16.x before 16.36.0 contains a missing authorization vulnerability in a CRM and Suppo |
| CVE-2026-134432 | 7.1 | 2026-11-21 | Frappe ERPNext 15.0.0 before 15.121.4 and 16.x before 16.36.0 contains a missing authorization vulnerability in a Stock  |
| CVE-2026-134433 | 8.5 | 2026-11-21 | Frappe ERPNext before 15.124.2 and 16.x before 16.53.0 fails to enforce record-level authorization in several endpoints, |
| CVE-2026-134434 | 7.7 | 2026-11-21 | Frappe ERPNext 16.0.0 before 16.36.0 contains a missing authorization vulnerability in a Manufacturing module endpoint t |
| CVE-2026-134435 | 7.7 | 2026-11-21 | Frappe ERPNext before 15.124.2 and 16.x before 16.50.0 contains a missing authorization vulnerability in an Accounts mod |
| CVE-2026-134436 | 7.7 | 2026-11-21 | Frappe ERPNext 15.8.0 before 15.121.4 and 16.x before 16.36.0 contains a missing authorization vulnerability in an endpo |
| CVE-2026-134448 | 8.1 | 2026-11-21 | Finsys Dockhand 1.0.7 before 1.0.57 contains a path traversal vulnerability that allows low-privileged users to read and |
| CVE-2026-134451 | 8.1 | 2026-11-21 | Dockhand before 1.0.57 contains a privilege escalation vulnerability that allows non-admin users with settings:edit perm |
| CVE-2026-134452 | 8.8 | 2026-11-21 | Dockhand before 1.0.57 merges stack secret environment variables into the environment used to spawn docker compose durin |
| CVE-2026-134454 | 7.4 | 2026-11-21 | Hysteria from 2.0.0 before 2.9.2 contains an ACL bypass vulnerability that allows authenticated clients to reach blocked |
| CVE-2026-134456 | 7.5 | 2026-11-21 | Hysteria 2.5.0 before 2.9.2 contains a denial of service vulnerability in the HTTP sniff implementation that fails to li |
| CVE-2026-134461 | 7.5 | 2026-11-21 | Web-Token jwt-framework and jwt-library before 3.4.10, 4.0.0 before 4.0.7, and 4.1.0 before 4.1.7 contain an uncontrolle |
| CVE-2026-133993 | 10.0 | 2026-11-21 | A security flaw has been discovered in D-Link DIR-600L 2.17b02. This affects the function FUN_0040efb0 of the file gena. |
| CVE-2026-125294 | 9.8 | 2026-11-21 | The Nexter Blocks Pro plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 5 |
| CVE-2026-134541 | 7.3 | 2026-11-22 | A vulnerability was detected in Surya2Developer Online Shopping System 1.0. This impacts an unknown function of the file |
| CVE-2026-134543 | 7.1 | 2026-11-22 | A flaw has been found in jprocms up to 1.7.7. Affected is the function StrUtil.format of the component Database Backup M |
| CVE-2026-134654 | 8.1 | 2026-11-22 | Mailflare before 48957fb contains a host header injection vulnerability in the password-reset request handler that allow |
| CVE-2026-134679 | 7.5 | 2026-11-22 | WeddingShare through 1.8.2 contains a missing authorization vulnerability in the anonymous MediaViewerController.Gallery |
| CVE-2026-134694 | 7.8 | 2026-11-22 | Gammapy through 2.1 contains a code injection vulnerability in WcsGeom.from_header() that passes the WCSSHAPE FITS heade |
| CVE-2026-134704 | 7.8 | 2026-11-22 | OpenShot Video Editor (openshot-qt) through 4.1.1 contains an unsafe deserialization vulnerability in ProjectDataStore.l |
| CVE-2026-134623 | 7.3 | 2026-11-22 | A flaw has been found in Microweber up to 2.0.20. This impacts the function UserManager::make_logged of the file src/Mic |
| CVE-2026-129016 | 7.1 | 2026-11-22 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Andrea Tarantini M |
| CVE-2026-131700 | 7.1 | 2026-11-22 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Dylan Kuhn  Geo Ma |
| CVE-2026-131705 | 8.5 | 2026-11-22 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Metagauss ProfileG |
| CVE-2026-131706 | 7.5 | 2026-11-22 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Metagauss ProfileG |
| CVE-2026-131707 | 8.8 | 2026-11-22 | Deserialization of Untrusted Data vulnerability in Metagauss ProfileGrid profilegrid-user-profiles-groups-and-communitie |
| CVE-2026-131708 | 7.1 | 2026-11-22 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Metagauss ProfileG |
| CVE-2026-131720 | 7.5 | 2026-11-22 | Insertion of Sensitive Information Into Sent Data vulnerability in Liquid Web / StellarWP BookIt bookit allows Retrieve  |
| CVE-2026-131701 | 8.5 | 2026-11-22 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in JoomUnited WP Medi |
| CVE-2026-131702 | 7.1 | 2026-11-22 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in NextScripts NextSc |
| CVE-2026-131714 | 7.1 | 2026-11-22 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Kaliforms Kali For |
| CVE-2026-131718 | 7.1 | 2026-11-22 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Liquid Web / Stell |
| CVE-2026-131724 | 7.1 | 2026-11-22 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Liquid Web / Stell |
| CVE-2026-131742 | 7.1 | 2026-11-22 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in PluginUs.Net Activ |
| CVE-2026-131780 | 7.1 | 2026-11-22 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Themify Themify Bu |
| CVE-2026-129083 | 7.1 | 2026-11-22 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WPKoi WordPress Th |
| CVE-2026-129085 | 7.5 | 2026-11-22 | Missing Authorization vulnerability in Aguila Technologies WP Customer Area customer-area allows Exploiting Incorrectly  |
| CVE-2026-131754 | 9.8 | 2026-11-22 | Deserialization of Untrusted Data vulnerability in Pierre Lannoy APCu Manager apcu-manager allows Object Injection.This  |
| CVE-2026-131775 | 7.1 | 2026-11-22 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in nK Ghost Kit ghost |
| CVE-2026-131782 | 9.8 | 2026-11-22 | Deserialization of Untrusted Data vulnerability in mra13 / Team Tips and Tricks HQ Simple Shopping Cart wordpress-simple |
| CVE-2026-134753 | 7.0 | 2026-11-22 | dsniff through 2.5a2 contains an integer underflow in decode_sniffer() in decode_sniffer.c that allows unauthenticated r |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-129448 | Apache / Roller | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2026-123890 | Broadcom / VMware vCenter | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2025-42884 | SAP / NetWeaver | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2026-76466 | Cisco / Expressway Series | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2024-10441 | Synology / DiskStation Manager (DSM) | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-40217 | BerriAI / LiteLLM | 2026-11-18 | 2026-12-02 | Unknown |
| CVE-2026-90817 | Vanderbilt University / Research Electronic Data Capture (REDCap) | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-90436 | Apache / Axis | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-115731 | Perforce / Puppet Enterprise | 2026-11-17 | 2026-12-01 | Unknown |

---

*Total entries in CISA KEV catalog: 1790*