---
schema: qual/card@1
id: P-S2HTH
kind: problem
title: "Let $G=S_5$, the symmetric group on 5 elements. Identify"
classification:
  areas:
  - algebra
  topics:
  - conjugacy
  - permutations
  - partitions
relations: []
review: draft
solved: true
---
:::{.problem}
Let $G=S_5$, the symmetric group on 5 elements. Identify
all conjugacy classes of elements in $G$, provide a representative from
each class, and prove that this list is complete.
:::

:::{.solution}


:::{.claim title="1"}
Conjugacy classes in $S_n$ are completely
determined by cycle type.
:::

This follows because of the result on homework 1, which says that for
any two cycles $\tau,\sigma\in S_n$, we have
$$\tau(s_1~s_2~\cdots~s_k)\tau^{-1} = (\tau(s^1)~\tau(s^2)~\cdots~\tau(s_k)).$$

In particular, this shows that the cycle type of a single cycle is
invariant under conjugation. If an element $\sigma \in S_n$ is comprised
of multiple cycles, say $\sigma = \sigma_1 \cdots \sigma_\ell$, then
$$\tau(\sigma)\tau^{-1} = \tau(\sigma_1 \cdots \sigma_\ell)\tau^{-1} 
= (\tau\sigma_1\tau^{-1})\cdots(\tau\sigma_\ell\tau^{-1}),$$

which shows that the entire cycle type is preserved under conjugation.
So each conjugacy class has exactly one cycle type, and distinct classes
have distinct cycle types, so this completely determines the conjugacy
classes.

**Claim 2:** Cycle types in $S_n$ are in bijective correspondence with
integer partitions of $n$.

This follows because any integer partition of $n$ can be used to obtain
a canonical representative of a conjugacy class of $S_n$: if
$n = a_1 + a_2 + \cdots a_n$, we simply take a cycle of length $a_1$ the
first $a_1$ integers in order, a cycle of length $a_2$ containing the
integers $a_1 + 1$ to $a_2$ in order, and so on.

Conversely, any permutation can be written as a product of disjoint
cycles, and when the cycles for fixed points are added in, every integer
between 1 and $n$ will appear, and the sum of the lengths of all cycles
must sum to $n$. Thus taking the cycle lengths yields an integer
partition of $n$.

All integer partitions of 5 are given below, along with a canonical
representative of the associated conjugacy class. $$\begin{aligned}
    5 && (1~2~3~4~5) \\
    4 + 1 && (1~2~3~4)(5) \\
    3 + 2 &&  (1~2~3)(4~5) \\
    3 + 1 + 1 && (1~2~3)(4)(5) \\
    2 + 2 + 1 && (1~2)(3~4)(5) \\
    2 + 1 + 1 + 1 && (1~2)(3)(4)(5) \\
    1 + 1 + 1 + 1 + 1 && (1)(2)(3)(4)(5) \\\end{aligned}$$ ◻
:::

