# Vulnerability Intelligence Report

**Date:** 2026-09-25  
**Generated:** 2026-09-25T13:15:43Z  

---

## Executive Summary

Our environment faces critical exposure across 185 high-severity vulnerabilities, including two rated CVSS 10.0 in HFS2 that allow unauthenticated remote code execution and arbitrary file access. Ten new actively exploited vulnerabilities were added to CISA's Known Exploited Vulnerabilities catalog this week, spanning widely used platforms including Adobe Commerce, F5 BIG-IP, and Check Point products. RPM package manager flaws and a Velociraptor CVSS 9.9 vulnerability further elevate risk. Immediate prioritization of patching and compensating controls is essential to prevent potential breaches.

---

## Risk Narrative

The current threat landscape reflects a surge in critical, actively exploited vulnerabilities targeting enterprise infrastructure, e-commerce platforms, and network orchestration tools. Two CVSS 10.0 vulnerabilities in HFS2 are particularly alarming, as they require no authentication and enable full system compromise. CISA's addition of ten KEV entries in seven days signals that threat actors are actively weaponizing these flaws in the wild. Supply chain risks are amplified by RPM vulnerabilities affecting automated build pipelines. Collectively, these exposures create pathways to data exfiltration, ransomware deployment, and prolonged unauthorized access, with significant potential for regulatory penalties, operational disruption, and reputational damage.

---

## Prioritized Action Items

1. Immediately isolate or patch HFS2 instances running version 2.4.0 or earlier to remediate the two CVSS 10.0 unauthenticated remote code execution and file access vulnerabilities.
2. Apply vendor patches for all five newly added CISA KEV entries—WSO2, Adobe Commerce, Arista VeloCloud, F5 BIG-IP APM, and Check Point—within 24–48 hours per federal mandate guidance.
3. Patch or restrict access to the Velociraptor CVSS 9.9 vulnerability to prevent exploitation of compiled VQL hunt objects by unauthorized actors.
4. Update RPM package manager to address the two CVSS 7.8 command injection and manifest parsing flaws that could enable arbitrary code execution during package operations.
5. Audit and patch remaining high-severity CVEs, including DCMTK, redis-parser, Halo, UlakPDF, and Altera Trusted Firmware, prioritizing internet-facing and production systems.

---

## High Severity CVEs (CVSS ≥ 7.0)

| CVE ID | CVSS | Published | Description |
|--------|------|-----------|-------------|
| CVE-2026-19072 | 9.9 | 2026-09-24 | Velociraptor stores the compiled VQL in the hunt object internally to avoid having to recompile the artifacts for each e |
| CVE-2026-88907 | 7.4 | 2026-09-24 | Incorrect Authorization vulnerability in TÜBİTAK ULAKBİM UlakPDF allows Authentication Bypass.

This issue affects UlakP |
| CVE-2026-97182 | 7.3 | 2026-09-24 | A security vulnerability has been detected in halo-dev Halo up to 2.25.4/2.26.1. Affected is an unknown function of the  |
| CVE-2026-95519 | 7.8 | 2026-09-24 | A flaw was found in rpm. An attacker can supply a crafted manifest file that, when processed by a user or automation usi |
| CVE-2026-95521 | 7.8 | 2026-09-24 | A command injection flaw was found in rpm. Installing or rebuilding a source RPM whose source or spec file basenames con |
| CVE-2026-97057 | 7.5 | 2026-09-24 | redis-parser through 3.0.0 fails to validate the multi-bulk length value in RESP protocol parsing, allowing attackers to |
| CVE-2026-97059 | 8.2 | 2026-09-24 | DCMTK through 3.7.0 contains a heap over-read vulnerability in ConcatenationLoader that copies pixel data frames without |
| CVE-2026-97359 | 10.0 | 2026-09-24 | HFS2 version 2.4.0 and earlier contains a template injection vulnerability in the multipart upload handler that allows u |
| CVE-2026-97360 | 10.0 | 2026-09-24 | HFS2 version 2.4.0 and earlier contains an unauthenticated arbitrary file access vulnerability that allows unauthenticat |
| CVE-2026-13465 | 8.1 | 2026-09-24 | Stack-based buffer overflow vulnerability in Altera Trusted Firmware on HPS allows Exploitation of Improperly Configured |
| CVE-2026-13466 | 8.1 | 2026-09-24 | Incorrect calculation of buffer size vulnerability in Altera Trusted Firmware on HPS allows Overflow Buffers.

