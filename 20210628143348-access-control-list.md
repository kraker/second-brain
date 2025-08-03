---
title: Access Control Lists
date: 2021-06-28 14:33
tags:
---

In [computer security](20210628143437-computer-security.md), an
**access-control list (ACL)** is a list of permissions associated with a
[system resource](20210628143640-system-resource.md) (object). An ACL
specifies which users or system processes are granted access to objects, as well
as what operations are allowed on given objects. Each entry in a typical ACL
specifies a subject and an operation. For instance, if a file object has an ACL
that contains _(Alice: read,write; Bob: read)_, this would give _Alice_
permission to read and write the file and only give _Bob_ permission to read it.

[Source](https://en.wikipedia.org/wiki/Access-control_list)

## References

* [Access Control Lists](https://wiki.archlinux.org/title/Access_Control_Lists)

## Security

### Administrative Access Control

Carefully control administrative accounts or limit access to them. 
