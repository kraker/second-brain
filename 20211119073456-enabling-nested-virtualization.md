---
title: Enabling Nested Virtualization
date: 2021-11-19 07:34
tags:
- #work
- #openstack
---

## How to enable nested virtualization

Fedora:
<https://docs.fedoraproject.org/en-US/quick-docs/using-nested-virtualization-in-kvm/>

Debian/Proxmox:
https://pve.proxmox.com/wiki/Nested_Virtualization

## How to check if virtualization is enabled:

```bash
root@moxie:~# cat /sys/module/kvm_intel/parameters/nested
N
```


