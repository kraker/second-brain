---
title: Continue Statements
date: 2021-09-11 11:18
tags:
- #python
---

**continue** statements are used inside of
[while](20210911083636-while-loop-statements.md) loops to jump back to the start of
the loop and reevaluate the loop's [condition](20210911072918-conditions.md). In 
[for](20210911121753-for-loops.md) loop's it jumps to the next iteration of the
loop.

## Example

```python
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
```
