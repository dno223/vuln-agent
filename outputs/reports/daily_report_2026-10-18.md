# Vulnerability Intelligence Report

**Date:** 2026-10-18  
**Generated:** 2026-10-18T12:27:00Z  

---

## Executive Summary

Our environment faces 41 high-severity vulnerabilities this cycle, with critical concerns in phpMyFAQ (multiple authentication bypasses, authorization flaws, and account takeover risks) and FreeRDP (memory corruption vulnerabilities). Nine new entries were added to CISA's Known Exploited Vulnerabilities catalog in the past seven days, including actively exploited flaws in BeyondTrust, Fortinet, Atlassian, Cisco, and Ahsay products. While no monitored assets currently match KEV entries, the volume and nature of these vulnerabilities represent significant exposure. Immediate patching and mitigation efforts are required to reduce organizational risk.

---

## Risk Narrative

The current threat landscape is characterized by actively exploited vulnerabilities across widely deployed enterprise platforms. CISA's addition of nine KEV entries in seven days—spanning remote support tools, network security appliances, collaboration platforms, and backup software—signals a sustained and broad attacker campaign. The phpMyFAQ vulnerabilities introduce serious identity and access risks, including unauthenticated account takeover and privilege escalation. FreeRDP memory corruption flaws heighten remote compromise potential in environments using virtual desktop infrastructure. Although no monitored assets currently appear in the KEV catalog, the proximity of these vulnerability classes to critical business systems elevates the likelihood of material breach, operational disruption, and regulatory exposure if remediation is delayed.

---

## Prioritized Action Items

