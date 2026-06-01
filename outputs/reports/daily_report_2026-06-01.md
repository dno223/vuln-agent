# Vulnerability Intelligence Report

**Date:** 2026-06-01  
**Generated:** 2026-06-01T13:36:40Z  

---

## Executive Summary

Our organization faces significant cybersecurity exposure with 35 high-severity vulnerabilities discovered, including critical CVSS 9.8-rated flaws in network infrastructure. Five new CISA Known Exploited Vulnerabilities were added this week, indicating active threat actor exploitation. The vulnerabilities primarily affect network devices (Tenda, TRENDnet, D-Link routers) and healthcare management systems, creating potential entry points for ransomware and data theft. Immediate patching is essential as these vulnerabilities enable remote code execution and system compromise.

---

## Risk Narrative

The threat landscape shows sophisticated targeting of network infrastructure and healthcare systems. With CVSS scores ranging from 7.3 to 9.8, these vulnerabilities enable attackers to gain initial access, escalate privileges, and move laterally through networks. The presence of router and IoT device vulnerabilities creates persistent backdoors for advanced persistent threats. Healthcare system vulnerabilities expose sensitive patient data to theft and regulatory penalties. The addition of five new CISA KEV entries indicates these attack vectors are actively being exploited in the wild, increasing our immediate risk profile significantly.

---

## Prioritized Action Items

