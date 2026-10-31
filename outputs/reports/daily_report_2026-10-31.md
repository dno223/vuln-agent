# Vulnerability Intelligence Report

**Date:** 2026-10-31  
**Generated:** 2026-10-31T14:18:21Z  

---

## Executive Summary

Our environment faces significant exposure from 176 high-severity CVEs, including multiple critical flaws scoring 9.8 CVSS. Key risks include authentication bypasses, hardcoded credentials, privilege escalation, SQL injection, and insecure password reset functions across CMS platforms, e-commerce tools, and learning management systems. Ten new CISA Known Exploited Vulnerability entries were added this week, covering Ivanti Connect Secure, GitLab, Cisco ASA, and VMware ESX — all actively exploited in the wild. While no monitored CVEs currently match the KEV catalog, the volume and severity of new vulnerabilities demand immediate prioritization and remediation action.

---

## Risk Narrative

The current threat landscape reflects a sharp rise in exploitation of CMS, LMS, and network security platforms. Attackers are actively targeting authentication weaknesses, hardcoded credentials, and privilege escalation paths — attack vectors that require little sophistication and offer immediate access to sensitive data and admin controls. The five new CISA KEV entries signal that nation-state and ransomware actors are weaponizing flaws in widely deployed enterprise tools. Unpatched SQL injection and unauthorized API access vulnerabilities further expand the attack surface. Business risks include data breaches, regulatory penalties, operational disruption, and reputational damage. The volume of high-severity CVEs without KEV overlap today does not reduce risk — it signals emerging threats that could enter active exploitation imminently.

---

## Prioritized Action Items

