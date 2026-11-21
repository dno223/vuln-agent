# Vulnerability Intelligence Report

**Date:** 2026-11-21  
**Generated:** 2026-11-21T15:54:50Z  

---

## Executive Summary

Our environment faces significant exposure across 120 high-severity vulnerabilities, including critical flaws in widely deployed platforms such as WordPress, Kubernetes, and CRM systems. Nine new entries were added to CISA's Known Exploited Vulnerabilities catalog this week, targeting Apache Roller, VMware vCenter, SAP NetWeaver, Cisco Expressway, and Synology DSM — all of which represent active, real-world exploitation. No monitored CVEs currently overlap with the KEV catalog, but the volume and diversity of high-severity findings demand immediate prioritization. Key risks include privilege escalation, unauthorized data access, authentication bypass, and account takeover. Coordinated patching and exposure reduction are urgently required.

---

## Risk Narrative

The current threat landscape reflects a convergence of opportunistic and targeted attacks against infrastructure, cloud, and application-layer systems. Active exploitation of VMware vCenter and SAP NetWeaver — both high-value enterprise targets — signals advanced threat actors probing perimeter and internal systems. The breadth of high-severity CVEs across low-code platforms, WordPress plugins, CRM tools, and Kubernetes infrastructure indicates a wide attack surface. Business risks include unauthorized data exfiltration, ransomware staging via compromised infrastructure, regulatory non-compliance, and reputational harm from account takeovers. The absence of monitored CVE matches in the KEV catalog is a limited positive, but the nine newly cataloged entries demand urgent response to prevent imminent compromise.

---

## Prioritized Action Items

