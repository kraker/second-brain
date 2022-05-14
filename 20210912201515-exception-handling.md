---
title: Exception Handling
date: 2021-09-12 20:15
tags:
- #python
---

Errors can be handled with _try_ and _except_ statements.

```python
# zeroDivide.py
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
```

```bash
[akraker@localhost python]$ python zeroDivide.py
21.0
3.5
Error: Invalid argument.
None
42.0
```
