---
title: Global Statements
date: 2021-09-12T19:55:00Z
tags:
- 'python'
---

You can modify a global variable from within a function with a **global
statement**.

_Note: this isn't done very often. It's better to be able to treat functions as
**black boxes**.

```python
def spam():
    global eggs   # <- global statement
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
```

Output:

```bash
spam
```