1. Immediately audit and patch Ivanti Connect Secure, GitLab, Cisco ASA, and VMware ESX systems against the five newly added CISA KEV entries, as these are confirmed to be actively exploited.
2. Remediate the two critical CVSS 9.8 vulnerabilities in MuseBot and Vvveb CMS by upgrading to patched versions, prioritizing the hardcoded-credential authentication bypass and broken password reset flaws.
3. Address the CVSS 9.0 Vvveb IDOR vulnerability and the CVSS 8.9 DataCap privilege escalation flaw to prevent authenticated users from gaining unauthorized administrative access.
4. Eliminate unauthenticated SQL injection vulnerabilities in CoreShop endpoints immediately by applying vendor patches or implementing WAF rules as an interim control.
5. Establish a weekly vulnerability review process to monitor new KEV catalog additions and ensure all 176 high-severity CVEs are tracked through a formal remediation SLA.
6. Conduct a full inventory of all CMS and LMS platforms in use, including DedeCMS, Chamilo, and Orchard CMS, to assess exposure and apply outstanding security patches.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2010-20125 | 7.5 | 2026-10-30 | DedeCMS before 5.7 contains a file inclusion vulnerability in plus/carbuyaction.php that allows remote unauthenticated a |
| CVE-2026-110799 | 9.8 | 2026-10-30 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to version |
| CVE-2026-112905 | 9.0 | 2026-10-30 | Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to version |
| CVE-2026-119649 | 7.1 | 2026-10-30 | Orchard CMS 1.10.3 through 1.11 contains an improper authorization vulnerability in MediaLibraryService.CheckMediaFolder |
| CVE-2026-119654 | 8.8 | 2026-10-30 | DataCap through 2025.1.1 contains a missing authorization vulnerability that allows any authenticated user to escalate p |
| CVE-2026-119655 | 7.5 | 2026-10-30 | CoreShop through 1.5.5 contains an unauthenticated sql injection vulnerability in the api/Good/GetGoodsPageList endpoint |
| CVE-2026-119656 | 7.5 | 2026-10-30 | CoreShop by CoreUnion through 1.5.5 contains an unauthenticated sql injection vulnerability in the api/Agent/GetGoodsPag |
| CVE-2026-119660 | 9.8 | 2026-10-30 | MuseBot before 2.0.0 contains an authentication bypass vulnerability that allows unauthenticated attackers to forge admi |
| CVE-2026-119662 | 8.8 | 2026-10-30 | Songloft 2.9.0 before 2.13.6 contains a hardcoded credentials vulnerability that allows adjacent network attackers to au |
| CVE-2026-45144 | 8.9 | 2026-10-30 | Chamilo LMS is an open-source learning management system. From 2.0.0 until 2.0.1, `GET /user/{username}` is anonymously  |
| CVE-2026-45145 | 7.5 | 2026-10-30 | Chamilo LMS is an open-source learning management system. Prior to 2.0.1, `public/main/inc/lib/career.lib.php` and `publ |
| CVE-2026-61708 | 8.5 | 2026-10-30 | SOCFortress CoPilot focuses on providing a single pane of glass for all your security operations needs. Prior to 0.1.76, |
| CVE-2026-61728 | 9.9 | 2026-10-30 | SOCFortress CoPilot focuses on providing a single pane of glass for all your security operations needs. In affected snap |
| CVE-2026-61729 | 9.4 | 2026-10-30 | SOCFortress CoPilot focuses on providing a single pane of glass for all your security operations needs. Prior to 0.1.76, |
| CVE-2026-61730 | 9.3 | 2026-10-30 | SOCFortress CoPilot focuses on providing a single pane of glass for all your security operations needs. In affected depl |
| CVE-2026-61737 | 9.8 | 2026-10-30 | ng-antd-admin is an Angular and NestJS administration system template. Prior to 22.0, a hardcoded default `JWT` secret p |
| CVE-2026-61738 | 10.0 | 2026-10-30 | SOCFortress CoPilot focuses on providing a single pane of glass for all your security operations needs. Prior to 0.1.77, |
| CVE-2026-61739 | 7.5 | 2026-10-30 | SOCFortress CoPilot focuses on providing a single pane of glass for all your security operations needs. Prior to 0.1.77, |
| CVE-2026-104061 | 7.8 | 2026-10-30 | Scribus before 1.6.7 contains a heap out-of-bounds write vulnerability in the scimgdataloader_psd loader that uses unche |
| CVE-2026-104062 | 7.8 | 2026-10-30 | Scribus before 1.6.7 contains a heap buffer overflow vulnerability in the PICT image loader and import plugin that allow |
| CVE-2026-104064 | 7.8 | 2026-10-30 | Scribus before 1.6.7 contains an integer overflow vulnerability in the scimgdataloader_tiff TIFF loader that allows atta |
| CVE-2026-104065 | 7.8 | 2026-10-30 | Scribus before 1.6.7 contains an out-of-bounds write vulnerability in the importdrw Micrografx Draw plugin that uses an  |
| CVE-2026-104066 | 7.8 | 2026-10-30 | Scribus before 1.6.7 contains a heap buffer overflow vulnerability in the Mac PICT image loader and import plugin when u |
| CVE-2026-104067 | 7.8 | 2026-10-30 | Scribus before 1.6.7 contains an out-of-bounds memory access vulnerability in the importsvm plugin that fails to verify  |
| CVE-2026-104615 | 7.9 | 2026-10-30 | A security vulnerability was discovered in SUSE Rancher Fleet's cluster registration flow, in Fleet versions before 0.12 |
| CVE-2026-118238 | 7.2 | 2026-10-30 | The Tenda W18E web management server is vulnerable to OS command injection via the "diagnose" packet-capture feature due |
| CVE-2026-119287 | 8.0 | 2026-10-30 | Zuke is a code-first, strongly typed build automation system for Deno. Prior to 1.51.0, the @zuke/core MCP registry mode |
| CVE-2026-119288 | 7.0 | 2026-10-30 | Zuke is a code-first, strongly typed build automation system for Deno. Prior to 1.51.0, @zuke/core launches resolved Win |
| CVE-2026-119289 | 7.1 | 2026-10-30 | Zuke is a code-first, strongly typed build automation system for Deno. Prior to 1.10.0, the @zuke/gh githubWorkflow(...) |
| CVE-2026-119290 | 7.5 | 2026-10-30 | Zuke is a code-first, strongly typed build automation system for Deno. Prior to 1.51.0, @zuke/core writes rendered repor |
| CVE-2026-119706 | 9.8 | 2026-10-30 | InternLM LMDeploy 0.9.0 through 0.18.0 contains an unauthenticated remote code execution vulnerability that allows remot |
| CVE-2026-119707 | 7.1 | 2026-10-30 | SonicJS through 3.0.0 contains a missing authorization vulnerability in the /api/:collection and /api/content write rout |
| CVE-2026-119710 | 7.1 | 2026-10-30 | PipesHub 0.3.0 before 0.10.0 contains an event type injection vulnerability that allows authenticated users with only th |
| CVE-2026-119713 | 8.8 | 2026-10-30 | Paperclip 2026.403.0 before 2026.416.0 contains a remote code execution vulnerability that allows agent API key holders  |
| CVE-2026-119716 | 8.1 | 2026-10-30 | pybars3 through 0.9.7 contains a code injection vulnerability in pybars/_compiler.py that allows template authors to exe |
| CVE-2026-119717 | 8.1 | 2026-10-30 | pybars4 through 0.9.13 contains a code injection vulnerability in pybars/_compiler.py that allows attackers to execute P |
| CVE-2026-119718 | 7.8 | 2026-10-30 | Blender before 4.5.15 and 5.x before 5.2.3 contains a heap buffer overflow vulnerability caused by integer overflow in p |
| CVE-2026-119719 | 7.8 | 2026-10-30 | Blender before 4.5.15 and 5.x before 5.2.3 contains a heap buffer overflow vulnerability in the blend file thumbnail ext |
| CVE-2026-119722 | 7.8 | 2026-10-30 | Blender before 4.5.15 and 5.x before 5.2.3 contains a heap out-of-bounds access vulnerability in read_struct() that skip |
| CVE-2026-115642 | 8.3 | 2026-10-30 | In OpenStack keystonemiddleware before 13.0.2, by supplying a custom X-Service-Token header in a request, anyone in poss |
| CVE-2026-119116 | 7.8 | 2026-10-30 | A use-after-free and double-free issue in the SetClient command handler of the kmstool-enclave sample application of AWS |
| CVE-2026-61804 | 8.1 | 2026-10-30 | myTinyWMS is a free, open-source warehouse management system. Prior to version 1.6.4, `Product (Artikel)` and `Category` |
| CVE-2026-61826 | 10.0 | 2026-10-30 | Bazarr is a companion application to Sonarr and Radarr. Prior to 1.5.7-beta.14, the `api_ns_plex` namespace in `bazarr/a |
| CVE-2026-65566 | 8.8 | 2026-10-30 | Cross-Site Request Forgery (CSRF) vulnerability in Meow Apps AI Engine ai-engine allows Cross Site Request Forgery.This  |
| CVE-2025-8574 | 8.7 | 2026-10-30 | The Database Cleaner plugin for WordPress is vulnerable to arbitrary table deletion in all versions up to, and including |
| CVE-2026-104744 | 7.2 | 2026-10-30 | The Independent Analytics Pro plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'utm_campaign' p |
| CVE-2026-105894 | 8.8 | 2026-10-30 | The Ak Framework plugin for WordPress, included in the Newsy - Viral News & Magazine WordPress Theme, is vulnerable to P |
| CVE-2026-107630 | 7.5 | 2026-10-30 | The Email Templates Customizer and Designer for WordPress and WooCommerce plugin for WordPress is vulnerable to authoriz |
| CVE-2026-110305 | 7.5 | 2026-10-30 | The Advanced Custom Fields: Extended plugin for WordPress is vulnerable to Sensitive Information Exposure in all version |
| CVE-2026-112365 | 7.2 | 2026-10-30 | The easy.jobs – AI powered Job Listing, Job Board, Career Page, Recruitment & Hiring Solution plugin for WordPress is vu |
| CVE-2026-115346 | 8.1 | 2026-10-30 | The Avada \| Website Builder For WordPress & WooCommerce theme for WordPress is vulnerable to Arbitrary File Upload in ve |
| CVE-2026-118205 | 7.4 | 2026-10-30 | The Essential Addons for Elementor – Popular Elementor Templates & Widgets plugin for WordPress is vulnerable to Privile |
| CVE-2026-118696 | 8.0 | 2026-10-30 | In JetBrains IntelliJ IDEA, PyCharm, PhpStorm, RubyMine and WebStorm before 2026.3, 2026.2.4, 2026.1.5.1, and 2025.3.6.2 |
| CVE-2026-118697 | 9.0 | 2026-10-30 | In JetBrains Toolbox App before 3.9.1 and 3.8.2; IntelliJ IDEA before 2026.3 and 2026.2.4, the jetbrainsd daemon trusted |
| CVE-2026-119619 | 7.3 | 2026-10-30 | A vulnerability was found in 37954679 cak-filemanagement-system up to 5e6433246475e66462e1fea980688de96a049297. This aff |
| CVE-2026-119620 | 7.3 | 2026-10-30 | A vulnerability was determined in 37954679 cak-filemanagement-system up to 5e6433246475e66462e1fea980688de96a049297. Thi |
| CVE-2026-119760 | 7.5 | 2026-10-30 | sniproxy through 0.7.0 contains a NULL pointer dereference vulnerability in resolv_cancel() that allows remote unauthent |
| CVE-2026-119762 | 7.5 | 2026-10-30 | Axigen Mail Server before 10.5.69, 10.6.x before 10.6.40, and 10.7.x before 10.7.2 contains an unauthenticated denial of |
| CVE-2026-119777 | 7.8 | 2026-10-30 | A flaw was found in GStreamer's gst-plugins-bad H.266/VVC parser. When processing a malformed H.266 media file or stream |
| CVE-2026-119978 | 8.5 | 2026-10-30 | Flowise through 3.1.4 contains a sandbox escape vulnerability that allows authenticated users to execute OS commands by  |
| CVE-2026-119979 | 8.8 | 2026-10-30 | LM Studio before 0.4.22+1 contains a path traversal vulnerability in the model downloader's resolveDownloadRequest that  |
| CVE-2026-76012 | 7.5 | 2026-10-30 | The Photo Gallery, Sliders, Proofing and Themes – NextGEN Gallery plugin for WordPress is vulnerable to Remote Code Exec |
| CVE-2026-84243 | 7.0 | 2026-10-30 | The gettext family of functions in the GNU C Library version 2.0 and later accept LANGUAGE environment variable entries  |
| CVE-2026-96894 | 7.2 | 2026-10-30 | The ERP: Complete HR, Accounting & CRM Suite Built for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Si |
| CVE-2026-97638 | 7.5 | 2026-10-30 | The Forminator Forms – Contact Form, Payment Form & Custom Form Builder plugin for WordPress is vulnerable to Insecure D |
| CVE-2026-105077 | 7.1 | 2026-10-30 | Unauthenticated Cross Site Scripting (XSS) in Ad Inserter <= 2.8.19 versions. |
| CVE-2026-116386 | 9.8 | 2026-10-30 | Unauthenticated Privilege Escalation in SMS Alert Order Notifications <= 4.0.2 versions. |
| CVE-2026-116401 | 7.5 | 2026-10-30 | Unauthenticated Broken Access Control in HUSKY <= 1.4.6 versions. |
| CVE-2026-116405 | 7.1 | 2026-10-30 | Unauthenticated Cross Site Scripting (XSS) in VikRentCar <= 1.4.9 versions. |
| CVE-2026-116847 | 7.1 | 2026-10-30 | Unauthenticated Cross Site Scripting (XSS) in Mang Board WP <= 2.4.6 versions. |
| CVE-2026-116851 | 7.1 | 2026-10-30 | Unauthenticated Cross Site Scripting (XSS) in eCommerce Product Catalog <= 3.6.5 versions. |
| CVE-2026-116852 | 9.1 | 2026-10-30 | Author Remote Code Execution (RCE) in Widget Options <= 4.2.5 versions. |
| CVE-2026-116861 | 7.5 | 2026-10-30 | Unauthenticated Sensitive Data Exposure in Flexible Chat <= 1.1.0 versions. |
| CVE-2026-116862 | 7.5 | 2026-10-30 | Unauthenticated Broken Access Control in WP REST Cache <= 2026.3.1 versions. |
| CVE-2026-118086 | 8.8 | 2026-10-30 | Subscriber Privilege Escalation in WP BASE Booking <= 6.5.2 versions. |
| CVE-2026-118089 | 7.2 | 2026-10-30 | Shop manager PHP Object Injection in Product Feed Manager <= 7.14.1 versions. |
| CVE-2026-118090 | 8.8 | 2026-10-30 | Subscriber PHP Object Injection in MasterStudy LMS <= 3.7.55 versions. |
| CVE-2026-119526 | 9.8 | 2026-10-30 | Deserialization of Untrusted Data vulnerability in ThemeREX Royal Event allows Object Injection.

