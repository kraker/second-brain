---
title: String Operations
date: 2021-09-18 07:47
tags:
- bash
---

## String length

`${#parameter}` Expands into length of the string contained by
*parameter*. If *parameter* is either '@' or '\*' then results in number
of positional parameters.

## Substring expansion

`${parameter:offset}` `${parameter:offset:length}` Expands to portion of
string defined by *offset* and *length*. End of string unless *length*
is specified. If *offset* negative taken from end of string. (Space
needed not to be confused with ${parameter:-word}, ${foo: -5}).

## Substring removal

`${parameter#pattern}` `${parameter##pattern}` Remove leading portion of
string contained in *parameter* defined by *pattern*. *Pattern* wildcard
like used in pathname expansion. '\#' removes shortest match and '\#\#'
removes longest match.

`${parameter%pattern}` `${parameter%%pattern}` Sames as previous except
they remove text from the end of the string contained in *parameter*.

## Search and replace

`{parameter/pattern/string}` `{parameter//pattern/string}`
`{parameter/#pattern/string}` `{parameter/%pattern/string}` Expansions
perform a search-and-replace on *parameter*. In normal form only first
occurance is replaced. '//' all occurrences replaced. If '/%' '/\#'
requires match occur at beginning of string '/%' requires match occur at
end of string In every occurance *string* may be omitted, causing text
matching *pattern* to be deleted.
