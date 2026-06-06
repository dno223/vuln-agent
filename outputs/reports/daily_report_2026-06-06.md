# Vulnerability Intelligence Report

**Date:** 2026-06-06  
**Generated:** 2026-06-06T10:03:12Z  

---

## Executive Summary

Our environment faces significant exposure from 52 high-severity vulnerabilities, primarily affecting Android systems and X.Org services. Multiple privilege escalation flaws in Samsung Galaxy services and critical buffer overflow vulnerabilities in X server components create substantial attack vectors. Five new CISA Known Exploited Vulnerabilities were added this week, including SolarWinds Serv-U and Oracle WebLogic Server exploits actively targeted by threat actors. The concentration of local privilege escalation vulnerabilities indicates potential for lateral movement if initial access is achieved.

---

## Risk Narrative

The threat landscape shows attackers increasingly targeting privilege escalation vulnerabilities for persistent access and lateral movement. Local attack vectors dominate this vulnerability set, suggesting threat actors focus on post-compromise activities rather than initial access. The addition of enterprise software like SolarWinds and Oracle to CISA's KEV catalog indicates active targeting of corporate infrastructure. Organizations face elevated risk of data breaches and system compromises, particularly in mixed Android-enterprise environments where multiple attack chains could be chained together for maximum impact.

---

## Prioritized Action Items