1. Patch or upgrade phpMyFAQ to version 4.1.9 or 4.2.0-beta immediately to remediate multiple authentication bypass, account takeover, and authorization vulnerabilities.
2. Audit all BeyondTrust Remote Support, Fortinet, Atlassian, Cisco Secure Email Gateway, and Ahsay deployments for exposure to the newly added CISA KEV vulnerabilities and apply vendor patches without delay.
3. Upgrade FreeRDP to version 3.32.0 or later to address heap out-of-bounds write and integer underflow vulnerabilities that could enable remote code execution.
4. Implement web application firewall rules and input validation controls to mitigate the WooCommerce PAYCOMET XSS vulnerability until a patch is applied.
5. Establish continuous KEV catalog monitoring with automated alerting to ensure any future matches against monitored assets trigger an immediate incident response workflow.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-109701 | 7.1 | 2026-10-17 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in PAYCOMET PAYCOMET  |
| CVE-2026-111880 | 7.4 | 2026-10-17 | FreeRDP versions from 2.0.0 before 3.32.0 contain a heap out-of-bounds write in the server hash-callback NTLM path that  |
| CVE-2026-111881 | 7.6 | 2026-10-17 | FreeRDP from 3.14.1 before 3.32.0 contains an integer underflow in the WinPR BMP writer, where a mismatched stride calcu |
| CVE-2026-111882 | 8.1 | 2026-10-17 | phpMyFAQ 3.2.0-alpha before 4.1.9 and 4.2.0-alpha before 4.2.0-beta contains an authentication bypass vulnerability that |
| CVE-2026-111884 | 8.3 | 2026-10-17 | phpMyFAQ before 4.1.9 and 4.2.0-alpha before 4.2.0-beta does not require the current password when changing an account e |
| CVE-2026-111897 | 7.1 | 2026-10-17 | phpMyFAQ 4.2.0-alpha before 4.2.0-beta contains an authorization bypass vulnerability that allows category-restricted ed |
| CVE-2026-111898 | 7.5 | 2026-10-17 | phpMyFAQ 4.2.0-alpha before 4.2.0-beta contains an authentication bypass vulnerability that allows Keycloak users to tak |
| CVE-2026-111901 | 7.5 | 2026-10-17 | phpMyFAQ 4.2.0-alpha before 4.2.0-beta contains an uncontrolled resource consumption vulnerability in the unauthenticate |
| CVE-2026-111907 | 7.1 | 2026-10-17 | phpMyFAQ 4.0.0 before 4.1.9 contains a cross-site request forgery vulnerability in the POST /admin/api/update-database e |
| CVE-2026-111908 | 8.3 | 2026-10-17 | phpMyFAQ 4.0.0 before 4.1.9 and 4.2.0-alpha before 4.2.0-beta contains a broken object-level authorization vulnerability |
| CVE-2026-111909 | 8.1 | 2026-10-17 | phpMyFAQ before 4.1.9 contains a missing authorization vulnerability in the deleteUser() API that allows authenticated n |
| CVE-2026-111911 | 9.8 | 2026-10-17 | phpMyFAQ 4.0.0 before 4.1.9 contains an authentication bypass vulnerability where WebAuthn registration endpoints attach |
| CVE-2026-111923 | 7.5 | 2026-10-17 | Fleet before 4.89.0 contains an unbounded recursion vulnerability in Apple MDM enrollment property list parsing that all |
| CVE-2026-111924 | 7.5 | 2026-10-17 | Fleet before 4.83.0 contains a denial of service vulnerability that allows unauthenticated attackers to exhaust server m |
| CVE-2026-111927 | 7.7 | 2026-10-17 | Coder before 2.29.20, 2.33.0 before 2.33.12, 2.34.0 before 2.34.8, and 2.35.0 before 2.35.4 contains an improper hostnam |
| CVE-2026-111866 | 7.3 | 2026-10-18 | A weakness has been identified in nemoTyrant manong up to 7c9e5228e133b9267ad3a415833bc9bb53193bb4. This impacts the fun |
| CVE-2026-111871 | 7.3 | 2026-10-18 | A weakness has been identified in itsmeravitejak Online-Examination-System up to e6208e630b14657999bbfe4c9912302d2a1e244 |
| CVE-2026-111872 | 7.3 | 2026-10-18 | A security vulnerability has been detected in itsmeravitejak Online-Examination-System up to e6208e630b14657999bbfe4c991 |
| CVE-2026-111873 | 7.3 | 2026-10-18 | A vulnerability was detected in itsmeravitejak Online-Examination-System up to e6208e630b14657999bbfe4c9912302d2a1e2449. |
| CVE-2026-110031 | 7.2 | 2026-10-18 | The Salon Booking System  WordPress plugin before 10.31.11 does not prevent users holding its custom salon staff role fr |
| CVE-2026-110981 | 7.1 | 2026-10-18 | The WP Photo Album Plus WordPress plugin before 9.2.11.002 does not properly escape a category navigation value before r |
| CVE-2026-96534 | 7.7 | 2026-10-18 | The Modern Events Calendar Lite WordPress plugin before 7.37.0, Modern Event Calendar Pro WordPress plugin before 7.37.0 |
| CVE-2026-107436 | 8.8 | 2026-10-18 | Deserialization of Untrusted Data vulnerability in WP Chill Strong Testimonials strong-testimonials allows Object Inject |
| CVE-2026-108485 | 7.1 | 2026-10-18 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in ThemeGrill eStore  |
| CVE-2026-109894 | 9.3 | 2026-10-18 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Arraytics Booktics |
| CVE-2026-109895 | 7.1 | 2026-10-18 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Arraytics Booktics |
| CVE-2026-110372 | 9.8 | 2026-10-18 | Incorrect Privilege Assignment vulnerability in Brainstorm Force OttoKit suretriggers allows Privilege Escalation.This i |
| CVE-2026-110373 | 8.1 | 2026-10-18 | Incorrect Privilege Assignment vulnerability in Hamid Alinia Login with phone number login-with-phone-number allows Priv |
| CVE-2026-110382 | 7.1 | 2026-10-18 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in NSquared Simply Sc |
| CVE-2026-110383 | 7.5 | 2026-10-18 | Authorization Bypass Through User-Controlled Key vulnerability in WP E-Signature Electronic Signature Add-on for Fluent  |
| CVE-2026-110886 | 9.8 | 2026-10-18 | Deserialization of Untrusted Data vulnerability in QuantumCloud Conversational Forms for ChatBot conversational-forms al |
| CVE-2026-110895 | 8.5 | 2026-10-18 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in DevItems Support G |
| CVE-2026-110897 | 7.1 | 2026-10-18 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in IdeaBox Creations  |
| CVE-2026-111998 | 9.8 | 2026-10-18 | Vanus 0.8.0 through 0.9.0 contains a default credentials vulnerability that allows unauthenticated remote attackers to g |
| CVE-2026-111999 | 7.5 | 2026-10-18 | Vanus 0.8.0 through 0.9.0 contains a missing authentication vulnerability that allows unauthenticated remote attackers t |
| CVE-2026-112000 | 7.6 | 2026-10-18 | Vanus 0.8.0 through 0.9.0 contains a missing authorization vulnerability in the gateway that allows any authenticated us |
| CVE-2026-112001 | 7.2 | 2026-10-18 | ProjectSend 2.0.0 before 2.7.0 contains an incorrect authorization vulnerability that allows restricted API token holder |
| CVE-2026-112005 | 7.7 | 2026-10-18 | WhoDB 0.104.0 before 0.135.0 contains a path traversal vulnerability that allows remote attackers to read and write arbi |
| CVE-2026-112015 | 7.5 | 2026-10-18 | Omnigent 0.3.0 before 0.14.0 contains a path traversal vulnerability that allows authenticated users to escape the works |
| CVE-2026-112018 | 7.0 | 2026-10-18 | cgltf through 1.15 contains a heap out-of-bounds write vulnerability in cgltf_accessor_unpack_floats() that allows attac |
| CVE-2026-112021 | 7.5 | 2026-10-18 | snac2 before 2.93 contains a heap-based buffer overflow vulnerability in _xs_json_load_lexer() that allows unauthenticat |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-102764 | BeyondTrust / Remote Support | 2026-10-16 | 2026-10-19 | Unknown |
| CVE-2025-61624 | Fortinet / Multiple Products | 2026-10-16 | 2026-10-19 | Unknown |
| CVE-2026-21589 | Atlassian / Multiple Products | 2026-10-15 | 2026-10-18 | Unknown |
| CVE-2026-105134 | Ahsay / AhsayCBS | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-76519 | Cisco / Secure Email Gateway | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-105133 | Ahsay / AhsayCBS | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-0322 | Palo Alto Networks / PAN-OS | 2026-10-14 | 2026-10-17 | Unknown |
| CVE-2026-104935 | Ivanti / Connect Secure | 2026-10-13 | 2026-10-16 | Unknown |
| CVE-2026-96951 | Microsoft / Windows | 2026-10-13 | 2026-10-16 | Unknown |

---

*Total entries in CISA KEV catalog: 1748*