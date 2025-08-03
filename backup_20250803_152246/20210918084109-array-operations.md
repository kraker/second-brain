---
title: Array Operations
date: 2021-09-18 08:41
tags:
- 'bash'
---

##  Outputting Contents

`*` and `@` can be used to access every element in an array.

``` bash
[me@linuxbox ~]$ animals=("a dog" "a cat" "a fish")
[me@linuxbox ~]$ for i in ${animals[*]}; do echo $i; done
a
dog
a
cat
a
fish
[me@linuxbox ~]$ for i in ${animals[@]}; do echo $i; done
a
dog
a
cat
a
fish
[me@linuxbox ~]$ for i in "${animals[*]}"; do echo $i; done
a dog a cat a fish
[me@linuxbox ~]$ for i in "${animals[@]}"; do echo $i; done
a dog
a cat
a fish
```

## Number of array elements

``` bash
[me@linuxbox ~]$ a[100]=foo
[me@linuxbox ~]$ echo ${#a[@]} # number of array elements
1
[me@linuxbox ~]$ echo ${#a[100]} # length of element 100
3
```

## Finding subscripts (indexes)

`${!array[*]} ${!array[@]}` both return indexes of the array

``` bash
[me@linuxbox ~]$ foo=([2]=a [u]=b [6]=c)
[me@linuxbox ~]$ for i in "${foo[@]}"; do echo $i; done
a
b
c
[me@linuxbox ~]$ for i in "${!foo[@]}"; do echo $i; done
2
4
6
```

## Adding elements to arrays

Appending elements to arrays

``` bash
[me@linuxbox ~]$ foo=(a b c)
[me@linuxbox ~]$ echo ${foo[@]}
a b c
[me@linuxbox ~]$ foo+=(d e f)
[me@linuxbox ~]$ echo ${foo[@]}
a b c d e f
```

## Sorting arrays

``` bash
#!/bin/bash

# array-sort: Sort an array

a=(f e d c b a)

echo "Original array: ${a[@]}"
a_sorted=($(for i in "${a[@]}"; do echo $i; done | sort))
echo "Sorted array: ${a_sorted[@]}"
```

``` bash
[me@linuxbox ~]$ array-sort
Original array: f e d c b a
Sorted array: a b c d e f
```

## Deleting Arrays and Elements

Use `unset` foo=(a b c d e f) unset foo echo ${foo\[@\]}

or unset 'foo\[2\]' echo ${foo\[@\]} a b d e f

*Note: assigning an empty value to an array doesn't empty it's
contents.*
