---
title: Regular Expressions
date: 2021-09-05 06:50
tags:
- 'dev'
- 'linux'
- 'sysadmin'
---

Symbolic notations used to identify patterns in text

## literal characters

## metacharacters

^ $ . \[ \] { } - ? \* + ( ) | \\ *Most of these have meaning to the
shell and must be quoted*

Metacharacters

| **Character** | **Meaning**        | **Usage**                                 |
| ------------- | ------------------ | ----------------------------------------- |
| .             | Any character      |                                           |
| ^             | Anchor             | Beginning of the line                     |
| $             |                    | End of the line                           |
| \[ \]         | Bracket Expression | Specify a set of characters at a position |
|               |                    | '^' negation within brackets              |
|               |                    | '-' range of something within brackets    |

POSIX Character Classes

| **character class** | **description**                                                   |
|---------------------|-------------------------------------------------------------------|
| `[:alnum:]`         | The alphanumeric characters. \[a-za-z0-9\]                        |
| `[:word:]`          | The same as \[:alnum:\], with the addition of '\_'                |
| `[:alpha:]`         | The alphabetic characters. \[a-zA-Z\]                             |
| `[:blank:]`         | Space and tab                                                     |
| `[:cntrl:]`         | Ascii control codes. ascii 0-31 and 127                           |
| `[:digit:]`         | Numerals 0-9                                                      |
| `[:graph:]`         | The visible characters. ASCII 33-126                              |
| `[:lower:]`         | Lowercase letters                                                 |
| `[:punct:]`         | The punctuation characters.                                       |
|                     | ASCII: `\[-\!"\#$%&'()\*+,./:;\<=>?@\[\\\\\\\]\_\{}\~\]`          |
|                     | with back-tick and vertical bar                                   |
| `[:print:]`         | The printable characters. `[:graph:]` plus space character        |
| `[:space:]`         | The whitespace characters.                                        |
|                     | space, tab, carriage return, newline, vertical tab, and form feed |
| `[:upper:]`         | The uppercase characters                                          |
| `[:xdigit:]`        | Hexadecimal numbers. ASCII: `[0-9A-Fa-f]`                         |


1. POSIX Basic vs Extended Regular Expressions
   BRE `^ $ . \[ \] \*` ERE `( ) { } ? + | *` and the BRE characters

## Alternation

'|' - or

```bash
~$ echo "AAA" | grep -E 'AAA|BBB'
AAA
~$ echo "BBB" | grep -E 'AAA|BBB'
BBB
~$ echo "CCC" | grep -E 'AAA|BBB'
~$
```

## Quantifiers

'?' - Match an Element Zero or One Time

Example: (nnn) nnn-nnnn or nnn nnn-nnnn ^\(?[0-9][0-9][0-9]\)?
\[0-9\]\[0-9\]\[0-9\]-\[0-9\]\[0-9\]\[0-9\]\[0-9\]$

'\*' - Match an Element Zero or More Times

Crude example to see whether a string is a sentence.
`[[:upper:]][[:upper:][:lower:] ]*\.`

'+' - Match an Element One or More Times

Example of a line matching of one or more alphabetic characters
separated by single spaces. `^([[:alpha:]]+ ?)+$`

'{}' - Match an Element a Specific Number of Times

| **Specifier** | **Meaning**                                        |
| ------------- | -------------------------------------------------- |
| {n}           | Match if occurs exactly n times                    |
| {n,m}         | Match if occurs between n to m times including n,m |
| {n,}          | n or more times                                    |
| {,m}          | no more than m times                               |

Specifying the Number of Matches

Simplified phone number example: ^\(?[0-9]{3}\)? \[0-9\]{3}-\[0-9\]{4}$

## Resources

* [Regular expression](https://en.wikipedia.org/wiki/Regular_expression)
* [Regex One](https://regexone.com/)
* [3 Top Secret Regex Debugging Techniques Experts Use](https://youtu.be/dL2PDkU-rOw)
* [Perl Regex Debugger](https://metacpan.org/pod/Regexp::Debugger)

### Books

* [Mastering Regular Expressions](https://www.amazon.com/Mastering-Regular-Expressions-Understand-Productive-ebook/dp/B007I8S1X0/ref=sr_1_1?crid=T82AM1SS4ARZ&keywords=mastering+regular+expressions&qid=1648731362&s=digital-text&sprefix=mastering+regular+expressions%2Cdigital-text%2C79&sr=1-1)
  + Recommended by Noah A.

### Interesting articles

* [Zero Length Regular Expression](https://susam.in/maze/zero-length-regular-expression.html)