1. Emergency patch deployment for all Totolink N300RH devices (CVE-2026-10187, CVSS 9.8) within 48 hours due to critical remote code execution risk.
2. Conduct immediate vulnerability assessment of all Tenda W12 router firmware and apply security updates to prevent network compromise.
3. Review and patch all instances of SourceCodester Hospitals Patient Records Management System to protect sensitive healthcare data.
4. Implement network segmentation around vulnerable TRENDnet and D-Link devices until patches can be applied.
5. Establish monitoring for the five new CISA KEV entries and develop incident response procedures for potential exploitation attempts.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-10183 | 8.8 | 2026-05-31 | A vulnerability was identified in TRENDnet TEW-432BRP 3.10B20. This affects the function formWlanSetup of the file /gofo |
| CVE-2026-10184 | 7.3 | 2026-05-31 | A security flaw has been discovered in SourceCodester Hospitals Patient Records Management System 1.0. This impacts an u |
| CVE-2026-10185 | 7.3 | 2026-05-31 | A weakness has been identified in SourceCodester Hospitals Patient Records Management System 1.0. Affected is an unknown |
| CVE-2026-10186 | 7.3 | 2026-05-31 | A security vulnerability has been detected in code-projects Online Hospital Management System 1.0. Affected by this vuln |
| CVE-2026-10187 | 9.8 | 2026-05-31 | A vulnerability was detected in Totolink N300RH 6.1c.1353_B20190305. Affected by this issue is the function setWiFiBasic |
| CVE-2026-10188 | 8.8 | 2026-05-31 | A flaw has been found in Tenda W12 3.0.0.7(4763). This affects the function cgistaKickOff of the file /bin/httpd. Execut |
| CVE-2026-10189 | 8.8 | 2026-05-31 | A vulnerability has been found in Tenda W12 3.0.0.7(4763). This vulnerability affects the function cgiSysTimeInfoSet of  |
| CVE-2026-10191 | 8.8 | 2026-05-31 | A vulnerability was determined in Tenda W12 3.0.0.7(4763). Impacted is the function cgiWifiMacFilterSet of the file /bin |
| CVE-2026-10192 | 8.8 | 2026-05-31 | A vulnerability was identified in Tenda W12 3.0.0.7(4763). The affected element is the function set_local_time_0 of the  |
| CVE-2026-10206 | 8.8 | 2026-06-01 | A vulnerability was detected in D-Link DI-8400 up to 16.07.26A1. This affects an unknown function of the file /dbsrv.asp |
| CVE-2026-10208 | 7.3 | 2026-06-01 | A flaw has been found in code-projects Online Hospital Management System 1.php. This impacts the function login_user of  |
| CVE-2026-10214 | 7.3 | 2026-06-01 | A weakness has been identified in zhayujie chatgpt-on-wechat up to 2.0.8. This issue affects the function _get_safety_wa |
| CVE-2026-10219 | 7.3 | 2026-06-01 | A vulnerability was found in nextlevelbuilder GoClaw up to 3.11.3. This impacts the function FsBridge.WriteFile of the f |
| CVE-2026-10220 | 7.3 | 2026-06-01 | A vulnerability was determined in NousResearch hermes-agent up to 2026.4.30. Affected is the function _serve_plugin_skil |
| CVE-2026-10221 | 7.3 | 2026-06-01 | A vulnerability was identified in NousResearch hermes-agent up to 0.12.0. Affected by this vulnerability is the function |
| CVE-2026-20452 | 8.0 | 2026-06-01 | In wlan AP driver, there is a possible memory corruption due to a heap buffer overflow. This could lead to remote (proxi |
| CVE-2026-20455 | 7.8 | 2026-06-01 | In geniezone, there is a possible out of bounds write due to a missing bounds check. This could lead to local escalation |
| CVE-2026-48188 | 9.1 | 2026-06-01 | An improper Input Validation vulnerability in OTRS or ((OTRS)) Community Edition database layer module allows an unauthe |
| CVE-2026-48209 | 7.1 | 2026-06-01 | An improper neutralization of user-controllable input in OTRS or ((OTRS)) Community Edition ticket handling allows authe |
| CVE-2026-10225 | 7.3 | 2026-06-01 | A vulnerability was detected in raisulislamg4 student_management_system_by_php up to 310d950e09013d5133c6b9210aff9444382 |
| CVE-2026-10226 | 7.3 | 2026-06-01 | A flaw has been found in raisulislamg4 student_management_system_by_php up to 310d950e09013d5133c6b9210aff9444382d16d1.  |
| CVE-2026-10227 | 7.3 | 2026-06-01 | A vulnerability has been found in raisulislamg4 student_management_system_by_php up to 310d950e09013d5133c6b9210aff94443 |
| CVE-2026-10236 | 7.3 | 2026-06-01 | A vulnerability has been found in SourceCodester Water Billing Management System 1.0. This issue affects some unknown pr |
| CVE-2026-10243 | 7.3 | 2026-06-01 | A security vulnerability has been detected in code-projects Smart Parking System 1.0. Affected is an unknown function of |
| CVE-2026-27788 | 7.8 | 2026-06-01 | Incorrect permission assignment for critical resource issue exists in ServerView Agents for Windows V11.60.04 and earlie |
| CVE-2026-32325 | 7.8 | 2026-06-01 | Privilege chaining issue exists in ServerView Agents for Windows V11.60.04 and earlier. If this vulnerability is exploit |
| CVE-2026-44825 | 8.1 | 2026-06-01 | Hardcoded credentials in the Basic Authentication setup tool (bin/solr auth enable) in Apache Solr versions 9.4.0 throug |
| CVE-2026-48827 | 7.1 | 2026-06-01 | Path traversal vulnerability in Apache MINA SSHD bundle sshd-git. Lack of path validation in git-upload-pack, git-receiv |
| CVE-2026-7858 | 9.8 | 2026-06-01 | A Deserialization of Untrusted Data vulnerability affecting Teamwork Cloud from No Magic Release 2022x through No Magic  |
| CVE-2026-9024 | 8.7 | 2026-06-01 | A Stored Cross-site Scripting (XSS) vulnerability affecting Process Experience Studio in DELMIA Service Process Engineer |
| CVE-2026-10249 | 7.3 | 2026-06-01 | A vulnerability was identified in itsourcecode Online Blood Bank Management System 1.0. Impacted is an unknown function  |
| CVE-2026-10250 | 7.3 | 2026-06-01 | A security flaw has been discovered in itsourcecode Online Blood Bank Management System 1.0. The affected element is an  |
| CVE-2026-10251 | 7.3 | 2026-06-01 | A weakness has been identified in itsourcecode Online House Rental System 1.0. The impacted element is an unknown functi |
| CVE-2026-10252 | 7.3 | 2026-06-01 | A security vulnerability has been detected in itsourcecode Online House Rental System 1.0. This affects an unknown funct |
| CVE-2026-10253 | 7.3 | 2026-06-01 | A vulnerability was detected in itsourcecode Online House Rental System 1.0. This impacts an unknown function of the fil |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-0257 | Palo Alto Networks / PAN-OS | 2026-05-29 | 2026-06-01 | Unknown |
| CVE-2026-48027 | Nx / Nx Console | 2026-05-27 | 2026-06-10 | Known |
| CVE-2026-45321 | TanStack / TanStack | 2026-05-27 | 2026-06-10 | Known |
| CVE-2026-8398 | Daemon / Daemon Tools Lite | 2026-05-27 | 2026-05-30 | Unknown |
| CVE-2026-48172 | LiteSpeed / cPanel Plugin | 2026-05-26 | 2026-05-29 | Unknown |

---

*Total entries in CISA KEV catalog: 1607*