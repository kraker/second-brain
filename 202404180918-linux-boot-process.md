---
title: Linux Boot Process
date: 2024-10-02 16:40:45 -05:00
modified: 2025-07-28 22:24:40 -05:00
tags:
- 'linux'
- 'sysadmin'
---

# Linux Boot Process

![](Pasted%20image%2020240418092112.png)

1. Power on
2. _Firmware_: [BIOS](202507282215-bios.md)/[UEFI](202507282221-uefi.md)
3. MBR/GPT
4. GRUB/[GRUB2](202404180922-grub2.md)
5. [Kernel](202507281552-linux-kernel.md)
6. initd/[systemd](202405121207-systemd.md)
7. Login
