---
title: Multiple Assignment Trick
date: 2021-09-15 06:46
tags:
- #python
---

You can assign multiple values to list _items_ with the **multiple assignment
trick** also called **tuple unpacking**. This is a shortcut technique as opposed
to assigning each variable individually.

```python
>>> cat = ['fat', 'gray', 'loud']
>>> size, color, disposition = cat
>>> cat
['fat', 'gray', 'loud']
>>> size
'fat'
>>> color
'gray'
>>> disposition
'loud'
>>>
```
