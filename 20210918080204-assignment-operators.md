---
title: Assignment Operators
date: 2021-09-18 08:03
tags:
- 'bash'
---

Variables can be assigned within arithmetic expressions.

| Notation            | Description                                        |
|---------------------|----------------------------------------------------|
| parameter = value   | Simple assignment. Assigns *value* to *parameter*. |
| paramater += value  | *parameter = parameter + value*                    |
| parameter -= value  | *parameter = parameter - value*                    |
| parameter \*= value | *parameter = parameter \* value*                   |
| parameter /= value  | *parameter = parameter / value*                    |
| parameter %= value  | *parameter = parameter % value*                    |
| parameter++         | Variable post-increment.                           |
|                     | *parameter = parameter + 1*                        |
| parameter--         | Variable post-decrement.                           |
|                     | *parameter = parameter - 1*                        |
| ++parameter         | Variable pre-increment.                            |
|                     | *parameter = parameter + 1*                        |
| --parameter         | Variable pre-decrement.                            |
|                     | /parameter = paramter - 1                          |


## Post-increment/decrement and Pre-increment/decrement

Post-increment and pre-increment (decrement) borrowed from **C**
programming language. If pre the parameter is
incremented/decremented before the parameter is returned. If post
the operation is performed after the parameter is returned.

``` bash
# post-incremented
[me@linuxbox ~]$ foo=1
[me@linuxbox ~]$ echo $((foo++))
1
[me@linuxbox ~]$ echo $foo
2
# pre-incremented
[me@linuxbox ~]$ foo=1
[me@linuxbox ~]$ echo $((++foo))
2
[me@linuxbox ~]$ echo $foo
2
```
