---
title: Dictionary Data Type
date: 2021-09-23 05:18
tags:
- #python
---

A **dictionary** is a mutable collection of many values. Values are associated
with keys. Unlike [lists](20210913183709-list.md), dictionaries aren't indexed
and _keys_ can be in any order. Dictionaries are a collection of _key-value
pairs_.

* Integers or strings can be used for keys. 

```python
>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
>>> myCat
{'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
>>> myCat['size']
'fat'
>>> 'My cat has ' + myCat['color'] + ' fur.'
'My cat has gray fur.'
>>> spam = {12345: 'Luggage Combination', 42: 'The Answer'}
```

* Python 3.7+ remembers order of insertion of key-value pairs, but this
  shouldn't be relied on.
