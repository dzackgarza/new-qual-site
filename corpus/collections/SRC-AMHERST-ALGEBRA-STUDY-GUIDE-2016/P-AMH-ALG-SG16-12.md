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
(January 1997) Suppose that $\sigma$ is a permutation in the alternating group $A_{10}$ given by
\[
\begin{pmatrix}
1&2&3&4&5&6&7&8&9&10\\
4&7&2&6&10&1&5&?&?&3
\end{pmatrix},
\]
where the images of $8$ and $9$ have been lost.
Determine the images of $8$ and $9$ under $\sigma$.
What is the order of $\sigma$?
:::

::: {.solution}
<1>1. The missing images are either
$$
\sigma(8)=8,\ \sigma(9)=9
$$
or
$$
\sigma(8)=9,\ \sigma(9)=8.
$$
::: {.proof}
The displayed values already use the images
$$
1,2,3,4,5,6,7,10.
$$
Since $\sigma$ is a permutation of $\{1,\ldots,10\}$, the two unused images are exactly $8$ and $9$.
:::

<1>2. The transposed choice $\sigma(8)=9$, $\sigma(9)=8$ is impossible.
::: {.proof}
With that choice,
$$
\sigma=(1\ 4\ 6)(2\ 7\ 5\ 10\ 3)(8\ 9).
$$
A $3$-cycle is even, a $5$-cycle is even, and the transposition $(8\ 9)$ is odd. Therefore this product is odd.

But $\sigma\in A_{10}$, so $\sigma$ must be even. Contradiction.
:::

<1>3. Therefore
$$
\boxed{\sigma(8)=8,\qquad \sigma(9)=9}.
$$
::: {.proof}
Step <1>1 gives the only two possibilities, and step <1>2 rules out the transposed one.
:::

<1>4. The disjoint-cycle decomposition is
$$
\sigma=(1\ 4\ 6)(2\ 7\ 5\ 10\ 3),
$$
so
$$
\boxed{\operatorname{ord}(\sigma)=15}.
$$
::: {.proof}
The omitted points $8$ and $9$ are fixed by step <1>3. The two displayed cycles have lengths $3$ and $5$, and they are disjoint. Therefore
$$
\operatorname{ord}(\sigma)=\operatorname{lcm}(3,5)=15.
$$
:::

<1>5. Q.E.D.
::: {.proof}
Step <1>3 determines the missing images, and step <1>4 gives the order.
:::
:::