This issu |
| CVE-2026-13467 | 8.1 | 2026-09-24 | Out-of-bounds write vulnerability in Altera Trusted Firmware on HPS allows Exploitation of Improperly Configured or Impl |
| CVE-2026-51995 | 7.5 | 2026-09-24 | An issue in geelen mcp-remote 0.1.32 through 0.1.38 allows a remote attacker to obtain sensitive information via the src |
| CVE-2026-56736 | 8.2 | 2026-09-24 | phpMyFAQ is an open source FAQ web application. A stored cross-site scripting (XSS) vulnerability in versions prior to 4 |
| CVE-2026-58004 | 8.1 | 2026-09-24 | Out-of-bounds read vulnerability in Altera Trusted Firmware on HPS allows Privilege Escalation and Overflow Buffers.

Th |
| CVE-2026-58005 | 8.1 | 2026-09-24 | Out-of-bounds read vulnerability in Altera Trusted Firmware on HPS allows Privilege Escalation and Overflow Buffers.

Th |
| CVE-2026-58006 | 8.1 | 2026-09-24 | Untrusted pointer dereference vulnerability in Altera Trusted Firmware on HPS allows Exploitation of Improperly Configur |
| CVE-2026-58007 | 8.1 | 2026-09-24 | Untrusted pointer dereference vulnerability in Altera Trusted Firmware on HPS allows Exploitation of Improperly Configur |
| CVE-2026-58008 | 8.1 | 2026-09-24 | Stack-based buffer overflow vulnerability in Altera Trusted Firmware on HPS allows Exploitation of Improperly Configured |
| CVE-2026-77874 | 8.6 | 2026-09-24 | IBM Enterprise Build of Quarkus 3.27.1 through 3.27.5.SP1, and 3.33.1 through 3.33.3.SP1 is vulnerable to SQL injection. |
| CVE-2026-81539 | 8.8 | 2026-09-24 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary code due to |
| CVE-2026-81545 | 8.8 | 2026-09-24 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary commands du |
| CVE-2026-81547 | 8.8 | 2026-09-24 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary commands du |
| CVE-2026-81548 | 8.8 | 2026-09-24 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary commands du |
| CVE-2026-81549 | 9.6 | 2026-09-24 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to obtain sensitive information  |
| CVE-2026-81552 | 8.8 | 2026-09-24 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary commands du |
| CVE-2026-82093 | 8.8 | 2026-09-24 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to execute arbitrary code due to |
| CVE-2026-82094 | 7.1 | 2026-09-24 | IBM DataStage on Cloud Pak for Data 5.4.0.0 could allow a remote authenticated attacker to traverse directories on the s |
| CVE-2026-90959 | 8.1 | 2026-09-24 | A path traversal vulnerability was found in pulpcore. The content upload API accepts a 'file_url' parameter that allows  |
| CVE-2026-97362 | 7.5 | 2026-09-24 | HFS2 version 2.4.0 and earlier contains a denial of service vulnerability that allows unauthenticated attackers to cause |
| CVE-2026-56737 | 8.1 | 2026-09-24 | phpMyFAQ is an open source FAQ web application. Versions 3.2.0 through 4.1.5 contain an authentication bypass in its pub |
| CVE-2026-63203 | 7.6 | 2026-09-24 | Logto is the modern, open-source auth infrastructure for SaaS and AI apps. From 1.31.0 until 1.42.0, the Account API han |
| CVE-2026-75907 | 7.5 | 2026-09-24 | The door access control on a Norwegian Cruise Line asset grants entry based only on the credential's static 7-byte UID s |
| CVE-2026-77581 | 8.6 | 2026-09-24 | BentoPDF is a client-side PDF toolkit that is self hostable. In 2.8.6 and earlier, the certificate and timestamp CORS pr |
| CVE-2026-88357 | 7.5 | 2026-09-24 | nDPI 5.1.0 contains a memory access issue in the DNS dissector and serializer deserialization code. Specially crafted ne |
| CVE-2026-88368 | 7.5 | 2026-09-24 | NanoSVG commit 239e102ec contains an incorrect numeric conversion vulnerability in the rasterizer's nsvg__addActive() fu |
| CVE-2026-93207 | 9.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

