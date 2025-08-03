---
title: Linux Boot Process
date: 2024-10-02 16:40:45 -05:00
modified: 2025-07-30 20:26:27 -05:00
tags:
- 'linux'
- 'sysadmin'
---

# Linux Boot Process

![](Pasted%20image%2020240418092112.png)

1. Power on
2. _Firmware_: [BIOS](20250728221500-bios.md)/[UEFI](20250728222100-uefi.md)
3. [MBR](20250730202300-mbr.md)/[GPT](20250730202400-gpt.md)
4. GRUB/[GRUB2](20240418092200-grub2.md)
5. [Kernel](20250728155200-linux-kernel.md)
6. initd/[systemd](20240512120700-systemd.md)
7. Login
