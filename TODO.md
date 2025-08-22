---
title: TODO
date: 2025-08-20T11:13:30Z
modified: 2025-08-22T10:36:21Z
tags: ['todo', 'gtd', 'ideas', 'blog']
---

# TODO

- [ ] Store RH subscription envvars persistently and load automatically
- [ ] Rebuild website(s) with pandoc + make
- [ ] Resume as a texinfo, html, man-page, curl-enabled, all with make
    - [ ] blog post because it's neat and show off portfolio, etc
- [ ] Fix linux_system_roles.sudo bug

## RHCSA

- [ ] Firewall
- [ ] SELinux
- [X] Containers
- [ ] Networking
- [ ] NFS + autofs
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

## Book Ideas

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
