# Vulnerability Intelligence Report

**Date:** 2026-06-04  
**Generated:** 2026-06-04T11:15:09Z  

---

## Executive Summary

Critical vulnerabilities discovered across industrial control systems and enterprise applications pose immediate threats. ABB T-MAC Plus devices face exposure risks with CVSS 9.9 file access vulnerabilities and authentication bypasses. School management systems show SQL injection and privilege escalation flaws. Five new CISA KEV entries including Linux Kernel and Oracle WebLogic vulnerabilities demand urgent attention. Industrial controllers contain hardcoded passwords enabling full device compromise.

---

## Risk Narrative

The threat landscape shows critical exposure in operational technology and enterprise systems. Industrial control vulnerabilities with hardcoded credentials and file exposure create pathways for ransomware and operational disruption. Authentication bypass flaws enable lateral movement within networks. SQL injection vulnerabilities in educational platforms risk data breaches affecting student records. The combination of OT/IT vulnerabilities with newly weaponized exploits on CISA's KEV list indicates active threat actor interest in these attack vectors.

---

## Prioritized Action Items

1. Immediately patch or isolate ABB T-MAC Plus 4.0-24 systems due to critical file exposure and authentication bypass vulnerabilities.
2. Apply emergency updates to Mojoomla School Management systems to prevent SQL injection and privilege escalation attacks.
3. Review and remediate hardcoded password vulnerabilities in affected firmware across all industrial control devices.
4. Prioritize patching of newly added CISA KEV entries including Linux Kernel CVE-2022-0492 and Oracle WebLogic CVE-2024-21182.
5. Conduct comprehensive security assessment of all industrial control systems to identify additional exposure risks.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2025-14771 | 9.9 | 2026-06-03 | Files or directories accessible to external parties vulnerability in ABB T-MAC Plus.

This issue affects T-MAC Plus: 4.0 |
| CVE-2025-14772 | 8.8 | 2026-06-03 | Authorization bypass through User-Controlled key vulnerability in ABB T-MAC Plus.

This issue affects T-MAC Plus: 4.0-24 |
| CVE-2025-14773 | 8.0 | 2026-06-03 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in ABB T-MAC Plus.

T |
| CVE-2025-14774 | 7.4 | 2026-06-03 | Incorrect Authorization vulnerability in ABB T-MAC Plus.

This issue affects T-MAC Plus: 4.0-24. |
| CVE-2025-15655 | 7.6 | 2026-06-03 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Mojoomla School Ma |
| CVE-2025-15656 | 8.8 | 2026-06-03 | Incorrect Privilege Assignment vulnerability in Mojoomla School Management allows Privilege Escalation.

This issue affe |
| CVE-2026-41032 | 7.5 | 2026-06-03 | It is possible for an unauthenticated adjacent attacker to download log files of the controller, which may disclose some |
| CVE-2026-47065 | 9.8 | 2026-06-03 | ZDRES-232: resolveProxyClass Not Overridden - acceptMatchers Filter Bypass via java.lang.reflect.Proxy


