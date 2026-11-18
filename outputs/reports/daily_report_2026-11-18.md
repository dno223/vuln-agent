# Vulnerability Intelligence Report

**Date:** 2026-11-18  
**Generated:** 2026-11-18T16:57:10Z  

---

## Executive Summary

Our environment faces significant cybersecurity exposure across 603 high-severity vulnerabilities, including critical flaws in network device firmware, AI/ML frameworks, and authentication systems. Three vulnerabilities have been actively added to CISA's Known Exploited Vulnerabilities catalog within the past week, indicating real-world threat actor activity. The most critical issues include an unauthenticated command injection vulnerability (CVSS 9.8) in device firmware, a broken NFC authentication flaw (CVSS 9.1), and multiple deserialization vulnerabilities in NVIDIA AI tools. Immediate remediation prioritization is essential to reduce breach risk.

---

## Risk Narrative

The threat landscape reflects a convergence of AI platform vulnerabilities, weak cryptographic controls, and actively exploited third-party software. Deserialization flaws in widely used NVIDIA ML tools expose data pipelines and model infrastructure to code execution. Critical firmware issues expose network-connected devices to command injection and credential theft without authentication. The CISA KEV additions signal that threat actors—including ransomware groups and nation-state actors—are actively weaponizing similar vulnerabilities. Business risks include operational disruption, sensitive data exfiltration, and potential regulatory penalties. The absence of monitored CVEs in the KEV catalog is a minor positive, but the volume of high-severity exposures demands urgent, structured response.

---

## Prioritized Action Items

