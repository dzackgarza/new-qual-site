---
schema: qual/card@1
id: D-MVNSV
kind: definition
title: Basis of a module
classification:
  areas:
  - topology
  topics:
  - Modules
  - Bases
relations:
- kind: variant-of
  target: D-I7D56
review: draft
---

::: {.definition}
Let $R$ be a ring and $M$ a left [[D-NQZUY|$R$-module]].
A subset $B\subseteq M$ is a \dfn{basis} of $M$ if it is a linearly independent generating set:

- every $m\in M$ is a finite sum $m=r_1b_1+\cdots+r_kb_k$ with $k\geq0$, $r_i\in R$, and $b_i\in B$; and

- whenever $r_1b_1+\cdots+r_kb_k=0$ with $r_i\in R$ and $b_1,\ldots,b_k\in B$ pairwise distinct, $r_1=\cdots=r_k=0$.
:::
