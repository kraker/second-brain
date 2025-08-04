---
title: String Comparison Operators
date: 2021-09-17T18:38:00Z
tags:
- 'bash'
---

| Expression         | Is True If…                                                                                                                                                                         |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| string             | string is not null                                                                                                                                                                  |
| -n string          | The length of string is greater than zero                                                                                                                                           |
| -z string          | The length of string is zero                                                                                                                                                        |
| string1 = string2  | *string1* and *string2* are equal. Single or double                                                                                                                                 |
| string1 == string2 | equal signs may be used. The use of double equal                                                            signs is supported by bash and is preferred, but is not POSIX compliant |
| string1 != string2 | *string1* and *string2* are not equal                                                                                                                                               |
| string1 > string2  | *string1* sorts after *string2*                                                                                                                                                     |
| string1 < string2  | *string1* sorts before *string2* *Note: the **>** and **<** must be escaped or quoted when used with test or they will be interpreted by the shell as redirect operators.*          |
