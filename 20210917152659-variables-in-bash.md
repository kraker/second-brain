---
title: Variables In Bash
date: 2021-09-17T15:27:00Z
tags:
- 'bash'
---


``` bash
key=var
echo $key
var
```

_Variables aren't assigned until the shell encounters them._

## Naming Rules

1. Variable names may consist of `[:alnum:_]+`
2. The first character of a variable name must be either a letter or `_`
3. Spaces and punctuation not allowed
4. Common convention is for CONSTANTS to be uppercase and variables
   lowercase.

## Assigning Values

* Treats all variables as strings.
* No spaces in assignment. `key= "var"` won't work, for example.
* Can have multiple assignments on a single line: `a=5 b="a string"`

## Expansion

Variable names may be surrounded by optional curly braces, {} Useful when
variable names become ambiguous.

``` bash
[me@linuxbox ~]$ filename="myfile"
[me@linuxbox ~]$ touch "$filename"
[me@linuxbox ~]$ mv "$filename" "$filename1"
mv: missing destination file operand after `myfile'
Try `mv --help' for more information.
[me@linuxbox ~]$ mv "$filename" "${filename}1"
```

Good practice to enclose variables and command substitutions in double quotes to
limit the effects of word-splitting by the shell.
