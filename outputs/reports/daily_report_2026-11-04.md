# Vulnerability Intelligence Report

**Date:** 2026-11-04  
**Generated:** 2026-11-04T16:32:52Z  

---

## Executive Summary

Our environment faces significant exposure across multiple platforms, with 260 high-severity vulnerabilities identified this period. Most critical are SolarWinds Dameware flaws including a CVSS 9.9 command injection enabling full remote host compromise and a CVSS 9.8 file upload vulnerability in gohttpserver. Seven new CISA Known Exploited Vulnerabilities were added in the past week affecting WordPress, Ivanti Connect Secure, GitLab, and Cisco Firewall products — all confirmed to be actively exploited in the wild. SonicWall GMS exposes internal files to unauthenticated attackers, and Elastic Stack components present denial-of-service and path traversal risks. Immediate remediation of the highest-scored vulnerabilities and KEV-listed products is essential to reduce breach likelihood.

---

## Risk Narrative

The current threat landscape reflects a convergence of unauthenticated remote attack vectors, actively exploited vulnerabilities, and widespread platform exposure. CISA KEV additions signal real-world exploitation targeting Ivanti, Cisco, GitLab, and WordPress — technologies commonly present in enterprise environments. SolarWinds Dameware's critical flaws create a direct path to full system compromise. Unauthenticated vulnerabilities in SonicWall and gohttpserver lower attacker effort significantly. Collectively, these risks threaten data confidentiality, operational continuity, and regulatory compliance. Exploitation of any KEV-listed vulnerability could result in ransomware deployment, data exfiltration, or persistent access — all carrying severe financial and reputational consequences for the organization.

---

## Prioritized Action Items

