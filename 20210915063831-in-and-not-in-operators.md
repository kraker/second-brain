---
title: in and not in Operators
date: 2021-09-15T06:38:00Z
tags:
- 'python'
---

You can determine whether a value is **in** or **not in** a [list](20210913183709-list.md). 
Returns _True_ or _False_.

```python
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> 'cat' in spam
False
>>> 'howdy' not in spam
False
>>> 'cat' not in spam
True
```

You can also use the _in_ and _not_ operators to check if a key or value exists
in a [dict](20210923051842-dictionary-data-type.md).

```python
>>> spam = {'name': 'Zophie', 'age': 7}
>>> 'name' in spam.keys()
True
>>> 'Zophie' in spam.values()
True
>>> 'color' in spam.keys()
False
>>> 'color' not in spam.keys()
True
>>> 'color' in spam
False
```

Note, the last `'color' in spam` style short-hand always checks the if it exists
as a _key_.
