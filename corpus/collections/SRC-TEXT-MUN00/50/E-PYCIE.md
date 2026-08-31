---
schema: qual/card@1
id: E-PYCIE
kind: exercise
title: Closed subspaces of euclidean space have dimension at most N
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Corollary.
Every closed subspace of $\mathbb{R}^N$ has topological dimension at most $N$.
:::

::: {.solution}
**Goal.** Show every closed subspace of $\RR^N$ has topological (covering) dimension $\le N$.

<1>1. $\RR^N$ has covering dimension $N$.
::: {.proof}
the standard result that $\dim \RR^N = N$ (Lebesgue covering dimension).
:::

<1>2. A subspace of a space of dimension $\le N$ has dimension $\le N$.
::: {.proof}
the covering dimension is monotone under taking subspaces (any open cover of the subspace extends to an open cover of the ambient space, and refinements restrict).
:::

<1>3. Hence every closed subspace of $\RR^N$ has dimension $\le N$.
::: {.proof}
<1>1 and <1>2.
:::

<1>4. Q.E.D.
::: {.proof}
<1>3 is the claim.
:::
:::