1. Patch or isolate SolarWinds Dameware immediately to remediate the CVSS 9.9 command injection and CVSS 8.4 remote code execution vulnerabilities.
2. Apply vendor patches for all seven newly added CISA KEV entries — WordPress Core, Ivanti Connect Secure, GitLab, and Cisco ASA/FTD — within 24-72 hours as active exploitation is confirmed.
3. Upgrade SonicWall GMS to a patched version beyond 9.5.2 to prevent unauthenticated internal file disclosure by external attackers.
4. Remediate the CVSS 9.8 Zip Slip vulnerability in gohttpserver by upgrading beyond v1.3.0 or disabling the upload endpoint until patching is complete.
5. Audit and update Elastic Stack components — Elasticsearch, Kibana, and Elastic Beats Docker images — to address denial-of-service, path traversal, and certificate validation weaknesses.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-109593 | 9.1 | 2026-11-03 | An unauthenticated attacker with network access to the SonicWall GMS 9.5.2 and earlier versions may be able to read inte |
| CVE-2026-115290 | 7.5 | 2026-11-03 | Uncontrolled Recursion (CWE-674) in Elasticsearch can lead to denial of service via Serialized Data with Nested Payloads |
| CVE-2026-115294 | 7.3 | 2026-11-03 | Improper Limitation of a Pathname to a Restricted Directory (CWE-22) in the Kibana Fleet feature can lead to unauthorize |
| CVE-2026-115714 | 7.4 | 2026-11-03 | Improper Certificate Validation (CWE-295) in the operating system certificate bundle shipped in the Docker images of APM |
| CVE-2026-119675 | 8.6 | 2026-11-03 | MongoDB Database Tools mongorestore inconsistently handles the system.buckets. prefix when validating collection names i |
| CVE-2026-28327 | 8.2 | 2026-11-03 | SolarWinds Dameware was found to be affected by a DLL hijacking vulnerability. The hijack occurs during installations on |
| CVE-2026-28335 | 8.4 | 2026-11-03 | SolarWinds Dameware was found to be affected by a buffer overflow vulnerability that can result in remote code execution |
| CVE-2026-28336 | 9.9 | 2026-11-03 | SolarWinds Dameware was found to be affected by a command injection vulnerability that could lead to the compromise of t |
| CVE-2026-38600 | 9.8 | 2026-11-03 | A Zip Slip vulnerability in the /upload endpoint of codeskyblue gohttpserver through v1.3.0 allows attackers to write ar |
| CVE-2026-44265 | 7.4 | 2026-11-03 | Elo is a purely functional expression language for no-code tools. Prior to 1.0.1, Elo's programmatic AST API accepts arb |
| CVE-2026-44266 | 9.8 | 2026-11-03 | Elo is a purely functional expression language for no-code tools. Prior to 1.0.1, the Ruby backend in src/compilers/ruby |
| CVE-2026-44267 | 9.8 | 2026-11-03 | Elo is a purely functional expression language for no-code tools. Prior to 1.0.1, plain Elo strings supplied to defaultF |
| CVE-2026-63418 | 7.0 | 2026-11-03 | Monitoring Plugins is a suite of plugins for monitoring applications. From 3.0.0-rc1 until 3.0.1, check_icmp stores the  |
| CVE-2026-119922 | 8.8 | 2026-11-03 | Improper access control in the Babelfish for PostgreSQL extension versions 1.2-1.5, 2.1-2.15, 3.1-3.12, 4.0-4.8, 5.1-5.4 |
| CVE-2026-120678 | 7.5 | 2026-11-03 | A memory management flaw in the MongoDB C Driver's handling of compressed responses may cause the client library to hold |
| CVE-2026-120955 | 7.5 | 2026-11-03 | The GridFS file download API in the MongoDB C Driver does not check the result of an internal operation under certain er |
| CVE-2026-120956 | 7.1 | 2026-11-03 | The MongoDB C Driver does not validate the type or format of a namespace field returned by the server in a query respons |
| CVE-2026-121382 | 7.5 | 2026-11-03 | A vulnerability was determined in Netcore NBR100V2 1.3.240614.030928. Affected by this issue is the function msg_aes_dec |
| CVE-2026-39379 | 7.1 | 2026-11-03 | GeoNetwork is a catalog application to manage spatially referenced resources. From 3.0.0 until 4.2.15 and 4.4.10, reques |
| CVE-2026-46487 | 7.5 | 2026-11-03 | GeoNetwork is a catalog application to manage spatially referenced resources. From 4.0.0-alpha.1 until 4.2.16 and 4.4.11 |
| CVE-2026-57154 | 8.1 | 2026-11-03 | OPNsense is a FreeBSD based firewall and routing platform. Prior to 26.1.11 and 26.4.1p1, authenticated Web UI or API us |
| CVE-2026-63197 | 7.3 | 2026-11-03 | traQ is a messenger application built for Digital Creators Club traP. Prior to 3.28.3, instances configured with TRAQ_ST |
| CVE-2026-63198 | 7.3 | 2026-11-03 | traQ is a messenger application built for Digital Creators Club traP. Prior to 3.28.3, OAuth2 silent authorization reque |
| CVE-2026-82976 | 7.1 | 2026-11-03 | A flaw was found in the image-customization-controller used in OpenShift's bare metal provisioning stack. The controller |
| CVE-2026-45146 | 7.2 | 2026-11-03 | Chamilo LMS is an open-source learning management system. Prior to 1.11.40 and 2.0.1, an authenticated administrator can |
| CVE-2026-54161 | 8.1 | 2026-11-03 | Network UPS Tools is a collection of programs which provide a common interface for monitoring and administering UPS, PDU |
| CVE-2026-63395 | 8.8 | 2026-11-03 | isomorphic-git is a pure JavaScript implementation of Git for Node.js and browsers. Prior to 1.38.6, isomorphic-git's gi |
| CVE-2026-63482 | 7.5 | 2026-11-03 | Yeti bridges the gap between CTI and DFIR practitioners by providing a Forensics Intelligence platform and pipeline. Pri |
| CVE-2026-63489 | 7.6 | 2026-11-03 | Yeti bridges the gap between CTI and DFIR practitioners by providing a Forensics Intelligence platform and pipeline. In  |
| CVE-2026-63500 | 7.1 | 2026-11-03 | Yeti bridges the gap between CTI and DFIR practitioners by providing a Forensics Intelligence platform and pipeline. Pri |
| CVE-2026-63501 | 7.5 | 2026-11-03 | ag-psd is a JavaScript library for reading and writing Photoshop Document files. Prior to 31.0.3, readPsd() accepts a to |
| CVE-2026-63502 | 8.3 | 2026-11-03 | Yeti bridges the gap between CTI and DFIR practitioners by providing a Forensics Intelligence platform and pipeline. Pri |
| CVE-2026-95722 | 8.8 | 2026-11-03 | A local privilege escalation vulnerability has been discovered in the Virtual Intranet Access (VIA) client. Successful e |
| CVE-2026-95723 | 8.4 | 2026-11-03 | A missing integrity verification vulnerability has been discovered in the Virtual Intranet Access (VIA) client. Successf |
| CVE-2026-95724 | 8.1 | 2026-11-03 | An improper certificate validation vulnerability exists in HPE Networking Virtual Intranet Access (VIA). Successful expl |
| CVE-2026-95725 | 7.8 | 2026-11-03 | A command injection vulnerability exists in the VIA client for Linux. Successful exploitation could allow a low-privileg |
| CVE-2026-95726 | 7.5 | 2026-11-03 | A buffer overflow vulnerability in HPE Networking VIA could allow an unauthenticated remote attacker to conduct a denial |
| CVE-2026-95727 | 7.2 | 2026-11-03 | A command injection vulnerability exists in HPE Networking VIA. Successful exploitation could allow an authenticated adm |
| CVE-2026-95728 | 7.1 | 2026-11-03 | An arbitrary file write vulnerability exists in the Virtual Intranet Access (VIA) client. Successful exploitation could  |
| CVE-2026-95731 | 9.8 | 2026-11-03 | Hardcoded password vulnerabilities in the command-line interface of HPE Networking Fabric Composer could allow an unauth |
| CVE-2026-95732 | 9.6 | 2026-11-03 | An authentication bypass vulnerability exists in the underlying operating system of HPE Networking Fabric Composer. Succ |
| CVE-2026-95733 | 9.6 | 2026-11-03 | A vulnerability exists in a component of HPE Networking Fabric Composer. Successful exploitation could allow an unauthen |
| CVE-2026-95734 | 8.8 | 2026-11-03 | A sensitive information disclosure vulnerability in the API of HPE Networking Fabric Composer could allow an authenticat |
| CVE-2026-95735 | 8.7 | 2026-11-03 | An improper certificate validation vulnerability exists in HPE Networking Fabric Composer. Successful exploitation could |
| CVE-2026-95736 | 8.3 | 2026-11-03 | Improper certificate validation vulnerabilities exist in the affected interface of HPE Networking Fabric Composer, which |
| CVE-2026-95737 | 8.2 | 2026-11-03 | A privilege escalation vulnerability exists in the underlying operating system of HPE Networking Fabric Composer. Succes |
| CVE-2026-95738 | 8.1 | 2026-11-03 | Authentication bypass vulnerabilities in the affected interface of HPE Networking Fabric Composer could allow an unauthe |
| CVE-2026-95739 | 8.1 | 2026-11-03 | An improper restriction of excessive authentication attempts vulnerability in the API of HPE Networking Fabric Composer  |
| CVE-2026-95740 | 8.0 | 2026-11-03 | An improper certificate validation vulnerability in HPE Networking Fabric Composer could allow an unauthenticated adjace |
| CVE-2026-95741 | 8.0 | 2026-11-03 | A missing integrity verification vulnerability exists in the API of HPE Networking Fabric Composer. Successful exploitat |
| CVE-2026-95742 | 7.8 | 2026-11-03 | An arbitrary file write vulnerability exists in the underlying operating system of HPE Networking Fabric Composer. Succe |
| CVE-2026-95743 | 7.8 | 2026-11-03 | Local privilege escalation vulnerabilities exist in the underlying operating system of HPE Networking Fabric Composer. S |
| CVE-2026-95744 | 7.7 | 2026-11-03 | A sensitive information disclosure vulnerability in the affected interface of HPE Networking Fabric Composer could allow |
| CVE-2026-95745 | 7.5 | 2026-11-03 | A vulnerability in the API of HPE Networking Fabric Composer could allow an unauthenticated remote attacker to conduct a |
| CVE-2026-95746 | 7.5 | 2026-11-03 | An authentication bypass vulnerability in the API endpoint of HPE Networking Fabric Composer could allow an unauthentica |
| CVE-2026-95747 | 7.5 | 2026-11-03 | A privilege escalation vulnerability exists in the SSH interface of HPE Networking Fabric Composer which could allow an  |
| CVE-2026-95748 | 7.5 | 2026-11-03 | A SQL injection vulnerability exists in HPE Networking Fabric Composer. Successful exploitation could allow an unauthent |
| CVE-2026-95749 | 7.5 | 2026-11-03 | A missing integrity verification vulnerability exists in HPE Networking Fabric Composer. Successful exploitation could a |
| CVE-2026-95750 | 7.5 | 2026-11-03 | An improper certificate validation vulnerability in HPE Networking Fabric Composer could allow an unauthenticated remote |
| CVE-2026-95751 | 7.4 | 2026-11-03 | An improper certificate validation vulnerability in the API of HPE Networking Fabric Composer could allow an unauthentic |
| CVE-2026-95752 | 7.1 | 2026-11-03 | A local privilege escalation vulnerability exists in the API of HPE Networking Fabric Composer. Successful exploitation  |
| CVE-2026-95753 | 7.1 | 2026-11-03 | A privilege escalation vulnerability exists in the API of HPE Networking Fabric Composer. Successful exploitation could  |
| CVE-2026-115878 | 7.8 | 2026-11-03 | Stanza is a Stanford NLP Python library for tokenization, sentence segmentation, NER, and parsing of many human language |
| CVE-2026-120952 | 7.1 | 2026-11-03 | An out-of-bounds write in the MongoDB Atlas SQL ODBC Driver may be triggered when a value of a particular database type  |
| CVE-2026-121030 | 9.6 | 2026-11-03 | Incorrect authorization in DevTools in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social  |
| CVE-2026-121034 | 9.6 | 2026-11-03 | Use after free in Views in Google Chrome on on Windows prior to 157.0.8103.38 allowed a remote attacker leveraging socia |
| CVE-2026-121035 | 9.6 | 2026-11-03 | Use after free in Prerender in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code  |
| CVE-2026-121036 | 8.8 | 2026-11-03 | Use after free in CSS in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-121037 | 9.6 | 2026-11-03 | Out of bounds write in ANGLE in Google Chrome on on Windows prior to 157.0.8103.38 allowed a remote attacker to potentia |
| CVE-2026-121044 | 8.8 | 2026-11-03 | Use after free in Layout in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-121047 | 8.8 | 2026-11-03 | Buffer overflow in Media in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-121048 | 8.8 | 2026-11-03 | Race condition in V8 in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-121052 | 8.8 | 2026-11-03 | Use after free in GPU in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-121057 | 8.8 | 2026-11-03 | Type confusion in V8 in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-121060 | 9.6 | 2026-11-03 | Incorrect authorization in FileSystem in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging socia |
| CVE-2026-121061 | 8.8 | 2026-11-03 | Use after free in Modularization in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary  |
| CVE-2026-121068 | 8.8 | 2026-11-03 | Type confusion in V8 in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-121069 | 8.8 | 2026-11-03 | Use after free in Track in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-121070 | 8.8 | 2026-11-03 | Use after free in WTF in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-121071 | 9.6 | 2026-11-03 | Incorrect authorization in FileSystem in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging socia |
| CVE-2026-121074 | 9.6 | 2026-11-03 | Memory corruption in GPU in Google Chrome on on Android prior to 157.0.8103.38 allowed a remote attacker to potentially  |
| CVE-2026-121076 | 9.6 | 2026-11-03 | Use after free in WebXR in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social engineering  |
| CVE-2026-121077 | 9.6 | 2026-11-03 | Use after free in Mobile in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social engineering |
| CVE-2026-121078 | 8.8 | 2026-11-03 | Type confusion in V8 in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrary  |
| CVE-2026-121079 | 8.8 | 2026-11-03 | Race condition in V8 in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-121082 | 8.8 | 2026-11-03 | Type confusion in V8 in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-121083 | 8.8 | 2026-11-03 | Use after free in Compositing in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary cod |
| CVE-2026-121084 | 8.3 | 2026-11-03 | Out of bounds read in Skia in Google Chrome prior to 157.0.8103.38 allowed a remote attacker who had compromised the ren |
| CVE-2026-121086 | 9.6 | 2026-11-03 | Buffer overflow in Skia in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code outs |
| CVE-2026-121089 | 9.6 | 2026-11-03 | Use after free in WebGPU in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitr |
| CVE-2026-121090 | 8.3 | 2026-11-03 | Improper privilege management in Navigation in Google Chrome on on iOS prior to 157.0.8103.38 allowed a remote attacker  |
| CVE-2026-121092 | 8.8 | 2026-11-03 | Uncontrolled recursion in SVG in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute a |
| CVE-2026-121094 | 8.8 | 2026-11-03 | Type confusion in V8 in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-121097 | 8.8 | 2026-11-03 | Use after free in Printing in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code i |
| CVE-2026-121098 | 8.3 | 2026-11-03 | Improper state validation in GPU in Google Chrome prior to 157.0.8103.38 allowed a remote attacker who had compromised t |
| CVE-2026-121100 | 8.8 | 2026-11-03 | Use after free in DOM in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-121104 | 9.6 | 2026-11-03 | Incorrect authorization in FileSystem in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging socia |
| CVE-2026-121112 | 8.3 | 2026-11-03 | Out of bounds read in Permissions in Google Chrome prior to 157.0.8103.38 allowed a remote attacker who had compromised  |
| CVE-2026-121114 | 9.6 | 2026-11-03 | Use after free in TabStrip in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code o |
| CVE-2026-121117 | 8.8 | 2026-11-03 | Use after free in Paint in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-121118 | 8.8 | 2026-11-03 | Use after free in SVG in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-121119 | 8.8 | 2026-11-03 | Use after free in Controls in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code i |
| CVE-2026-121123 | 8.8 | 2026-11-03 | Use after free in Canvas in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-121124 | 8.8 | 2026-11-03 | Improper adherence to coding standards in XML in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to poten |
| CVE-2026-121126 | 9.6 | 2026-11-03 | Use after free in Core in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrar |
| CVE-2026-121127 | 8.8 | 2026-11-03 | Use after free in WebAudio in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code i |
| CVE-2026-121128 | 8.8 | 2026-11-03 | Use after free in Scheduling in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code |
| CVE-2026-121129 | 8.8 | 2026-11-03 | Use after free in WebRTC in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-121131 | 9.6 | 2026-11-03 | Use after free in Mobile in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social engineering |
| CVE-2026-121137 | 8.8 | 2026-11-03 | Type confusion in DevTools in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social engineeri |
| CVE-2026-121140 | 8.3 | 2026-11-03 | Out of bounds read in Internals in Google Chrome prior to 157.0.8103.38 allowed a remote attacker who had compromised th |
| CVE-2026-121148 | 9.6 | 2026-11-03 | Use after free in ANGLE in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code outs |
| CVE-2026-121156 | 9.6 | 2026-11-03 | Buffer overflow in Dawn in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitra |
| CVE-2026-121166 | 8.8 | 2026-11-03 | Type confusion in PDFium in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-121168 | 8.8 | 2026-11-03 | Improper resource exposure in DevTools in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging soci |
| CVE-2026-121178 | 8.3 | 2026-11-03 | Use after free in Aura in Google Chrome prior to 157.0.8103.38 allowed a remote attacker who had compromised the rendere |
| CVE-2026-121179 | 8.8 | 2026-11-03 | Use after free in PDFium in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-121180 | 8.8 | 2026-11-03 | Buffer overflow in Media in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-121181 | 8.8 | 2026-11-03 | Use after free in Editing in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code in |
| CVE-2026-121182 | 8.8 | 2026-11-03 | Use after free in DOM in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-121183 | 8.3 | 2026-11-03 | Incorrect authorization in Extensions in Google Chrome prior to 157.0.8103.38 allowed a remote attacker who had compromi |
| CVE-2026-121184 | 8.8 | 2026-11-03 | Out of bounds read in Media in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute arb |
| CVE-2026-121185 | 9.6 | 2026-11-03 | Use after free in PictureInPicture in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social e |
| CVE-2026-121188 | 8.8 | 2026-11-03 | Use after free in PerformanceAPIs in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary |
| CVE-2026-121189 | 9.6 | 2026-11-03 | Use after free in Browser in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code ou |
| CVE-2026-121200 | 9.6 | 2026-11-03 | Incorrect reference resolution in DevTools in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging  |
| CVE-2026-121201 | 8.8 | 2026-11-03 | Use after free in Animation in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code  |
| CVE-2026-121202 | 9.6 | 2026-11-03 | Use after free in Autofill in Google Chrome prior to 157.0.8103.38 allowed a remote attacker leveraging social engineeri |
| CVE-2026-121203 | 8.8 | 2026-11-03 | Use after free in Geometry in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code i |
| CVE-2026-121208 | 8.8 | 2026-11-03 | Out of bounds read in Media in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute arb |
| CVE-2026-121210 | 8.8 | 2026-11-03 | Type confusion in V8 in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-121214 | 9.6 | 2026-11-03 | Use after free in Passwords in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute arb |
| CVE-2026-121218 | 8.8 | 2026-11-03 | Type confusion in V8 in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-121219 | 8.3 | 2026-11-03 | Integer overflow in GPU in Google Chrome prior to 157.0.8103.38 allowed a remote attacker who had compromised the render |
| CVE-2026-121221 | 8.8 | 2026-11-03 | Type confusion in V8 in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrary  |
| CVE-2026-121226 | 8.8 | 2026-11-03 | Type confusion in V8 in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitrary  |
| CVE-2026-121228 | 8.8 | 2026-11-03 | Type confusion in V8 in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-121229 | 9.6 | 2026-11-03 | Memory corruption in ANGLE in Google Chrome on on Android prior to 157.0.8103.38 allowed a remote attacker to potentiall |
| CVE-2026-121230 | 8.3 | 2026-11-03 | Race condition in ANGLE in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to potentially execute arbitra |
| CVE-2026-121233 | 8.8 | 2026-11-03 | Type confusion in CacheStorage in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary co |
| CVE-2026-121234 | 9.6 | 2026-11-03 | Privilege elevation in Contacts in Google Chrome on on Android prior to 157.0.8103.38 allowed a remote attacker to poten |
| CVE-2026-121238 | 8.8 | 2026-11-03 | Use after free in Source in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-121241 | 9.6 | 2026-11-03 | Use after free in Navigation in Google Chrome on on Android prior to 157.0.8103.38 allowed a remote attacker to potentia |
| CVE-2026-121246 | 9.6 | 2026-11-03 | Use after free in WebGL in Google Chrome on on Android prior to 157.0.8103.38 allowed a remote attacker to potentially e |
| CVE-2026-121247 | 9.6 | 2026-11-03 | Buffer overflow in Dawn in Google Chrome on on Android prior to 157.0.8103.38 allowed a remote attacker to potentially e |
| CVE-2026-121249 | 9.6 | 2026-11-03 | Buffer overflow in ANGLE in Google Chrome prior to 157.0.8103.38 allowed a remote attacker to execute arbitrary code out |
| CVE-2026-121256 | 8.3 | 2026-11-03 | Use of released resource in GPU in Google Chrome prior to 157.0.8103.38 allowed a remote attacker who had compromised th |
| CVE-2026-121502 | 7.3 | 2026-11-03 | A vulnerability was identified in mathurvishal CloudClassroom-PHP-Project. The impacted element is an unknown function o |
| CVE-2026-121621 | 8.8 | 2026-11-03 | A command injection vulnerability was found in Argo CD Image Updater, where a proxy URL configured on an SSH Git reposit |
| CVE-2026-82155 | 7.8 | 2026-11-03 | Dell OS Recovery tool versions, prior to 2.4.4, contain a use of Untrusted Search Path vulnerability. An unauthenticated |
| CVE-2026-82158 | 9.0 | 2026-11-03 | Dell Wyse Management Suite, versions prior to 2609.0.0.155, contain an Improper Neutralization of Input During Web Page  |
| CVE-2026-82159 | 8.8 | 2026-11-03 | Dell Wyse Management Suite, versions prior to 2609.0.0.155, contain an Improper Neutralization of Input During Web Page  |
| CVE-2026-95860 | 9.1 | 2026-11-03 | node-opcua is an OPC UA implementation for TypeScript and Node.js. From 2.42.0 until 2.180.0, namespace-level access con |
| CVE-2026-112354 | 9.8 | 2026-11-03 | Etrel INCH AC charging station management web interface prior to firmware versions 7.1.2 and 8.0.1 contains a hard-coded |
| CVE-2026-119084 | 8.1 | 2026-11-03 | Unsafe reflection in the connection parameter and credentials profile handling of Amazon Redshift JDBC Driver before 2.3 |
| CVE-2026-120931 | 9.6 | 2026-11-03 | Out of bounds write in WebGL in Google Chrome on on Android prior to 156.0.8078.47 allowed a remote attacker to execute  |
| CVE-2026-121524 | 7.3 | 2026-11-03 | A flaw has been found in sumiie24 School-Management-System up to d946d649c7c95e101fc5679ecd91999533bb10d7. Affected by t |
| CVE-2022-29966 | 9.8 | 2026-11-03 | Emerson Ovation has several protocols that have no authentication, which could allow an attacker to change controller co |
| CVE-2022-30267 | 7.5 | 2026-11-03 | Emerson Ovation 
was found to have no authentication of firmware signing and relies on an insecure checksum for integrit |
| CVE-2026-116650 | 7.5 | 2026-11-03 | Tanium addressed an unauthorized code execution vulnerability in Threat Response. |
| CVE-2026-116651 | 7.5 | 2026-11-03 | Tanium addressed an unauthorized code execution vulnerability in Threat Response. |
| CVE-2026-120775 | 7.2 | 2026-11-03 | Tanium addressed a heap-based buffer overflow vulnerability in Deploy. |
| CVE-2026-121565 | 7.4 | 2026-11-03 | Tanium addressed an improper certificate validation vulnerability in multiple products. Products have been updated to di |
| CVE-2026-121727 | 7.5 | 2026-11-03 | Kore before 4.3.0 contains an integer underflow vulnerability in HTTP request body handling that allows unauthenticated  |
| CVE-2026-121729 | 8.3 | 2026-11-03 | emailflare before commit cf31f33 contains a missing authorization vulnerability in the inbox service /api/keys routes th |
| CVE-2026-121731 | 8.8 | 2026-11-03 | RosarioSIS before 12.9 contains a sql injection vulnerability that allows authenticated non-student users, including par |
| CVE-2026-114549 | 9.8 | 2026-11-04 | NoMachine nxwebrunner Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote a |
| CVE-2026-114550 | 8.1 | 2026-11-04 | libwebsockets MQTT Protocol PUBACK Packet Handling Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnera |
| CVE-2026-118623 | 7.8 | 2026-11-04 | MLflow PickleEvaluationArtifact Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerabilit |
| CVE-2026-118627 | 7.8 | 2026-11-04 | MLflow SHAP load_explainer Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerability all |
| CVE-2026-118628 | 8.2 | 2026-11-04 | MLflow get-artifacts Server-Side Request Forgery Information Disclosure Vulnerability. This vulnerability allows remote  |
| CVE-2026-121597 | 9.9 | 2026-11-04 | A weakness has been identified in TOTOLINK A950RG 4.1.2cu.5268_B20221104. This affects the function setAppEasyWizardConf |
| CVE-2026-92185 | 7.2 | 2026-11-04 | Quest Foglight for Databases AbstractParser XML External Entity Processing Information Disclosure Vulnerability. This vu |
| CVE-2026-92186 | 8.8 | 2026-11-04 | Quest Foglight for Databases paFnUploadFileAndCreateInfo Directory Traversal Remote Code Execution Vulnerability. This v |
| CVE-2026-92187 | 8.8 | 2026-11-04 | Quest Foglight for Databases extractAndCreateUploadInfoList Directory Traversal Remote Code Execution Vulnerability. Thi |
| CVE-2026-92188 | 9.8 | 2026-11-04 | Quest Foglight for Databases ForgeMBeanServerSupport Missing Authentication Remote Code Execution Vulnerability. This vu |
| CVE-2026-92189 | 9.8 | 2026-11-04 | Quest Foglight for Databases writeTopologySectionToFile External Control of File Path Remote Code Execution Vulnerabilit |
| CVE-2026-92190 | 9.8 | 2026-11-04 | Quest Foglight for Databases baseRmiServiceExporter Deserialization of Untrusted Data Remote Code Execution Vulnerabilit |
| CVE-2026-92191 | 8.8 | 2026-11-04 | Quest Foglight for Databases runScript Incorrect Authorization Remote Code Execution Vulnerability. This vulnerability a |
| CVE-2026-92192 | 8.8 | 2026-11-04 | Quest Foglight for Databases installLicense Directory Traversal Remote Code Execution Vulnerability. This vulnerability  |
| CVE-2026-92194 | 8.8 | 2026-11-04 | Quest Foglight for Databases loadManageServerLicense Directory Traversal Remote Code Execution Vulnerability. This vulne |
| CVE-2026-92195 | 8.8 | 2026-11-04 | Quest Foglight for Databases loadEvolveLicense Directory Traversal Remote Code Execution Vulnerability. This vulnerabili |
| CVE-2026-92196 | 7.2 | 2026-11-04 | Quest Foglight for Databases renderTemplateString Server-Side Template Injection Remote Code Execution Vulnerability. Th |
| CVE-2026-92197 | 8.8 | 2026-11-04 | Quest Foglight for Databases unzipFile Directory Traversal Remote Code Execution Vulnerability. This vulnerability allow |
| CVE-2026-92198 | 8.2 | 2026-11-04 | Quest Foglight for Databases getSource XML External Entity Processing Information Disclosure Vulnerability. This vulnera |
| CVE-2026-92199 | 7.8 | 2026-11-04 | Quest Foglight for Databases EncryptionUtil Hardcoded Encyption Key Local Privilege Escalation Vulnerability. This vulne |
| CVE-2026-92200 | 7.8 | 2026-11-04 | Quest Foglight for Databases Incorrect Permission Assignment Local Privilege Escalation Vulnerability. This vulnerabilit |
| CVE-2026-92211 | 7.8 | 2026-11-04 | Pixar Animation Studio OpenUSD Crate File Parsing Double Free Remote Code Execution Vulnerability. This vulnerability al |
| CVE-2026-121598 | 9.9 | 2026-11-04 | A security vulnerability has been detected in TOTOLINK A950RG 4.1.2cu.5268_B20221104. This impacts the function strcpy o |
| CVE-2026-121599 | 9.9 | 2026-11-04 | A vulnerability was detected in TOTOLINK A950RG 4.1.2cu.5268_B20221104. Affected is the function setWiFiMultipleConfig/d |
| CVE-2026-121600 | 9.9 | 2026-11-04 | A flaw has been found in TOTOLINK A950RG 4.1.2cu.5268_B20221104. Affected by this vulnerability is the function setMacFi |
| CVE-2026-121606 | 10.0 | 2026-11-04 | A vulnerability has been found in Qihoo 360 D621-2, D603-2, D600-2, D619, D606-6 and D706 up to 6.4.9. Affected by this  |
| CVE-2026-121607 | 10.0 | 2026-11-04 | A vulnerability was found in Qihoo 360 D603-2, D600-2, D606-6 and D706 up to 6.4.9. This affects the function testspeed_ |
| CVE-2026-121608 | 7.3 | 2026-11-04 | A vulnerability was determined in Qihoo 360 D603-2, D600-2 and D606-6 up to 6.3.2. This vulnerability affects the functi |
| CVE-2026-121609 | 10.0 | 2026-11-04 | A vulnerability was identified in Qihoo 360 Whole Home Router M5 4.0.17.1566. This issue affects the function Home of th |
| CVE-2026-121610 | 7.3 | 2026-11-04 | A security flaw has been discovered in funadmin 7.1.0. Impacted is the function Curd::selectList of the file /frontend/a |
| CVE-2026-121615 | 10.0 | 2026-11-04 | A vulnerability was determined in Linksys E5600 1.1.0.26. Affected is an unknown function of the file /cgi-bin/mesh_logi |
| CVE-2026-121617 | 7.5 | 2026-11-04 | A security flaw has been discovered in Linksys E5600 1.1.0.26. Affected by this issue is the function init_multipart of  |
| CVE-2026-121802 | 9.1 | 2026-11-04 | @better-auth/expo before 1.7.16 allows certain account-takeover outcomes (e.g., unauthenticated changes of any account's |
| CVE-2026-79405 | 7.5 | 2026-11-04 | In Modem Firmware, there is a possible system crash due to improper input validation of dedicated PUCCH configuration. T |
| CVE-2026-80335 | 7.6 | 2026-11-04 | In the bootloader download module, there is a possible out-of-bounds write due to a failure to reset a global offset var |
| CVE-2025-11229 | 7.2 | 2026-11-04 | The system fails to properly enforce scope authorization when the `authorize_all_scopes` configuration is enabled. This  |
| CVE-2026-105413 | 7.5 | 2026-11-04 | The Form Maker by 10Web  WordPress plugin before 1.15.51 does not consistently escape user-submitted field values before |
| CVE-2026-108041 | 7.1 | 2026-11-04 | The SEOPress  WordPress plugin before 10.4 does not sanitise and escape some of its analytics tracking settings before o |
| CVE-2026-118422 | 7.1 | 2026-11-04 | The Stape Conversion Tracking WordPress plugin before 2.3.11 does not validate the sub-path appended to its same-origin  |
| CVE-2026-16511 | 8.8 | 2026-11-04 | Two RTIO syscall verifiers, in subsys/rtio/rtio_syscalls.c (subsys/rtio/rtio_handlers.c before v4.3.0), did not validate |
| CVE-2026-77690 | 8.8 | 2026-11-04 | ZohoCorp ManageEngine Key Manager Plus versions before 7151 were vulnerable to a Command Injection vulnerability that al |
| CVE-2026-77779 | 7.7 | 2026-11-04 | ManageEngine Key Manager Plus versions before 7151 were vulnerable to an Improper Access Control vulnerability that allo |
| CVE-2026-87038 | 7.0 | 2026-11-04 | The user-mode verification handler for the i3c_transfer() system call, z_vrfy_i3c_transfer() in drivers/i3c/i3c_handlers |
| CVE-2026-87039 | 7.8 | 2026-11-04 | The user-mode syscall verifier z_vrfy_i2s_configure() in drivers/i2s/i2s_handlers.c copies the caller's struct i2s_confi |
| CVE-2026-87040 | 8.3 | 2026-11-04 | The nRF link-layer receive paths of the open-source Bluetooth LE Controller did not validate the on-air LENGTH field of  |
| CVE-2026-87041 | 7.8 | 2026-11-04 | The RTIO submission-queue verifier rtio_vrfy_sqe() in subsys/rtio/rtio_syscalls.c (subsys/rtio/rtio_handlers.c before v4 |
| CVE-2026-121816 | 8.8 | 2026-11-04 | Herowatch Mini developed by About Time Technologies has a Missing Authentication vulnerability. Unauthenticated remote a |
| CVE-2026-121817 | 7.5 | 2026-11-04 | Herowatch Go Server developed by About Time Technologies has a Insecure Direct Object Reference vulnerability. Authentic |
| CVE-2026-121818 | 7.8 | 2026-11-04 | Herowatch Mini developed by About Time Technologies has a system signing vulnerability. Authenticated local attackers ca |
| CVE-2026-54851 | 7.1 | 2026-11-04 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Awesomemotive Cont |
| CVE-2026-62000 | 7.5 | 2026-11-04 | Missing Authorization vulnerability in WC Lovers WCFM Marketplace wc-multivendor-marketplace allows Exploiting Incorrect |
| CVE-2026-119366 | 7.1 | 2026-11-04 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in AdvancedCoding wpD |
| CVE-2026-119477 | 7.1 | 2026-11-04 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Jacob N. Breetvelt |
| CVE-2026-54861 | 7.1 | 2026-11-04 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Aguila Technologie |
| CVE-2026-56065 | 7.5 | 2026-11-04 | Insertion of Sensitive Information into Externally-Accessible File or Directory vulnerability in Doofinder Doofinder for |
| CVE-2026-57639 | 7.1 | 2026-11-04 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Roland Murg WP Boo |
| CVE-2026-57666 | 7.1 | 2026-11-04 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Aguila Technologie |
| CVE-2026-62007 | 7.1 | 2026-11-04 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Unlimited Elements |
| CVE-2026-62126 | 7.5 | 2026-11-04 | Allocation of Resources Without Limits or Throttling vulnerability in miniOrange SAML SP Single Sign On miniorange-saml- |
| CVE-2026-110022 | 8.4 | 2026-11-04 | The PFI plugin framework deploys executable assemblies (DLLs) from a signed plugin package into the local plugin reposit |
| CVE-2026-110935 | 8.4 | 2026-11-04 | The PFI plugin framework deployment routine does not validate path components when extracting archive entries to the loc |
| CVE-2026-115498 | 7.2 | 2026-11-04 | The Slim Jetpack plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'g<PAGE_ID>-website (Website  |
| CVE-2026-120554 | 8.8 | 2026-11-04 | The Import and export users and customers plugin for WordPress is vulnerable to Privilege Escalation in all versions up  |
| CVE-2026-59264 | 7.8 | 2026-11-04 | The Windows installers of Apache OpenOffice 4.1.16 and earlier allow an already manipulated system to run external code  |
| CVE-2026-59268 | 7.3 | 2026-11-04 | An out-of-bounds Write vulnerability in Apache OpenOffice versions through 4.1.16 could allow an attacker to craft a Mic |
| CVE-2026-90624 | 7.3 | 2026-11-04 | An unchecked memory access in the PDF import code of Apache OpenOffice versions through 4.1.16 on allows a crafted PDF t |
| CVE-2026-90626 | 7.3 | 2026-11-04 | An uncontrolled memory access in the PDF import code of Apache OpenOffice versions through 4.1.16 allows a crafted PDF t |
| CVE-2026-90628 | 7.3 | 2026-11-04 | An uncontrolled memory access in the PDF export code of Apache OpenOffice versions through 4.1.16 allows a crafted CFF f |
| CVE-2026-90629 | 7.3 | 2026-11-04 | An uncontrolled memory access in the WMF import code of Apache OpenOffice versions through 4.1.16 allows a crafted WMF f |
| CVE-2026-90634 | 7.3 | 2026-11-04 | An uncontrolled memory access in the PDF import code of Apache OpenOffice versions through 4.1.16 allows a crafted PDF t |
| CVE-2026-104799 | 8.8 | 2026-11-04 | The Mobile builder plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 1.4. |
| CVE-2026-59267 | 7.8 | 2026-11-04 | A crafted DXF document causes a heap buffer overflow in Draw in Apache OpenOffice 4.1.16 and earlier. This could cause a |
| CVE-2026-97397 | 7.2 | 2026-11-04 | The Remove Google Fonts – Disable, Block, or Replace with Bunny Fonts for GDPR Compliance plugin for WordPress is vulner |
| CVE-2026-119468 | 7.1 | 2026-11-04 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Noptin Newsletter  |
| CVE-2026-119481 | 9.8 | 2026-11-04 | Incorrect Privilege Assignment vulnerability in Crocoblock JetFormBuilder jetformbuilder allows Privilege Escalation.Thi |
| CVE-2026-121939 | 8.1 | 2026-11-04 | Databasement before 1.10.9 contains an authentication bypass vulnerability in OAuthService::findOrCreateLocalUser() that |
| CVE-2026-121940 | 8.8 | 2026-11-04 | Stonewuu ai-fusion-video before 1.3.0 contains an insecure direct object reference vulnerability that allows authenticat |
| CVE-2026-121941 | 7.8 | 2026-11-04 | libmt32emu before 2.8.4 contains a heap buffer overflow vulnerability in MidiStreamParserImpl::parseSysex that allows at |
| CVE-2026-121945 | 7.6 | 2026-11-04 | CoopCycle coopcycle-web before 6.20.1 contains a broken access control vulnerability that allows any courier to read and |
| CVE-2026-121946 | 7.2 | 2026-11-04 | zbateson mail-mime-parser before 3.0.9 and 4.x before 4.0.6 contains a CRLF header injection vulnerability in message-bu |
| CVE-2026-65555 | 9.8 | 2026-11-04 | Incorrect Privilege Assignment vulnerability in Uncanny Owl Uncanny Toolkit for LearnDash uncanny-learndash-toolkit allo |
| CVE-2026-122006 | 9.8 | 2026-11-04 | The activestorage gem before 8.1.4.1 for Ruby on Rails, when ImageMagick attachment processing occurs, can allow server  |
| CVE-2026-121951 | 7.5 | 2026-11-04 | FreeRDP 3.0.0 before 3.32.2 server-side RDP peer input parsing skips the six-byte body of a slow-path input event with a |
| CVE-2026-121952 | 9.8 | 2026-11-04 | FreeRDP before 3.32.2 has an out-of-bounds write in the proxy because rdp_read_bitmap_cache_v2_capability_set rejects on |
| CVE-2026-121953 | 9.8 | 2026-11-04 | FreeRDP before 3.32.2 has a use-after-free in the client's rdpgfx dynamic virtual channel: a duplicate-name channel with |
| CVE-2026-121955 | 7.5 | 2026-11-04 | FreeRDP before 3.32.2 contains a use-after-free vulnerability in Emulate_SCardReleaseContext that frees the emulated SCa |
| CVE-2026-121956 | 7.5 | 2026-11-04 | FreeRDP before 3.32.2 contains a double free in the WinPR Kerberos SSPI retrieveSomeTgt function, which installs the krb |
| CVE-2026-121957 | 7.5 | 2026-11-04 | FreeRDP before 3.32.2 contains a use-after-free vulnerability that allows malicious RDP servers to corrupt client memory |
| CVE-2026-121958 | 8.8 | 2026-11-04 | FreeRDP through 3.32.1 has a heap out-of-bounds write in the RDPGFX client because the delete_surface callback truncates |
| CVE-2026-121960 | 7.5 | 2026-11-04 | FreeRDP before 3.32.2 contains a denial of service vulnerability in the NLA-enabled shadow server when a CredSSP TSReque |
| CVE-2026-121962 | 8.1 | 2026-11-04 | FreeRDP before 3.32.2 contains a heap buffer overflow in transport_default_read_pdu when handling partial Early User Aut |
| CVE-2026-121964 | 7.5 | 2026-11-04 | FreeRDP before 3.32.2 contains a heap-based buffer overflow in the RD Gateway RPC client, where rpc_client_recv_fragment |
| CVE-2026-121966 | 8.7 | 2026-11-04 | Traefik 2.x before 2.11.60 and 3.x before 3.7.16 sends ForwardAuth subrequests (and, in 3.7, Ingress NGINX auth-url requ |
| CVE-2026-92704 | 8.3 | 2026-11-04 | SharpEmu is an experimental PlayStation 5 emulator for Windows and Linux. In version 0.0.3-release.3 and earlier, the re |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-119977 | WordPress / WordPress Core | 2026-11-03 | 2026-11-06 | Unknown |
| CVE-2026-118527 | Ivanti / Connect Secure | 2026-10-30 | 2026-11-13 | Unknown |
| CVE-2026-111357 | Ivanti / Connect Secure | 2026-10-30 | 2026-11-02 | Unknown |
| CVE-2026-97229 | GitLab / Community Edition and Enterprise Edition | 2026-10-29 | 2026-11-01 | Unknown |
| CVE-2026-76418 | Cisco / Secure Firewall ASA Software and Cisco Secure FTD Software | 2026-10-29 | 2026-11-01 | Unknown |
| CVE-2026-41709 | Broadcom / VMware ESX | 2026-10-28 | 2026-11-11 | Unknown |
| CVE-2026-46300 | Linux / Kernel | 2026-10-28 | 2026-10-31 | Unknown |

---

*Total entries in CISA KEV catalog: 1767*