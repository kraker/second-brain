---
title: Internal Field Separator
date: 2021-09-17T19:27:00Z
tags:
- 'bash'
---

Internal Field Separator By default space, tab, and newline are used.

Example:

``` bash
#!/bin/bash

# read-ifs: read fields from a file

FILE=/etc/passwd
read -p "Enter a username > " user_name
file_info="$(grep "^$user_name:" $FILE)"
if [ -n "$file_info" ]; then
    IFS=":" read user pw uid gid name home shell <<< "$file_info"
    # Note: IFS variable assignment only lasts duration of the command
    # and you can't pipe to read so '<<<' indicates a 'here string'.

    echo "User =      '$user'"
    echo "UID =       '$uid'"
    echo "GID =       '$gid'"
    echo "Full Name = '$name'"
    echo "Home Dir. = '$home'"
    echo "Shell =     '$shell'"
else
    echo "No such user '$user_name'" >&2
    exit 1
fi
```
