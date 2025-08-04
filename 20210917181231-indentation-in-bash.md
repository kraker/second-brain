---
title: Indentation In Bash
date: 2021-09-17T18:12:00Z
tags:
---

## Indentation and Line-Continuation

Spread long commands over multiple lines

``` bash
find playground \
    ( \
        -type f \
        -not -perm 0600 \
        -exec chmod 0600 ‘{}’ ‘;’ \
    ) \
    -or \
    ( \
        -type d \
        -not -perm 0700 \
        -exec chmod 0700 ‘{}’ ‘;’ \
    )
```