1. Immediately patch or isolate systems running Apache Roller, VMware vCenter, SAP NetWeaver, Cisco Expressway, and Synology DSM due to confirmed active exploitation per CISA KEV.
2. Upgrade all Budibase self-hosted deployments to version 3.50.0 or later to remediate the unauthenticated admin initialization and privilege escalation vulnerabilities.
3. Apply the GiveWP WordPress plugin update immediately to eliminate the donor account takeover vulnerability affecting all versions up to the latest patched release.
4. Audit and restrict access to KubeVirt and AWS ssosync deployments, applying available patches to address privilege assignment and storage class escalation flaws.
5. Conduct a full inventory review of remaining high-severity CVEs, prioritizing those with network-accessible attack vectors and low authentication requirements for accelerated remediation.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-122244 | 7.7 | 2026-11-20 | Budibase is an open-source low-code platform. Prior to 3.50.0, a BASIC application user, or an unauthenticated visitor t |
| CVE-2026-122247 | 8.2 | 2026-11-20 | Budibase is an open-source low-code platform. Prior to 3.50.0, the public POST /api/global/users/init endpoint on a self |
| CVE-2026-132275 | 7.5 | 2026-11-20 | svglib reads SVG files and converts them to other formats. Prior to 2.3.1, the svg2rlg() renderer recursively expands ne |
| CVE-2026-133199 | 8.5 | 2026-11-20 | Incorrect privilege assignment in the user and group reconciliation logic in AWS ssosync before 2.9.5 might allow an aut |
| CVE-2026-133872 | 7.4 | 2026-11-20 | LessPass self-hosted sync server backend before commit 9469b0c lacks rate limiting on the JWT login endpoints /tokens/au |
| CVE-2026-133874 | 8.1 | 2026-11-20 | Iceburg CRM through 5.0.0 contains an incorrect authorization vulnerability in Module::saveRecord() that allows authenti |
| CVE-2026-133879 | 7.7 | 2026-11-20 | A flaw was found in KubeVirt/containerized-data-importer. When a VirtualMachine with an embedded DataVolumeTemplate carr |
| CVE-2026-79751 | 7.6 | 2026-11-20 | SportEase is a web application for managing school sports events, class rosters, and competition teams. Prior to 1.3, an |
| CVE-2026-82675 | 8.1 | 2026-11-20 | The GiveWP – Donation Plugin and Fundraising Platform plugin for WordPress is vulnerable to donor account account takeov |
| CVE-2026-104184 | 7.1 | 2026-11-20 | LinkAce is a self-hosted archive to collect website links. Prior to 2.6.0, LinkController::update() in app/Http/Controll |
| CVE-2026-133212 | 9.0 | 2026-11-20 | @fastify/reply-from is a Fastify plugin that forwards an incoming HTTP request to an upstream server. In versions before |
| CVE-2026-45354 | 7.5 | 2026-11-20 | Netatalk is a Free and Open Source file server suite for Unix-like operating systems. Prior to 4.4.3, libatalk/dsi/dsi_s |
| CVE-2026-45355 | 7.1 | 2026-11-20 | Netatalk is a Free and Open Source file server suite for Unix-like operating systems. Prior to 4.4.3, the afpd Spotlight |
| CVE-2026-45356 | 7.1 | 2026-11-20 | Netatalk is a Free and Open Source file server suite for Unix-like operating systems. Prior to 4.4.3, the afpd Spotlight |
| CVE-2026-49387 | 7.1 | 2026-11-20 | Netatalk is a Free and Open Source file server suite for Unix-like operating systems. From 3.1.0 until 4.5.0, the afpd F |
| CVE-2026-49388 | 7.1 | 2026-11-20 | Netatalk is a Free and Open Source file server suite for Unix-like operating systems. From 3.1.0 until 4.5.0, sl_unpack_ |
| CVE-2026-55216 | 8.1 | 2026-11-20 | Logto is the modern, open-source auth infrastructure for SaaS and AI apps. Prior to 1.46.0, social account linking can u |
| CVE-2026-77309 | 8.8 | 2026-11-20 | AIT GUI provides a framework for building custom websites for real-time telemetry monitoring, commanding, and other miss |
| CVE-2026-77350 | 7.3 | 2026-11-20 | pmo-platform is a modular PMO and release-management platform for Claude Code. Prior to 3.69.1, core/hooks/block-credent |
| CVE-2026-84693 | 8.1 | 2026-11-20 | The WPvivid — Backup, Migration & Staging plugin for WordPress is vulnerable to Arbitrary File Deletion in version up to |
| CVE-2026-95826 | 7.5 | 2026-11-20 | The SMSC911x/LAN9220 Ethernet driver stages every outgoing frame in a fixed-size static buffer before pushing it to the  |
| CVE-2026-125132 | 8.6 | 2026-11-20 | libumqtt is vulnerable to an integer underflow which may allow a remote attacker to cause a denial of service, memory co |
| CVE-2026-125273 | 9.6 | 2026-11-20 | No replay or command-integrity protection. Commands lack sequence numbers, nonces, or session tokens; captured commands  |
| CVE-2026-129007 | 7.1 | 2026-11-20 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Knit Pay Knit Pay  |
| CVE-2026-129029 | 7.2 | 2026-11-20 | Server-Side Request Forgery (SSRF) vulnerability in Brainstorm Force OttoKit suretriggers allows Server Side Request For |
| CVE-2026-129033 | 7.1 | 2026-11-20 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Ays Pro Quiz Maker |
| CVE-2026-129037 | 7.1 | 2026-11-20 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Ahmad WP Job Porta |
| CVE-2026-129042 | 7.1 | 2026-11-20 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Tribulant Software |
| CVE-2026-129054 | 7.5 | 2026-11-20 | Insertion of Sensitive Information Into Sent Data vulnerability in Datasolution AcyMailing SMTP Newsletter acymailing al |
| CVE-2026-129063 | 7.1 | 2026-11-20 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Brainstorm Force S |
| CVE-2026-129995 | 8.8 | 2026-11-20 | mcp-ssh-manager is an MCP server for managing servers over SSH with human approval, an encrypted vault, and a live audit |
| CVE-2026-130601 | 7.1 | 2026-11-20 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in BdThemes Element P |
| CVE-2026-130602 | 7.1 | 2026-11-20 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in BdThemes Prime Sli |
| CVE-2026-133968 | 9.8 | 2026-11-20 | monailabel (aka MONAI Label) through 0.8.5 allows directory traversal, with resultant remote code execution, via the ima |
| CVE-2026-48118 | 8.2 | 2026-11-20 | NukeViet CMS is a multi Content Management System. Prior to 4.5.09, the Comment module accepts attacker-controlled base6 |
| CVE-2026-49259 | 8.7 | 2026-11-20 | NukeViet CMS is a multi Content Management System. From the 4.x release line until 4.5.09, a low-privileged authenticate |
| CVE-2026-54064 | 8.7 | 2026-11-20 | NukeViet CMS is a multi Content Management System. Prior to 4.5.09, a user with news-posting permission can bypass NukeV |
| CVE-2026-54065 | 8.7 | 2026-11-20 | NukeViet CMS is a multi Content Management System. Prior to 4.5.09, an authenticated administrator can submit a crafted  |
| CVE-2026-55372 | 7.2 | 2026-11-20 | NukeViet CMS is a multi Content Management System. Prior to 4.5.09, an unauthenticated attacker can submit the __serverI |
| CVE-2026-61832 | 7.5 | 2026-11-20 | NukeViet CMS is a multi Content Management System. Prior to 4.6.00, a network attacker who can alter outbound traffic to |
| CVE-2026-77324 | 7.5 | 2026-11-20 | MapServer is a system for developing web-based GIS applications. From 4.4.0 until 8.6.5, an unauthenticated remote attac |
| CVE-2026-77326 | 8.6 | 2026-11-20 | MapServer is a system for developing web-based GIS applications. From 8.2.0 until 8.6.5, an unauthenticated attacker can |
| CVE-2026-77355 | 8.8 | 2026-11-20 | isomorphic-git is a pure JavaScript implementation of Git for Node.js and browsers. Prior to 1.38.7, tree-entry validati |
| CVE-2026-86017 | 8.0 | 2026-11-20 | isomorphic-git is a pure JavaScript implementation of Git for Node.js and browsers. Prior to 1.38.8, git cherry-pick app |
| CVE-2026-94561 | 7.2 | 2026-11-20 | NukeViet CMS is a multi Content Management System. In 4.6.00, an unauthenticated attacker can place the configured domai |
| CVE-2026-94562 | 7.2 | 2026-11-20 | NukeViet CMS is a multi Content Management System. Prior to 4.6.01, a super-administrator satisfying the NV_IS_SPADMIN g |
| CVE-2026-94564 | 8.2 | 2026-11-20 | NukeViet CMS is a multi Content Management System. Prior to 4.6.01, an unauthenticated visitor can submit Contact module |
| CVE-2026-94565 | 9.3 | 2026-11-20 | NukeViet CMS is a multi Content Management System. From the 3.x release line until 4.6.01, an unauthenticated visitor ca |
| CVE-2026-94567 | 9.3 | 2026-11-20 | NukeViet CMS is a multi Content Management System. Prior to 4.5.12 and 4.6.02, an attacker with access to an SVG upload  |
| CVE-2026-94597 | 7.5 | 2026-11-20 | NukeViet CMS is a multi Content Management System. Prior to 4.5.12 and 4.6.02, an attacker who can reach an image-upload |
| CVE-2026-94598 | 8.2 | 2026-11-20 | NukeViet CMS is a multi Content Management System. From 4.5.08 until 4.5.12 and 4.6.02, an attacker can place NukeViet's |
| CVE-2026-96805 | 9.6 | 2026-11-20 | The affected products have an unauthenticated command injection, which may allow an in-range BLE device to gain access t |
| CVE-2026-114494 | 7.8 | 2026-11-20 | codebase-memory-mcp provides local code intelligence for developers and AI agents through a persistent graph and MCP too |
| CVE-2026-114495 | 7.8 | 2026-11-20 | codebase-memory-mcp provides local code intelligence for developers and AI agents through a persistent graph and MCP too |
| CVE-2026-129175 | 9.8 | 2026-11-20 | U.S Department of the Interior Unstable Slope Management Program allows an unauthenticated user to inject unauthorized S |
| CVE-2026-129176 | 8.2 | 2026-11-20 | U.S Department of the Interior Unstable Slope Management Program accepts a POST request from an unauthenticated user, wi |
| CVE-2026-129177 | 7.5 | 2026-11-20 | U.S Department of the Interior Unstable Slope Management Program contains a vulnerable endpoint that allows an unauthent |
| CVE-2026-129179 | 8.1 | 2026-11-20 | U.S Department of the Interior Unstable Slope Management Program allows attackers with valid local application credentia |
| CVE-2026-129998 | 7.3 | 2026-11-20 | MaxKB is an open-source AI assistant for enterprise. Prior to 2.10.7-lts, custom Tool Init Param definitions accept atta |
| CVE-2026-133680 | 9.9 | 2026-11-20 | A vulnerability was found in D-Link DCS-935L 1.10.01. This affects the function loginRouter of the file web/cgi-bin/loca |
| CVE-2026-134035 | 7.8 | 2026-11-20 | Krita JC2 File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote  |
| CVE-2026-134036 | 7.8 | 2026-11-20 | Krita ABR File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote  |
| CVE-2026-134037 | 7.8 | 2026-11-20 | Krita ASL File Parsing Integer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote attackers  |
| CVE-2026-134038 | 7.8 | 2026-11-20 | Krita PSB File Parsing Integer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote attackers  |
| CVE-2026-134039 | 7.8 | 2026-11-20 | Krita TIFF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability allows remote attack |
| CVE-2026-134040 | 7.8 | 2026-11-20 | Krita HEIC File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote |
| CVE-2026-134041 | 7.8 | 2026-11-20 | Krita EXR File Parsing Integer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote attackers  |
| CVE-2026-134042 | 7.8 | 2026-11-20 | Krita HEIC File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability. This vulnerability allows remote attack |
| CVE-2026-134043 | 7.8 | 2026-11-20 | Krita TIF File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows remote  |
| CVE-2026-134052 | 8.8 | 2026-11-20 | Open Robotics RViz fillIndexBuffer Heap-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability al |
| CVE-2026-19776 | 7.8 | 2026-11-20 | G DATA Total Security TSNxGService Link Following Local Privilege Escalation Vulnerability. This vulnerability allows lo |
| CVE-2026-19779 | 7.3 | 2026-11-20 | G DATA Total Security Backup Service Uncontrolled Search Path Element Local Privilege Escalation Vulnerability. This vul |
| CVE-2026-54039 | 8.1 | 2026-11-20 | LibreChat is an enhanced ChatGPT clone that supports multiple AI providers. From 0.7.0 until 0.8.6, when local registrat |
| CVE-2026-54044 | 7.7 | 2026-11-20 | LibreChat is an enhanced ChatGPT clone that supports multiple AI providers. Prior to 0.8.7, POST /api/agents/actions/:ag |
| CVE-2026-133835 | 7.3 | 2026-11-20 | A flaw has been found in hankcs HanLP up to 2.1.6. Impacted is the function uncompress of the file hanlp/utils/io_util.p |
| CVE-2026-134164 | 7.5 | 2026-11-20 | probe-image-size before 7.5.0 contains an algorithmic-complexity denial of service vulnerability in lib/exif_utils.js th |
| CVE-2026-134167 | 7.5 | 2026-11-20 | devpi-web before 5.2.0 contains an unauthenticated path traversal vulnerability in the +doc documentation route because  |
| CVE-2026-134169 | 7.5 | 2026-11-20 | Qwik City before 1.20.3 (@builder.io/qwik-city) and @qwik.dev/router before 2.0.0-rc.4 contain an improperly controlled  |
| CVE-2026-134172 | 7.8 | 2026-11-20 | audio-separator before 0.47.2 contains an insecure deserialization vulnerability that allows attackers to execute code b |
| CVE-2026-19793 | 8.8 | 2026-11-21 | The WP Import Export Lite plugin for WordPress is vulnerable to Limited Code Injection in all versions up to, and includ |
| CVE-2026-120539 | 9.8 | 2026-11-21 | The Restrictions for BuddyPress plugin for WordPress is vulnerable to Remote Code Execution in all versions up to, and i |
| CVE-2026-123086 | 8.1 | 2026-11-21 | The PublishPress Revisions: Duplicate Posts, Submit, Approve and Schedule Content Changes plugin for WordPress is vulner |
| CVE-2026-129220 | 8.8 | 2026-11-21 | The Everest Forms – Contact Form, Payment Form, Quiz, Survey & Custom Form Builder with AI plugin for WordPress is vulne |
| CVE-2026-107713 | 7.2 | 2026-11-21 | The Flutterwave Payments plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'form_id' parameter i |
| CVE-2026-116619 | 7.2 | 2026-11-21 | The MetForm – Contact Form, Survey, Quiz, Conditional Forms, Form Templates & Custom Form Builder for Elementor plugin f |
| CVE-2026-119632 | 7.2 | 2026-11-21 | The Forminator Forms – Contact Form, Payment Form & Custom Form Builder plugin for WordPress is vulnerable to Stored Cro |
| CVE-2026-120485 | 7.2 | 2026-11-21 | The Admin Columns plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'url' parameter in all versi |
| CVE-2026-120529 | 7.2 | 2026-11-21 | The Admin Columns plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'HTTP_USER_AGENT' parameter  |
| CVE-2026-120676 | 7.2 | 2026-11-21 | The Forminator Forms – Contact Form, Payment Form & Custom Form Builder plugin for WordPress is vulnerable to Stored Cro |
| CVE-2026-125039 | 7.2 | 2026-11-21 | The EZ SQL Reports Shortcode Widget and DB Backup plugin for WordPress is vulnerable to Stored Cross-Site Scripting via  |
| CVE-2026-126011 | 7.2 | 2026-11-21 | The Photo Gallery, Sliders, Proofing and Themes – NextGEN Gallery plugin for WordPress is vulnerable to Stored Cross-Sit |
| CVE-2026-131822 | 7.2 | 2026-11-21 | The Contact Form to Any API plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'your-message (any |
| CVE-2026-132620 | 7.2 | 2026-11-21 | The WPBot – AI ChatBot for WordPress & Growth Suite: SEO, AI Writer, Email Marketing, Social Media plugin for WordPress  |
| CVE-2026-133361 | 7.2 | 2026-11-21 | The BlockStrap Page Builder – Bootstrap Blocks plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the |
| CVE-2026-96991 | 7.2 | 2026-11-21 | The SchemaEngine AI – AI Schema Markup, Reviews & Rich Snippets for SEO plugin for WordPress is vulnerable to Stored Cro |
| CVE-2026-125054 | 7.2 | 2026-11-21 | The SiteOrigin CSS plugin for WordPress is vulnerable to Stored DOM-Based Cross-Site Scripting via the 'class' parameter |
| CVE-2026-107632 | 7.2 | 2026-11-21 | The Unbounce Landing Pages plugin for WordPress is vulnerable to Stored Cross-Site Scripting in versions up to, and incl |
| CVE-2026-118049 | 8.1 | 2026-11-21 | The Tutor LMS – eLearning and online course solution plugin for WordPress is vulnerable to authorization bypass in all v |
| CVE-2026-118061 | 7.2 | 2026-11-21 | The VikBooking Hotel Booking Engine & PMS plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'inq |
| CVE-2026-119061 | 7.2 | 2026-11-21 | The VikBooking Hotel Booking Engine & PMS plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'vbf |
| CVE-2026-119114 | 7.4 | 2026-11-21 | The WP Fastest Cache – WordPress Cache Plugin plugin for WordPress is vulnerable to arbitrary directory deletion due to  |
| CVE-2026-120526 | 7.2 | 2026-11-21 | The WCFM Membership – WooCommerce Memberships for Multivendor Marketplace plugin for WordPress is vulnerable to Stored C |
| CVE-2026-122230 | 7.2 | 2026-11-21 | The Thim Kit for Elementor – Pre-built Templates & Widgets for Elementor plugin for WordPress is vulnerable to Stored DO |
| CVE-2026-131609 | 7.2 | 2026-11-21 | The Germanized for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'billing_addres |
| CVE-2026-133367 | 7.2 | 2026-11-21 | The WPC Frequently Bought Together for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via |
| CVE-2026-107654 | 7.5 | 2026-11-21 | The One to one user Chat by WPGuppy plugin for WordPress is vulnerable to generic SQL Injection via the 'userId' paramet |
| CVE-2026-116518 | 7.2 | 2026-11-21 | The ElasticPress plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'orderby' parameter in all ve |
| CVE-2026-120736 | 7.2 | 2026-11-21 | The AutomatorWP – No-Code Workflow Automation, Integration & Webhooks Plugin, now with AI plugin for WordPress is vulner |
| CVE-2026-120745 | 7.2 | 2026-11-21 | The Paid Membership Plugin, Ecommerce, User Registration Form, Login Form, User Profile & Restrict Content – ProfilePres |
| CVE-2026-123830 | 7.2 | 2026-11-21 | The wpForo Forum plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'data[display_name]' paramete |
| CVE-2026-124216 | 7.2 | 2026-11-21 | The Orphans plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'comment' parameter in all version |
| CVE-2026-124976 | 7.2 | 2026-11-21 | The Swift Performance Lite plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the '<attacker-chosen p |
| CVE-2026-130323 | 7.2 | 2026-11-21 | The Accept Stripe Payments plugin for WordPress is vulnerable to Stored DOM-Based Cross-Site Scripting via the 'href of  |
| CVE-2026-129794 | 8.8 | 2026-11-21 | The EoE fragment reassembly code uses a frame size from the wire as the bound for memcpy into the application receive bu |
| CVE-2026-129796 | 8.8 | 2026-11-21 | The CoE SDO download handler for flexible-length objects (VISIBLE_STRING, OCTET_STRING, and similar) does not check that |
| CVE-2026-129797 | 8.8 | 2026-11-21 | SDO_downloadsegment is called whenever a mailbox frame carries the DOWNLOADSEGREQ command byte, regardless of whether a  |
| CVE-2026-129798 | 8.8 | 2026-11-21 | The CoE SDO segmented download handler advances a write pointer by each incoming segment's size but does not track how m |
| CVE-2026-129801 | 7.1 | 2026-11-21 | The FoE DATA frame handler computes the payload length from the master-supplied mailbox length field and passes it direc |
| CVE-2026-129811 | 8.8 | 2026-11-21 | The PDO mapping bit lengths stored in the mapping objects are writable by the master via SDO. sizeOfPDO summed them with |
| CVE-2026-133983 | 7.3 | 2026-11-21 | A vulnerability was detected in eigent-ai eigent up to 1.0.2. Affected by this vulnerability is an unknown functionality |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-129448 | Apache / Roller | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2026-123890 | Broadcom / VMware vCenter | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2025-42884 | SAP / NetWeaver | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2026-76466 | Cisco / Expressway Series | 2026-11-20 | 2026-11-23 | Unknown |
| CVE-2024-10441 | Synology / DiskStation Manager (DSM) | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-40217 | BerriAI / LiteLLM | 2026-11-18 | 2026-12-02 | Unknown |
| CVE-2026-90817 | Vanderbilt University / Research Electronic Data Capture (REDCap) | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-90436 | Apache / Axis | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-115731 | Perforce / Puppet Enterprise | 2026-11-17 | 2026-12-01 | Unknown |

---

*Total entries in CISA KEV catalog: 1790*