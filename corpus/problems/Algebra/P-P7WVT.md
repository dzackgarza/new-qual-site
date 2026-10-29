---
schema: qual/card@1
id: P-P7WVT
kind: problem
title: $I$ is a maximal ideal iff $R/I$ is a field
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source leaves R and I undeclared; the statement declares R as a commutative ring with identity and I as an ideal of R.
---

::: {.problem}
Let $R$ be a commutative ring with identity and $I$ an ideal of $R$. Show that $I$ is maximal iff $R/I$ is a field.
:::

::: {.solution}

::: pf

::: {.pf-step #correspondence}

$I$ is maximal if and only if $R/I\neq0$ and the only ideals of $R/I$ are $0$ and $R/I$.

::: pf-proof

By the correspondence theorem, $J\mapsto J/I$ is an inclusion-preserving bijection from ideals of $R$ containing $I$ to ideals of $R/I$. Maximality of $I$ says that $I\neq R$ and the only such $J$ are $I$ and $R$.

:::

:::

::: {.pf-step #field}

A commutative ring $S$ with identity is a field if and only if $S\neq0$ and its only ideals are $0$ and $S$.

::: pf-proof

If $S$ is a field and $J\neq0$ is an ideal, then $J$ contains a unit, so $J=S$. Conversely, if $0\neq a\in S$, then $(a)\neq0$, so $(a)=S$ and $ab=1$ for some $b\in S$.

:::

:::

::: pf-step

$I$ is maximal if and only if $R/I$ is a field.

::: pf-proof

Apply step [](#field){.pf-ref} to $S=R/I$ and compare with step [](#correspondence){.pf-ref}.

:::

:::

:::

:::
