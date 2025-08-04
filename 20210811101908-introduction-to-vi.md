---
title: Introduction to Vi
date: 2021-08-11T10:19:00Z
tags:
- 'vim'
---

This article aims to cover the basics of using **Vi** (or **Vim**) to edit text.
Many modern linux distributions contain either Vi or Vim. Often Vim, which
stands for _vi improved_ will be symbolically linked (or aliased) to vi on
Linux systems. Most if not all of what's in this tutorial is interchangeable
between Vi or Vim.

Vi was first written in 1976 by Bill Joy at the University of California at
berkley. vim was written by and is still maintained by Bram Moolenaar.

# Why Learn Vi/Vim?

* Vi is almost always available on Linux systems. If you're ssh'd into a server
	and you don't have the ability (or the authority...) to install additional
	software packages, vi will almost always be available by default.  You may not
	always have access to a graphical CLI editor like nano.
* Vi is lightweight and fast. Vi is designed for typing speed and efficiency.
	There's a learning curve, but once over that hurdle you may find yourself
	wondering why all user interfaces where you edit text don't have a _vi mode._
* You want other Linux nerds to respect you and you're irrationally concerned
	with being judged by based on your bash history.

# Basics

Starting vi (vim):

``` bash
$ vi
$ # Or ...
$ vim
```

You should see something like the following in your terminal:

``` viml
  1
~
~                                 VIM - Vi IMproved
~
~                                  version 8.2.3182
~                              by Bram Moolenaar et al.
~                         Modified by <bugzilla@redhat.com>
~                    vim is open source and freely distributable
~
~                           Become a registered Vim user!
~                   type  :help register<Enter>   for information
~
~                   type  :q<Enter>               to exit
~                   type  :help<Enter>  or  <F1>  for on-line help
~                   type  :help version8<Enter>   for version info
~
~
~
```

To exit vi (vim) type `:q` then press **Enter**.

``` viml
:q
```

This should return you to the shell prompt. If for some reason this doesn't work
we can _force_ the issue with:
_(this can sometimes happen if we've made a change to the file that hasn't been
written yet.)_

``` viml
:q!
```

**Tip:** if you get lost in vi/vim try pressing the **Esc** key twice.

You can create a new file with vi by passing a filename that doesn't exist as
an argument:

``` bash
$ vi foo.txt
```

Or you may open a file that already exists with vi by providing the file as an
argument:

``` bash
$ vi /path/to/somefile.txt
```

## Editing Modes

Vi is a modal editor. When vi starts it's in _command mode._ In this mode
almost everything is a command. Be careful what you type in this mode, you may
end up executing commands you didn't intend.

### Entering Insert Mode

After you've opened or created a file that you're trying to edit, in order to
add some text you need to enter _insert mode._ To do this press the **i** key.
You should see the following at the bottom of the screen:

``` vim
-- insert --
```

Try typing some text:

``` txt
the quick brown fox jumped over the lazy dog.
```

To exit insert mode and return to command mode, press the **Esc** key.

### Saving Your Work

To save changes to your file enter an _ex command_ while in command mode. You
can do this by typing **:**.  You should see a colon character appear at the
bottom of your terminal.
```
:
```

To write our modified file, type a **w** and then press **Enter.**
```
:w
```

The file will be written to disk. You should get a confirmation message at the
bottom of your terminal that looks similar to this:
```
"foo.txt" [new] 1l, 46c written
```

**Tip:** the vim documentation confusingly calls command mode _normal mode_ and
that _ex_ commands are called _command mode._

### Moving Around the Buffer

While in command mode, vi offers a large amount of movement commands.  Many of
these are shared with the `less` pager. In fact many Linux utilities have some
type of vi mode.  Once you learn these, this skill is farily _portable._

Cursor movement keys

