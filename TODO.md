---
title: TODO
date: 2025-08-20T11:13:30Z
modified: 2025-08-23T21:07:08Z
tags: 
  - 'todo'
  - 'gtd'
  - 'ideas'
  - 'blog'
  - 'projects'
  - 'portfolio'
---

# TODO

- [ ] Store RH subscription envvars persistently and load automatically
- [ ] Rebuild website(s) with pandoc + make. Simpler is better
- [ ] Resume as a texinfo, html, man-page, curl-enabled, all with make
    - [ ] blog post because it's neat and show off portfolio, etc
- [ ] Fix linux_system_roles.sudo bug
- Linux+
    - [ ] Need crib-notes, "cliff notes", crib-sheet, or study guide for seasoned linux admin
    - [ ] CompTIA flashcards app?
    - [ ] Exam coupon/discount code + purchase voucher?
    - [ ] Schedule exam
- [ ] Order paul's birthday present? Baofeng radio or sharpening stones?
- [ ] Belated birthday present for Chelsea?

## RHCSA

- [ ] Clean office
    - [ ] Cleanup trash
    - [ ] Sweep floor
    - [ ] Clear 2nd desk
    - [ ] Move and/or dismantle 2nd desk?
    - [ ] Put away work computer and KVM switch
    - [ ] Connect/test ethernet
    - [ ] Vacuum futon
- [X] Firewall
- [X] SELinux
- [X] Containers
- [X] Networking
  - [X] Intro
  - [X] Exercises
  - [ ] Challenge Labs
- [ ] NFS + autofs
  - [ ] Intro
  - [ ] Exercises
  - [ ] Challenge Labs
- [ ] Review
- [ ] Mock Exam
- [ ] Make USB
    - [ ] Hardware test

# Ideas

- [ ] Version control Anki decks with Git?

## Blog Ideas

- [ ] How I studied for the RHCSA
- [ ] Resume with make
- [ ] Ansible anti-patterns
    - Shelling out your secrets
    - Hardcoded secrets
    - Lineinfile instead of Template
    - Static templates instead of jinja vars
    - Testing for AWS by looking for awscli
- Ansible + CI/CD
    - [ ] Ansible + GitLab CI + Molecule for integration testing
    - [ ] Building a ubi9 Ansible executor for GitLab CI
- Committing and pushing code in GitLab CI pipeilnes.
- GitLab CI + pre-commit for validation
- How I publish my notes with git submodules and mkdocs
- IT aphorisms
- Ethical use of AI. "Do no harm", cite AI as a contributor, editor, primary author, etc. 100% human authored will become increasingly more rare and valuable as ai generated slop fills greater percentages of content. AI generated content should cite it's source, it's disingenous and ethically dubious to posit content, code, work product, etc as derived primarily or 100% by the efforts of the author rather. Alignment could pose a serious existential risk and great care should be taken in the user of ai to ensure continued alignment. This should be an inalienable minimum ethical standard.

## The real business value of AI

Rather than focusing on AI as a workforce or labor replacement, focus on training and enrichment. The current paradigm is that hours or work in == production out and production out is directly correlated with delivery of value. This is the type of thinking born out of the industrial revolution and still holds sway today in terms of implicit bias of leadership, return to office initiatives, etc...

This is oversimplifying delivery of value. This frequently goes along with measuring the wrong things... "metrics" or "key performance indicators" in corporate speak.

How do you effectively measure delivery of value? Is it _lines of code_ (LOC), is it number of commits? Is it number of pull-requests?

> What get's measured get's managed...

AI generated slop can crush these metrics, but at what cost?

In call center work there's "customer satisfaction", "contacts per hour", etc. But one of my favorite metrics that was probably a better indicator of delivery of value was "first contact resolution" (FCR). This is harder to measure because it's necessary to accurately capture what the issue is and across the various mediums which customer's seek support and determine when and by who (if at all) their issue was resolved and whether or not they had to reach out a 2nd, 3rd, or fourth time.

If bonuses are tied to contacts/hr, ticket close rates, etc. savvy tech's will game the system and hit those bonus metrics every pay-period, but at what cost to the customer? The value proposition is murky at best, or maybe customer's just never get their issues resolved and never call back, they find a different way to solve their issue or not at all.

