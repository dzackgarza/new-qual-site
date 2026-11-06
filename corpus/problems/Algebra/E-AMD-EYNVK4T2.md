---
schema: qual/card@1
id: E-AMD-EYNVK4T2
kind: problem
title: An $m$-cycle is odd iff $m$ is even
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    standard exercise, no repair needed), and the existing prose solution against
    a fresh re-derivation: the factorization of an m-cycle into the m-1
    transpositions (a_1 a_j) is verified symbol by symbol under the
    right-to-left convention, and the sign of a product of m-1 transpositions is
    (-1)^{m-1}. The prose left the factorization unchecked, which is the only
    substantive gap; the structured proof verifies it on a_1, on a_j for
    2 <= j <= m-1, and on a_m. The m = 1 case (identity, even, and 1 is odd) is
    covered explicitly in the last step, with the empty product of sign 1. No
    source solution is retained for this card, so no source comparison was made.
    What was not checked: any printed source.
---

::: {.exercise}
Show that an $m$-cycle is an odd permutation if and only if $m$ is an even number.
:::

::: {.solution}
Let $m\geq1$ and let $\sigma=(a_1\ a_2\ \cdots\ a_m)$ be an $m$-cycle on distinct symbols $a_1,\ldots,a_m$; transpositions compose right to left, and $\operatorname{sgn}$ is the sign homomorphism $S_n\to\{\pm1\}$, which sends every transposition to $-1$.

::: pf

::: {.pf-step #factorization}
$\sigma=(a_1\ a_m)(a_1\ a_{m-1})\cdots(a_1\ a_2)$, a product of exactly $m-1$ transpositions.

::: pf-proof
Write $\tau=(a_1\ a_m)(a_1\ a_{m-1})\cdots(a_1\ a_2)$ and compare $\tau$ with $\sigma$ on each of the symbols involved; compositions are applied from the right.

For $a_1$: the rightmost factor $(a_1\ a_2)$ sends $a_1\mapsto a_2$, and every other factor $(a_1\ a_j)$ with $j\geq3$ fixes $a_2$, so $\tau(a_1)=a_2=\sigma(a_1)$.

For $a_j$ with $2\leq j\leq m-1$: the factors to the right of $(a_1\ a_j)$ involve only $a_1$ and symbols $a_i$ with $i<j$, so they fix $a_j$; the factor $(a_1\ a_j)$ sends $a_j\mapsto a_1$; the factor immediately to its left is $(a_1\ a_{j+1})$, which sends $a_1\mapsto a_{j+1}$; every factor further left involves $a_1$ and some $a_i$ with $i>j+1$, and fixes $a_{j+1}$. Hence $\tau(a_j)=a_{j+1}=\sigma(a_j)$.

For $a_m$: every factor except the leftmost $(a_1\ a_m)$ fixes $a_m$, and the leftmost sends $a_m\mapsto a_1$, so $\tau(a_m)=a_1=\sigma(a_m)$.

Every other symbol is fixed by both sides. Hence $\tau=\sigma$, and the product has one factor for each $j$ with $2\leq j\leq m$, that is $m-1$ factors.
:::

:::

::: {.pf-step #sign}
$\operatorname{sgn}(\sigma)=(-1)^{m-1}$.

::: pf-proof
The sign is a homomorphism, so the sign of a product is the product of the signs; by step [](#factorization){.pf-ref} $\sigma$ is a product of $m-1$ transpositions, and each transposition has sign $-1$. Hence $\operatorname{sgn}(\sigma)=(-1)^{m-1}$.
:::

:::

::: {.pf-step #parity}
$\sigma$ is odd if and only if $m$ is even.

::: pf-proof
A permutation is odd exactly when its sign is $-1$. By step [](#sign){.pf-ref} that happens exactly when $(-1)^{m-1}=-1$, that is exactly when $m-1$ is odd, which is equivalent to $m$ being even.
:::

:::

::: {.pf-step}
An $m$-cycle is an odd permutation if and only if $m$ is an even number.

::: pf-proof
Step [](#parity){.pf-ref} is the statement for $m\geq2$, where the cycle is the one described in the notation above. For $m=1$ the $1$-cycle is the identity, an even permutation, and $1$ is odd, so the equivalence holds there as well; the factorization of step [](#factorization){.pf-ref} is then the empty product, of sign $(-1)^0=1$.
:::

:::

:::
:::