| **key**                 | **Moves The Cursor**                                            |
|-------------------------|-----------------------------------------------------------------|
| `l` or right arrow      | Right one character                                             |
| `h` or left arrow       | Left one character                                              |
| `j` or down arrow       | Down one line                                                   |
| `k` or up arrow         | Up one line                                                     |
| `0` (zero)              | Beginning of the current line                                   |
| `^`                     | First non-whitespace character on the current line              |
| `$`                     | End of the current line                                         |
| `w`                     | Beginning of the next word or punctuation character             |
| `W`                     | Beginning of the next word, ignoring punctuation characters     |
| `b`                     | Beginning of the previous word or punctuation character         |
| `B`                     | Beginning of the previous word, ignoring punctuation characters |
| `Ctrl-f` or `Page Down` | Down one page                                                   |
| `Ctrl-b` or `Page Up`   | Up one page                                                     |
| `#G`                    | To line #.                                                      |
|                         | For example, `12G` moves to the 12th line of the file           |
| `G`                     | To the last line of the file                                    |
| `gg`                    | To the first line of the file                                   |

When vi was originally written not all video terminals had arrow keys and
commonly the letters _h_, _j_, _k_, and _l_ were used.  Many commands in vi can
be prefixed with a number. We can specify the number of times a command will be
executed. For example, `5j` will move the cursor down 5 lines.

### Basic Editing

In general editing text consists of basic operations like inserting text,
deleting text, moving text around by cutting and pasting, etc. Vi supports all
of this and more. Vi also provides undo if you press **u** while in command mode.
This undo's the last change you made and will come in handy while you practice
some basic text editing in Vi.

#### Appending and Inserting Text

To _append_ text after the cursor press **a** and then type the text that you
with to add.

Try moving the cursor to the end of the line in your text file and appending
some text.

```
The quick brown fox jumped over the lazy dog. It was cool.
```

Type **Esc** to get out of insert mode after you've finished inserting your
text.

Instead of moving to the end of the line and typing **a** in order to append
text. You can type **A** and this will automatically put you at the end of the
line and in insert mode. Similarly lowercase **i** allows you to enter insert
mode before the cursor, but capital **I** puts you in insert mode at the
beginning of the line. As you grow more familiar with the variety of Vi commands
at your disposal you'll learn that for most things that you would want to do,
there's often a short-cut available like this.

#### Opening a Line

We can also insert a line above or below the current line and enter insert mode.
To do this type **o** to insert a line below the current one and type **O** to
insert a line above the one your cursor is currently on.

For example:

```
Line above.
The quick brown fox jumped over the lazy dog. It was cool.
Line below.
```

Again to exit insert mode just type **Esc**.

#### Deleting text

Vi offers a variety of ways to delete text. To delete the character underneath
the cursor type **x**. You may preceed **x** with a number to delete that many
characters. The **d** command is more general purpose. **d** is followed by a
_movement command_ that controls the size of the deletion. To delete the current
line type **dd**. You can preceed **d** with a number like **x**, to execute a
delete command that many times.

**Text Deletion Commands**

| **Command** | **Deletes**                                                    |
|-------------|----------------------------------------------------------------|
| `x`         | Current character                                              |
| `#x`        | # of characters                                                |
| `dd`        | Current line                                                   |
| `#dd`       | # of lines                                                     |
| `dW`        | From current cursor position to beginning of next word         |
| `d$`        | From current cursor position to end of line                    |
| `d0`        | From current cursor position to beginning of line              |
| `d^`        | From current cursor position to first non-whitespace character |
| `dG`        | From current line to end of file                               |
| `d#G`       | From current line to # line of file                            |

If you make a mistake, you can undo a deletion with the **u** command.

**Note:** Real vi supports only a single level of undo. Vim supports multiple
levels of undo.

#### Cutting, Copying, and Pasting Text

The **d** command not only deletes text but it also "cuts" text. Anytime you use
the **d** command it will save that snippet of text into a paste buffer that can
later be used. To paste text use the **p** command to paste the contents
after the cursor or the **P** command to paste the contents before the cursor.

The **y** command is used to "yank" (copy) text to the paste buffer.

