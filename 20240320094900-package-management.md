---
title: Package Management
date: 2024-03-20T09:49:00Z
modified: 2025-08-29T10:47:03Z
tags:
- 'linux'
- 'sysadmin'
---

# Package Management

## Red Hat Family

* [rpm](20220525072458-rpm.md)

### RHEL, CentOS, Fedora, Rocky, Alma

* [dnf](20240320095100-dnf.md)

#### Common

My system is already _subscribed_ how do I list all of the repositories available?

```bash
subscription-manager repos --list
```

It's an offline exam, so we shouldn't assume that we'll be able to use subscription manager. We may have to configure the repo's like we did for the RHCSA.

If you have the repository URL, how do you easily generate the repository client file?

```bash
dnf config-manager --add-repo=http://reposerver.example.com/BaseOS
```

For the exam, manually edit the file so that it includes the line gpgcheck=0 since that's not needed and setting it up is more complicated.

### SUSE

* [zypper](20240320095300-zypper.md)

## Debian Family

* [dpkg](20240320095900-dpkg.md)
* [apt](20240320095500-apt.md)

## Arch Linux Family

* [pacman](20240320100000-pacman.md)
