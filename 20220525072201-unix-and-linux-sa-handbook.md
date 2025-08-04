---
title: Unix and Linux System Administration Handbook
date: 2022-05-25T00:00:00Z
tags:
- 'linux'
- 'sysadmin'
---

## Software

* [20220525072458-rpm](20220525072458-rpm.md)

Look for software on my path:

```bash
which gcc
```

Find files quickly from precompiled index of filesystem:

```bash
locate signal.h
```

### Package Management

Query for presence of package on Red Hat:

```bash
rpm -q python
```

Find what package a file belongs to:

```bash
# Red Hat
rpm -qf /etc/httpd
```

```bash
# FreeBSD
pkg which /usr/local/sbin/httpd
```

```bash
# Ubuntu
dpkg-query -S /etc/apache2
```

#### Installing packages

```bash
# Debian
sudo apt install tcpdump
sudo apt-get install tcpdump
# Red Hat
sudo yum install tcpdump
sudo dnf install tcpdump
# FreeBSD
sudo pkg install -y tcpdump
```


### Building from Source

STUB

### Installing from a web script

STUB

## Booting

* Basic Input/Output System (BIOS)
* Unified Extensible Firmware Interface (UEFI)

### UEFI



