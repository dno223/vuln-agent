# Vulnerability Intelligence Report

**Date:** 2026-09-27  
**Generated:** 2026-09-27T13:32:24Z  

---

## Executive Summary

Our environment faces significant exposure from 107 high-severity vulnerabilities, primarily in Flowise and Capgo platforms, alongside 10 newly added CISA Known Exploited Vulnerabilities affecting widely deployed products including MikroTik, Microsoft SharePoint, WordPress, WSO2, and Adobe Commerce. The Flowise vulnerabilities expose critical access control failures allowing unauthorized data access, authentication bypass, and privilege escalation. Capgo vulnerabilities introduce cross-tenant data integrity risks and privilege escalation via API key manipulation. CISA KEV additions signal active exploitation in the wild, demanding immediate patch prioritization. No monitored CVEs currently overlap with the KEV catalog, which is a positive indicator, but the broader threat landscape requires urgent remediation action.

---

## Risk Narrative

The current threat landscape reflects a convergence of unpatched access control weaknesses in internal platforms and actively exploited vulnerabilities in widely deployed enterprise software. Flowise and Capgo vulnerabilities create pathways for privilege escalation, cross-tenant data access, and authentication bypass, posing significant risks to data confidentiality and platform integrity. CISA KEV additions for MikroTik, SharePoint, WordPress, WSO2, and Adobe Commerce indicate adversaries are actively exploiting these flaws in production environments globally. Business risks include unauthorized access to sensitive AI workflow data, potential lateral movement across tenants, regulatory compliance exposure, and reputational damage from a breach. Prompt patching and access control hardening are critical to containing these risks.

---

## Prioritized Action Items

