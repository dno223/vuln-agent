# Vulnerability Intelligence Report

**Date:** 2026-06-05  
**Generated:** 2026-06-05T11:28:24Z  

---

## Executive Summary

Our environment faces significant cybersecurity exposure with 181 high-severity vulnerabilities detected, including critical CVSS 9.8 rated flaws affecting SQL injection, file download, and code execution vectors. Five new CISA KEV entries in the past week indicate active exploitation of vulnerabilities in Linux Kernel, Oracle WebLogic, and Palo Alto Networks systems. The threat landscape shows attackers targeting authentication bypasses, privilege escalation, and unauthenticated attack vectors that could lead to data breaches and system compromise.

---

## Risk Narrative

The current threat landscape reveals attackers actively exploiting authentication and authorization weaknesses across multiple platforms. With five new CISA KEV additions including Linux Kernel and Oracle WebLogic vulnerabilities, adversaries are leveraging known exploits for initial access and privilege escalation. The concentration of SQL injection and cross-site scripting vulnerabilities creates multiple attack vectors for data exfiltration. Business operations face potential disruption through system compromises, while regulatory compliance risks increase due to possible data breaches from unauthenticated attack vectors.

---

## Prioritized Action Items

1. Immediately patch or isolate systems running OpenShift Pipelines operator (CVE-2026-10840) due to CVSS 9.6 privilege escalation risk.
2. Conduct emergency security assessment of TeknoPass systems for authorization bypass vulnerability (CVE-2026-4104) with CVSS 9.8 rating.
3. Review and update Oracle WebLogic Server instances to address newly exploited CVE-2024-21182 on CISA KEV list.
4. Implement web application firewall rules to block SQL injection attempts targeting identified vulnerable applications.
5. Schedule comprehensive vulnerability scanning within 48 hours to identify additional instances of these high-risk CVEs.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2025-52612 | 7.1 | 2026-06-04 | HCL iControl was affected by Export CSV - CSV Injection vulnerability. It is vulnerable to a reflected cross-site script |
| CVE-2026-10840 | 9.6 | 2026-06-04 | A flaw was found in the OpenShift Pipelines operator. The tekton-scheduler-rolebinding ClusterRoleBinding grants the sys |
| CVE-2026-10843 | 7.2 | 2026-06-04 | A flaw was found in the OpenShift Cloud Credential Operator Mint-mode IAM policies for AWS. Operator credentials are pro |
| CVE-2026-4104 | 9.8 | 2026-06-04 | Authorization bypass through User-Controlled SQL primary key vulnerability in Akmer Informatics Automation Industry and  |
| CVE-2019-25726 | 8.2 | 2026-06-04 | All in One Video Downloader 1.2 contains an SQL injection vulnerability that allows unauthenticated attackers to execute |
| CVE-2019-25727 | 9.8 | 2026-06-04 | WordPress Plugin ad manager wd 1.0.11 contains an arbitrary file download vulnerability that allows unauthenticated atta |
| CVE-2019-25728 | 8.2 | 2026-06-04 | Care2x 2.7 contains multiple SQL injection vulnerabilities that allow unauthenticated attackers to execute arbitrary SQL |
| CVE-2019-25729 | 9.8 | 2026-06-04 | PDF Signer 3.0 contains a server-side template injection vulnerability that allows unauthenticated attackers to execute  |
| CVE-2019-25730 | 8.2 | 2026-06-04 | Listing Hub CMS 1.0 contains a SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary SQ |
| CVE-2019-25731 | 7.2 | 2026-06-04 | Zuz Music 2.1 contains a persistent cross-site scripting vulnerability that allows unauthenticated attackers to inject m |
| CVE-2019-25732 | 8.2 | 2026-06-04 | PHP EI-Tube Script 3 contains an SQL injection vulnerability that allows unauthenticated attackers to execute arbitrary  |
| CVE-2019-25733 | 8.4 | 2026-06-04 | NetShareWatcher 1.5.8.0 contains a structured exception handler buffer overflow vulnerability that allows local attacker |
| CVE-2019-25735 | 8.4 | 2026-06-04 | AllPlayer 7.4 contains a local buffer overflow vulnerability in URL handling that allows attackers to overwrite structur |
| CVE-2019-25736 | 8.4 | 2026-06-04 | LabF nfsAxe 3.7 Ping Client contains a buffer overflow vulnerability that allows local attackers to execute arbitrary co |
| CVE-2019-25737 | 7.2 | 2026-06-04 | Live Chat Unlimited 2.8.3 contains a stored cross-site scripting vulnerability that allows unauthenticated attackers to  |
| CVE-2019-25738 | 9.8 | 2026-06-04 | WordPress Hybrid Composer 1.4.6 contains an unauthenticated settings change vulnerability that allows unauthenticated at |
| CVE-2019-25741 | 9.8 | 2026-06-04 | Mobatek MobaXterm 12.1 contains a structured exception handling (SEH) based buffer overflow vulnerability in the usernam |
| CVE-2019-25745 | 8.2 | 2026-06-04 | WordPress Plugin Google Review Slider 6.1 contains a time-based blind SQL injection vulnerability that allows unauthenti |
| CVE-2025-46638 | 7.5 | 2026-06-04 | Dell BSAFE SSL-J contains an allocation of resources without limits or throttling vulnerability. An unauthenticated remo |
| CVE-2025-59874 | 8.1 | 2026-06-04 | HCL Hive Telco Observability is affected by  a Required directives missing from the CSP issue is detected in keycloak co |
| CVE-2026-8037 | 9.6 | 2026-06-04 | OS Command Injection Remote Code Execution Vulnerability in API in Progress ADC Products allows an un-authenticated atta |
| CVE-2026-28318 | 7.5 | 2026-06-04 | SolarWinds Serv-U is susceptible to specially crafted POST requests that crash the Serv-U service without authentication |
| CVE-2026-35906 | 9.6 | 2026-06-04 | An undocumented debug CGI endpoint in T3 Technology CPE models T625Pro v1.0.07, T6825G v1.0.03 allows unauthenticated at |
| CVE-2026-36176 | 7.1 | 2026-06-04 | GNCC GP5 v7.1.76 was discovered to store pre-signed Backblaze B2 upload URLs (PUT requests) in plaintext to the serial c |
| CVE-2026-43984 | 8.9 | 2026-06-04 | Tautulli is a Python based monitoring and tracking tool for Plex Media Server. Versions prior to 2.17.1 expose `log_js_e |
| CVE-2026-43985 | 8.8 | 2026-06-04 | Tautulli is a Python based monitoring and tracking tool for Plex Media Server. Versions prior to 2.17.1 expose `configUp |
| CVE-2026-43986 | 9.9 | 2026-06-04 | Tautulli is a Python based monitoring and tracking tool for Plex Media Server. Versions prior to 2.17.1 expose a public  |
| CVE-2026-44393 | 7.4 | 2026-06-04 | An issue was discovered in OpenStack oslo.messaging 1.0.0 through 17.3.0. The oslo.messaging RabbitMQ driver does not pe |
| CVE-2026-5228 | 8.8 | 2026-06-04 | Improper Access Control, Missing Authorization vulnerability in Kurt Software Studio WriteUp Mobile App allows Accessing |
| CVE-2025-67446 | 9.8 | 2026-06-04 | Improper Authentication (Authentication Bypass) exists in Neterbit NW-431F Router 20241014-IR03 and before. The router u |
| CVE-2026-46741 | 7.5 | 2026-06-04 | Etsy::StatsD versions through 1.002002 for Perl allow metric injections.

