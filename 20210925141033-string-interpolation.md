---
title: String Interpolation
date: 2021-09-25 14:10
tags:
- #python
---

Instead of using [string concatenation](20210910201646-string-concatenation-and-replication.md)
an often easier way is to use **string interpolation**.

```python
>>> name = 'Al'
>>> age = 4000
>>> 'My name is %s. I am %s years old.' % (name, age)
'My name is Al. I am 4000 years old.'
```
