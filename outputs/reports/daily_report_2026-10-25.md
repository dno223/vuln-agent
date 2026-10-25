# Vulnerability Intelligence Report

**Date:** 2026-10-25  
**Generated:** 2026-10-25T12:57:55Z  

---

## Executive Summary

Our environment faces critical exposure across multiple platforms. Seventeen high-severity CVEs have been identified, including two near-perfect CVSS 9.9 and 9.6 scores in Postiz affecting session token security and arbitrary file read. Oracle Java SE carries a CVSS 9.1 vulnerability in JSSE. Additionally, eight new CISA Known Exploited Vulnerability catalog entries were added in the past seven days, covering Arista VeloCloud, Collabora Online, and Plex Media Server — all indicating active exploitation in the wild. Immediate remediation and patching are required to reduce organizational risk.

---

## Risk Narrative

The current threat landscape combines critical unpatched vulnerabilities with confirmed active exploitation. CISA KEV additions signal that threat actors are actively leveraging weaknesses in widely deployed products including media servers and network orchestration platforms. The Postiz token confusion flaw enables privilege escalation and account takeover at scale. Oracle Java SE exposure broadens attack surface across enterprise environments. Deserialization flaws and missing authorization controls in popular WordPress plugins increase the risk of supply-chain-style compromise. Collectively, these vulnerabilities expose the organization to data breaches, service disruption, unauthorized access, and potential regulatory liability.

---

## Prioritized Action Items

1. Patch or mitigate Postiz CVE-2026-115933 (CVSS 9.9) and CVE-2026-115932 (CVSS 9.6) immediately by rotating shared secrets and restricting media path handling.
2. Apply Oracle Java SE patches for CVE-2026-114820 (CVSS 9.1) across all affected JDK and GraalVM instances without delay.
3. Audit and remediate all eight newly added CISA KEV entries, prioritizing Arista VeloCloud and Plex Media Server given confirmed active exploitation.
4. Address the Unitree Robotics CVE-2026-115995 (CVSS 9.6) by restricting network access to affected robotic systems and applying vendor patches.
5. Remediate deserialization and missing authorization vulnerabilities in WordPress plugins (CVE-2026-114704, CVE-2026-114191) to prevent object injection and privilege escalation.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-115932 | 9.6 | 2026-10-24 | When a post is published, Postiz treats a media path that is not a web address as a file on the server's disk, but it do |
| CVE-2026-114191 | 7.5 | 2026-10-24 | Missing Authorization vulnerability in Knit Pay UPI QR Code Payment Gateway for WooCommerce upi-qr-code-payment-for-wooc |
| CVE-2026-114704 | 7.2 | 2026-10-24 | Deserialization of Untrusted Data vulnerability in Christoph Vielgrader Relevanssi  relevanssi allows Object Injection.T |
| CVE-2026-115933 | 9.9 | 2026-10-24 | Postiz signs its session, invitation and password reset tokens with one shared secret and without any marker of what a t |
| CVE-2026-115969 | 7.3 | 2026-10-24 | A flaw has been found in Travisun Opptrix 0.4.0. This affects an unknown function of the file /api/auth/setup of the com |
| CVE-2026-115970 | 7.3 | 2026-10-24 | A vulnerability has been found in Travisun Opptrix 0.4.0. This impacts an unknown function of the file /api/system-updat |
| CVE-2026-114820 | 9.1 | 2026-10-24 | Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition product of Oracle Java SE |
| CVE-2026-115973 | 7.3 | 2026-10-24 | A vulnerability was identified in FaveoSuite Faveo Helpdesk 2.0.3. Affected by this issue is the function ForgotPassword |
| CVE-2026-115995 | 9.6 | 2026-10-24 | A security vulnerability has been detected in Unitree Robotics Unitree Go2 up to 1.1.11.4. The impacted element is the f |
| CVE-2026-115999 | 7.3 | 2026-10-25 | A vulnerability has been found in mansi-k Restaurant_IMS d7ad49f61ab7cc1ec6eb359ac2b5378bdbde0694. Affected is the funct |
| CVE-2026-116000 | 7.3 | 2026-10-25 | A security flaw has been discovered in Zylon PrivateGPT 1.0.0/1.0.1. This vulnerability affects the function load_file_f |
| CVE-2026-116006 | 7.3 | 2026-10-25 | A vulnerability was detected in YunaiV/zhijiantianya ruoyi-vue-pro up to 2026.09. The affected element is an unknown fun |
| CVE-2026-116048 | 7.3 | 2026-10-25 | A vulnerability was detected in krupalshah EmployeeRecruitmentSystem up to 922ff6d208278282e7c8e36d70d9ae356adec9fe. Aff |
| CVE-2026-116049 | 7.3 | 2026-10-25 | A flaw has been found in krupalshah EmployeeRecruitmentSystem up to 922ff6d208278282e7c8e36d70d9ae356adec9fe. Affected b |
| CVE-2026-116050 | 7.3 | 2026-10-25 | A vulnerability has been found in krupalshah Employee Recruitment System up to 922ff6d208278282e7c8e36d70d9ae356adec9fe. |
| CVE-2026-116067 | 8.2 | 2026-10-25 | Paisa before 0.7.8 contains a path traversal vulnerability in the GetFile, GetSheet, DeleteBackups, and DeleteSheetBacku |
| CVE-2026-116068 | 8.8 | 2026-10-25 | Dokploy through 0.30.10 contains an authorization bypass vulnerability that allows owners or admins of any organization  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-114625 | Arista / VeloCloud Orchestrator | 2026-10-23 | 2026-10-26 | Unknown |
| CVE-2026-110447 | Collabora / Collabora Online – Built-in CODE Server | 2026-10-23 | 2026-10-26 | Unknown |
| CVE-2026-106931 | EG Secure Solutions / SiteGuard Server Edition | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96656 | Plex / Media Server | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96655 | Plex / Media Server | 2026-10-20 | 2026-11-03 | Unknown |
| CVE-2026-96654 | Plex / Media Server | 2026-10-20 | 2026-10-23 | Unknown |
| CVE-2026-96652 | Plex / Media Server | 2026-10-20 | 2026-11-03 | Unknown |
| CVE-2026-110936 | Siemens / Software Center | 2026-10-20 | 2026-11-03 | Unknown |

---

*Total entries in CISA KEV catalog: 1756*