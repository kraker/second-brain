---
title: File Permissions
date: 2021-09-05 13:57
tags:
- 'linux'
- 'sysadmin'
---

# File Permissions

## File Types

| Attribute | File Type                                                     |
| --------- | ------------------------------------------------------------- |
| -         | A regular file                                                |
| d         | Directory                                                     |
| l         | Symbolic link                                                 |
| c         | *Character special file* (streams of bytes like /dev/null)    |
| b         | *Block special file* (handles data in blocks like HDD or DVD) |

### Examples

Regular file:

```bash
[root@server1 ~]# ls -l anaconda-ks.cfg 
-rw-------. 1 root root 1216 Feb 16 09:14 anaconda-ks.cfg
```

Directory:

```bash
[root@server1 ~]# ls -l /usr
dr-xr-xr-x.   2 root root 49152 Feb 16 09:10 bin
```

Symbolic link:

```bash
[root@server1 ~]# ls -l /usr/sbin/vigr
lrwxrwxrwx. 1 root root 4 Jul 12  2023 /usr/sbin/vigr -> vipw
```

Character device special:

```bash
[root@server1 ~]# ls -l /dev/console
crw--w----. 1 root tty 5, 1 Feb 23 14:43 /dev/console
```

Block device special:

```
[root@server1 ~]# ls -l /dev/sd*
brw-rw----. 1 root disk 8, 0 Feb 23 14:43 /dev/sda
```

## Permissions

### Permission Classes

* user (u)
* group (g)
* other (o) (aka _public_)

### Permission Modes

* add (+)
* revoke (-)
* assign (=)

### Permission Attributes

| Attribute | Files   | Directories                                                       | 
| --------- | ------- | ----------------------------------------------------------------- |
| r         | read    | Contents can be listed if *x* also set                            |
| w         | write   | Files within can be created, deleted, and renamed if *x* also set |
| x         | execute | Allows directory to be entered                                    |

### Symbolic notation

Combination of letters (ugo/rwx) and symbols (+,-,=).

### Octal notation

| Octal Value | Binary Notation | Symbolic Notation | Explanation                          |
| ----------- | --------------- | ----------------- | ------------------------------------ |
| 0           | 000             | ---               | No permissions                       |
| 1           | 001             | --x               | Execute permission only              |
| 2           | 010             | -w-               | Write permission only                |
| 3           | 011             | -wx               | Write and execute permissions        |
| 4           | 100             | r--               | Read permission only                 |
| 5           | 101             | r-x               | Read and execute permissions         |
| 6           | 110             | rw-               | Read and write permissions           |
| 7           | 111             | rwx               | Read, write, and execute permissions |

## Special File Permissions

Summary of special file permissions:

| Permission | Octal Value | Relative Value | On Files                                           | On Directories                                      |
| ---------- | ----------- | -------------- | -------------------------------------------------- | --------------------------------------------------- |
| SUID       | 4           | u+s            | User executes file with permissions of file owner  | No meaning                                          |
| SGID       | 2           | g+s            | User executes file with permissions of group owner | Files created in directory get the same group owner |
| Sticky bit | 1           | +t             | No meaning                                         | Prevents users from deleting files from other users |

### SUID - setuid

Execute binary files with the same privileges as the owner.

```bash
[root@server1 ~]# ls -l /usr/bin/su
-rwsr-xr-x. 1 root root 56944 Aug 24  2023 /usr/bin/su
[root@server1 ~]# stat -c %a /usr/bin/su
4755
```

### SGID - setgid

Execute binary files with the same privileges as the group.

```bash
[root@server1 ~]# ls -l /usr/bin/write
-rwxr-sr-x. 1 root tty 23800 Aug 24  2023 /usr/bin/write
[root@server1 ~]# stat -c %a /usr/bin/write
2755
```

### Sticky bit

The "sticky bit" is set on public or shared writable directories to protect files and subdirectories owned by normal users from being deleted or moved by other normal users.

```bash
[root@server1 ~]# ls -ld /tmp /var/tmp
drwxrwxrwt. 17 root root 4096 Feb 23 16:03 /tmp
drwxrwxrwt. 12 root root 4096 Feb 23 16:03 /var/tmp
[root@server1 ~]# stat -c %a /tmp /var/tmp
1777
1777
```

## Access Control Lists

* [Access Control Lists](20210628143348-access-control-list.md)

## Umask

* [umask](20210905082726-umask.md)

## File attributes

* [File attributes](202507262125-file-attributes.md)

## Utilities

* [Utilities](20210919173649-linux-utilities.md)
* [chmod](20200628184910-chmod.md)
* [find](20210905081005-find.md)