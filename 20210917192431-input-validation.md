---
title: Input Validation
date: 2021-09-17 19:24
tags:
- bash
---

Often this is the difference between well-written and poorly written
programs. One-off or individually used programs you can get away with
little to no input validation. But on scripts that are shared by
multiple users input validation is important.

<span class="label">Example</span>

``` bash
#!/bin/bash

# read-validate: validate input

invalid_input () {
    echo "Invalid input '$REPLY'" >&2
    exit 1
}

read -p "Enter a single item > "

# input is empty (invalid)
[[ -z "$REPLY" ]] && invalid_input

# input is multiple items (invalid)
(( "$(echo "$REPLY" | wc -w)" > 1 )) && invalid_input

# is input a valid filename?
if [[ "$REPLY" =~ ^[-[:alnum:]\._]+$ ]]; then
    echo "'$REPLY' is a valid filename."
    if [[ -e "$REPLY" ]]; then
        echo "And file '$REPLY' exists."
    else
        echo "However, file '$REPLY' does not exist."
    fi

    # is input a floating point number?
    if [[ "$REPLY" =~ ^-?[[:digit:]]*\.[[:digit:]]+$ ]]; then
        echo "'$REPLY' is a floating point number."
    else
        echo "'$REPLY' is not a floating point number."
    fi

    # is input an integer?
    if [[ "$REPLY" =~ ^-?[[:digit:]]+$ ]]; then
        echo "'$REPLY' is an integer."
    else
        echo "'$REPLY' is not an integer."
    fi
else
    echo "The string '$REPLY' is not a valid filename."
fi
```

## Verify Input

* If receives input must be able to deal with any possible input `[[
  $REPLY =~ ^[0-3]$ ]]`
* Design as a function of time
  + Sometimes quick and dirt "one-off" scripts is ok
  + Production scripts should be more carefully thought out
