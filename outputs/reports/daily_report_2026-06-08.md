# Vulnerability Intelligence Report

**Date:** 2026-06-08  
**Generated:** 2026-06-08T12:27:54Z  

---

## Executive Summary

Our vulnerability assessment reveals 30 high-severity CVEs requiring immediate attention, with CVSS scores ranging from 7.2 to 9.8. Critical concerns include remote code execution vulnerabilities in WordPress plugins and firewall driver flaws. CISA has added 5 new Known Exploited Vulnerabilities to their catalog this week, including SolarWinds Serv-U and Oracle WebLogic Server issues. The most severe vulnerability (CVE-2023-54352, CVSS 9.8) allows unauthenticated remote code execution in WordPress Seotheme. While none of our monitored CVEs appear in the KEV catalog, the high volume of critical vulnerabilities demands coordinated remediation efforts across multiple system components.

---

## Risk Narrative

The current threat landscape presents significant exposure through web-facing applications and network security components. WordPress plugin vulnerabilities enable attackers to gain initial access through remote code execution, while firewall driver flaws compromise network perimeter defenses. The addition of enterprise software vulnerabilities to CISA's KEV catalog indicates active exploitation attempts against SolarWinds and Oracle products. Organizations face elevated risk of data breaches, service disruption, and regulatory compliance violations. The combination of unauthenticated remote code execution capabilities and network security bypass techniques creates multiple attack vectors for threat actors seeking persistent access to corporate environments.

---

## Prioritized Action Items

