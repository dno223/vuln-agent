# Vulnerability Intelligence Report

**Date:** 2026-11-20  
**Generated:** 2026-11-20T16:42:45Z  

---

## Executive Summary

Our environment faces significant exposure from 183 high-severity vulnerabilities, including a CVSS 10.0 critical flaw in Mitel MiCollab's conferencing component that allows unauthenticated remote code execution. Additionally, 7 new CISA Known Exploited Vulnerabilities (KEVs) were added this week across products including Synology DSM, Apache Axis, and Perforce Puppet Enterprise, indicating active threat actor exploitation. A command injection flaw in OpenStack Cinder (CVSS 9.6) and a stored XSS vulnerability in JTL-Shop (CVSS 9.3) further elevate organizational risk. Immediate remediation prioritization is required to prevent potential data breach, system compromise, or operational disruption.

---

## Risk Narrative

The current threat landscape reflects a surge in actively exploited vulnerabilities targeting enterprise infrastructure, collaboration platforms, and open-source components. The presence of a CVSS 10.0 unauthenticated RCE in Mitel MiCollab, combined with seven freshly KEV-listed vulnerabilities, signals that threat actors are actively targeting these attack surfaces. Command injection in OpenStack Cinder poses particular risk to cloud storage infrastructure, while web application flaws in JTL-Shop expose customer-facing platforms to data theft and account takeover. The breadth of 183 high-severity CVEs across diverse technology stacks increases the probability of successful exploitation, raising the risk of ransomware deployment, lateral movement, and regulatory compliance violations.

---

## Prioritized Action Items

