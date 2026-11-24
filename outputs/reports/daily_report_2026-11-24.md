# Vulnerability Intelligence Report

**Date:** 2026-11-24  
**Generated:** 2026-11-24T19:20:23Z  

---

## Executive Summary

Our environment faces significant exposure across 293 high-severity vulnerabilities, including ten critical CVEs with CVSS scores up to 9.6. The most urgent threats include server-side request forgery in Azure Machine Learning and Profile Data Roaming Service, authorization bypass in Microsoft Clarity, and remote code execution in HPE Morpheus Manager. CISA added 14 new actively exploited vulnerabilities to its Known Exploited Vulnerabilities catalog in the past seven days, signaling active threat actor targeting. Immediate remediation focus should center on the highest-scored CVEs enabling privilege escalation and unauthenticated code execution, as these pose the greatest risk to business continuity and data integrity.

---

## Risk Narrative

The current threat landscape is characterized by a surge in privilege escalation and remote code execution vulnerabilities targeting cloud services, enterprise software, and open-source platforms. High-profile Microsoft Azure services, HPE infrastructure, and widely deployed CMS platforms like Drupal are actively targeted, as confirmed by CISA KEV additions. Threat actors are exploiting SSRF, authorization bypass, and XSS flaws to move laterally, exfiltrate data, and gain persistent access. The 14 new KEV entries in seven days indicate accelerating exploitation activity. Business risks include unauthorized access to sensitive cloud workloads, financial loss via e-commerce price manipulation, and potential regulatory penalties from data exposure through Elasticsearch vulnerabilities. Failure to act promptly could result in full infrastructure compromise.

---

## Prioritized Action Items

