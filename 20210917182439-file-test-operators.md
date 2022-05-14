---
title: File Test Operators
date: 2021-09-17 18:24
tags:
- #bash
---


| Expression      | Is True If                                                                                                                                    |
|-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| file1 -ef file2 | *file1* and *file2* the two filenames refer to the same hardlinked file                                                                        |
| file1 -nt file2 | *file1* is newer than *file2*                                                                                                                  |
| file1 -ot file2 | *file1* is older than *file2*                                                                                                                  |
| -b file         | *file* exists and is a block-special (device) file                                                                                             |
| -c file         | *file* exists and is a character-special (device) file                                                                                         |
| -d file         | *file* exists and is a directory                                                                                                               |
| -e file         | *file* exists                                                                                                                                  |
| -f file         | *file* exists and is a regular file                                                                                                            |
| -g file         | *file* exists and is set-group-**ID**                                                                                                          |
| -G file         | *file* exists and is owned by effective group **ID**                                                                                           |
| -k file         | *file* exists and has its "stkicky bit" set                                                                                                    |
| -L file         | *file* exists and is a symbolic link                                                                                                           |
| -O file         | *file* exists and is owned by the effective user **ID**                                                                                        |
| -p file         | *file* exists and is a named pipe                                                                                                              |
| -r file         | *file* exists and is readable                                                                                                                  |
| -s file         | *file* exists and has a length greater than zero                                                                                               |
| -S file         | *file* exists and is a network socket                                                                                                          |
| -t fd           | *fd* is a file descriptor directed to/from the terminal. This can be used to determine whether standard input/output/error is being redirected |
| -u file         | *file* exists and is setuid                                                                                                                    |
| -w file         | *file* exists and is writable                                                                                                                  |
| -x file         | *file* exists and is executable                                                                                                                |
