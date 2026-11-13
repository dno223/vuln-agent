# Vulnerability Intelligence Report

**Date:** 2026-11-13  
**Generated:** 2026-11-13T15:55:18Z  

---

## Executive Summary

Our environment faces significant cybersecurity exposure across 247 high-severity vulnerabilities alongside 11 newly added CISA Known Exploited Vulnerabilities (KEVs). Key risks include authentication bypass flaws in SOGo enabling brute-force attacks, multiple cross-site scripting vulnerabilities in Progress Kendo UI, a kernel-level charger driver flaw, and a systemd vulnerability affecting OpenShift Sandboxed Containers. Critically, 11 CVEs were added to the CISA KEV catalog this week—including Microsoft Office and Barracuda Networks products—indicating active exploitation in the wild. Immediate prioritization of KEV remediation and high-CVSS patching is essential to reduce organizational risk.

---

## Risk Narrative

The current threat landscape reflects active exploitation of enterprise software vulnerabilities across productivity tools, network security appliances, and web frameworks. The addition of Barracuda Networks, Microsoft Office, and Cisco BroadWorks to the CISA KEV catalog signals targeted campaigns by sophisticated threat actors. XSS vulnerabilities in widely deployed jQuery UI components expand the attack surface for credential theft and session hijacking. Authentication weaknesses in SOGo expose email and collaboration infrastructure to account compromise. The kernel-level charger driver flaw presents a local privilege escalation risk. Collectively, these vulnerabilities threaten data confidentiality, operational continuity, and regulatory compliance, with potential for significant financial and reputational damage if exploited.

---

## Prioritized Action Items

