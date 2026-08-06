# Vulnerability Intelligence Report

**Date:** 2026-08-06  
**Generated:** 2026-08-06T10:36:50Z  

## Pipeline Warnings

- summarizer failed: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-sonnet-4-20250514'}, 'request_id': 'req_011CdmM9eqyZ2YQbmQddDe1K'}

---

## Executive Summary

_No summary available._

---

## Risk Narrative

_No risk narrative available._

---

## Prioritized Action Items

_No action items available._

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-12609 | 7.5 | 2026-08-05 | In Eclipse Theia versions 1.66.0 and up until including 1.73.1, the `@theia/plugin-ext` backend exposes the `/hostedPlug |
| CVE-2026-60009 | 8.8 | 2026-08-05 | In Eclipse Theia versions up to and including 1.73.1, the `@theia/filesystem` backend binds `POST /file-upload` in every |
| CVE-2026-66747 | 9.8 | 2026-08-05 | Zbtlink router firmware ships an embedded remote-control implant, ENDLESSDOORS, present in every published build across  |
| CVE-2026-71231 | 9.8 | 2026-08-05 | IOTSmartHome's gui/login.php checkCookie() function builds an authentication query as SELECT * FROM users WHERE ID='<dec |
| CVE-2026-71232 | 7.2 | 2026-08-05 | MacCMS10's admin template editor (application/admin/controller/Template.php) blocks dangerous PHP functions in template  |
| CVE-2026-71233 | 8.7 | 2026-08-05 | InvoiceNinja v5-stable renders an invoice or quote's "terms" field in the client portal using Laravel Blade's raw output |
| CVE-2026-71234 | 7.5 | 2026-08-05 | Documize Community's attachment download route (domain/attachment/endpoint.go, Download function, registered via AddPubl |
| CVE-2026-71235 | 8.8 | 2026-08-05 | Magistrala's Rules Engine allows authenticated users to create rules with embedded Go or Lua scripts executed server-sid |
| CVE-2026-71236 | 8.7 | 2026-08-05 | Grocy's API request-body parser (controllers/Api/BaseApiController.php, GetParsedAndFilteredRequestBody) purifies incomi |
| CVE-2026-71237 | 9.8 | 2026-08-05 | Miantang/IoT-PHP's index.php implements a POST /userlogin route that reads the password directly from $_POST['pwd'] with |
| CVE-2026-71238 | 9.1 | 2026-08-05 | DjangoCRM ships with its Django SECRET_KEY hardcoded directly in the committed webcrm/settings.py rather than read from  |
| CVE-2026-71239 | 8.1 | 2026-08-05 | DjangoCRM's massmail module renders user-controlled EmlMessage fields (subject, content) through Django's Template() con |
| CVE-2026-71241 | 7.5 | 2026-08-05 | Book-Management-System's Flask API endpoints /student, /record, /books, /find_stu_book, and /find_not_return_book are mi |
| CVE-2026-71242 | 8.3 | 2026-08-05 | Crater's NotePolicy checks only a blanket Bouncer ability (manage-all-notes / view-all-notes) with no company-ownership  |
| CVE-2026-71243 | 8.8 | 2026-08-05 | The backmeup npm package assembles shell command strings by directly concatenating its option values (name, source, dest |
| CVE-2026-71245 | 7.1 | 2026-08-05 | Mautic's getLeadIdsByFieldValueAction (LeadBundle/Controller/AjaxController.php) reads a field parameter from the reques |
| CVE-2026-71248 | 9.8 | 2026-08-05 | Inventory-Management-System-PHP's login.php constructs its authentication query via direct string concatenation of raw P |
| CVE-2026-71252 | 8.2 | 2026-08-05 | toner-management's admin state-changing handlers (add.php, edit.php, delete.php under admin/toners, admin/toner-brands,  |
| CVE-2026-18933 | 7.2 | 2026-08-05 | The wp-downloadmanager WordPress plugin, in version 1.68.11 (also affecting the 6.9.4 release line), allows an admin-pri |
| CVE-2026-46581 | 7.5 | 2026-08-05 | In Eclipse Mojarra versions 2.3 and following, URL handing in `DefaultFaceletFactory` does not properly sanitize and/or  |
| CVE-2026-61891 | 7.5 | 2026-08-05 | In Eclipse Theia versions up to and including 1.73.1, the `@theia/filesystem` backend exposes HTTP file-download endpoin |
| CVE-2026-71254 | 9.8 | 2026-08-05 | nanoMODBUS through v1.23.0 contains an out-of-bounds write in the Modbus server-side handle_read_file_record() function  |
| CVE-2026-71255 | 8.6 | 2026-08-05 | nanoMODBUS through v1.23.0 contains an out-of-bounds write in the Modbus client-side recv_read_device_identification_res |
| CVE-2026-71256 | 9.8 | 2026-08-05 | nanoMODBUS through v1.23.0 contains an out-of-bounds stack read leading to a wild-pointer write in nmbs_read_device_iden |
| CVE-2026-16022 | 7.8 | 2026-08-05 | @oblique/cli 15.4.0 contains an OS command injection vulnerability in the project creation functionality. The CLI constr |
| CVE-2026-71226 | 7.3 | 2026-08-05 | Memory Corruption via Uncanceled AIO Requests on Error: libkcapi's one-shot AIO path can return an error before all subm |
| CVE-2026-71259 | 8.6 | 2026-08-05 | ESPHome through 2026.7.0-dev contains an operator-precedence bug in the cv.url() validator in esphome/config_validation. |
| CVE-2026-71261 | 7.8 | 2026-08-05 | dr_libs dr_wav.h (all versions through current master) contains an integer overflow in W64 CUE chunk metadata parsing. I |
| CVE-2026-71262 | 9.8 | 2026-08-05 | IoTSharp BlobStorageController.cs lacks the [Authorize] attribute applied to every other controller in the application ( |
| CVE-2026-71263 | 9.1 | 2026-08-05 | The LINUXTCP port of FreeModbus contains an off-by-one bounds check in xMBPortTCPPool() (demo/LINUXTCP/port/porttcp.c).  |
| CVE-2026-71264 | 8.2 | 2026-08-05 | WLED's GET /json/cfg endpoint (registered in wled00/wled_server.cpp) calls serveJson() with no settings-PIN check, unlik |
| CVE-2026-71265 | 7.5 | 2026-08-05 | Domoticz's MochadTCP::MatchLine() handler for MOCHAD_RFSEC messages (hardware/MochadTCP.cpp) copies network-received dat |
| CVE-2026-71266 | 7.8 | 2026-08-05 | tinyobjloader-c's tinyobj_parse_and_index_mtl_file() (tinyobj_loader_c.h) reads each line of a .mtl material file into a |
| CVE-2026-71267 | 9.8 | 2026-08-05 | microtar's mtar_write_file_header() and mtar_write_dir_header() functions (src/microtar.c) copy a caller-supplied entry  |
| CVE-2026-71268 | 9.9 | 2026-08-05 | OpenPLC Runtime v3's compile_program() function (webserver/openplc.py) parses `(*FILE:path content*)` directives from up |
| CVE-2026-71269 | 7.2 | 2026-08-05 | Node-RED's local-filesystem library storage module (getLibraryEntry() and saveLibraryEntry() in packages/node_modules/@n |
| CVE-2026-71270 | 8.6 | 2026-08-05 | Stirling-PDF's POST /api/v1/convert/url/pdf endpoint (ConvertWebsiteToPDF.java) was not updated with the CustomHtmlSanit |
| CVE-2026-71271 | 8.5 | 2026-08-05 | Memos' webhook URL validation, isReservedIP() (internal/webhook/validate.go), checks a candidate IP against a reservedCI |
| CVE-2026-71272 | 8.5 | 2026-08-05 | Memos' webhook dispatch function safeDialContext() (internal/webhook/webhook.go) resolves the target hostname via net.De |
| CVE-2026-71274 | 8.5 | 2026-08-05 | OpenBK7231T's CHANNEL_SetLabel() (src/cmnds/cmd_channels.c) stores channel labels received via the MQTT SetChannelLabel  |
| CVE-2026-71276 | 7.1 | 2026-08-05 | Magistrala (formerly Mainflux)'s message-readers API reads a `format` value from the HTTP query string (readers/api/http |
| CVE-2026-71277 | 9.1 | 2026-08-05 | rust-iot-platform's AuthToken request-guard implementation (api/src/main.rs) only checks whether the Authorization HTTP  |
| CVE-2026-71278 | 9.8 | 2026-08-05 | rust-iot-platform allows creating a "calc rule" via POST /calc-rule/create (api/src/controller/calc_rule_router.rs) cont |
| CVE-2026-71279 | 8.0 | 2026-08-05 | Zigbee2MQTT's ExternalJSExtension.getFilePath() (lib/extension/externalJS.ts) joins a `name` parameter received via an M |
| CVE-2026-71280 | 8.5 | 2026-08-05 | go-shiori's DownloadBookmark() (internal/core/download.go) fetches a caller-supplied bookmark URL using a plain http.Cli |
| CVE-2026-71281 | 8.8 | 2026-08-05 | Hugging Face peft's LoRA-GA and CorDA initialization modules (src/peft/tuners/lora/corda.py lines ~102 and ~163, and src |
| CVE-2026-71284 | 7.2 | 2026-08-05 | Fledge's backup-restore upload handler, upload_backup() (python/fledge/services/core/api/backup_restore.py), takes the f |
| CVE-2026-71285 | 8.1 | 2026-08-05 | Uptime Kuma's Matomo analytics integration (server/analytics/matomo-analytics.js) injects the admin-configurable Matomo  |
| CVE-2026-71287 | 8.8 | 2026-08-05 | Cacti's sanitize_sql_column() (lib/functions.php) sanitizes user-supplied ORDER BY column names using the regex `preg_re |
| CVE-2026-71288 | 8.8 | 2026-08-05 | Koha's guided report builder (reports/guided_reports.pl) reads the `order_by` CGI parameter and, for each value, a dynam |
| CVE-2026-71289 | 9.8 | 2026-08-05 | The NASA-AMMOS Asynchronous Network Management System (ANMS) reference implementation's default docker-compose.yml publi |
| CVE-2026-71291 | 8.8 | 2026-08-05 | Bolt CMS renders content field values through Twig's full application-level Environment with no SandboxExtension registe |
| CVE-2026-71292 | 7.2 | 2026-08-05 | Subrion CMS's admin grid sorting helper, _gridGetSorting() in includes/classes/ia.base.controller.admin.php, whitelists  |
| CVE-2026-71294 | 7.6 | 2026-08-05 | Cotonti CMS's Comments plugin deserializes user-supplied data without restricting the classes that may be instantiated.  |
| CVE-2025-70962 | 7.5 | 2026-08-05 | Zosi C519M V4.2.8.823C01450BA is vulnerable to Incorrect Access Control. The application contains hardcoded credentials  |
| CVE-2026-15979 | 8.1 | 2026-08-05 | The Content Egg – Affiliate Product Importer & Price Comparison plugin for WordPress is vulnerable to Arbitrary File Del |
| CVE-2026-16443 | 7.4 | 2026-08-05 | A flaw was found in the SAML metadata import functionality of the keycloak-services component, which is the core engine  |
| CVE-2026-17506 | 7.2 | 2026-08-05 | The Independent Analytics plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 404 not_found_url tr |
| CVE-2026-67623 | 8.8 | 2026-08-05 | Mistral Vibe before 2.23.3 contains a remote code execution vulnerability that allows attackers to execute arbitrary com |
| CVE-2026-7529 | 7.5 | 2026-08-05 | The wiseCampaign – WooCommerce Conversions Made Easy plugin for WordPress is vulnerable to unauthorized modification and |
| CVE-2026-12410 | 7.8 | 2026-08-05 | Link following vulnerability in the Uninstaller component in CCleaner prior to 7.10.1464 on Windows allows a local, low- |
| CVE-2026-15573 | 8.1 | 2026-08-05 | A flaw was found in Keycloak's Authorization Services. The component responsible for matching request paths to security  |
| CVE-2026-16102 | 8.1 | 2026-08-05 | A flaw was found in the Dynamic Client Registration (DCR) component of Keycloak, an identity and access management solut |
| CVE-2026-17613 | 7.5 | 2026-08-05 | Penpot’s ::import-binfile RPC command lacks authorization on the optional file-id parameter, allowing any authenticated  |
| CVE-2026-54876 | 7.5 | 2026-08-05 | Issue summary: A malicious TLS server can cause a memory leak in a TLS
client that has enabled OCSP response checking by |
| CVE-2026-10025 | 8.2 | 2026-08-05 | IBM QRadar 7.6.0.0 through 7.6.0.1, and 7.5.0 through 7.5.0 UP 15 Interim Fix 005 has an XML External Entity (XXE) injec |
| CVE-2026-15572 | 8.8 | 2026-08-05 | A flaw was found in Keycloak's Dynamic Client Registration (DCR) security policy management. The "Allowed Protocol Mappe |
| CVE-2026-16442 | 7.4 | 2026-08-05 | A flaw was found in the SAML broker component of Keycloak, which is used to manage identity federation and user authenti |
| CVE-2026-39923 | 8.1 | 2026-08-05 | Flarum before 1.8.16 contains a password reset token expiry bypass vulnerability that allows unauthenticated attackers t |
| CVE-2026-70601 | 7.5 | 2026-08-05 | Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.9, |
| CVE-2026-70604 | 7.4 | 2026-08-05 | Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.10 |
| CVE-2026-7326 | 7.5 | 2026-08-05 | A cross-site request forgery vulnerability in the Admin UI of Progress MarkLogic Server before 11.3.6 and 12.0.3 allows  |
| CVE-2026-7327 | 8.1 | 2026-08-05 | An improper privilege management vulnerability in the REST API document processing pipeline of Progress MarkLogic Server |
| CVE-2026-7329 | 9.9 | 2026-08-05 | An improper privilege management vulnerability in the SQL, SPARQL, and Optic REST query interfaces of Progress MarkLogic |
| CVE-2026-7557 | 9.1 | 2026-08-05 | An improper verification of cryptographic signature vulnerability in the SAML authentication module of Progress MarkLogi |
| CVE-2026-8400 | 8.1 | 2026-08-05 | IBM WebSphere Application Server 8.5, and 9.0 and IBM WebSphere Application Server - Liberty Continuous delivery has a f |
| CVE-2026-8709 | 9.9 | 2026-08-05 | An improper privilege management vulnerability in the REST API document patch operation of Progress MarkLogic Server bef |
| CVE-2026-9190 | 9.1 | 2026-08-05 | An HTTP request smuggling vulnerability in the HTTP App Server of Progress MarkLogic Server before 11.3.6 and 12.0.3 all |
| CVE-2026-9192 | 9.8 | 2026-08-05 | An authentication bypass vulnerability in the ODBC App Server of Progress MarkLogic Server before 11.3.6 and 12.0.3 allo |
| CVE-2026-9193 | 9.9 | 2026-08-05 | An improper privilege management vulnerability in the Hadoop integration of Progress MarkLogic Server before 11.3.6 and  |
| CVE-2026-9195 | 9.3 | 2026-08-05 | A cross-site scripting vulnerability in the Query Console of Progress MarkLogic Server before 11.3.6 and 12.0.3 allows a |
| CVE-2026-9203 | 8.5 | 2026-08-05 | A server-side request forgery vulnerability in Progress MarkLogic Server before 11.3.6 and 12.0.3 allows an authenticate |
| CVE-2026-17617 | 8.5 | 2026-08-05 | IBM Application Gateway Operator 22.2 through 26.06 is vulnerable to Server-Side Request Forgery (SSRF) due to insuffici |
| CVE-2026-17623 | 8.8 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3 could allow a remote authenticated attacker to execute arbitrary commands due to i |
| CVE-2026-17626 | 8.8 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3 Langflow could allow an authenticated attacker to read, modify, or expose sensitiv |
| CVE-2026-17630 | 7.2 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3 could allow a remote attacker to execute arbitrary code due to improper validation |
| CVE-2026-20124 | 7.7 | 2026-08-05 | A vulnerability in the Simple Network Management Protocol (SNMP) subsystem of Cisco IOS XE Software could allow an authe |
| CVE-2026-20200 | 8.8 | 2026-08-05 | A vulnerability in the web-based management interface of Cisco IMC could allow an authenticated, remote attacker with lo |
| CVE-2026-20263 | 8.6 | 2026-08-05 | A vulnerability in the Blocks Extensible Exchange Protocol (BEEP) feature of Cisco IOS XE Software could allow an unauth |
| CVE-2026-20267 | 9.0 | 2026-08-05 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco IOS XE Software engineering t |
| CVE-2026-20268 | 8.6 | 2026-08-05 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco IOS XE Software engineering t |
| CVE-2026-20269 | 8.6 | 2026-08-05 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco IOS XE Software engineering t |
| CVE-2026-20270 | 8.6 | 2026-08-05 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco IOS XE Software engineering t |
| CVE-2026-20271 | 8.6 | 2026-08-05 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco IOS XE Software engineering t |
| CVE-2026-20272 | 9.8 | 2026-08-05 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco IOS XE Software engineering t |
| CVE-2026-20273 | 8.6 | 2026-08-05 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco IOS XE Software engineering t |
| CVE-2026-20301 | 8.6 | 2026-08-05 | A vulnerability in the Extensible Messaging Client Protocol (XMCP), also referred to as the External Client protocol, of |
| CVE-2026-20303 | 9.9 | 2026-08-05 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Catalyst SD-WAN engineering t |
| CVE-2026-20304 | 9.9 | 2026-08-05 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Catalyst SD-WAN engineering t |
| CVE-2026-20310 | 9.1 | 2026-08-05 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Catalyst SD-WAN engineering t |
| CVE-2026-20312 | 8.8 | 2026-08-05 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Catalyst SD-WAN engineering t |
| CVE-2026-20313 | 7.7 | 2026-08-05 | As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Catalyst SD-WAN engineering t |
| CVE-2026-8446 | 7.5 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3 contain an authentication bypass vulnerability in the Model Context Protocol (MCP) |
| CVE-2026-9077 | 8.5 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3 Langflow allows remote authenticated attackers to bypass localhost-only restrictio |
| CVE-2026-17625 | 7.2 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3, 1.0.0 through 1.10.3, 1.0.0 through 1.10.3, 1.0.0 through 1.10.3, 1.0.0 through 1 |
| CVE-2026-70426 | 9.0 | 2026-08-05 | In Remoting 3384.v60d89463d9e0 and earlier, except 3355.3357.v931d3c992987, included in Jenkins 2.575 and earlier, LTS 2 |
| CVE-2026-70431 | 8.8 | 2026-08-05 | Jenkins Multijob Plugin 669.v9d96a_d9c71b_0 and earlier provides Groovy scripting features that do not integrate with Sc |
| CVE-2026-70432 | 8.8 | 2026-08-05 | A cross-site request forgery (CSRF) vulnerability in Jenkins Multijob Plugin 669.v9d96a_d9c71b_0 and earlier allows atta |
| CVE-2026-70448 | 7.1 | 2026-08-05 | Jenkins Ivy Report Plugin 1.2 and earlier does not configure its XML parser to prevent XML external entity (XXE) attacks |
| CVE-2026-70608 | 7.2 | 2026-08-05 | Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.10 |
| CVE-2026-9081 | 7.1 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3, and 1.0.0 through 1.10.3 contains a Server-Side Request Forgery (SSRF) vulnerabil |
| CVE-2026-17624 | 8.5 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3, 1.0.0 through 1.10.3, 1.0.0 through 1.10.3, 1.0.0 through 1.10.3, 1.0.0 through 1 |
| CVE-2026-17632 | 8.8 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3 could allow a remote authenticated attacker to execute arbitrary code due to impro |
| CVE-2026-17633 | 8.5 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3 could allow a remote authenticated attacker to execute arbitrary code due to code  |
| CVE-2026-18485 | 7.8 | 2026-08-05 | There is a local privilege escalation vulnerability recently discovered in the NI-PAL kernel driver.  This may allow a l |
| CVE-2026-48168 | 10.0 | 2026-08-05 | PraisonAI is a multi-agent teams system. In versions prior to 4.6.40, the bundled Claude GitHub Actions workflow is vuln |
| CVE-2026-8182 | 8.8 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3 installations allow anyone on the internet to execute arbitrary code on the server |
| CVE-2026-8183 | 7.7 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3, 1.0.0 through 1.10.3, 1.0.0 through 1.10.3, 1.0.0 through 1.10.3, 1.0.0 through 1 |
| CVE-2026-8470 | 7.4 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3, 1.0.0 through 1.10.3, 1.0.0 through 1.10.3, and 1.0.0 through 1.10.3 use Python's |
| CVE-2026-8478 | 8.8 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3 could allow a remote attacker to inject arbitrary code on the system, due to the i |
| CVE-2026-9130 | 7.1 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3 contain an authorization bypass vulnerability in the MemoryComponent that allows a |
| CVE-2026-9196 | 8.1 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3 could allow an authenticated attacker to execute unintended code during Agentic As |
| CVE-2026-9201 | 8.8 | 2026-08-05 | IBM Langflow OSS 1.0.0 through 1.10.3 could allow an authenticated attacker to execute arbitrary code due to a cryptogra |
| CVE-2026-9205 | 7.4 | 2026-08-05 | IBM Langflow OSS contains a weak cryptographic key derivation vulnerability in the ensure_fernet_key() function. |
| CVE-2026-18953 | 8.6 | 2026-08-05 | Improper limitation of a pathname to a restricted directory in the get_resource tool in Amazon awslabs.aws-transform-mcp |
| CVE-2026-18958 | 7.3 | 2026-08-05 | A vulnerability was detected in imranrisal-dev Student-Management-System 18ea7904c339e0c7b0234724a79c939ce6191def/a8d43a |
| CVE-2026-55522 | 7.8 | 2026-08-05 | PraisonAI is a multi-agent teams system. In versions 3.9.26 through 4.6.57 of praiseonai and 0.12.12 through 1.6.57 of p |
| CVE-2026-55524 | 7.5 | 2026-08-05 | PraisonAI is a multi-agent teams system. In versions prior to 1.6.58, the web_crawl tool performs its SSRF check only on |
| CVE-2026-69111 | 7.5 | 2026-08-05 | Milvus through 2.6.22 and 3.0.0 contains an unauthenticated denial of service vulnerability that allows remote attackers |
| CVE-2026-70615 | 9.9 | 2026-08-05 | boringproxy through 0.10.0 contains a newline injection vulnerability that allows authenticated low-privileged users wit |
| CVE-2026-70617 | 8.1 | 2026-08-05 | Spacebar Server before commit dcfd910 contains a missing authorization vulnerability that allows any authenticated attac |
| CVE-2026-17583 | 8.4 | 2026-08-05 | The affected

