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

## Permission Attributes

| Attribute | Files   | Directories                                                       | 
| --------- | ------- | ----------------------------------------------------------------- |
| r         | read    | Contents can be listed if *x* also set                            |
| w         | write   | Files within can be created, deleted, and renamed if *x* also set |
| x         | execute | Allows directory to be entered                                    |

### Octal permission notation

| Octal | Binary | File Mode | Explanation                          |
| ----- | ------ | --------- | ------------------------------------ |
| 0     | 000    | ---       | No permissions                       |
| 1     | 001    | --x       | Execute permission only              |
| 2     | 010    | -w-       | Write permission only                |
| 3     | 011    | -wx       | Write and execute permissions        |
| 4     | 100    | r--       | Read permission only                 |
| 5     | 101    | r-x       | Read and execute permissions         |
| 6     | 110    | rw-       | Read and write permissions           |
| 7     | 111    | rwx       | Read, write, and execute permissions | 

## Utilities

* [20200628184910-chmod](20200628184910-chmod.md)