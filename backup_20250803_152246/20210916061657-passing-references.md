---
title: Passing References
date: 2021-09-16 06:17
tags:
- 'python'
---

Arguments get passed to functions as **references**. When the function is called
the values of the arguments are copied to the parameter variables. For lists and
dictionaries a copy of the reference is used for the parameter.

```python
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)
```

```bash
i[akraker@localhost python]$ python passingReference.py
[1, 2, 3, 'Hello']
```

Because `someParameter` and `spam` both use a copy of the reference, the list is
modified.

Note, forgetting this can be the source of bugs.
