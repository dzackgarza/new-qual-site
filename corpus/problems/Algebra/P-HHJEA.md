---
schema: qual/card@1
id: P-HHJEA
kind: problem
title: Groups of order $p^n$ are solvable, and groups of order $p^r q^s$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Solvable Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}

Can you show that all groups of order $p^n$ for $p$ prime are solvable?
Do you know how to do this for groups of order $p^r q^s$?

:::

::: {.solution}

::: pf

::: pf-step

Every finite $p$-group is solvable.

::: pf-proof

We argue by induction on $\abs{G}$. The trivial group is solvable. Let $G$ be a nontrivial finite $p$-group. Its center $Z(G)$ is nontrivial and abelian, hence solvable. The quotient $G/Z(G)$ is a $p$-group of order less than $\abs{G}$, so it is solvable by induction. An extension of a solvable group by a solvable group is solvable, so $G$ is solvable.

:::

:::

::: pf-step

Every finite group of order $p^r q^s$ with $p,q$ prime is solvable.

::: pf-proof

This is Burnside's $p^a q^b$ theorem, whose classical proof uses character theory.

:::

:::

:::

:::
