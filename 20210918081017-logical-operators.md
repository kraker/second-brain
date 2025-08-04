---
title: Logical and Comparison Operators
date: 2021-09-18T08:10:00Z
tags:
- 'bash'
---

| Operator            | Description                                          |
|---------------------|------------------------------------------------------|
| `<=`                | Less than or equal to                                |
| `>=`                | Greater than or equal to                             |
| `<`                 | Less than                                            |
| `>`                 | Greater than                                         |
| `==`                | Equal to                                             |
| `!=`                | Not equal to                                         |
| `&&`                | Logical AND                                          |
| `||`                | Logical OR                                           |
| `expr1?expr2:expr3` | Comparison (ternary) operator. if expression *expr1* |
|                     | evaluates to be non-zero (arithmetic true), then     |
|                     | *expr2*; else *expr3*.                               |

```bash
# arithmetic true/false
[me@linuxbox ~]$ if ((1)); then echo "true"; else echo "false"; fi
true
[me@linuxbox ~]$ if ((0)); then echo "true"; else echo "false"; fi
false

# ternary operator example: "toggle"
[me@linuxbox ~]$ a=0
[me@linuxbox ~]$ ((a<1?++a:--a))
[me@linuxbox ~]$ echo $a
1
[me@linuxbox ~]$ ((a<1?++a:--a))
[me@linuxbox ~]$ echo $a
0
```