**Yanking Commands**

| **Command** | **Copies**                                    |
|-------------|-----------------------------------------------|
| `yy`        | Current line                                  |
| `#yy`       | Copies # of lines                             |
| `yW`        | From cursor to beginning of next word         |
| `y$`        | From cursor to end of line                    |
| `y0`        | From cursor to beginning of line              |
| `y^`        | From cursor to first non-whitespace character |
| `yG`        | From current line to end of file              |
| `y#G`       | "yank" current line to line #                 |

Just like with the **d** command anything that you "yank" into the paste buffer
with the **y** command can be pasted back into your file using either **p** or
**P**.

Feel free to practice adding, deleting, yanking and pasting text into your text
file. Remember, you can always undo with **u**.

### Search-and-Replace

In vi you can search a single line or a whole file. You can also perform text
replacements as in a _search-replace_, also known as a _substitution_.

#### Searching Within a Line

The **f** command searches a line and moves the cursor to the next instance of a
specified character. For example **fa** would move the cursor to the next
occurrence of the character **a**.  After performing a character search the
search may be repeated by typing **;**.

#### Searching the Entire File

To search for a word or phrase the **/** command is used. After typing **/**
type a string to search for and press **Enter**. This will move the cursor to
next occurrence of that string in the file. You can repeat the search forward
through the file by pressing **n**. You can perform the search backwards through
the file by pressing **N**.

Vi's search function allows for the use of Regular Expressions, but that is
outside of the scope of this tutorial. Feel free to type `:help` in command mode
to refer to vim's help docs.

#### Global Search-and-Replace

The basic syntax for searching a whole file and replacing every occurrence of a
string is:

```
:%s/search/replace/g
```

**If we break this down...**

`:` starts an _ex_ command.

`%` specifies the range of lines for the operation, in this case `%` is a
shortcut that means from the 1st line to the last line in the file (aka the
whole file).

`s` specifies the operation we're performing which in this case is a _substitution_.

`/search/replace/` specifies the _search_ text and the _replacement_ text. Those
of you who are familiar with `sed` might notice the similarity between how vi
performs substitutions and how `sed` does.

The `g` means "global" which will
replace every occurrence of the search string that's found with the replacement
string.

Vi can also ask for confirmation for every substitution if we add the
_confirmation_ command to our search-replace.

```
:%s/line/Line/gc
```
Before each substitution you will be prompted with:
```
replace with Line (y/n/a/q/l/^E/^Y)?
```
_yes, no, all, quit, last, Ctrl-e (scroll up), Ctrl-y (scroll down)_

# Resources

## Vimtutor

There's actually a tutorial built right into Vim that is highly recommended.
The above introduction is just that, an introduction.  There's quite a bit more
that you can do with vim and which is unfortunately ouside of the scope of this
article.

If you're learning vim, running `vimtutor` from your terminal or `:help tutor`
from inside of vim will open the tutorial that's builtin to the editor.
This covers much of what's in the tutorial above as well as quite a bit that
wasn't able to be covered here. There's the added benefit of being able to
practice your vim skills right inside of vim.

One suggestion is to work through the vimtutor once per day for a week or so for
about 20 minutes each time and restarting the tutor each time you complete it.
Practice and repetition is a good way to solidify your skills and commit many of
the keyboard commands and skills to memory. After a week of practice you'll be
well on your way to becoming proficient in Vim.

## Other Resources

As always there's the official help docs which ship with vim if you run `:help`
from any vim buffer.

* [Official docs](https://www.vim.org/docs.php)
* [Cheat sheet](https://vim.rtorr.com)

# Acknowledgements

This "Introduction to Vi" is largely based on the "Gentle Introduction to Vi"
that's written by William Shotts and that's available online for free download
on his [site](http://www.linuxcommand.org/tlcl.php/tlcl.php) as part of his book
on the Linux CLI. This resource is highly recommended to anyone interested in
learning the Linux CLI as well as the chapter on Vi.
