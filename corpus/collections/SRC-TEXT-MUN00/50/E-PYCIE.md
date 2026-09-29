---
schema: qual/card@1
id: E-PYCIE
kind: problem
title: Closed subspaces of $\RR^N$ have dimension at most $N$
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

::: pf

::: {.pf-step #s1}

$\RR^N$ has covering dimension $N$.

::: pf-proof

This is the standard computation of the Lebesgue covering dimension of $\RR^N$.

:::

:::

::: {.pf-step #s2}

A closed subspace $A$ of a space $X$ with $\dim X \le N$ has $\dim A \le N$.

::: pf-proof

Let $\mathcal{U}$ be an open cover of $A$. Each $U \in \mathcal{U}$ is $A \cap U'$ for some open $U' \subseteq X$. The sets $U'$ together with $X \setminus A$ form an open cover of $X$, which has an open refinement $\mathcal{V}$ of order at most $N + 1$. The sets $V \cap A$, $V \in \mathcal{V}$, form an open cover of $A$ of order at most $N + 1$; each $V$ meeting $A$ lies in some $U'$, since $X \setminus A$ misses $A$, so $V \cap A$ lies in the corresponding $U$.

:::

:::

::: pf-qed

Apply step [](#s2){.pf-ref} to $X = \RR^N$, using step [](#s1){.pf-ref}.

:::

:::

:::
