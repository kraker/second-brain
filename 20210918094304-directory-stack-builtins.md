---
title: Directory Stack Builtins
date: 2021-09-18T09:43:00Z
tags:
- 'bash'
---

## dirs

Prints current directory stack.

## popd

Removes current directory from stack and `cd`s into previous directory on the
stack.

## pushd

Usage: `pushd /some/dir`

_Pushes_ directory onto stack and `cd`s into that directory.

## Example

```bash
i[akraker@localhost ~]$ pushd ~/wiki
~/wiki ~
i[akraker@localhost wiki]$ pushd ~/dotfiles
~/dotfiles ~/wiki ~
i[akraker@localhost dotfiles]$ dirs
~/dotfiles ~/wiki ~
i[akraker@localhost dotfiles]$ popd
~/wiki ~
i[akraker@localhost wiki]$ popd
~
```
