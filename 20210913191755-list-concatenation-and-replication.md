---
title: List Concatenation And Replication
date: 2021-09-13T19:17:00Z
tags:
- 'python'
---

Just like with [strings](20210910201646-string-concatenation-and-replication.md)
lists can be **concatenated** and **replicated** with `+` and `*`.

```python
>>> [1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']
>>> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
>>> spam = [1, 2, 3]
>>> spam = spam + ['A', 'B', 'C']
```
