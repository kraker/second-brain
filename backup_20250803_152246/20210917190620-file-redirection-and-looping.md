---
title: File Redirection And Looping
date: 2021-09-17 19:06
tags:
---

Place the _<_ after the `done` statement. Also can pipe stuff to
loops.

## Redirection

```bash
#!/bin/bash

# while-read: read lines from a file

while read distro version release; do
    printf "Distro: %s\tVersion: %s\tReleased: %s\n" \
        "$distro" \
        "$version" \
        "$release"
done < distros.txt    # <- redirecting a file to a loop goes here
```

While uses the `read` builtin and will exit status 0 until EOF.

## Piping

```bash
#!/bin/bash

# while-read2: read lines from a file

sort -k 1,1 -k 2n distros.txt | while read distro version release; do
    printf "Distro: %s\tVersion: %s\tReleased: %s\n" \
        "$distro" \
        "$version" \
        "$release"
done
# since pipe executes in a subshell any variables will be lost when
# loop terminates
```
