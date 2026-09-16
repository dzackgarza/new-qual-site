---
schema: qual/card@1
id: D-JGYK4
kind: definition
title: Primary ideal
classification:
  areas:
  - algebra
  topics:
  - Primary Decomposition
  - Ideals
relations: []
review: draft
prompts:
- Show that maximal implies prime implies both radical and primary, and that neither radical nor primary implies the other.
---

::: {.definition}
Let $R$ be a commutative ring.
A proper [[D-GOFWL|ideal]] $I\subsetneq R$ is \dfn{primary} if for all $p,q\in R$ with $pq\in I$, either $p\in I$ or there exists $n\geq 1$ such that $q^n\in I$.
:::

::: {.proposition}
In a commutative ring, every maximal ideal is prime, and every prime ideal is both radical and primary.
[@AM18]
:::

::: {.example}
In $k[x,y]$ the ideal $(xy)$ is radical but not primary, since $x \cdot y \in (xy)$ while $x \notin (xy)$ and no power of $y$ lies in $(xy)$.
In $k[x]$ the ideal $(x^2)$ is primary but not radical, since $x \notin (x^2)$ and $x^2 \in (x^2)$.
:::