1. Immediately patch all X.Org X server and Xwayland installations to address critical buffer overflow and use-after-free vulnerabilities.
2. Deploy Samsung Mobile Release June 2026 patches to all Galaxy devices to fix privilege escalation flaws in editing and audio services.
3. Update SolarWinds Serv-U and Oracle WebLogic Server instances within 72 hours due to active exploitation confirmed by CISA.
4. Implement enhanced monitoring for privilege escalation attempts on Android and Linux systems.
5. Conduct emergency vulnerability assessment to identify additional affected systems not captured in current inventory.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-21029 | 7.8 | 2026-06-05 | Improper export of android application components in Galaxy Editing Service prior to SMR Jun-2026 Release 1 allows local |
| CVE-2026-21030 | 7.8 | 2026-06-05 | Improper access control in MediaTek Audio HAL prior to SMR Jun-2026 Release 1 allows local attackers to trigger privileg |
| CVE-2026-21031 | 7.8 | 2026-06-05 | Improper authorization in AppBlock prior to SMR Jun-2026 Release 1 allows local attacker to launch arbitrary activity. U |
| CVE-2026-50265 | 7.0 | 2026-06-05 | A flaw was found in libinput. A local attacker with access to /dev/uinput can inject arbitrary udev properties through t |
| CVE-2026-50256 | 7.8 | 2026-06-05 | A stack-based buffer overflow flaw was found in the X.Org X server and Xwayland. A mismatch between the X server and the |
| CVE-2026-50257 | 7.8 | 2026-06-05 | A use-after-free flaw was found in the X.Org X server and Xwayland in miSyncDestroyFence(). A client that sets up multip |
| CVE-2026-50258 | 7.8 | 2026-06-05 | A stack-based buffer overflow flaw was found in the X.Org X server and Xwayland. The X server has multiple stack buffers |
| CVE-2026-50259 | 7.8 | 2026-06-05 | A stack-based buffer overflow flaw was found in the X.Org X server and Xwayland. _XkbSetMapChecks() declares a fixed-siz |
| CVE-2026-50260 | 7.8 | 2026-06-05 | A use-after-free flaw was found in the X.Org X server and Xwayland in FreeCounter(). A client that sets up multiple Sync |
| CVE-2026-50261 | 7.8 | 2026-06-05 | A use-after-free flaw was found in the X.Org X server and Xwayland in SyncChangeCounter(). A client that sets up multipl |
| CVE-2026-50264 | 7.8 | 2026-06-05 | An out-of-bounds write flaw was found in the X.Org X server and Xwayland in DRIGetBuffers/DRIGetBuffersWithFormat. A cli |
| CVE-2026-50231 | 7.2 | 2026-06-05 | Lyrion Music Server 9.2.0 contains an unauthenticated stored cross-site scripting vulnerability in the log viewer that a |
| CVE-2026-50232 | 7.2 | 2026-06-05 | Lyrion Music Server 9.2.0 contains a stored cross-site scripting vulnerability that allows attackers to inject malicious |
| CVE-2026-50234 | 7.5 | 2026-06-05 | Lyrion Music Server 9.2.0 contains a path traversal vulnerability that allows unauthenticated attackers to read arbitrar |
| CVE-2026-11334 | 7.3 | 2026-06-05 | A vulnerability was detected in tittuvarghese CollegeManagementSystem 3e476335cfbfb9a049e09f474c7ec885f69a9df3/a38852979 |
| CVE-2026-48095 | 8.8 | 2026-06-05 | 7-Zip is a file archiver with a high compression ratio. Versions 26.00 and prior contain a heap buffer overflow vulnerab |
| CVE-2025-5088 | 8.3 | 2026-06-05 | An authenticated Redis session could be used to obtain full root access to all servers in the CVX cluster. Note that thi |
| CVE-2025-71317 | 9.8 | 2026-06-05 | NetMan 204 contains a hard-coded backdoor account with the username and password 'eurek' that grants administrative acce |
| CVE-2025-71318 | 9.8 | 2026-06-05 | NetMan 204 fails to enforce authentication on its administrative pages and command endpoints. A remote, unauthenticated  |
| CVE-2026-11342 | 7.3 | 2026-06-05 | A vulnerability has been found in code-projects Hotel and Tourism Reservation System 1.0. This affects an unknown functi |
| CVE-2026-11344 | 7.3 | 2026-06-05 | A vulnerability was found in code-projects Vehicle Management System 1.0. This impacts an unknown function of the file n |
| CVE-2026-45290 | 7.5 | 2026-06-05 | Cloudburst Network provides network components used within Cloudburst projects. A vulnerability in versions prior to `1. |
| CVE-2026-45291 | 7.5 | 2026-06-05 | Cloudburst Network provides network components used within Cloudburst projects. A vulnerability in versions prior to `1. |
| CVE-2026-45327 | 8.2 | 2026-06-05 | TinyIce is a streaming server for audio and video. In versions 0.8.95 through 2.4.1, missing authentication on WebRTC in |
| CVE-2026-45743 | 8.1 | 2026-06-05 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. 16 file-ma |
| CVE-2026-45744 | 9.9 | 2026-06-05 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. Prior to v |
| CVE-2026-45745 | 8.0 | 2026-06-05 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. Starting i |
| CVE-2026-45746 | 9.0 | 2026-06-05 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. Prior to v |
| CVE-2026-45748 | 9.8 | 2026-06-05 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. The `POST  |
| CVE-2026-45749 | 8.1 | 2026-06-05 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. The `POST  |
| CVE-2026-45750 | 9.0 | 2026-06-05 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. Prior to v |
| CVE-2026-49492 | 8.8 | 2026-06-05 | Markdown Preview Enhanced before 0.8.28 opens external files and links from the preview through a shell and does not val |
| CVE-2026-49493 | 8.8 | 2026-06-05 | Markdown Preview Enhanced before 0.8.28 parses Bitfield fenced code blocks with interpretJS(), which evaluates the block |
| CVE-2026-50733 | 8.8 | 2026-06-05 | Markdown Preview Enhanced before 0.8.28 parses WaveDrom diagrams by evaluating untrusted markdown content with eval(), a |
| CVE-2026-10580 | 9.8 | 2026-06-05 | The Hippoo Mobile App for WooCommerce plugin for WordPress is vulnerable to Authentication Bypass leading to Administrat |
| CVE-2026-46389 | 10.0 | 2026-06-05 | UDS Identity Config builds the Keycloak configuration image (realm, plugins, theme, truststore, JARs) consumed by UDS Co |
| CVE-2026-46392 | 8.7 | 2026-06-05 | HAX CMS helps manage microsite universe with PHP or NodeJs backends. Prior to version 26.0.0 of HAX CMS PHP, the `saveFi |
| CVE-2026-5411 | 8.8 | 2026-06-05 | The WP Captcha PRO (the premium version of the Advanced Google reCAPTCHA plugin, both have the same slug) plugin for Wor |
| CVE-2026-5415 | 8.8 | 2026-06-05 | The WP Captcha PRO (the premium version of the Advanced Google reCAPTCHA plugin, both have the same slug) plugin for Wor |
| CVE-2026-11400 | 8.0 | 2026-06-05 | An untrusted search path issue in the GlobalDatabasePlugin in the AWS Advanced JDBC Wrapper for Amazon Aurora PostgreSQL |
| CVE-2026-11401 | 8.0 | 2026-06-05 | An untrusted search path issue in the GlobalDatabasePlugin in the AWS Advanced Go Wrapper for Amazon Aurora PostgreSQL w |
| CVE-2026-45300 | 7.4 | 2026-06-05 | The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process HT |
| CVE-2026-45758 | 9.6 | 2026-06-05 | Guardrails AI is a Python framework that helps build AI applications. On May 11, 2026 at approximately 6:00 PM Pacific,  |
| CVE-2026-46493 | 7.5 | 2026-06-05 | HAX CMS helps manage microsite universe with PHP or NodeJs backends. Versions prior to 26.0.1 use `uniqid` for generatin |
| CVE-2026-11422 | 7.1 | 2026-06-05 | Markdown Preview Enhanced 0.8.x with crossnote engine 0.9.28 contains a code injection vulnerability in the WaveDrom ren |
| CVE-2026-11416 | 8.1 | 2026-06-05 | MoviePilot contains a path traversal vulnerability in the AliPan, U115, and Rclone cloud storage download handlers where |
| CVE-2026-7654 | 8.8 | 2026-06-05 | The Admin Columns plugin for WordPress is vulnerable to PHP Object Injection leading to Remote Code Execution in version |
| CVE-2026-9290 | 7.5 | 2026-06-06 | The WP User Manager – User Profile Builder & Membership plugin for WordPress is vulnerable to Local File Inclusion in al |
| CVE-2026-8438 | 7.2 | 2026-06-06 | The All-In-One Security (AIOS) – Security and Firewall plugin for WordPress is vulnerable to Stored Cross-Site Scripting |
| CVE-2026-8901 | 7.2 | 2026-06-06 | The Integration for Freshsales – Contact Form 7, WPForms, Elementor, Gravity Forms and More plugin for WordPress is vuln |
| CVE-2026-7537 | 7.2 | 2026-06-06 | The MDJM Event Management plugin for WordPress is vulnerable to Arbitrary File Upload in all versions up to, and includi |
| CVE-2026-9851 | 7.2 | 2026-06-06 | The Booking Package plugin for WordPress is vulnerable to Privilege Escalation via Account Takeover in versions up to, a |

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