1. Immediately patch or isolate devices affected by CVE-2026-130801 (CVSS 9.8), as the lack of cryptographic validation allows unauthenticated command injection.
2. Apply vendor mitigations for CVE-2026-130802 (CVSS 9.1) to eliminate the static NFC challenge vulnerability that enables replay attacks.
3. Audit and remediate CISA KEV entries for Perforce Puppet Enterprise, UnrealIRCd, and Check Point products, as these are confirmed to be actively exploited in the wild.
4. Restrict and sandbox all NVIDIA Megatron-LM and Model Optimizer workloads to mitigate deserialization vulnerabilities (CVE-2026-65132, CVE-2026-100967, CVE-2026-100968, CVE-2026-67455) until patches are applied.
5. Conduct a full inventory review to identify all systems affected by the remaining 597 high-severity CVEs and establish a risk-ranked remediation schedule within 30 days.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-100967 | 7.8 | 2026-11-17 | NVIDIA Megatron-LM contains a vulnerability where an attacker could cause deserialization of untrusted data. A successfu |
| CVE-2026-100968 | 7.8 | 2026-11-17 | NVIDIA Megatron-LM contains a vulnerability in dataset loading where an attacker could cause deserialization of untruste |
| CVE-2026-129246 | 7.8 | 2026-11-17 | Due to a Debian-specific patch, the directory used to share data between the
LightDM and the users logging in was writab |
| CVE-2026-130801 | 9.8 | 2026-11-17 | The device's command parser does not require asymmetric cryptographic signatures to validate incoming APDU packets. This |
| CVE-2026-130802 | 9.1 | 2026-11-17 | The NFC authentication handshake relies on a fixed, static challenge instead of a unique, random value for every session |
| CVE-2026-130803 | 7.5 | 2026-11-17 | The firmware and flash memory store critical cryptographic secrets, such as global AES keys and network master keys, in  |
| CVE-2026-65132 | 7.8 | 2026-11-17 | NVIDIA Megatron-LM contains a vulnerability in checkpoint loading where an attacker could cause deserialization of untru |
| CVE-2026-67455 | 8.8 | 2026-11-17 | NVIDIA Model Optimizer for Linux and Windows contains a vulnerability where an attacker could cause a deserialization of |
| CVE-2026-104100 | 8.8 | 2026-11-17 | Teable is an AI spreadsheet for business. Prior to release.2026-07-21T11-27-40Z.2320, a registered user can supply path  |
| CVE-2026-110782 | 8.7 | 2026-11-17 | The SimpleSAMLphp SAML2 library is a PHP library for SAML2 related functionality. From 6.2.2 until 6.2.4 and 7.0.0-rc2,  |
| CVE-2026-86061 | 8.8 | 2026-11-17 | Teable is an AI spreadsheet for business. Prior to release.2026-07-17T05-20-38Z.2264, the routes for PluginService::rege |
| CVE-2026-104868 | 7.8 | 2026-11-17 | A maliciously crafted DWG file, when parsed by Autodesk AutoCAD, can trigger an Integer Overflow vulnerability in RLE bi |
| CVE-2026-113781 | 7.1 | 2026-11-17 | ESP-IDF is the Espressif Internet of Things (IoT) Development Framework. Prior to 5.2.8, 5.3.6, 5.5.6, and 6.0.3, the Bl |
| CVE-2026-119793 | 7.5 | 2026-11-17 | libp2p is a JavaScript implementation of the libp2p networking stack. Prior to 17.0.0, the @libp2p/gossipsub default con |
| CVE-2026-130621 | 8.2 | 2026-11-17 | A time-of-check time-of-use (TOCTOU) race condition in the local port selection in AWS efs-utils (amazon-efs-utils) befo |
| CVE-2026-16780 | 7.8 | 2026-11-17 | A maliciously crafted DXF file, when parsed through Autodesk AutoCAD, can force a Heap-Based Buffer Overflow vulnerabili |
| CVE-2026-18826 | 7.8 | 2026-11-17 | A maliciously crafted DXF file, when parsed through Autodesk AutoCAD, can force a Type Confusion vulnerability. A malici |
| CVE-2026-18827 | 7.8 | 2026-11-17 | A maliciously crafted DWG file containing an attacker-controlled Excel Data Link connection string, when processed throu |
| CVE-2026-28273 | 9.9 | 2026-11-17 | ZoneMinder is a free, open source closed-circuit television software application. Prior to 1.38.4, any authenticated use |
| CVE-2026-77942 | 7.8 | 2026-11-17 | A maliciously crafted IES file, when parsed through Autodesk AutoCAD, can force an Out-of-Bounds Write vulnerability. A  |
| CVE-2026-77943 | 7.8 | 2026-11-17 | A maliciously crafted DXF file, when parsed through Autodesk AutoCAD, can force an Out-of-Bounds Write vulnerability. A  |
| CVE-2026-84855 | 7.8 | 2026-11-17 | A maliciously crafted DGN file, when parsed through Autodesk AutoCAD, can force a Heap-Based Buffer Overflow vulnerabili |
| CVE-2026-85646 | 7.8 | 2026-11-17 | A maliciously crafted DWF file, when parsed through Autodesk AutoCAD, can force a Heap-Based Buffer Overflow vulnerabili |
| CVE-2026-85647 | 7.8 | 2026-11-17 | A maliciously crafted DWG file containing a malformed embedded image, when parsed through Autodesk AutoCAD, can force a  |
| CVE-2026-85648 | 7.8 | 2026-11-17 | A maliciously crafted DDS file, when parsed through Autodesk AutoCAD, can force a Heap-Based Buffer Overflow vulnerabili |
| CVE-2026-93299 | 7.8 | 2026-11-17 | A maliciously crafted DWG file, when parsed through Autodesk AutoCAD or processed by the installed DWG thumbnail handler |
| CVE-2026-100397 | 10.0 | 2026-11-17 | Rucio is a scientific data management framework. From 1.14.0 until 35.9.1, 38.6.1, 40.4.2, and 41.1.1, validate_auth_tok |
| CVE-2026-110789 | 7.5 | 2026-11-17 | libp2p is a JavaScript implementation of the libp2p networking stack. Prior to 5.1.22, the @libp2p/crypto code reached b |
| CVE-2026-119192 | 7.5 | 2026-11-17 | Forge, also called node-forge, is a native implementation of Transport Layer Security in JavaScript. Prior to 1.4.1, pub |
| CVE-2026-121716 | 7.0 | 2026-11-17 | fzf is a command-line fuzzy finder. Prior to 0.74.5, bin/fzf-tmux validates separately supplied layout sizes but does no |
| CVE-2026-128073 | 7.5 | 2026-11-17 | gosaml2 is a Pure Go implementation of SAML 2.0. Prior to 0.12.0, ValidateEncodedResponse() calls decryptAssertions() on |
| CVE-2026-130622 | 7.1 | 2026-11-17 | Incorrect authorization in the credential loading logic in AWS Private CA Connector for Kubernetes (aws-privateca-issuer |
| CVE-2026-130623 | 7.1 | 2026-11-17 | Incorrect authorization in the credential handling for namespace-scoped issuers in AWS Private CA Connector for Kubernet |
| CVE-2026-130796 | 8.2 | 2026-11-17 | Flowise 3.1.3 through 3.1.4 contains an information disclosure vulnerability that allows unauthenticated attackers to re |
| CVE-2026-130838 | 7.4 | 2026-11-17 | Radicale 3.3.0 before 3.8.3 contains an authorization bypass vulnerability that allows unauthenticated attackers to inhe |
| CVE-2026-130839 | 7.8 | 2026-11-17 | ModelScope 1.11.0 to before 1.40.1 contains an unsafe reflection vulnerability in the image-to-3D SyncDreamer pipeline t |
| CVE-2026-130840 | 9.8 | 2026-11-17 | BISHENG before 3.0.0 contains an authentication bypass vulnerability that allows unauthenticated remote attackers to imp |
| CVE-2026-130841 | 7.5 | 2026-11-17 | ioBroker.lovelace before 7.0.0 contains a path traversal vulnerability in the onCards() request handler that allows unau |
| CVE-2026-130843 | 8.8 | 2026-11-17 | HyperFrames before 0.9.30 contains a missing Origin and Host validation vulnerability in the unauthenticated Studio API  |
| CVE-2026-130847 | 7.2 | 2026-11-17 | Dolibarr ERP CRM before 24.0.2 contains an improper authorization vulnerability in the Users REST API put() method that  |
| CVE-2026-130848 | 8.8 | 2026-11-17 | Dolibarr ERP CRM through 24.0.3 contains a code injection vulnerability in Website::importWebSite() that allows website  |
| CVE-2026-130849 | 9.8 | 2026-11-17 | BZFlag bzfs before 2.4.32 contains a heap out-of-bounds write vulnerability in NetHandler::tcpReceive() that allows remo |
| CVE-2026-130851 | 7.1 | 2026-11-17 | wishthis through 1.2.3 contains an authorization bypass vulnerability in User::ownsWishlist() that allows authenticated  |
| CVE-2026-130853 | 7.2 | 2026-11-17 | Nexterm through 1.2.2-BETA contains a privilege escalation vulnerability that allows users with permissions.manage to ga |
| CVE-2026-130855 | 8.8 | 2026-11-17 | Bonsai through 6.0 contains an incorrect authorization vulnerability that allows authenticated Editor users to access ad |
| CVE-2026-130856 | 9.8 | 2026-11-17 | 53AIHub before 0.5.5 contains a missing authentication vulnerability that allows remote unauthenticated attackers to rei |
| CVE-2026-130857 | 8.3 | 2026-11-17 | EveryDocs Core before 1.6.1 contains an authorization bypass vulnerability that allows authenticated users to access oth |
| CVE-2026-130860 | 8.2 | 2026-11-17 | Flagr before 1.2.5 contains an authentication bypass vulnerability that allows unauthenticated remote attackers to acces |
| CVE-2026-130861 | 8.8 | 2026-11-17 | UrlHub before 1.20.1 contains a missing authorization vulnerability that allows any authenticated user to create account |
| CVE-2026-130863 | 8.8 | 2026-11-17 | ArtisanCloud PowerX through 1.0.2 contains a missing authorization vulnerability in the IAM role management API that all |
| CVE-2026-130867 | 7.5 | 2026-11-17 | GreaterWMS through 2.1.54 contains an unauthenticated path traversal vulnerability in the css, js, statics and fonts rou |
| CVE-2026-130868 | 7.4 | 2026-11-17 | GreaterWMS through 2.1.54 contains a predictable authentication token vulnerability that allows unauthenticated attacker |
| CVE-2026-130870 | 7.4 | 2026-11-17 | ClearFlask before 2.7.3 contains an improper authorization vulnerability that allows any account holding an invitation I |
| CVE-2026-130874 | 7.5 | 2026-11-17 | Seerr before 3.5.2 contains an uncontrolled resource consumption vulnerability that allows unauthenticated attackers to  |
| CVE-2026-130875 | 7.5 | 2026-11-17 | tac_plus-ng before commit d8493e0 contains a stack-based buffer overflow vulnerability that allows clients holding the T |
| CVE-2026-82138 | 7.4 | 2026-11-17 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3 contain a Download of Code Without Integrity Check vulnerabil |
| CVE-2026-82139 | 7.4 | 2026-11-17 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3, contain an Improper Certificate Validation vulnerability. An |
| CVE-2026-82142 | 7.1 | 2026-11-17 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3, contain a Missing Authorization vulnerability. A low privile |
| CVE-2026-82143 | 7.8 | 2026-11-17 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3 contain an Improper Authorization vulnerability. A low privil |
| CVE-2026-82146 | 7.8 | 2026-11-17 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3, contain an Untrusted Search Path vulnerability. A low privil |
| CVE-2026-82150 | 8.0 | 2026-11-17 | Dell SupportAssist OS Recovery, versions prior to 5.5.16.3, contain an Insufficient Verification of Data Authenticity vu |
| CVE-2026-97698 | 7.5 | 2026-11-17 | Mistune is a Python Markdown parser with renderers and plugins. Prior to 3.3.4, parse_link_href performs an unbounded pa |
| CVE-2026-97699 | 7.5 | 2026-11-17 | Mistune is a Python Markdown parser with renderers and plugins. Prior to 3.3.4, inline image parsing sends nested ![ ope |
| CVE-2026-102529 | 7.5 | 2026-11-17 | HtmlSanitizer is a .NET library for cleaning HTML fragments and documents from constructs that can lead to XSS attacks.  |
| CVE-2026-130907 | 8.3 | 2026-11-17 | Use after free in Autofill in Google Chrome on on Android prior to 158.0.8127.36 allowed a remote attacker leveraging so |
| CVE-2026-130909 | 8.8 | 2026-11-17 | Use after free in Extensions in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code |
| CVE-2026-130910 | 9.6 | 2026-11-17 | Protection mechanism failure in ANGLE in Google Chrome on on Android prior to 158.0.8127.36 allowed a remote attacker to |
| CVE-2026-130915 | 8.8 | 2026-11-17 | Use after free in CSS in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-130917 | 8.3 | 2026-11-17 | Use after free in Browser in Google Chrome prior to 158.0.8127.36 allowed a remote attacker leveraging social engineerin |
| CVE-2026-130918 | 8.3 | 2026-11-17 | Use after free in Views in Google Chrome prior to 158.0.8127.36 allowed a remote attacker leveraging social engineering  |
| CVE-2026-130919 | 8.3 | 2026-11-17 | Race condition in Printing in Google Chrome prior to 158.0.8127.36 allowed a remote attacker who had compromised the ren |
| CVE-2026-130923 | 8.8 | 2026-11-17 | Out of bounds write in V8 in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code in |
| CVE-2026-130930 | 8.3 | 2026-11-17 | Use after free in Ozone in Google Chrome prior to 158.0.8127.36 allowed a remote attacker who had compromised the render |
| CVE-2026-130938 | 8.3 | 2026-11-17 | Use after free in Accessibility in Google Chrome on on Windows prior to 158.0.8127.36 allowed a remote attacker to execu |
| CVE-2026-130943 | 8.8 | 2026-11-17 | Use after free in Chromecast in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code |
| CVE-2026-130944 | 8.3 | 2026-11-17 | Use after free in Omnibox in Google Chrome on on Windows prior to 158.0.8127.36 allowed a remote attacker who had compro |
| CVE-2026-130945 | 8.3 | 2026-11-17 | Use after free in VR in Google Chrome on on Android prior to 158.0.8127.36 allowed a remote attacker to execute arbitrar |
| CVE-2026-130948 | 8.3 | 2026-11-17 | Use after free in Omnibox in Google Chrome prior to 158.0.8127.36 allowed a remote attacker who had compromised the rend |
| CVE-2026-130950 | 8.8 | 2026-11-17 | Type confusion in V8 in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-130951 | 8.8 | 2026-11-17 | Use after free in Plugins in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code in |
| CVE-2026-130956 | 8.3 | 2026-11-17 | Improper input validation in WebAppInstalls in Google Chrome prior to 158.0.8127.36 allowed a remote attacker who had co |
| CVE-2026-130957 | 8.8 | 2026-11-17 | Improper state validation in Performance in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to potentiall |
| CVE-2026-130960 | 8.3 | 2026-11-17 | Use after free in Session in Google Chrome prior to 158.0.8127.36 allowed a remote attacker leveraging social engineerin |
| CVE-2026-130969 | 8.3 | 2026-11-17 | Incorrect authorization in Omnibox in Google Chrome on on Windows prior to 158.0.8127.36 allowed a remote attacker who h |
| CVE-2026-130971 | 9.6 | 2026-11-17 | Out of bounds write in ANGLE in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to potentially execute ar |
| CVE-2026-130974 | 8.3 | 2026-11-17 | Use after free in UserEducation in Google Chrome prior to 158.0.8127.36 allowed a remote attacker who had compromised th |
| CVE-2026-130975 | 8.8 | 2026-11-17 | Use after free in WebAudio in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code i |
| CVE-2026-130976 | 8.8 | 2026-11-17 | Use after free in PDFium in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-130979 | 8.8 | 2026-11-17 | Use after free in Forms in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code insi |
| CVE-2026-130980 | 8.8 | 2026-11-17 | Use after free in Layout in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-130982 | 8.3 | 2026-11-17 | Incorrect authorization in Omnibox in Google Chrome prior to 158.0.8127.36 allowed a remote attacker who had compromised |
| CVE-2026-130987 | 8.3 | 2026-11-17 | Race condition in Downloads in Google Chrome on on Windows prior to 158.0.8127.36 allowed a remote attacker who had comp |
| CVE-2026-130992 | 8.3 | 2026-11-17 | Incorrect authorization in Views in Google Chrome prior to 158.0.8127.36 allowed a remote attacker who had compromised t |
| CVE-2026-130994 | 9.6 | 2026-11-17 | Use after free in WebGL in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to potentially execute arbitra |
| CVE-2026-130996 | 9.6 | 2026-11-17 | Out of bounds write in ANGLE in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to potentially execute ar |
| CVE-2026-130999 | 8.3 | 2026-11-17 | Use after free in Downloads in Google Chrome on on Windows prior to 158.0.8127.36 allowed a remote attacker leveraging s |
| CVE-2026-131000 | 8.3 | 2026-11-17 | Improper input validation in WebAppInstalls in Google Chrome prior to 158.0.8127.36 allowed a remote attacker who had co |
| CVE-2026-131001 | 8.8 | 2026-11-17 | Buffer overflow in Video in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-131004 | 8.3 | 2026-11-17 | Use after free in FedCM in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code outs |
| CVE-2026-131005 | 8.8 | 2026-11-17 | Use after free in DevTools in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code i |
| CVE-2026-131008 | 8.8 | 2026-11-17 | Use after free in GarbageCollection in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitra |
| CVE-2026-131013 | 8.3 | 2026-11-17 | Buffer overflow in Skia in Google Chrome prior to 158.0.8127.36 allowed a remote attacker who had compromised the render |
| CVE-2026-131021 | 8.8 | 2026-11-17 | Use after free in Accessibility in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary c |
| CVE-2026-131022 | 8.8 | 2026-11-17 | Use after free in DOM in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-131025 | 9.6 | 2026-11-17 | Out of bounds read in ANGLE in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to potentially execute arb |
| CVE-2026-131031 | 9.6 | 2026-11-17 | Out of bounds write in GPU in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code o |
| CVE-2026-131039 | 8.3 | 2026-11-17 | Use after free in Mojo in Google Chrome on on Windows prior to 158.0.8127.36 allowed a remote attacker who had compromis |
| CVE-2026-131042 | 8.8 | 2026-11-17 | Use after free in V8 in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code inside  |
| CVE-2026-131044 | 8.3 | 2026-11-17 | Use after free in Payments in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to potentially execute arbi |
| CVE-2026-131050 | 8.3 | 2026-11-17 | Use after free in Mojo in Google Chrome on on Windows prior to 158.0.8127.36 allowed a remote attacker who had compromis |
| CVE-2026-131051 | 8.3 | 2026-11-17 | Incorrect authorization in UI in Google Chrome prior to 158.0.8127.36 allowed a remote attacker who had compromised the  |
| CVE-2026-131054 | 9.6 | 2026-11-17 | Out of bounds write in ANGLE in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code |
| CVE-2026-131056 | 8.3 | 2026-11-17 | Use after free in WebAppInstalls in Google Chrome prior to 158.0.8127.36 allowed a remote attacker leveraging social eng |
| CVE-2026-131057 | 9.6 | 2026-11-17 | Out of bounds read in ANGLE in Google Chrome on on Android prior to 158.0.8127.36 allowed a remote attacker to potential |
| CVE-2026-131059 | 8.8 | 2026-11-17 | Use after free in Autofill in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code i |
| CVE-2026-131060 | 8.8 | 2026-11-17 | Buffer overflow in Media in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-131061 | 9.6 | 2026-11-17 | Buffer overflow in Color in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code out |
| CVE-2026-131063 | 8.3 | 2026-11-17 | Use after free in CameraCapture in Google Chrome on on Windows prior to 158.0.8127.36 allowed a remote attacker leveragi |
| CVE-2026-131065 | 8.8 | 2026-11-17 | Use after free in Autofill in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code i |
| CVE-2026-131074 | 8.3 | 2026-11-17 | Use after free in DeviceBoundSessionCredentials in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to pot |
| CVE-2026-131077 | 9.6 | 2026-11-17 | Out of bounds write in Tint in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to potentially execute arb |
| CVE-2026-131078 | 8.3 | 2026-11-17 | Use after free in Proxy in Google Chrome prior to 158.0.8127.36 allowed a remote attacker who had compromised the render |
| CVE-2026-131079 | 8.8 | 2026-11-17 | Use after free in Bindings in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code i |
| CVE-2026-131082 | 8.8 | 2026-11-17 | Use after free in CSS in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-131084 | 8.8 | 2026-11-17 | Use after free in XML in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code inside |
| CVE-2026-131087 | 8.8 | 2026-11-17 | Type confusion in V8 in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to potentially execute arbitrary  |
| CVE-2026-131088 | 9.6 | 2026-11-17 | Improper input validation in WebAppInstalls in Google Chrome prior to 158.0.8127.36 allowed a remote attacker who had co |
| CVE-2026-131090 | 8.8 | 2026-11-17 | Use after free in Geometry in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code i |
| CVE-2026-131092 | 8.3 | 2026-11-17 | Use after free in Mojo in Google Chrome on on Windows prior to 158.0.8127.36 allowed a remote attacker who had compromis |
| CVE-2026-131093 | 8.3 | 2026-11-17 | Use after free in FedCM in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code outs |
| CVE-2026-131100 | 8.8 | 2026-11-17 | Use after free in Loader in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code ins |
| CVE-2026-131101 | 8.8 | 2026-11-17 | Out of bounds read in Editing in Google Chrome prior to 158.0.8127.36 allowed a remote attacker leveraging social engine |
| CVE-2026-131106 | 8.8 | 2026-11-17 | Buffer overflow in Partition in Google Chrome prior to 158.0.8127.36 allowed a remote attacker to execute arbitrary code |
| CVE-2026-65963 | 7.2 | 2026-11-17 | Pi-hole FTL is the core engine of the Pi-hole network-level advertisement and tracker blocker. From 6.6.2 until 6.7, PAT |
| CVE-2026-69155 | 8.7 | 2026-11-17 | Atomic Server is an open source headless CMS and real-time database. From 0.30.0 until 0.40.3, an authenticated Agent wi |
| CVE-2026-69156 | 8.1 | 2026-11-17 | Atomic Server is an open source headless CMS and real-time database. From 0.30.0 until 0.40.3, the Commit application pa |
| CVE-2026-69157 | 9.8 | 2026-11-17 | Atomic Server is an open source headless CMS and real-time database. From 0.29.0 to 0.40.2, Atomic Server provisions a w |
| CVE-2026-69158 | 8.6 | 2026-11-17 | Atomic Server is an open source headless CMS and real-time database. Prior to 0.40.3, unauthenticated requests to /bookm |
| CVE-2026-71304 | 8.8 | 2026-11-17 | Pi-hole FTL is the core engine of the Pi-hole network-level advertisement and tracker blocker. From 6.0 until 6.7, check |
| CVE-2026-101652 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Mobile Field Service product of Oracle E-Business Suite (component: Internal Operations).  S |
| CVE-2026-101657 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Mobile Field Service product of Oracle E-Business Suite (component: Admin UI).  Supported ve |
| CVE-2026-101659 | 8.2 | 2026-11-17 | Vulnerability in the Oracle Mobile Field Service product of Oracle E-Business Suite (component: Admin UI).  Supported ve |
| CVE-2026-101663 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Mobile Field Service product of Oracle E-Business Suite (component: Admin UI).  Supported ve |
| CVE-2026-101691 | 9.3 | 2026-11-17 | Vulnerability in the Oracle Mobile Field Service product of Oracle E-Business Suite (component: Admin UI).  Supported ve |
| CVE-2026-101693 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Data Quality Management, Enterprise Edition product of Oracle Hyperion (c |
| CVE-2026-101838 | 7.2 | 2026-11-17 | Vulnerability in the Oracle Contracts product of Oracle E-Business Suite (component: Internal Operations).  Supported ve |
| CVE-2026-101839 | 7.2 | 2026-11-17 | Vulnerability in the Oracle Contracts product of Oracle E-Business Suite (component: Internal Operations).  Supported ve |
| CVE-2026-101848 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Data Quality Management, Enterprise Edition product of Oracle Hyperion (c |
| CVE-2026-103931 | 8.7 | 2026-11-17 | Instatic is an open source visual content management system for building static websites. Prior to 0.0.14, isSafeUrl() a |
| CVE-2026-114783 | 8.6 | 2026-11-17 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: BI Platform |
| CVE-2026-114784 | 10.0 | 2026-11-17 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Platform Se |
| CVE-2026-114785 | 9.6 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-114788 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-114792 | 7.8 | 2026-11-17 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Installatio |
| CVE-2026-114793 | 7.8 | 2026-11-17 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Analytics S |
| CVE-2026-114794 | 7.8 | 2026-11-17 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Platform Se |
| CVE-2026-114799 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-114809 | 7.7 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-114813 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Platform Se |
| CVE-2026-114814 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: Analytics A |
| CVE-2026-114815 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: BI Foundati |
| CVE-2026-114817 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Business Intelligence Enterprise Edition product of Oracle Analytics (component: BI Platform |
| CVE-2026-114818 | 7.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-114819 | 9.9 | 2026-11-17 | Vulnerability in the Oracle Text component of Oracle Database Server.  Supported versions that are affected are 19.3-19. |
| CVE-2026-114822 | 9.9 | 2026-11-17 | Vulnerability in the RDBMS component of Oracle Database Server.  Supported versions that are affected are 23.4.0-23.26.4 |
| CVE-2026-114824 | 10.0 | 2026-11-17 | Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Third |
| CVE-2026-114825 | 8.1 | 2026-11-17 | Vulnerability in the Oracle WebCenter Sites product of Oracle Fusion Middleware (component: WebCenter Sites).   The supp |
| CVE-2026-114826 | 9.8 | 2026-11-17 | Vulnerability in the Service Delivery Platform product of Oracle Fusion Middleware (component: Messaging Enabler).   The |
| CVE-2026-114827 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Managed File Transfer product of Oracle Fusion Middleware (component: MFT Runtime Server).   |
| CVE-2026-114828 | 7.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-114829 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Enterprise Manager Base Platform product of Oracle Enterprise Manager (component: Job System |
| CVE-2026-114835 | 10.0 | 2026-11-17 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Admin Console).  Supported ve |
| CVE-2026-114846 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Financial Services Customer Screening product of Oracle Financial Services Applications (com |
| CVE-2026-114847 | 9.1 | 2026-11-17 | Vulnerability in Oracle Autonomous Health Framework (component: Developer triaging platform).  Supported versions that a |
| CVE-2026-114848 | 9.9 | 2026-11-17 | Vulnerability in the Oracle Text component of Oracle Database Server.  Supported versions that are affected are 19.3-19. |
| CVE-2026-114849 | 9.8 | 2026-11-17 | Vulnerability in Oracle APEX (component: General).  Supported versions that are affected are 24.1.22, 24.2.21, 26.1.5 an |
| CVE-2026-114850 | 9.8 | 2026-11-17 | Vulnerability in Oracle APEX (component: General).  Supported versions that are affected are 24.1.22, 24.2.21, 26.1.5 an |
| CVE-2026-114852 | 8.1 | 2026-11-17 | Vulnerability in Oracle REST Data Services (component: Core).  Supported versions that are affected are 24.2.0-26.3.0. E |
| CVE-2026-114856 | 9.6 | 2026-11-17 | Vulnerability in Oracle REST Data Services (component: General).  Supported versions that are affected are 24.2.0-26.3.0 |
| CVE-2026-114857 | 8.8 | 2026-11-17 | Vulnerability in Oracle REST Data Services (component: PL/SQL Gateway).  Supported versions that are affected are 24.2.0 |
| CVE-2026-114859 | 8.8 | 2026-11-17 | Vulnerability in Oracle Application Testing Suite (component: Test Manager for Web Apps).   The supported version that i |
| CVE-2026-114860 | 8.7 | 2026-11-17 | Vulnerability in Oracle Application Testing Suite (component: Test Manager for Web Apps).   The supported version that i |
| CVE-2026-114861 | 7.8 | 2026-11-17 | Vulnerability in Oracle Application Testing Suite (component: OpenScript).   The supported version that is affected is 1 |
| CVE-2026-114862 | 9.1 | 2026-11-17 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Weblogic).  Supported ve |
| CVE-2026-114863 | 9.8 | 2026-11-17 | Vulnerability in the Oracle Universal Work Queue product of Oracle E-Business Suite (component: Media Integration issues |
| CVE-2026-114864 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Sales Online product of Oracle E-Business Suite (component: Internal Operations).  Supported |
| CVE-2026-114865 | 7.6 | 2026-11-17 | Vulnerability in the Oracle Sales Online product of Oracle E-Business Suite (component: Internal Operations).  Supported |
| CVE-2026-114866 | 7.6 | 2026-11-17 | Vulnerability in the Oracle Sales Online product of Oracle E-Business Suite (component: Internal Operations).  Supported |
| CVE-2026-114867 | 7.1 | 2026-11-17 | Vulnerability in the Oracle Sales Online product of Oracle E-Business Suite (component: Internal Operations).  Supported |
| CVE-2026-114869 | 7.3 | 2026-11-17 | Vulnerability in the Applications DBA product of Oracle E-Business Suite (component: AD Utilities).  Supported versions  |
| CVE-2026-114871 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Sales Online product of Oracle E-Business Suite (component: Internal Operations).  Supported |
| CVE-2026-114872 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Sales Online product of Oracle E-Business Suite (component: Internal Operations).  Supported |
| CVE-2026-114873 | 7.1 | 2026-11-17 | Vulnerability in the Oracle iProcurement product of Oracle E-Business Suite (component: Internal operations).  Supported |
| CVE-2026-114874 | 7.7 | 2026-11-17 | Vulnerability in the Oracle iProcurement product of Oracle E-Business Suite (component: Internal operations).  Supported |
| CVE-2026-114876 | 8.6 | 2026-11-17 | Vulnerability in the Oracle iStore product of Oracle E-Business Suite (component: Shopping Cart).  Supported versions th |
| CVE-2026-114877 | 7.4 | 2026-11-17 | Vulnerability in the Oracle iStore product of Oracle E-Business Suite (component: Shopping Cart).  Supported versions th |
| CVE-2026-114878 | 7.1 | 2026-11-17 | Vulnerability in the Oracle iStore product of Oracle E-Business Suite (component: Shopping Cart).  Supported versions th |
| CVE-2026-114880 | 9.8 | 2026-11-17 | Vulnerability in the Document Management and Collaboration product of Oracle E-Business Suite (component: Attachments).  |
| CVE-2026-114881 | 9.1 | 2026-11-17 | Vulnerability in the Document Management and Collaboration product of Oracle E-Business Suite (component: Attachments).  |
| CVE-2026-114882 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Product Workbench product of Oracle E-Business Suite (component: Internal Operations).  Supp |
| CVE-2026-114883 | 7.2 | 2026-11-17 | Vulnerability in the Oracle Teleservice product of Oracle E-Business Suite (component: Service Request Form).  Supported |
| CVE-2026-114884 | 7.2 | 2026-11-17 | Vulnerability in the Oracle Lease and Finance Management product of Oracle E-Business Suite (component: Internal Operati |
| CVE-2026-114885 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Mobile Field Service product of Oracle E-Business Suite (component: Admin UI).  Supported ve |
| CVE-2026-114887 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Mobile Field Service product of Oracle E-Business Suite (component: Internal Operations).  S |
| CVE-2026-114888 | 7.3 | 2026-11-17 | Vulnerability in the Oracle Mobile Field Service product of Oracle E-Business Suite (component: Admin UI).  Supported ve |
| CVE-2026-114894 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Universal Work Queue product of Oracle E-Business Suite (component: Media Integration issues |
| CVE-2026-114896 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Collaborative Planning product of Oracle E-Business Suite (component: Horizontal View).  Sup |
| CVE-2026-114897 | 8.8 | 2026-11-17 | Vulnerability in the Oracle iProcurement product of Oracle E-Business Suite (component: Redirection).  Supported version |
| CVE-2026-114898 | 7.1 | 2026-11-17 | Vulnerability in the Applications DBA product of Oracle E-Business Suite (component: AD Utilities).  Supported versions  |
| CVE-2026-114901 | 7.5 | 2026-11-17 | Vulnerability in the Oracle E-Business Suite Integrated SOA Gateway product of Oracle E-Business Suite (component: SOA P |
| CVE-2026-114902 | 7.2 | 2026-11-17 | Vulnerability in the Oracle Product Hub product of Oracle E-Business Suite (component: Internal Operations).  Supported  |
| CVE-2026-114903 | 7.4 | 2026-11-17 | Vulnerability in the Oracle E-Business Suite Integrated SOA Gateway product of Oracle E-Business Suite (component: Web S |
| CVE-2026-114904 | 8.2 | 2026-11-17 | Vulnerability in the Oracle E-Business Suite Integrated SOA Gateway product of Oracle E-Business Suite (component: SOA P |
| CVE-2026-114906 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Purchasing product of Oracle E-Business Suite (component: Internal Operations).  Supported v |
| CVE-2026-114907 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Purchasing product of Oracle E-Business Suite (component: Internal Operations).  Supported v |
| CVE-2026-114909 | 8.1 | 2026-11-17 | Vulnerability in the Oracle iProcurement product of Oracle E-Business Suite (component: Requisition Management).  Suppor |
| CVE-2026-114911 | 7.5 | 2026-11-17 | Vulnerability in the Oracle iProcurement product of Oracle E-Business Suite (component: Approval List and Workflow).  Su |
| CVE-2026-114912 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Purchasing product of Oracle E-Business Suite (component: Internal Operations).  Supported v |
| CVE-2026-114913 | 7.1 | 2026-11-17 | Vulnerability in the Oracle Purchasing product of Oracle E-Business Suite (component: Internal Operations).  Supported v |
| CVE-2026-114914 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Purchasing product of Oracle E-Business Suite (component: Endeca).  Supported versions that  |
| CVE-2026-114915 | 7.1 | 2026-11-17 | Vulnerability in the Oracle E-Business Suite Secure Enterprise Search product of Oracle E-Business Suite (component: Sea |
| CVE-2026-114916 | 8.7 | 2026-11-17 | Vulnerability in the Oracle Applications Framework product of Oracle E-Business Suite (component: Security).  Supported  |
| CVE-2026-114917 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Applications Framework product of Oracle E-Business Suite (component: Personalization).  Sup |
| CVE-2026-114918 | 8.7 | 2026-11-17 | Vulnerability in the Oracle Concurrent Processing product of Oracle E-Business Suite (component: BI Publisher Integratio |
| CVE-2026-114924 | 9.8 | 2026-11-17 | Vulnerability in the Oracle Application Object Library product of Oracle E-Business Suite (component: Core).  Supported  |
| CVE-2026-114925 | 9.8 | 2026-11-17 | Vulnerability in the Oracle Applications Framework product of Oracle E-Business Suite (component: REST Services).  Suppo |
| CVE-2026-114927 | 7.2 | 2026-11-17 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Report Distribution).  S |
| CVE-2026-114928 | 8.8 | 2026-11-17 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Application Server).  Su |
| CVE-2026-114929 | 7.5 | 2026-11-17 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Application Server).  Su |
| CVE-2026-114930 | 7.5 | 2026-11-17 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Application Server).  Su |
| CVE-2026-114931 | 7.8 | 2026-11-17 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Test Framework).  Suppor |
| CVE-2026-114932 | 8.7 | 2026-11-17 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Test Framework).  Suppor |
| CVE-2026-114933 | 8.2 | 2026-11-17 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Security).  Supported ve |
| CVE-2026-114934 | 9.3 | 2026-11-17 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Integration Broker).  Su |
| CVE-2026-114935 | 7.5 | 2026-11-17 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Integration Broker).  Su |
| CVE-2026-114937 | 8.8 | 2026-11-17 | Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Updates Environment Mgmt |
| CVE-2026-114938 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition product of Oracle Java SE |
| CVE-2026-114939 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition product of Oracle Java SE |
| CVE-2026-114940 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition product of Oracle Java SE |
| CVE-2026-114941 | 7.0 | 2026-11-17 | Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK product of Oracle Java SE (component: Compiler).  Supported  |
| CVE-2026-114942 | 7.0 | 2026-11-17 | Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK product of Oracle Java SE (component: Libraries).  Supported |
| CVE-2026-114949 | 7.2 | 2026-11-17 | Vulnerability in the MySQL Server, MySQL Cluster product of Oracle MySQL (component: Server: Replication).  Supported ve |
| CVE-2026-114950 | 7.2 | 2026-11-17 | Vulnerability in the MySQL Server, MySQL Cluster product of Oracle MySQL (component: Server: Optimizer).  Supported vers |
| CVE-2026-114951 | 7.2 | 2026-11-17 | Vulnerability in the MySQL Server, MySQL Cluster product of Oracle MySQL (component: Server: Logging).  Supported versio |
| CVE-2026-114952 | 9.1 | 2026-11-17 | Vulnerability in the MySQL Server, MySQL Cluster product of Oracle MySQL (component: Client programs).  Supported versio |
| CVE-2026-114955 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-114956 | 9.3 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-114958 | 8.2 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-114976 | 8.1 | 2026-11-17 | Vulnerability in the Siebel CRM Deployment product of Oracle Siebel CRM (component: Cloud Gateway).  Supported versions  |
| CVE-2026-114977 | 7.5 | 2026-11-17 | Vulnerability in the Siebel CRM Deployment product of Oracle Siebel CRM (component: Siebel Management Console).  Support |
| CVE-2026-114978 | 9.9 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-114979 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-114980 | 9.9 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security Related Issues).   The supported |
| CVE-2026-114981 | 7.5 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security Related Issues).   The supported |
| CVE-2026-115035 | 8.8 | 2026-11-17 | Vulnerability in the Siebel CRM Deployment product of Oracle Siebel CRM (component: Siebel Remote).  Supported versions  |
| CVE-2026-115044 | 8.8 | 2026-11-17 | Vulnerability in the Siebel CRM Integration product of Oracle Siebel CRM (component: EAI).  Supported versions that are  |
| CVE-2026-115046 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115047 | 9.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115048 | 9.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Security).  |
| CVE-2026-115049 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115050 | 9.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115051 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115053 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115054 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115057 | 7.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-115058 | 7.6 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Security).  |
| CVE-2026-115059 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115060 | 8.2 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115061 | 7.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-115062 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-115063 | 7.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115064 | 7.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115065 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115066 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115067 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115070 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-115071 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-115072 | 7.2 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115074 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-115076 | 7.7 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-115077 | 7.0 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115078 | 8.2 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-115080 | 9.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115081 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115082 | 8.2 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115086 | 9.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-115087 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-115088 | 8.7 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-115089 | 9.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Application Development Framework). |
| CVE-2026-115092 | 8.2 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Application Development Framework). |
| CVE-2026-115094 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-115101 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-115117 | 7.6 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-115120 | 8.7 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Management product of Oracle Hyperion (component: Security).   The suppor |
| CVE-2026-115124 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-115128 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-115129 | 7.7 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-115130 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Application Development Framework). |
| CVE-2026-115131 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Application Development Framework). |
| CVE-2026-115133 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-115138 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-115139 | 9.3 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115140 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-115141 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Hyperion Planning product of Oracle Hyperion (component: Security).   The supported version  |
| CVE-2026-115142 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115143 | 7.6 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115146 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115150 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115151 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115153 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Security).  |
| CVE-2026-115155 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115157 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115158 | 7.7 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115159 | 7.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115160 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Security).  |
| CVE-2026-115163 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Security).  |
| CVE-2026-115164 | 8.7 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115166 | 8.2 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115170 | 7.7 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Security).  |
| CVE-2026-115172 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Security).  |
| CVE-2026-115173 | 8.5 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Security).  |
| CVE-2026-115176 | 7.6 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115177 | 7.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115178 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Installation and C |
| CVE-2026-115179 | 8.4 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Common Security).  |
| CVE-2026-127306 | 8.6 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security Related Issues).   The supported |
| CVE-2026-127307 | 8.8 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127308 | 8.1 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127319 | 7.1 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127324 | 9.8 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127325 | 9.8 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127326 | 9.8 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127327 | 9.8 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127328 | 8.1 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127329 | 8.1 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127330 | 8.1 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127331 | 7.5 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127334 | 8.8 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127335 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-127337 | 7.9 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127339 | 7.1 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127340 | 7.6 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-127349 | 7.7 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-127351 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-127357 | 8.3 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-127360 | 7.4 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-127362 | 9.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-127369 | 9.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-127370 | 8.6 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-127371 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-127372 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-127373 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Hyperion Financial Close Management product of Oracle Hyperion (component: Reconciliation Ma |
| CVE-2026-127392 | 7.7 | 2026-11-17 | Vulnerability in the Product Lifecycle Analytics product of Oracle Supply Chain (component: Installation Issues).   The  |
| CVE-2026-127394 | 7.2 | 2026-11-17 | Vulnerability in the Product Lifecycle Analytics product of Oracle Supply Chain (component: Installation Issues).   The  |
| CVE-2026-127402 | 8.1 | 2026-11-17 | Vulnerability in the Oracle AutoVue product of Oracle Supply Chain (component: Security).   The supported version that i |
| CVE-2026-127413 | 7.5 | 2026-11-17 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-127414 | 7.1 | 2026-11-17 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-127415 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Lifecycle Manageme |
| CVE-2026-127416 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Lifecycle Manageme |
| CVE-2026-127418 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Hyperion Infrastructure Technology product of Oracle Hyperion (component: Lifecycle Manageme |
| CVE-2026-127421 | 8.6 | 2026-11-17 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-127422 | 7.1 | 2026-11-17 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-127423 | 7.1 | 2026-11-17 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-127425 | 8.1 | 2026-11-17 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-127426 | 7.4 | 2026-11-17 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-127427 | 7.5 | 2026-11-17 | Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).   The supported version th |
| CVE-2026-127428 | 7.1 | 2026-11-17 | Vulnerability in the MySQL Server, MySQL Cluster product of Oracle MySQL (component: Server: GIS).  Supported versions t |
| CVE-2026-61675 | 9.8 | 2026-11-17 | WeGIA is a web manager for charitable institutions. Prior to 3.8.7, web/html/socio/sistema/atualiza_pagamentos.php perfo |
| CVE-2026-61676 | 9.8 | 2026-11-17 | WeGIA is a web manager for charitable institutions. Prior to 3.8.7, web/html/socio/sistema/cadastro_cobranca.php creates |
| CVE-2026-61677 | 9.8 | 2026-11-17 | WeGIA is a web manager for charitable institutions. Prior to 3.8.7, web/html/socio/sistema/processa_edicao_socio.php upd |
| CVE-2026-61680 | 9.8 | 2026-11-17 | WeGIA is a web manager for charitable institutions. Prior to 3.8.6, web/html/socio/sistema/cadastro_cobrancas_geracao.ph |
| CVE-2026-61713 | 8.3 | 2026-11-17 | Servo is a lightweight, high-performance web rendering engine for embedding web technologies in applications. Prior to 0 |
| CVE-2026-61715 | 8.8 | 2026-11-17 | Servo is a lightweight, high-performance web rendering engine for embedding web technologies in applications. Prior to 0 |
| CVE-2026-69187 | 8.8 | 2026-11-17 | WeGIA is a web manager for charitable institutions. Prior to 3.9.1, web/controle/control.php authorizes FuncionarioContr |
| CVE-2026-69188 | 7.2 | 2026-11-17 | WeGIA is a web manager for charitable institutions. Prior to 3.9.1, a user with backup-management permission can upload  |
| CVE-2026-83362 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Purchasing product of Oracle E-Business Suite (component: Internal Operations).  Supported v |
| CVE-2026-83365 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Purchasing product of Oracle E-Business Suite (component: Internal Operations).  Supported v |
| CVE-2026-91456 | 9.8 | 2026-11-17 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions t |
| CVE-2026-91469 | 9.4 | 2026-11-17 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions t |
| CVE-2026-91470 | 9.8 | 2026-11-17 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions t |
| CVE-2026-91498 | 7.2 | 2026-11-17 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine).  Supp |
| CVE-2026-91500 | 10.0 | 2026-11-17 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine).  Supp |
| CVE-2026-91507 | 9.3 | 2026-11-17 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine).  Supp |
| CVE-2026-91509 | 8.7 | 2026-11-17 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine).  Supp |
| CVE-2026-91510 | 10.0 | 2026-11-17 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine).  Supp |
| CVE-2026-91516 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine).  Supp |
| CVE-2026-91522 | 8.1 | 2026-11-17 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine).  Supp |
| CVE-2026-91531 | 7.2 | 2026-11-17 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine).  Supp |
| CVE-2026-91533 | 8.2 | 2026-11-17 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine).  Supp |
| CVE-2026-91540 | 7.3 | 2026-11-17 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine).  Supp |
| CVE-2026-91543 | 8.2 | 2026-11-17 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine).  Supp |
| CVE-2026-91548 | 8.6 | 2026-11-17 | Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Third |
| CVE-2026-91551 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Platform Security for Java product of Oracle Fusion Middleware (component: Centralized Third |
| CVE-2026-91556 | 8.8 | 2026-11-17 | Vulnerability in the Service Delivery Platform product of Oracle Fusion Middleware (component: Messaging Enabler).   The |
| CVE-2026-91558 | 8.3 | 2026-11-17 | Vulnerability in the Service Delivery Platform product of Oracle Fusion Middleware (component: Messaging Enabler).  Supp |
| CVE-2026-91561 | 9.6 | 2026-11-17 | Vulnerability in the Oracle Service Bus product of Oracle Fusion Middleware (component: Core).  Supported versions that  |
| CVE-2026-91564 | 7.5 | 2026-11-17 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine).  Supp |
| CVE-2026-91566 | 8.8 | 2026-11-17 | Vulnerability in the Oracle Service Bus product of Oracle Fusion Middleware (component: Core).  Supported versions that  |
| CVE-2026-91569 | 10.0 | 2026-11-17 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: TopLink Integration).  Suppo |
| CVE-2026-91570 | 9.8 | 2026-11-17 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: TopLink Integration).  Suppo |
| CVE-2026-91583 | 9.8 | 2026-11-17 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: TopLink Integration).  Suppo |
| CVE-2026-91585 | 9.8 | 2026-11-17 | Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: TopLink Integration).  Suppo |
| CVE-2026-91586 | 7.4 | 2026-11-17 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Composer).  Supported versi |
| CVE-2026-91587 | 8.6 | 2026-11-17 | Vulnerability in the Oracle WebCenter Portal product of Oracle Fusion Middleware (component: Composer).  Supported versi |
| CVE-2026-91618 | 9.1 | 2026-11-17 | Vulnerability in the Oracle Application Development Framework (ADF) product of Oracle Fusion Middleware (component: Secu |
| CVE-2026-91671 | 8.5 | 2026-11-17 | Vulnerability in the Oracle Access Manager product of Oracle Fusion Middleware (component: Authentication Engine).  Supp |
| CVE-2026-129025 | 8.8 | 2026-11-17 | Cross-Site Request Forgery (CSRF) vulnerability in Brainstorm Force ZIP AI zip-ai allows Cross Site Request Forgery.This |
| CVE-2026-118630 | 8.8 | 2026-11-18 | Winmate HotTab Exposed Dangerous Function Local Privilege Escalation Vulnerability. This vulnerability allows local atta |
| CVE-2026-126962 | 8.8 | 2026-11-18 | open62541 Subscription Use-After-Free Remote Code Execution Vulnerability. This vulnerability allows remote attackers to |
| CVE-2026-126963 | 7.5 | 2026-11-18 | Hinemos Agent Improper Certificate Validation Remote Code Execution Vulnerability. This vulnerability allows network-adj |
| CVE-2026-126966 | 8.8 | 2026-11-18 | SmarterTools SmarterMail Missing Authorization Privilege Escalation Vulnerability. This vulnerability allows remote atta |
| CVE-2026-126967 | 8.8 | 2026-11-18 | SmarterTools SmarterMail File Edit API Directory Traversal Remote Code Execution Vulnerability. This vulnerability allow |
| CVE-2026-126969 | 9.1 | 2026-11-18 | SmarterTools SmarterMail Insufficient Entropy Authentication Bypass Vulnerability. This vulnerability allows remote atta |
| CVE-2026-126970 | 7.8 | 2026-11-18 | KiCad Altium SCHLIB File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability allows remo |
| CVE-2026-126971 | 7.8 | 2026-11-18 | KiCad Project Archive File Handling Directory Traversal Remote Code Execution Vulnerability. This vulnerability allows r |
| CVE-2026-126972 | 7.8 | 2026-11-18 | KiCad Plugin Directory Traversal Remote Code Execution   Vulnerability. This vulnerability allows remote attackers to ex |
| CVE-2026-126973 | 7.8 | 2026-11-18 | KDE Gwenview PNG File Parsing Integer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote att |
| CVE-2026-126974 | 7.8 | 2026-11-18 | llama.cpp GGUF File Parsing Integer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote attac |
| CVE-2026-126975 | 7.8 | 2026-11-18 | llama.cpp GGUF File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows re |
| CVE-2026-126976 | 7.0 | 2026-11-18 | llama.cpp MTMD Multimodal GGUF File Parsing Integer Overflow Remote Code Execution Vulnerability. This vulnerability all |
| CVE-2026-126977 | 8.1 | 2026-11-18 | Philips Hue Bridge HomeKit Pair-Setup Default Password Authentication Bypass Vulnerability. This vulnerability allows ne |
| CVE-2026-126978 | 8.8 | 2026-11-18 | Philips Hue Bridge hap_pair_setup_handler Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerabi |
| CVE-2026-126979 | 8.8 | 2026-11-18 | Philips Hue Bridge HomeKit Accessory Protocol chacha20_decrypt Integer Underflow Remote Code Execution Vulnerability. Th |
| CVE-2026-131848 | 7.4 | 2026-11-18 | Snap7 through 1.4.3 contains an out-of-bounds write vulnerability in TSnap7MicroClient::opReadMultiVars() that allows ma |
| CVE-2026-131849 | 7.4 | 2026-11-18 | Snap7 through 1.4.3 contains a heap-based buffer overflow in TSnap7MicroClient::opReadSZL() that allows malicious PLCs t |
| CVE-2026-131850 | 7.2 | 2026-11-18 | ILIAS 11.0 before 11.6 contains an sql injection vulnerability in RegistrationCodeRepository::getCodesData() that concat |
| CVE-2026-131851 | 8.8 | 2026-11-18 | ILIAS before 9.25, 10.13, and 11.6 contains an SQL injection vulnerability in ilPRGAssignmentFilter::toConditions() that |
| CVE-2026-131852 | 9.8 | 2026-11-18 | OwnTracks Recorder before 1.0.5 contains a format string vulnerability in json_response() and related output functions t |
| CVE-2026-131857 | 7.5 | 2026-11-18 | Supergateway 4.2.0 through 4.2.2 contains a denial of service vulnerability in stdio-to-SSE mode that allows unauthentic |
| CVE-2026-92182 | 8.8 | 2026-11-18 | Netgate pfSense CE XMLRPC Incorrect Authorization Remote Code Execution Vulnerability. This vulnerability allows remote  |
| CVE-2026-105929 | 8.1 | 2026-11-18 | A path traversal vulnerability (CWE-22) was found in ansible-core's ansible-galaxy role installation. An explicit role " |
| CVE-2026-107950 | 8.2 | 2026-11-18 | An XML External Entity (XXE) vulnerability affects a Storefront REST API in HCL Commerce versions 8, 9.0.1 and 9.1.x.  A |
| CVE-2026-131871 | 7.8 | 2026-11-18 | WLA DX 9.7 through 10.7 contains a stack-based buffer overflow vulnerability in parse_data_blocks() in wlalink/analyze.c |
| CVE-2026-131875 | 8.8 | 2026-11-18 | fqterm before 0.9.11 contains a heap out-of-bounds write vulnerability in FQTermDecode that allows malicious servers to  |
| CVE-2026-101113 | 7.2 | 2026-11-18 | Multiple ELECOM wireless LAN routers contain an OS command injection vulnerability that may cause an arbitrary OS comman |
| CVE-2026-130121 | 7.2 | 2026-11-18 | The AI Puffer - MCP Server for Claude & ChatGPT, with AI Chatbot plugin for WordPress is vulnerable to Stored Cross-Site |
| CVE-2026-130644 | 8.1 | 2026-11-18 | A path traversal flaw was found in ansible-core. When installing a collection with ansible-galaxy collection install, th |
| CVE-2026-118900 | 7.8 | 2026-11-18 | An OS command injection vulnerability exists in the Android application "Imperial Palaces Guide" provided by The Imperia |
| CVE-2026-111825 | 7.2 | 2026-11-18 | The Event Tickets with Ticket Scanner plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'code' p |
| CVE-2026-5765 | 8.8 | 2026-11-18 | The Essential Real Estate plugin for WordPress is vulnerable to PHP Object Injection in all versions up to, and includin |
| CVE-2025-15716 | 8.1 | 2026-11-18 | An incorrect implementation of authentication algorithm vulnerability in the SSO API in Synology DiskStation Manager (DS |
| CVE-2025-2235 | 8.8 | 2026-11-18 | Improper Verification of Cryptographic Signature vulnerability in OpenText™ Connected MX allows Privilege Escalation. Th |
| CVE-2026-125820 | 8.8 | 2026-11-18 | Deserialization of Untrusted Data vulnerability in Rymera Web Co Product Feed PRO for WooCommerce woo-product-feed-pro a |
| CVE-2026-125829 | 7.7 | 2026-11-18 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Rymera Web Co Product Fe |
| CVE-2026-131959 | 7.8 | 2026-11-18 | GNU Emacs 31.1 contains a code injection vulnerability in its handling of directory-local variables. A crafted .dir-loca |
| CVE-2026-113497 | 8.8 | 2026-11-18 | A low-privileged remote attacker can change the password of arbitrary users using the REST API, including administrative |
| CVE-2026-95643 | 9.1 | 2026-11-18 | Zohocorp Manageengine DDI Central build below 6500 are affected by a authenticated PowerShell command injection vulnerab |
| CVE-2026-95645 | 9.1 | 2026-11-18 | Zohocorp Manageengine DDI Central build below 6500 are affected by a authenticated command injection vulnerability in th |
| CVE-2026-110486 | 9.8 | 2026-11-18 | In Eclipse Mosquitto versions 2.1 through 2.1.2, a listener configured with `protocol websockets` mishandles empty WebSo |
| CVE-2026-111508 | 9.1 | 2026-11-18 | Dell PowerStore contains an OS Command Injection vulnerability. Exploitation could lead to arbitrary command execution w |
| CVE-2026-116530 | 7.2 | 2026-11-18 | The Check & Log Email – Easy Email Testing & Mail logging plugin for WordPress is vulnerable to Stored Cross-Site Script |
| CVE-2026-116536 | 7.2 | 2026-11-18 | The Custom Twitter Feeds – A Tweets Widget or X Feed Widget plugin for WordPress is vulnerable to Stored Cross-Site Scri |
| CVE-2026-119161 | 7.2 | 2026-11-18 | The HTML Forms – Simple WordPress Forms Plugin plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the |
| CVE-2026-119220 | 7.5 | 2026-11-18 | The Dokan: AI Powered WooCommerce Multivendor Marketplace Solution – Build Your Own Amazon, eBay, Etsy plugin for WordPr |
| CVE-2026-119635 | 7.2 | 2026-11-18 | The Groundhogg plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'post_title' merge-tag of the [ |
| CVE-2026-120686 | 7.2 | 2026-11-18 | The AMP for WP – Accelerated Mobile Pages plugin for WordPress is vulnerable to Stored Cross-Site Scripting in versions  |
| CVE-2026-127921 | 7.5 | 2026-11-18 | The AppPresser – Mobile App Framework plugin for WordPress is vulnerable to generic SQL Injection via the 'appp_cam_file |
| CVE-2026-130648 | 8.7 | 2026-11-18 | WWBN AVideo from 6.5 contains a stored cross-site scripting vulnerability that allows users with upload permission to in |
| CVE-2026-130650 | 9.1 | 2026-11-18 | WWBN AVideo through c3edcc274c389816d434acadac07ee78eaf330c1 contains a cross-site scripting vulnerability because the d |
| CVE-2026-130673 | 7.1 | 2026-11-18 | Craft CMS from 5.0.0 before 5.11.5 contains an sql injection vulnerability that allows authenticated low-privilege users |
| CVE-2026-130674 | 9.8 | 2026-11-18 | Craft CMS from 5.0.0 before 5.11.4 contains an incomplete blocklist fix that allows attackers who can author entry type  |
| CVE-2026-130675 | 9.8 | 2026-11-18 | Craft CMS from 5.0.0 before 5.11.4 contains a remote code execution vulnerability in ImageTransforms::normalizeTransform |
| CVE-2026-130677 | 7.5 | 2026-11-18 | Craft CMS from 5.0.0 before 5.11.4 contains an improper session management vulnerability that fails to invalidate existi |
| CVE-2026-130678 | 9.0 | 2026-11-18 | SiYuan before 3.8.10 contains a stored cross-site scripting vulnerability that allows attackers to execute script by sto |
| CVE-2026-130679 | 9.0 | 2026-11-18 | SiYuan before 3.8.10 contains a stored cross-site scripting vulnerability in genAVValueHTML() that allows attackers who  |
| CVE-2026-130680 | 9.6 | 2026-11-18 | SiYuan from 3.3.0 before 3.8.10 contains a stored cross-site scripting vulnerability that allows attackers to inject HTM |
| CVE-2026-130681 | 9.0 | 2026-11-18 | SiYuan before 3.8.10 contains a stored cross-site scripting vulnerability, an incomplete fix for CVE-2026-44670, because |
| CVE-2026-130682 | 9.6 | 2026-11-18 | SiYuan before 3.8.10 persists a table block's caption attribute into IAL properties without HTML sanitization, causing s |
| CVE-2026-130683 | 8.2 | 2026-11-18 | SiYuan before 3.8.10 uses an incomplete deny-list in IsSensitivePath that omits shell-initialization files such as .zshe |
| CVE-2026-130685 | 7.5 | 2026-11-18 | vLLM from 0.28.0 before 0.33.0 contains an improper input validation vulnerability that allows unauthenticated attackers |
| CVE-2026-130686 | 7.5 | 2026-11-18 | vLLM from 0.6.0 before 0.33.0 lacks a request-wide media budget, allowing remote inference clients to exhaust frontend r |
| CVE-2026-130689 | 8.8 | 2026-11-18 | NocoDB before 2026.10.0 contains an sql injection vulnerability that allows authenticated users with the Creator role to |
| CVE-2026-130690 | 8.8 | 2026-11-18 | NocoDB before 2026.10.1 contains an incorrect authorization vulnerability that allows organization Creators to reach rou |
| CVE-2026-130692 | 8.8 | 2026-11-18 | NocoDB before 2026.10.1 contains a template injection vulnerability that allows authenticated Creator-role users to exec |
| CVE-2026-130697 | 7.1 | 2026-11-18 | NocoDB from 0.301.4 before 2026.10.0 contains an information disclosure vulnerability that allows authenticated workspac |
| CVE-2026-130700 | 8.1 | 2026-11-18 | NocoDB before 2026.10.1 contains a consent phishing vulnerability that allows unauthenticated attackers to register OAut |
| CVE-2026-130701 | 8.3 | 2026-11-18 | NocoDB before 2026.10.1 contains an SQL injection vulnerability because select-field option titles are embedded into MyS |
| CVE-2026-130702 | 8.8 | 2026-11-18 | NocoDB before 2026.10.0 contains an account takeover vulnerability that allows users with the base creator role to hijac |
| CVE-2026-130704 | 8.8 | 2026-11-18 | NocoDB before 2026.10.0 contains an improper access control vulnerability that allows Creator-role users to attach NocoD |
| CVE-2026-130706 | 9.1 | 2026-11-18 | NocoDB before 2026.09.0 contains an sql injection vulnerability that allows authenticated Creator or Owner users to inje |
| CVE-2026-130708 | 7.5 | 2026-11-18 | NocoDB before 2026.09.0 contains an improper authorization vulnerability that allows workspace Creator users to read pla |
| CVE-2026-130709 | 8.8 | 2026-11-18 | NocoDB before 2026.09.0 contains a server-side template injection vulnerability that allows authenticated Creator or Own |
| CVE-2026-130712 | 9.6 | 2026-11-18 | NocoDB before 2026.08.1 contains an authorization bypass vulnerability that allows authenticated Creators to access anot |
| CVE-2026-130716 | 8.7 | 2026-11-18 | NocoDB before 2026.08.0 contains a stored cross-site scripting vulnerability that allows authenticated Creator or Editor |
| CVE-2026-130718 | 7.5 | 2026-11-18 | NocoDB before 2026.08.0 contains an authorization bypass vulnerability that allows anonymous share link holders to acces |
| CVE-2026-130721 | 8.1 | 2026-11-18 | NocoDB from 2026.06.2 before 2026.08.0 contains an authorization bypass vulnerability that allows authenticated base Edi |
| CVE-2026-130723 | 7.5 | 2026-11-18 | NocoDB before 2026.08.0 contains an information disclosure vulnerability that allows unauthenticated attackers to access |
| CVE-2026-130724 | 8.5 | 2026-11-18 | NocoDB before 2026.08.0 contains a server-side request forgery vulnerability that allows authenticated base Editors to m |
| CVE-2026-130727 | 7.5 | 2026-11-18 | NocoDB before 2026.08.0 contains an authorization bypass vulnerability in public shared-view endpoints that fetch record |
| CVE-2026-130728 | 7.3 | 2026-11-18 | NocoDB before 2026.08.0 contains a stored cross-site scripting vulnerability that allows any authenticated user to regis |
| CVE-2026-130729 | 7.5 | 2026-11-18 | NocoDB before 2026.08.0 contains an authorization bypass in its public shared-view relation endpoints, which verify that |
| CVE-2026-130730 | 8.7 | 2026-11-18 | NocoDB before 2026.10.1 contains an authentication bypass vulnerability that allows OAuth token holders to act as full s |
| CVE-2026-130732 | 7.5 | 2026-11-18 | Traefik from 2.11.58 before 2.11.61 contains a resource leak vulnerability that allows unauthenticated attackers to exha |
| CVE-2026-130733 | 9.8 | 2026-11-18 | Grav from 2.0.0 before 2.2.18 contains an authorization bypass vulnerability that allows publishers to overwrite pages t |
| CVE-2026-130735 | 9.8 | 2026-11-18 | Grav from 2.0.0 before 2.2.18 contains a Twig injection vulnerability that allows media-only accounts and anonymous uplo |
| CVE-2026-130736 | 8.8 | 2026-11-18 | Grav from 2.0.0 before 2.2.18 contains a remote code execution vulnerability that allows publishers to bypass the media  |
| CVE-2026-130737 | 7.2 | 2026-11-18 | Grav from 2.0.0 before 2.2.18 contains a privilege escalation vulnerability that allows user managers to grant super-adm |
| CVE-2026-130738 | 7.2 | 2026-11-18 | Grav from 2.0.0 before 2.2.18 contains a privilege escalation vulnerability that allows user managers with admin.users.u |
| CVE-2026-130739 | 8.8 | 2026-11-18 | Grav from 2.0.0 before 2.2.18 contains a privilege escalation vulnerability that allows user managers and Flex editors t |
| CVE-2026-130740 | 7.5 | 2026-11-18 | Grav from 2.0.0 before 2.2.18 contains an information disclosure vulnerability that allows publishers and read-only user |
| CVE-2026-130741 | 8.8 | 2026-11-18 | Grav from 2.0.0 before 2.2.18 contains a Twig sandbox bypass vulnerability that allows publishers to read any server fil |
| CVE-2026-130742 | 8.8 | 2026-11-18 | Grav 2.0.0 before 2.2.18 resolves Flex sort and filter field names by first calling them as public methods, so a field n |
| CVE-2026-130743 | 8.8 | 2026-11-18 | Grav from 2.0.0 before 2.2.18 contains an insecure blueprint trust vulnerability that allows publisher accounts to read  |
| CVE-2026-130744 | 8.8 | 2026-11-18 | Grav from 2.0.0 before 2.2.18 contains a remote code execution vulnerability that allows page editors to escape the Twig |
| CVE-2026-130746 | 7.5 | 2026-11-18 | Grav before 1.7.53.7 and 2.x before 2.2.18 serves page media files, and rendered pages when lazy sessions are enabled, w |
| CVE-2026-130747 | 8.1 | 2026-11-18 | Grav before 1.7.53.7 and 2.x before 2.2.18 contains an authentication bypass vulnerability that allows anonymous visitor |
| CVE-2026-130748 | 7.5 | 2026-11-18 | Grav from 2.0.0 before 2.2.18 contains a password reset poisoning vulnerability that allows anonymous attackers to redir |
| CVE-2026-130749 | 7.5 | 2026-11-18 | Grav from 2.0.0 before 2.2.18 contains a resource exhaustion vulnerability that allows unauthenticated attackers to fill |
| CVE-2026-82952 | 8.8 | 2026-11-18 | Latvijas Valsts radio un televīzijas centrs (LVRTC)
eParakstītājs 3.0 version 1.10.0-resolute for Linux allows an unauth |
| CVE-2026-87789 | 8.8 | 2026-11-18 | Latvijas Valsts radio un televīzijas centrs (LVRTC)
eParakstītājs 3.0 version 1.10.0 for macOS allows an unauthenticated |
| CVE-2026-87790 | 8.8 | 2026-11-18 | Latvijas Valsts radio un televīzijas centrs (LVRTC)
eParakstītājs 3.0 version 1.10.0-resolute allows an unauthenticated  |
| CVE-2026-96571 | 7.2 | 2026-11-18 | The FancyBox for WordPress plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comment Anchor 'href' A |
| CVE-2026-107518 | 8.7 | 2026-11-18 | Dell PowerStore contains a Server-Side Request Forgery (SSRF) vulnerability. An authenticated user with limited privileg |
| CVE-2026-107519 | 8.1 | 2026-11-18 | Dell PowerStore contains an integer underflow vulnerability. An attacker could exploit this vulnerability, potentially l |
| CVE-2026-113699 | 7.2 | 2026-11-18 | Improper neutralization of special elements used in an OS command ('OS command injection') vulnerability in Aidata Biliş |
| CVE-2026-125033 | 7.2 | 2026-11-18 | The Smash Balloon Social Post Feed – Simple Social Feeds for WordPress plugin for WordPress is vulnerable to Stored Cros |
| CVE-2026-130333 | 7.2 | 2026-11-18 | The SNORDIAN's H5PxAPIkatchu plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'xapi' parameter  |
| CVE-2026-132121 | 8.1 | 2026-11-18 | Supergateway 2.4.0 through 4.2.2 contains a cross-site WebSocket hijacking vulnerability in stdio-to-WebSocket mode that |
| CVE-2026-107515 | 8.8 | 2026-11-18 | Dell PowerStore contains an Improper Privilege Management vulnerability. An authenticated attacker could exploit this vu |
| CVE-2026-107516 | 7.2 | 2026-11-18 | Dell PowerStore contains an OS command injection vulnerability. An authenticated user with limited privileges could pote |
| CVE-2026-107644 | 7.4 | 2026-11-18 | The Bizuno Accounting – ERP/Accounting/CRM (for WordPress) plugin for WordPress is vulnerable to Authentication Bypass v |
| CVE-2026-108761 | 7.1 | 2026-11-18 | The UpdraftPlus: WP Backup & Migration Plugin for WordPress is vulnerable to second-order SQL Injection via the user pro |
| CVE-2026-110009 | 9.8 | 2026-11-18 | The Unzer Payments plugin for WordPress is vulnerable to Authentication Bypass leading to Account Takeover in all versio |
| CVE-2026-110811 | 9.8 | 2026-11-18 | The Trust Payments Gateway for WooCommerce (JavaScript Library) plugin for WordPress is vulnerable to Authentication Byp |
| CVE-2026-115815 | 7.5 | 2026-11-18 | The rus to lat advanced plugin for WordPress is vulnerable to blind SQL Injection via the 'name' parameter in all versio |
| CVE-2026-115826 | 7.4 | 2026-11-18 | The Multi Step for Contact Form 7 plugin for WordPress is vulnerable to Insecure Direct Object Reference in all versions |
| CVE-2026-116519 | 7.2 | 2026-11-18 | The Geo Mashup plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'author (comment form) / displa |
| CVE-2026-116758 | 7.2 | 2026-11-18 | The Advanced Country Blocker plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'REQUEST_URI' par |
| CVE-2026-116764 | 8.1 | 2026-11-18 | The The GDPR Framework By Data443 plugin for WordPress is vulnerable to authorization bypass in all versions up to, and  |
| CVE-2026-123123 | 7.5 | 2026-11-18 | An attacker that is able to send a crafted network packet to the affected component may trigger an integer overflow duri |
| CVE-2026-123419 | 8.1 | 2026-11-18 | The immonex Kickstart plugin for WordPress is vulnerable to Local File Inclusion in all versions up to, and including, 1 |
| CVE-2026-125053 | 7.2 | 2026-11-18 | The WEB-Translation – eTranslation Multilingual plugin for WordPress is vulnerable to Stored Cross-Site Scripting via th |
| CVE-2026-126131 | 7.2 | 2026-11-18 | The WP Instant Feeds plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'data[images][][url]' par |
| CVE-2026-130014 | 7.5 | 2026-11-18 | The Team VCard generator plugin for WordPress is vulnerable to Directory Traversal in all versions up to, and including, |
| CVE-2026-130893 | 7.8 | 2026-11-18 | Tanium addressed an unauthorized code execution vulnerability. |
| CVE-2026-131575 | 7.5 | 2026-11-18 | Tanium addressed an insertion of sensitive information into a log file vulnerability in TanOS. |
| CVE-2026-95787 | 10.0 | 2026-11-18 | Vulnerabilities in the PAPI protocol of AOS-10 could allow an unauthenticated remote attacker to circumvent existing aut |
| CVE-2026-95788 | 7.1 | 2026-11-18 | An unauthenticated buffer overflow vulnerability exists in the underlying operating system of AOS-10 or AOS-8 and could  |
| CVE-2026-95789 | 7.2 | 2026-11-18 | Command injection vulnerability in the affected interface of AOS-10 or AOS-8 could allow an authenticated remote attacke |
| CVE-2026-96665 | 7.2 | 2026-11-18 | The SendPress Newsletters plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'sp_firstname' param |
| CVE-2026-109908 | 7.8 | 2026-11-18 | A heap buffer overflow in reading encoding files in X.Org libfontenc before 1.11.0 could be used by local attackers able |
| CVE-2026-111507 | 8.1 | 2026-11-18 | Dell PowerStore contains an authorization bypass vulnerability. A remote attacker could exploit this vulnerability to ac |
| CVE-2026-116446 | 9.8 | 2026-11-18 | Dell PowerStore SDNAS contains an out-of-bounds memory vulnerability in the NAS NFS service that an unauthenticated remo |
| CVE-2026-116447 | 8.8 | 2026-11-18 | Dell PowerStore SDNAS contains a local privilege-escalation vulnerability that could allow a low-privileged attacker to  |
| CVE-2026-116448 | 9.8 | 2026-11-18 | Dell PowerStore SDNAS contains an OS Command Injection vulnerability that could allow an attacker with internal network  |
| CVE-2026-131801 | 7.7 | 2026-11-18 | Tanium addressed an improper input validation vulnerability in Threat Response. |
| CVE-2026-132038 | 7.8 | 2026-11-18 | Rapid7 Metasploit Framework versions prior to 6.5.10 suffer from an Improper Access Control issue in the msfdb database  |
| CVE-2026-132150 | 7.8 | 2026-11-18 | A flaw was found in the file-xmc plugin in GIMP. When processing a specially crafted XMC image file, the plugin does not |
| CVE-2026-3232 | 7.2 | 2026-11-18 | The Easy Appointments plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'name' and 'phone' field |
| CVE-2026-82171 | 8.0 | 2026-11-18 | Dell PowerStore contains an XML External Entity (XXE) Injection vulnerability. A high-privileged attacker could exploit  |
| CVE-2026-95823 | 7.5 | 2026-11-18 | tcp_pkt_linearize() in subsys/net/ip/tcp.c is used by th_get() whenever a received TCP header is not contiguous in a sin |
| CVE-2012-20007 | 9.8 | 2026-11-18 | ThinkPHP 2.0 through 2.2 and 3.0 Lite mode contains an eval injection vulnerability in the Dispatcher PATH_INFO parsing, |
| CVE-2012-20008 | 8.8 | 2026-11-18 | openSIS 5.1 before 9.0 contains a local file inclusion vulnerability that allows authenticated users to include arbitrar |
| CVE-2016-20105 | 8.1 | 2026-11-18 | Lucee Server versions 5.0.0.0 before 5.3.4.46 contain an insecure default configuration that allows unauthenticated atta |
| CVE-2016-20106 | 7.5 | 2026-11-18 | NUUO NVRmini 2 through 3.0.8 contains a file disclosure vulnerability that allows unauthenticated attackers to read web- |
| CVE-2018-25442 | 8.3 | 2026-11-18 | Baidu UEditor 1.4.0 before 1.4.3.1 contains a server-side request forgery vulnerability that allows unauthenticated atta |
| CVE-2018-25443 | 9.8 | 2026-11-18 | Baidu UEditor 1.4.0 through 1.4.3.3 contains an unrestricted file upload vulnerability in the catchimage action of /uedi |
| CVE-2019-25782 | 9.8 | 2026-11-18 | ThinkPHP 5.0.0 before 5.0.24 contains a code injection vulnerability that allows unauthenticated attackers to execute co |
| CVE-2019-25784 | 8.2 | 2026-11-18 | FineCMS versions 5.0.4 before 5.0.11 contain an unauthenticated SQL injection vulnerability in the data2 API action hand |
| CVE-2019-25785 | 7.5 | 2026-11-18 | FineReport 8.0 contains a path traversal vulnerability that allows unauthenticated attackers to read arbitrary files thr |
| CVE-2021-48021 | 8.2 | 2026-11-18 | Chamilo LMS 1.11.10 before 1.11.16 contains an unauthenticated SQL injection vulnerability in the searchOptionsFromTags  |
| CVE-2021-48022 | 7.5 | 2026-11-18 | Rocket.Chat versions 0.61.0 before 3.11.4, 3.12.x before 3.12.4 and 3.13.x before 3.13.2 contain a missing authorization |
| CVE-2021-48023 | 9.8 | 2026-11-18 | Weaver E-cology 9.0 contains an unrestricted file upload vulnerability in /page/exportImport/uploadOperation.jsp that al |
| CVE-2021-48025 | 9.8 | 2026-11-18 | OpenSNS 3.2.1 contains an unauthenticated code injection vulnerability in the shareBox method of ShareController that al |
| CVE-2022-51027 | 9.8 | 2026-11-18 | MeterSphere versions 1.13.0 before 1.14.7 and 1.15.0 before 1.16.4 contain a pre-authentication code injection vulnerabi |
| CVE-2022-51028 | 8.2 | 2026-11-18 | CmsEasy 7.7.5_20210919 contains an unauthenticated SQL injection vulnerability in the execsql_action function at /?case= |
| CVE-2022-51029 | 7.5 | 2026-11-18 | Synway SMG Gateway Management Software builds through 2022-03-15 contain a path traversal vulnerability that allows unau |
| CVE-2022-51030 | 7.5 | 2026-11-18 | QiboCMS V7 contains an arbitrary file download vulnerability in inc/job/download.php that allows unauthenticated attacke |
| CVE-2022-51034 | 8.2 | 2026-11-18 | Tangshan Pingsheng Reservoir Safety Supervision Platform builds through 2022-11-30 contain an unauthenticated SQL inject |
| CVE-2023-54417 | 7.5 | 2026-11-18 | Nuxt 3.0.0 before 3.4.2 contains a semi-arbitrary file read vulnerability in the vite-node dev server middleware that al |
| CVE-2023-54418 | 7.5 | 2026-11-18 | Nuxt 3.0.0-rc.1 before 3.0.0-rc.13 contains an arbitrary file read vulnerability caused by the Vite dev server default s |
| CVE-2023-54419 | 9.8 | 2026-11-18 | nginxWebUI 3.0.0 before 3.5.8 contains an authentication bypass vulnerability that allows unauthenticated attackers to r |
| CVE-2023-54420 | 7.5 | 2026-11-18 | LiveBOS builds through 2023-08-16 contain a path traversal vulnerability that allows unauthenticated attackers to read a |
| CVE-2023-54422 | 9.8 | 2026-11-18 | iDocView before 13.10.1_20231115 contains an unrestricted file upload vulnerability in the /html/2word endpoint that all |
| CVE-2024-58402 | 8.2 | 2026-11-18 | Azon Dominator releases through 2024-06-03 contain an SQL injection vulnerability that allows unauthenticated attackers  |
| CVE-2024-58403 | 7.5 | 2026-11-18 | AnyShare builds through 2024-11 contain a missing authentication vulnerability in the /api/ShareMgnt/Usrm_GetAllUsers en |
| CVE-2026-113425 | 8.1 | 2026-11-18 | When NGINX Plus or NGINX Open Source is configured as a mail proxy, undisclosed traffic can cause a use-after-free in an |
| CVE-2026-116443 | 9.8 | 2026-11-18 | Dell PowerStore SDNAS contains a stack-based buffer overflow in the NAS TFTP service that could allow an unauthenticated |
| CVE-2026-116449 | 9.8 | 2026-11-18 | Dell PowerStore SDNAS contains an OS Command Injection vulnerability that could allow an attacker with internal network  |
| CVE-2026-116953 | 9.8 | 2026-11-18 | Description:

When an iRule that processes client traffic using the GENERICMESSAGE::route command is configured on a vir |
| CVE-2026-118899 | 7.5 | 2026-11-18 | When using the listen directive with the ssl parameter in the http block with TLSv1.3 enabled, an attacker can use a spe |
| CVE-2026-120285 | 9.8 | 2026-11-18 | Description
When an HTTP profile and an iRule containing the PSC::ip_address command are configured on a virtual server, |
| CVE-2026-120292 | 9.8 | 2026-11-18 | Description:


When an HTTP profile and an iRule using the 

MR::message 

route command are configured on a virtual ser |
| CVE-2026-120718 | 8.1 | 2026-11-18 | Description: 
BIG-IP iControl REST tokens may not expire as expected in all scenarios.   

Impact: 
An attacker who has  |
| CVE-2026-120722 | 9.8 | 2026-11-18 | Description:

When an iRule that processes client traffic using the DNS::scrape command is configured on a virtual serve |
| CVE-2026-121805 | 9.8 | 2026-11-18 | Description:

When an iRule that processes client traffic using the PEM::subscriber command is configured on a virtual s |
| CVE-2026-121810 | 8.1 | 2026-11-18 | Description:
This issue affects NGINX Plus and NGINX Open Source configurations that use HTTP/3. A remote, unauthenticat |
| CVE-2026-121812 | 7.5 | 2026-11-18 | Description:


When BIG-IP APM is provisioned, and a virtual server is configured with an APM access profile and a per-r |
| CVE-2026-123007 | 8.1 | 2026-11-18 | This issue affects NGINX Plus or NGINX Open Source configurations that use HTTP/2. When NGINX processes undisclosed traf |
| CVE-2026-123633 | 8.1 | 2026-11-18 | When NGINX Plus or NGINX Open Source is configured to use HTTP/2 for client connections and proxy client requests to a b |
| CVE-2026-123634 | 8.1 | 2026-11-18 | This issue occurs when NGINX Plus or NGINX Open Source is configured as a proxy, the proxied server name includes variab |
| CVE-2026-123637 | 9.8 | 2026-11-18 | When BIG-IP APM is provisioned and a per-request policy that includes the Client Information agent and Endpoint Security |
| CVE-2026-124990 | 9.8 | 2026-11-18 | The Masteriyo LMS – LMS Course Builder, Quizzes & Certificates plugin for WordPress is vulnerable to PHP Object Injectio |
| CVE-2026-125272 | 7.5 | 2026-11-18 | Description:






When BIG-IP APM is licensed and provisioned, and a virtual server with the APM access profile is conf |
| CVE-2026-125274 | 8.8 | 2026-11-18 | An authenticated iControl SOAP user with at least Guest access can inject an unauthorized management request.





Impac |
| CVE-2026-126336 | 7.5 | 2026-11-18 | Description:


When BIG-IP APM is provisioned and a virtual server is configured with an APM Access profile and a SAML S |
| CVE-2026-126721 | 7.5 | 2026-11-18 | The Magic Login Mail or QR Code plugin for WordPress is vulnerable to Privilege Escalation via Administrator Account Tak |
| CVE-2026-126752 | 9.8 | 2026-11-18 | Dagu 1.23.0 before 2.0.0 defaults auth.mode to none, allowing unauthenticated attackers to execute OS commands through t |
| CVE-2026-126755 | 9.8 | 2026-11-18 | ArangoDB before 3.12.11 contains an authentication bypass vulnerability caused by a parser differential between the raw  |
| CVE-2026-126822 | 7.5 | 2026-11-18 | Description:





When BIG-IP APM is provisioned, an Access Profile is configured as a SAML SP (Service Provider) and is |
| CVE-2026-127178 | 8.1 | 2026-11-18 | A stored cross site scripting attack when viewing email aliases in postfixadmin 4.0 before 4.0.7, and postfixadmin 3.3 b |
| CVE-2026-63189 | 9.8 | 2026-11-18 | Dialoqbase is an application for creating chatbots. Prior to 1.11.5, the unauthenticated GET /api/v1/view/* route in ser |
| CVE-2026-71861 | 7.4 | 2026-11-18 | The Chainguard SDK is a public Go SDK for integrating with the Chainguard platform. Prior to 0.1.107, auth/aws.VerifyTok |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-115731 | Perforce / Puppet Enterprise | 2026-11-17 | 2026-12-01 | Unknown |
| CVE-2026-114713 | UnrealIRCd / UnrealIRCd | 2026-11-13 | 2026-11-16 | Unknown |
| CVE-2026-123039 | Check Point / Multiple Products | 2026-11-13 | 2026-11-16 | Unknown |

---

*Total entries in CISA KEV catalog: 1782*