1. Immediately patch or isolate Mitel MiCollab (CVE-2026-133323, CVSS 10.0) to block unauthenticated remote code execution against conferencing infrastructure.
2. Remediate OpenStack Cinder SSH storage driver command injection (CVE-2026-133189, CVSS 9.6) by applying vendor patches or disabling the vulnerable driver.
3. Apply patches for all 7 newly added CISA KEV entries, including Synology DSM, Apache Axis, and Perforce Puppet Enterprise, within the mandatory federal remediation window.
4. Address the JTL-Shop stored XSS and URL injection vulnerabilities (CVE-2026-22309, CVE-2026-22310) to prevent session hijacking and admin-panel compromise.
5. Conduct a full audit of remaining high-severity CVEs to triage exposure, prioritize asset-critical findings, and validate patch coverage across all affected systems.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-129234 | 7.3 | 2026-11-19 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research a |
| CVE-2026-133189 | 9.6 | 2026-11-19 | A command injection vulnerability was found in OpenStack Cinder's SSH-based storage-driver support. Incomplete validatio |
| CVE-2026-133303 | 9.0 | 2026-11-19 | A vulnerability in the Audio, Web, and Video Conferencing (AWV) component of Mitel MiCollab through 10.3 (10.3.0.18) cou |
| CVE-2026-133306 | 7.0 | 2026-11-19 | VideoLAN libaacs 0.7.0 through 0.12.0 on non-macOS, non-Windows builds contains stack-based buffer overflows in aacs_res |
| CVE-2026-133307 | 8.8 | 2026-11-19 | ClassiCube before 1.4.0 contains a heap-based out-of-bounds write vulnerability in Png_Decode in src/Bitmap.c that allow |
| CVE-2026-133309 | 7.8 | 2026-11-19 | @scalar/typebox before 0.1.4 contains a code injection vulnerability in TypeCompiler that allows attackers to execute Ja |
| CVE-2026-133310 | 8.1 | 2026-11-19 | Wing FTP Server before 8.2.8 contains a file mask bypass vulnerability allowing attackers to upload restricted files via |
| CVE-2026-133323 | 10.0 | 2026-11-19 | A vulnerability in the Audio, Web, and Video Conferencing (AWV) component of Mitel MiCollab through 10.3 (10.3.0.18) cou |
| CVE-2026-22309 | 9.3 | 2026-11-19 | The visitor tracking of JTL-Shop automatically
registers unknown crawler user agents without filtering the value, and th |
| CVE-2026-22310 | 8.0 | 2026-11-19 | When the setting for saving requests to non-existent
pages (404) is enabled, JTL-Shop stores the raw requested URL in it |
| CVE-2026-59988 | 8.2 | 2026-11-19 | django-docutils provides reStructuredText support for Django. Prior to 0.30.0, public rendering paths including publish_ |
| CVE-2026-77367 | 9.4 | 2026-11-19 | Daptin is a GraphQL/JSON-API headless CMS. Prior to 0.12.30, the generic GET /api/{entity} list endpoint accepts attacke |
| CVE-2026-77369 | 9.6 | 2026-11-19 | Daptin is a GraphQL/JSON-API headless CMS. From 0.11.4 until 0.12.30, the generic GET /yjs/:documentName WebSocket route |
| CVE-2026-117659 | 8.1 | 2026-11-19 | The InfoScan Electron desktop client improperly handles TLS certificate errors by accepting certificates without validat |
| CVE-2026-128135 | 7.1 | 2026-11-19 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research a |
| CVE-2026-128138 | 9.8 | 2026-11-19 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research a |
| CVE-2026-128139 | 7.5 | 2026-11-19 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research a |
| CVE-2026-129222 | 7.5 | 2026-11-19 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research a |
| CVE-2026-129223 | 7.5 | 2026-11-19 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research a |
| CVE-2026-129229 | 7.5 | 2026-11-19 | NLTK (Natural Language Toolkit) is a suite of open source Python modules, data sets, and tutorials supporting research a |
| CVE-2026-22308 | 9.3 | 2026-11-19 | The preview mode of the OPC (OnPage Composer) page
builder of JTL-Shop is activated by a request parameter alone and
ren |
| CVE-2026-103026 | 8.1 | 2026-11-19 | Paymenter is a free and open-source webshop solution for management of hosting services. Prior to 1.5.7, the HasConfirma |
| CVE-2026-103035 | 8.3 | 2026-11-19 | TeamPass is a self-hosted collaborative password manager. Prior to 3.2.1.2, the update_folder action in app/sources/fold |
| CVE-2026-104129 | 8.1 | 2026-11-19 | pREST (PostgreSQL REST) is an API that delivers an application on top of a Postgres database. Prior to 2.4.0, the vulner |
| CVE-2026-126088 | 8.1 | 2026-11-19 | In Autonomy Logic OpenPLC Runtime versions 4.2.4 and prior, a race condition allows multiple concurrent requests to pass |
| CVE-2026-127064 | 8.2 | 2026-11-19 | @fastify/reply-from is a Fastify plugin that forwards requests to an upstream HTTP server. In versions before 12.8.4, it |
| CVE-2026-129500 | 7.5 | 2026-11-19 | @fastify/http-proxy is a Fastify plugin that proxies HTTP and WebSocket traffic to an upstream server. In versions from  |
| CVE-2026-129502 | 7.5 | 2026-11-19 | @fastify/http-proxy is a Fastify plugin that proxies HTTP and WebSocket traffic to an upstream server. In versions from  |
| CVE-2026-130157 | 7.5 | 2026-11-19 | RepoManager is a self-hosted deb/rpm package repository. Prior to 5.13.3, an attacker who controls an upstream RPM repos |
| CVE-2026-130158 | 9.0 | 2026-11-19 | RepoManager is a self-hosted deb/rpm package repository. Prior to 5.13.3, a registered host or a party with its host/API |
| CVE-2026-130160 | 8.8 | 2026-11-19 | RepoManager is a self-hosted deb/rpm package repository. Prior to 5.13.3, an authenticated user can supply a user-contro |
| CVE-2026-130647 | 7.5 | 2026-11-19 | @fastify/http-proxy is a Fastify plugin that proxies HTTP and WebSocket traffic to an upstream server. In versions from  |
| CVE-2026-130886 | 8.2 | 2026-11-19 | @fastify/reply-from is a Fastify plugin that forwards requests to an upstream HTTP server. In versions 12.8.1 through 12 |
| CVE-2026-104099 | 9.1 | 2026-11-19 | Fabio is an HTTP(S) and TCP router for deploying applications managed by consul. Prior to 1.7.3, route/table.go selects  |
| CVE-2026-115463 | 7.4 | 2026-11-19 | Poweradmin is a web-based DNS administration tool for PowerDNS server. From 4.0.0 until 4.2.6, 4.3.5, and 4.4.1, lib/Dom |
| CVE-2026-115578 | 7.5 | 2026-11-19 | Go-Guerrilla SMTP Daemon is a lightweight SMTP server written in Go. In 1.6.7 and earlier, according to the repository a |
| CVE-2026-129938 | 7.4 | 2026-11-19 | An improper neutralization of delimiters in the MongoDB C# driver's DNS SRV connection-string resolution lets an unauthe |
| CVE-2026-130176 | 7.5 | 2026-11-19 | aMQTT is an open source MQTT broker and client. From 0.11.0 until 0.12.1, the QoS 2 transaction handler in amqtt/mqtt/pr |
| CVE-2026-131175 | 7.6 | 2026-11-19 | In Splunk Enterprise versions below 10.4.4, 10.2.8, 10.0.11, and 9.4.16, a user who holds the "power" Splunk role could  |
| CVE-2026-131177 | 7.1 | 2026-11-19 | In Splunk Enterprise versions below 10.4.4, 10.2.9, 10.0.12, and 9.4.16, a user who does not hold the "admin" or "power" |
| CVE-2026-131178 | 7.6 | 2026-11-19 | In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user who holds the "power" Splunk role could  |
| CVE-2026-131179 | 7.6 | 2026-11-19 | In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user who holds the "power" Splunk role could  |
| CVE-2026-131181 | 7.1 | 2026-11-19 | In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.16, a user who does not hold the "admin" or "power" |
| CVE-2026-131182 | 7.6 | 2026-11-19 | In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user who holds the "power" Splunk role could  |
| CVE-2026-131188 | 7.1 | 2026-11-19 | In Splunk Enterprise versions below 10.4.4, 10.2.8, 10.0.11, and 9.4.16, an unauthenticated user could craft a malicious |
| CVE-2026-131190 | 7.5 | 2026-11-19 | In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user could access RapidDiag  |
| CVE-2026-131192 | 7.5 | 2026-11-19 | In Splunk Enterprise versions below 10.6.1, 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user could access li |
| CVE-2026-131196 | 7.5 | 2026-11-19 | In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user who can connect to a Sp |
| CVE-2026-131198 | 7.1 | 2026-11-19 | In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the mc_view_im_data capability could c |
| CVE-2026-131199 | 8.8 | 2026-11-19 | In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the mc_investigation_read capability c |
| CVE-2026-131200 | 8.1 | 2026-11-19 | In Splunk Enterprise Security versions below 8.7.0, a user who holds the "ess_analyst" Splunk Enterprise Security role c |
| CVE-2026-131202 | 9.1 | 2026-11-19 | In Splunk Enterprise Security versions below 8.7.0, a user who holds the "ess_admin" Splunk Enterprise Security role cou |
| CVE-2026-131203 | 8.3 | 2026-11-19 | In Splunk Enterprise Security versions below 8.7.0, a user who holds the "ess_analyst" Splunk Enterprise Security role c |
| CVE-2026-131209 | 8.3 | 2026-11-19 | In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the ueba_ers_execution_post capability |
| CVE-2026-131210 | 8.1 | 2026-11-19 | In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the ueba_finding_exclusion_edit capabi |
| CVE-2026-131211 | 7.3 | 2026-11-19 | In Splunk App for Payment Card Industry Compliance versions below 8.7.0, a user who holds the "ess_user" Splunk Enterpri |
| CVE-2026-131215 | 8.3 | 2026-11-19 | In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the ueba_finding_exclusion_edit capabi |
| CVE-2026-131218 | 8.3 | 2026-11-19 | In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the mc_investigation_read capability c |
| CVE-2026-131236 | 8.8 | 2026-11-19 | In Splunk Enterprise Security versions below 8.7.0, an unauthenticated user who can influence indexed event data could s |
| CVE-2026-131239 | 7.3 | 2026-11-19 | In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the run_collect capability could store |
| CVE-2026-131243 | 7.6 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, an authenticated user with permission to view an affected container could query the |
| CVE-2026-131245 | 7.1 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user with edit permission for the container label of a pending external prompt co |
| CVE-2026-131246 | 8.8 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, an authenticated user with edit permission for the container label on a pending app |
| CVE-2026-131248 | 7.2 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user that holds a role with the System Settings edit permission and restricted te |
| CVE-2026-131252 | 8.8 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user that holds a role with the Assets edit or delete permission and access to on |
| CVE-2026-131253 | 9.9 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, an authenticated user that holds a role with the Apps edit, Containers edit, and Pl |
| CVE-2026-131255 | 7.5 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, an unauthenticated user could gain administrator privileges through a user account  |
| CVE-2026-131256 | 7.2 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, an authenticated user that holds a role with the System Settings edit permission co |
| CVE-2026-131258 | 8.7 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user with edit permission for a container or workbook task could store attacker-c |
| CVE-2026-131260 | 8.7 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user with the containers:edit permission could import a container that includes a |
| CVE-2026-131261 | 8.8 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user that holds a role with the Apps edit permission could execute arbitrary code |
| CVE-2026-131262 | 7.1 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, an authenticated user who can view and edit containers in at least one container la |
| CVE-2026-131263 | 8.8 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user that holds a role with only the apps:edit permission could install a connect |
| CVE-2026-131266 | 7.7 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user that holds a role with the System Settings edit permission could cause Splun |
| CVE-2026-131268 | 7.2 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user that holds a role with the System Settings edit permission could use a custo |
| CVE-2026-131269 | 8.8 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user that holds a role with the Apps edit permission could cause Splunk SOAR to e |
| CVE-2026-131270 | 8.8 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, an authenticated user with repository edit access could cause Splunk SOAR to write  |
| CVE-2026-131271 | 8.8 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, an authenticated user with permission to view and edit containers for one label cou |
| CVE-2026-131272 | 7.2 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user that holds a role with the System Settings edit permission could use the Aut |
| CVE-2026-131278 | 7.3 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user with local access to the affected host could obtain a live Splunk SOAR sessi |
| CVE-2026-131282 | 8.1 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user who holds the "Observer" Splunk SOAR role could access a password-reset cred |
| CVE-2026-131286 | 7.1 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, an authenticated user with permission to author and run playbooks could view action |
| CVE-2026-131287 | 9.6 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user that holds a role with the Playbooks view, edit, execute, and delete permiss |
| CVE-2026-131288 | 7.3 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, a user with access to the configured load balancer account could replace a load bal |
| CVE-2026-131293 | 8.3 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, an authenticated user with permission to edit and run playbooks could read or overw |
| CVE-2026-131295 | 8.8 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, an authenticated user with permission to create and run playbooks could start child |
| CVE-2026-131297 | 8.1 | 2026-11-19 | In Splunk SOAR versions below 8.8.0, an operator of a configured identity provider could authenticate as an existing use |
| CVE-2026-131299 | 7.5 | 2026-11-19 | In Splunk App for Stream versions below 8.1.7, an unauthenticated user who can reach the Splunk App for Stream Represent |
| CVE-2026-131303 | 7.1 | 2026-11-19 | In Splunk AI Assistant versions below 2.0.0, a user who does not hold the "admin" or "power" Splunk roles could obtain l |
| CVE-2026-131304 | 8.1 | 2026-11-19 | In Splunk AI Assistant versions below 2.0.0 a user who does not hold the "admin" or "power" Splunk roles could access da |
| CVE-2026-131305 | 8.1 | 2026-11-19 | In Splunk AI Assistant versions below 2.0.0, a user who does not hold the "admin" or "power" Splunk roles could submit c |
| CVE-2026-76535 | 9.1 | 2026-11-19 | In Splunk Enterprise versions below 10.6.1, 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user could run arbit |
| CVE-2026-76536 | 9.4 | 2026-11-19 | In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user could use an empty clus |
| CVE-2026-76538 | 8.8 | 2026-11-19 | In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.16, a user who does not hold the "admin" or "power" |
| CVE-2026-76540 | 8.8 | 2026-11-19 | In Splunk Enterprise versions below 9.4.17, 10.0.12, 10.2.9, and 10.4.5, a user who does not hold the "admin" or "power" |
| CVE-2026-76544 | 8.1 | 2026-11-19 | In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.16, a user who does not hold the "admin" or "power" |
| CVE-2026-129932 | 7.4 | 2026-11-19 | The MongoDB Java driver applies its DNS seedlist domain restriction to a record value that is later re-interpreted diffe |
| CVE-2026-130151 | 8.5 | 2026-11-19 | Okta Privileged Access (OPA) Gateway includes a version of the FreeRDP library affected by memory management issues in i |
| CVE-2026-130179 | 8.5 | 2026-11-19 | The Okta .NET SDK Abstractions library systematically writes per-request authentication credentials to a shared HTTP cli |
| CVE-2026-130234 | 8.0 | 2026-11-19 | The Okta Swift Management SDK does not percent-encode forward slash (/) characters during path parameter interpolation.  |
| CVE-2026-130235 | 8.7 | 2026-11-19 | In the Okta .NET SDK Abstractions library, outbound HTTP requests are not restricted to the configured Okta organization |
| CVE-2026-130236 | 8.5 | 2026-11-19 | In the Auth0 Authorization Extension, request authentication handling can process claims from query parameters independe |
| CVE-2026-133201 | 7.5 | 2026-11-19 | A vulnerability was determined in smartalock wireguard-lwip up to cfba91666590e86bd67842c71cedf9a423be823a. Impacted is  |
| CVE-2026-62955 | 7.2 | 2026-11-19 | baserCMS is a website development framework. From 5.2.3 until 5.3.0, BcThemeFileService::getFullpath() in plugins/bc-the |
| CVE-2026-82339 | 9.1 | 2026-11-19 | IBM Guardium Data Protection 12.2 is vulnerable to missing authentication in the SharePoint S-TAP RelayService, allowing |
| CVE-2026-82342 | 8.1 | 2026-11-19 | IBM Guardium Data Protection 12.2 is vulnerable to a stack-based buffer overflow when processing a specially crafted PRO |
| CVE-2026-84087 | 7.8 | 2026-11-19 | IBM Guardium Data Protection 12.2 is vulnerable to local privilege escalation via the SUID-root podman_wrapper binary on |
| CVE-2026-84236 | 9.8 | 2026-11-19 | IBM Guardium Data Protection 12.2 is vulnerable to insecure deserialization in the SharePoint Tap MulticastTransceiver c |
| CVE-2026-84273 | 8.1 | 2026-11-19 | IBM Guardium Data Protection 12.2 is vulnerable to path traversal in the datasource functionality. An authenticated atta |
| CVE-2026-85018 | 8.1 | 2026-11-19 | IBM Guardium Data Protection 12.2 is vulnerable to improper TLS certificate validation in the GDP Terraform provider, al |
| CVE-2026-87977 | 9.8 | 2026-11-19 | IBM Guardium Data Protection 12.2 is vulnerable to SQL injection in the edge-controller component. An unauthenticated re |
| CVE-2026-114516 | 9.8 | 2026-11-19 | Etherpad is a real-time collaborative editor. From 1.8.14 until 3.3.3, the pre-authentication /static/* plugin asset han |
| CVE-2026-133325 | 9.8 | 2026-11-19 | Key exchange without entity authentication vulnerability in Apache Tomcat allowed an unauthenticated node to join a clus |
| CVE-2026-133476 | 8.8 | 2026-11-19 | In Dolibarr before 24.0.3, dolForgeSQLCriteriaCallback() in htdocs/core/lib/functions.lib.php allows account takeover be |
| CVE-2026-61798 | 8.1 | 2026-11-19 | netty-incubator-codec-ohttp implements Oblivious HTTP (OHTTP) gateway and client functionality using Netty. Prior to 0.0 |
| CVE-2026-63124 | 7.5 | 2026-11-19 | netty-incubator-codec-ohttp implements Oblivious HTTP (OHTTP) gateway and client functionality using Netty. Prior to 0.0 |
| CVE-2026-63202 | 7.5 | 2026-11-19 | netty-incubator-codec-ohttp implements Oblivious HTTP (OHTTP) gateway and client functionality using Netty. Prior to 0.0 |
| CVE-2026-77312 | 10.0 | 2026-11-19 | Flyto2 Core is an execution kernel for automation and AI-agent workflows. Prior to 2.26.8, the earlier CVE-2026-67429 re |
| CVE-2026-77313 | 7.1 | 2026-11-19 | Flyto2 Core is an execution kernel for automation and AI-agent workflows. Prior to 2.26.8, validate_url_ssrf in src/core |
| CVE-2026-77315 | 8.5 | 2026-11-19 | Flyto2 Core is an execution kernel for automation and AI-agent workflows. Prior to 2.26.8, http.paginate in src/core/mod |
| CVE-2026-77316 | 7.1 | 2026-11-19 | Flyto2 Core is an execution kernel for automation and AI-agent workflows. Prior to 2.26.8, validate_url_ssrf() in src/co |
| CVE-2026-122676 | 8.5 | 2026-11-19 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in PublishPress Publi |
| CVE-2026-133528 | 8.6 | 2026-11-20 | BeamNG.drive before 0.40.6 contains an out-of-bounds write vulnerability because JIT-compiled LuaJIT traces omit FFI arr |
| CVE-2026-133415 | 7.3 | 2026-11-20 | A vulnerability has been found in sumiie24 School-Management-System up to d946d649c7c95e101fc5679ecd91999533bb10d7. The  |
| CVE-2026-133478 | 7.3 | 2026-11-20 | A security vulnerability has been detected in rajesh2211 Doctor-Appointment-System up to ee974dcf4c50da85e6ea026e27f4370 |
| CVE-2026-133534 | 7.5 | 2026-11-20 | PowerLink developed by Neotroni Lighting has a SQL Injection vulnerability, allowing unauthenticated remote attackers to |
| CVE-2026-65094 | 9.0 | 2026-11-20 | NVIDIA VIRTIO-Net for Bluefield contains a vulnerability in Virtio-Net where a VM user may cause a Write-What-Where cond |
| CVE-2026-113347 | 7.2 | 2026-11-20 | Multiple products produced by Ruijie Networks Co., Ltd. contain an OS command injection vulnerability that may lead to a |
| CVE-2026-133553 | 7.8 | 2026-11-20 | A flaw was found in crun. When copying files onto a tmpfs mounted with tmpcopyup, crun opens the destination a second ti |
| CVE-2026-133493 | 10.0 | 2026-11-20 | A vulnerability was identified in D-Link DIR-600L 2.17b02. Affected is the function genacgi_main of the file gena.cgi of |
| CVE-2026-133577 | 7.7 | 2026-11-20 | A flaw was found in the Kuadrant WebAssembly (WASM) shim shipped in Red Hat Connectivity Link 1.5. When a TokenRateLimit |
| CVE-2026-104927 | 7.5 | 2026-11-20 | The King Addons for Elementor – 100+ Elementor Widgets, 4 000+ Elementor Templates, WooCommerce Builder, Mega Menu, Popu |
| CVE-2026-105074 | 7.1 | 2026-11-20 | Cross-Site Request Forgery (CSRF) vulnerability in ShortPixel ShortPixel Image Optimizer shortpixel-image-optimiser allo |
| CVE-2026-120508 | 7.2 | 2026-11-20 | The Charitable – Donation & Fundraising Platform (Donation Forms, Recurring Donations & Fundraising Campaigns) plugin fo |
| CVE-2026-120556 | 8.1 | 2026-11-20 | The Toocheke Companion plugin for WordPress is vulnerable to Missing Authorization leading to arbitrary post and attachm |
| CVE-2026-128102 | 7.5 | 2026-11-20 | The rtMedia for WordPress, BuddyPress and bbPress plugin for WordPress is vulnerable to generic SQL Injection via the 'c |
| CVE-2026-129015 | 7.5 | 2026-11-20 | Improper Restriction of XML External Entity Reference vulnerability in ReviewX ReviewX reviewx allows XML Entity Linking |
| CVE-2026-129036 | 7.5 | 2026-11-20 | Incorrect Privilege Assignment vulnerability in weDevs WP ERP erp allows Privilege Escalation.This issue affects WP ERP: |
| CVE-2026-129056 | 9.8 | 2026-11-20 | Incorrect Privilege Assignment vulnerability in Paul Ryan Authorizer authorizer allows Privilege Escalation.This issue a |
| CVE-2026-129065 | 7.5 | 2026-11-20 | Missing Authorization vulnerability in Backup For WP WP Database Backup wp-database-backup allows Exploiting Incorrectly |
| CVE-2026-129075 | 7.1 | 2026-11-20 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Imran Tauqeer Cube |
| CVE-2026-129327 | 7.2 | 2026-11-20 | The Apaczka.pl WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the '_apaczka[<id>][err |
| CVE-2026-130055 | 7.5 | 2026-11-20 | The VidShop for WooCommerce plugin for WordPress is vulnerable to Sensitive Information Exposure in versions up to, and  |
| CVE-2026-130813 | 7.1 | 2026-11-20 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Liquid Web / Stell |
| CVE-2026-131582 | 7.2 | 2026-11-20 | The PagBank / PagSeguro e Vindi para WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via t |
| CVE-2026-131645 | 7.2 | 2026-11-20 | The Kognetiks Chatbot plugin for WordPress is vulnerable to Stored DOM-Based Cross-Site Scripting via the 'comment' para |
| CVE-2026-131795 | 8.1 | 2026-11-20 | Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion') vulnerability in |
| CVE-2026-131797 | 7.1 | 2026-11-20 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Imran Tauqeer Cube |
| CVE-2026-89095 | 8.1 | 2026-11-20 | The Shortcodes and extra features for Phlox theme plugin for WordPress is vulnerable to Local File Inclusion in all vers |
| CVE-2026-118522 | 8.1 | 2026-11-20 | The Video & Photo Gallery for Ultimate Member plugin for WordPress is vulnerable to Arbitrary File Deletion in versions  |
| CVE-2026-121985 | 7.2 | 2026-11-20 | The FV Flowplayer Video Player plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'comment' param |
| CVE-2026-127112 | 7.2 | 2026-11-20 | The Events Made Easy plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'event[event_notes]' para |
| CVE-2026-128915 | 8.5 | 2026-11-20 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in InstaWP InstaWP Co |
| CVE-2026-129840 | 7.5 | 2026-11-20 | In the nrfconnect/ncs-zigbee repository, the GitHub Actions workflow
.github/workflows/build_documentation.yml used the  |
| CVE-2026-130010 | 8.1 | 2026-11-20 | The Chatterbug Forms – Fast, Flexible WordPress Form Builder plugin for WordPress is vulnerable to arbitrary file deleti |
| CVE-2026-133500 | 9.1 | 2026-11-20 | A vulnerability was identified in Gladys Assistant up to 4.71.0. This affects an unknown function of the file gateway.do |
| CVE-2026-133501 | 9.0 | 2026-11-20 | A security flaw has been discovered in Gladys Assistant up to 4.71.0. This impacts an unknown function of the file serve |
| CVE-2026-133502 | 7.3 | 2026-11-20 | A weakness has been identified in blinkospace blinko up to 1.8.8. Affected is an unknown function of the file /api/auth/ |
| CVE-2026-109387 | 7.2 | 2026-11-20 | The Photo Gallery, Sliders, Proofing and Themes – NextGEN Gallery plugin for WordPress is vulnerable to Stored Cross-Sit |
| CVE-2026-116550 | 7.2 | 2026-11-20 | The Photo Gallery, Sliders, Proofing and Themes – NextGEN Gallery plugin for WordPress is vulnerable to Stored Cross-Sit |
| CVE-2026-119611 | 7.2 | 2026-11-20 | The NextGEN Gallery plugin for WordPress is vulnerable to Stored Cross-Site Scripting in versions up to, and including,  |
| CVE-2026-120681 | 9.1 | 2026-11-20 | The Mang Board plugin for WordPress is vulnerable to authorization bypass in all versions up to, and including, 2.4.7. T |
| CVE-2026-121790 | 7.2 | 2026-11-20 | The CWILL (Formerly ParcelPanel) – Shipment Tracking, Tracking & Order Tracking for WooCommerce plugin for WordPress is  |
| CVE-2026-125059 | 7.5 | 2026-11-20 | The Mang Board plugin for WordPress is vulnerable to Arbitrary File Deletion via Path Traversal in versions up to, and i |
| CVE-2026-125085 | 8.8 | 2026-11-20 | The Nexter Extension – Security, Performance, Code Snippets & Site Toolkit plugin for WordPress is vulnerable to Privile |
| CVE-2026-126716 | 8.1 | 2026-11-20 | The Mega Forms – Drag & Drop Form Builder with Multi-Step & Conditional Logic plugin for WordPress is vulnerable to arbi |
| CVE-2026-96771 | 7.2 | 2026-11-20 | The Hydrogen Calendar Embeds plugin for WordPress is vulnerable to Stored DOM-Based Cross-Site Scripting via ICS Feed Ev |
| CVE-2026-125094 | 7.2 | 2026-11-20 | The Optimole – Optimize Images \| Convert WebP & AVIF \| CDN & Lazy Load \| Image Optimization plugin for WordPress is vuln |
| CVE-2026-131804 | 7.2 | 2026-11-20 | The Seraphinite Accelerator plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'HTTP_USER_AGENT'  |
| CVE-2026-133578 | 7.3 | 2026-11-20 | A vulnerability was detected in itsourcecode Banking Management System 1.0. This impacts an unknown function of the file |
| CVE-2026-109878 | 7.1 | 2026-11-20 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Elementor Elemento |
| CVE-2026-128997 | 7.5 | 2026-11-20 | Missing Authorization vulnerability in RomanCode MapSVG mapsvg-lite-interactive-vector-maps allows Exploiting Incorrectl |
| CVE-2026-129073 | 9.8 | 2026-11-20 | Authentication Bypass Using an Alternate Path or Channel vulnerability in miniOrange miniorange otp verification miniora |
| CVE-2026-133707 | 7.8 | 2026-11-20 | The targets R package before 1.12.1 contains a code execution vulnerability that allows attackers to run arbitrary R cod |
| CVE-2026-133708 | 7.8 | 2026-11-20 | diffpy.structure before 3.5.1 contains a code execution vulnerability that allows attackers to run Python code by supply |
| CVE-2026-133710 | 7.8 | 2026-11-20 | llama.cpp b11003 before b12556 contains an integer overflow in the hrm_text loader load_arch_hparams() that allows attac |
| CVE-2026-128996 | 7.1 | 2026-11-20 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Tomdever wpForo Fo |
| CVE-2026-129017 | 7.1 | 2026-11-20 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Gemini Labs Site R |
| CVE-2026-129039 | 9.8 | 2026-11-20 | Deserialization of Untrusted Data vulnerability in Tribulant Software Newsletters newsletters-lite allows Object Injecti |
| CVE-2026-129043 | 9.3 | 2026-11-20 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Tribulant Software |
| CVE-2026-129074 | 7.1 | 2026-11-20 | Missing Authorization vulnerability in miniOrange miniOrange's Google Authenticator miniorange-2-factor-authentication a |
| CVE-2026-14914 | 10.0 | 2026-11-20 | Unrestricted upload of file with dangerous type vulnerability in Tegsoft Yönetim ve Bilişim Hizmetleri Tic. Ltd. Şti. Te |
| CVE-2026-80188 | 9.8 | 2026-11-20 | The BuddyBoss Addons plugin for WordPress is vulnerable to Authentication Bypass leading to Account Takeover in versions |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2024-10441 | Synology / DiskStation Manager (DSM) | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-40217 | BerriAI / LiteLLM | 2026-11-18 | 2026-12-02 | Unknown |
| CVE-2026-90817 | Vanderbilt University / Research Electronic Data Capture (REDCap) | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-90436 | Apache / Axis | 2026-11-18 | 2026-11-21 | Unknown |
| CVE-2026-115731 | Perforce / Puppet Enterprise | 2026-11-17 | 2026-12-01 | Unknown |
| CVE-2026-114713 | UnrealIRCd / UnrealIRCd | 2026-11-13 | 2026-11-16 | Unknown |
| CVE-2026-123039 | Check Point / Multiple Products | 2026-11-13 | 2026-11-16 | Unknown |

---

*Total entries in CISA KEV catalog: 1786*