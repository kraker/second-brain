---
title: Manage Empty Variables
date: 2021-09-18 07:36
tags:
- bash
---

## Use a default value

`${parameter:-word}` - If parameter is empty/unset results in *word*, else 
results in *parameter* 

## Assign a default value

`${parameter:=word}` - If parameter is empty/unset results in *word* and *word* 
is assigned to *parameter*, else results in *parameter*.

*Note: Positional and other special parameters cannot be assigned this
way.*

## Display error if null or unset

`${parameter:?word}` - If *parameter* is empty/unset script exits and
*word* sent to stderr, else results in *parameter*. 

## Use an alternate value

`${parameter:+word}` - If *parameter* is empty/unset expansion results in nothing, else the
value of *word* is substituted for *parameter*, but *parameter* is not
changed.
