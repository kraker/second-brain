---
title: append() and insert()
date: 2021-09-15T13:36:00Z
tags:
- 'python'
---

You can add new items to a list using the **append()** and **insert()** [methods](20210915132936-methods.md).

```python
>>> spam = ['cat', 'dog', 'bat']
>>> spam.append('moose')  # <- append
>>> spam
['cat', 'dog', 'bat', 'moose']
>>> spam.insert(1, 'chicken') # <- insert
>>> spam
['cat', 'chicken', 'dog', 'bat', 'moose']
```

Note the list is modified in place. Unlike a
[function](20210912120056-functions.md) it doesn't always return a value.
