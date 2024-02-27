---
title: Local User Authentication Files
date: 2024-02-26 20:58
tags:
- 'sysadmin'
---

# Local User Authentication Files

List of local user auth files and their backups.

```bash
[root@server1 ~]# ls -l /etc/{passwd,group,shadow,gshadow}*
-rw-r--r--. 1 root root  881 Feb 23 15:59 /etc/group
-rw-r--r--. 1 root root  873 Feb 23 15:59 /etc/group-
----------. 1 root root  710 Feb 23 15:59 /etc/gshadow
----------. 1 root root  702 Feb 23 15:59 /etc/gshadow-
-rw-r--r--. 1 root root 2203 Feb 23 15:57 /etc/passwd
-rw-r--r--. 1 root root 2158 Feb 23 15:57 /etc/passwd-
----------. 1 root root 1402 Feb 23 15:58 /etc/shadow
----------. 1 root root 1164 Feb 23 15:57 /etc/shadow-
```

## passwd

## shadow

## group

## gshadow