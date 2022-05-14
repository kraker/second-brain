---
title: Local And Global Scope
date: 2021-09-12 19:44
tags:
- #python
---

## Local Scope

Variables that are assigned inside a function have a **local scope** to that
function.

These are called _local variables_.

## Global Scope

Variables that have a **global scope** are (typically) defined outside of functions. 

These are called _global variables_.

### Global Statements

Global variables can be modified in a function with a [global
statement](20210912195538-global-statements.md).

## Why do scopes matter?

* Code in global scope cannot use local variables
* Code in local scope _can_ access global variables
* Code in a function's local scope cannot use variables in any other local scope
* You can use the same name for different variables if they are in different
  scopes.
  + It's not considered best practice to do this though, so this should be
    avoided unless for a good reason

## How to tell if a variable is global or local?

Four rules:

* If a variable is defined in a global scope its global
* If a _global statement_ is used in a function its global
* If a variable is used in an _assignment statement_ in a function it's local
* But if a variable is not used in an _assignment statement_ it is a global
  variable.

See: [variables](20210910202050-variables.md)
