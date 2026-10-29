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

The first factor applied, $(a_1\ a_2)$, sends $a_1$ to $a_2$, and no later factor moves $a_2$. For $2\le i\le k$, the first factor that moves $a_i$ is $(a_1\ a_i)$, which sends it to $a_1$; the next factor, $(a_1\ a_{i+1})$ when $i<k$, sends $a_1$ to $a_{i+1}$, and no later factor moves $a_{i+1}$. So the product sends $a_i\mapsto a_{i+1}$ for $i<k$ and $a_k\mapsto a_1$. Every other point is fixed.

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