1. Immediately patch or mitigate all 11 newly added CISA KEV vulnerabilities, particularly Microsoft Office, Barracuda ESG, and Cisco BroadWorks, as these are actively exploited in the wild.
2. Apply SOGo patches to version 5.12.13 or later to remediate authentication brute-force and TOTP rate-limiting vulnerabilities that enable account takeover.
3. Patch the kernel charger driver vulnerability (CVE-2026-91007, CVSS 7.8) to prevent user-mode privilege escalation on affected systems.
4. Remediate all Progress Kendo UI XSS vulnerabilities by updating to vendor-patched releases and validating input encoding across Chart, Spreadsheet, Gantt, and Form components.
5. Establish a continuous vulnerability prioritization process aligned to CISA KEV updates, ensuring critical patches are deployed within 24-72 hours of catalog additions.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-127111 | 7.4 | 2026-11-12 | SOGo before 5.12.13 contains an improper restriction of excessive authentication attempts vulnerability that allows unau |
| CVE-2026-127131 | 7.4 | 2026-11-12 | SOGo before 5.12.13 contains a missing rate limiting vulnerability in its web login TOTP verification that allows attack |
| CVE-2026-91007 | 7.8 | 2026-11-12 | The user-mode syscall verifiers for the charger driver API in drivers/charger/charger_handlers.c did not inspect the pro |
| CVE-2026-121876 | 7.9 | 2026-11-12 | A flaw was found in the interaction between systemd-gpt-auto-generator and 
confidential computing guest VM images in Op |
| CVE-2026-124691 | 7.1 | 2026-11-12 | In Progress Kendo UI for jQuery Gantt, the task editor's Parent dropdown renders task titles as HTML. An attacker who ca |
| CVE-2026-124695 | 7.1 | 2026-11-12 | In Progress Kendo UI for jQuery Form, the items[].hint option is documented as a string but is rendered as HTML. An atta |
| CVE-2026-124696 | 7.1 | 2026-11-12 | In Progress Kendo UI for jQuery, Spreadsheet sheet names are inserted into the SheetsBar menu button's data-sheet-name a |
| CVE-2026-124697 | 7.1 | 2026-11-12 | In Progress Kendo UI for jQuery, Chart shared-tooltip rendering treats bound category and series-name values as raw HTML |
| CVE-2026-124698 | 7.1 | 2026-11-12 | In Progress Kendo UI for jQuery, the Chart default tooltip renders point values as raw HTML. An attacker who can influen |
| CVE-2026-126190 | 7.5 | 2026-11-12 | Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4. Prior to 4.0, Soup Sieve repeatedly walk |
| CVE-2026-126191 | 7.5 | 2026-11-12 | Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4. Prior to 3.0, the CSS_ESCAPES and IDENTI |
| CVE-2026-126837 | 7.4 | 2026-11-12 | A validation flaw in the DNS SRV host discovery of the MongoDB Node.js driver may cause the driver to connect to a host  |
| CVE-2026-127029 | 7.5 | 2026-11-12 | A flaw was found in freeradius's Extensible Authentication Protocol Method for Subscriber Identity Module (EAP-SIM) modu |
| CVE-2026-127030 | 7.5 | 2026-11-12 | A flaw was found in freeradius. An improper length validation in the EAP-FAST module allows a stack-based buffer overflo |
| CVE-2026-106146 | 8.6 | 2026-11-12 | In Progress® Telerik® UI for ASP.NET MVC versions `2012.2.710` through `2026.3.1015`, server-side filter processing does |
| CVE-2026-106154 | 8.6 | 2026-11-12 | In Progress® Telerik® UI for ASP.NET Core versions `2015.1.318` through `2026.3.1015`, the server-side FilterParser proc |
| CVE-2026-106475 | 7.1 | 2026-11-12 | The Elasticsearch data source resource proxy forwards the request method and path to Elasticsearch using the data source |
| CVE-2026-124700 | 7.8 | 2026-11-12 | In Telerik UI for WinForms, versions prior to 2026.4.1111, an untrusted URL redirection vulnerability exists that allows |
| CVE-2026-124702 | 7.8 | 2026-11-12 | In Telerik UI for WPF, versions prior to 2026.4.1110, an untrusted URL redirection vulnerability exists that allows an a |
| CVE-2026-126196 | 8.1 | 2026-11-12 | pgEdge Postgres MCP Server enables SQL queries against PostgreSQL databases through Model Context Protocol compatible cl |
| CVE-2026-126197 | 8.8 | 2026-11-12 | pgEdge Postgres MCP Server enables SQL queries against PostgreSQL databases through Model Context Protocol compatible cl |
| CVE-2026-127204 | 7.5 | 2026-11-12 | WooCommerce PayPal Pro Payment Gateway plugin before 4.1.1 contains an unauthenticated payment bypass vulnerability that |
| CVE-2026-18379 | 8.8 | 2026-11-12 | A flaw was found in yggdrasil-worker-package-manager. An authenticated attacker can exploit this issue to achieve arbitr |
| CVE-2026-107152 | 7.1 | 2026-11-12 | An improper authentication vulnerability has been found in the task console in the smart_proxy_dynflow package. The cons |
| CVE-2026-107360 | 9.6 | 2026-11-12 | A flaw was found in rubygem-safemode. Compound assignment expressions in sandboxed code are evaluated without mediating  |
| CVE-2026-107443 | 7.7 | 2026-11-12 | A flaw was found in Foreman. An authenticated user with view_hosts privileges can retrieve rendered provisioning templat |
| CVE-2026-111456 | 7.1 | 2026-11-12 | A missing authorization check has been found in ConsumerResource.setupOwner() function of consumer registration module i |
| CVE-2026-124002 | 9.8 | 2026-11-12 | XWEB EVO versions 5.2.3 through before 5.7.0 contains a pre-authentication OS command injection vulnerability that allow |
| CVE-2026-124003 | 7.8 | 2026-11-12 | XWEB EVO before 5.6.2 contains a command injection vulnerability where the setuid-root Lua CGI interpreter wlua executes |
| CVE-2026-124004 | 9.8 | 2026-11-12 | XWEB EVO before 5.6.2 contains a hardcoded backdoor password vulnerability that allows unauthenticated remote attackers  |
| CVE-2026-124005 | 8.1 | 2026-11-12 | XWEB EVO 4.3.0 through 5.8.8 contains a weak password generation vulnerability that allows remote attackers to derive th |
| CVE-2026-124006 | 8.1 | 2026-11-12 | XWEB EVO through 5.8.8 contains a predictable credential generation vulnerability that allows attackers to derive the Li |
| CVE-2026-124007 | 8.1 | 2026-11-12 | XWEB EVO before 5.6.2 contains a pre-authentication OS command injection vulnerability that allows unauthenticated remot |
| CVE-2026-124008 | 7.2 | 2026-11-12 | XWEB EVO 5.2.3 through 5.8.8 contains an authenticated OS command injection vulnerability in the devices.lua template ha |
| CVE-2026-124009 | 7.2 | 2026-11-12 | XWEB EVO 5.2.3 through 5.8.8 contains an authenticated OS command injection vulnerability that allows authenticated atta |
| CVE-2026-124010 | 9.8 | 2026-11-12 | XWEB EVO before 5.6.2 contains a command injection vulnerability that allows unauthenticated remote attackers to execute |
| CVE-2026-124012 | 8.1 | 2026-11-12 | XWEB EVO 5.6.2 through 5.8.8 contains a hardcoded credential vulnerability where the Administrator web account is config |
| CVE-2026-124013 | 8.8 | 2026-11-12 | XWEB EVO 5.6.2 through 5.8.8 contains an authenticated OS command injection vulnerability in the api.lua import_preconfi |
| CVE-2026-124014 | 9.1 | 2026-11-12 | XWEB EVO 4.3.0 through 5.8.8 contains an unauthenticated arbitrary file write vulnerability that allows remote attackers |
| CVE-2026-45265 | 8.2 | 2026-11-12 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4 and 1.5.1, t |
| CVE-2026-45341 | 7.5 | 2026-11-12 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. From versions 1.4.0 to before 1.4.4, |
| CVE-2026-46674 | 7.5 | 2026-11-12 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4 and 1.5.1, a |
| CVE-2026-47217 | 7.5 | 2026-11-12 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4 and 1.5.1, a |
| CVE-2026-47257 | 8.1 | 2026-11-12 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. In versions 1.5.0 and 1.6.0-rc1, the |
| CVE-2026-47258 | 8.2 | 2026-11-12 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4, 1.5.1, and  |
| CVE-2026-47259 | 8.2 | 2026-11-12 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4, 1.5.1, and  |
| CVE-2026-47710 | 8.2 | 2026-11-12 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4, 1.5.1, and  |
| CVE-2026-47711 | 8.6 | 2026-11-12 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.4, 1.5.1, and  |
| CVE-2026-52786 | 7.1 | 2026-11-12 | BACnet Stack is a BACnet open source protocol stack C library for embedded systems. Prior to versions 1.4.5, 1.5.1, and  |
| CVE-2026-68548 | 9.4 | 2026-11-12 | Algernon is a small self-contained pure-Go web server. Prior to version 1.17.10, Algernon's URL-prefix authorization gat |
| CVE-2026-126793 | 8.0 | 2026-11-12 | An untrusted search path issue in Aurora PostgreSQL dialect detection in the AWS Advanced Go Wrapper from release 2026-0 |
| CVE-2026-127208 | 8.8 | 2026-11-12 | datamodel-code-generator before 0.84.0 contains a code injection vulnerability that allows attackers to achieve arbitrar |
| CVE-2026-86322 | 8.8 | 2026-11-12 | A flaw was found in Foreman’s Api::V2::PersonalAccessTokensController, where Foreman::Controller::UserAware#find_user re |
| CVE-2026-126823 | 7.0 | 2026-11-12 | A local user with an ordinary account on the same host can place a file in a shared temporary location that the JDBC dri |
| CVE-2026-126366 | 7.5 | 2026-11-13 | MessagePack for Ruby is an implementation of the MessagePack binary serialization format. Prior to 1.8.7, the Java-platf |
| CVE-2026-126982 | 7.5 | 2026-11-13 | A type allow-list bypass in the BSON serialization library of the MongoDB C# Driver allows a type-restriction check to b |
| CVE-2026-127275 | 10.0 | 2026-11-13 | A vulnerability was determined in Linksys EA8100 1.0.3.216940. This issue affects the function SetRemoteSetting/SetUnsec |
| CVE-2026-127277 | 10.0 | 2026-11-13 | A security flaw has been discovered in Linksys EA8100 1.0.3.216940. The affected element is an unknown function of the f |
| CVE-2026-127278 | 7.3 | 2026-11-13 | A weakness has been identified in AIP-PUB ACPs-community up to 2.2.0. The impacted element is the function send_verifica |
| CVE-2026-127279 | 7.3 | 2026-11-13 | A vulnerability was detected in AIP-PUB ACPs-community up to 2.2.0. This impacts an unknown function of the file discove |
| CVE-2026-127281 | 7.3 | 2026-11-13 | A vulnerability was found in lanyulei ferry 1.0.0-beta.1/1.0.0. Affected is an unknown function of the file middleware/a |
| CVE-2026-127283 | 7.3 | 2026-11-13 | A vulnerability was identified in SourceCodester Food Ordering System 1.0. Affected by this issue is some unknown functi |
| CVE-2026-127284 | 7.3 | 2026-11-13 | A security flaw has been discovered in SourceCodester Food Ordering System 1.0. This affects an unknown part of the file |
| CVE-2026-127286 | 7.3 | 2026-11-13 | A vulnerability was identified in Zackriya-Solutions Meetily up to 0.4.1. Affected is an unknown function of the file ba |
| CVE-2026-116417 | 8.1 | 2026-11-13 | Dell PowerScale InsightIQ, versions 6.3.0 through 6.4.0, contains a Weak Password Requirements vulnerability. An unauthe |
| CVE-2023-54423 | 7.5 | 2026-11-13 | OpenMage magento-lts before 20.2.0 contains a stored cross-site scripting vulnerability because the TinyMCE WYSIWYG edit |
| CVE-2024-58404 | 7.7 | 2026-11-13 | Zipline versions from 3.4.5 before 3.7.10 contain a path traversal vulnerability in the user data export endpoint via th |
| CVE-2024-58405 | 8.6 | 2026-11-13 | Zipline through 3.7.9 contains an improper authorization vulnerability in the /api/auth/register endpoint, which enforce |
| CVE-2025-71459 | 8.1 | 2026-11-13 | Zipline through 4.3.2 contains a path traversal vulnerability that allows authenticated uploaders to write files outside |
| CVE-2026-116418 | 7.5 | 2026-11-13 | Dell PowerScale InsightIQ, versions 6.3.0 through 6.4.0, contains an Incorrect Authorization vulnerability. A low privil |
| CVE-2026-116615 | 8.8 | 2026-11-13 | The Widget Options – Advanced Conditional Visibility for Gutenberg Blocks & Classic Widgets plugin for WordPress is vuln |
| CVE-2026-118191 | 8.1 | 2026-11-13 | The Photo Gallery, Sliders, Proofing and Themes – NextGEN Gallery plugin for WordPress is vulnerable to arbitrary file d |
| CVE-2026-119077 | 9.8 | 2026-11-13 | The ELEX WordPress HelpDesk & Customer Ticketing System plugin for WordPress is vulnerable to PHP Object Injection in al |
| CVE-2026-120688 | 7.2 | 2026-11-13 | The EZ SQL Reports Shortcode Widget and DB Backup plugin for WordPress is vulnerable to Stored Cross-Site Scripting via  |
| CVE-2026-123769 | 8.8 | 2026-11-13 | The SureDash – Community, Courses & Member Dashboard plugin for WordPress is vulnerable to Privilege Escalation in all v |
| CVE-2026-124218 | 8.2 | 2026-11-13 | The Drag and Drop File Upload for Elementor Forms plugin for WordPress is vulnerable to arbitrary file deletion due to i |
| CVE-2026-125055 | 9.8 | 2026-11-13 | The Chatterbug Forms – Fast, Flexible WordPress Form Builder plugin for WordPress is vulnerable to Arbitrary File Upload |
| CVE-2026-126264 | 7.7 | 2026-11-13 | SiYuan before 3.8.9 contains an information disclosure vulnerability that allows authenticated Reader users to retrieve  |
| CVE-2026-126265 | 7.4 | 2026-11-13 | SiYuan 2.1.0 before 3.8.9 contains a flaw where the loginAuth CAPTCHA challenge lives in a signed client-side cookie, al |
| CVE-2026-126266 | 7.5 | 2026-11-13 | SiYuan from 3.6.0 before 3.8.9 contains an information disclosure vulnerability that allows unauthenticated publish visi |
| CVE-2026-126269 | 8.7 | 2026-11-13 | NocoDB before 2026.09.0 contains a stored cross-site scripting vulnerability that allows authenticated Editor users to e |
| CVE-2026-126271 | 7.7 | 2026-11-13 | NocoDB before 2026.09.0 contains an information disclosure vulnerability that allows authenticated base Viewers to obtai |
| CVE-2026-126273 | 8.1 | 2026-11-13 | NocoDB before 2026.09.0 contains a privilege escalation vulnerability in initAdminFromEnv.ts that silently skips super-a |
| CVE-2026-126274 | 8.7 | 2026-11-13 | NocoDB before 2026.08.0 contains a stored cross-site scripting vulnerability that allows authenticated Creator users to  |
| CVE-2026-126275 | 7.1 | 2026-11-13 | NocoDB before 2026.09.0 contains an insecure direct object reference vulnerability that allows authenticated users to re |
| CVE-2026-126277 | 7.5 | 2026-11-13 | NocoDB before 2026.08.1 contains an uncontrolled resource consumption vulnerability that allows unauthenticated attacker |
| CVE-2026-126278 | 7.5 | 2026-11-13 | NocoDB before 2026.08.1 contains a race condition vulnerability in users.service.ts that allows holders of a valid reset |
| CVE-2026-126280 | 7.4 | 2026-11-13 | NocoDB before 2026.08.0 contains a race condition in refresh-token rotation that allows attackers to reuse tokens becaus |
| CVE-2026-126282 | 8.0 | 2026-11-13 | NocoDB from 2026.04.0 before 2026.08.0 contains an improper privilege management vulnerability in org-users.service.ts w |
| CVE-2026-126283 | 8.8 | 2026-11-13 | NocoDB before 2026.08.0 contains an incorrect authorization vulnerability that lets base-scoped API tokens act as accoun |
| CVE-2026-126285 | 7.7 | 2026-11-13 | NocoDB before 2026.08.0 contains an sql injection vulnerability that allows authenticated users with read access to run  |
| CVE-2026-126286 | 8.1 | 2026-11-13 | NocoDB before 2026.08.0 contains a reflected cross-site scripting vulnerability in PageLeavingWarning.vue that allows un |
| CVE-2026-126291 | 8.8 | 2026-11-13 | NocoDB before 2026.06.2 contains an SQL injection vulnerability in base-user.cte.utils.ts, which concatenates base membe |
| CVE-2026-126294 | 7.5 | 2026-11-13 | Grav Login plugin before 3.11.0 contains an authentication bypass vulnerability that allows attackers with an account pa |
| CVE-2026-126297 | 7.5 | 2026-11-13 | NLTK before 3.10.4 contains a quadratic-time denial of service vulnerability in ConllCorpusReader._get_srl_instances tha |
| CVE-2026-126298 | 7.5 | 2026-11-13 | NLTK before 3.10.4 contains a denial of service vulnerability in Tree.chomsky_normal_form that allows remote attackers t |
| CVE-2026-126299 | 7.5 | 2026-11-13 | NLTK before 3.10.4 contains a denial of service vulnerability in the CCG lexicon parser fromstring that allows remote at |
| CVE-2026-126303 | 7.5 | 2026-11-13 | NLTK before 3.10.4 contains an uncontrolled resource consumption vulnerability in SteppingRecursiveDescentParser.parse() |
| CVE-2026-126304 | 7.5 | 2026-11-13 | NLTK from 3.10.0 before 3.10.4 contains a symlink escape vulnerability in YCOECorpusReader that allows attackers to read |
| CVE-2026-126305 | 7.3 | 2026-11-13 | EspoCRM before 9.3.11 and 10.x before 10.0.9 contains a stored cross-site scripting vulnerability in Knowledge Base arti |
| CVE-2026-126306 | 8.0 | 2026-11-13 | EspoCRM before 9.3.11 and 10.x before 10.0.8 contains a stored cross-site scripting vulnerability that allows low-privil |
| CVE-2026-126307 | 7.5 | 2026-11-13 | Nezha Dashboard before 2.6.0 contains multiple authorization, tenant isolation, and resource exhaustion vulnerabilities  |
| CVE-2026-126308 | 7.7 | 2026-11-13 | The web dashboard in Coder 2.24.0 before 2.29.23, 2.30.0 before 2.34.14, 2.35.0 before 2.36.9, 2.37.0 before 2.37.6, and |
| CVE-2026-126309 | 7.1 | 2026-11-13 | OpenBao before 2.6.5 and 2.7.2 contains a path traversal vulnerability in Transit key import that allows authenticated a |
| CVE-2026-126310 | 8.7 | 2026-11-13 | OpenBao before 2.6.5 and 2.7.2 contains an authentication bypass vulnerability that allows unauthenticated callers to ob |
| CVE-2026-126312 | 7.1 | 2026-11-13 | OpenBao before 2.6.5 and 2.7.x before 2.7.2, and the openbao-plugins LDAP and RADIUS auth plugins before 0.2.0, contain  |
| CVE-2026-126314 | 8.8 | 2026-11-13 | Frappe HRMS 15.0.0 before 15.64.6 and 16.0.0 before 16.20.1 does not check access to each employee on endpoints that cre |
| CVE-2026-126315 | 9.8 | 2026-11-13 | Frappe HRMS 16.14.0 before 16.20.1 sends product usage events on certain HR transactions without checking the site's tel |
| CVE-2026-126317 | 8.8 | 2026-11-13 | Frappe HRMS from 16.0.0 before 16.20.1 contains a missing authorization vulnerability that allows authenticated users to |
| CVE-2026-126321 | 8.3 | 2026-11-13 | Dockhand before 1.0.55 contains a path traversal vulnerability that allows authenticated users with stacks:edit to bypas |
| CVE-2026-126322 | 8.1 | 2026-11-13 | OpenEMR before 8.3.0 contains an unsanitized deserialization vulnerability that allows authenticated attackers to contro |
| CVE-2026-126370 | 8.8 | 2026-11-13 | Vvveb through 1.0.8.6 contains a remote code execution vulnerability allowing restricted site_admin roles to inject PHP  |
| CVE-2026-126372 | 8.8 | 2026-11-13 | Vvveb through 1.0.8.6 contains an incomplete fix for CVE-2026-41934 that allows authenticated editor or site_admin users |
| CVE-2026-126375 | 8.1 | 2026-11-13 | Vvveb through 1.0.8.6 contains a missing authorization vulnerability that allows low-privilege vendors to rename, delete |
| CVE-2026-126377 | 8.1 | 2026-11-13 | Vvveb before 1.0.9.0 contains an authentication bypass vulnerability in generateCookie() in system/user/user.php that us |
| CVE-2026-126378 | 9.1 | 2026-11-13 | Vvveb through 1.0.8.6 contains a file upload vulnerability in the theme installer validFile() function that uses strpos( |
| CVE-2026-126379 | 7.6 | 2026-11-13 | Vvveb 1.0.8.6 contains an incomplete server-side request forgery fix that allows authenticated admin users to bypass DNS |
| CVE-2026-126380 | 9.1 | 2026-11-13 | Vvveb before 1.0.9.0 contains a denylist bypass in system/traits/media.php where '.phar' is misconfigured with a leading |
| CVE-2026-126383 | 8.2 | 2026-11-13 | n8n before 1.123.89, 2.x before 2.45.5, 2.46.x before 2.46.1, and 3.x before 3.0.1 contains a NoSQL injection vulnerabil |
| CVE-2026-126384 | 7.5 | 2026-11-13 | n8n before 1.123.89, 2.x before 2.45.5, 2.46.x before 2.46.1, and 3.x before 3.0.1 bundles a GraphicsMagick version with |
| CVE-2026-126385 | 7.7 | 2026-11-13 | n8n before 2.45.5, 2.46.x before 2.46.1, and 3.x before 3.0.1 contains a flaw in the OAuth2 credential callback of the d |
| CVE-2026-126391 | 7.5 | 2026-11-13 | n8n before 1.123.89 contains an insufficient isolation vulnerability in workflow expression evaluation that allows authe |
| CVE-2026-126397 | 7.5 | 2026-11-13 | vLLM from 0.10.1 before 0.31.0 forwards a request-controlled mm_processor_kwargs.max_patches value to the Hugging Face p |
| CVE-2026-126401 | 7.5 | 2026-11-13 | Fleet before 4.86.2 contains a denial of service vulnerability that allows unauthenticated attackers to exhaust server m |
| CVE-2026-126402 | 7.2 | 2026-11-13 | Fleet before 4.89.0 contains an incorrect authorization flaw in its user administration API that accepts user creation o |
| CVE-2026-126412 | 8.8 | 2026-11-13 | Frappe HRMS 15.0.0 before 15.64.1 and 16.0.0 before 16.19.0 lacks a write permission check on a bulk record processing a |
| CVE-2026-126414 | 8.8 | 2026-11-13 | Frappe HRMS 15.0.0 before 15.64.2 and 16.0.0 before 16.20.0 contains a missing authorization vulnerability in certain re |
| CVE-2026-126416 | 7.1 | 2026-11-13 | OpenEMR before 8.5.0 contains an improper authorization vulnerability in patient_tracker_status.php that allows low-priv |
| CVE-2026-126425 | 7.2 | 2026-11-13 | OpenEMR before 8.5.0 contains a stored SQL injection vulnerability in which History layout field identifiers saved throu |
| CVE-2026-126428 | 7.5 | 2026-11-13 | OpenEMR before 8.5.0 contains a remote code execution vulnerability that allows authenticated billing users to store att |
| CVE-2026-126430 | 8.1 | 2026-11-13 | OpenEMR before 8.5.0 contains an sql injection vulnerability that allows any authenticated core user to inject SQL by su |
| CVE-2026-126434 | 8.1 | 2026-11-13 | OpenEMR before 8.5.0 contains a missing authorization vulnerability in interface/forms/procedure_order/common.php that a |
| CVE-2026-126436 | 7.5 | 2026-11-13 | OpenEMR before 8.5.0 contains an authorization bypass vulnerability that allows OAuth2 clients to use unregistered grant |
| CVE-2026-126442 | 8.1 | 2026-11-13 | OpenEMR before 8.5.0 contains a missing authorization vulnerability in create_portallogin.php that allows low-privilege  |
| CVE-2026-126449 | 7.1 | 2026-11-13 | OpenEMR before 8.5.0 contains a missing authorization vulnerability in immunizations.php, diagnosis_full.php, and billin |
| CVE-2026-126451 | 7.3 | 2026-11-13 | OpenEMR before 8.5.0 contains a stored cross-site scripting vulnerability that allows portal patients to run JavaScript  |
| CVE-2026-126452 | 7.1 | 2026-11-13 | OpenEMR before 8.5.0 contains a missing authorization vulnerability in diagnosis_full.php that allows authenticated user |
| CVE-2026-126454 | 8.1 | 2026-11-13 | OpenEMR before 8.5.0 lacks rate limiting or lockout on TOTP submission, allowing attackers with a valid password to brut |
| CVE-2026-126455 | 8.1 | 2026-11-13 | OpenEMR before 8.5.0 contains multiple missing authorization and SQL injection defects across report, portal, transactio |
| CVE-2026-126458 | 8.8 | 2026-11-13 | OpenEMR before 8.5.0 contains a missing authorization vulnerability in authorizations_full.php that allows any authentic |
| CVE-2026-126460 | 7.1 | 2026-11-13 | OpenEMR before 8.5.0 contains a persistent SQL injection vulnerability in SLEOB::slInvoiceNumber(), where the CLP01 clai |
| CVE-2026-126463 | 7.1 | 2026-11-13 | OpenEMR before 8.5.0 contains multiple sql injection vulnerabilities that allow authenticated users to inject payloads t |
| CVE-2026-126466 | 8.8 | 2026-11-13 | OpenEMR before 8.5.0 contains a missing authorization vulnerability that allows any authenticated user to create patient |
| CVE-2026-126468 | 8.8 | 2026-11-13 | OpenEMR before 8.5.0 contains a missing authorization vulnerability that allows any authenticated low-privilege user to  |
| CVE-2026-126469 | 8.8 | 2026-11-13 | OpenEMR before 8.5.0 contains a missing authorization vulnerability in several custom/ scripts that rely only on session |
| CVE-2026-126470 | 8.8 | 2026-11-13 | OpenEMR before 8.5.0 contains an insecure direct object reference vulnerability in the Carecoordination module that allo |
| CVE-2026-126472 | 8.8 | 2026-11-13 | OpenEMR before 8.5.0 contains a missing authorization vulnerability in ccdaservice/ccda_gateway.php that allows any auth |
| CVE-2026-126473 | 9.1 | 2026-11-13 | OpenEMR before 8.4.0 contains OAuth scope canonicalization and containment flaws that allow unauthenticated attackers to |
| CVE-2026-126478 | 7.6 | 2026-11-13 | OpenEMR before 8.5.0 contains an SQL injection vulnerability in the Syndromic Surveillance report because the form_icd_c |
| CVE-2026-126479 | 7.6 | 2026-11-13 | OpenEMR before 8.5.0 contains a missing authorization vulnerability in five Module Manager InstallerController actions t |
| CVE-2026-126480 | 8.1 | 2026-11-13 | OpenEMR before 8.5.0 contains an sql injection vulnerability in CcrTable::insertApprovedData() that allows authenticated |
| CVE-2026-126481 | 8.1 | 2026-11-13 | OpenEMR before 8.5.0 contains a path traversal vulnerability in era_payments.php and sl_eob_search.php that allows authe |
| CVE-2026-126482 | 8.8 | 2026-11-13 | OpenEMR before 8.5.0 contains an SQL injection vulnerability in SLEOB::slInvoiceNumber() in src/Billing/SLEOB.php, which |
| CVE-2026-126486 | 7.6 | 2026-11-13 | OpenEMR before 8.5.0 contains a missing authorization vulnerability in portal/import_template.php, where several portal  |
| CVE-2026-126487 | 8.8 | 2026-11-13 | OpenEMR before 8.5.0 contains an authorization bypass vulnerability that allows authenticated users to override system-w |
| CVE-2026-126488 | 7.7 | 2026-11-13 | OpenEMR before 8.5.0 contains an SQL injection vulnerability in the patient portal OnsiteDocument.Query endpoint, where  |
| CVE-2026-126489 | 7.2 | 2026-11-13 | OpenEMR before 8.5.0 contains a second-order SQL injection vulnerability in the IPPF contraceptive issue feature because |
| CVE-2026-126491 | 7.6 | 2026-11-13 | OpenEMR before 8.5.0 contains a stored SQL injection vulnerability in getByPatientDemographics() where layout_options fi |
| CVE-2026-126492 | 7.1 | 2026-11-13 | OpenEMR before 8.5.0 contains a second-order sql injection vulnerability that allows low-privileged authenticated users  |
| CVE-2026-126494 | 7.1 | 2026-11-13 | OpenEMR before 8.4.0 contains an improper authorization vulnerability in ScopeRepository::finalizeScopes() that allows r |
| CVE-2026-126937 | 8.1 | 2026-11-13 | Zipline before 4.6.5 contains a TOCTOU race condition in the POST /api/setup endpoint that allows unauthenticated attack |
| CVE-2026-126938 | 7.1 | 2026-11-13 | Zipline before 4.6.4 contains a resource allocation vulnerability that allows authenticated users to bypass chunked-uplo |
| CVE-2026-126945 | 8.7 | 2026-11-13 | Zipline before 4.5.1 contains a stored cross-site scripting vulnerability in the HighlightCode component that renders un |
| CVE-2026-126948 | 8.8 | 2026-11-13 | Zipline before 4.5.0 contains an insecure direct object reference vulnerability caused by missing ownership verification |
| CVE-2026-126952 | 8.1 | 2026-11-13 | Zipline through 4.4.0 contains an authentication bypass vulnerability in the WebAuthn login endpoint that creates sessio |
| CVE-2026-126953 | 8.1 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains an OS command injection vulnerability that allows a malicious or compromised ACS to e |
| CVE-2026-127073 | 9.9 | 2026-11-13 | OpsTree BuildPiper before 2.7.0 contains a privilege escalation vulnerability that allows project users to gain Kubernet |
| CVE-2026-127077 | 7.1 | 2026-11-13 | OpsTree BuildPiper before 2.7.0 contains an authorization bypass vulnerability that allows authenticated users to create |
| CVE-2026-127078 | 7.1 | 2026-11-13 | OpsTree BuildPiper before 2.7.0 contains an authorization bypass vulnerability that allows authenticated users to attach |
| CVE-2026-127079 | 7.4 | 2026-11-13 | OpsTree BuildPiper before 2.7.0 lacks rate limiting on password-reset OTP verification, allowing unauthenticated attacke |
| CVE-2026-127080 | 9.9 | 2026-11-13 | OpsTree BuildPiper before 2.7.0 contains an improper authorization vulnerability that allows authenticated deploy users  |
| CVE-2026-127082 | 7.7 | 2026-11-13 | Huginn before 2026.11.09 contains an information exposure vulnerability in JqAgent that allows authenticated users to re |
| CVE-2026-127084 | 7.3 | 2026-11-13 | Teable before 2026-10-12T12-45-53Z.3331 contains a stored cross-site scripting vulnerability that allows authenticated u |
| CVE-2026-127088 | 8.1 | 2026-11-13 | 2FAuth before 9.0.1 contains a weak password recovery vulnerability that allows unauthenticated attackers to poison rese |
| CVE-2026-127090 | 8.8 | 2026-11-13 | Jadaptive Maverick Synergy Server before 3.0.33 and 3.1.x before 3.1.7, and Maverick Legacy Server before 1.8.1, contain |
| CVE-2026-127094 | 7.6 | 2026-11-13 | Pagelayer 2.1.7 before 2.2.1 contains a missing authorization vulnerability in Abilities API abilities registered in mai |
| CVE-2026-128014 | 8.1 | 2026-11-13 | FrankenPHP standalone static binaries 1.8.0 before 1.13.2 bundle the PHP brotli extension statically linked with Brotli  |
| CVE-2026-128023 | 7.4 | 2026-11-13 | FrankenPHP before 1.13.0 contains an authentication bypass vulnerability that allows unauthenticated attackers to spoof  |
| CVE-2026-128027 | 9.8 | 2026-11-13 | FrankenPHP Docker images before 1.1.11 were rebuilt only when new base image tags were created, so security fixes that A |
| CVE-2026-128041 | 8.0 | 2026-11-13 | OpenMage magento-lts before 20.18.2 and 21.0.0-beta1 before 21.0.0-beta3 serves RSS feeds with a text/html content type  |
| CVE-2026-128044 | 7.7 | 2026-11-13 | OpenMage magento-lts before 20.18.2 and 21.x before 21.0.0-beta3 validates OAuth 1.0a oauth_callback URLs with a string- |
| CVE-2026-128046 | 8.1 | 2026-11-13 | OpenMage magento-lts 20.17.0 before 20.18.2 and 21.0.0-beta1 before 21.0.0-beta3 contains an unrestricted file upload vu |
| CVE-2026-128047 | 8.1 | 2026-11-13 | OpenMage magento-lts before 20.18.2 and 21.0.0-beta pre-releases before 21.0.0-beta3 generate customer email-confirmatio |
| CVE-2026-128049 | 9.0 | 2026-11-13 | OpenMage Magento LTS before 20.18.2 and 21.0.0-beta1 before 21.0.0-beta3 contains a cross-site request forgery vulnerabi |
| CVE-2026-128242 | 7.5 | 2026-11-13 | actix-http before 3.20.1 and actix-web before 4.18.2 contain an unbounded decompression vulnerability in encoding::Decod |
| CVE-2026-128329 | 7.7 | 2026-11-13 | Dokploy 0.28.0 before 0.31.1 contains a path traversal vulnerability that allows authenticated organization members to r |
| CVE-2026-128332 | 7.4 | 2026-11-13 | Listmonk 6.0.0 before 7.0.0-beta.2 contains a 2FA bypass vulnerability that allows attackers with a valid password to br |
| CVE-2026-128333 | 7.4 | 2026-11-13 | listmonk 6.0.0 before 7.0.0-beta.2 contains an authentication bypass vulnerability in doResetPassword that skips TOTP ve |
| CVE-2026-128337 | 7.0 | 2026-11-13 | ExcelJS through 4.4.0 contains a prototype pollution vulnerability in mergeConditionalFormattings that allows attackers  |
| CVE-2026-128338 | 7.5 | 2026-11-13 | exceljs through 4.4.0 contains a memory exhaustion vulnerability that allows attackers to crash applications by supplyin |
| CVE-2026-128339 | 7.5 | 2026-11-13 | ExcelJS through 4.4.0 contains a memory exhaustion vulnerability in Worksheet._parseMergeCells that allows attackers to  |
| CVE-2026-128340 | 7.5 | 2026-11-13 | ExcelJS through 4.4.0 contains a memory exhaustion vulnerability that allows attackers to crash applications by supplyin |
| CVE-2026-128341 | 7.5 | 2026-11-13 | ExcelJS through 4.4.0 contains a resource exhaustion vulnerability in data-validations-xform.js that allows attackers to |
| CVE-2026-128342 | 7.5 | 2026-11-13 | ExcelJS through 4.4.0 contains a denial of service vulnerability that allows attackers to block the event loop by supply |
| CVE-2026-128343 | 7.5 | 2026-11-13 | exceljs through 4.4.0 contains a denial of service vulnerability that allows attackers to block the event loop by supply |
| CVE-2026-128344 | 7.5 | 2026-11-13 | ExcelJS through 4.4.0 contains a memory exhaustion vulnerability that allows attackers to crash applications by supplyin |
| CVE-2026-128346 | 7.5 | 2026-11-13 | ExcelJS through 4.4.0 contains a resource leak vulnerability in the streaming WorkbookReader.parse that leaves temporary |
| CVE-2026-128347 | 7.5 | 2026-11-13 | ExcelJS through 4.4.0 contains an arbitrary file read vulnerability in the streaming WorkbookWriter that allows attacker |
| CVE-2026-61418 | 7.5 | 2026-11-13 | Dell SmartFabric OS10 Software, versions prior to 10.6.0.10, contains an Incorrect Authorization vulnerability. A low pr |
| CVE-2026-75487 | 7.2 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains a command injection vulnerability that allows authenticated administrators to execute |
| CVE-2026-75490 | 7.5 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains a remote code execution vulnerability that allows unauthenticated adjacent attackers  |
| CVE-2026-75491 | 8.1 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains an authentication bypass vulnerability in the Mosquitto plugin auth_plugin_jwt.so tha |
| CVE-2026-75492 | 7.5 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains an unauthenticated stack buffer overflow vulnerability in the stun_client TR-111 UDP  |
| CVE-2026-75494 | 7.4 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains an argument injection vulnerability that allows a malicious or compromised ACS to inj |
| CVE-2026-75495 | 8.1 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains an OS command injection vulnerability that allows a malicious or compromised ACS to e |
| CVE-2026-75576 | 7.2 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains a command injection vulnerability that allows authenticated administrators to execute |
| CVE-2026-75577 | 7.2 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains a command injection vulnerability that allows authenticated administrators to execute |
| CVE-2026-75578 | 7.2 | 2026-11-13 | Cudy TR3000 before 2.5.42 contains a command injection vulnerability in luci/model/cbi/vpn/openvpn/client.lua, which emb |
| CVE-2026-109903 | 7.8 | 2026-11-13 | A buffer overread caused by casting a negative integer to CARD32 in XvQueryImageAttributes in X.Org X Server before 21.1 |
| CVE-2026-86355 | 8.3 | 2026-11-13 | Dell PowerStore contains an External Control of File Name or Path vulnerability. A remote authenticated attacker could e |
| CVE-2026-86356 | 8.8 | 2026-11-13 | Dell PowerStore contains an authorization-bypass vulnerability that could lead to elevation of privilege to administrato |
| CVE-2026-95518 | 7.0 | 2026-11-13 | Time-of-check time-of-use (TOCTOU) race condition vulnerability in TÜBİTAK BİLGEM Yazılım Teknolojileri Araştırma Enstit |
| CVE-2026-116411 | 8.8 | 2026-11-13 | Dell PowerStore contains a Server-Side Request Forgery (SSRF) vulnerability. An authenticated user with limited privileg |
| CVE-2026-116413 | 7.1 | 2026-11-13 | Dell PowerStore contains a use-of-broken-cryptography vulnerability. A low-privileged attacker could exploit it to imper |
| CVE-2026-82177 | 7.2 | 2026-11-13 | Dell PowerStore contains an OS Command Injection vulnerability. A high-privileged attacker could exploit this vulnerabil |
| CVE-2026-103769 | 7.2 | 2026-11-13 | Deserialization of Untrusted Data vulnerability in Acowebs PDF Invoices and Packing Slips For WooCommerce pdf-invoices-a |
| CVE-2026-107522 | 7.2 | 2026-11-13 | Dell PowerStore contains an Improper Authorization vulnerability. An authenticated user could exploit this vulnerability |
| CVE-2026-107523 | 8.7 | 2026-11-13 | Dell PowerStore contains an integer overflow vulnerability. An adjacent attacker could exploit it to bypass volume bound |
| CVE-2026-107524 | 8.8 | 2026-11-13 | Dell PowerStore contains an integer overflow vulnerability. An authenticated storage host could exploit this vulnerabili |
| CVE-2026-109092 | 7.8 | 2026-11-13 | Incorrectly handled negative sizes when processing ProcXvShmPutImage requests in the X.Org xwayland before 24.1.15 and X |
| CVE-2026-109445 | 9.8 | 2026-11-13 | PLANET GS-5220-8P2T2S (hardware version 3.0) firmware versions before 3.2412b261008 contains a stack-based buffer overfl |
| CVE-2026-111547 | 8.1 | 2026-11-13 | Dell PowerStore contains an out-of-bounds read vulnerability. An attacker could exploit this vulnerability, potentially  |
| CVE-2026-118976 | 7.5 | 2026-11-13 | In Progress® Telerik® UI for Blazor versions v11.1.0 through v14.0.0, the demo application's Chat AI Integration example |
| CVE-2026-119512 | 8.8 | 2026-11-13 | Deserialization of Untrusted Data vulnerability in Tribulant Software Newsletters newsletters-lite allows Object Injecti |
| CVE-2026-119517 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in VillaTheme Catna – |
| CVE-2026-120835 | 8.8 | 2026-11-13 | Deserialization of Untrusted Data vulnerability in VillaTheme AFFI – Affiliate Marketing for WooCommerce affi-affiliate- |
| CVE-2026-123975 | 7.5 | 2026-11-13 | Grid Community Toolkit before 6.2.20261111 (globus-gss-assist before 12.9) contains a heap out-of-bounds write in globus |
| CVE-2026-124260 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Jacob N. Breetvelt |
| CVE-2026-124265 | 8.5 | 2026-11-13 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Tribulant Software |
| CVE-2026-124267 | 7.5 | 2026-11-13 | Missing Authorization vulnerability in Noor Alam Gmail SMTP gmail-smtp allows Exploiting Incorrectly Configured Access C |
| CVE-2026-124272 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Dimitri Grassi Sal |
| CVE-2026-124410 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in wpLingua Translati |
| CVE-2026-124415 | 9.3 | 2026-11-13 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Alejandro Alex Res |
| CVE-2026-124420 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Themeisle Woody ad |
| CVE-2026-124970 | 9.3 | 2026-11-13 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in WP BASE WP BASE Bo |
| CVE-2026-125452 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Denishua WPJAM Bas |
| CVE-2026-125783 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in madalin.ungureanu  |
| CVE-2026-125811 | 8.5 | 2026-11-13 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in myCred myCred mycr |
| CVE-2026-125837 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in thethemefoundry Ma |
| CVE-2026-125851 | 9.9 | 2026-11-13 | Unrestricted Upload of File with Dangerous Type vulnerability in themagnifico52 Hotel Booking Lite hotel-booking-lite al |
| CVE-2026-125852 | 7.7 | 2026-11-13 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Realtyna Realtyna Organi |
| CVE-2026-125854 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Unbounce Unbounce  |
| CVE-2026-125855 | 9.8 | 2026-11-13 | Deserialization of Untrusted Data vulnerability in Elextensions ELEX WordPress HelpDesk & Customer Ticketing System elex |
| CVE-2026-125856 | 7.1 | 2026-11-13 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Sarah Giles Dynami |
| CVE-2026-128908 | 8.8 | 2026-11-13 | OS command injection (CWE-78) in the network-configuration handling of the management service (uavmonitor_usbv1) of the  |
| CVE-2026-128909 | 8.8 | 2026-11-13 | Improper verification of cryptographic signature (CWE-347) in the firmware update handler of the management service (uav |
| CVE-2026-128990 | 7.8 | 2026-11-13 | xschem 2.9.9 through 3.4.7 contains a heap out-of-bounds write vulnerability in read_dataset() in src/rawtovcd.c due to  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-124194 | Microsoft / Office | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-111793 | Openwave Messaging Limited / Webtop Media Transcoder | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-20320 | Cisco / BroadWorks | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-111560 | Barracuda Networks / Multiple Products | 2026-11-10 | 2026-11-13 | Unknown |
| CVE-2026-116606 | Barracuda Networks / Barracuda Email Security Gateway (ESG) | 2026-11-10 | 2026-11-13 | Unknown |
| CVE-2026-125350 | Google / Chromium | 2026-11-10 | 2026-11-24 | Unknown |
| CVE-2026-102895 | GPUStack / GPUStack | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-123158 | OpenBSD / OpenSSH | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-116779 | SignalWire / FreeSwitch | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-123218 | IBM / Aspera Faspex | 2026-11-09 | 2026-11-12 | Unknown |
| CVE-2026-19868 | SonicWall / SonicOS SSLVPN | 2026-11-06 | 2026-11-20 | Unknown |

---

*Total entries in CISA KEV catalog: 1779*