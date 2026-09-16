---
schema: qual/card@1
id: FD-W3MQW
kind: definition
title: Stabilizer of a point
prompts:
- What is the stabilizer of a point under a group action?
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Orbit-Stabilizer
  - Subgroups
relations: []
review: draft
---

::: {.definition}
Let a group $G$ with identity $e$ act on a set $X$, and let $x\in X$.
The \dfn{stabilizer} of $x$ is the subgroup
$$
G_x \coloneqq \theset{g\in G \st g\cdot x = x}
$$
of $G$.
:::

::: {.remark}
$G_x$ is a [[D-IQ4OX|subgroup]]: $e\cdot x=x$; if $g,h\in G_x$, then $(gh)\cdot x=g\cdot(h\cdot x)=x$; and if $g\in G_x$, then $g^{-1}\cdot x=g^{-1}\cdot(g\cdot x)=x$.
:::
