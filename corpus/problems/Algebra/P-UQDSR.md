---
schema: qual/card@1
id: P-UQDSR
kind: problem
title: A $k$-cycle as a product of transpositions
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
---

::: {.problem}
Show directly that every $k$-cycle is a product of transpositions, and determine the minimum number of transpositions needed.
:::

::: {.solution}
Let $\sigma=(a_1\ a_2\ \cdots\ a_k)$ be a $k$-cycle in $S_n$. Products are composed from right to left, and the number of cycles of a permutation counts fixed points as cycles of length $1$.

::: pf

::: {.pf-step #upper}

$\sigma=(a_1\ a_k)(a_1\ a_{k-1})\cdots(a_1\ a_2)$, a product of $k-1$ transpositions.

::: pf-proof

For $1\le i<k$, the transpositions to the right of $(a_1\ a_{i+1})$ do not move $a_i$ unless $i=1$, and they send $a_1$ to $a_2$; in both cases the product sends $a_i$ to $a_{i+1}$. The point $a_k$ is moved only by the last factor $(a_1\ a_k)$, which sends it to $a_1$. Every other point is fixed.

:::

:::

::: {.pf-step #change}

Multiplying a permutation by a transposition changes its number of cycles by exactly $1$.

::: pf-proof

If the two points of the transposition lie in different cycles, the product joins those cycles; if they lie in the same cycle, the product splits it into two. The other cycles are unchanged.

:::

:::

::: {.pf-step #lower}

At least $k-1$ transpositions are needed.

::: pf-proof

The identity of $S_n$ has $n$ cycles and $\sigma$ has $n-k+1$. By step [](#change){.pf-ref}, a product of $t$ transpositions has at least $n-t$ cycles, so $\sigma$ needs $t\ge k-1$.

:::

:::

::: pf-qed

By steps [](#upper){.pf-ref} and [](#lower){.pf-ref}, the minimum number of transpositions is $\boxed{k-1}$.

:::

:::

:::
