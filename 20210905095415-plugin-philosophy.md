---
title: Plugin Philosophy
date: 2021-09-05T09:54:00Z
tags:
---

Plugins shouldn't override too much of vim's defaults. Vimwiki for example.
Plugins should do one thing and do it well.  This was the inspiration behind why
that author created wiki.vim. Vimwiki tries to take control of things like
markdown syntax highlighting and folding. And it's just not that good at it when
it comes down to it. Vimwiki doesn't handle markdown very well. It's like the
forgotten step-child of the Vimwiki project. Vimwiki is probably really nice
using Vimwiki syntax. But who needs another syntax to learn when there's
Markdown. And Vimwiki just isn't portable anywhere else. The purpose built
vim-markdown plugin is much better at this. 

If you want _software_ running in an OS, use **emacs**. The philosophy of vim is
do to do one thing and do it well.

Resist the urge to add all kinds of plugins. Be choosy about the plugins you
add. And use plugins that are well-documented and still seem to be actively
developed. Use plugins that do one thing well. Don't add plugins to add
additional features that is available in native vim or in those plugins you
already have that do one things well.

For example, notational-fzf-vim uses FZF to find and created new articles. But
all of this can already be handled by FZF _ fzf.vim. The author of FZF wrote
fzf.vim so it's really nice. And both FZF and fzf.vim are well documented.
There's no reason to have notational-fzf-vim on top of that. And notational adds
errors or issues that are difficult to troubleshoot without good docs.

If you don't do this be willing to address the added complexity you've
introduced into your editor. If you love troubleshooting problems with your
editor rather than getting any work done, then feel free to ignore sensible
restraint.