FCR, might be one of the only metrics that matters in the context. maybe the call is 45 minutes long and just kills your contacts or close rate, but if their issue is resolved... permanently. The overall labor savings are probably greater than if they had to tie up multiple reps in multiple mediums or escalate multiple tiers. Worse if they submit a complaint or there's the very real risk if they're dissatisfied of losing their revenue forever.

Measuring what matters and is the greatest value is a hard problem to solve. I think it's a penny wise and a pound foolish to make the kind of bets on ai workforce replacement that results in layoffs.

Training the workforce on ai, integrating ai into systems where it already does things very well, and "enriching" the delivery of real business value through the strategic and tactical use of ai in the workforce is where the real long-term benefits are to be garnered.

The real tangible and lasting benefit is the augment not to replace, or to use a better word, to _enrich_ the value delivery of the work force.

Certain tribal knowledge, types of heuristic pattern recognition, and things that human's a very good.

It should be used to reduce toil, make inefficient manual or laborious processes automated or streamlined. The biggest investment is still in the people doing the work where the biggest long-term growth is to be gained.

There's also issues with alignment and replacing human's with ai can have unintended consequences. This isn't something that can be implemented by fiat of corporate policy and hope to be as successful, or worse detrimental to the bottom line. It's not a silver bullet, it's a tool. A really powerful tool but a tool nonetheless.

replacing workforce with ai only improves this quarters p & l, this shouldn't be a long-term strategy

## Book Ideas

- A book on self-hosting everything, degoogling, etc.
    - copyparty?
    - nextcloud?
    - mini servers, old laptops/old hardware, raspberry pi
    - along the lines of the original "lifehacker" book and the subsequent "lifehacker" site and /r/selfhosted, for the layperson, diy'er, most techies tend to have their own homelab
- RHCSA crib notes for seasoned admin going after the cert
- Automate the boring stuff with Bash
- Bash'isms?

### Ansible for Windows

- Windows patching
  - windows patching role
- Installing packages, MSI, EXE, etc
- Creating Scheduled tasks
- Chocolatey package management
- AD and GPO
- Windows remote connectivity
- Vagrant windows boxes
- Troubleshooting windows remote connectivity issues

### Advanced Ansible for DevOps

- Project skeletons
- Integration testing via CI/CD pipelines, Jenkins, GitLab CI, GitHub Actions
- Ansible style + best-practices
  - Modular/maintainable architecture
- Linting and syntax checking with pre-commit
- Publishing collections from roles, managing large ansible projects
  - Monorepo vs modular architecture?
- rhel-system-roles, linux-system-roles
- Managing sudoers with Ansible and linux_system_roles.sudo
- linux_system_roles
    - bootloader
    - firewalld
    - sudo
    - fapolicyd
- Simple and alternative project structure
- Dynamic cloud inventory with plugins
    - AWS
    - Azure
    - GCP
- Managing containers with ansible
- Proxmox VE?
- VMWare?
- Network devices?
- Ansible for Windows
- Ansible REPL
- ansible-doc
- ansible-inventory
- Installing + configuring Splunk
- Installing + configuring Dynatrace Oneagent
- Installing + configuring Prometheus/Grafana
- Writing collections
    - Playbooks from collections
- Writing roles
    - Returning custom facts from roles
    - Supporting multi-os
- advanced text munging and filtering
    - map
    - merge
    - filtering

### Learn Linux Sysadmin the Hard Way

- Install Arch the hard way (I use arch btw)

## Portfolio projects

- [ ] Implement linux_system_roles.fapolicyd feature request
- [ ] Implement cisagov.upgrade reboot feature
- [ ] Rewrite plus3it/spel "ansibleize" their bash scripts, or produce ansible role/collection that does this idempotently. Add RHEL for SAP support.
- [ ] The Cloud Resume Challenge

## Business ideas

RHCSA study app.

There aren't any good apps for studying for the RHCSA exams. The fact that it's a practical exam may pose certain challenges. Still though, MVP might just be curated flashcards similar to other CompTIA apps in the space, since some people derive value out of those and may be willing to pay a few bucks for it. Maybe able to reinvest any revenue into developing UI for labs on mobile.
