---
title: Process Substitution
date: 2021-09-18 08:49
tags:
- 'bash'
---

**Process Substitution** is a form or _redirection_ where the input of output of
a process appear as a temporary file.

```bash
<( <LIST> ) 

>( <LIST> )
```

**Explanation:**

The command _LIST_ is executed and its:

* standard output filedescriptor in the <( ... ) form or
* standard input filedescriptor in the >( ... ) form

is connected to a FIFO or a file in `/dev/fd/`.

* Useful for redirecting output of a command to something that expects input
from a file and not from _stdin_.

See: [Bash Hackers Wiki - Process Substitution](https://wiki.bash-hackers.org/syntax/expansion/proc_subst)

## Further explanation

* Get variables out of subshells (and pipes) <(list) >(list)

``` bash
read < <(echo "foo")
echo $REPLY
```

``` bash
#!/bin/bash

# pro-sub: demo of process substitution

while read attr links owner group size date time filename; do
    cat <<- EOF
    Filename:   $filename
    Size:       $size
    Owner:      $owner
    Group:      $group
    Modified:   $date $time
    Links:      $links
    Attributes: $attr
    EOF
done < <(ls -l | tail -n +2)
```

## Cautionary

The scope of process substitution file descriptors is **not** stable,
guaranteed, or specified by bash.

See: [Bash Hackers Wiki - Process Substitution](https://wiki.bash-hackers.org/syntax/expansion/proc_subst)
