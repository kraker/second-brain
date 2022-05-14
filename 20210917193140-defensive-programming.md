---
title: Defensive Programming
date: 2021-09-17 19:31
tags:
---

* Important to verify assumptions
  + Carefully evaluate exit status of programs and commands that are
    used
* Watch out for filenames
  + Unix is too permissive about filenames `rm ./*` to prevent odd filenames
  + from wreaking havoc POSIX Portable Filename Character Set
    - \[A-Za-z0-9.-\_\], and don't begin filename with hyphen
