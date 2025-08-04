---
title: For C Language Form
date: 2021-09-17T19:16:00Z
tags:
- 'bash'
---

Introduced in recent versions of bash for (( expression1;
expression2; expression3 )); do dommands done

Here *expression1*, *expression2*, and *expression3* are
arithmetic and *commands* are the commands to be performed.

``` bash
#!/bin/bash
# simple_counter: demo of C style for command
for (( i=0; i<5; i=i+1 )); do
    echo $i
done
```