1. Immediately patch CVE-2023-54352 (CVSS 9.8) WordPress Seotheme remote code execution vulnerability on all web properties.
2. Prioritize patching of all WordPress plugin vulnerabilities (CVE-2023-54350, CVE-2023-54351) to prevent unauthorized access.
3. Update Comodo Internet Security firewall drivers to address CVE-2026-49494 integer underflow vulnerability.
4. Coordinate with IT teams to patch SolarWinds Serv-U and Oracle WebLogic Server per new CISA KEV requirements.
5. Establish weekly vulnerability monitoring process to track new CISA KEV additions and cross-reference with our infrastructure.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-49494 | 7.5 | 2026-06-07 | Comodo Internet Security's firewall driver Inspect.sys contains an integer underflow in its IPv6 packet parser. The pars |
| CVE-2026-11460 | 7.3 | 2026-06-07 | A flaw has been found in Boost Serialization up to 1.91. The impacted element is an unknown function. This manipulation  |
| CVE-2026-11462 | 7.3 | 2026-06-07 | A vulnerability was found in Chengdu Everbrite Network Technology BeikeShop up to 1.6.0.22. This impacts the function ca |
| CVE-2026-11463 | 7.3 | 2026-06-07 | A vulnerability was determined in USCiLab Cereal up to 1.3.2. Affected is an unknown function of the component Shared Po |
| CVE-2026-11471 | 7.3 | 2026-06-08 | A vulnerability was found in SourceCodester Class and Exam Timetabling System 1.0. The impacted element is an unknown fu |
| CVE-2026-11472 | 7.3 | 2026-06-08 | A vulnerability was determined in SourceCodester Class and Exam Timetabling System 1.0. This affects an unknown function |
| CVE-2026-11474 | 7.3 | 2026-06-08 | A security flaw has been discovered in Kushan2k student-management-system up to f16a4ceaddd6729c4b306ed4641cda3176c1ef2a |
| CVE-2023-54350 | 7.5 | 2026-06-08 | WordPress Augmented-Reality plugin contains a remote code execution vulnerability in the elFinder connector that allows  |
| CVE-2023-54351 | 7.2 | 2026-06-08 | WordPress Sonaar Music Plugin 4.7 contains a stored cross-site scripting vulnerability that allows unauthenticated attac |
| CVE-2023-54352 | 9.8 | 2026-06-08 | WordPress Seotheme contains a remote code execution vulnerability that allows unauthenticated attackers to execute arbit |
| CVE-2024-58348 | 9.8 | 2026-06-08 | WordPress Background Image Cropper version 1.2 contains a remote code execution vulnerability that allows unauthenticate |
| CVE-2024-58349 | 9.8 | 2026-06-08 | WordPress Theme Travelscape 1.0.3 contains an arbitrary file upload vulnerability that allows unauthenticated attackers  |
| CVE-2026-11482 | 7.3 | 2026-06-08 | A vulnerability was identified in SourceCodester Class and Exam Timetabling System 1.0. The impacted element is an unkno |
| CVE-2026-11483 | 7.3 | 2026-06-08 | A security flaw has been discovered in SourceCodester Class and Exam Timetabling System 1.0. This affects an unknown fun |
| CVE-2026-11484 | 7.3 | 2026-06-08 | A weakness has been identified in SourceCodester Class and Exam Timetabling System 1.0. This impacts an unknown function |
| CVE-2026-11485 | 7.3 | 2026-06-08 | A security vulnerability has been detected in SourceCodester Class and Exam Timetabling System 1.0. Affected is an unkno |
| CVE-2026-11486 | 7.3 | 2026-06-08 | A vulnerability was detected in SourceCodester Class and Exam Timetabling System 1.0. Affected by this vulnerability is  |
| CVE-2026-11488 | 7.3 | 2026-06-08 | A vulnerability has been found in code-projects Simple Flight Ticket Booking System 1.0. This affects an unknown part of |
| CVE-2026-11489 | 7.3 | 2026-06-08 | A vulnerability was found in code-projects Online Music Site 1.0. This vulnerability affects unknown code of the file /A |
| CVE-2026-11490 | 7.3 | 2026-06-08 | A vulnerability was determined in code-projects Online Music Site 1.0. This issue affects some unknown processing of the |
| CVE-2026-11498 | 8.8 | 2026-06-08 | A vulnerability was found in Tenda HG7HG9 and HG10 300001138_en_xpon. Affected by this issue is the function asp_voip_Ot |
| CVE-2026-11499 | 9.8 | 2026-06-08 | A vulnerability was determined in Tenda HG7HG9 and HG10 300001138_en_xpon. This affects the function formDOMAINBLK of th |
| CVE-2026-3238 | 7.5 | 2026-06-08 | A flaw was found in Samba’s WINS server component when running as an Active Directory Domain Controller. The WINS protoc |
| CVE-2026-41722 | 8.0 | 2026-06-08 | VMware Cloud Foundation Operations contains multiple stored cross-site scripting vulnerabilities.A malicious actor with  |
| CVE-2026-41723 | 8.0 | 2026-06-08 | VMware Cloud Foundation Operations contains multiple stored cross-site scripting vulnerabilities.A malicious actor with  |
| CVE-2026-41724 | 8.0 | 2026-06-08 | VMware Cloud Foundation Operations contains multiple stored cross-site scripting vulnerabilities.A malicious actor with  |
| CVE-2026-11501 | 7.3 | 2026-06-08 | A security flaw has been discovered in SourceCodester Hospitals Patient Records Management System 1.0. This issue affect |
| CVE-2026-11503 | 8.8 | 2026-06-08 | A security vulnerability has been detected in Tenda CX12L 16.03.53.12. The affected element is the function form_fast_se |
| CVE-2026-11504 | 8.8 | 2026-06-08 | A vulnerability was detected in Tenda CX12L 16.03.53.12. The impacted element is the function setSchedWifi of the file / |
| CVE-2026-50752 | 7.4 | 2026-06-08 | A weakness in the certificate validation logic of the deprecated IKEv1 key exchange may allow an unauthenticated attacke |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-28318 | SolarWinds / Serv-U | 2026-06-05 | 2026-06-19 | Unknown |
| CVE-2026-45247 | Mirasvit / Mirasvit Full Page Cache Warmer | 2026-06-03 | 2026-06-06 | Unknown |
| CVE-2022-0492 | Linux / Kernel | 2026-06-02 | 2026-06-05 | Unknown |
| CVE-2025-48595 | Android / Framework | 2026-06-02 | 2026-06-05 | Unknown |
| CVE-2024-21182 | Oracle / WebLogic Server | 2026-06-01 | 2026-06-04 | Unknown |

---

*Total entries in CISA KEV catalog: 1612*