# Vulnerability Intelligence Report

**Date:** 2026-10-13  
**Generated:** 2026-10-13T15:35:41Z  

---

## Executive Summary

Our environment faces significant exposure across 292 high-severity vulnerabilities, including two critical-rated flaws in Progress MarkLogic Server (CVSS 9.9) involving authorization bypass and XQuery injection. Six new entries were added to CISA's Known Exploited Vulnerabilities catalog this week, spanning widely deployed products including Ivanti Connect Secure, Apache Struts, and ISC BIND. While no monitored CVEs currently match the KEV catalog, the volume and severity of unresolved vulnerabilities, combined with active exploitation signals from CISA, indicates elevated organizational risk requiring immediate prioritization and remediation action.

---

## Risk Narrative

The current threat landscape reflects a dangerous combination of newly disclosed critical vulnerabilities and actively exploited legacy flaws. Adversaries are targeting well-known platforms—Ivanti, Apache Struts, and ISC BIND—that remain unpatched in many enterprise environments. The two CVSS 9.9 MarkLogic vulnerabilities represent the most immediate business risk, potentially enabling full database compromise and data exfiltration. Deserialization and authentication bypass flaws further expose application layers to unauthorized access. The addition of six CVEs to CISA's KEV catalog signals confirmed, ongoing exploitation in the wild. Without rapid remediation, the organization faces elevated risk of ransomware deployment, data breach, regulatory penalties, and reputational harm.

---

## Prioritized Action Items

