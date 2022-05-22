---
title: Boolean Operators
date: 2021-09-10 21:27
tags:
- 'python'
---

The three **Boolean operators** are:

* and
* or
* not

These are used to compare [Boolean values](20210910210804-boolean-values.md).

## Binary Boolean Operators

The _and_ and _or_ operators always take two Boolean values so they're considered
_binary_ operators.

**The _and_ Operator's Truth Table**

| **Expression**  | **Evaluates to ...** |
|-----------------|----------------------|
| True and False  | False                |
| False and True  | False                |
| False and False | False                |

**The _or_ Operator's Truth Table**

| **Expression** | **Evaluates to ...** |
|----------------|----------------------|
| True or True   | True                 |
| True or False  | True                 |
| False or True  | True                 |
| False or False | False                |

## Unary Boolean Operator

Operates on only one Boolean value which makes it _unary_.

**The _not_ Operator's Truth Table**

| **Expression** | **Evaluates to ...** |
|----------------|----------------------|
| not True       | False                |
| not False      | True                 |

## Mixing Boolean and Comparison Operators

Because [comparison operators](20210910210949-comparison-operators.md) evaluate
to Boolean values, you can use them in expressions with the Boolean operators.

```python
>>>(4 < 5) and (5 < 6)
True
```
