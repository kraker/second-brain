---
title: File Attributes
date: 2025-07-26
tags:
---

# File Attributes

Commands:

* `chattr`
* `lsattr` 

These are a few useful attributes. Not all filesystems support every attribute.

- `a` - append only: File can only be opened for appending.
- `c` - compressed: Enable filesystem-level compression for the file.
- `i` - immutable: Cannot be modified, deleted, renamed, linked to. Can only be set by root.
- `j` - data journaling: Use the [journal](https://wiki.archlinux.org/title/File_systems#Journaling "File systems") for file data writes as well as metadata.
- `m` - no compression: Disable filesystem-level compression for the file.
- `A` - no atime update: The file's atime will not be modified.
- `C` - no copy on write: Disable copy-on-write, for filesystems that support it.

See `man chattr` for a complete list of attributes and for more info on what each attribute does.

A common operation is to make a file _immutable_ with:

```bash
chattr +i file
```

To remove an attribute on a file just change `+` to `-`.

Example:

```bash
[root@rhel9-a ~]# chattr +i /etc/passwd
[root@rhel9-a ~]# lsattr /etc/passwd
----i----------------- /etc/passwd
```