1. Immediately patch Progress MarkLogic Server to version 12.1.0 or 11.3.7 to remediate two CVSS 9.9 critical vulnerabilities enabling authorization bypass and XQuery injection.
2. Apply patches or mitigations for all six newly added CISA KEV entries—including Ivanti Connect Secure and Apache Struts—within 24 to 48 hours per federal guidance.
3. Remediate the insecure deserialization vulnerability in Square Squash (CVE-2026-109391, CVSS 8.1) and the improper certificate validation flaw in SWUpdate (CVE-2026-109399, CVSS 8.1) as high-priority items.
4. Address the authentication bypass in Thirty Bees (CVE-2026-109394) and the unrestricted file upload in Thelia (CVE-2026-109397) to prevent unauthenticated access and remote code execution.
5. Conduct a full inventory sweep to identify any instances of CVE-2015-5477 (ISC BIND) and CVE-2016-3081 (Apache Struts) in the environment, as both are legacy vulnerabilities now under active exploitation.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-108899 | 7.3 | 2026-10-12 | A flaw has been found in tobychui zoraxy up to 3.3.4. This impacts the function handleBasicAuth of the file mod/dynamicp |
| CVE-2026-108900 | 7.3 | 2026-10-12 | A vulnerability has been found in Exponent CMS up to 3.0.2patch2. Affected is the function userLogin of the file xmlrpc. |
| CVE-2026-108906 | 7.2 | 2026-10-12 | A vulnerability has been found in Netcore NR268 1.7.121109. This affects the function filter_arp_put_file_cgi of the fil |
| CVE-2026-109391 | 8.1 | 2026-10-12 | Square Squash through commit e73f280 contains an insecure deserialization vulnerability that allows unauthenticated atta |
| CVE-2026-109394 | 7.4 | 2026-10-12 | Thirty bees through 1.7.0 contains an authentication bypass vulnerability in PasswordController::resolveCustomer() that  |
| CVE-2026-109397 | 7.2 | 2026-10-12 | Thelia before 3.1.2 and 3.2.x before 3.2.1 contains an unrestricted file upload vulnerability that allows authenticated  |
| CVE-2026-109398 | 7.5 | 2026-10-12 | Gumlet php-image-resize before 3.0.1 contains a denial of service vulnerability because the ImageResize constructor in l |
| CVE-2026-109399 | 8.1 | 2026-10-12 | SWUpdate through 2026.05.1 contains an improper certificate validation vulnerability in crypto/swupdate_cms_verify_opens |
| CVE-2026-85947 | 9.9 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain an authorization flaw in c |
| CVE-2026-85948 | 9.9 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain an XQuery injection flaw i |
| CVE-2026-85949 | 8.1 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 may record security-sensitive info |
| CVE-2026-85950 | 8.4 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain an authorization flaw that |
| CVE-2026-85951 | 8.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 on Azure contain a server-side req |
| CVE-2026-85952 | 8.5 | 2026-10-12 | Affected Linux-based Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain a ser |
| CVE-2026-85953 | 8.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain privileged legacy InfoStud |
| CVE-2026-85954 | 8.6 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 can evaluate user-controlled value |
| CVE-2026-85955 | 9.9 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 allow a remote attacker with query |
| CVE-2026-85956 | 9.6 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 allow a remote attacker with deleg |
| CVE-2026-9191 | 9.6 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 do not sufficiently isolate user-s |
| CVE-2026-108907 | 10.0 | 2026-10-12 | A vulnerability was determined in Netcore NR268 1.7.121109. Affected is the function user_ok of the component CGI Execut |
| CVE-2026-108914 | 9.9 | 2026-10-12 | A flaw has been found in Edimax BR-6208AC 1.32. Affected by this issue is some unknown functionality of the file /goform |
| CVE-2026-109237 | 8.1 | 2026-10-12 | Crawl4AI from 0.9.0 before 0.9.4 contains an untrusted-config gate bypass that allows non-admin API clients to construct |
| CVE-2026-109238 | 8.6 | 2026-10-12 | Crawl4AI 0.7.0 before 0.9.4 contains a server-side request forgery vulnerability that allows API clients to reach intern |
| CVE-2026-109242 | 7.1 | 2026-10-12 | FreeRDP before 3.0.0 and 3.6.0 before 3.32.0 renders uninitialized heap memory from un-decoded progressive tiles because |
| CVE-2026-109286 | 8.1 | 2026-10-12 | Open WebUI from 0.7.0 before 0.11.4 contains a cross-origin message handling vulnerability in SyncStatsModal that allows |
| CVE-2026-109290 | 7.3 | 2026-10-12 | Open WebUI from 0.11.1 before 0.11.4 contains a stored cross-site scripting vulnerability in DocxPreview.svelte that all |
| CVE-2026-109291 | 7.3 | 2026-10-12 | Open WebUI from 0.6.33 before 0.11.4 contains a cross-site scripting vulnerability that allows authenticated users to ex |
| CVE-2026-109305 | 8.8 | 2026-10-12 | Craft CMS from 5.10.2 before 5.10.14 contains a Twig sandbox bypass that allows non-admin users to invoke PHP callables  |
| CVE-2026-109308 | 8.8 | 2026-10-12 | Craft CMS 4.0.0 before 4.18.7 and 5.0.0 before 5.10.14 passes the raw 'updates' request parameter in AppController::acti |
| CVE-2026-109312 | 8.1 | 2026-10-12 | Grav Login plugin 2.7.0 before 3.9.9 contains an authentication bypass in processUserProfile(), which checks that the se |
| CVE-2026-109313 | 8.1 | 2026-10-12 | Grav Login plugin 2.7.0 before 3.9.9 contains an authentication bypass vulnerability that allows attackers with a valid  |
| CVE-2026-109314 | 7.3 | 2026-10-12 | Grav Login plugin 1.2.0 before 3.9.9 contains an information disclosure vulnerability that allows publishers to obtain p |
| CVE-2026-109317 | 7.2 | 2026-10-12 | Grav grav-plugin-api before 1.0.36 contains a privilege escalation vulnerability that allows delegated user managers to  |
| CVE-2026-109318 | 8.8 | 2026-10-12 | Grav Git Sync 1.0.2 through 3.4.12 contains a command injection vulnerability that allows authenticated content editors  |
| CVE-2026-109321 | 9.1 | 2026-10-12 | Grav Login OAuth plugin (grav-plugin-login-oauth) before 1.4.3 provisions OAuth accounts as ordinary Grav users with a d |
| CVE-2026-109325 | 7.5 | 2026-10-12 | Grav from 2.0.22 before 2.1.7 contains an authentication bypass vulnerability in the Clockwork profiler that trusts loop |
| CVE-2026-109326 | 7.5 | 2026-10-12 | Grav before 2.1.7 contains an information disclosure vulnerability because bundled nginx, lighttpd, IIS, and Caddy 2 con |
| CVE-2026-109331 | 7.4 | 2026-10-12 | Network-AI from 5.14.0 before 5.15.2 contains a security control bypass vulnerability in the ClaudeHookBridge PreToolUse |
| CVE-2026-109334 | 8.1 | 2026-10-12 | SurrealDB before 3.3.0 does not check the caller-selected namespace or database against the level at which a namespace-  |
| CVE-2026-109341 | 7.1 | 2026-10-12 | SurrealDB before 3.3.0 contains an authorization bypass vulnerability that allows callers with table-level write permiss |
| CVE-2026-109343 | 8.1 | 2026-10-12 | SurrealDB before 3.3.0 allows cross-tenant access because the SurrealQL USE statement switches a session to any namespac |
| CVE-2026-109346 | 8.1 | 2026-10-12 | better-auth from 1.3.8-beta.3 before 1.7.0-rc.3 contains a UI misrepresentation vulnerability in the deviceAuthorization |
| CVE-2026-109347 | 7.2 | 2026-10-12 | Adminer before 6.1.1 contains a remote code execution vulnerability that allows authenticated SQLite users to bypass ATT |
| CVE-2026-109353 | 7.1 | 2026-10-12 | LibreNMS before 26.9.0 contains an SQL injection vulnerability that allows unprivileged users to inject SQL by supplying |
| CVE-2026-109357 | 8.1 | 2026-10-12 | LibreNMS before 26.9.0 contains an LDAP filter injection in ldap-authorization and ad-authorization modes because userna |
| CVE-2026-109358 | 7.8 | 2026-10-12 | Edgeless Systems Contrast 1.8.0 before 1.24.1 contains an incorrect permissions vulnerability where the node installer w |
| CVE-2026-109359 | 7.7 | 2026-10-12 | Contrast 1.8.0 before 1.24.1 contains an improper verification vulnerability in Coordinator peer recovery that fails to  |
| CVE-2026-109360 | 7.5 | 2026-10-12 | MONAI 0.4.0 before 1.6.1 contains a remote code execution vulnerability that allows on-path attackers to execute code by |
| CVE-2026-109361 | 7.3 | 2026-10-12 | MONAI 1.2.0 before 1.6.1 contains an insecure deserialization vulnerability in nnUNetV2Runner that unpickles the postpro |
| CVE-2026-109363 | 7.5 | 2026-10-12 | ZcashFoundation Zebra 6.4.0 before 6.4.2 parses version 6 transactions carrying a pre-NU6.3 consensus branch ID, but the |
| CVE-2026-109371 | 8.2 | 2026-10-12 | ZITADEL 3.0.0 before 4.18.0 contains a missing authentication vulnerability in the hosted Login V1 UI, where the change- |
| CVE-2026-109372 | 8.7 | 2026-10-12 | ZITADEL 4.x before 4.19.2 and 3.x through 3.4.15 contains an authentication bypass in the SAML identity-provider intent  |
| CVE-2026-109373 | 8.1 | 2026-10-12 | ZITADEL 3.0.0 before 4.19.2 contains an authentication bypass vulnerability in the Login V2 UI that allows unauthenticat |
| CVE-2026-75888 | 7.7 | 2026-10-12 | A flaw was found in the OpenShift console. An authenticated console user can exploit a Server-Side Request Forgery (SSRF |
| CVE-2026-85957 | 7.5 | 2026-10-12 | Affected Progress MarkLogic Server 11.x releases before 11.3.7 use a SAML parser configuration that can process external |
| CVE-2026-85958 | 7.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain an authentication validati |
| CVE-2026-85959 | 7.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 do not consistently record success |
| CVE-2026-85960 | 7.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 use predictable CSRF tokens in Que |
| CVE-2026-85961 | 7.5 | 2026-10-12 | On Azure deployments, Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 may record s |
| CVE-2026-85962 | 7.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain an improper authentication |
| CVE-2026-85963 | 7.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 include deprecated OpsDirector fun |
| CVE-2026-85964 | 7.7 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 allow an authenticated Query Conso |
| CVE-2026-85965 | 8.0 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain memory-safety defects in t |
| CVE-2026-85966 | 7.7 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 do not sufficiently restrict acces |
| CVE-2026-85968 | 7.1 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 contain an out-of-bounds read vulnerability in certain query-proce |
| CVE-2026-85969 | 7.1 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 contain an out-of-bounds write vul |
| CVE-2026-85970 | 7.1 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 enable XML external entity process |
| CVE-2026-85971 | 7.1 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 assign overly permissive operating |
| CVE-2026-85972 | 7.4 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 do not sufficiently verify the ide |
| CVE-2026-85973 | 7.4 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 may use cleartext transport for certain cluster-management communi |
| CVE-2026-85974 | 7.4 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 do not consistently validate TLS c |
| CVE-2026-85975 | 7.5 | 2026-10-12 | Progress MarkLogic Server 12.x releases before 12.1.0 and 11.x releases before 11.3.7 may use cleartext transport for Am |
| CVE-2026-108479 | 8.1 | 2026-10-12 | Cross-Site Request Forgery (CSRF) vulnerability in Patreon Patreon WordPress patreon-connect allows Cross Site Request F |
| CVE-2026-108481 | 7.4 | 2026-10-12 | Cross-Site Request Forgery (CSRF) vulnerability in Patreon Patreon WordPress patreon-connect allows Cross Site Request F |
| CVE-2026-108915 | 9.9 | 2026-10-12 | A vulnerability has been found in Edimax BR-6208AC 1.32. This affects an unknown part of the file /goform/formWlanMP. Su |
| CVE-2026-108916 | 8.3 | 2026-10-12 | A vulnerability was found in Edimax BR-6208AC 1.32. This vulnerability affects unknown code of the file /goform/formAcce |
| CVE-2026-108917 | 10.0 | 2026-10-12 | A vulnerability was determined in Edimax BR-6208AC 1.32. This issue affects some unknown processing of the file /goform/ |
| CVE-2026-108918 | 10.0 | 2026-10-12 | A vulnerability was identified in Edimax BR-6208AC 1.32. Impacted is an unknown function of the file /goform/formWlanMP. |
| CVE-2026-77363 | 8.8 | 2026-10-12 | obsidian-tc is a governed, agent-ready Model Context Protocol server for Obsidian vaults. Prior to 1.3.1, the Streamable |
| CVE-2026-77366 | 9.9 | 2026-10-12 | obsidian-tc is a governed, agent-ready Model Context Protocol server for Obsidian vaults. Prior to 1.3.1, tool dispatch  |
| CVE-2026-105464 | 8.8 | 2026-10-12 | IBM Db2 11.5.0 through 11.5.9, and 12.1.0 through 12.1.5 for Linux, UNIX and Windows (includes DB2 Connect Server) could |
| CVE-2026-105465 | 8.8 | 2026-10-12 | IBM Db2 11.5.0 through 11.5.9, and 12.1.0 through 12.1.5 is vulnerable to privilege escalation when db2locssh is enabled |
| CVE-2026-108921 | 7.3 | 2026-10-12 | A vulnerability was detected in KusalkaSilva Learning-Management-System up to ffeb873f8803f1e9664384ff75000c7da45466d2.  |
| CVE-2026-18166 | 7.7 | 2026-10-12 | IBM Db2 11.5.0 through 11.5.9, and 12.1.0 through 12.1.5 for Linux, UNIX and Windows (includes DB2 Connect Server) could |
| CVE-2026-57118 | 9.8 | 2026-10-12 | PraisonAI is a multi-agent teams system. Prior to praisonaiagents 1.6.59, AgentTeam.launch and the Agents alias register |
| CVE-2026-57143 | 8.8 | 2026-10-12 | PraisonAI is a multi-agent teams system. Prior to praisonaiagents 1.6.62, searxng_search and the search_web SearxNG prov |
| CVE-2026-59976 | 8.1 | 2026-10-12 | ConvertX is a self-hosted file conversion service. Prior to 0.18.0, the ImageMagick converter uses the unsanitized conve |
| CVE-2026-59977 | 8.1 | 2026-10-12 | ConvertX is a self-hosted file conversion service. Prior to 0.18.0, the /delete/{id} endpoint uses HTTP GET for permanen |
| CVE-2026-65954 | 8.6 | 2026-10-12 | PHPCSUtils is a suite of utility functions for use with PHP_CodeSniffer. From 1.0.0-alpha1 until 1.2.3, PHPCSUtils\Abstr |
| CVE-2026-83535 | 7.4 | 2026-10-12 | A flaw was found in openstack-network-exporter. When an operator configures user authentication but omits or misconfigur |
| CVE-2026-87744 | 9.1 | 2026-10-12 | A flaw was found in Quarkus REST Data Panache. This vulnerability allows unauthenticated attackers to bypass security co |
| CVE-2026-109422 | 8.1 | 2026-10-12 | NetEase Cloud Music client for Windows (cloudmusic.exe) versions 3.1.38 and 3.1.39.205426 contains a remote code executi |
| CVE-2026-109423 | 7.4 | 2026-10-12 | NetEase Cloud Music client for Windows (cloudmusic.exe) versions 3.1.38 and 3.1.39.205426 contains a TLS certificate val |
| CVE-2026-109575 | 9.8 | 2026-10-12 | In HAProxy Data Plane API 2.2.0 through 3.4.3 (and corresponding Enterprise Edition releases), Server.ConfigureAPI() has |
| CVE-2026-41510 | 7.2 | 2026-10-12 | OWASP Coraza WAF is a golang modsecurity compatible web application firewall library. From 3.0.0 until 3.8.1, Coraza sil |
| CVE-2026-95837 | 7.8 | 2026-10-12 | containerd is an open-source container runtime. From 2.1.0 until 2.2.7 and 2.3.4, containerd's CRI CreateContainer check |
| CVE-2026-96012 | 9.9 | 2026-10-12 | IBM Db2 Mirror for i 7.4, 7.5, and 7.6 is vulnerable to privilege escalation. An authenticated attacker could craft a ma |
| CVE-2020-37279 | 8.1 | 2026-10-12 | easy-pdf-merge 0.1.0 through 0.2.6 contains an OS command injection vulnerability that allows attackers to execute comma |
| CVE-2020-37280 | 7.5 | 2026-10-12 | cbor-sync through 1.0.4 contains a resource exhaustion vulnerability in CBOR.decode that trusts declared array and map l |
| CVE-2021-48011 | 7.5 | 2026-10-12 | Servor 1.0.0 through 4.0.2 contains a path traversal vulnerability that allows unauthenticated remote attackers to escap |
| CVE-2021-48012 | 8.2 | 2026-10-12 | fast-toml through 0.5.4 contains a prototype pollution vulnerability that allows attackers to modify Object.prototype by |
| CVE-2025-71429 | 9.8 | 2026-10-12 | GPT-SoVITS through 20250606v2pro contains an OS command injection vulnerability in tools/uvr5/vr.py that allows unauthen |
| CVE-2026-105052 | 7.5 | 2026-10-12 | IBM Maximo Application Suite 8.10, 8.11, 9.0, 9.1, and 9.2 could allow a remote attacker to traverse directories on the  |
| CVE-2026-108929 | 9.9 | 2026-10-12 | A flaw has been found in Netcore NR268 1.7.121109. The affected element is the function execvp of the file /router/DDNSs |
| CVE-2026-109380 | 7.5 | 2026-10-12 | modern-tar 0.3.5 through 0.8.5 contains a memory exhaustion vulnerability that allows attackers to produce negative entr |
| CVE-2026-109426 | 7.5 | 2026-10-12 | Telegram-Stremio through 5.1.0 contains an insecure storage vulnerability that allows attackers with access to the Mongo |
| CVE-2026-109556 | 8.0 | 2026-10-12 | EdgeEver Desktop 1.92.0 through 1.112.0 contains a remote code execution vulnerability in the desktop:acp-probe IPC hand |
| CVE-2026-109557 | 8.7 | 2026-10-12 | EdgeEver through 1.112.0 contains a stored cross-site scripting vulnerability in setMemoDragPreview that allows attacker |
| CVE-2026-109558 | 8.7 | 2026-10-12 | EdgeEver 1.6.0 through 1.112.0 contains a stored cross-site scripting vulnerability in TemplatesPane.tsx that renders te |
| CVE-2026-109559 | 8.7 | 2026-10-12 | EdgeEver Desktop 1.6.26 through 1.112.0 contains a navigation allowlist bypass that lets attackers load arbitrary origin |
| CVE-2026-109560 | 7.5 | 2026-10-12 | Continue CLI (@continuedev/cli) through 1.5.47 contains a permission bypass vulnerability that allows attackers to run u |
| CVE-2026-109563 | 7.5 | 2026-10-12 | N3.js before 2.11.1 contains a regular expression denial of service vulnerability in the N3Lexer number pattern that bac |
| CVE-2026-109566 | 9.8 | 2026-10-12 | Rapyd Admin from 9.0.0 before 9.20.0 contains a hard-coded credentials vulnerability that allows remote unauthenticated  |
| CVE-2026-109567 | 7.2 | 2026-10-12 | Rapyd Admin from 9.0.0 before 9.20.0 contains an improper privilege management vulnerability in the UsersEdit Livewire c |
| CVE-2026-109568 | 7.1 | 2026-10-12 | Shaark 1.2.13 through 1.2.44 contains a missing authorization vulnerability in the Link, Story, Chest and Album API cont |
| CVE-2026-109569 | 8.8 | 2026-10-12 | sandboxed.sh through 1.3.0 contains a container escape vulnerability that allows code in container workspaces to access  |
| CVE-2026-18513 | 7.2 | 2026-10-12 | IBM Maximo Application Suite - Location Service for Esri Component 9.2, 9.1, and 9.0 is vulnerable to improper access co |
| CVE-2026-18517 | 7.7 | 2026-10-12 | IBM Maximo Application Suite - Location Service for Esri Component 9.2, 9.1, and 9.0 IBM Maximo Application Suite — Loca |
| CVE-2026-18529 | 8.7 | 2026-10-12 | IBM Maximo Application Suite - Location Service for Esri Component 9.2, 9.1, and 9.0 is vulnerable to command injection  |
| CVE-2026-18537 | 8.7 | 2026-10-12 | IBM Maximo Application Suite - Location Service for Esri Component 9.2, 9.1, and 9.0 is vulnerable to improper input val |
| CVE-2026-53997 | 7.4 | 2026-10-12 | Netherman Portal del Hermano (portaldelhermano.es) before 2026-10-06 contains a broken authentication vulnerability in i |
| CVE-2026-75881 | 7.5 | 2026-10-12 | IBM Maximo Application Suite - IoT Component 9.2.0, 9.1.0, and 9.0.0 could allow a remote attacker to cause a denial of  |
| CVE-2026-78673 | 7.5 | 2026-10-12 | IBM Maximo AI Service 9.1.0, and 9.2.0 could allow a remote attacker to cause a denial of service due to improper input  |
| CVE-2026-84313 | 8.8 | 2026-10-12 | Nginx UI is a web user interface for the Nginx web server. Prior to 2.4.1, POST /api/otp_enroll and POST /api/finish_pas |
| CVE-2026-84315 | 8.3 | 2026-10-12 | Nginx UI is a web user interface for the Nginx web server. Prior to 2.4.1, Nginx UI does not apply RequireSecureSession  |
| CVE-2026-84316 | 8.8 | 2026-10-12 | Nginx UI is a web user interface for the Nginx web server. Prior to 2.4.1, config.ValidateConfigDirectives splits config |
| CVE-2026-84317 | 8.8 | 2026-10-12 | Nginx UI is a web user interface for the Nginx web server. Prior to 2.4.1, internal/config/validation.go (ValidateConfig |
| CVE-2026-84318 | 8.8 | 2026-10-12 | Nginx UI is a web user interface for the Nginx web server. From 2.0.0-rc.6 until 2.4.1, the MCP tool nginx_config_add wr |
| CVE-2026-84319 | 8.3 | 2026-10-12 | Nginx UI is a web user interface for the Nginx web server. Prior to 2.4.1, the regular HTTP configuration API rejects re |
| CVE-2026-84360 | 8.1 | 2026-10-12 | Nginx UI is a web user interface for the Nginx web server. Prior to 2.4.1, the HTTP configuration mutation routes requir |
| CVE-2026-96261 | 7.3 | 2026-10-12 | IBM Power Systems Firmware FW1060.00 through FW1060.81 is affected by a vulnerability in host firmware configuration par |
| CVE-2026-96262 | 8.2 | 2026-10-12 | IBM Power Systems Firmware FW1060.00 through FW1060.81 is affected by a vulnerability in the service processor mailbox i |
| CVE-2026-96263 | 8.2 | 2026-10-12 | IBM Power Systems Firmware FW1120.00 through FW1120.01, FW1110.00 through FW1110.31, and FW1060.00 through FW1060.81 is  |
| CVE-2026-96264 | 8.2 | 2026-10-12 | IBM Power Systems Firmware FW1060.00 through FW1060.81  is affected by a vulnerability in the service processor mailbox  |
| CVE-2026-96265 | 8.2 | 2026-10-12 | IBM Power Systems Firmware FW1060.00 through FW1060.81 is affected by a vulnerability in the service processor mailbox i |
| CVE-2026-96266 | 8.2 | 2026-10-12 | IBM Power Systems Firmware FW1060.00 through FW1060.81 is affected by a vulnerability in host firmware configuration par |
| CVE-2026-84312 | 7.1 | 2026-10-12 | Nginx UI is a web user interface for the Nginx web server. Prior to 2.4.1, GetCasdoorUri uses the configured Casdoor app |
| CVE-2026-90911 | 7.5 | 2026-10-12 | IBM Maximo AI Service 9.1.0, and 9.2.0 could allow a remote attacker to cause a denial of service due to uncontrolled re |
| CVE-2026-90912 | 7.5 | 2026-10-12 | IBM Maximo AI Service 9.1.0, and 9.2.0 SaaS could allow a remote attacker to cause a denial of service due to uncontroll |
| CVE-2026-90920 | 9.8 | 2026-10-12 | IBM Maximo AI Service 9.1.0, and 9.2.0 could allow a remote attacker to execute arbitrary code due to improper control o |
| CVE-2026-90921 | 7.5 | 2026-10-12 | IBM Maximo AI Service 9.1.0, and 9.2.0 could allow a remote attacker to cause a denial of service due to improper handli |
| CVE-2026-92876 | 7.5 | 2026-10-12 | IBM Maximo Application Suite - IoT Component 9.2.0, 9.1.0, and 9.0.0 could allow a remote attacker to cause a denial of  |
| CVE-2024-58390 | 8.8 | 2026-10-12 | Frappe before 14.81.4 and 15.x before 15.41.0 contains an improper privilege management vulnerability involving a certai |
| CVE-2025-71432 | 8.1 | 2026-10-12 | Frappe ERPNext before 14.92.1 and 15.x before 15.83.0 contains a reflected cross-site scripting vulnerability due to mis |
| CVE-2026-102627 | 8.8 | 2026-10-12 | IBM TRIRIGA Application Platform 5.0.0 through 5.0.8 could allow a remote authenticated attacker to execute arbitrary co |
| CVE-2026-109572 | 7.6 | 2026-10-12 | Open WebUI from 0.8.6 before 0.11.4 contains a privilege escalation vulnerability in the terminal proxy that allows auth |
| CVE-2026-109573 | 8.1 | 2026-10-12 | phpMyFAQ before 4.1.9 contains an SQL injection vulnerability in PdoMysql::escape(), which escapes single quotes with ba |
| CVE-2026-109604 | 7.3 | 2026-10-12 | Frappe ERPNext before 15.112.0 and 16.x before 16.23.0 contains a stored cross-site scripting vulnerability because a to |
| CVE-2026-109608 | 8.8 | 2026-10-12 | Frappe ERPNext before 15.121.0 and 16.x before 16.34.0 contains an SQL injection vulnerability in several endpoints that |
| CVE-2026-109612 | 7.3 | 2026-10-12 | Frappe ERPNext before 15.120.0 and 16.x before 16.33.0 contains a stored cross-site scripting vulnerability in a report  |
| CVE-2026-109613 | 7.1 | 2026-10-12 | Frappe ERPNext before 15.121.0 and 16.x before 16.34.0 contains a missing authorization vulnerability in which certain e |
| CVE-2026-109616 | 7.1 | 2026-10-12 | Frappe ERPNext before 15.121.3 and 16.x before 16.35.0 contains a missing authorization vulnerability in which certain e |
| CVE-2026-109617 | 7.1 | 2026-10-12 | Frappe ERPNext before 15.121.0 and 16.x before 16.34.0 contains a missing authorization vulnerability in certain endpoin |
| CVE-2026-109633 | 8.1 | 2026-10-12 | Frappe ERPNext before 15.119.1 and 16.x before 16.32.0 contains a stored cross-site scripting vulnerability because cont |
| CVE-2026-109640 | 8.1 | 2026-10-12 | Frappe ERPNext before 16.22.0 contains a missing authorization vulnerability that allows authenticated users to modify r |
| CVE-2026-109652 | 8.8 | 2026-10-12 | Frappe ERPNext before 15.119.1 and 16.x before 16.32.0 contains a server-side template injection vulnerability because u |
| CVE-2026-109653 | 7.3 | 2026-10-12 | Frappe ERPNext before 15.119.0 and 16.x before 16.31.0 contains a stored cross-site scripting vulnerability because reco |
| CVE-2026-109667 | 8.8 | 2026-10-12 | Frappe ERPNext before 15.111.0 and 16.x before 16.22.0 contains a privilege escalation vulnerability in a record-creatio |
| CVE-2026-109671 | 7.3 | 2026-10-12 | Frappe ERPNext before 15.113.0 and 16.x before 16.24.0 contains a stored cross-site scripting vulnerability in a profile |
| CVE-2026-109673 | 7.3 | 2026-10-12 | Frappe ERPNext before 15.103.0 and 16.x before 16.12.0 contains a stored cross-site scripting vulnerability because the  |
| CVE-2026-17475 | 7.1 | 2026-10-12 | IBM Planning Analytics 2.0, and 2.1 could allow a remote authenticated attacker to delete folders and applications belon |
| CVE-2026-19620 | 8.8 | 2026-10-12 | IBM Planning Analytics 2.0, and 2.1 could allow a remote attacker to gain unauthorized administrative access due to impr |
| CVE-2026-19622 | 8.8 | 2026-10-12 | IBM Planning Analytics 2.0, and 2.1 could allow a remote attacker to bypass authentication and escalate privileges due t |
| CVE-2026-19627 | 8.2 | 2026-10-12 | IBM Planning Analytics 2.0, and 2.1 could allow a remote attacker to read arbitrary host files and overwrite certain app |
| CVE-2026-75061 | 7.5 | 2026-10-12 | IBM Planning Analytics 2.0, and 2.1 could allow a remote attacker to traverse directories on the system. An attacker cou |
| CVE-2026-75095 | 7.5 | 2026-10-12 | IBM Aspera Enterprise WebApps 1.0.0 through 1.0.6 could allow a remote attacker to cause a denial of service due to unco |
| CVE-2026-75782 | 7.8 | 2026-10-12 | IBM Aspera Enterprise WebApps 1.0.0 through 1.0.6 could allow a local attacker to gain elevated privileges due to a misc |
| CVE-2026-82096 | 8.8 | 2026-10-12 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary commands du |
| CVE-2026-82101 | 9.6 | 2026-10-12 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to cause a denial of service due |
| CVE-2026-82103 | 9.6 | 2026-10-12 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to obtain sensitive information  |
| CVE-2026-82108 | 8.8 | 2026-10-12 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary code due to |
| CVE-2026-82110 | 9.6 | 2026-10-12 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary code due to |
| CVE-2026-84418 | 7.4 | 2026-10-12 | IBM DataStage on Cloud Pak for Data 5.4.0.0 can allow a man-in-the-middle attacker to present a forged TLS certificate,  |
| CVE-2026-85457 | 8.1 | 2026-10-12 | IBM Planning Analytics 2.0, and 2.1 could allow a remote authenticated attacker to execute arbitrary code due to a stack |
| CVE-2026-93891 | 7.6 | 2026-10-12 | IBM TRIRIGA Application Platform 5.0.0 through 5.0.8 could allow a remote authenticated attacker to obtain sensitive inf |
| CVE-2026-93892 | 8.1 | 2026-10-12 | IBM TRIRIGA Application Platform 5.0.0 through 5.0.8 could allow a remote authenticated attacker to obtain sensitive inf |
| CVE-2026-93886 | 8.3 | 2026-10-13 | IBM i 7.3, 7.4, 7.5, and 7.6 could allow a remote authenticated attacker to execute arbitrary script code due to imprope |
| CVE-2026-96119 | 9.9 | 2026-10-13 | IBM i 7.3, 7.4, 7.5, and 7.6 could allow a remote authenticated attacker to obtain sensitive information or execute arbi |
| CVE-2026-58249 | 7.5 | 2026-10-13 | SAP NetWeaver and SAP Web Dispatcher do not properly validate certain fields in specially crafted requests handled by an |
| CVE-2026-87689 | 9.8 | 2026-10-13 | The Metasploit Framework Web Service REST API (msf-ws) exposes the credential store through Msf::WebServices::Credential |
| CVE-2026-89107 | 9.9 | 2026-10-13 | SAP S/4HANA (Manage Substitution/Validation Rules) does not sufficiently validate input processed by rule definition fun |
| CVE-2026-89108 | 9.1 | 2026-10-13 | SAP Manufacturing Integration and Intelligence does not sufficiently enforce authorization boundaries within certain adm |
| CVE-2026-89110 | 9.9 | 2026-10-13 | SAP NetWeaver Visual Composer does not perform sufficient authorization checks in certain portal functionality. An attac |
| CVE-2026-89111 | 10.0 | 2026-10-13 | The SAP Cloud SDK for Python contains an OAuth2 SSRF vulnerability affecting multi-tenant BTP applications. An attacker  |
| CVE-2026-89113 | 8.8 | 2026-10-13 | SAP Commerce Cloud does not sufficiently validate certain user-supplied input before it is incorporated into a database  |
| CVE-2026-89120 | 7.1 | 2026-10-13 | A regression caused by an API change in SAP ABAP Platform reintroduces a previously fixed authorization weakness. The se |
| CVE-2026-108956 | 7.3 | 2026-10-13 | A vulnerability was identified in code-projects Online Reviewer System 1.0. The affected element is an unknown function  |
| CVE-2026-14814 | 8.2 | 2026-10-13 | GitLab has remediated an issue in GitLab CE/EE affecting all versions before 19.2.8, 19.3 before 19.3.5, and 19.4 before |
| CVE-2026-16301 | 8.5 | 2026-10-13 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 18.7 before 19.2.8, 19.3 before 19.3.5, and 1 |
| CVE-2026-35001 | 7.8 | 2026-10-13 | OpenS100 through commit daa35b contains an integer overflow vulnerability in the S-102 Bathymetric Surface parser that a |
| CVE-2026-81839 | 7.7 | 2026-10-13 | GitLab has remediated an issue in GitLab EE affecting all versions from 18.1 before 19.2.8, 19.3 before 19.3.5, and 19.4 |
| CVE-2026-92883 | 8.7 | 2026-10-13 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 19.1 before 19.2.8, 19.3 before 19.3.5, and 1 |
| CVE-2026-96893 | 7.3 | 2026-10-13 | GitLab has remediated an issue in GitLab EE affecting all versions from 19.1 before 19.2.8, 19.3 before 19.3.5, and 19.4 |
| CVE-2026-97229 | 10.0 | 2026-10-13 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 19.2 before 19.2.8, 19.3 before 19.3.5, and 1 |
| CVE-2026-108964 | 7.3 | 2026-10-13 | A vulnerability was found in SourceCodester Performance Indicator System 1.0. This affects an unknown part of the file / |
| CVE-2026-108965 | 7.3 | 2026-10-13 | A vulnerability was determined in SourceCodester Performance Indicator System 1.0. This vulnerability affects unknown co |
| CVE-2026-108966 | 7.3 | 2026-10-13 | A vulnerability was identified in SourceCodester Performance Indicator System 1.0. This issue affects some unknown proce |
| CVE-2026-108967 | 7.3 | 2026-10-13 | A security flaw has been discovered in SourceCodester Performance Indicator System 1.0. Impacted is an unknown function  |
| CVE-2026-108968 | 7.3 | 2026-10-13 | A weakness has been identified in SourceCodester Performance Indicator System 1.0. The affected element is an unknown fu |
| CVE-2026-108969 | 7.3 | 2026-10-13 | A security vulnerability has been detected in itsmeravitejak Online-Examination-System up to e6208e630b14657999bbfe4c991 |
| CVE-2026-108970 | 7.3 | 2026-10-13 | A vulnerability was detected in itsmeravitejak Online-Examination-System up to e6208e630b14657999bbfe4c9912302d2a1e2449. |
| CVE-2026-108971 | 9.6 | 2026-10-13 | A flaw has been found in D-Link DCS-930L B1.08B4. This impacts the function mpfd_decode of the file bootloader_region.bi |
| CVE-2026-108972 | 7.3 | 2026-10-13 | A vulnerability was found in SourceCodester Human Resource Management System 1.0. Affected by this vulnerability is the  |
| CVE-2026-103316 | 7.1 | 2026-10-13 | The macOS version of the DigiD app is not signed with Hardened Runtime. As a result, a local process can load its own dy |
| CVE-2026-108973 | 7.3 | 2026-10-13 | A vulnerability was determined in SourceCodester Contact Tracing System 1.0. Affected by this issue is the function move |
| CVE-2026-108974 | 7.3 | 2026-10-13 | A vulnerability was identified in SourceCodester E-Learning System 1.0. This affects the function save_users of the file |
| CVE-2026-108975 | 7.3 | 2026-10-13 | A security flaw has been discovered in SourceCodester Library Management System 1.0. This vulnerability affects the func |
| CVE-2026-102007 | 7.2 | 2026-10-13 | The Bit integrations – Form Integration, Webhook, Spreadsheets, CRM, LMS & Email Automation plugin for WordPress is vuln |
| CVE-2026-102562 | 7.2 | 2026-10-13 | The AcyMailing plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the customField[] parameter of the  |
| CVE-2026-103418 | 8.8 | 2026-10-13 | Firefox for iOS directly interpolated the page’s HTML language attribute into translation JavaScript, allowing attacker- |
| CVE-2026-109108 | 9.9 | 2026-10-13 | A security vulnerability has been detected in Wavlink WL-WN530BE1-A 251117. This affects the function popen of the file  |
| CVE-2026-109109 | 10.0 | 2026-10-13 | A vulnerability was detected in Wavlink WL-WN530BE1-A 251117. This vulnerability affects the function strcpy of the file |
| CVE-2026-101020 | 7.8 | 2026-10-13 | An incorrect permission assignment for critical resource issue exists in AssetView, AssetView CLOUD, and AssetView Cloud |
| CVE-2026-108179 | 7.6 | 2026-10-13 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in PluginUs.Net WOLF  |
| CVE-2026-109110 | 10.0 | 2026-10-13 | A flaw has been found in Wavlink WL-WN592AX6 250422. This issue affects the function system of the component wmapd Daemo |
| CVE-2026-109114 | 7.3 | 2026-10-13 | A vulnerability has been found in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff |
| CVE-2026-109115 | 7.3 | 2026-10-13 | A vulnerability was found in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff6b9c. |
| CVE-2026-109116 | 7.3 | 2026-10-13 | A vulnerability was determined in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff |
| CVE-2026-109687 | 7.6 | 2026-10-13 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Link Whisper INC L |
| CVE-2026-13138 | 8.6 | 2026-10-13 | Client-Side Enforcement of Server-Side Security vulnerability in Divasoft Software and E-Commerce Inc. Biletiva Ticketin |
| CVE-2026-102073 | 8.2 | 2026-10-13 | A vulnerability has been identified in APOGEE MBC (PPC) (BACnet) (All versions), APOGEE MBC (PPC) (P2 Ethernet) (All ver |
| CVE-2026-102074 | 7.5 | 2026-10-13 | A vulnerability has been identified in APOGEE MBC (PPC) (BACnet) (All versions), APOGEE MBC (PPC) (P2 Ethernet) (All ver |
| CVE-2026-102075 | 7.5 | 2026-10-13 | A vulnerability has been identified in APOGEE MBC (PPC) (BACnet) (All versions), APOGEE MBC (PPC) (P2 Ethernet) (All ver |
| CVE-2026-102076 | 7.5 | 2026-10-13 | A vulnerability has been identified in APOGEE MBC (PPC) (BACnet) (All versions), APOGEE MBC (PPC) (P2 Ethernet) (All ver |
| CVE-2026-44415 | 9.1 | 2026-10-13 | Affected systems do not properly restrict access to internal APIs and paths for authenticated users. This could allow an |
| CVE-2026-59241 | 8.8 | 2026-10-13 | A vulnerability has been identified in SIMATIC WinCC V7.5 (All versions), SIMATIC WinCC V8.0 (All versions < V8.0 Update |
| CVE-2026-63350 | 9.6 | 2026-10-13 | Affected devices do not properly restrict executable content contained in imported trace files.

This could allow an a |
| CVE-2026-63353 | 9.6 | 2026-10-13 | Affected devices do not properly sanitize comment fields contained in imported trace files before rendering them on the  |
| CVE-2026-63354 | 9.6 | 2026-10-13 | Affected devices do not properly validate and sanitize visual marker data contained in imported CSV trace files before r |
| CVE-2026-72895 | 7.7 | 2026-10-13 | A vulnerability has been identified in SIMATIC IPC BX-21A (All versions < V31.01.13), SIMATIC IPC RW-543A (All versions  |
| CVE-2026-78556 | 7.4 | 2026-10-13 | A vulnerability has been identified in Industrial Edge App Publisher (All versions < V1.27.9). The affected software doe |
| CVE-2026-78557 | 8.3 | 2026-10-13 | A vulnerability has been identified in Industrial Edge App Publisher (All versions < V1.27.9). The application fails to  |
| CVE-2026-85114 | 7.5 | 2026-10-13 | A vulnerability has been identified in .NET Client Library for SIMATIC S7 Webserver API (All versions < V3.3.61). Affect |
| CVE-2026-89196 | 8.8 | 2026-10-13 | A vulnerability has been identified in RUGGEDCOM CROSSBOW (All versions < V6.0). Affected devices do not properly valida |
| CVE-2026-89197 | 8.8 | 2026-10-13 | A vulnerability has been identified in RUGGEDCOM CROSSBOW (All versions < V6.0). Affected devices do not properly valida |
| CVE-2026-89198 | 8.8 | 2026-10-13 | A vulnerability has been identified in RUGGEDCOM CROSSBOW (All versions < V6.0). Affected devices do not properly valida |
| CVE-2026-89199 | 8.8 | 2026-10-13 | A vulnerability has been identified in RUGGEDCOM CROSSBOW (All versions < V6.0). Affected devices do not properly restri |
| CVE-2026-89201 | 7.5 | 2026-10-13 | A vulnerability has been identified in RUGGEDCOM CROSSBOW (All versions < V6.0). Affected devices do not properly valida |
| CVE-2026-109157 | 9.9 | 2026-10-13 | A vulnerability was found in TRENDnet TEW-432BRP 3.10B20. Affected by this vulnerability is the function formTcpipSetup  |
| CVE-2026-109832 | 7.5 | 2026-10-13 | A flaw was found in gnome-remote-desktop as shipped in Red Hat Enterprise Linux. In the VNC TLS I/O handlers, retryable  |
| CVE-2026-109403 | 7.3 | 2026-10-13 | A vulnerability was determined in conductor-oss conductor up to 3.32.5. Affected by this vulnerability is the function A |
| CVE-2026-109405 | 7.3 | 2026-10-13 | A security flaw has been discovered in conductor-oss conductor up to 3.33.0-rc10. This affects the function KafkaPublish |
| CVE-2026-109705 | 9.6 | 2026-10-13 | Sandbox escape, site isolation issue due to incorrect boundary conditions, use-after-free in the Networking component. T |
| CVE-2026-109707 | 9.6 | 2026-10-13 | Sandbox escape due to use-after-free in the Networking component. This vulnerability was fixed in Firefox 158 and Firefo |
| CVE-2026-109709 | 8.8 | 2026-10-13 | Information disclosure, privilege escalation in the Security: Process Sandboxing component. This vulnerability was fixed |
| CVE-2026-109756 | 8.8 | 2026-10-13 | Privilege escalation in the DOM: Navigation component. This vulnerability was fixed in Firefox 158 and Firefox ESR 153.5 |
| CVE-2026-109778 | 8.8 | 2026-10-13 | Privilege escalation in the WebExtensions component. This vulnerability was fixed in Firefox 158 and Firefox ESR 153.5. |
| CVE-2026-65101 | 8.6 | 2026-10-13 | NVIDIA AIStore for Linux contains a vulnerability in the distributed sort component where an attacker could cause server |
| CVE-2026-65103 | 8.1 | 2026-10-13 | NVIDIA AIStore for Linux contains a path traversal vulnerability in the target-side object rename handler, where an unau |
| CVE-2026-65104 | 7.1 | 2026-10-13 | NVIDIA Megatron-LM for all platforms contains a vulnerability in inference, where an attacker could cause hash collision |
| CVE-2026-65110 | 7.8 | 2026-10-13 | NVIDIA Megatron-LM contains a vulnerability in checkpoint loading where, an attacker could cause an RCE by convincing a  |
| CVE-2026-65141 | 7.8 | 2026-10-13 | NVIDIA Isaac Lab contains a vulnerability where an attacker could cause an eval injection. A successful exploit of this  |
| CVE-2026-65147 | 7.3 | 2026-10-13 | NVIDIA DALI contains a vulnerability where an attacker could cause an uncontrolled out-of-bounds read. A successful expl |
| CVE-2026-65148 | 7.3 | 2026-10-13 | NVIDIA DALI contains a vulnerability where an attacker could cause a stack-based buffer overflow. A successful exploit o |
| CVE-2026-65149 | 7.3 | 2026-10-13 | NVIDIA DALI contains a vulnerability where an attacker could cause an uncontrolled out-of-bounds write. A successful exp |
| CVE-2026-65150 | 7.3 | 2026-10-13 | NVIDIA DALI contains a vulnerability where an attacker could cause an uncontrolled out-of-bounds read. A successful expl |
| CVE-2026-65161 | 7.5 | 2026-10-13 | NVIDIA AIStore for Linux contains a vulnerability in the Promote API where an unauthenticated remote attacker may read f |
| CVE-2026-65162 | 10.0 | 2026-10-13 | NVIDIA AIStore for Linux contains a vulnerability in the legacy ETL Kubernetes PodSpec initialization API where a remote |
| CVE-2026-65164 | 8.1 | 2026-10-13 | NVIDIA AIStore for Linux contains a path traversal vulnerability in the dSort archive extraction component where a remot |
| CVE-2026-65170 | 8.6 | 2026-10-13 | NVIDIA AIStore for Linux contains a vulnerability in the experimental HT backend where an unauthenticated remote attacke |
| CVE-2026-65172 | 8.6 | 2026-10-13 | NVIDIA AIStore for Linux and Kubernetes contains a missing authorization vulnerability in the ETL management API where a |
| CVE-2026-65173 | 9.1 | 2026-10-13 | NVIDIA AIStore for Linux contains a missing authentication vulnerability in the token-revocation endpoint where an unaut |
| CVE-2026-65180 | 7.8 | 2026-10-13 | NVIDIA Megatron-LM contains a vulnerability in checkpoint loading where an Attacker may cause an RCE by convincing a use |
| CVE-2026-103499 | 7.5 | 2026-10-13 | IBM WebSphere Application Server - Liberty 17.0.0.3 through 26.0.0.10 and IBM WebSphere Application Server 8.5, and 9.0  |
| CVE-2026-109519 | 8.3 | 2026-10-13 | A vulnerability was detected in YouTransfer up to 0.0.7/1.0.6/1.1.0. Affected is an unknown function of the file /settin |
| CVE-2026-109520 | 8.8 | 2026-10-13 | A flaw has been found in Colorful iGameCenter 2.0.0.82. Affected by this vulnerability is the function MmMapIoSpace in t |
| CVE-2026-109676 | 8.8 | 2026-10-13 | FreeRDP from 3.0.0-beta1 before 3.32.0 contains a use-after-free vulnerability in smartcard handling that allows attacke |
| CVE-2026-109956 | 7.0 | 2026-10-13 | NLTK through 3.10.3 contains a path traversal vulnerability in WekaClassifier that allows attackers to bypass nltk.paths |
| CVE-2026-109960 | 7.7 | 2026-10-13 | Froxlor 2.0.0 before 2.3.14 contains a stored cross-site scripting vulnerability that allows authenticated customers to  |
| CVE-2026-109961 | 8.5 | 2026-10-13 | Froxlor 0.10.0 before 2.3.14 contains a newline injection vulnerability that allows authenticated customers to inject ar |
| CVE-2026-109965 | 7.1 | 2026-10-13 | Serena before 2.0.0 contains an improper link resolution vulnerability that allows attackers to access files outside the |
| CVE-2026-109967 | 7.5 | 2026-10-13 | yt-dlp-web-ui through 4.0.0 contains a NULL pointer dereference vulnerability in the Service.Formats JSON-RPC method tha |
| CVE-2026-74034 | 7.5 | 2026-10-13 | Wazuh from 4.1.0 before 4.14.8 contains a missing origin check in wm_agent_upgrade that allows enrolled agents to issue  |
| CVE-2026-74035 | 7.2 | 2026-10-13 | Wazuh versions from 4.6.0 before 4.14.8 contain an authentication bypass vulnerability where security.update_user places |
| CVE-2026-74036 | 7.2 | 2026-10-13 | Wazuh from 4.3.0 before 4.14.8 contains a remote code execution vulnerability where SCA policy trust is determined by fi |
| CVE-2026-74037 | 7.2 | 2026-10-13 | Wazuh 4.0.0 before 4.14.8 fails to invalidate issued tokens for run_as users with zero static roles, because check_token |
| CVE-2026-74040 | 9.1 | 2026-10-13 | Wazuh versions from 3.9.0 before 4.14.8 contain an arbitrary file overwrite vulnerability in MasterHandler.process_files |
| CVE-2026-74041 | 9.1 | 2026-10-13 | Wazuh 4.14.3 before 4.14.8 contains a case-sensitivity mismatch between the ossec.conf validator and wazuh-logcollector  |
| CVE-2026-74043 | 9.0 | 2026-10-13 | Wazuh from 4.1.1 before 4.14.8 contains a path traversal vulnerability in upload_list_file, upload_rule_file, and upload |
| CVE-2026-74045 | 7.1 | 2026-10-13 | Wazuh from 3.12.0 before 4.14.8 contains a heap buffer overflow in fim_generate_alert() where full_log is sized from inp |
| CVE-2026-93907 | 8.1 | 2026-10-13 | IBM WebSphere Application Server 8.5, and 9.0 could allow a remote attacker to bypass authentication by exploiting a fla |
| CVE-2026-95680 | 8.0 | 2026-10-13 | IBM WebSphere Application Server 8.5, and 9.0 could allow an authenticated attacker to bypass authorization leading to a |
| CVE-2026-104192 | 9.6 | 2026-10-13 | Dragonfly is an in-memory data store built for modern application workloads. Prior to 1.40, OpaqueObjLoader::CreateStrea |
| CVE-2026-108184 | 7.4 | 2026-10-13 | Improper certificate validation in certain Zoom Clients for Windows may allow an unauthenticated user to conduct an info |
| CVE-2026-108185 | 7.4 | 2026-10-13 | Improper certificate validation in the My Notes feature of certain Zoom Clients may allow an unauthenticated user to con |
| CVE-2026-109521 | 7.3 | 2026-10-13 | A vulnerability was detected in girishsaraf Online-Appointment-Booking-System up to f427b4757128ca253d33d0cc4e87bbb9c999 |
| CVE-2026-109522 | 7.3 | 2026-10-13 | A vulnerability has been found in girishsaraf Online-Appointment-Booking-System up to f427b4757128ca253d33d0cc4e87bbb9c9 |
| CVE-2026-109523 | 7.3 | 2026-10-13 | A vulnerability was found in girishsaraf Online-Appointment-Booking-System up to f427b4757128ca253d33d0cc4e87bbb9c999a4d |
| CVE-2026-53418 | 8.1 | 2026-10-13 | Improper Authorization in Handler for Custom URL Scheme in Zoom Workplace for Android before version 7.2.1 may allow an  |
| CVE-2026-53420 | 8.0 | 2026-10-13 | Buffer overflow in a Zoom Phone feature of Zoom Workplace Clients may allow an unauthenticated user to conduct a escalat |
| CVE-2026-53709 | 9.8 | 2026-10-13 | MCP Context Forge is an MCP gateway and administrative platform. Prior to 1.0.2, mcpgateway/config.py and .env.example s |
| CVE-2026-65198 | 8.6 | 2026-10-13 | Huawei's openUBMC ships a default SNMPv3 USM key that uses one value for both authentication and privacy. An attacker wh |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-104935 | Ivanti / Connect Secure | 2026-10-13 | 2026-10-16 | Unknown |
| CVE-2015-5477 | ISC / BIND | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2016-3081 | Apache / Struts | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2023-22894 | Strapi / Strapi | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2021-3199 | ONLYOFFICE / Docs | 2026-10-08 | 2026-10-11 | Unknown |
| CVE-2015-3306 | ProFTPD / ProFTPD | 2026-10-08 | 2026-10-11 | Unknown |

---

*Total entries in CISA KEV catalog: 1740*