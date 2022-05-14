---
title: File Permissions
date: 2021-09-05 13:57
tags:
---

## File Types

| **Attribute** | **File Type**                                                 |
| ------------- | ------------------------------------------------------------- |
| \-            | A regular file                                                |
| d             | Directory                                                     |
| l             | Symbolic link                                                 |
| c             | *Character special file* (streams of bytes like /dev/null)    |
| b             | *Block special file* (handles data in blocks like HDD or DVD) |

## Permission Attributes

| **Attribute** | **Files** | **Directories**                                                   |
| ------------- | --------- | ----------------------------------------------------------------- |
| r             | read      | Contents can be listed if *x* also set                            |
| w             | write     | Files within can be created, deleted, and renamed if *x* also set |
| x             | execute   | Allows directory to be entered                                    |


