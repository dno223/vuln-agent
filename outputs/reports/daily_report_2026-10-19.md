# Vulnerability Intelligence Report

**Date:** 2026-10-19  
**Generated:** 2026-10-19T15:17:17Z  

---

## Executive Summary

Our environment faces significant exposure from 47 high-severity vulnerabilities, including a critical CVSS 9.8 flaw in GeoWebServer and multiple high-risk issues in database, CMS, and container infrastructure components. Nine new actively exploited vulnerabilities were added to CISA's Known Exploited Vulnerabilities catalog this week, targeting widely deployed products including BeyondTrust, Fortinet, Atlassian, and Cisco. While no monitored assets currently match KEV entries, the volume and severity of new disclosures demand immediate attention. Exploitation of these vulnerabilities could result in unauthorized system access, data breaches, or full system compromise.

---

## Risk Narrative

Threat actors are actively exploiting vulnerabilities in enterprise-grade remote access, email security, and collaboration platforms, as evidenced by this week's CISA KEV additions. The presence of a CVSS 9.8 vulnerability in GeoWebServer represents a critical attack surface for network-level compromise. Supply chain and container risks are elevated due to flaws in bootc image validation, while database vulnerabilities in openGauss introduce potential for privilege escalation and data exfiltration. The combination of publicly disclosed high-severity CVEs and active exploitation campaigns significantly increases the likelihood of a successful breach, with potential business impacts including operational disruption, regulatory exposure, and reputational damage.

---

## Prioritized Action Items

1. Immediately patch or isolate GeoWebServer instances affected by CVE-2026-108983 (CVSS 9.8), as unauthenticated remote exploitation is likely feasible.
2. Audit and remediate all systems running BeyondTrust Remote Support, Fortinet, Atlassian, and Cisco Secure Email Gateway products against the five newly added CISA KEV entries within 24–72 hours.
3. Apply available patches for the openGauss-server HLL buffer validation flaw (CVE-2026-111441) and JDBC class-loading vulnerability (CVE-2026-111440) to prevent database-layer exploitation.
4. Review and harden bootc container image validation policies to address CVE-2026-16487 and CVE-2026-16460, preventing unauthorized or unvalidated image deployments.
5. Establish continuous KEV catalog monitoring with automated alerting to reduce response time if any currently monitored assets appear in future CISA KEV additions.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-112025 | 7.3 | 2026-10-18 | A weakness has been identified in light0011 cms c774dce31c6df0055568a8d5c53d964d99be199d/f72cf46f601efb2a0618c3814cc2f61 |
| CVE-2026-108983 | 9.8 | 2026-10-19 | A vulnerability is in Web Server default connection ports under the process name GeoWebServer.exe . |
| CVE-2026-108984 | 7.5 | 2026-10-19 | A vulnerability is in Web Server default connection ports under the process name GeoWebServer.exe . |
| CVE-2026-111441 | 8.1 | 2026-10-19 | 在 openGauss-server 的 src/gausskernel/cbb/utils/hll/hll.cpp 中，内置函数 HllObjectUnpack() 存在长度校验缺陷。该函数从用户提供的 packed HLL 解析 len |
| CVE-2026-112044 | 7.3 | 2026-10-19 | A security vulnerability has been detected in dotnet eShop up to 913acea66708a59595351174cee9b29f37179d29. The affected  |
| CVE-2026-111440 | 7.0 | 2026-10-19 | 在 openGauss-connector-jdbc 的 pgjdbc/src/main/java/org/postgresql/log/LogFactory.java 中，LogFactory 根据 JDBC 连接参数中的 logger  |
| CVE-2026-112082 | 7.5 | 2026-10-19 | A vulnerability was identified in sgl-project SGLang up to 0.5.19. This impacts the function Scheduler.expert_distributi |
| CVE-2026-16487 | 8.1 | 2026-10-19 | A flaw was found in bootc when operating with the default containers signature policy. Automatic or manual upgrades of a |
| CVE-2026-16460 | 7.4 | 2026-10-19 | A flaw was found in bootc and ostree. Already-staged deployments are finalized without revalidating the deployment's con |
| CVE-2026-76740 | 7.2 | 2026-10-19 | A security vulnerability in HPE Compute Scale-up Server 3200 and 3250 platforms, Superdome Flex and Superdome Flex 280 s |
| CVE-2026-104679 | 7.1 | 2026-10-19 | VOCALOID6 Editor provided by Yamaha Corporation improperly restricts XML external entity references. Loading a specially |
| CVE-2026-110379 | 7.1 | 2026-10-19 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Ays Pro Quiz Maker |
| CVE-2026-110887 | 9.9 | 2026-10-19 | Improper Control of Generation of Code ('Code Injection') vulnerability in HivePress HivePress hivepress allows Remote C |
| CVE-2026-111398 | 7.7 | 2026-10-19 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in PT Norther Lights Produc |
| CVE-2026-111406 | 9.9 | 2026-10-19 | Unrestricted Upload of File with Dangerous Type vulnerability in PT Norther Lights Production MapSVG mapsvg-lite-interac |
| CVE-2026-111408 | 8.8 | 2026-10-19 | Deserialization of Untrusted Data vulnerability in ExpressTech Quiz And Survey Master quiz-master-next allows Object Inj |
| CVE-2026-112104 | 7.3 | 2026-10-19 | A flaw has been found in eremef bandcamp-player up to 1.8.33-beta. The impacted element is an unknown function of the fi |
| CVE-2026-78164 | 8.2 | 2026-10-19 | Improper Neutralization of Special Elements Used in a Template Engine and Exposure of Sensitive Information to an Unauth |
| CVE-2026-78165 | 8.8 | 2026-10-19 | Deserialization of Untrusted Data vulnerability in Apache Camel Spring Redis component.



