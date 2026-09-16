---
schema: qual/card@1
id: FF-UYMWY
kind: fact
title: One-step submodule test
prompts:
- What is the one-step submodule test?
classification:
  areas:
  - algebra
  topics:
  - Modules
relations: []
review: draft
---

::: {.fact}
Let $R$ be a ring, let $M$ be a left $R$-module, and let $N\subseteq M$ be a nonempty subset.
If $rm+n\in N$ for all $r\in R$ and $m,n\in N$, then $N$ is a submodule of $M$.
:::

::: {.proof}
Choose $n\in N$; then $0=(-1)n+n\in N$.
For $r\in R$ and $m\in N$, $rm=rm+0\in N$; in particular $-m=(-1)m\in N$.
For $m,n\in N$, $m+n=1\cdot m+n\in N$.
So $N$ is an additive subgroup closed under scalar multiplication.
:::
