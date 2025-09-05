---
title: Terraform Associate
date: 2025-09-04T19:43:08Z
modified: 2025-09-05T15:14:16Z
tags:
  - 'iac'
  - 'devops'
---

# Terraform Associate

Terraform Associate (003) Exam

* [Exam Content List - Terraform Associate (003) \| Terraform \| HashiCorp Developer](https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-review-003)
* [Learning Path - Terraform Associate (003) \| Terraform \| HashiCorp Developer](https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-study-003)
* [Sample Questions - Terraform Associate (003) \| Terraform \| HashiCorp Developer](https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-questions)

## Notes

[Graphviz](https://graphviz.org/) can be used to visualize the terraform dependency graph.

```bash
i❯ terraform graph
digraph G {
  rankdir = "RL";
  node [shape = rect, fontname = "sans-serif"];
  "aws_instance.example" [label="aws_instance.example"];
  "aws_security_group.instance" [label="aws_security_group.instance"];
  "aws_instance.example" -> "aws_security_group.instance";
}
```

Output is in a graph description language called DOT.

## Review

What are the 4 core values of the DevOps movement?
* culture
* automation
* measurement
* sharing
Abbv. _CAMS_

How do I print a dependency graph with terraform?

```bash
terraform graph
```
