---
schema: qual/card@1
id: P-SWIZT
kind: problem
title: When conjugacy classes of $S_n$ split in $A_n$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Permutations
relations: []
review: draft
---

::: {.problem}
When does an $S_n$-conjugacy class contained in $A_n$ split into two $A_n$-conjugacy classes?
:::

::: {.solution}

Let $\sigma\in A_n$, with cycle type taken to include fixed points as $1$-cycles.

::: pf

::: {.pf-step #criterion}

The $S_n$-class of $\sigma$ splits into two $A_n$-classes if and only if $C_{S_n}(\sigma)\subseteq A_n$.

::: pf-proof

By orbit--stabilizer, the $S_n$-class has $[S_n:C_{S_n}(\sigma)]$ elements and the $A_n$-class has $[A_n:C_{A_n}(\sigma)]$ elements, where $C_{A_n}(\sigma)=C_{S_n}(\sigma)\cap A_n$. Since $A_n\normal S_n$ has index $2$, the $S_n$-class is a union of $A_n$-classes permuted transitively by $S_n/A_n$, so it is one class or two of equal size. The ratio of the two class sizes is $2/[C_{S_n}(\sigma):C_{A_n}(\sigma)]$, which is $2$ exactly when $C_{S_n}(\sigma)\subseteq A_n$.

:::

:::

::: {.pf-step #no-split}

If the cycle type of $\sigma$ has an even part or a repeated odd part, then $C_{S_n}(\sigma)\not\subseteq A_n$.

::: pf-proof

An even-length cycle of $\sigma$ commutes with $\sigma$ and is an odd permutation. If $(a_1\ \cdots\ a_k)$ and $(b_1\ \cdots\ b_k)$ are two cycles of $\sigma$ with $k$ odd, the permutation $(a_1\ b_1)(a_2\ b_2)\cdots(a_k\ b_k)$ commutes with $\sigma$ and is a product of $k$ transpositions, hence odd.

:::

:::

::: {.pf-step #split}

If the cycle type of $\sigma$ consists of distinct odd parts, then $C_{S_n}(\sigma)\subseteq A_n$.

::: pf-proof

An element $\tau\in C_{S_n}(\sigma)$ maps each cycle of $\sigma$ to a cycle of $\sigma$ of the same length, so with distinct lengths it preserves the support of each cycle. On the support of a $k$-cycle $c$, $\tau$ commutes with $c$, so it is a power of $c$, because the centralizer of a $k$-cycle in the symmetric group on its support is $\langle c\rangle$. Each power of an odd-length cycle is even, so $\tau$ is even.

:::

:::

::: pf-qed

By steps [](#criterion){.pf-ref}, [](#no-split){.pf-ref}, and [](#split){.pf-ref}, the class splits exactly when its cycle type consists of $\boxed{\text{distinct odd parts}}$.

:::

:::

:::