Thermo Fisher Applied Biosystems Genetic Analyzers are vulnerable because .fsa/.hid output files can be ed |
| CVE-2026-18411 | 8.1 | 2026-08-05 | The KARR Security System and SWDS dealer-installed automotive anti-theft systems use a shared Bluetooth authentication k |
| CVE-2026-34966 | 7.6 | 2026-08-05 | Gitea prior to 1.27.0 contains a server-side request forgery vulnerability that allows authenticated attackers to bypass |
| CVE-2026-71312 | 8.0 | 2026-08-05 | rclone is a command-line program to sync files and directories to and from different cloud storage providers. Prior to v |
| CVE-2026-71314 | 7.5 | 2026-08-05 | Nuxt is an open-source web development framework for Vue.js. From 3.1.0 until 3.21.10 and 4.5.1, an unauthenticated atta |
| CVE-2026-71315 | 8.2 | 2026-08-05 | Nuxt is an open-source web development framework for Vue.js. From 3.21.7 until 3.21.10 and 4.5.1, mixed-case routeRules  |
| CVE-2026-71316 | 7.5 | 2026-08-05 | Nuxt is an open-source web development framework for Vue.js. From 4.4.0 until 4.5.1, runtime cache:nuxt:payload entries  |
| CVE-2026-71319 | 9.6 | 2026-08-05 | Nuxt is an open-source web development framework for Vue.js. Prior to 3.3.1, Nuxt DevTools (development mode only) expos |
| CVE-2026-71320 | 8.1 | 2026-08-05 | Nuxt is an open-source web development framework for Vue.js. From 3.4.0 until 3.21.10 and 4.5.1, an attacker can inject  |
| CVE-2026-71321 | 7.5 | 2026-08-05 | Nuxt is an open-source web development framework for Vue.js. From 3.1.0 until 3.21.10 and 4.5.1, the internal island ren |
| CVE-2026-67863 | 7.5 | 2026-08-05 | In open62541 1.5.5, a server-side use-after-free exists in the local MonitoredItem callback path. The issue occurs when  |
| CVE-2026-18969 | 7.3 | 2026-08-06 | A vulnerability was detected in Rongzhitong Visual Integrated Command and Dispatch Platform up to 20260617. Impacted is  |
| CVE-2026-18970 | 7.3 | 2026-08-06 | A flaw has been found in Rongzhitong Visual Integrated Command and Dispatch Platform up to 20260617. The affected elemen |
| CVE-2026-67869 | 7.5 | 2026-08-06 | Buffer Overflow vulnerability in open62541 v1.5.5 allows a remote attacker to cause a denial of service via the Service_ |
| CVE-2026-18973 | 7.3 | 2026-08-06 | A vulnerability has been found in heshengtao super-agent-party up to 0.4.1. The impacted element is the function sanitiz |
| CVE-2026-18990 | 7.3 | 2026-08-06 | A vulnerability was detected in letta-ai LettaBot 0.2.0. Impacted is an unknown function of the file src/api/server.ts o |
| CVE-2026-18991 | 7.3 | 2026-08-06 | A security vulnerability has been detected in nanocoai NanoClaw up to 2.0.64. This affects an unknown part of the file c |
| CVE-2026-15991 | 8.8 | 2026-08-06 | The File Manager plugin for WordPress is vulnerable to arbitrary file deletion due to insufficient file path validation  |
| CVE-2026-16636 | 7.2 | 2026-08-06 | The FluentSMTP – WP SMTP Plugin with Amazon SES, SendGrid, MailGun, Postmark, Google and Any SMTP Provider plugin for Wo |
| CVE-2026-18325 | 7.2 | 2026-08-06 | The Forminator Forms – Contact Form, Payment Form & Custom Form Builder plugin for WordPress is vulnerable to Stored Cro |
| CVE-2026-15459 | 8.1 | 2026-08-06 | The WPMU DEV Dashboard plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including, |
| CVE-2026-19000 | 7.3 | 2026-08-06 | A vulnerability was identified in JeecgBoot up to 3.9.2. The affected element is an unknown function of the file /airag/ |
| CVE-2026-18510 | 7.2 | 2026-08-06 | The TranslatePress – Translate Multilingual sites with AI Translation plugin for WordPress is vulnerable to Stored Cross |
| CVE-2025-15039 | 9.4 | 2026-08-06 | The Conditional Authentication (Adaptive Authentication) script does not correctly enforce the completion of all require |
| CVE-2026-18597 | 8.5 | 2026-08-06 | The PDF creation feature of Foxit PDF Services API supports referencing external files. Although local file access is re |
| CVE-2026-18649 | 7.5 | 2026-08-06 | A flaw was found in the GStreamer gst-plugins-good package. The rtph264depay and rtph265depay RTP depayloader elements d |
| CVE-2026-19009 | 7.3 | 2026-08-06 | A weakness has been identified in TinyAGI 0.0.20. This issue affects the function collectFiles of the file packages/core |
| CVE-2026-19010 | 7.3 | 2026-08-06 | A security vulnerability has been detected in TinyAGI 0.0.20. Impacted is the function processMessage of the file packag |
| CVE-2026-19021 | 7.3 | 2026-08-06 | A security vulnerability has been detected in SourceCodester Computer Repair Shop Management System 1.0. Affected by thi |
| CVE-2026-1728 | 9.8 | 2026-08-06 | Tokens issued to a low-privileged user are not sufficiently restricted, allowing them to be used to access product-level |
| CVE-2026-5430 | 10.0 | 2026-08-06 | The JWT authentication mechanism accepts tokens signed with algorithms other than those explicitly configured or support |
| CVE-2026-55978 | 8.4 | 2026-08-06 | An improper access control vulnerability in CatchPulse could allow a non-administrative local attacker to connect to an  |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-63077 | JetBrains / TeamCity | 2026-08-05 | 2026-08-08 | Unknown |
| CVE-2026-18556 | N-able / N-central | 2026-08-04 | 2026-08-07 | Unknown |
| CVE-2026-34486 | Apache / Tomcat | 2026-08-04 | 2026-08-07 | Unknown |
| CVE-2026-9198 | IBM / Langflow | 2026-08-04 | 2026-08-07 | Unknown |
| CVE-2026-18577 | N-able / N-central | 2026-08-03 | 2026-08-06 | Unknown |

---

*Total entries in CISA KEV catalog: 1661*