This issue affects Apache Cam |
| CVE-2026-79983 | 7.4 | 2026-10-19 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Camel FTP compone |
| CVE-2026-79984 | 7.4 | 2026-10-19 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Camel Mina SFTP c |
| CVE-2026-79985 | 7.4 | 2026-10-19 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Camel SMB compone |
| CVE-2026-79986 | 7.4 | 2026-10-19 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Camel Azure Files |
| CVE-2026-80312 | 8.2 | 2026-10-19 | Improper Authentication vulnerability in Apache Camel OAuth component.



This issue affects Apache Camel: from 4.11.0 b |
| CVE-2026-80343 | 8.2 | 2026-10-19 | Improper Handling of Case Sensitivity vulnerability in Apache Camel Netty HTTP component.



This issue affects Apache C |
| CVE-2026-80344 | 8.2 | 2026-10-19 | Server-Side Request Forgery (SSRF) vulnerability in Apache Camel AS2 component.

This issue affects Apache Camel: from 4 |
| CVE-2026-83531 | 8.8 | 2026-10-19 | Improper Control of Generation of Code ('Code Injection'), Improper Neutralization of Special Elements used in an Expres |
| CVE-2026-85250 | 7.5 | 2026-10-19 | Improper Restriction of XML External Entity Reference vulnerability in Apache Camel XPath component.

This issue affects |
| CVE-2026-85251 | 7.5 | 2026-10-19 | Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Apache Camel HTTP component.

This issue aff |
| CVE-2026-88901 | 8.2 | 2026-10-19 | Improper Restriction of XML External Entity Reference vulnerability in Apache Camel.



This issue affects Apache Camel: |
| CVE-2026-112139 | 7.3 | 2026-10-19 | A vulnerability has been found in subhajitkhan online-clinic-management-system up to e9ee77a8827a1446220fa07ee693dc4d9a2 |
| CVE-2026-88900 | 8.8 | 2026-10-19 | Deserialization of Untrusted Data vulnerability in Apache Camel Camel-Jgroups component.



This issue affects Apache Ca |
| CVE-2026-103314 | 7.4 | 2026-10-19 | A flaw was found in Red Hat Advanced Cluster Security for Kubernetes (RHACS). The Central SAML authentication ACS endpoi |
| CVE-2026-112141 | 7.3 | 2026-10-19 | A vulnerability was determined in satya-vinay Events-Management-System up to 437c77ceb69bf9fe2e3f4f46f7871b83f425383a. A |
| CVE-2026-112142 | 7.3 | 2026-10-19 | A vulnerability was identified in satya-vinay Events-Management-System up to 437c77ceb69bf9fe2e3f4f46f7871b83f425383a. A |
| CVE-2026-112143 | 7.3 | 2026-10-19 | A security flaw has been discovered in satya-vinay Events-Management-System up to 437c77ceb69bf9fe2e3f4f46f7871b83f42538 |
| CVE-2026-112145 | 7.3 | 2026-10-19 | A security vulnerability has been detected in speaches-ai speaches up to 0.9.0-rc.3. This vulnerability affects the func |
| CVE-2026-112146 | 7.4 | 2026-10-19 | A vulnerability was detected in D-Link E15, M32, R15 and R32. This issue affects some unknown processing of the file /et |
| CVE-2026-112262 | 7.1 | 2026-10-19 | RisingWave before 3.1.0 contains a missing authorization vulnerability that allows low-privileged SQL users to read and  |
| CVE-2026-112263 | 7.8 | 2026-10-19 | Television (tv) 0.15.0 through 0.15.9 contains an OS command injection vulnerability that allows attackers to run shell  |
| CVE-2026-112264 | 7.8 | 2026-10-19 | BentoML through 1.4.39 contains a Dockerfile instruction injection vulnerability that allows attackers to add arbitrary  |
| CVE-2026-112287 | 7.1 | 2026-10-19 | Krayin CRM before 2.2.7 contains a broken object level authorization vulnerability in EmailController write actions that |
| CVE-2026-112292 | 9.8 | 2026-10-19 | CheckCle through 1.6.0 contains a missing authorization vulnerability that allows unauthenticated attackers to read, mod |
| CVE-2026-112296 | 9.8 | 2026-10-19 | FlyCms through commit edfdf724 contains a default credentials vulnerability that allows unauthenticated remote attackers |
| CVE-2026-112149 | 7.3 | 2026-10-19 | A vulnerability was identified in vraj404 Criminal-Management-System up to 2808d057e7ddc5295519a487365b0cacfd0ba8c4. Thi |
| CVE-2026-112150 | 7.3 | 2026-10-19 | A security flaw has been discovered in vraj404 Criminal-Management-System up to 2808d057e7ddc5295519a487365b0cacfd0ba8c4 |
| CVE-2026-112151 | 7.3 | 2026-10-19 | A weakness has been identified in vraj404 Criminal Management System up to 2808d057e7ddc5295519a487365b0cacfd0ba8c4. Aff |

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