1. Immediately patch CVE-2026-109480 and CVE-2026-118285 (CVSS 9.6 SSRF vulnerabilities in PDRS and Azure Machine Learning) to prevent privilege escalation over the network.
2. Remediate CVE-2026-95793 (CVSS 8.8 RCE in HPE Morpheus Manager) as unauthenticated remote code execution represents a critical threat to infrastructure integrity.
3. Address CVE-2026-109490 and CVE-2026-113824 (CVSS 9.3 and 9.1) to close XSS and authorization bypass vulnerabilities enabling unauthorized privilege elevation.
4. Review and apply mitigations for all 14 newly added CISA KEV entries, prioritizing Drupal Core and N-able MailAssure due to their broad deployment footprints.
5. Conduct a full audit of the remaining 283 high-severity CVEs to identify any assets exposed to internet-facing attack surfaces and prioritize patching accordingly.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-135470 | 7.5 | 2026-11-23 | WPC Product Options for WooCommerce before 4.0.9 contains a price manipulation vulnerability that allows unauthenticated |
| CVE-2026-95793 | 8.8 | 2026-11-23 | An arbitrary remote code execution vulnerability exists in HPE Morpheus Manager. |
| CVE-2026-130164 | 7.8 | 2026-11-23 | Hermes Agent is an open-source autonomous AI agent built by Nous Research for running tool-using workflows across CLI, d |
| CVE-2026-82303 | 7.5 | 2026-11-23 | A buffer over-read vulnerability in Elasticsearch transport decompression can expose data from other requests. The LZ4 d |
| CVE-2026-109480 | 9.6 | 2026-11-23 | Server-side request forgery in Profile Data Roaming Service (PDRS) allows an authorized attacker to elevate privileges o |
| CVE-2026-109490 | 9.3 | 2026-11-23 | Improper neutralization of input during web page generation ('cross-site scripting') in Authentication Methods Portal Ex |
| CVE-2026-113824 | 9.1 | 2026-11-23 | Authorization bypass through user-controlled key in Microsoft Clarity allows an unauthorized attacker to elevate privile |
| CVE-2026-118285 | 9.6 | 2026-11-23 | Server-side request forgery in Azure Machine Learning allows an authorized attacker to elevate privileges over a network |
| CVE-2026-118286 | 9.1 | 2026-11-23 | Improper access control in Azure Site Recovery allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-120777 | 7.1 | 2026-11-23 | Incorrect authorization in Azure Managed Service Identity allows an authorized attacker to elevate privileges over a net |
| CVE-2026-120787 | 7.5 | 2026-11-23 | Improper certificate validation in Microsoft Office PowerPoint allows an unauthorized attacker to execute code over a ne |
| CVE-2026-129837 | 7.5 | 2026-11-23 | A flaw was found in rsyslog. A remote, unauthenticated attacker can cause a Denial of Service (DoS) by sending a special |
| CVE-2026-134069 | 7.3 | 2026-11-23 | Use of a default cryptographic key in the instance registration component in Amazon SSM Agent before 3.3.5226.0 on AWS-p |
| CVE-2026-50691 | 9.9 | 2026-11-23 | Improper authorization in M365 Copilot allows an authorized attacker to elevate privileges over a network. |
| CVE-2026-62841 | 10.0 | 2026-11-23 | Improper authentication in Azure Event Grid allows an unauthorized attacker to elevate privileges over a network. |
| CVE-2026-65817 | 8.3 | 2026-11-23 | Improper neutralization of special elements used in an os command ('os command injection') in Azure Managed Instance for |
| CVE-2026-69437 | 8.6 | 2026-11-23 | Missing authorization in Azure AI Foundry allows an unauthorized attacker to disclose information over a network. |
| CVE-2026-69899 | 9.1 | 2026-11-23 | Authentication bypass by spoofing in Azure DevTest Labs allows an unauthorized attacker to perform spoofing over a netwo |
| CVE-2026-70193 | 9.9 | 2026-11-23 | Improper limitation of a pathname to a restricted directory ('path traversal') in Microsoft Office SharePoint allows an  |
| CVE-2026-70305 | 9.6 | 2026-11-23 | Improper neutralization of input during web page generation ('cross-site scripting') in Azure Portal allows an unauthori |
| CVE-2026-81962 | 8.6 | 2026-11-23 | Incorrect authorization in Azure Machine Learning allows an unauthorized attacker to disclose information over a network |
| CVE-2026-93700 | 9.0 | 2026-11-23 | An authenticated WHMCS client could potentially leverage this flaw to read sensitive configuration files on the WHMCS ho |
| CVE-2026-101862 | 8.8 | 2026-11-23 | EUSurvey through 1.6, prior to commit 0669a36, contains a path traversal vulnerability in the survey import function tha |
| CVE-2026-101863 | 8.8 | 2026-11-23 | EUSurvey 1.5.5 through 1.6, prior to commit d5295d5, contains a missing authorization vulnerability in the POST /forms/b |
| CVE-2026-101864 | 7.7 | 2026-11-23 | EUSurvey through 1.6, prior to commit a4161a9, contains a weak password recovery mechanism that allows attackers who obt |
| CVE-2026-101866 | 8.2 | 2026-11-23 | EUSurvey through 1.6, prior to commit 118facd, contains an authorization bypass vulnerability in the public POST /runner |
| CVE-2026-101867 | 8.1 | 2026-11-23 | EUSurvey through 1.6, prior to commit edb5021, contains an incorrect authorization vulnerability in the GET /settings/sh |
| CVE-2026-101868 | 7.5 | 2026-11-23 | EUSurvey through 1.6, prior to commit 4bf95a3, contains an authorization bypass vulnerability in the GET /preparepublish |
| CVE-2026-101869 | 7.5 | 2026-11-23 | EUSurvey 1.4.4.6738 through 1.6, prior to commit de1145c, contains an SQL injection vulnerability in the public results  |
| CVE-2026-101870 | 7.5 | 2026-11-23 | EUSurvey through 1.6, prior to commit de1145c, contains an authorization bypass vulnerability in the public POST /editco |
| CVE-2026-101871 | 7.5 | 2026-11-23 | EUSurvey 1.5.2 through 1.6, prior to commit ffd5da7, contains a missing authorization vulnerability in the public POST / |
| CVE-2026-130169 | 10.0 | 2026-11-23 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agent |
| CVE-2026-132257 | 8.2 | 2026-11-23 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agent |
| CVE-2026-134021 | 7.5 | 2026-11-23 | TastyIgniter is an open-source online ordering, table reservation, and restaurant management system. Prior to 4.3.1, the |
| CVE-2026-134023 | 7.4 | 2026-11-23 | TastyIgniter is an open-source online ordering, table reservation, and restaurant management system. Prior to 4.2.0, che |
| CVE-2026-120747 | 8.8 | 2026-11-24 | Tanium addressed a command injection vulnerability in Comply. |
| CVE-2026-133863 | 8.8 | 2026-11-24 | Tanium addressed an improper access controls vulnerability in Tanium Server. |
| CVE-2026-133864 | 8.8 | 2026-11-24 | Tanium addressed a command injection vulnerability in Default Content. |
| CVE-2026-133880 | 8.8 | 2026-11-24 | Tanium addressed a command injection vulnerability in Threat Response. |
| CVE-2026-133955 | 7.1 | 2026-11-24 | Tanium addressed an improper input validation vulnerability in Core Content. |
| CVE-2026-133959 | 8.8 | 2026-11-24 | Tanium addressed a command injection vulnerability in Core Content - Enhanced Tags. |
| CVE-2026-133960 | 8.8 | 2026-11-24 | Tanium addressed an unauthorized code execution vulnerability in the Tanium Default Content. |
| CVE-2026-133961 | 7.2 | 2026-11-24 | Tanium addressed an unauthorized code execution vulnerability in the Tanium Default Content. |
| CVE-2026-134401 | 9.6 | 2026-11-24 | Improper input validation in Variations in Google Chrome prior to 158.0.8127.88 allowed a remote attacker to potentially |
| CVE-2026-134493 | 7.5 | 2026-11-24 | Tanium addressed a path traversal vulnerability in Core Content. |
| CVE-2026-134494 | 8.0 | 2026-11-24 | Tanium addressed an argument injection vulnerability in Core Content. |
| CVE-2026-134496 | 7.3 | 2026-11-24 | Tanium addressed an improper input validation vulnerability in Core Content. |
| CVE-2026-134618 | 7.3 | 2026-11-24 | Tanium addressed a local privilege escalation vulnerability in Emerging Issues Content. |
| CVE-2026-134619 | 7.3 | 2026-11-24 | Tanium addressed a local privilege escalation vulnerability in Emerging Issues Content. |
| CVE-2026-134620 | 8.8 | 2026-11-24 | Tanium addressed a command injection vulnerability in Engage. |
| CVE-2026-133448 | 7.1 | 2026-11-24 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agent |
| CVE-2026-135686 | 7.4 | 2026-11-24 | Trilium through 0.107.0 contains an sql injection vulnerability in updateNormalEntity() that allows malicious sync partn |
| CVE-2026-135689 | 8.1 | 2026-11-24 | Community Store for Concrete CMS before 2.8.0 contains a stored cross-site scripting vulnerability that allows unauthent |
| CVE-2026-135691 | 8.8 | 2026-11-24 | Open5GS WebUI through 2.8.0 contains an incorrect authorization vulnerability in webui/server/routes/db.js that allows a |
| CVE-2026-135692 | 8.8 | 2026-11-24 | rConfig Core 8.0.0 before 8.2.17 and rConfig Pro before 8.4.0 contain a PHP object injection vulnerability in app/Casts/ |
| CVE-2026-135693 | 8.7 | 2026-11-24 | rConfig Core 8.0.0 before 8.2.17 and rConfig Pro before 8.4.0 contain a stored cross-site scripting vulnerability in the |
| CVE-2026-135695 | 8.8 | 2026-11-24 | rConfig Core 8.0.0 before 8.2.13 and rConfig Pro before 8.4.0 contain an authorization bypass vulnerability in the users |
| CVE-2026-135696 | 7.5 | 2026-11-24 | rConfig Core 8.2.19 before 8.2.22 contains a server-side request forgery vulnerability that allows authenticated users t |
| CVE-2026-130178 | 7.7 | 2026-11-24 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agent |
| CVE-2026-18530 | 9.9 | 2026-11-24 | OS command injection in the a3cli restricted shell in Lantronix S2220 Series 2 allows an authenticated attacker to bypas |
| CVE-2026-135706 | 7.0 | 2026-11-24 | FFmpeg before 9.1 contains a heap buffer overflow vulnerability in modplug_read_header() in libavformat/libmodplug.c tha |
| CVE-2026-135709 | 7.0 | 2026-11-24 | FFmpeg before 9.1 contains an out-of-bounds write vulnerability in ogg_buffer_data() in libavformat/oggenc.c because ogg |
| CVE-2026-135722 | 7.8 | 2026-11-24 | FFmpeg before 9.1 contains a heap-based buffer overflow vulnerability in peak_init_writer() and wav_write_packet() in li |
| CVE-2026-135723 | 7.0 | 2026-11-24 | FFmpeg before 9.1 contains a double free vulnerability in the fill_marker() function of libavformat/imf_cpl.c that frees |
| CVE-2026-135725 | 7.8 | 2026-11-24 | FFmpeg before 9.1 contains a stack-based buffer overflow vulnerability in ff_rtmp_packet_write() in libavformat/rtmppkt. |
| CVE-2026-135734 | 7.8 | 2026-11-24 | FFmpeg before 9.1 contains a heap out-of-bounds write vulnerability in the deflicker filter that lets attackers corrupt  |
| CVE-2026-135736 | 8.1 | 2026-11-24 | FFmpeg 4.4 before 9.1 contains a heap out-of-bounds read and write vulnerability in libavfilter/vf_deband.c that allows  |
| CVE-2026-135737 | 7.8 | 2026-11-24 | FFmpeg before 9.1 contains a heap out-of-bounds write and read vulnerability in the tmidequalizer filter that allows att |
| CVE-2026-135738 | 7.8 | 2026-11-24 | FFmpeg before 9.1 contains a heap out-of-bounds write vulnerability in libavfilter/vf_signalstats.c that allows attacker |
| CVE-2026-135740 | 7.8 | 2026-11-24 | FFmpeg before 9.1 contains a heap out-of-bounds write vulnerability in libavfilter/vf_readeia608.c because build_histogr |
| CVE-2026-135742 | 7.5 | 2026-11-24 | FFmpeg before 9.1 contains a heap buffer overflow vulnerability in recv_msg() of the zmq and azmq filters that allows un |
| CVE-2026-135743 | 8.1 | 2026-11-24 | FFmpeg 4.3 before 9.1 contains a heap out-of-bounds read and write vulnerability in the dynaudnorm filter because cqueue |
| CVE-2026-135457 | 7.3 | 2026-11-24 | A security flaw has been discovered in amirhamza05 Student-Management-System up to 449397e35d42e3779f14f0bfc654ab307103f |
| CVE-2026-105304 | 8.6 | 2026-11-24 | ACME challenge routing logic of Zoraxy fails to validate request URIs properly, that allows an attacker to send an arbit |
| CVE-2026-135202 | 9.8 | 2026-11-24 | Several plugins for WordPress published by WP connect (Orders Sync to Airtable for WooCommerce, Add-On for Contact Form  |
| CVE-2026-121016 | 8.8 | 2026-11-24 | The affected products insufficiently restrict runtime-supplied visualization data, allowing local program execution on t |
| CVE-2026-121017 | 8.8 | 2026-11-24 | The affected products insufficiently restrict runtime-supplied visualization data, allowing to invoke local COM/ActiveX  |
| CVE-2026-121018 | 8.8 | 2026-11-24 | The affected products insufficiently restrict runtime-supplied visualization commands, allowing local functionality on t |
| CVE-2026-127182 | 8.8 | 2026-11-24 | A stack buffer overflow in DLP/WAF in the enforcer dataplane of SUSE NeuVector before 5.5, 5.5 before 5.5.6, 5.6.0 befor |
| CVE-2026-127183 | 7.5 | 2026-11-24 | Various memory-safety issues in dataplane of SUSE Neuvector before 5.5, 5.5.0 before 5.5.6, 5.6.0 before 5.6.5 could be  |
| CVE-2026-59415 | 10.0 | 2026-11-24 | TypesenseVectorStore is vulnerable to a document ID injection in its delete operation that can cause unintended document |
| CVE-2026-117593 | 9.1 | 2026-11-24 | Weak Password Recovery Mechanism for Forgotten Password vulnerability in ITG Bilgisayar Teknoloji Grubu Tic. Ltd. Şti. V |
| CVE-2026-119543 | 8.8 | 2026-11-24 | Authorization bypass through User-Controlled key vulnerability in ITG Bilgisayar Teknoloji Grubu Tic. Ltd. Şti. VSRM all |
| CVE-2026-119582 | 9.8 | 2026-11-24 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in ITG Bilgisayar Tek |
| CVE-2026-13137 | 7.5 | 2026-11-24 | A stack-based buffer overflow vulnerability exists in multiple parsers of RTU500 components of User management, REST res |
| CVE-2026-127181 | 7.6 | 2026-11-24 | SUSE Neuvector before 5.5, 5.5.0 before 5.5.6 and 5.6.0 before 5.6.5 handling of ephemeral containers was not setting so |
| CVE-2026-134962 | 7.1 | 2026-11-24 | Missing Authorization vulnerability in Slim & Dapper Theater for WordPress theatre allows Exploiting Incorrectly Configu |
| CVE-2026-136120 | 8.1 | 2026-11-24 | Ziit 1.3.2 contains a cross-site request forgery vulnerability in the /api/auth/epilogue/callback handler that accepts r |
| CVE-2026-136123 | 7.5 | 2026-11-24 | Friendica through 2026.05-1 contains an improper validation vulnerability in APContact::compactProfile() that allows rem |
| CVE-2026-136126 | 8.1 | 2026-11-24 | c-icap-server through 0.5.15 and 0.6.5 contains an out-of-bounds write in process_encapsulated() that allows unauthentic |
| CVE-2026-136128 | 8.7 | 2026-11-24 | WPC Linked Variation plugin for WordPress, all versions before 4.6.1, contain a stored cross-site scripting vulnerabilit |
| CVE-2026-14569 | 7.5 | 2026-11-24 | Use of externally-controlled format string vulnerability exists in RTU500 component of the logging function for TLS, PPP |
| CVE-2026-82216 | 7.5 | 2026-11-24 | Server-Side request forgery (SSRF) vulnerability in ITG Bilgisayar Teknolojileri Grubu Ltd. Şti. VSRM allows Server Side |
| CVE-2026-100965 | 7.5 | 2026-11-24 | NVIDIA Triton Inference Server for Linux contains a vulnerability where an attacker could cause an uncaught exception. A |
| CVE-2026-100969 | 7.5 | 2026-11-24 | NVIDIA Triton Inference Server for Linux contains a vulnerability where an attacker could cause a NULL pointer dereferen |
| CVE-2026-100985 | 8.1 | 2026-11-24 | NVIDIA AIStore contains a vulnerability in object-copy destination validation where an unauthenticated attacker could us |
| CVE-2026-100986 | 8.1 | 2026-11-24 | NVIDIA AIStore contains a vulnerability in append-operation handle validation where an unauthenticated attacker could ca |
| CVE-2026-130822 | 7.5 | 2026-11-24 | In Valkey before 7.2.16, 8.0.x before 8.0.13, 8.1.x before 8.1.12, 9.0.x before 9.0.8, 9.1.x before 9.1.4 and 9.2.0 rele |
| CVE-2026-135500 | 8.8 | 2026-11-24 | Privilege escalation due to integer overflow in the Graphics: WebGPU component. This vulnerability was fixed in Firefox  |
| CVE-2026-135501 | 9.6 | 2026-11-24 | Sandbox escape due to use-after-free in the Audio/Video: cubeb component. This vulnerability was fixed in Firefox 161 an |
| CVE-2026-135504 | 8.8 | 2026-11-24 | Privilege escalation due to use-after-free in the Graphics component. This vulnerability was fixed in Firefox 161, Firef |
| CVE-2026-135505 | 8.8 | 2026-11-24 | Privilege escalation due to incorrect boundary conditions in the Audio/Video: Playback component. This vulnerability was |
| CVE-2026-135506 | 9.6 | 2026-11-24 | Sandbox escape in the Graphics: Text component. This vulnerability was fixed in Firefox 161, Firefox ESR 153.8, Thunderb |
| CVE-2026-135507 | 8.8 | 2026-11-24 | Use-after-free in the Disability Access APIs component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, |
| CVE-2026-135508 | 9.6 | 2026-11-24 | Sandbox escape due to use-after-free in the Graphics component. This vulnerability was fixed in Firefox 161, Firefox ESR |
| CVE-2026-135509 | 9.6 | 2026-11-24 | Sandbox escape due to use-after-free in the Graphics: WebRender component. This vulnerability was fixed in Firefox 161,  |
| CVE-2026-135510 | 9.6 | 2026-11-24 | Sandbox escape in the Networking: HTTP component. This vulnerability was fixed in Firefox 161 and Thunderbird 161. |
| CVE-2026-135511 | 8.8 | 2026-11-24 | Use-after-free in the DOM: Core & HTML component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firef |
| CVE-2026-135512 | 8.8 | 2026-11-24 | Use-after-free in the Cycle Collector component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firefo |
| CVE-2026-135513 | 9.6 | 2026-11-24 | Sandbox escape due to use-after-free in the Networking: HTTP component. This vulnerability was fixed in Firefox 161 and  |
| CVE-2026-135514 | 8.8 | 2026-11-24 | Use-after-free in the Cycle Collector component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firefo |
| CVE-2026-135515 | 8.8 | 2026-11-24 | Incorrect boundary conditions in the Networking: Cache component. This vulnerability was fixed in Firefox 161, Firefox E |
| CVE-2026-135517 | 8.8 | 2026-11-24 | Use-after-free in the Networking: Cache component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Fire |
| CVE-2026-135518 | 8.8 | 2026-11-24 | Use-after-free in the DOM: Core & HTML component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firef |
| CVE-2026-135519 | 9.6 | 2026-11-24 | Sandbox escape due to use-after-free in the Networking component. This vulnerability was fixed in Firefox 161, Firefox E |
| CVE-2026-135520 | 9.6 | 2026-11-24 | Sandbox escape in the Graphics: CanvasWebGL component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46,  |
| CVE-2026-135521 | 9.6 | 2026-11-24 | Sandbox escape in the DOM: Navigation component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firefo |
| CVE-2026-135522 | 8.8 | 2026-11-24 | Incorrect boundary conditions in the Audio/Video: Web Codecs component. This vulnerability was fixed in Firefox 161 and  |
| CVE-2026-135524 | 8.8 | 2026-11-24 | Use-after-free in the JavaScript Engine component. This vulnerability was fixed in Firefox 161, Firefox ESR 153.8, Thund |
| CVE-2026-135525 | 9.6 | 2026-11-24 | Sandbox escape due to use-after-free in the Graphics: WebRender component. This vulnerability was fixed in Firefox 161,  |
| CVE-2026-135526 | 8.8 | 2026-11-24 | Use-after-free in the DOM: Networking component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firefo |
| CVE-2026-135527 | 8.8 | 2026-11-24 | Use-after-free in the DOM: Core & HTML component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firef |
| CVE-2026-135528 | 7.5 | 2026-11-24 | Race condition in the Networking: HTTP component. This vulnerability was fixed in Firefox 161, Firefox ESR 153.8, Thunde |
| CVE-2026-135529 | 9.6 | 2026-11-24 | Sandbox escape in the Graphics: Text component. This vulnerability was fixed in Firefox 161, Firefox ESR 153.8, Thunderb |
| CVE-2026-135530 | 9.6 | 2026-11-24 | Sandbox escape due to incorrect boundary conditions in the Networking: HTTP component. This vulnerability was fixed in F |
| CVE-2026-135531 | 8.8 | 2026-11-24 | Privilege escalation due to use-after-free in the Networking: Cache component. This vulnerability was fixed in Firefox 1 |
| CVE-2026-135532 | 8.8 | 2026-11-24 | Use-after-free in the Networking component. This vulnerability was fixed in Firefox 161, Firefox ESR 153.8, Thunderbird  |
| CVE-2026-135533 | 8.8 | 2026-11-24 | Incorrect boundary conditions in the Layout: Tables component. This vulnerability was fixed in Firefox 161, Firefox ESR  |
| CVE-2026-135534 | 8.8 | 2026-11-24 | Use-after-free in the DOM: Core & HTML component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firef |
| CVE-2026-135535 | 8.8 | 2026-11-24 | Incorrect boundary conditions in the Graphics: Skia component. This vulnerability was fixed in Firefox 161, Firefox ESR  |
| CVE-2026-135537 | 8.8 | 2026-11-24 | Incorrect boundary conditions in the Layout: Text and Fonts component. This vulnerability was fixed in Firefox 161, Fire |
| CVE-2026-135538 | 8.8 | 2026-11-24 | Use-after-free in the Graphics: ImageLib component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Fir |
| CVE-2026-135539 | 8.8 | 2026-11-24 | Use-after-free in the DOM: CSS Object Model component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46,  |
| CVE-2026-135540 | 8.8 | 2026-11-24 | Incorrect boundary conditions in the JavaScript Engine: JIT component. This vulnerability was fixed in Firefox 161, Fire |
| CVE-2026-135541 | 8.8 | 2026-11-24 | Use-after-free in the XSLT component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firefox ESR 153.8 |
| CVE-2026-135542 | 8.8 | 2026-11-24 | Incorrect boundary conditions in the Layout: Text and Fonts component. This vulnerability was fixed in Firefox 161, Fire |
| CVE-2026-135546 | 8.8 | 2026-11-24 | Privilege escalation due to incorrect boundary conditions in the Layout: Text and Fonts component. This vulnerability wa |
| CVE-2026-135547 | 9.6 | 2026-11-24 | Sandbox escape due to incorrect boundary conditions in the DOM: Networking component. This vulnerability was fixed in Fi |
| CVE-2026-135548 | 8.8 | 2026-11-24 | Use-after-free in the Layout component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firefox ESR 153 |
| CVE-2026-135549 | 8.8 | 2026-11-24 | Use-after-free in the XSLT component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firefox ESR 153.8 |
| CVE-2026-135551 | 8.8 | 2026-11-24 | Use-after-free in the Layout component. This vulnerability was fixed in Firefox 161, Firefox ESR 153.8, Thunderbird 161, |
| CVE-2026-135552 | 8.8 | 2026-11-24 | Use-after-free in the Graphics: Canvas2D component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Fir |
| CVE-2026-135553 | 8.8 | 2026-11-24 | Use-after-free in the DOM: Core & HTML component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firef |
| CVE-2026-135554 | 8.8 | 2026-11-24 | Use-after-free in the DOM: Navigation component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firefo |
| CVE-2026-135555 | 8.8 | 2026-11-24 | Use-after-free in the XML component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firefox ESR 153.8, |
| CVE-2026-135557 | 8.8 | 2026-11-24 | Use-after-free in the JavaScript Engine component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Fire |
| CVE-2026-135560 | 8.8 | 2026-11-24 | Use-after-free in the Gecko Profiler component. This vulnerability was fixed in Firefox 161, Firefox ESR 115.46, Firefox |
| CVE-2026-135565 | 8.8 | 2026-11-24 | Use-after-free in the Graphics component. This vulnerability was fixed in Firefox 161, Firefox ESR 153.8, Thunderbird 16 |
| CVE-2026-135566 | 8.8 | 2026-11-24 | Use-after-free in the JavaScript Engine: JIT component. This vulnerability was fixed in Firefox 161 and Thunderbird 161. |
| CVE-2026-135568 | 8.8 | 2026-11-24 | Use-after-free in the Graphics: CanvasWebGL component. This vulnerability was fixed in Firefox 161, Firefox ESR 153.8, T |
| CVE-2026-135570 | 8.8 | 2026-11-24 | Use-after-free in the DOM: Workers component. This vulnerability was fixed in Firefox 161, Firefox ESR 153.8, Thunderbir |
| CVE-2026-135571 | 9.6 | 2026-11-24 | Sandbox escape due to use-after-free in the Panning and Zooming component. This vulnerability was fixed in Firefox 161,  |
| CVE-2026-135574 | 8.8 | 2026-11-24 | Incorrect boundary conditions in the JavaScript Engine component. This vulnerability was fixed in Firefox 161 and Thunde |
| CVE-2026-135575 | 8.8 | 2026-11-24 | Use-after-free in the Cycle Collector component. This vulnerability was fixed in Firefox 161 and Thunderbird 161. |
| CVE-2026-135578 | 9.6 | 2026-11-24 | Sandbox escape due to use-after-free in the Machine Learning: On Device component. This vulnerability was fixed in Firef |
| CVE-2026-135579 | 8.8 | 2026-11-24 | Privilege escalation due to incorrect boundary conditions in the Graphics component. This vulnerability was fixed in Fir |
| CVE-2026-135580 | 8.8 | 2026-11-24 | Use-after-free in the JavaScript: WebAssembly component. This vulnerability was fixed in Firefox 161 and Thunderbird 161 |
| CVE-2026-135581 | 8.8 | 2026-11-24 | Use-after-free in the Audio/Video: Playback component. This vulnerability was fixed in Firefox 161, Firefox ESR 153.8, T |
| CVE-2026-135582 | 9.6 | 2026-11-24 | Sandbox escape due to use-after-free in the Networking: HTTP component. This vulnerability was fixed in Firefox 161 and  |
| CVE-2026-135583 | 8.8 | 2026-11-24 | Use-after-free in the Networking: DNS component. This vulnerability was fixed in Firefox 161 and Thunderbird 161. |
| CVE-2026-135584 | 7.5 | 2026-11-24 | Race condition in the Graphics component. This vulnerability was fixed in Firefox 161, Firefox ESR 153.8, Thunderbird 16 |
| CVE-2026-135585 | 8.8 | 2026-11-24 | Use-after-free in the Layout: Scrolling and Overflow component. This vulnerability was fixed in Firefox 161, Firefox ESR |
| CVE-2026-135588 | 8.8 | 2026-11-24 | Use-after-free in the DOM: UI Events & Focus Handling component. This vulnerability was fixed in Firefox 161, Firefox ES |
| CVE-2026-135590 | 8.8 | 2026-11-24 | Use-after-free in the Storage: Cache API component. This vulnerability was fixed in Firefox 161, Firefox ESR 153.8, Thun |
| CVE-2026-135591 | 8.8 | 2026-11-24 | Incorrect boundary conditions in the Widget: Gtk component. This vulnerability was fixed in Firefox 161 and Thunderbird  |
| CVE-2026-135593 | 8.8 | 2026-11-24 | Incorrect boundary conditions in the Widget component. This vulnerability was fixed in Firefox 161 and Thunderbird 161. |
| CVE-2026-135596 | 9.6 | 2026-11-24 | Sandbox escape due to incorrect boundary conditions in the Graphics: WebRender component. This vulnerability was fixed i |
| CVE-2026-135597 | 9.6 | 2026-11-24 | Sandbox escape due to use-after-free in the DOM: Navigation component. This vulnerability was fixed in Firefox 161, Fire |
| CVE-2026-135600 | 8.8 | 2026-11-24 | Use-after-free in the JavaScript Engine component. This vulnerability was fixed in Firefox 161 and Thunderbird 161. |
| CVE-2026-135611 | 8.8 | 2026-11-24 | Privilege escalation in the Internationalization component. This vulnerability was fixed in Firefox ESR 153.8 and Thunde |
| CVE-2026-65135 | 9.8 | 2026-11-24 | NVIDIA Video Codec SDK for Linux contains a vulnerability where a user may cause a heap-based buffer overflow issue. A s |
| CVE-2026-65136 | 8.8 | 2026-11-24 | NVIDIA Jetson Linux for Linux contains a vulnerability where an attacker may cause an out of bounds write. A successful  |
| CVE-2026-65137 | 7.1 | 2026-11-24 | NVIDIA Jetson Linux for Linux contains a vulnerability where a local attacker may cause a NULL pointer dereference issue |
| CVE-2026-65154 | 7.8 | 2026-11-24 | NVIDIA Open GPU Kernel Module for Linux contains a vulnerability where a user may cause a use-after-free issue. A succes |
| CVE-2026-65155 | 7.5 | 2026-11-24 | NVIDIA CUDA Video Codec SDK (CUVID) for Jetson Linux contains a vulnerability where an attacker may cause a loop with an |
| CVE-2026-65156 | 7.5 | 2026-11-24 | NVIDIA CUDA Video Codec SDK for Jetson Linux contains a vulnerability where an attacker may cause an infinite loop. A su |
| CVE-2026-65157 | 7.5 | 2026-11-24 | NVIDIA Video Codec SDK for Linux contains a vulnerability where a user may cause an out of bounds read. A successful exp |
| CVE-2026-65158 | 7.5 | 2026-11-24 | NVIDIA Video Codec SDK for Linux contains a vulnerability where a user may cause a NULL pointer dereference issue. A suc |
| CVE-2026-65159 | 7.5 | 2026-11-24 | NVIDIA Video Codec SDK for Linux contains a vulnerability where a user may cause an out-of-bounds write issue. A success |
| CVE-2026-65175 | 9.8 | 2026-11-24 | NVIDIA AIStore contains a vulnerability in storage-target node-control authorization where an unauthenticated attacker c |
| CVE-2026-77670 | 7.1 | 2026-11-24 | Improper access control of a file path in TXOne StellarProtect and Stellar Agent (Windows) allows a local attacker to wr |
| CVE-2026-77671 | 7.1 | 2026-11-24 | Unverified configuration export destination path in TXOne StellarProtect and Stellar Agent (Windows) allows a local atta |
| CVE-2026-77672 | 7.8 | 2026-11-24 | Missing server-side authorization in the IPC interface of TXOne StellarProtect and Stellar Agent (Windows) allows a loca |
| CVE-2026-136132 | 8.6 | 2026-11-24 | Pangolin before 1.21.0 contains an authentication bypass vulnerability in isPathAllowed() in server/lib/pathMatch.ts tha |
| CVE-2026-136155 | 8.8 | 2026-11-24 | In Valkey 9.1.0 and 9.1.1, the Lua script debugger builds its command table once and caches it with a pointer to the Lua |
| CVE-2026-136156 | 8.8 | 2026-11-24 | In Valkey before 7.2.15, 8.0.x before 8.0.12, 8.1.x before 8.1.11, 9.0.x before 9.0.7, 9.1.x before 9.1.3 and 9.2.0-rc1, |
| CVE-2026-136157 | 7.5 | 2026-11-24 | In Valkey 8.0.x before 8.0.11, 8.1.x before 8.1.10, 9.0.x before 9.0.6 and 9.1.x before 9.1.2, the RDMA transport's pend |
| CVE-2026-136158 | 8.8 | 2026-11-24 | In Valkey JSON 1.0.0 through 1.0.2, a recursive JSONPath expression such as $..* returns both an array and elements nest |
| CVE-2026-136159 | 8.8 | 2026-11-24 | TypiCMS Core before 17.0.46 contains an insufficiently protected credentials vulnerability that allows authenticated use |
| CVE-2026-136160 | 7.8 | 2026-11-24 | Pyro through 1.9.2 contains an insecure deserialization vulnerability in ParamStoreDict.load() that calls torch.load wit |
| CVE-2026-136165 | 7.4 | 2026-11-24 | Fider before 0.40.0 contains an account takeover vulnerability that allows unauthenticated attackers to sign in as exist |
| CVE-2026-136167 | 7.8 | 2026-11-24 | vedo through 2026.6.3 contains an insecure deserialization vulnerability that allows attackers to execute code by supply |
| CVE-2026-136168 | 8.8 | 2026-11-24 | RedVector before 8.1.0 contains a hard-coded credentials vulnerability that allows unauthenticated attackers to execute  |
| CVE-2026-136170 | 7.0 | 2026-11-24 | Assimp through 6.0.6 contains a use-after-free and double free vulnerability in OpenGEXImporter.cpp because InternReadFi |
| CVE-2026-136172 | 7.0 | 2026-11-24 | Assimp through 6.0.6 contains a heap out-of-bounds write vulnerability in the OBJ exporter that allows attackers to corr |
| CVE-2026-65320 | 8.1 | 2026-11-24 | fastcore through 2.2.44 contains a path traversal vulnerability in the fastcore.xtras.untar_dir() archive extraction hel |
| CVE-2026-75582 | 7.1 | 2026-11-24 | Frappe LMS before 2.65.0 contains an improper authorization vulnerability that allows Batch Evaluators to modify any eva |
| CVE-2026-123166 | 7.2 | 2026-11-24 | SolarWinds Serv-U fails to properly sanitize user-controlled arguments, which could allow the injection of 
commands. Th |
| CVE-2026-123167 | 9.1 | 2026-11-24 | SolarWinds Serv-U is affected by a privilege escalation vulnerability that, when exploited, can allow a domain administr |
| CVE-2026-123168 | 9.1 | 2026-11-24 | SolarWinds Serv-U is affected by an insufficient 
validation vulnerability that, when exploited, could lead 
to privileg |
| CVE-2026-123172 | 9.1 | 2026-11-24 | Solarwinds Serv-U is affected by a privilege escalation vulnerability that, when exploited, could lead to the escalation |
| CVE-2026-124615 | 8.8 | 2026-11-24 | The shell command ACL for the feature scope (etc/org.apache.karaf.command.acl.feature.cfg) restricts feature:install, fe |
| CVE-2026-129833 | 7.5 | 2026-11-24 | A flaw was found in rsyslog. A remote, unauthenticated attacker can trigger a stack-based buffer overflow by sending a m |
| CVE-2026-130808 | 8.8 | 2026-11-24 | In Apache Karaf, the default command ACL configuration for the feature scope (etc/org.apache.karaf.command.acl.feature.c |
| CVE-2026-134019 | 9.8 | 2026-11-24 | PyTables is a Python package to manage extremely large amounts of data. In 3.11.1 and earlier, tables/attributeset.py tr |
| CVE-2026-134034 | 8.1 | 2026-11-24 | HortusFox is a self-hosted web application for collaborative plant management. Prior to 6.2, the toggle_boolean_value()  |
| CVE-2026-134959 | 8.8 | 2026-11-24 | Cross-Site Request Forgery (CSRF) vulnerability in Webdeclic WPMasterToolKit wpmastertoolkit allows Cross Site Request F |
| CVE-2026-135387 | 7.1 | 2026-11-24 | HortusFox is a self-hosted web application for collaborative plant management. Prior to 6.2, state-changing AdminControl |
| CVE-2026-135388 | 9.1 | 2026-11-24 | Pion DTLS is a Go implementation of Datagram Transport Layer Security. From 2.0.0 until 3.1.13, the implementation selec |
| CVE-2026-135389 | 9.1 | 2026-11-24 | Pion DTLS is a Go implementation of Datagram Transport Layer Security. From 2.1.0 until 3.1.14, a server with a SessionS |
| CVE-2026-135390 | 7.4 | 2026-11-24 | Pion DTLS is a Go implementation of Datagram Transport Layer Security. From 2.1.0 until 3.1.14, a listener performing DT |
| CVE-2026-135788 | 9.9 | 2026-11-24 | A weakness has been identified in D-Link DIR-X1860 4.5.2. Affected by this vulnerability is an unknown functionality of  |
| CVE-2026-135789 | 9.1 | 2026-11-24 | A security vulnerability has been detected in D-Link R95 101B06. Affected by this issue is the function GetBluetoothAdap |
| CVE-2026-135790 | 9.9 | 2026-11-24 | A vulnerability was detected in Panabit Smart Application Gateway TANGr7p10. This affects an unknown part of the file /c |
| CVE-2026-136177 | 7.2 | 2026-11-24 | RayLabsHQ gitea-mirror before 3.38.1 contains a server-side request forgery vulnerability that allows unauthenticated at |
| CVE-2026-136179 | 7.1 | 2026-11-24 | EpicStaff 1.2.0 before 1.3.1 contains an insecure direct object reference vulnerability in DocumentViewSet download and  |
| CVE-2026-136181 | 7.5 | 2026-11-24 | cnpmcore 3.46.0 before 3.84.3 and 4.0.0 before 4.37.3 contains an information disclosure vulnerability that allows unaut |
| CVE-2026-136183 | 8.8 | 2026-11-24 | Mercur @mercurjs/core before 2.3.2 contains a missing object-level authorization vulnerability that allows authenticated |
| CVE-2026-136184 | 9.6 | 2026-11-24 | compose-farm 0.19.0 before 1.22.0 contains a cross-site WebSocket hijacking and cross-site request forgery vulnerability |
| CVE-2026-136185 | 7.1 | 2026-11-24 | Prismor before 1.57.0 contains a wildcard CORS misconfiguration and missing authentication in its local HTTP API that al |
| CVE-2026-136187 | 8.8 | 2026-11-24 | Spug 4.0.0 before 4.1.1 contains an OS command injection vulnerability that allows any authenticated user to execute com |
| CVE-2026-136189 | 8.8 | 2026-11-24 | Schmitech ORBIT before 2.17.15 contains an improper authorization vulnerability in the permission_or_api_key dependency  |
| CVE-2026-136190 | 8.1 | 2026-11-24 | RayLabsHQ gitea-mirror before 3.38.1 contains an authorization bypass vulnerability in the /api/sso/providers handlers t |
| CVE-2026-50048 | 7.8 | 2026-11-24 | Genetec Security Center can expose access control unit credentials in plain text in server log files when specific non-d |
| CVE-2026-82168 | 7.7 | 2026-11-24 | Dell Virtual Storage Integrator for VMware vSphere Web Client, versions prior to 10.12.0.0, contains a Use of Hard-coded |
| CVE-2026-82169 | 8.3 | 2026-11-24 | Dell Virtual Storage Integrator for VMware vSphere Web Client, versions prior to 10.12.0.0, contains an OS Command Injec |
| CVE-2026-82170 | 7.7 | 2026-11-24 | Dell Virtual Storage Integrator for VMware vSphere Web Client, versions prior to 10.12.0.0, contains a Server-Side Reque |
| CVE-2026-82313 | 8.4 | 2026-11-24 | SolarWinds Serv-U is affected by a business logic 
vulnerability that may allow access to a higher privileged
account, w |
| CVE-2026-82315 | 9.1 | 2026-11-24 | SolarWinds Serv-U is affected by another Time-of-Check 
to Time-of-Use (TOCTOU) vulnerability. A user with 
domain admin |
| CVE-2026-82316 | 9.1 | 2026-11-24 | SolarWinds Serv-U is affected by a Time-of-Check to 
Time-of-Use (TOCTOU) vulnerability. A user with domain 
administrat |
| CVE-2026-82319 | 9.1 | 2026-11-24 | SolarWinds Serv-U is affected by a time-of-check to time-of-use (TOCTOU) vulnerability. A user with domain 
administrato |
| CVE-2026-82320 | 9.1 | 2026-11-24 | SolarWinds Serv-U was found to be affected by another 
type confusion vulnerability that may allow domain 
administrator |
| CVE-2026-82321 | 9.1 | 2026-11-24 | SolarWinds Serv-U was found to be affected by a type 
confusion vulnerability that may allow domain 
administrators to e |
| CVE-2026-82322 | 9.1 | 2026-11-24 | SolarWinds Serv-U is affected by an Insecure Direct Object Reference (IDOR) vulnerability that allows a domain group adm |
| CVE-2026-109484 | 10.0 | 2026-11-24 | Failure to sanitize special elements into a different plane (special element injection) in Azure App Service allows an u |
| CVE-2026-111546 | 9.1 | 2026-11-24 | Dell PowerStore contains an OS Command Injection vulnerability. An authenticated user with limited privileges could pote |
| CVE-2026-116445 | 8.8 | 2026-11-24 | Dell PowerStore SDNAS contains a local privilege-escalation vulnerability that could allow a low-privileged attacker to  |
| CVE-2026-121754 | 7.8 | 2026-11-24 | Parallels Desktop inittool2 Link Following Local Privilege Escalation Vulnerability. This vulnerability allows local att |
| CVE-2026-121756 | 8.8 | 2026-11-24 | Parallels Desktop CSHAShellExt Improper Access Control Local Privilege Escalation Vulnerability. This vulnerability allo |
| CVE-2026-123342 | 9.9 | 2026-11-24 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-123721 | 9.6 | 2026-11-24 | Adobe Campaign Classic (ACC) is affected by an Incorrect Authorization vulnerability that could result in privilege esca |
| CVE-2026-123722 | 9.9 | 2026-11-24 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-123723 | 9.9 | 2026-11-24 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-123986 | 9.9 | 2026-11-24 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-123987 | 9.9 | 2026-11-24 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-125675 | 9.9 | 2026-11-24 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-125676 | 9.9 | 2026-11-24 | Adobe Campaign Classic (ACC) is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability t |
| CVE-2026-125716 | 9.3 | 2026-11-24 | Adobe Campaign Classic (ACC) is affected by a reflected Cross-Site Scripting (XSS) vulnerability. An attacker could expl |
| CVE-2026-125717 | 9.6 | 2026-11-24 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL  |
| CVE-2026-125718 | 9.1 | 2026-11-24 | Adobe Campaign Classic (ACC) is affected by an Improper Neutralization of Special Elements used in an SQL Command ('SQL  |
| CVE-2026-125723 | 9.0 | 2026-11-24 | Adobe Campaign Classic (ACC) is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by a  |
| CVE-2026-135791 | 9.9 | 2026-11-24 | A flaw has been found in Panabit Smart Application Gateway TANGr7p10. This vulnerability affects the function edit_data_ |
| CVE-2026-135792 | 10.0 | 2026-11-24 | A vulnerability has been found in Panabit Smart Application Gateway TANGr7p10. This issue affects the function send_emai |
| CVE-2026-135793 | 9.9 | 2026-11-24 | A vulnerability was found in Panabit Smart Application Gateway TANGr7p10. Impacted is the function import_upgrde/upload_ |
| CVE-2026-119579 | 8.7 | 2026-11-24 | Adobe Experience Manager is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by a low- |
| CVE-2026-121357 | 8.7 | 2026-11-24 | Adobe Experience Manager is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by a low- |
| CVE-2026-123253 | 8.7 | 2026-11-24 | Adobe Experience Manager is affected by an Improper Neutralization of Special Elements Used in a Template Engine vulnera |
| CVE-2026-123256 | 7.1 | 2026-11-24 | Adobe Experience Manager is affected by an Incorrect Authorization vulnerability that could result in a Security feature |
| CVE-2026-123266 | 9.9 | 2026-11-24 | Adobe Experience Manager is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that  |
| CVE-2026-129959 | 8.8 | 2026-11-24 | When sftpEnabled=true (the default configuration in etc/org.apache.karaf.shell.cfg), the SSH server exposes the karaf.ba |
| CVE-2026-132877 | 9.9 | 2026-11-24 | Adobe Experience Manager is affected by an Improper Control of Generation of Code ('Code Injection') vulnerability that  |
| CVE-2026-134066 | 7.3 | 2026-11-24 | Improper neutralization of special elements in data query logic in the query construction of AWS Graph Explorer before 3 |
| CVE-2026-134068 | 7.5 | 2026-11-24 | A stack-based buffer overflow in the replication origin name parsing component in AWS pgactive before 2.1.10 might allow |
| CVE-2026-134716 | 8.8 | 2026-11-24 | Cross-Site Request Forgery (CSRF) vulnerability in Mahmudul Hasan Arif Ninja Charts ninja-charts allows Cross Site Reque |
| CVE-2026-134986 | 8.8 | 2026-11-24 | Cross-Site Request Forgery (CSRF) vulnerability in Brainstorm Force SureCart surecart allows Cross Site Request Forgery. |
| CVE-2026-135794 | 9.9 | 2026-11-24 | A vulnerability was determined in Panabit Smart Application Gateway TANGr7p10. The affected element is the function add_ |
| CVE-2026-135796 | 9.9 | 2026-11-24 | A vulnerability was determined in Volans NGFW Next-Generation Firewall r5.1. This issue affects the function exec/system |
| CVE-2026-135797 | 10.0 | 2026-11-24 | A vulnerability was identified in Volans NGFW Next-Generation Firewall r5.1. Impacted is the function exec of the file s |
| CVE-2026-135798 | 7.3 | 2026-11-24 | A security flaw has been discovered in Volans NGFW Next-Generation Firewall r5.1. The affected element is an unknown fun |
| CVE-2026-136404 | 9.8 | 2026-11-24 | ntop n2n supernode 3.0 through 3.1.1 contains a stack-based buffer overflow vulnerability that allows remote unauthentic |
| CVE-2026-136410 | 9.0 | 2026-11-24 | Thymeleaf before 3.1.6.RELEASE contains a restricted expression mode bypass vulnerability that allows unauthenticated re |
| CVE-2026-136411 | 9.8 | 2026-11-24 | BusyBox through 1.38.0 contains an absolute path traversal vulnerability in tftpd that allows unauthenticated remote att |
| CVE-2026-136412 | 8.1 | 2026-11-24 | OpenResty stream-lua-nginx-module before 0.0.20rc4 contains a use-after-free vulnerability that allows remote peers to t |
| CVE-2026-136422 | 7.8 | 2026-11-24 | Soda PDF Desktop PDF File Parsing Memory Corruption Remote Code Execution Vulnerability. This vulnerability allows remot |
| CVE-2026-136423 | 7.8 | 2026-11-24 | Soda PDF Desktop PDF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability allows rem |
| CVE-2026-136424 | 7.8 | 2026-11-24 | Soda PDF Desktop PDF File Parsing Memory Corruption Remote Code Execution Vulnerability. This vulnerability allows remot |
| CVE-2026-136425 | 7.8 | 2026-11-24 | Soda PDF Desktop App Object Use-After-Free Remote Code Execution Vulnerability. This vulnerability allows remote attacke |
| CVE-2026-136426 | 7.8 | 2026-11-24 | PyTorch Foundation PyTorch PT2 File Parsing Code Injection Remote Code Execution Vulnerability. This vulnerability allow |
| CVE-2026-136427 | 7.8 | 2026-11-24 | PyTorch Foundation PyTorch AOTIModelPackageLoader Command Injection Remote Code Execution Vulnerability. This vulnerabil |
| CVE-2026-136428 | 7.8 | 2026-11-24 | PyTorch Foundation PyTorch load_compiled_function Deserialization of Untrusted Data Remote Code Execution Vulnerability. |
| CVE-2026-136429 | 7.0 | 2026-11-24 | PyTorch Foundation PyTorch PT2 File Parsing Exposed Dangerous Method Remote Code Execution Vulnerability. This vulnerabi |
| CVE-2026-136430 | 7.8 | 2026-11-24 | PyTorch Foundation PyTorch AOTIModelPackageLoader  Directory Traversal Remote Code Execution Vulnerability. This vulnera |
| CVE-2026-136431 | 7.8 | 2026-11-24 | PyTorch Foundation PyTorch load_state_dict_from_url Deserialization of Untrusted Data Remote Code Execution Vulnerabilit |
| CVE-2026-136432 | 7.8 | 2026-11-24 | PyTorch Foundation PyTorch FileSystemReader Deserialization of Untrusted Data Remote Code Execution Vulnerability. This  |
| CVE-2026-136433 | 7.8 | 2026-11-24 | PyTorch Foundation PyTorch torch_save_to_dcp Deserialization of Untrusted Data Remote Code Execution Vulnerability. This |
| CVE-2026-136434 | 9.8 | 2026-11-24 | Super Magic PHPSandbox Command Injection Sandbox Escape Vulnerability. This vulnerability allows remote attackers to byp |
| CVE-2026-136435 | 7.8 | 2026-11-24 | DeepSpeed InferenceEngine Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerability allo |
| CVE-2026-136436 | 7.8 | 2026-11-24 | DeepSpeed torch_checkpoint_engine Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerabil |
| CVE-2026-136437 | 7.8 | 2026-11-24 | DeepSpeed parse_optim_states Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerability a |
| CVE-2026-136438 | 7.8 | 2026-11-24 | DeepSpeed build_engine_from_ds_checkpoint Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vu |
| CVE-2026-136439 | 7.8 | 2026-11-24 | DeepSpeed _get_zero_stage Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerability allo |
| CVE-2026-136440 | 7.3 | 2026-11-24 | Python Packaging Authority pip Configuration File Incorrect Permission Assignment Local Privilege Escalation Vulnerabili |
| CVE-2026-136441 | 9.8 | 2026-11-24 | Bytebase DBHub MCP Incorrect Authorization Authentication Bypass Vulnerability. This vulnerability allows remote attacke |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-132224 | Optimizely / Web Experimentation | 2026-11-24 | 2026-11-27 | Unknown |
| CVE-2026-131914 | Idunno / AntiCsrf | 2026-11-24 | 2026-11-27 | Unknown |
| CVE-2026-132165 | Drupal / Core | 2026-11-24 | 2026-11-27 | Unknown |
| CVE-2026-133968 | Project MONAI / MONAI Label | 2026-11-23 | 2026-11-26 | Unknown |
| CVE-2026-134624 | N-able / MailAssure | 2026-11-23 | 2026-11-26 | Unknown |
| CVE-2026-129448 | Apache / Roller | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2026-123890 | Broadcom / VMware vCenter | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2025-42884 | SAP / NetWeaver | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2026-76466 | Cisco / Expressway Series | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2024-10441 | Synology / DiskStation Manager (DSM) | 2026-11-18 | 2026-11-21 | Known |
| CVE-2026-40217 | BerriAI / LiteLLM | 2026-11-18 | 2026-12-02 | Unknown |
| CVE-2026-90817 | Vanderbilt University / Research Electronic Data Capture (REDCap) | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-90436 | Apache / Axis | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-115731 | Perforce / Puppet Enterprise | 2026-11-17 | 2026-12-01 | Unknown |

---

*Total entries in CISA KEV catalog: 1795*