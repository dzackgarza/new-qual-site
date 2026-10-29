---
schema: qual/card@1
id: P-S2HTH
kind: problem
title: Conjugacy classes in $S_5$ by cycle type, corresponding to partitions of $5$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Permutations
  - Partitions
relations: []
review: draft
---

::: {.problem}
Let $G=S_5$, the symmetric group on 5 elements. Identify
all conjugacy classes of elements in $G$, provide a representative from
each class, and prove that this list is complete.
:::

::: {.solution}

The cycle type of $\sigma\in S_n$ is the multiset of lengths of the cycles in its disjoint cycle decomposition, fixed points counted as $1$-cycles.

::: pf

::: {.pf-step #conj-formula}

For $\tau\in S_n$ and a cycle $(s_1\ s_2\ \cdots\ s_k)$,
$$
\tau(s_1\ s_2\ \cdots\ s_k)\tau^{-1}=(\tau(s_1)\ \tau(s_2)\ \cdots\ \tau(s_k)).
$$

::: pf-proof

The left side sends $\tau(s_i)$ to $\tau(s_{i+1})$, indices mod $k$, and fixes every point not of the form $\tau(s_i)$, as the right side does.

:::

:::

::: {.pf-step #classes}

Two elements of $S_n$ are conjugate if and only if they have the same cycle type.

::: pf-proof

If $\sigma=\sigma_1\cdots\sigma_\ell$ is a product of disjoint cycles, then $\tau\sigma\tau^{-1}=(\tau\sigma_1\tau^{-1})\cdots(\tau\sigma_\ell\tau^{-1})$, and by step [](#conj-formula){.pf-ref} the factors are disjoint cycles of the same lengths. So conjugate elements have the same cycle type. Conversely, if $\sigma$ and $\sigma'$ have the same cycle type, write both as products of disjoint cycles, fixed points included, with cycles of equal length aligned; the permutation $\tau$ sending each entry of $\sigma$ to the entry of $\sigma'$ in the same position satisfies $\tau\sigma\tau^{-1}=\sigma'$ by step [](#conj-formula){.pf-ref}.

:::

:::

::: {.pf-step #partitions}

Cycle types in $S_n$ are in bijection with partitions of $n$.

::: pf-proof

The cycle lengths of $\sigma$, fixed points included, sum to $n$, so they form a partition of $n$. Conversely, a partition $n=a_1+\cdots+a_r$ is the cycle type of the permutation whose cycles are $(1\ \cdots\ a_1)$, $(a_1+1\ \cdots\ a_1+a_2)$, and so on through consecutive blocks of integers.

:::

:::

::: pf-qed

By steps [](#classes){.pf-ref} and [](#partitions){.pf-ref}, the conjugacy classes of $S_5$ correspond to the seven partitions of $5$, which gives the complete list:
$$
\begin{aligned}
5 &\quad (1\ 2\ 3\ 4\ 5)\\
4+1 &\quad (1\ 2\ 3\ 4)\\
3+2 &\quad (1\ 2\ 3)(4\ 5)\\
3+1+1 &\quad (1\ 2\ 3)\\
2+2+1 &\quad (1\ 2)(3\ 4)\\
2+1+1+1 &\quad (1\ 2)\\
1+1+1+1+1 &\quad \operatorname{id}
\end{aligned}
$$

:::

:::

:::
