---
title: Positional Parameters
date: 2021-09-17 19:43
tags:
- 'bash'
---

$0-$9 You can access parameters greater than 9 with parameter expansion.
${10}

- $\# Number of arguments
- use `shift` to get all parameters with a loop

  ``` bash
  #!/bin/bash
  # posit-param2: script to display all arguments
  count=1
  while [[ $# -gt 0 ]]; do
      echo "Argument $count = $1"
      count=$((count + 1))
      shift
  done
  ```

- A useful trick is to `PROGNAME="$(basename "$0")"` in the usage for
  the program name.

- You can use positional parameters to pass arguments to functions:

  ``` bash
  file_info () {
      # file_info: function to display file information

      if [[ -e "$1" ]]; then
          echo -e "\nFile Type:"
          file "$1"
          echo -e "\nFile Status:"
          stat "$1"
      else
          echo "$FUNCNAME: usage: $FUNCNAME file" >&2
          return 1
      fi
  }
  ```

  *Note: **FUNCNAME** is a shell variable, can be updated to keep
  track of* *currently executed function.*