1. Immediately patch or isolate MikroTik RouterOS, Microsoft SharePoint, WordPress Core, WSO2, and Adobe Commerce instances listed in the CISA KEV catalog due to confirmed active exploitation.
2. Upgrade Flowise to a version beyond 3.1.4 or apply compensating controls to address authentication bypass, missing RBAC, and unauthorized dashboard access vulnerabilities.
3. Upgrade Capgo to version 12.267.1 or later to remediate API key privilege escalation, cross-tenant integrity flaws, and access control gaps.
4. Conduct an emergency access control audit across all AI workflow and mobile delivery platforms to identify additional unauthorized permission paths or misconfigured endpoints.
5. Establish continuous KEV monitoring and a 48-hour patch SLA for any assets matching newly added CISA Known Exploited Vulnerability entries.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-100605 | 7.1 | 2026-09-26 | Flowise through 3.1.4 contains missing route-level RBAC checks on chat message endpoints that allow low-privileged API k |
| CVE-2026-100606 | 7.7 | 2026-09-26 | Flowise through 3.1.4 (Enterprise/platform mode with SSO enabled) contains an authentication bypass in the SSO login pat |
| CVE-2026-100607 | 7.7 | 2026-09-26 | Flowise through 3.1.4 resolves SSO and local-password users solely by email without storing provider or subject identifi |
| CVE-2026-100608 | 8.3 | 2026-09-26 | Flowise through 3.1.4 does not enforce authorization on the BullMQ admin dashboard. When the server runs in queue mode w |
| CVE-2026-100610 | 7.5 | 2026-09-26 | Flowise through 3.1.4 exposes GET /api/v1/upsert-history/:id and PATCH /api/v1/upsert-history without route-level permis |
| CVE-2026-100612 | 7.2 | 2026-09-26 | Capgo (capgo.app) through version 12.261.0 contains an incomplete access-control fix for the public.sso_providers table. |
| CVE-2026-100614 | 8.8 | 2026-09-26 | Capgo before 12.244.1 contains a cross-tenant integrity vulnerability in the metadata-cleaning worker that trusts image  |
| CVE-2026-100615 | 8.8 | 2026-09-26 | Cap-go capgo.app before 12.267.1 fails to validate target API key privilege during rotation, allowing an apikey_manager  |
| CVE-2026-100617 | 8.8 | 2026-09-26 | Cap-go capgo.app fails to validate that principals in channel_permission_overrides belong to the organization, allowing  |
| CVE-2026-100618 | 8.5 | 2026-09-26 | Capgo (capgo.app) is affected by an authorization flaw in the app icon update path. The PUT /app/:id endpoint accepts a  |
| CVE-2026-100619 | 8.8 | 2026-09-26 | Capgo (capgo.app) blocks direct user inserts into the public.manifest table with a RESTRICTIVE row-level security policy |
| CVE-2026-100622 | 7.5 | 2026-09-26 | capgo.app through 12.129.0 fails to verify deletion status when serving cached bundle artifacts from the public file rea |
| CVE-2026-100623 | 8.8 | 2026-09-26 | Capgo (capgo.app) exposes the legacy membership table public.org_users directly through Supabase PostgREST. The table's  |
| CVE-2026-100625 | 7.1 | 2026-09-26 | Capgo (capgo.app) exposes a native build TUS upload proxy (supabase/functions/_backend/public/build/upload.ts) that auth |
| CVE-2026-100627 | 8.1 | 2026-09-26 | Capgo (Cap-go/capgo.app) server backend Supabase functions contain an incorrect authorization flaw in the API-key bundle |
| CVE-2026-100631 | 7.5 | 2026-09-26 | Parse Server is an open source backend server. In versions prior to 8.6.90 and in versions from 9.0.0 prior to 9.10.1-al |
| CVE-2026-100636 | 7.6 | 2026-09-26 | SiYuan versions before v3.8.4 contain a path traversal vulnerability in the exportBrowserHTML endpoint that allows authe |
| CVE-2026-100637 | 7.6 | 2026-09-26 | SiYuan versions before v3.8.4 contain a path traversal vulnerability in the checkoutRepo endpoint that allows authentica |
| CVE-2026-100638 | 7.6 | 2026-09-26 | SiYuan versions before v3.8.4 contain a path traversal vulnerability in the setNotebookIcon endpoint that allows authent |
| CVE-2026-100639 | 8.8 | 2026-09-26 | SiYuan v3.8.3 fails to HTML-escape the data-subtype attribute when generating gutter-button markup (app/src/protyle/gutt |
| CVE-2026-100641 | 8.0 | 2026-09-26 | SiYuan before v3.8.4 does not HTML-escape stored flashcard block content before interpolating it into the card-manager l |
| CVE-2026-100642 | 7.6 | 2026-09-26 | SiYuan versions from v2.1.0 before v3.8.4 contain a cross-site request forgery vulnerability in the CheckAuth lock-scree |
| CVE-2026-100643 | 8.0 | 2026-09-26 | SiYuan versions before v3.8.4 fail to properly escape four stored Attribute View values in textarea elements, allowing a |
| CVE-2026-100644 | 7.5 | 2026-09-26 | SiYuan before v3.8.4 contains a SQL injection vulnerability in the graph query endpoint where the dailyNoteSavePath para |
| CVE-2026-100645 | 8.0 | 2026-09-26 | SiYuan versions 3.7.0 before 3.8.4 contain a stored cross-site scripting vulnerability in gallery and kanban database re |
| CVE-2026-100646 | 8.1 | 2026-09-26 | SiYuan is a self-hosted personal knowledge management system. In versions up to and including 3.8.3, the kernel's authen |
| CVE-2026-100655 | 7.5 | 2026-09-26 | Netty (io.netty:netty-codec-http) versions up to and including 4.1.137.Final and from 4.2.0.Final through 4.2.17.Final a |
| CVE-2026-100656 | 7.5 | 2026-09-26 | Netty (io.netty:netty-codec-http) contains an unbounded per-connection queue growth flaw in HttpServerCodec. The codec t |
| CVE-2026-100657 | 7.5 | 2026-09-26 | Netty's STOMP codec (io.netty:netty-codec-stomp) contains a ByteBuf leak in StompSubframeDecoder. Once a frame's declare |
| CVE-2026-100660 | 7.5 | 2026-09-26 | Netty's HTTP/3 codec (io.netty:netty-codec-http3) from 4.2.0.Final through 4.2.17.Final retains unbounded per-stream QPA |
| CVE-2026-100661 | 7.5 | 2026-09-26 | Netty's HTTP/3 codec (io.netty:netty-codec-http3) versions 4.2.0.Final through 4.2.17.Final contain a denial-of-service  |
| CVE-2026-100662 | 7.5 | 2026-09-26 | Netty's HTTP/3 codec (io.netty:netty-codec-http3) versions 4.2.0.Final through 4.2.17.Final contain an uncontrolled reso |
| CVE-2026-100663 | 7.5 | 2026-09-26 | Netty's HTTP/3 codec (io.netty:netty-codec-http3) from 4.2.2.Final through 4.2.17.Final does not special-case HTTP/1 CON |
| CVE-2026-100664 | 7.5 | 2026-09-26 | Netty's HTTP/3 codec (io.netty:netty-codec-http3) versions 4.2.2.Final through 4.2.17.Final builds the HTTP/3 :authority |
| CVE-2026-100665 | 7.5 | 2026-09-26 | Netty versions from 4.2.11.Final before 4.2.18.Final contain an incomplete hostname verification fix in the QUIC certifi |
| CVE-2026-100666 | 7.3 | 2026-09-26 | Netty's HttpServerCodec (io.netty:netty-codec-http) in versions 4.2.0.Final through 4.2.16.Final and in versions up to a |
| CVE-2026-100669 | 7.5 | 2026-09-26 | Grav before 2.0.25 ships web server configuration samples whose access-control deny rules are matched case-sensitively.  |
| CVE-2026-100670 | 8.8 | 2026-09-26 | Grav CMS 2.0.14 through 2.0.24 contains a privilege escalation vulnerability in the group and account blueprints. The ac |
| CVE-2026-100671 | 8.0 | 2026-09-26 | Grav is a flat-file CMS. In versions 2.0.19 through 2.0.24 — and in 2.0.0 through 2.0.18 and 1.7.x only where content Tw |
| CVE-2026-100672 | 7.5 | 2026-09-26 | The Comments plugin (getgrav/grav-plugin-comments) for Grav CMS through version 1.2.10 registers an admin handler that r |
| CVE-2026-100673 | 8.2 | 2026-09-26 | The Grav Data Manager plugin (getgrav/grav-plugin-datamanager) versions 1.0.1 through 1.4.4 render stored data entries i |
| CVE-2026-100676 | 8.2 | 2026-09-26 | January, the media proxy/embed service of stoatchat (stoatchat/stoatchat), before version 0.15.5 improperly resolves SVG |
| CVE-2026-100679 | 8.8 | 2026-09-26 | stoatchat before 0.15.5 fails to validate that MFA tickets belong to the authenticated user, allowing attackers to bypas |
| CVE-2026-100680 | 8.1 | 2026-09-26 | Budibase versions before 3.45.0 fail to disable external JSON reference resolution in the OpenAPI/Swagger import validat |
| CVE-2026-100682 | 8.8 | 2026-09-26 | Budibase Server before 3.45.0 contains an arbitrary file write vulnerability in the PWA icon upload endpoint that extrac |
| CVE-2026-100683 | 8.0 | 2026-09-26 | Budibase (@budibase/server) before 3.45.0 builds MySQL and MSSQL column-rename DDL in packages/backend-core/src/sql/sqlT |
| CVE-2026-100684 | 8.1 | 2026-09-26 | Budibase versions 3.41.0 before 3.45.0 contain an authentication bypass in the OIDC/SSO login path of @budibase/server.  |
| CVE-2026-100685 | 7.7 | 2026-09-26 | Budibase before 3.45.0 fails to properly scope the GET /api/chat-links endpoint by workspace, allowing builders to enume |
| CVE-2026-100686 | 8.1 | 2026-09-26 | Budibase versions before 3.45.0 fail to validate per-app authorization in the POST /api/global/groups/:groupId/apps endp |
| CVE-2026-100690 | 7.5 | 2026-09-26 | Hugo versions from v0.161.0 through v0.165.0 run Node.js tools (css.PostCSS, css.TailwindCSS, js.Babel) under the Node.j |
| CVE-2026-100692 | 7.5 | 2026-09-26 | Hugo is a static site generator. In versions after v0.123.0 and before v0.166.0, Hugo's symlink confinement checks stopp |
| CVE-2026-100693 | 8.4 | 2026-09-26 | Hugo versions from v0.162.0 before v0.166.0 contain a case-sensitive validation flaw in the security.http.urls IP-litera |
| CVE-2026-100697 | 8.6 | 2026-09-26 | Adminer 6.0.0 through 6.0.1, when the official ClickHouse driver plugin (plugins/drivers/clickhouse.php, rewritten in 6. |
| CVE-2026-100700 | 7.5 | 2026-09-26 | nodemailer before 10.0.6 contains a denial of service vulnerability in the addressparser free-text fallback regex patter |
| CVE-2026-100703 | 7.7 | 2026-09-26 | Kyverno 1.16.0 through 1.19.0 registers the globalcontext.Lib CEL library in its policy environment without confining it |
| CVE-2026-100704 | 7.7 | 2026-09-26 | Kyverno is a policy engine for Kubernetes. In versions 1.14.0 through 1.19.0, the ImageValidatingPolicy (policies.kyvern |
| CVE-2026-100705 | 7.6 | 2026-09-26 | Kyverno before 1.19.1 is vulnerable to server-side request forgery. The default egress blocklist (169.254.169.254, 169.2 |
| CVE-2026-100706 | 9.9 | 2026-09-26 | kyverno before 1.19.1 fails to properly validate URL-encoded path segments in Policy apiCall urlPath, allowing namespace |
| CVE-2026-100707 | 7.7 | 2026-09-26 | Kyverno before 1.19.1 contains a namespace isolation bypass in the apiCall context entry of namespaced Policy resources  |
| CVE-2026-100708 | 7.1 | 2026-09-26 | Froxlor before 2.3.13 returns the ssl_key_file column — which stores the raw PEM TLS private-key content — verbatim in t |
| CVE-2026-100709 | 7.5 | 2026-09-26 | Froxlor through 2.3.10 stores only a numeric user ID in remembered-2FA tokens (panel_2fa_tokens) without recording the a |
| CVE-2026-100711 | 7.5 | 2026-09-26 | froxlor versions before 2.3.12 fail to invalidate existing panel sessions, API keys, and 2FA trust cookies when a user p |
| CVE-2026-100713 | 7.8 | 2026-09-26 | Froxlor 2.3.10 and earlier contain a time-of-check time-of-use (TOCTOU) race condition in the SSH key synchronization cr |
| CVE-2026-100714 | 9.1 | 2026-09-26 | Froxlor before 2.3.12 does not restrict or escape the system.letsencryptchallengepath setting: unlike sibling settings h |
| CVE-2026-100715 | 9.6 | 2026-09-26 | Froxlor through 2.3.10 is vulnerable to arbitrary file deletion via symlink following in the FTP data deletion cron task |
| CVE-2026-100716 | 9.9 | 2026-09-26 | Froxlor is a server administration panel. In versions 2.3.10 and earlier, the customer data-export (DataDump) cron fails |
| CVE-2026-100717 | 9.9 | 2026-09-26 | froxlor is a server administration panel. In versions 2.3.10 and earlier, Validate::validateUrl rejects carriage return  |
| CVE-2026-100718 | 7.1 | 2026-09-26 | Froxlor through 2.3.10 does not enforce the mail.allow_external_domains policy in the EmailSender.add API command. When  |
| CVE-2026-100720 | 8.7 | 2026-09-26 | Froxlor 2.0.0 through 2.3.10 is vulnerable to stored cross-site scripting. When a customer (the lowest-privileged authen |
| CVE-2026-77203 | 8.8 | 2026-09-26 | The Groups – Memberships and Access Control plugin for WordPress is vulnerable to Privilege Escalation in all versions u |
| CVE-2026-85984 | 9.8 | 2026-09-26 | The miniOrange OTP Login, Verification and SMS Notifications plugin for WordPress is vulnerable to Authentication Bypass |
| CVE-2026-82901 | 9.8 | 2026-09-26 | The Ultra Addons for Contact Form 7 plugin for WordPress is vulnerable to Arbitrary File Upload due to insufficient file |
| CVE-2026-72668 | 7.3 | 2026-09-26 | Unintended Proxy or Intermediary ('Confused Deputy') (CWE-441) in Kibana Agent Builder can lead to privilege escalation. |
| CVE-2026-100739 | 7.3 | 2026-09-26 | A vulnerability was detected in mathurvishal CloudClassroom-PHP-Project up to 5dadec098bfbbf3300d60c3494db3fb95b66e7be.  |
| CVE-2026-100740 | 9.9 | 2026-09-27 | A vulnerability was detected in D-Link DIR-895L A1_102b07. Impacted is the function tunnel_set_params of the file tunnel |
| CVE-2025-71423 | 7.3 | 2026-09-27 | Edgelesssys Contrast is a confidential-computing runtime for Kubernetes. In versions 1.9.0 before 1.12.2, the initialize |
| CVE-2025-71425 | 7.3 | 2026-09-27 | Contrast (Edgeless Systems) before 1.8.1 logs the workload secret to stderr, and thus to Kubernetes logs, when the Contr |
| CVE-2025-71426 | 7.1 | 2026-09-27 | Contrast is a confidential-computing runtime for Kubernetes. In versions before 1.4.1, a recovering Coordinator does not |
| CVE-2026-100721 | 9.0 | 2026-09-27 | vm2 before 3.12.2 contains an authorization bypass in the NodeVM external-module resolver. When an embedder configures ` |
| CVE-2026-100723 | 7.5 | 2026-09-27 | vm2 before 3.12.2 does not apply its Buffer backing-store ownership invariant (byteOffset === 0 and buffer.byteLength == |
| CVE-2026-100744 | 7.3 | 2026-09-27 | A flaw has been found in coollabsio Coolify up to 4.1.2. The affected element is an unknown function of the file app/Htt |
| CVE-2026-100833 | 8.2 | 2026-09-27 | Contrast (edgelesssys/contrast) versions 1.14.0 before 1.23.1 generate runtime policies that fail to detect all containe |
| CVE-2026-100835 | 7.4 | 2026-09-27 | Contrast before 1.16.0 is susceptible to remote attestation relay attacks. Contrast accepted any TEE attestation report  |
| CVE-2026-100838 | 8.1 | 2026-09-27 | Contrast is a confidential-computing runtime for Kubernetes. In versions before 1.19.1, the Kata agent policies generate |
| CVE-2026-100839 | 8.4 | 2026-09-27 | Contrast is a confidential-computing runtime for Kubernetes. In versions before 1.18.0, the guest kernel's ACPI/AML hand |
| CVE-2026-100840 | 7.8 | 2026-09-27 | MONAI through 1.6.0 contains a remote code execution vulnerability in the bundle configuration engine that resolves _tar |
| CVE-2026-100841 | 7.8 | 2026-09-27 | In MONAI 1.6.0, PersistentDataset (monai/data/dataset.py) explicitly rejects the combination track_meta=True with weight |
| CVE-2026-100842 | 7.0 | 2026-09-27 | MONAI through 1.6.0 contains an eval injection vulnerability in _get_fake_spatial_shape() in monai/bundle/scripts.py. Th |
| CVE-2026-100843 | 7.8 | 2026-09-27 | MONAI versions before 1.6.0 contain a remote code execution vulnerability in the algo_from_pickle() function due to unsa |
| CVE-2026-100844 | 8.4 | 2026-09-27 | MONAI before 1.6.0 is vulnerable to OS command injection in the nnUNetV2Runner component (monai.apps.nnunet.nnunetv2_run |
| CVE-2026-100845 | 7.8 | 2026-09-27 | MONAI before 1.6.0 contains an unsafe deserialization vulnerability in the NumpyReader class that unconditionally uses n |
| CVE-2026-100846 | 7.6 | 2026-09-27 | MONAI before 1.5.2 contains a deserialization of untrusted data vulnerability in the algo_from_pickle function in monai/ |
| CVE-2026-100847 | 7.5 | 2026-09-27 | AzuraCast before 0.23.8 contains a DQL injection vulnerability in the sortOrder API parameter of AbstractSearchableListA |
| CVE-2026-100848 | 7.1 | 2026-09-27 | AzuraCast (Composer package azuracast/azuracast) before 0.23.8 validates a station's "Remote Relay" URL only for URL syn |
| CVE-2026-100849 | 7.1 | 2026-09-27 | AzuraCast is a self-hosted web radio management suite. In AzuraCast before 0.23.8, the station webhook URL validation in |
| CVE-2026-100850 | 7.7 | 2026-09-27 | AzuraCast before 0.23.8 contains a server-side request forgery and local file read vulnerability in the AutoDJ remote pl |
| CVE-2026-100851 | 7.6 | 2026-09-27 | AzuraCast before 0.23.8 contains a broken access control vulnerability in the GET /api/station/{id}/vue/profile endpoint |
| CVE-2026-100852 | 8.8 | 2026-09-27 | AzuraCast through 0.23.x contains a command injection vulnerability in the Liquidsoap config generation for live recordi |
| CVE-2026-100856 | 8.8 | 2026-09-27 | AzuraCast before 0.23.6 contains a code injection vulnerability in the remote relay password field due to incomplete mig |
| CVE-2026-100857 | 8.0 | 2026-09-27 | AzuraCast before 0.23.4 contains a code injection vulnerability in the ConfigWriter::cleanUpString() method that fails t |
| CVE-2026-100864 | 8.8 | 2026-09-27 | heym before 0.0.91 contains a sandbox escape vulnerability in the expression engine's DotList map/filter and fallback re |
| CVE-2026-100865 | 8.8 | 2026-09-27 | Heym before 0.0.53 contains multiple independent vulnerabilities. (1) The workflow condition evaluator uses Python eval( |
| CVE-2026-100746 | 7.3 | 2026-09-27 | A vulnerability was found in coollabsio Coolify up to 4.1.0. This affects the function Github::redirect of the file /web |
| CVE-2026-100741 | 9.8 | 2026-09-27 | Eval injection in the JScript event-script dispatcher in Progressive Robot Ltd's hMailServer, versions 6.0.0 through 6.3 |
| CVE-2026-100870 | 8.8 | 2026-09-27 | Sylius versions before 1.12.25, 1.13.17, 1.14.20, 2.1.16, and 2.2.9 build administrator password-reset links using the r |
| CVE-2026-100871 | 8.8 | 2026-09-27 | Sylius versions before 1.12.25, 1.13.17, 1.14.20, 2.1.16, and 2.2.9 fail to include firewall identification in JWT token |
| CVE-2026-100872 | 7.5 | 2026-09-27 | Sylius versions before 2.1.16 and 2.2.9 fail to validate payment amounts during cart recalculation, allowing unauthentic |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-67279 | MikroTik / RouterOS | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-65660 | Microsoft / SharePoint | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-87902 | WordPress / Core | 2026-09-25 | 2026-09-28 | Unknown |
| CVE-2026-5430 | WSO2 / Multiple Products | 2026-09-24 | 2026-09-27 | Unknown |
| CVE-2026-71362 | Adobe / Commerce and Magento  | 2026-09-24 | 2026-09-27 | Unknown |
| CVE-2026-93952 | Arista / VeloCloud Orchestrator | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-94127 | F5 / BIG-IP APM | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-93616 | Check Point / Multiple Products | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-85102 | Check Point / Multiple Products | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-7273 | Zyxel / GS1900 Series Switches | 2026-09-21 | 2026-09-24 | Unknown |

---

*Total entries in CISA KEV catalog: 1726*