---
schema: qual/card@1
id: P-JWPJ5
kind: problem
title: Number of irreducible representations of $S_n$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Partitions
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
(a) How many non-isomorphic irreducible complex representations does the symmetric group $S_n$ have?

(b) What classical function in mathematics does this number equal, and how are the irreducible representations explicitly indexed?
:::

::: {.solution}

::: pf

::: {.pf-step #classes}

The conjugacy classes of $S_n$ are indexed by the partitions $\lambda\vdash n$.

::: pf-proof

Two permutations are conjugate exactly when they have the same cycle type, and the cycle lengths of a permutation, in decreasing order, form a partition of $n$; every partition occurs.

:::

:::

::: pf-step

(a) $S_n$ has $\boxed{p(n)}$ irreducible complex representations up to isomorphism.

::: pf-proof

For a finite group, the number of isomorphism classes of irreducible complex representations equals the number of conjugacy classes. Apply step [](#classes){.pf-ref}.

:::

:::

::: pf-step

(b) The number is the partition function $p(n)$, and the irreducible representations are the Specht modules $S^\lambda$, one for each $\lambda\vdash n$.

::: pf-proof

This is the classification of irreducible representations of $S_n$ by Specht modules. Their dimensions are given by the hook-length formula
$$
\dim S^\lambda=\frac{n!}{\prod_{u\in\lambda}h(u)}.
$$

:::

:::

:::

:::