This issue affects Roy |
| CVE-2026-28160 | 7.1 | 2026-10-30 | Unauthenticated Cross Site Scripting (XSS) in VikRentCar <= 1.4.10 versions. |
| CVE-2026-39732 | 9.3 | 2026-10-30 | Unauthenticated SQL Injection in Transliterator <= 2.5.13 versions. |
| CVE-2026-39734 | 7.5 | 2026-10-30 | Unauthenticated Path Traversal in WP EasyPay <= 4.5.4 versions. |
| CVE-2026-39738 | 9.8 | 2026-10-30 | Unauthenticated PHP Object Injection in FunnelKit Automations <= 3.8.6.1 versions. |
| CVE-2026-39786 | 7.1 | 2026-10-30 | Unauthenticated Cross Site Scripting (XSS) in BA Book Everything <= 1.8.33 versions. |
| CVE-2026-46560 | 7.5 | 2026-10-30 | Open Access Management (OpenAM) is an access management solution. Prior to 16.1.1, the `RADIUS` authentication module op |
| CVE-2026-48201 | 7.1 | 2026-10-30 | Unauthenticated Cross Site Scripting (XSS) in Fast Velocity Minify <= 3.5.7 versions. |
| CVE-2026-54855 | 7.1 | 2026-10-30 | Unauthenticated Cross Site Scripting (XSS) in Profile Builder <= 4.0.5 versions. |
| CVE-2026-59978 | 7.5 | 2026-10-30 | AdminNeo is a full-featured database management tool written in PHP. From 4.6.2 until 5.5.0, the unauthenticated `?scrip |
| CVE-2026-61854 | 8.2 | 2026-10-30 | VoiceSentinel is a real-time voice moderation system for Minecraft servers. From 2.2.1 until 3.3.1, the optional report  |
| CVE-2026-62264 | 7.5 | 2026-10-30 | PDF Reader MCP is a Model Context Protocol server for reading PDF documents. In versions 2.2.0 and later prior to 3.0.1, |
| CVE-2026-62331 | 8.2 | 2026-10-30 | praktor is a multi-agent Claude Code orchestrator with Telegram input and output, Docker isolation, and a Mission Contro |
| CVE-2026-73186 | 8.8 | 2026-10-30 | Subscriber PHP Object Injection in Enable Media Replace <= 4.2.2 versions. |
| CVE-2026-78527 | 8.8 | 2026-10-30 | Contributor PHP Object Injection in GS Testimonial Slider <= 3.3.10 versions. |
| CVE-2026-90888 | 9.8 | 2026-10-30 | Unauthenticated PHP Object Injection in LeadSnap <= 1.25 versions. |
| CVE-2026-94175 | 7.1 | 2026-10-30 | Unauthenticated Cross Site Scripting (XSS) in All In One Login <= 2.4.1 versions. |
| CVE-2026-116238 | 8.1 | 2026-10-30 | In server mode pgAdmin 4 locks an internal account after MAX_LOGIN_ATTEMPTS failed logins (3 by default). The limit coul |
| CVE-2026-116239 | 8.5 | 2026-10-30 | In server mode pgAdmin 4 keeps an account per authentication source, so the same username can exist as, for example, an  |
| CVE-2026-116241 | 9.9 | 2026-10-30 | pgAdmin 4's Import/Export Data tool wraps a user's query export in a psql \copy (...) TO command and checks that the que |
| CVE-2026-116242 | 8.2 | 2026-10-30 | pgAdmin 4 opens SSH tunnels with the sshtunnel library but gave it neither host_pkey_directories nor ssh_config_file, so |
| CVE-2026-116243 | 7.5 | 2026-10-30 | pgAdmin 4 runs pg_dump, pg_restore, pg_dumpall and psql from the binary path a user sets in their preferences. In server |
| CVE-2026-116244 | 8.2 | 2026-10-30 | When a pgAdmin 4 connection was not meant to use a Kerberos user's delegated credentials, pgAdmin removed KRB5CCNAME fro |
| CVE-2026-116245 | 8.2 | 2026-10-30 | libpq looks a connection service up in the service file of the operating-system account running pgAdmin 4, and an entry  |
| CVE-2026-116247 | 8.2 | 2026-10-30 | When a server in pgAdmin 4 had no password file, client certificate or client key configured, or the configured one coul |
| CVE-2026-116249 | 8.4 | 2026-10-30 | In server mode pgAdmin 4 resolves a server's password file, SSL certificate, key, CRL and SSH tunnel identity file relat |
| CVE-2026-119331 | 7.1 | 2026-10-30 | Ladybird is a truly independent web browser. Prior to the c0d68bddf3e3616e5173835f0f4c155ee9700d91 commit, CSSStyleSheet |
| CVE-2026-119332 | 8.8 | 2026-10-30 | Ladybird is a truly independent web browser. Prior to 209579c96473c75bd5eba9701fcadb841a045964, FinalizationRegistry::cl |
| CVE-2026-119333 | 7.8 | 2026-10-30 | draw.io Desktop is the official Electron build of draw.io. Prior to 31.5.2, the Windows application launched powershell  |
| CVE-2026-119335 | 7.8 | 2026-10-30 | Pi-hole is a DNS sinkhole that protects devices from unwanted content without installing any client-side software. Prior |
| CVE-2026-119336 | 7.8 | 2026-10-30 | Pi-hole is a DNS sinkhole that protects devices from unwanted content without installing any client-side software. From  |
| CVE-2026-119337 | 7.1 | 2026-10-30 | RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine. From 0.25.2 until 0.27.3, POST /api/v1/agents/cha |
| CVE-2026-55598 | 9.1 | 2026-10-30 | PinePods is a complete, self-hosted podcast management system written in Rust. Prior to 0.9.0, an authenticated user can |
| CVE-2026-61620 | 9.8 | 2026-10-30 | HoneySQL turns Clojure data structures into SQL. From 2.0.0 until 2.7.1392, applications that pass user input or other a |
| CVE-2026-78402 | 7.8 | 2026-10-30 | Stack-based buffer overflow and out-of-bounds
write vulnerability in Thales Sentinel Keys Server on Windows allows Overf |
| CVE-2026-78403 | 9.8 | 2026-10-30 | Stack-based buffer overflow and missing
authorization vulnerability in Thales Sentinel Keys Server on Windows allows
Ove |
| CVE-2026-40573 | 8.6 | 2026-10-30 | NovumOS is a custom 32-bit operating system written in Zig and x86 Assembly. Prior to version 0.25-beta.1, the `Nova` in |
| CVE-2026-58412 | 8.2 | 2026-10-30 | Filecoin Pin is an IPFS Pinning Service API implementation that pins to Filecoin's PDP service. Prior to 1.1.0, the uplo |
| CVE-2026-62297 | 7.5 | 2026-10-30 | ag-psd is a JavaScript library for reading and writing Photoshop Document files. Before the allocation-limit remediation |
| CVE-2026-62847 | 8.2 | 2026-10-30 | Metalama is a Roslyn-based open-source patterns and architecture toolkit for C#. Prior to 2025.1.18, 2026.0.25 and 2026. |
| CVE-2026-62848 | 7.3 | 2026-10-30 | Metalama is a Roslyn-based open-source patterns and architecture toolkit for C#. From 2023.0.101-rc until 2025.1.18, 202 |
| CVE-2026-62849 | 9.1 | 2026-10-30 | ThingLinks is an enterprise IoT platform. Prior to 1.4.0, an unauthenticated SQL injection vulnerability in the `TDengin |
| CVE-2026-62853 | 9.9 | 2026-10-30 | ThingLinks is an enterprise IoT platform. Prior to 1.4.0, the `/groovyScriptTest/registerScript` endpoint accepts user-s |
| CVE-2026-62863 | 9.6 | 2026-10-30 | MoLing is a computer-use and browser-use based MCP server. Prior to 0.5.0, when MoLing runs in SSE mode using `-l`, its  |
| CVE-2026-62864 | 7.5 | 2026-10-30 | Ring is a Clojure web applications library inspired by Python's WSGI and Ruby's Rack. Prior to 1.15.5, `wrap-nested-para |
| CVE-2026-62958 | 7.9 | 2026-10-30 | libriscv is a RISC-V sandbox and emulator. Prior to 1.18, a crafted ELF binary can cause out-of-bounds reads in the host |
| CVE-2026-62966 | 7.5 | 2026-10-30 | ESPAsyncWebServer is an asynchronous HTTP and WebSocket server library for ESP32, ESP8266, RP2040 and RP2350. Prior to v |
| CVE-2026-62967 | 8.1 | 2026-10-30 | ZTNET is a ZeroTier web UI for private controllers with multiuser and organization support. Prior to 0.8.0, any authenti |
| CVE-2026-62989 | 8.1 | 2026-10-30 | Shopper is a Headless e-commerce Admin Panel. Prior to 2.10.0, the Variants Livewire component in `packages/admin/src/Li |
| CVE-2026-62990 | 8.7 | 2026-10-30 | Shopper is a Headless e-commerce Admin Panel. In versions from 2.0.0 prior to 2.10.1 and in the 3.0.0 prereleases beta.1 |
| CVE-2026-111578 | 7.5 | 2026-10-30 | The PDF Invoices & Packing Slips for WooCommerce WordPress plugin from 5.16.2 before 5.16.5 does not properly escape sev |
| CVE-2026-118938 | 8.8 | 2026-10-30 | In Trail of Bits fickling through 0.1.12, a pickle STACK_GLOBAL operand carrying a dotted __qualname__ (for example "Val |
| CVE-2026-16760 | 8.8 | 2026-10-30 | In Trail of Bits fickling through 0.1.12, the _process_import() method in fickle.py adds an imported name to the likely_ |
| CVE-2026-63182 | 8.1 | 2026-10-30 | LightSAML implements SAML 2.0 data model classes, XML serialization and deserialization, XML security, certificate suppo |
| CVE-2026-63184 | 7.1 | 2026-10-30 | Refitter is a tool for generating a C# REST API client using the Refit library. Prior to 2.1.1, the `refitter` dotnet to |
| CVE-2026-63338 | 8.3 | 2026-10-30 | IXP Manager is a full-stack web application for managing Internet Exchange Points. Prior to version 7.3.0, an authentica |
| CVE-2026-63339 | 8.8 | 2026-10-30 | IXP Manager is a full-stack web application for managing Internet Exchange Points. Prior to version 7.3.0, an authentica |
| CVE-2026-63341 | 7.5 | 2026-10-30 | Aedes is an MQTT broker that can run on any stream server. Prior to 1.1.1, the MQTT broker does not bound topic depth or |
| CVE-2026-63377 | 9.8 | 2026-10-30 | TAKO AI Agent for Okta is a local-first AI agent that helps Okta administrators query tenant data using natural language |
| CVE-2026-63378 | 8.8 | 2026-10-30 | TAKO AI Agent for Okta is a local-first AI agent that helps Okta administrators query tenant data using natural language |
| CVE-2026-116755 | 7.4 | 2026-10-31 | Improper Neutralization of Special Elements used in a Command ('Command Injection') in the Orchestrator component of Sof |
| CVE-2026-109234 | 7.2 | 2026-10-31 | The Meow Lightbox plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'post_content (bbPress reply |
| CVE-2026-109997 | 7.2 | 2026-10-31 | The Ninja Forms – Contact Form Builder with Calculators, Quizzes, Signatures & AI Form Builder plugin for WordPress is v |
| CVE-2026-116520 | 7.2 | 2026-10-31 | The PPWP – Password Protect Pages plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'comment / s |
| CVE-2026-119977 | 8.1 | 2026-10-31 | WordPress Core is vulnerable to Remote Code Execution in versions 4.7 through 7.1.3. This is due to predictable, web-acc |
| CVE-2026-107653 | 7.2 | 2026-10-31 | The SureCart – Ecommerce Made Easy For Selling Physical Products, Digital Downloads, Subscriptions, Donations, & Payment |
| CVE-2026-107750 | 7.2 | 2026-10-31 | The PDF Invoices & Packing Slips for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via t |
| CVE-2026-109220 | 9.8 | 2026-10-31 | The PDF Invoice for WooCommerce + Drag and Drop Template Builder plugin for WordPress is vulnerable to PHP Object Inject |
| CVE-2026-111254 | 7.2 | 2026-10-31 | The W3 Total Cache plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'comment' parameter in all  |
| CVE-2026-115840 | 7.2 | 2026-10-31 | The VikRentCar Car Rental Management System plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'p |
| CVE-2026-116522 | 7.2 | 2026-10-31 | The Relevanssi – A Better Search plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'comment' par |
| CVE-2026-116548 | 7.2 | 2026-10-31 | The VikRentCar Car Rental Management System plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'o |
| CVE-2026-116557 | 9.1 | 2026-10-31 | The WP Booking System - Booking Calendar plugin for WordPress is vulnerable to unauthorized modification of data due to  |
| CVE-2026-118070 | 7.2 | 2026-10-31 | The Welcart e-Commerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'gid' parameter in all  |
| CVE-2026-119065 | 7.2 | 2026-10-31 | The Shipping Zones by Drawing for WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the  |
| CVE-2026-119089 | 7.2 | 2026-10-31 | The ThirstyAffiliates – Affiliate Links, Link Branding, Link Tracking & Marketing Plugin plugin for WordPress is vulnera |
| CVE-2026-119162 | 7.2 | 2026-10-31 | The User Submitted Posts – Enable Users to Submit Posts from the Front End plugin for WordPress is vulnerable to Stored  |
| CVE-2026-119163 | 7.5 | 2026-10-31 | The FunnelKit Automations – Email Marketing Automation and CRM for WordPress & WooCommerce plugin for WordPress is vulne |
| CVE-2026-120040 | 7.5 | 2026-10-31 | The Mail logging & Catcher plugin for WordPress is vulnerable to Sensitive Information Exposure in all versions up to, a |
| CVE-2026-89270 | 9.1 | 2026-10-31 | The Popup Builder – Create highly converting, mobile friendly marketing popups. plugin for WordPress is vulnerable to au |
| CVE-2026-103898 | 8.1 | 2026-10-31 | The Wp Social Login and Register Social Counter plugin for WordPress is vulnerable to Authentication Bypass in all versi |
| CVE-2026-104012 | 8.8 | 2026-10-31 | The Rox Appointment Booking – Appointment Booking Scheduling Solution plugin for WordPress is vulnerable to Privilege Es |
| CVE-2026-107759 | 7.2 | 2026-10-31 | The WPO365 \| MICROSOFT 365 GRAPH MAILER plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'Subje |
| CVE-2026-116512 | 9.8 | 2026-10-31 | The Project Manager – AI Powered Project Management, Task Management, Kanban Board & Time Tracker plugin for WordPress i |
| CVE-2026-118057 | 7.2 | 2026-10-31 | The Shield Security – Smart Bot Blocking, Brute-Force Login Protection & File Scanning plugin for WordPress is vulnerabl |
| CVE-2026-119096 | 9.8 | 2026-10-31 | The Uncanny Toolkit for LearnDash plugin for WordPress is vulnerable to Authentication Bypass in versions up to, and inc |
| CVE-2026-120070 | 8.8 | 2026-10-31 | The User Frontend – Membership, User Registration, User Profile, User Directory & Content Restriction with Frontend Post |
| CVE-2026-103882 | 9.1 | 2026-10-31 | The Acadlix LMS – AI Quiz Maker, Online Exam & Course Plugin for WordPress plugin for WordPress is vulnerable to arbitra |
| CVE-2026-110530 | 7.2 | 2026-10-31 | The FeedWordPress plugin for WordPress is vulnerable to Stored Cross-Site Scripting in versions up to, and including, 20 |
| CVE-2026-114217 | 8.6 | 2026-10-31 | A flaw was found in konflux-ci. Continuous Integration (CI) automation scripts store sensitive GitHub access tokens in p |
| CVE-2026-116086 | 8.8 | 2026-10-31 | A flaw was found in konflux-ci. An attacker with permission to trigger automated workflow runs can cause an information  |
| CVE-2026-116964 | 8.4 | 2026-10-31 | A flaw was found in konflux-ci. An attacker with repository write access can achieve arbitrary code execution within the |
| CVE-2026-117681 | 8.0 | 2026-10-31 | A flaw was found in konflux-ci. This vulnerability allows privilege escalation when the user interface proxy automatical |
| CVE-2026-118235 | 9.8 | 2026-10-31 | The SimpleForm – Form Maker to Chat Apps with Quiz, Poll and Multi Lead Notifications plugin for WordPress is vulnerable |
| CVE-2026-120075 | 7.2 | 2026-10-31 | The WP Activity Log plugin for WordPress is vulnerable to Stored Cross-Site Scripting in all versions up to, and includi |
| CVE-2026-109197 | 7.5 | 2026-10-31 | The WP Directory Kit plugin for WordPress is vulnerable to generic SQL Injection via the 'idfield' parameter in all vers |
| CVE-2026-120114 | 7.2 | 2026-10-31 | The Debug Log Manager – Conveniently Monitor and Inspect Errors plugin for WordPress is vulnerable to Stored Cross-Site  |
| CVE-2026-120194 | 7.5 | 2026-10-31 | A flaw was found in json-glib. The JSONPath slice evaluator used by json_path_query() can enter an infinite loop when gi |
| CVE-2026-76010 | 8.8 | 2026-10-31 | The Photo Gallery, Sliders, Proofing and Themes – NextGEN Gallery plugin for WordPress is vulnerable to Remote Code Exec |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-118527 | Ivanti / Connect Secure | 2026-10-30 | 2026-11-13 | Unknown |
| CVE-2026-111357 | Ivanti / Connect Secure | 2026-10-30 | 2026-11-02 | Unknown |
| CVE-2026-97229 | GitLab / Community Edition and Enterprise Edition | 2026-10-29 | 2026-11-01 | Unknown |
| CVE-2026-76418 | Cisco / Secure Firewall ASA Software and Cisco Secure FTD Software | 2026-10-29 | 2026-11-01 | Unknown |
| CVE-2026-41709 | Broadcom / VMware ESX | 2026-10-28 | 2026-11-11 | Unknown |
| CVE-2026-46300 | Linux / Kernel | 2026-10-28 | 2026-10-31 | Unknown |
| CVE-2026-48356 | Adobe / Commerce and Magento | 2026-10-27 | 2026-11-10 | Unknown |
| CVE-2026-111497 | Google / Brotli | 2026-10-27 | 2026-11-10 | Unknown |
| CVE-2026-109618 | PHP Group / PHP | 2026-10-26 | 2026-10-29 | Unknown |
| CVE-2026-109619 | PHP Group / PHP | 2026-10-26 | 2026-10-29 | Unknown |

---

*Total entries in CISA KEV catalog: 1766*