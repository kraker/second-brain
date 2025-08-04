---
title: Markdown Tutorial
date: 2021-07-30T15:53:00Z
tags:
- 'dac'
---

# Overview

**Markdown** is a lightweight markup language for creating formatted text using a
plain-text editor. It's designed to be easy to write and read in a plain-text
editor and be easily rendered into structurally valid HTML (or XHTML). Markdown
was originally created by John Bruber and Aaron Swartz as a markup language
that's appealing to humans. 

Because of it's utility Markdown is a popular markup language with broad
support. You can configure Slack to use Markdown syntax. GitHub and GitLab use
their own flavor of Markdown. Many common CMS and web-development frameworks
include support or plugins for rendering Markdown. Notable examples include
Jekyll and Hugo, static site generators. 

* [Official docs](https://daringfireball.net/projects/markdown/)

# Basics

In order to get started writing in Markdown you need a text editor that supports
syntax highlighting. Many plain-text editors include native support for Markdown
syntax highlighting. Common editors that include support for `*.md` which you 
might use are Vim, Emacs, Vscode, Sublime, Notepad++ to name a few. Install your
favorite text editor and create a file with the `*.md` extension to start
writing in Markdown.

## Headings

Headings are created with the use of `#` characters. To create a heading of
levels 1-6 prefix the corresponding number of `#` characters to the beginning of
the _header_.

```
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

If you're familiar with HTML markup, these render to header elements 
_<h1>, <h2>, <h3> ..._ etc. 

## Bold & Italic

Bold and italics (different degrees of _emphasis_) can be denoted by wrapping a
string of text in either one or two asterisks `*` or underscores `_`. For
example: 

```
*Italicized*
_Italicized_

**Bold**
__Bold__
```

## Blockquote

Much like plain-text email, you can create a blockquote with the right carrot
`>`.

```
> Blockquote
```

## Lists

### Ordered lists

Ordered lists are just a numbered list.

```
1. First item
2. Second item
3. Third item
```

### Unordered lists

Unordered lists are denoted by either a `*`, `+` or `-`. This author prefers `*`
but use what you prefer, just try to be consistent.  It's considered bad style
to mix it up too much. 

```
- First item
- Second item
- Third item

+ First item
+ Second item
+ Third item

* First item
* Second item
* Third item
```

### Nested lists

You can create lists within lists. It's possible to mix ordered and unordered
lists this way too. 

```
1. First item
	* Unordered sub-item 1
	* Unordered sub-item 2
2. Second item
	1. Ordered sub-item 1
	2. Ordered sub-item 2

* First item
	1. Ordered sub-item 1
	2. Ordered sub-item 2
* Second item
	+ Unordered sub-item 
	+ Unordered sub-item
```

## Code

You can denote inline code with '`' 

```
`inline code`
```

And you can denote code blocks with '```'

```
```
Some block of 
Code goes here
```
```

## Horizontal line

Horizontal lines are denoted with `---`

```
Text here
---
Other text
```

## Links

Links (or _anchors) can be created like this:

```
[link](http://www.example.com)
```

## Images

Images can be denoted like so:

```
![alt text](image.jpg)
```
_Often the image file is included in the same directory as the *.md file_

# See also

* [Official specifications](https://daringfireball.net/projects/markdown/)
* [Markdown guide](https://www.markdownguide.org/getting-started/)
* [Cheat sheet](https://www.markdownguide.org/cheat-sheet/)
