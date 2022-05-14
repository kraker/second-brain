---
title: Grouping Commands
date: 2021-09-18 08:48
tags:
---

Group command `{ command1; command2; [command3; ...] }` Must have a
space before/after braces. Last command terminated by a ';'.

Subshell `(command1; command2; [command3;...])`

```bash
ls -l > output.txt
echo "Listing of foo.txt" >> output.txt
cat foo.txt >> output.txt

# can be written with a group command
{ ls -l; echo "Listing of foo.txt"; cat foo.txt; } > output.txt

# or as a subshell command
(ls -l; echo "Listing of foo.txt"; cat foo.txt) > output.txt

# groupings really useful for pipelines
{ ls -l; echo "Listing of foo.txt"; cat foo.txt; } | lpr
```

*Note: any changes made in a subshell environment, such as variables*
*are lost when the subshell exits. Therefore most often group commands*
*are preferrable to subshells.*
