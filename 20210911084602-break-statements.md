---
title: Break Statements
date: 2021-09-11T08:46:00Z
tags:
- 'python'
---

When a [while](20210911083636-while-loop-statements.md) or
[for](20210911121753-for-loops.md) loop's [clause](20210911075037-clause.md)
reaches a **break** statement it exits the loop.

```python
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')
