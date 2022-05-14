---
title: Escape Characters
date: 2021-09-25 13:45
tags:
- #python
---

An **escape character** allows use of characters that otherwise would be
impossible to use in a string.

```python
>>> spam = 'Say hi to Bob\'s mother.'
>>> spam
"Say hi to Bob's mother."
```

## Escape Characters

| Escape character | Prints as            |
|------------------|----------------------|
| `\'`             | Single quote         |
| `\"`             | Double quote         |
| `\t`             | Tab                  |
| `\n`             | Newline (line break) |
| `\\`             | Backslash            |

```python
>>> print("Hello there!\nHow are you?\nI\'m doing fine.")
Hello there!
How are you?
I'm doing fine.
>>>
```
