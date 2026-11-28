# Vulnerability Intelligence Report

**Date:** 2026-11-28  
**Generated:** 2026-11-28T16:38:29Z  

---

## Executive Summary

Our environment faces significant cybersecurity risk from 38 high-severity vulnerabilities and 18 newly added CISA Known Exploited Vulnerabilities (KEVs). Critical concerns include multiple insecure deserialization flaws enabling remote code execution, a denial-of-service risk in the widely used libexpat library, and a SQL injection vulnerability in DB-GPT. CISA KEV additions affecting GeoServer, Drupal Core, HPE Juniper networking infrastructure, and Vates Xen Orchestra indicate active exploitation in the wild. Immediate prioritization of patching and compensating controls is required to reduce exposure and prevent potential business disruption or data compromise.

---

## Risk Narrative

The current threat landscape reflects adversaries actively exploiting vulnerabilities in infrastructure platforms, content management systems, and developer tooling. CISA KEV additions signal real-world exploitation of GeoServer, Drupal, and networking appliances, posing immediate risk of unauthorized access and lateral movement. Insecure deserialization flaws across multiple libraries create broad remote code execution vectors, particularly dangerous in development and AI-integrated environments. Supply chain risk is elevated given vulnerabilities in popular third-party components like libexpat and Dreamweaver dependencies. Successful exploitation could result in data breaches, service disruption, ransomware deployment, and significant regulatory and reputational consequences for the organization.

---

## Prioritized Action Items

