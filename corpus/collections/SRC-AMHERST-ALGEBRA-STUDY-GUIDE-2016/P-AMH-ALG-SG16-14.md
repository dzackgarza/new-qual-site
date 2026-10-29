---
schema: qual/card@1
id: P-AMH-ALG-SG16-14
kind: problem
title: Elements of order 21 and 11 in $S_{10}$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
Recall that $S_n$ denotes the group of permutations on $n$ symbols.
(a) Find an element of $S_{10}$ of order $21$.
(b) Prove that no element of $S_{10}$ has order $11$.
:::

::: {.solution}

::: pf

::: pf-step
The permutation
$$
\boxed{\sigma=(1\ 2\ 3)(4\ 5\ 6\ 7\ 8\ 9\ 10)}
$$
has order $21$ in $S_{10}$.

::: pf-proof
The two cycles are disjoint and have lengths $3$ and $7$. Therefore
$$
\operatorname{ord}(\sigma)
=\operatorname{lcm}(3,7)
=21.
$$
:::

:::

::: pf-step
No element of $S_{10}$ has order $11$.

::: pf-proof
Suppose, for contradiction, that $\tau\in S_{10}$ has order $11$. Write $\tau$ as a product of disjoint cycles with lengths
$$
\ell_1,\ldots,\ell_r.
$$
Then
$$
11=\operatorname{ord}(\tau)
=\operatorname{lcm}(\ell_1,\ldots,\ell_r).
$$
Hence every $\ell_i$ divides $11$. Since $11$ is prime,
$$
\ell_i\in\{1,11\}
$$
for every $i$.

But an $11$-cycle requires $11$ distinct symbols, impossible in $S_{10}$. Therefore every $\ell_i=1$, so $\tau$ is the identity permutation, which has order $1$, not $11$. Contradiction.
:::

:::

:::

:::
