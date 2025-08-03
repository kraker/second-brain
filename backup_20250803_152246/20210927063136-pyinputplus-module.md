---
title: Pyinputplus Module
date: 2021-09-27 06:31
tags:
- 'python'
---

**PyInputPlus** is a Python module that provides input validation.

## Install

```bash
pip install --user pyinputplus
```

## Usage

```python
i>>> import pyinputplus as pyip
i>>> response = pyip.inputNum()
five
'five' is not a number.
42
i>>> response
42
i>>> response = input('Enter a number: ')
iEnter a number: 42
i>>> response
'42'
i>>> response = pyip.inputInt(prompt='Enter a number: ')
Enter a number: cat
'cat' is not an integer.
Enter a number: 42
i>>> response
42
```

Note, you can provide a prompt just like with `input()` by passing a _prompt_
keyword argument to the PyInputPlus function.

### Help

Use Python's `help()` function to get help for the various PyInputPlus
module functions.

E.g.

```python
i>>> help(pyip.inputChoice)
```

## See also

* <https://pyinputplus.readthedocs.io>