SUNRPC: Zero rpc_gss_wire_cred at svcauth_gss_decod |
| CVE-2026-93221 | 8.1 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

nfsd: convert nfsd_net boolean flags to unsigned lo |
| CVE-2026-93224 | 8.1 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

svcrdma: Fix unmatched rn_unregister on failed acce |
| CVE-2026-93225 | 7.4 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

phy: fsl-imx8mq-usb: fix typec switch leak on probe |
| CVE-2026-93228 | 9.1 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

svcrdma: Reject Write/Reply chunks with segcount 0
 |
| CVE-2026-93229 | 7.1 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

nfsd: add missing read barrier to rpc_status_get du |
| CVE-2026-93237 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

LoongArch: Add DIRECT_MAP_PHYSMEM_END definition

g |
| CVE-2026-93250 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

vxlan: mdb: Fix use-after-free in vxlan_mdb_flush() |
| CVE-2026-93260 | 7.4 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

powerpc/xive: propagate IPI init errors to prevent  |
| CVE-2026-93262 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

md/raid5-ppl: fix use-after-free in ppl_do_flush()
 |
| CVE-2026-93265 | 7.7 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

PCI/pwrctrl: tc9563: Fix parsing the integrated Eth |
| CVE-2026-93277 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

RDMA/bnxt_re: Validate udata before executing comma |
| CVE-2026-93280 | 8.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

greybus: audio: bound the topology section sizes ag |
| CVE-2026-93282 | 8.1 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

ksmbd: fix maximum allowed access checks

