---
schema: qual/card@1
id: PR-TAPZF
kind: proposition
title: One-step submodule test
classification:
  areas:
  - algebra
  topics:
  - Modules
relations: []
review: draft
---

::: {.proposition}
Let $R$ be a ring and $M$ an $R$-module.
A subset $N\subseteq M$ is an $R$-submodule if and only if $N$ is nonempty and $rx+y\in N$ for all $r\in R$ and $x, y \in N$.
:::

::: {.proof}
A submodule contains $0$ and is closed under addition and scalar multiplication, so it satisfies the condition.
Conversely, choose $x\in N$; taking $r=-1$ and $y=x$ gives $0\in N$.
Taking $y=0$ gives $rx\in N$ for all $r\in R$ and $x\in N$, in particular $-x\in N$, and taking $r=1$ gives $x+y\in N$.
Hence $N$ is an additive subgroup of $M$ closed under scalar multiplication.
:::