1. Immediately patch or isolate systems running OSGeo GeoServer, Drupal Core, HPE Juniper Session Smart products, and Vates Xen Orchestra, as these are confirmed actively exploited per CISA KEV.
2. Prioritize remediation of insecure deserialization vulnerabilities in Leo, HCIPy, Detoxify, and JSONSchema2PoPo2 (CVSS 7.8) to eliminate remote code execution risk.
3. Apply available patches or mitigations for the libexpat denial-of-service vulnerability (CVE-2026-137992) across all systems using this widely deployed parsing library.
4. Restrict and audit access to the DB-GPT SQL execution endpoint (CVE-2026-137684) until a patched version is deployed to prevent unauthorized database access.
5. Conduct an urgent inventory of all third-party dependencies, including smalot/pdfparser and WooCommerce plugins, and apply vendor patches to close remaining high-severity exposure.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-137684 | 7.3 | 2026-11-27 | A security flaw has been discovered in eosphoros-ai DB-GPT up to 0.8.3. This affects the function editor_sql_run of the  |
| CVE-2026-137992 | 7.5 | 2026-11-27 | libexpat through 2.11.0 contains a denial of service vulnerability in defineAttribute() of lib/xmlparse.c that fails to  |
| CVE-2026-137994 | 7.8 | 2026-11-27 | Leo through 6.8.10 contains an insecure deserialization vulnerability that allows attackers to execute code by embedding |
| CVE-2026-137997 | 7.8 | 2026-11-27 | HCIPy through 0.7.1 contains an insecure deserialization vulnerability that allows attackers to execute code by supplyin |
| CVE-2026-137998 | 7.8 | 2026-11-27 | Detoxify 0.5.3 through 0.5.4 contains an insecure deserialization vulnerability in load_checkpoint that allows attackers |
| CVE-2026-137999 | 7.8 | 2026-11-27 | JSONSchema2PoPo2 through 3.0.3 contains a code injection vulnerability that allows attackers to inject Python code by su |
| CVE-2026-81041 | 7.1 | 2026-11-27 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Certificate Validation |
| CVE-2026-132876 | 7.7 | 2026-11-27 | Dreamweaver Desktop is affected by a Dependency on Vulnerable Third-Party Component vulnerability that could result in a |
| CVE-2026-134129 | 7.5 | 2026-11-27 | smalot/pdfparser before 2.14.0 contains an inefficient algorithmic complexity vulnerability that allows remote attackers |
| CVE-2026-136112 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Amit Mittal Shipme |
| CVE-2026-136113 | 9.3 | 2026-11-27 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Hello Clever Pty H |
| CVE-2026-136114 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in e4jvikwp VikBookin |
| CVE-2026-136115 | 9.8 | 2026-11-27 | Incorrect Privilege Assignment vulnerability in expresstechsoftware MemberPress Discord Addon expresstechsoftwares-membe |
| CVE-2026-136116 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Solid Plugins, LLC |
| CVE-2026-136117 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Solid Plugins, LLC |
| CVE-2026-131776 | 7.1 | 2026-11-27 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Hai Zheng / Lite S |
| CVE-2026-137898 | 7.3 | 2026-11-27 | A flaw was found in pam. When built with libeconf and an unconfigured vendor directory, the pam_econf configuration hand |
| CVE-2026-138026 | 7.3 | 2026-11-27 | Crypto APIs MCP server packages (@cryptoapis-io/mcp-*) before 0.4.0, mcp-blockchain-events, mcp-blockchain-fees, mcp-bro |
| CVE-2026-138027 | 7.5 | 2026-11-27 | Bagel (bagel-mcp) before 2.5.5 exposes unsandboxed DuckDB SQL execution through the read-only annotated query_messages M |
| CVE-2026-138028 | 7.5 | 2026-11-27 | Bagel (bagel-mcp) before 2.5.5 contains an argument injection vulnerability in RsyncFilesToLocalDirectory that allows at |
| CVE-2026-138034 | 7.5 | 2026-11-27 | bigcommerce-api-mcp before 1.0.1 contains a missing authentication vulnerability that allows remote unauthenticated atta |
| CVE-2026-137941 | 7.8 | 2026-11-27 | A flaw was found in GIMP. The Levels configuration setter does not validate the channel enum before using it to index fi |
| CVE-2026-137974 | 7.0 | 2026-11-27 | A flaw was found in tuned. This vulnerability allows local privilege escalation because the spindown-disk profile script |
| CVE-2026-138003 | 9.0 | 2026-11-27 | A weakness has been identified in TRENDnet TEW-751DR 1.03B01. This impacts the function FUN_0040ed90 of the file wfadev. |
| CVE-2026-138004 | 10.0 | 2026-11-27 | A security vulnerability has been detected in TRENDnet TEW-751DR and TEW-733GR 1.03B01. Affected is the function soapcgi |
| CVE-2026-138117 | 7.8 | 2026-11-28 | HyperSpy from 1.2.0 before 2.6.0 contains a code execution vulnerability that allows attackers to run Python code by emb |
| CVE-2026-138118 | 7.8 | 2026-11-28 | HyperSpy from 1.4.0 before 2.6.0 contains an insecure deserialization vulnerability that allows attackers to execute arb |
| CVE-2026-138119 | 8.8 | 2026-11-28 | Kestra before 1.3.36 contains a reflected cross-site scripting vulnerability that allows unauthenticated attackers to ex |
| CVE-2026-138154 | 8.6 | 2026-11-28 | POSTAL 2 before build 26810491 contains a sandbox escape vulnerability that allows malicious Steam Workshop mods to exec |
| CVE-2026-138159 | 7.5 | 2026-11-28 | edbrowse through 3.8.19 contains an integer overflow in stringAndBytes() that allows malicious servers to write past a h |
| CVE-2026-138160 | 7.8 | 2026-11-28 | Gammu before 1.45.2 contains a stack-based buffer overflow vulnerability in ReadBackupTextLen() that allows attackers to |
| CVE-2026-138161 | 7.8 | 2026-11-28 | Gammu before 1.45.2 contains a buffer overflow vulnerability in LoadBackup() that allows attackers to corrupt memory by  |
| CVE-2026-138162 | 7.0 | 2026-11-28 | Gammu before 1.45.2 contains a stack-based buffer overflow vulnerability in ALCATEL_EncodeString() that allows attackers |
| CVE-2026-138163 | 7.8 | 2026-11-28 | Gammu before 1.45.2 contains a heap-based buffer overflow in ReadWAPSettingsEntry() that allows attackers to corrupt hea |
| CVE-2026-138005 | 10.0 | 2026-11-28 | A vulnerability was detected in TRENDnet TEW-751DR 1.03B01. Affected by this vulnerability is the function gena.php::GEN |
| CVE-2026-138050 | 7.3 | 2026-11-28 | A weakness has been identified in OpenAirInterface oai-cn5g-udr up to 2.2.2. This vulnerability affects unknown code of  |
| CVE-2026-138055 | 7.3 | 2026-11-28 | A vulnerability was found in Cloud-CV EvalAI up to 30128ca50ab24a0c65e556d78199309e8ecc3eae. This affects an unknown fun |
| CVE-2026-138056 | 7.3 | 2026-11-28 | A vulnerability was determined in SonicJs-Org SonicJS up to 3.0.1. This impacts the function AuthManager.verifyToken of  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-120705 | OSGeo / GeoServer | 2026-11-27 | 2026-11-30 | Unknown |
| CVE-2026-129243 | OSGeo / GeoServer | 2026-11-27 | 2026-11-30 | Unknown |
| CVE-2026-136716 | Drupal / Core | 2026-11-27 | 2026-11-30 | Unknown |
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

---

*Total entries in CISA KEV catalog: 1808*