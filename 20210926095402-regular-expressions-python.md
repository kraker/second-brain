---
title: Regular Expressions in Python
date: 2021-09-26T09:54:00Z
tags:
- 'python'
---

```python
>>> import re
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> print('Phone number found: ' + mo.group())
Phone number found: 415-555-4242
```

1. Import regex module with `import re`
2. Create **Regex** object with the `re.compile()` function
3. Pass the string you want to search into the **Regex** object's `search()` 
   method
4. Call the **Match** object's `group()` method to return the string of matched
   text

## Basic Regular Expression Syntax

| Specifier                | Meaning - _(This matches ...)_                   |
|--------------------------|--------------------------------------------------|
| `?`                      | 0 or 1 of preceding group                        |
| `*`                      | 0 or more of preceding group                     |
| `+`                      | 1 or more of preceding group                     |
| `{n}`                    | exactly _n_ of preceding group                   |
| `{n,}`                   | _n_ or more of preceding group                   |
| `{,m}`                   | 0 to _m_ of preceding group                      |
| `{n,m}`                  | _n_ to _m_ of preceding group                    |
| `{n,m}?` or `*?` or `+?` | non-greedy match of preceding group              |
| `^`                      | beginning of string                              |
| `$`                      | end of string                                    |
| `.`                      | any character (except newlines)                  |
| `\d`                     | any digit                                        |
| `\w`                     | any alphanumeric `[0-9a-zA-Z]`                   |
| `\s`                     | any whitespace `[ \t\n\r\f\v]`                   |
| `\D`                     | any non-digit                                    |
| `\W`                     | any non-alphanumeric                             |
| `\S`                     | any non-whitespace                               |
| `[abc]`                  | any character between the `[ ]`                  |
| `[^abc]`                 | any character that isn't between the `[ ]`       |
| `\|`                     | either or, like logical _or_                     |
| `()`                     | creates a capture group and indicates precedence |

### Escaping specifiers

If you want to detect any of the special characters in the table above, you need
to escape them. For example:

```
\. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \)
```

## See also

* <https://pythex.org/>
* <https://www.regular-expressions.info/>
* <https://regex101.com/python> \*
* <https://docs.python.org/3.6/library/re.html>
* <https://github.com/tartley/python-regex-cheatsheet/blob/master/cheatsheet.rst> \*
* <https://docs.python.org/3.9/howto/regex.html>
* <https://www.debuggex.com/> \*
  + Best regex visualizer I've found

## Groupings

Use `group()` and `groups()` (methods?) to grab specific groups of matches. Like
so:

```python
i>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
i>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
i>>> mo.group(1)
'415'
i>>> mo.group(2)
'555-4242'
i>>> mo.group(0)
'415-555-4242'
i>>> mo.group()
'415-555-4242'
i>>> mo.groups()
('415', '555-4242')
i>>> areaCode, mainNumber = mo.groups()
i>>> print(areaCode, mainNumber)
415 555-4242
```

## findall()

In Python regex `search()` will return the first result. But, `findall()`
returns all results.

## Case-Insensitive Matching

Pass `re.IGNORECASE` or `re.I` as a second argument to `re.compile()` to search
case-insensitively.

```python
>>> robocop = re.compile(r'robocop', re.I)
>>> robocop.search('RoboCop is part man, part machine, all cop.').group()
'RoboCop'
```

## Matching Newlines

Allow `.*` to match everything _including newlines_ by passing `re.DOTALL`

## Substitution

Use the `sub()` method to substitute strings that match a regex.

```python
i>>> namesRegex = re.compile(r'Agent \w+')
i>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'
```

Using groupings to include match in substitution.

```python
i>>> agentNamesRegex = re.compile(r'Agent (\w)\w*')
i>>> agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
'A**** told C**** that E**** knew B**** was a double agent.'
```

## Managing Complex Regexes

Tell `re.compile()` to ignore whitespace and comments with _verbose mode_ by
passing `re.VERBOSE`.

```python
>>> phoneRegex = re.compile(r'''(
...     (\d{3}|\(\d{3}\))?            # area code
...     (\s|-|\.)?                    # separator
...     \d{3}                         # first 3 digits
...     (\s|-|\.)                     # separator
...     \d{4}                         # last 4 digits
...     (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
...     )''', re.VERBOSE)
```

