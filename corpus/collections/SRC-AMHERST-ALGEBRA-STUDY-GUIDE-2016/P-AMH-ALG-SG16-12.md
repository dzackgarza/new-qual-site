---
schema: qual/card@1
id: P-AMH-ALG-SG16-12
kind: problem
title: Recovering a lost permutation in $A_{10}$ and its order
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
Suppose that $\sigma$ is a permutation in the alternating group $A_{10}$ given by
$$
\begin{pmatrix}
1&2&3&4&5&6&7&8&9&10\\
4&7&2&6&10&1&5&?&?&3
\end{pmatrix},
$$
where the images of $8$ and $9$ have been lost.
Determine the images of $8$ and $9$ under $\sigma$.
What is the order of $\sigma$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
The missing images are either
$$
\sigma(8)=8,\ \sigma(9)=9
$$
or
$$
\sigma(8)=9,\ \sigma(9)=8.
$$

::: pf-proof
The displayed values already use the images
$$
1,2,3,4,5,6,7,10.
$$
Since $\sigma$ is a permutation of $\{1,\ldots,10\}$, the two unused images are exactly $8$ and $9$.
:::

:::

::: {.pf-step #s1-2}
The transposed choice $\sigma(8)=9$, $\sigma(9)=8$ is impossible.

::: pf-proof
With that choice,
$$
\sigma=(1\ 4\ 6)(2\ 7\ 5\ 10\ 3)(8\ 9).
$$
A $3$-cycle is even, a $5$-cycle is even, and the transposition $(8\ 9)$ is odd. Therefore this product is odd.

But $\sigma\in A_{10}$, so $\sigma$ must be even. Contradiction.
:::

:::

::: {.pf-step #s1-3}
Therefore
$$
\boxed{\sigma(8)=8,\qquad \sigma(9)=9}.
$$

::: pf-proof
Step [](#s1-1){.pf-ref} gives the only two possibilities, and step [](#s1-2){.pf-ref} rules out the transposed one.
:::

:::

::: pf-step
The disjoint-cycle decomposition is
$$
\sigma=(1\ 4\ 6)(2\ 7\ 5\ 10\ 3),
$$
so
$$
\boxed{\operatorname{ord}(\sigma)=15}.
$$

::: pf-proof
The omitted points $8$ and $9$ are fixed by step [](#s1-3){.pf-ref}. The two displayed cycles have lengths $3$ and $5$, and they are disjoint. Therefore
$$
\operatorname{ord}(\sigma)=\operatorname{lcm}(3,5)=15.
$$
:::

:::

:::

:::