The DACL  |
| CVE-2026-93425 | 9.9 | 2026-09-24 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, the patch.readRepoDirectories tRPC proc |
| CVE-2026-96744 | 7.1 | 2026-09-24 | Improper neutralization of special elements in data query logic in the cache lock implementation of the MongoDB integrat |
| CVE-2026-96750 | 7.1 | 2026-09-24 | MongoDB Compass can interpolate a database name without escaping into the initial input of its embedded MongoDB shell wh |
| CVE-2026-62368 | 8.1 | 2026-09-24 | Snipe-IT is an IT asset/license management system. Prior to 8.7.0, a user with the customfields.create permission can st |
| CVE-2026-63498 | 8.7 | 2026-09-24 | Snipe-IT is an IT asset/license management system. Prior to 8.7.0, the uploaded-files API endpoint GET /api/v1/{object_t |
| CVE-2026-79764 | 7.7 | 2026-09-24 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. From 2.5.0 |
| CVE-2026-79766 | 9.1 | 2026-09-24 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. From 2.4.1 |
| CVE-2026-88372 | 7.5 | 2026-09-24 | libsndfile 1.2.2 contains an integer overflow vulnerability in mat4_read_header() when parsing crafted MAT4 (MATLAB v4)  |
| CVE-2026-88376 | 7.5 | 2026-09-24 | Bento4 1.6.0.0 contains an integer underflow vulnerability in AP4_AvccAtom::Create() and AP4_HvccAtom::Create(). A speci |
| CVE-2026-88382 | 7.5 | 2026-09-24 | hiredis commit 29ea279 (post-v1.5.0) contains an uncontrolled memory allocation vulnerability in its RESP aggregate pars |
| CVE-2026-88390 | 7.7 | 2026-09-24 | An out-of-bounds write vulnerability in jslGetTokenValueAsString() in Espruino 2v29 (commit bffc6d0) allows crafted Java |
| CVE-2026-91122 | 8.7 | 2026-09-24 | Discourse is an open-source discussion platform. Prior to 2026.1.8, 2026.6.3, 2026.7.2, and 2026.8.0, the video placehol |
| CVE-2026-91123 | 7.2 | 2026-09-24 | Discourse is an open-source discussion platform. Prior to 2026.1.8, 2026.6.3, 2026.7.2, and 2026.8.0, the iframe src tra |
| CVE-2026-91160 | 8.2 | 2026-09-24 | OpenWA is a free, open source, self-hosted WhatsApp API gateway. Prior to 0.23.5, the /events WebSocket gateway delivers |
| CVE-2026-93284 | 8.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

drm/pagemap: dma-unmap pages before handling migrat |
| CVE-2026-93287 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

i2c: smbus: reject oversized block transfers in the |
| CVE-2026-93288 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

netfilter: nfnetlink_log: wait for rcu grace period |
| CVE-2026-93543 | 7.4 | 2026-09-24 | An out-of-bounds read in libXi's XI2 class parser in libXi before 1.8.4 could be used by malicious X servers to crash an |
| CVE-2026-93782 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

vhost-scsi: flush backend after device ioctls

vhos |
| CVE-2026-93786 | 8.1 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

ksmbd: preserve VFS inherited POSIX ACL mask

The V |
| CVE-2026-93787 | 8.1 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

smb: client: bound dirent name against end of SMB r |
| CVE-2026-93790 | 8.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

wifi: iwlwifi: mvm: fix out-of-bounds tid_data acce |
| CVE-2026-93793 | 8.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

wifi: iwlwifi: mvm: validate TX_CMD response layout |
| CVE-2026-93796 | 7.0 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

wifi: iwlwifi: pcie: null RX pointers after free

W |
| CVE-2026-93798 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

btrfs: fix reloc root cleanup in merge_reloc_roots( |
| CVE-2026-93799 | 8.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

wifi: iwlwifi: mvm: validate sta_id in BA window st |
| CVE-2026-93801 | 7.0 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

smb/client: zero-initialize stack-allocated cifs_op |
| CVE-2026-93806 | 8.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

wifi: cfg80211: validate assoc response length befo |
| CVE-2026-93810 | 7.0 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

cachefiles: Fix double fput

Fix a double fput() in |
| CVE-2026-93813 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

btrfs: tree-checker: validate INODE_REF's namelen

 |
| CVE-2026-93816 | 7.1 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

f2fs: validate inline dentry name lengths before co |
| CVE-2026-93817 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

perf: Fix addr_filter_ranges lifetime

Lee Jia Jie  |
| CVE-2026-93826 | 7.5 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

HID: hidpp: fix potential UAF in hidpp_connect_even |
| CVE-2026-93827 | 8.4 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

virtio-fs: avoid double-free on failed queue setup
 |
| CVE-2026-93830 | 7.5 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

net: stmmac: xgmac2: disable RBUE in default RX int |
| CVE-2026-94606 | 8.9 | 2026-09-24 | authentik is an open-source identity provider. Prior to 2026.2.7, 2026.5.7, and 2026.8.2, authentik email authenticator  |
| CVE-2026-94609 | 8.8 | 2026-09-24 | authentik is an open-source identity provider. Prior to 2026.2.7, 2026.5.7, and 2026.8.2, an account with delegated perm |
| CVE-2026-94611 | 8.1 | 2026-09-24 | authentik is an open-source identity provider. Prior to 2026.2.7, 2026.5.7, and 2026.8.2, authentik API serializers retu |
| CVE-2026-94612 | 7.4 | 2026-09-24 | authentik is an open-source identity provider. Prior to 2026.2.7, 2026.5.7, and 2026.8.2, an authentik SAML Source verif |
| CVE-2026-94613 | 7.5 | 2026-09-24 | authentik is an open-source identity provider. Prior to 2026.2.7, 2026.5.7, and 2026.8.2, an unauthenticated attacker ca |
| CVE-2026-97231 | 7.3 | 2026-09-24 | A vulnerability was found in volotat Anagnorisis up to 0.3.1/0.4.0. Affected is an unknown function of the file app.py o |
| CVE-2026-97409 | 8.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

nvme-fc: Do not cancel requests in io target before |
| CVE-2026-97413 | 9.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

RDMA/rtrs-srv: Fix integer underflow in process_rea |
| CVE-2026-97415 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

btrfs: tree-checker: validate names in ROOT_REF and |
| CVE-2026-97417 | 7.5 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

netfilter: nf_conntrack: use get_unaligned_be32() i |
| CVE-2026-97421 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

RDMA/umem: Be careful about boundary conditions in  |
| CVE-2026-97428 | 7.7 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

drm/amdgpu: harden FRU PIA parsing with bounded hel |
| CVE-2026-97429 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

drm/amdkfd: fix UAF race in destroy_queue_cpsch

wa |
| CVE-2026-97433 | 8.2 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

nvme: validate FDP configuration descriptor sizes

 |
| CVE-2026-97437 | 7.1 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

ntfs3: fix out-of-bounds read in ntfs_dir_emit() an |
| CVE-2026-97438 | 7.1 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

fs/ntfs3: validate index entry key bounds

[BUG]
A  |
| CVE-2026-97442 | 8.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

wifi: ath11k: fix invalid data access in ath11k_dp_ |
| CVE-2026-97444 | 7.7 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

ACPICA: add boundary checks in two places

Add boun |
| CVE-2026-97445 | 7.7 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

ACPICA: Enhance buffer validation in acpi_ut_walk_a |
| CVE-2026-97448 | 7.7 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

ACPICA: Add validation for node in acpi_ns_build_no |
| CVE-2026-97450 | 8.4 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

ACPICA: validate handler object type in two places
 |
| CVE-2026-97451 | 8.4 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

ACPICA: Fix integer overflow in acpi_ex_opcode_3A_1 |
| CVE-2026-97452 | 8.4 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

ACPICA: Prevent adding invalid references

Prevent  |
| CVE-2026-97454 | 7.7 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

ACPICA: add boundary checks in acpi_ps_get_next_fie |
| CVE-2026-97455 | 8.4 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

ACPICA: Fix use-after-free in acpi_ds_terminate_con |
| CVE-2026-97474 | 7.4 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

wifi: iwlwifi: mld: purge async notifications upon  |
| CVE-2026-97478 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

virt: acrn: Fix irqfd use-after-free during eventfd |
| CVE-2026-97496 | 7.1 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

drm/amdkfd: Fix OOB memory exposure in get_wave_sta |
| CVE-2026-97497 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

drm/amdkfd: Check bounds for allocate_sdma_queue re |
| CVE-2026-97508 | 7.5 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

thunderbolt: Set tb->root_switch to NULL when domai |
| CVE-2026-97509 | 8.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

thunderbolt: Keep XDomain reference during the life |
| CVE-2026-97513 | 7.8 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

media: chips-media: wave5: Release m2m_ctx after In |
| CVE-2026-97520 | 7.1 | 2026-09-24 | In the Linux kernel, the following vulnerability has been resolved:

gfs2: move quota_init qc iterator increment

Move q |
| CVE-2026-57178 | 7.4 | 2026-09-24 | Python Social Auth is a social authentication/registration mechanism. Prior to version 5.0.0, the `vk-app` backend accep |
| CVE-2026-61732 | 10.0 | 2026-09-24 | Decepticon is an autonomous hacking agent for red teams. Versions prior to 1.1.17 wrap web crawl results — the output of |
| CVE-2026-61741 | 9.3 | 2026-09-24 | http4s-scala-xml provides `EntityDecoder[F, scala.xml.Elem]` instances that parse XML message bodies. Prior to versions  |
| CVE-2026-61782 | 7.5 | 2026-09-24 | Rsdoctor is a build analyzer tailored for projects built with Rspack. Prior to version 1.5.16, the default Rsdoctor repo |
| CVE-2026-61788 | 7.4 | 2026-09-24 | DBHub is a database MCP server for Postgres, MySQL, SQL Server, Oracle, MariaDB, SQLite. Prior to version 0.22.6, settin |
| CVE-2026-61815 | 7.2 | 2026-09-24 | zbateson/mail-mime-parser is a mail mime parser alternative to PHP's imap* functions and Pear libraries for reading mess |
| CVE-2026-61816 | 7.5 | 2026-09-24 | zbateson/mail-mime-parser is a mail mime parser alternative to PHP's imap* functions and Pear libraries for reading mess |
| CVE-2026-63645 | 7.5 | 2026-09-24 | OpenObserve is a cloud-native observability platform. Prior to 0.90.3, OpenObserve registers the /config/runtime endpoin |
| CVE-2026-71540 | 7.5 | 2026-09-24 | Wazuh is an open-source security platform providing unified XDR and SIEM protection for endpoints and cloud workloads. F |
| CVE-2026-85056 | 8.2 | 2026-09-24 | ZITADEL is an open source identity management platform. From 4.0.0 until 4.16.1, ZITADEL Login V2 creates a browser sess |
| CVE-2026-85057 | 8.7 | 2026-09-24 | ZITADEL is an open source identity management platform. From 3.0.0 until 3.4.13 and 4.16.1, ZITADEL Actions V1 enables t |
| CVE-2026-95985 | 8.8 | 2026-09-24 | The file write tool in Amazon Kiro IDE versions before 1.0.242 might allow remote unauthenticated actors to inject craft |
| CVE-2026-13248 | 8.8 | 2026-09-24 | An Authenticated Remote Code Execution via Arbitrary File Write in the Intermec Fingerprint Command Interface vulnerabil |
| CVE-2026-13249 | 9.8 | 2026-09-24 | An unauthenticated Remote Code Execution via Arbitrary File Upload vulnerability in the web management interface in Hone |
| CVE-2026-48070 | 7.1 | 2026-09-24 | Docmost is open-source collaborative wiki and documentation software. Prior to 0.80.1, authenticated users can store att |
| CVE-2026-57440 | 7.5 | 2026-09-24 | The EmbedVideo Extension is a MediaWiki extension which adds a parser function called #ev and various parser tags for em |
| CVE-2026-61823 | 7.3 | 2026-09-24 | code16 Sharp is a Laravel-based framework for building content-management and administrative interfaces. Versions before |
| CVE-2026-61825 | 8.7 | 2026-09-24 | code16 Sharp is a Laravel-based framework for building content-management and administrative interfaces. Versions before |
| CVE-2026-77293 | 7.1 | 2026-09-24 | TREK is a collaborative travel planner. Prior to 3.3.0, the DELETE /api/trips/:tripId/collab/notes/:noteId/files/:fileId |
| CVE-2026-77294 | 8.1 | 2026-09-24 | TREK is a collaborative travel planner. Prior to 3.3.0, TREK allows an authenticated user to store an attacker-controlle |
| CVE-2026-81455 | 8.6 | 2026-09-24 | Dell ThinOS 10, versions prior to SecurityAddon_2605.10.2766_T10, contain a Missing Authentication for Critical Function |
| CVE-2026-81473 | 8.1 | 2026-09-24 | Dell Rugged Control Center (RCC), versions prior to 5.2.206, contain an Improper Authorization vulnerability. A low priv |
| CVE-2026-82157 | 8.3 | 2026-09-24 | Dell ThinOS 10, versions prior to SecurityAddon_2605.10.2766_T10, contains an Improper Certificate Validation vulnerabil |
| CVE-2026-89325 | 7.8 | 2026-09-24 | An uncontrolled search path element in InsightVM assessment content in Rapid7 Insight Agent on Windows allows a local, l |
| CVE-2026-96749 | 8.4 | 2026-09-24 | An integer overflow in the BSON document encoding component of the MongoDB Python Driver's bundled native extension may  |
| CVE-2026-77967 | 8.1 | 2026-09-24 | The Botslab G980H dash camera firmware accepts a reusable authentication value without adequately verifying its freshnes |
| CVE-2026-82164 | 7.1 | 2026-09-24 | Dell Trusted Device Client, versions prior to 8.1.359.0, contain an Incorrect Permission Assignment for Critical Resourc |
| CVE-2026-82566 | 8.8 | 2026-09-24 | The Botslab G980H dash camera firmware contains a session management vulnerability in which authentication state can rem |
| CVE-2026-84399 | 8.8 | 2026-09-24 | The Botslab G980H dash camera firmware contains an authorization vulnerability in its session based command functionalit |
| CVE-2026-85496 | 8.8 | 2026-09-24 | The Botslab G980H dash camera firmware generates session identifiers using a small sequential value space rather than a  |
| CVE-2026-93289 | 7.5 | 2026-09-24 | The affected products are vulnerable to command injection attack that could allow an unauthenticated attacker to execute |
| CVE-2026-93291 | 9.4 | 2026-09-24 | Omni C20 lacks proper certificate validation which could allow an attacker to perform a man-in-the-middle attack which c |
| CVE-2026-93354 | 8.1 | 2026-09-24 | Taskview Community before 1.56.0 contains a missing authentication vulnerability that allows unauthenticated attackers t |
| CVE-2026-96883 | 8.8 | 2026-09-24 | pgcollection is an open source extension to PostgreSQL. A type confusion issue in AWS pgcollection 2.0.0 through 2.1.1 m |
| CVE-2026-97324 | 7.3 | 2026-09-24 | A vulnerability was identified in YunaiV/zhijiantianya ruoyi-vue-pro up to 2026.08. Affected is the function updateDemoO |
| CVE-2026-97326 | 7.3 | 2026-09-24 | A weakness has been identified in songxinjianqwe Chat up to ac63d25297079eed5e4ba7e88d3b7a032637150d. Affected by this i |
| CVE-2026-81630 | 8.1 | 2026-09-24 | The Botslab G980H dash camera firmware does not adequately verify the authenticity of firmware updates. The update proce |
| CVE-2026-95699 | 9.6 | 2026-09-24 | Prior to 9/18/2026, the iSteamX mobile application's AWS policy could grant authenticated users access to wildcard MQTT  |
| CVE-2026-97646 | 7.3 | 2026-09-25 | A weakness has been identified in ningzichun student-management-system up to 98760f5711cf6dc8b4adca53a9e207ca49b02ebf. T |
| CVE-2026-97730 | 8.5 | 2026-09-25 | In Netgate pfSense Plus before 26.07 and pfSense CE before 2.9.0, a Local File Inclusion (LFI) vulnerability in the Dash |
| CVE-2026-97731 | 7.1 | 2026-09-25 | MinIO through 7aac2a2 does not verify that every x-amz-* header present on a request also appears in the client-supplied |
| CVE-2026-97735 | 8.0 | 2026-09-25 | ITFlow before 26.08 allows SVG attachments in the ticket email parser (cron/ticket_email_parser.php) for email messages  |
| CVE-2026-97737 | 7.4 | 2026-09-25 | In Wakapi before 2.17.6, the user caching service allows a lookup to be resolved in an unintended lookup context, leadin |
| CVE-2026-97818 | 8.6 | 2026-09-25 | phpIPAM through 1.8.3 has incorrect authorization for id=="admins" and id=="all" in api/controllers/User.php. |
| CVE-2026-14281 | 9.8 | 2026-09-25 | The Automation Web Platform – Notifications and OTP for WooCommerce, Advanced Country Code plugin for WordPress is vulne |
| CVE-2026-62062 | 8.8 | 2026-09-25 | Cross-Site Request Forgery (CSRF) vulnerability in Elementor Website Builder allows Cross Site Request Forgery.

This is |
| CVE-2026-83591 | 7.2 | 2026-09-25 | The AMP for WP – Accelerated Mobile Pages plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Comment  |
| CVE-2026-84279 | 7.2 | 2026-09-25 | The Fancy Product Designer plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'output_format' par |
| CVE-2026-84281 | 7.2 | 2026-09-25 | The Fancy Product Designer plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'productTitle' in '_fpd |
| CVE-2026-89055 | 9.1 | 2026-09-25 | The Customer Reviews for WooCommerce plugin for WordPress is vulnerable to authorization bypass in all versions up to, a |
| CVE-2026-93303 | 7.2 | 2026-09-25 | The HT Contact Form – Drag & Drop Form Builder for WordPress plugin for WordPress is vulnerable to Stored DOM-Based Cros |
| CVE-2026-93399 | 9.1 | 2026-09-25 | The Bookly plugin for WordPress is vulnerable to Insecure Direct Object Reference in versions up to, and including, 28.2 |
| CVE-2026-96039 | 7.2 | 2026-09-25 | The BA Book Everything plugin for WordPress is vulnerable to Stored Cross-Site Scripting via first_name Parameter in all |
| CVE-2026-13456 | 7.5 | 2026-09-25 | The WP Maps – Google Maps,OpenStreetMap,Mapbox,Store Locator,Listing,Directory & Filters plugin for WordPress is vulnera |
| CVE-2026-19804 | 8.8 | 2026-09-25 | The s2Member – Excellent for All Kinds of Memberships, Content Restriction Paywalls & Member Access Subscriptions plugin |
| CVE-2026-84280 | 7.2 | 2026-09-25 | The Fancy Product Designer plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Shortcode Order 'elemen |
| CVE-2026-89406 | 7.5 | 2026-09-25 | The Modula Image Gallery – Photo Grid & Video Gallery plugin for WordPress is vulnerable to unauthorized disclosure of p |
| CVE-2026-89426 | 8.8 | 2026-09-25 | The Knit Pay – Cashfree, Instamojo, Razorpay, PayPal and more plugin for WordPress is vulnerable to Privilege Escalation |
| CVE-2026-92713 | 8.1 | 2026-09-25 | The Modula Image Gallery – Photo Grid & Video Gallery plugin for WordPress is vulnerable to arbitrary file deletion due  |
| CVE-2026-93654 | 7.2 | 2026-09-25 | The Premium Packages – Sell Digital Products Securely plugin for WordPress is vulnerable to Stored Cross-Site Scripting  |
| CVE-2026-93901 | 7.3 | 2026-09-25 | The Optima Express IDX plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including,  |
| CVE-2026-94573 | 7.2 | 2026-09-25 | The Repeater Fields for Elementor Forms plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Repeater F |
| CVE-2026-95864 | 7.2 | 2026-09-25 | The Themify Builder plugin for WordPress is vulnerable to Stored Cross-Site Scripting via 'css[fonts]' Parameter in all  |
| CVE-2026-95866 | 7.2 | 2026-09-25 | The User Profile Builder – Beautiful User Registration Forms, User Profiles & User Role Editor plugin for WordPress is v |
| CVE-2026-96568 | 7.2 | 2026-09-25 | The Restaurant Menu and Food Ordering plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the 'phone_n |
| CVE-2026-96752 | 7.2 | 2026-09-25 | The Zero Spam for WordPress plugin for WordPress is vulnerable to Stored Cross-Site Scripting via Nested POST Array Keys |
| CVE-2026-97875 | 8.1 | 2026-09-25 | Rojo's "rojo serve" HTTP API (default port 34872) has no Host/Origin header validation, making it vulnerable to DNS rebi |

---

## CISA KEV New Entries (Last 7 Days)

| CVE ID | Vendor / Product | Date Added | Due Date | Ransomware |
|--------|-----------------|------------|----------|------------|
| CVE-2026-5430 | WSO2 / Multiple Products | 2026-09-24 | 2026-09-27 | Unknown |
| CVE-2026-71362 | Adobe / Commerce and Magento  | 2026-09-24 | 2026-09-27 | Unknown |
| CVE-2026-93952 | Arista / VeloCloud Orchestrator | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-94127 | F5 / BIG-IP APM | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-93616 | Check Point / Multiple Products | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-85102 | Check Point / Multiple Products | 2026-09-22 | 2026-09-25 | Unknown |
| CVE-2026-7273 | Zyxel / GS1900 Series Switches | 2026-09-21 | 2026-09-24 | Unknown |
| CVE-2025-39964 | Linux / Kernel | 2026-09-18 | 2026-09-21 | Unknown |
| CVE-2026-53266 | Linux / Kernel | 2026-09-18 | 2026-09-21 | Unknown |
| CVE-2025-39682 | Linux / Kernel | 2026-09-18 | 2026-09-21 | Unknown |

---

*Total entries in CISA KEV catalog: 1723*