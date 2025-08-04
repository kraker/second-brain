---
title: File Redirection
date: 2021-09-05T13:51:00Z
tags:
---

## File Streams

1.  standard input
    *stdin* 0

2.  standard output
    *stdout* 1

3.  standard error
    *stderr* 2

## I/O Redirection

Change were output goes and input comes from.

| **Operator**  | **Action**                                                                   |
| ------------- | ---------------------------------------------------------------------------- |
| \>            | Redirect to file                                                             |
| \>\>          | Append to file                                                               |
| |             | Pipe output                                                                  |
| 2\>           | Redirect *stderr* to file                                                    |
| 2\>&1         | Redirect *stderr* to file descriptor 1, if no file then default is to screen |
| &\>,$\>\>     | Redirect *stdout* and *stderr* to file                                       |
| 2\> /dev/null | Dispose of *stderr*                                                          |