Assessment: Ful |
| CVE-2026-35075 | 9.8 | 2026-06-03 | An unauthenticated remote attacker can recover a default, hard coded password from a firmware image and thus gain full a |
| CVE-2026-35076 | 8.1 | 2026-06-03 | The bac-scanresult method allows a remote attacker with user privileges to delete arbitrary local files due to insuffici |
| CVE-2026-35077 | 8.1 | 2026-06-03 | The ugw-delete-file method allows a remote attacker with user privileges  to delete arbitrary local files due to insuffi |
| CVE-2026-35078 | 8.1 | 2026-06-03 | The ugw-logstop method allows a remote attacker with user privileges  to delete arbitrary local files due to insufficien |
| CVE-2026-35079 | 8.1 | 2026-06-03 | The ugw-restore method allows a remote attacker with user privileges to delete arbitrary local files due to insufficient |
| CVE-2026-35080 | 8.1 | 2026-06-03 | The ugw-restoreinfo method allows a remote attacker with user privileges to delete arbitrary local files due to insuffic |
| CVE-2026-35081 | 8.1 | 2026-06-03 | The ugw-logstop method allows a remote attacker with user privileges to terminate arbitrary processes due to insufficien |
| CVE-2026-35082 | 8.8 | 2026-06-03 | The ugw-logread method allows a remote attacker with user privileges to access arbitrary local files due to insufficient |
| CVE-2026-35083 | 8.8 | 2026-06-03 | A remote attacker with user privileges can exploit a stack buffer overflow to gain full system access as root. |
| CVE-2026-35084 | 8.8 | 2026-06-03 | A remote attacker with user privileges can exploit a stack buffer overflow in dali-devconfig to gain full system access  |
| CVE-2026-35085 | 8.8 | 2026-06-03 | A remote attacker with user privileges can exploit a stack buffer overflow in gdv-serverconfig to gain full system acces |
| CVE-2022-49036 | 7.8 | 2026-06-03 | An inclusion of functionality from untrusted control sphere vulnerability in OpenSSL configuration in Synology Active Ba |
| CVE-2022-49042 | 7.8 | 2026-06-03 | An inclusion of functionality from untrusted control sphere vulnerability in MinGW DLL component in Synology Hyper Backu |
| CVE-2026-5241 | 8.0 | 2026-06-03 | A vulnerability in the LightGlue model loading path of huggingface/transformers version 5.2.0 allows an attacker-control |
| CVE-2026-36576 | 9.8 | 2026-06-03 | An OS command injection vulnerability in the app.py component of openlabs docker-wkhtmltopdf-aas up to commit 9f50579 al |
| CVE-2026-36748 | 9.0 | 2026-06-03 | RockRMS v16.13 and before v.17.7.0 is vulnerable to Cross Site Scripting (XSS) via Social Media links in user profile. |
| CVE-2026-37462 | 7.3 | 2026-06-03 | An integer underflow in the BGPUpdate.DecodeFromBytes function (/bgp/bgp.go) of gobgp v4.3.0 allows attackers to cause a |
| CVE-2026-20230 | 8.6 | 2026-06-03 | A vulnerability in Cisco Unified Communications Manager (Unified CM) and Cisco Unified Communications Manager Session Ma |
| CVE-2026-36606 | 7.1 | 2026-06-03 | Mercusys AC12G (EU) V1 router with firmware AC12G(EU)_V1_200909 encrypts configuration backups with a hardcoded DES key  |
| CVE-2026-36607 | 8.8 | 2026-06-03 | Mercusys AC12G (EU) V1 router with firmware AC12G(EU)_V1_200909 allows unauthenticated brute-force attacks via the TDDP  |
| CVE-2026-36608 | 8.8 | 2026-06-03 | Mercusys AC12G (EU) V1 router with firmware AC12G(EU)_V1_200909 allows UPnP AddPortMapping to forward external ports to  |
| CVE-2026-36609 | 7.3 | 2026-06-03 | Mercusys AC12G (EU) V1 router with firmware AC12G(EU)_V1_200909 uses a static authentication nonce that does not change  |
| CVE-2026-36611 | 7.3 | 2026-06-03 | Mercusys AC12G (EU) V1 with firmware AC12G(EU)_V1_200909 returns 128 bytes of uninitialized buffer when receiving POST r |
| CVE-2026-40290 | 7.8 | 2026-06-03 | OP-TEE is a Trusted Execution Environment (TEE) designed as companion to a non-secure Linux kernel running on Arm; Corte |
| CVE-2026-42061 | 7.3 | 2026-06-03 | Local privilege escalation due to excessive permissions assigned to child processes. The following products are affected |
| CVE-2026-44609 | 7.3 | 2026-06-03 | Local privilege escalation due to EXE hijacking vulnerability. The following products are affected: Acronis DeviceLock D |
| CVE-2026-44682 | 7.3 | 2026-06-03 | Local privilege escalation due to DLL hijacking vulnerability. The following products are affected: Acronis DeviceLock D |
| CVE-2026-50033 | 7.3 | 2026-06-03 | Local privilege escalation due to DLL hijacking vulnerability. The following products are affected: Acronis DeviceLock D |
| CVE-2026-10771 | 7.3 | 2026-06-03 | A vulnerability was found in crmeb crmeb_java 1.4. Affected is the function RestTemplate.getForEntity of the file crmeb- |
| CVE-2026-10777 | 7.3 | 2026-06-03 | A vulnerability was identified in ealpha072 Student-Management-System up to 01451bd7a2f58cdda07bd0b86e3967582e3ecd08. Af |
| CVE-2026-10737 | 7.5 | 2026-06-04 | The SP Project & Document Manager plugin for WordPress is vulnerable to unauthorized access due to a missing capability  |
| CVE-2026-41011 | 8.2 | 2026-06-04 | PackagePersister.validate_tgz builds "tar -tf #{tgz} 2>&1" where tgz = File.join(release_dir, 'packages', "#{name}.tgz") |
| CVE-2026-41858 | 7.5 | 2026-06-04 | Weak Randomness / Insecure Cryptographic Primitive (CWE-338) in Get-RandomPassword in BOSH-Ecosystem / windows-utilities |
| CVE-2026-41859 | 7.8 | 2026-06-04 | A network man-in-the-middle between nats-sync and the BOSH director can steal the director credentials (Basic auth heade |
| CVE-2026-41860 | 8.8 | 2026-06-04 | CWE-326 in BOSH allows a local attacker to steal Basic-auth credentials or redirect UAA token requests via MITM. HttpReq |
| CVE-2026-41010 | 8.2 | 2026-06-04 | ReleaseJob#unpack builds job_dir = File.join(@release_dir, 'jobs', name) and job_tgz = File.join(@release_dir, 'jobs', " |
| CVE-2026-41283 | 9.9 | 2026-06-04 | OpenStack Mistral through 22.0.0 allows Arbitrary Remote Code Execution when the API is exposed. There are endpoints tha |
| CVE-2026-3820 | 7.2 | 2026-06-04 | There is a vulnerability in the Supermicro BMC  SMTP service at Supermicro AS-2115HS-TNR. 
An attacker may obtain admini |
| CVE-2026-49771 | 7.6 | 2026-06-04 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in 10Web Photo Galler |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-45247 | Mirasvit / Mirasvit Full Page Cache Warmer | 2026-06-03 | 2026-06-06 | Unknown |
| CVE-2022-0492 | Linux / Kernel | 2026-06-02 | 2026-06-05 | Unknown |
| CVE-2025-48595 | Android / Framework | 2026-06-02 | 2026-06-05 | Unknown |
| CVE-2024-21182 | Oracle / WebLogic Server | 2026-06-01 | 2026-06-04 | Unknown |
| CVE-2026-0257 | Palo Alto Networks / PAN-OS | 2026-05-29 | 2026-06-01 | Unknown |

---

*Total entries in CISA KEV catalog: 1611*