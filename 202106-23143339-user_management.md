---
title: User Management
date: 2021-06-23 14:33
tags:
- 'sysadmin'
---

# User Management

* List users currently logged in: `who`
* List all existing user accounts w/properties: `passwd -Sa` (as root)
* To add a new user, use the `useradd` command:

```
# useradd -m -G {additional_groups} -s {login_shell} {username}
```

`-m/--create-home` 
the user's home directory is created as `/home/username`.

`-G/--groups`
a comma separated list of supplementary groups which the user is also a member
of.

`-s/--shell`
a path to the user's login shell.

## Example adding a user

Add a new user creating it's home directory and otherwise using all defaults:
```
# useradd -m archie
# passwd archie
```

Add a new administrative user with `sudo` powers:
```
# useradd -m -G wheel archie
# passwd archie
```

Source: https://wiki.archlinux.org/title/Users_and_groups#User_management

## useradd and login.defs

The `useradd` command picks up default values from `/etc/default/useradd` and `/etc/login.defs`.

useradd defaults:

```bash
[root@server1 ~]# useradd -D
GROUP=100
HOME=/home
INACTIVE=-1
EXPIRE=
SHELL=/bin/bash
SKEL=/etc/skel
CREATE_MAIL_SPOOL=yes
```

login defaults:

```bash
[root@server1 ~]# grep -v ^# /etc/login.defs | grep -v ^$
MAIL_DIR	/var/spool/mail
UMASK		022
HOME_MODE	0700
PASS_MAX_DAYS	99999
PASS_MIN_DAYS	0
PASS_WARN_AGE	7
UID_MIN                  1000
UID_MAX                 60000
SYS_UID_MIN               201
SYS_UID_MAX               999
SUB_UID_MIN		   100000
SUB_UID_MAX		600100000
SUB_UID_COUNT		    65536
GID_MIN                  1000
GID_MAX                 60000
SYS_GID_MIN               201
SYS_GID_MAX               999
SUB_GID_MIN		   100000
SUB_GID_MAX		600100000
SUB_GID_COUNT		    65536
ENCRYPT_METHOD SHA512
USERGROUPS_ENAB yes
CREATE_HOME	yes
HMAC_CRYPTO_ALGO SHA512
```

## User & Group Management Commands

* useradd
* userdel
* usermod
* groupadd
* groupdel
* groupmod
* passwd
* chage

## No-Login User Account

The `/usr/sbin/nologin`  (or `/sbin/nologin`) shell is a special purpose shell for accounts that don't require a login or shouldn't be able to login to the system. 

```bash
[root@server1 ~]# grep nologin /etc/passwd | head
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:65534:65534:Kernel Overflow User:/:/sbin/nologin
tss:x:59:59:Account used for TPM access:/:/sbin/nologin
```

Example:

```bash
[root@server1 ~]# useradd -s /sbin/nologin user4
[root@server1 ~]# echo user1234 | passwd --stdin user4
Changing password for user user4.
passwd: all authentication tokens updated successfully.
[root@server1 ~]# grep user4 /etc/passwd
user4:x:1011:1011::/home/user4:/sbin/nologin
[root@server1 ~]# su - user4
This account is currently not available.
```

## Additional Resources

https://www.redhat.com/sysadmin/linux-user-account-management
* [Local User Authentication Files](202402262058-local-user-auth-files.md)