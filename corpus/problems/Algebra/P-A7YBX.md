---
schema: qual/card@1
id: P-A7YBX
kind: problem
title: Every simple $R$-module is cyclic
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Semisimplicity
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
We want to show that every simple $R\dash$module $M$ is cyclic, i.e. if the only ideals of $M$ are $(0)$ and $M$ itself, that $M = \generators{m}$ for some element $m\in M$.

Towards a contradiction, let $M$ be a simple $R\dash$module and suppose $M$ is not cyclic, so $M\neq \generators{m}$ for any $m\in M$.
But then let $a\in M$ be an arbitrary nontrivial element; then $(a)$ is a non-empty ideal (since it contains $a$), so $(a) \neq 0$.
Since $M$ is simple, we must have $(a) = M$, a contradiction.
:::

::: {.solution}
Let $R$ be a ring with identity. Recall that an $R$-module $M$ is \dfn{simple} if $M\neq0$ and its only submodules are $0$ and $M$.

<1>1. For every $0\neq m\in M$, $M=Rm$.

::: {.proof}
$Rm$ is a submodule of $M$, and $m=1\cdot m\in Rm$, so $Rm\neq0$.
By simplicity, $Rm=M$.
:::

<1>2. For every $0\neq m\in M$, $M\cong R/\operatorname{ann}_R(m)$, and $\operatorname{ann}_R(m)$ is a maximal left ideal.

::: {.proof}
The map $R\to M$, $r\mapsto rm$, is $R$-linear, surjective by step <1>1, and has kernel $\operatorname{ann}_R(m)$.
Submodules of $R/\operatorname{ann}_R(m)$ correspond to left ideals of $R$ containing $\operatorname{ann}_R(m)$, and $M$ has exactly two submodules, so $\operatorname{ann}_R(m)$ is maximal.
:::

<1>3. Q.E.D.

::: {.proof}
A simple module is nonzero, so it has some $m\neq0$, and $M=Rm$ is cyclic by step <1>1.
:::
:::
