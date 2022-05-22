---
title: Keyword Arguments
date: 2021-09-12 19:11
tags:
- 'python'
---

Most arguments are identified by their position in the function call.

```python
random.randint(1, 10)
# random.randint(10, 1) causes an error. 
# Order of arguments matters
```

**Keyword arguments** are identified by the _keyword_ put before them in the
function call. Keyword arguments are often _optional parameters_.

See: 
* [parameters](20210912121919-parameters.md)
* [arguments](20210912122000-arguments.md)

Example:

```python
print('Hello', end='')
print('World')
```

Output:

```bash
HelloWorld
```

Example:

```python
>>> print('cats', 'dogs', 'mice')
cats dogs mice
>>> print('cats', 'dogs', 'mice', sep=',')
cats,dogs,mice
```

_Note how the print() function automatically separates strings with a ' ', but
you can specify the field separator with `sep=`._
