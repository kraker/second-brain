---
title: Case Modification
date: 2021-09-18 07:50
tags:
- bash
---

Good for normalizing input. `declare -u` upper-case `declare -l`
lower-case

| Format                          | Result                                         |
|---------------------------------|------------------------------------------------|
| ${parameter,,pattern}           | Expand the value of *parameter* into all       |
|                                 | lowercase. *pattern* is optional.              |
| ${parameter,pattern}            | Expand value of *parameter*, changing          |
|                                 | only first character to lowercase.             |
| ${parameter^<sup>pattern</sup>} | Expand value of *parameter* into all uppercase |
| ${parameter<sup>pattern</sup>}  | Expand value of *parameter*, changing only     |
|                                 | first character to uppercase.                  |

Case Conversion Parameter Expansions