The metric names and values are not checked fo |
| CVE-2026-49941 | 7.5 | 2026-06-04 | Net::CIDR::Set versions through 0.20 for Perl did not validate IP addresses.

The add method called the _encode method t |
| CVE-2026-49942 | 7.3 | 2026-06-04 | Net::CIDR::Set versions through 0.20 for Perl did not validate network masks.

The mask portion of a network mask could  |
| CVE-2026-50076 | 9.1 | 2026-06-04 | Deserialization of Untrusted Data in the Java replace-resolve path in Apache Fory fory-core Java SDK before 1.1.0 on Jav |
| CVE-2025-67447 | 9.8 | 2026-06-04 | The network diagnosis (ping) module in Neterbit NW-431F Router 20241014-IR03 and before is vulnerable to OS command inje |
| CVE-2025-67448 | 7.1 | 2026-06-04 | The SMS module in Neterbit NW-431F Router 20241014-IR03 and before is vulnerable to stored XSS. The application does not |
| CVE-2025-69755 | 8.2 | 2026-06-04 | An issue in Neterbit NW-431F Router vNW-431F-20241014-IR03 allows a remote attacker to obtain sensitive information and  |
| CVE-2026-10796 | 7.5 | 2026-06-04 | nvm (Node Version Manager) through 0.40.4 executes arbitrary commands from version strings supplied by the configured No |
| CVE-2026-10880 | 9.8 | 2026-06-04 | OSNexus QuantaStor SDS Manager is vulnerable to SQL injection in the login endpoint. The username field is not properly  |
| CVE-2026-25550 | 9.8 | 2026-06-04 | Seagull Software BarTender 2010, 2016, and 2019 contain an unauthenticated remote code execution vulnerability in the .N |
| CVE-2026-25551 | 7.8 | 2026-06-04 | Seagull Software BarTender 2021 R1 through 12.0.1 contains an insecure deserialization vulnerability that allows low-pri |
| CVE-2026-50292 | 7.4 | 2026-06-04 | In libinput before 1.30.4 and 1.31.x before 1.31.3, libinput-device-group unescaped phys output can inject udev properti |
| CVE-2025-71316 | 9.8 | 2026-06-04 | SQLite 'sqldiff.exe' does not securely handle the way the Microsoft Windows C runtime converts Unicode characters to ANS |
| CVE-2026-41234 | 7.6 | 2026-06-04 | Froxlor is open source server administration software. Prior to version 2.3.7, the `DomainZones.add` API endpoint does n |
| CVE-2026-41236 | 8.8 | 2026-06-04 | Froxlor is open source server administration software. Version 2.3.6 contains a symlink-following flaw in the root-owned |
| CVE-2026-41249 | 8.2 | 2026-06-04 | CoreShop is a Pimcore enhanced eCommerce solution. In versions 5.0.1 through 5.1.0-beta.1,, the GitHub Actions workflow  |
| CVE-2026-41518 | 7.6 | 2026-06-04 | Chartbrew is an open-source web application that can connect directly to databases and APIs and use the data to create c |
| CVE-2026-10870 | 7.2 | 2026-06-04 | A flaw has been found in Shibby Tomato 1.28.0000. This affects the function start_dhcpc of the file /sbin/rc of the comp |
| CVE-2026-10871 | 7.2 | 2026-06-04 | A vulnerability has been found in Shibby Tomato 1.28.0000. This vulnerability affects the function start_6rd_tunnel of t |
| CVE-2024-27890 | 9.6 | 2026-06-04 | Affected platforms running Arista EOS with OpenConfig configured, a gNMI Set request can be run when it should have been |
| CVE-2024-27892 | 9.6 | 2026-06-04 | Affected platforms running Arista EOS with OpenConfig configured, a gNMI Set request can be run when it should have been |
| CVE-2025-8873 | 7.5 | 2026-06-04 | On affected platforms running Arista EOS with IPsec configured, a specially crafted packet can cause the dataplane to st |
| CVE-2026-10872 | 7.2 | 2026-06-04 | A vulnerability was found in Shibby Tomato 1.28.0000. This issue affects the function start_vpnserver of the file /sbin/ |
| CVE-2026-10873 | 7.2 | 2026-06-04 | A vulnerability was determined in Shibby Tomato 1.28.0000. Impacted is the function rstats_path of the file /bin/rstats  |
| CVE-2026-10881 | 9.6 | 2026-06-04 | Out of bounds read and write in ANGLE in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to potentially p |
| CVE-2026-10882 | 8.8 | 2026-06-04 | Use after free in Network in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code vi |
| CVE-2026-10883 | 8.8 | 2026-06-04 | Type Confusion in ANGLE in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to potentially exploit heap co |
| CVE-2026-10884 | 8.3 | 2026-06-04 | Use after free in Chromecast in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the r |
| CVE-2026-10885 | 8.8 | 2026-06-04 | Use after free in Chrome for iOS in Google Chrome on iOS prior to 149.0.7827.53 allowed a remote attacker to execute arb |
| CVE-2026-10886 | 9.6 | 2026-06-04 | Use after free in FileSystem in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to potentially perform a  |
| CVE-2026-10887 | 8.1 | 2026-06-04 | Use after free in Chromoting in Google Chrome on Mac prior to 149.0.7827.53 allowed a remote attacker to execute arbitra |
| CVE-2026-10888 | 8.8 | 2026-06-04 | Use after free in Cast Streaming in Google Chrome prior to 149.0.7827.53 allowed an attacker on the local network segmen |
| CVE-2026-10889 | 8.3 | 2026-06-04 | Out of bounds read in ANGLE in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the re |
| CVE-2026-10890 | 8.8 | 2026-06-04 | Use after free in Cast in Google Chrome prior to 149.0.7827.53 allowed an attacker on the local network segment to poten |
| CVE-2026-10891 | 8.8 | 2026-06-04 | Use after free in GFX in Google Chrome on Linux prior to 149.0.7827.53 allowed a remote attacker to potentially exploit  |
| CVE-2026-10894 | 8.3 | 2026-06-04 | Use after free in Printing in Google Chrome on Linux prior to 149.0.7827.53 allowed a remote attacker who had compromise |
| CVE-2026-10895 | 8.8 | 2026-06-04 | Use after free in Ozone in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code via  |
| CVE-2026-10896 | 8.8 | 2026-06-04 | Use after free in Chrome for iOS in Google Chrome on iOS prior to 149.0.7827.53 allowed a remote attacker to execute arb |
| CVE-2026-10898 | 8.3 | 2026-06-04 | Stack buffer overflow in GPU in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the r |
| CVE-2026-10899 | 7.5 | 2026-06-04 | Use after free in Ozone in Google Chrome on Linux prior to 149.0.7827.53 allowed a remote attacker who convinced a user  |
| CVE-2026-10900 | 7.5 | 2026-06-04 | Use after free in Passwords in Google Chrome on Mac prior to 149.0.7827.53 allowed a remote attacker who convinced a use |
| CVE-2026-10901 | 7.5 | 2026-06-04 | Use after free in Passwords in Google Chrome on Mac prior to 149.0.7827.53 allowed a remote attacker who convinced a use |
| CVE-2026-10902 | 8.8 | 2026-06-04 | Use after free in Ozone in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code via  |
| CVE-2026-10903 | 8.8 | 2026-06-04 | Use after free in WebRTC in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-10905 | 8.3 | 2026-06-04 | Use after free in Network in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the rend |
| CVE-2026-10906 | 7.5 | 2026-06-04 | Use after free in WebAuthentication in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who convinced a us |
| CVE-2026-10907 | 8.8 | 2026-06-04 | Out of bounds write in ANGLE in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to potentially exploit he |
| CVE-2026-10908 | 8.3 | 2026-06-04 | Use after free in FullScreen in Google Chrome on Windows prior to 149.0.7827.53 allowed a remote attacker who had compro |
| CVE-2026-10909 | 8.3 | 2026-06-04 | Use after free in Dawn in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the rendere |
| CVE-2026-10910 | 8.8 | 2026-06-04 | Type Confusion in V8 in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-10911 | 8.3 | 2026-06-04 | Insufficient validation of untrusted input in Media in Google Chrome prior to 149.0.7827.53 allowed a remote attacker wh |
| CVE-2026-10913 | 8.8 | 2026-06-04 | Use after free in ANGLE in Google Chrome on Windows prior to 149.0.7827.53 allowed a remote attacker to execute arbitrar |
| CVE-2026-10914 | 8.8 | 2026-06-04 | Use after free in ANGLE in Google Chrome on Windows prior to 149.0.7827.53 allowed a remote attacker to execute arbitrar |
| CVE-2026-10915 | 8.3 | 2026-06-04 | Use after free in Core in Google Chrome on iOS prior to 149.0.7827.53 allowed a remote attacker who had compromised the  |
| CVE-2026-10917 | 8.3 | 2026-06-04 | Insufficient validation of untrusted input in Media in Google Chrome prior to 149.0.7827.53 allowed a remote attacker wh |
| CVE-2026-10918 | 8.3 | 2026-06-04 | Use after free in Viz in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the renderer |
| CVE-2026-10919 | 8.3 | 2026-06-04 | Use after free in ANGLE in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the render |
| CVE-2026-10920 | 8.3 | 2026-06-04 | Insufficient validation of untrusted input in WebShare in Google Chrome on Mac prior to 149.0.7827.53 allowed a remote a |
| CVE-2026-10921 | 8.3 | 2026-06-04 | Integer overflow in Dawn in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the rende |
| CVE-2026-10924 | 8.3 | 2026-06-04 | Integer overflow in Chromecast in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the |
| CVE-2026-10925 | 8.3 | 2026-06-04 | Out of bounds write in Skia in Google Chrome on Mac prior to 149.0.7827.53 allowed a remote attacker who had compromised |
| CVE-2026-10926 | 8.8 | 2026-06-04 | Use after free in Cast in Google Chrome prior to 149.0.7827.53 allowed an attacker on the local network segment to execu |
| CVE-2026-10927 | 8.3 | 2026-06-04 | Out of bounds read in Dawn in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the ren |
| CVE-2026-10928 | 8.8 | 2026-06-04 | Script injection in Headless in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code |
| CVE-2026-10929 | 8.3 | 2026-06-04 | Heap buffer overflow in ANGLE in Google Chrome on Android prior to 149.0.7827.53 allowed a remote attacker who had compr |
| CVE-2026-10932 | 8.8 | 2026-06-04 | Use after free in UI in Google Chrome on Android prior to 149.0.7827.53 allowed a remote attacker to potentially exploit |
| CVE-2026-10933 | 8.3 | 2026-06-04 | Use after free in Audio in Google Chrome on Windows prior to 149.0.7827.53 allowed a remote attacker who had compromised |
| CVE-2026-10934 | 8.3 | 2026-06-04 | Use after free in Autofill in Google Chrome on Android prior to 149.0.7827.53 allowed a remote attacker who had compromi |
| CVE-2026-10935 | 8.8 | 2026-06-04 | Type Confusion in V8 in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-10936 | 8.8 | 2026-06-04 | Type Confusion in V8 in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-10939 | 8.8 | 2026-06-04 | Use after free in WebRTC in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-10940 | 8.3 | 2026-06-04 | Race in Codecs in Google Chrome on Windows prior to 149.0.7827.53 allowed a remote attacker who had compromised the rend |
| CVE-2026-10941 | 8.8 | 2026-06-04 | Out of bounds memory access in Skia in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitra |
| CVE-2026-10942 | 7.8 | 2026-06-04 | Inappropriate implementation in UI in Google Chrome on Windows prior to 149.0.7827.53 allowed a local attacker to perfor |
| CVE-2026-10943 | 8.8 | 2026-06-04 | Use after free in WebRTC in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-10945 | 8.8 | 2026-06-04 | Use after free in PDF in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who convinced a user to engage i |
| CVE-2026-10946 | 7.5 | 2026-06-04 | Heap buffer overflow in Media in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who convinced a user to  |
| CVE-2026-10947 | 8.8 | 2026-06-04 | Use after free in WebRTC in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-10948 | 8.8 | 2026-06-04 | Use after free in WebRTC in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-10949 | 8.3 | 2026-06-04 | Heap buffer overflow in Video in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the  |
| CVE-2026-10952 | 8.8 | 2026-06-04 | Use after free in Chrome for iOS in Google Chrome on iOS prior to 149.0.7827.53 allowed a remote attacker to potentially |
| CVE-2026-10953 | 8.3 | 2026-06-04 | Use after free in Core in Google Chrome on Android prior to 149.0.7827.53 allowed a remote attacker who had compromised  |
| CVE-2026-10954 | 8.8 | 2026-06-04 | Use after free in Actor in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-10956 | 8.8 | 2026-06-04 | Use after free in MimeHandlerView in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary |
| CVE-2026-10957 | 8.8 | 2026-06-04 | Use after free in Glic in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code insid |
| CVE-2026-10958 | 8.8 | 2026-06-04 | Use after free in Chrome for iOS in Google Chrome on iOS prior to 149.0.7827.53 allowed a remote attacker who convinced  |
| CVE-2026-10959 | 8.8 | 2026-06-04 | Use after free in Input in Google Chrome on Android prior to 149.0.7827.53 allowed a remote attacker to execute arbitrar |
| CVE-2026-10960 | 8.3 | 2026-06-04 | Uninitialized Use in Codecs in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the re |
| CVE-2026-10961 | 8.3 | 2026-06-04 | Use after free in Chrome for iOS in Google Chrome on iOS prior to 149.0.7827.53 allowed a remote attacker who had compro |
| CVE-2026-10962 | 8.8 | 2026-06-04 | Type Confusion in Media in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-10963 | 8.8 | 2026-06-04 | Integer overflow in V8 in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code insid |
| CVE-2026-10964 | 8.8 | 2026-06-04 | Integer overflow in V8 in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code insid |
| CVE-2026-10965 | 8.8 | 2026-06-04 | Integer overflow in DevTools in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code |
| CVE-2026-10967 | 8.3 | 2026-06-04 | Use after free in SurfaceCapture in Google Chrome on Android prior to 149.0.7827.53 allowed a remote attacker who had co |
| CVE-2026-10969 | 7.5 | 2026-06-04 | Insufficient validation of untrusted input in Extensions in Google Chrome prior to 149.0.7827.53 allowed a remote attack |
| CVE-2026-10970 | 8.3 | 2026-06-04 | Insufficient validation of untrusted input in InterestGroups in Google Chrome prior to 149.0.7827.53 allowed a remote at |
| CVE-2026-10975 | 8.8 | 2026-06-04 | Use after free in WebRTC in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-10978 | 8.8 | 2026-06-04 | Use after free in Chromoting in Google Chrome on Windows prior to 149.0.7827.53 allowed a remote attacker to execute arb |
| CVE-2026-10982 | 8.8 | 2026-06-04 | Use after free in WebXR in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-10986 | 8.8 | 2026-06-04 | Integer overflow in Media in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code in |
| CVE-2026-10987 | 8.8 | 2026-06-04 | Integer overflow in V8 in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code insid |
| CVE-2026-10991 | 8.8 | 2026-06-04 | Use after free in V8 in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who convinced a user to engage in |
| CVE-2026-11000 | 8.8 | 2026-06-04 | Use after free in Fonts in Google Chrome on Linux prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary  |
| CVE-2026-11003 | 8.8 | 2026-06-04 | Use after free in WebRTC in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-11028 | 8.8 | 2026-06-04 | Use after free in Media in Google Chrome on Linux and ChromeOS prior to 149.0.7827.53 allowed a remote attacker who had  |
| CVE-2026-11046 | 8.8 | 2026-06-04 | Insufficient validation of untrusted input in Media in Google Chrome prior to 149.0.7827.53 allowed a remote attacker wh |
| CVE-2026-11049 | 8.8 | 2026-06-04 | Use after free in Password Manager in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrar |
| CVE-2026-11050 | 8.8 | 2026-06-04 | Use after free in V8 in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-11054 | 8.8 | 2026-06-04 | Use after free in WebRTC in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-11055 | 8.8 | 2026-06-04 | Use after free in ANGLE in Google Chrome on Windows prior to 149.0.7827.53 allowed a remote attacker to execute arbitrar |
| CVE-2026-11058 | 7.5 | 2026-06-04 | Integer overflow in CredentialProvider in Google Chrome on Windows prior to 149.0.7827.53 allowed a remote attacker who  |
| CVE-2026-11059 | 8.8 | 2026-06-04 | Use after free in Blink in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-11060 | 8.8 | 2026-06-04 | Use after free in Media in Google Chrome on Windows prior to 149.0.7827.53 allowed a remote attacker to execute arbitrar |
| CVE-2026-11068 | 8.8 | 2026-06-04 | Use after free in WebSockets in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code |
| CVE-2026-11074 | 8.8 | 2026-06-04 | Use after free in WebRTC in Google Chrome on Linux prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary |
| CVE-2026-11076 | 8.8 | 2026-06-04 | Type Confusion in CSS in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-11077 | 8.8 | 2026-06-04 | Bad cast in Dawn in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code inside a sa |
| CVE-2026-11086 | 8.8 | 2026-06-04 | Inappropriate implementation in Dawn in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromis |
| CVE-2026-11117 | 8.8 | 2026-06-04 | Use after free in Views in Google Chrome on Windows prior to 149.0.7827.53 allowed a remote attacker to execute arbitrar |
| CVE-2026-11118 | 8.8 | 2026-06-04 | Use after free in WebRTC in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-11125 | 8.8 | 2026-06-04 | Use after free in Compositing in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary cod |
| CVE-2026-11130 | 8.8 | 2026-06-04 | Use after free in Media in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-11136 | 8.8 | 2026-06-04 | Use after free in Canvas in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-11147 | 8.8 | 2026-06-04 | Use after free in WebML in Google Chrome on Windows prior to 149.0.7827.53 allowed a remote attacker to execute arbitrar |
| CVE-2026-11149 | 7.5 | 2026-06-04 | Insufficient validation of untrusted input in Extensions in Google Chrome prior to 149.0.7827.53 allowed a remote attack |
| CVE-2026-11164 | 8.8 | 2026-06-04 | Use after free in Blink in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-11171 | 8.8 | 2026-06-04 | Integer overflow in Blink in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code in |
| CVE-2026-11173 | 8.8 | 2026-06-04 | Out of bounds write in V8 in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the rend |
| CVE-2026-11230 | 8.8 | 2026-06-04 | Use after free in Extensions in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code |
| CVE-2026-11235 | 8.8 | 2026-06-04 | Insufficient policy enforcement in Compositing in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had |
| CVE-2026-20245 | 7.8 | 2026-06-04 | A vulnerability in the CLI of Cisco Catalyst SD-WAN Manager, formerly SD-WAN vManage, could allow an authenticated, loca |
| CVE-2026-45497 | 7.7 | 2026-06-04 | Improper neutralization of special elements used in a command ('command injection') in Microsoft Copilot allows an autho |
| CVE-2026-48567 | 10.0 | 2026-06-04 | Authentication bypass by spoofing in Azure HorizonDB allows an unauthorized attacker to elevate privileges over a networ |
| CVE-2026-48579 | 9.1 | 2026-06-04 | Improper authorization in Microsoft Exchange Online allows an unauthorized attacker to disclose information over a netwo |
| CVE-2026-10586 | 7.2 | 2026-06-05 | The Gutenberg Essential Blocks – Page Builder for Gutenberg Blocks & Patterns plugin for WordPress is vulnerable to Serv |
| CVE-2026-10877 | 7.3 | 2026-06-05 | A security vulnerability has been detected in SourceCodester Ship Ferry Ticket Reservation System up to 1.0. This impact |
| CVE-2026-11239 | 7.5 | 2026-06-05 | Inappropriate implementation in Extensions in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had com |
| CVE-2026-11241 | 8.0 | 2026-06-05 | Insufficient validation of untrusted input in Cast in Google Chrome prior to 149.0.7827.53 allowed an attacker on the lo |
| CVE-2026-11262 | 8.8 | 2026-06-05 | Use after free in TabStrip in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code v |
| CVE-2026-11279 | 8.8 | 2026-06-05 | Out of bounds read in DevTools in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary co |
| CVE-2026-11296 | 7.5 | 2026-06-05 | Inappropriate implementation in ImageCapture in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had c |
| CVE-2026-11303 | 8.8 | 2026-06-05 | Use after free in PDFium in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-11305 | 8.8 | 2026-06-05 | Use after free in PDFium in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-11306 | 8.8 | 2026-06-05 | Use after free in PDFium in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-11307 | 8.8 | 2026-06-05 | Use after free in PDFium in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-41567 | 7.2 | 2026-06-05 | Moby is an open source container framework. In versions prior to 29.5.1 and in moby/moby v2 prior to v2.0.0-beta.14, whe |
| CVE-2026-50593 | 7.3 | 2026-06-05 | Graphite before 1.3.15 has an integer underflow and resultant out-of-bounds write via Graphite actions, because slotat d |
| CVE-2026-11332 | 7.8 | 2026-06-05 | A flaw was found in ansible-core. The ansible-galaxy role install command processes dependency specifications from a rol |
| CVE-2026-49777 | 10.0 | 2026-06-05 | Improper Validation of Specified Quantity in Input vulnerability in ShapedPlugin, LLC Product Slider Pro for WooCommerce |
| CVE-2026-6274 | 9.8 | 2026-06-05 | Improper Authentication, Missing authentication for critical function, Weak Authentication vulnerability in DTS Electron |
| CVE-2026-50265 | 7.0 | 2026-06-05 | A flaw was found in libinput. A local attacker with access to /dev/uinput can inject arbitrary udev properties through t |

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