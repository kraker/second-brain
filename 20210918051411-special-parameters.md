---
title: Special Parameters
date: 2021-09-18 05:14
tags:
- 'bash'
---

Both the `$*` and `$@` variables contain all of of the parameters passed to the
script. They're a single _special variable_ that contains all of the parameters
used when the script was ran.

| Parameter | Description                                                 |
|-----------|-------------------------------------------------------------|
| `$*`      | Expands into the list of positional parameters, starting    |
|           | with 1. When "$\*" expands into a double-quoted string each |
|           | separated by first IFS shell variable (default=space).      |
| `$@`      | Expands into the list of positional parameters, starting    |
|           | with 1. When "$@" expands each positional parameter into    |
|           | individual words surrounded by their own double-quotes.     |

The `*` and `@` Special Parameters

``` example
"$*" produces a one-word result:
"word words with spaces"
"$@" produces a two-word result:
"word" "words with spaces"
```

Note: `$@` is most useful for most situations since preserves integrity of each
positional parameter. Use this almost always.

## Counting Parameters

The special variable `$#` contains the number of command-line parameters used
when the script was run.

Example:

```bash
i[akraker@localhost bash]$ cat countparameters.sh
#!/bin/bash
# Counting command-line parameter

if [ $# -eq 1 ]
then
    fragment="parameter was"
else
    fragment="parameters were"
fi
echo $# $fragment supplied.
exit
i[akraker@localhost bash]$ ./countparameters.sh
0 parameters were supplied.
i[akraker@localhost bash]$ ./countparameters.sh Hello
1 parameter was supplied.
i[akraker@localhost bash]$ ./countparameters.sh Hello World
2 parameters were supplied.
i[akraker@localhost bash]$ ./countparameters.sh "Hello World"
1 parameter was supplied.
```

## See also

* [Bash Manual - Special Parameters](https://www.gnu.org/software/bash/manual/html_node/Special-Parameters.html)
