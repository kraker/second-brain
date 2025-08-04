---
title: Multiline Strings
date: 2021-09-25T13:55:00Z
tags:
- 'python'
---

A **multiline string** begins and ends with either 3 single-quotes or
double-quotes.

```python
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
```

Note, [escape characters](20210925134527-escape-characters.md) aren't necessary
in multiline strings.

## Multiline Comments

A multiline string is often used for multiline comments.

```python
"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

this program was designed for Python 3, not Python 2.
"""

def spam():
  """This is a multiline comment to help
  explain what the spam() function does."""
  print('Hello!')
```
