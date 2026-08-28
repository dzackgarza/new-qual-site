---
schema: qual/card@1
id: E-AMD-EYNVK4T2
kind: exercise
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
---

::: {.exercise}
Show that an $m$-cycle is an odd permutation if and only if $m$ is an even number.
:::

::: solution
**Goal:** Prove that for any $m$-cycle $\sigma \in S_n$, the sign satisfies $\operatorname{sgn}(\sigma) = (-1)^{m-1}$, and hence $\sigma$ is odd if and only if $m$ is even.

<1>1. Transposition factorization:
    *Proof:*
    <2>1. Let $\sigma = (a_1 \, a_2 \, \dots \, a_m)$ be an $m$-cycle of length $m \ge 2$.
    <2>2. We can factor $\sigma$ as a product of $m - 1$ transpositions:
        $$(a_1 \, a_2 \, \dots \, a_m) = (a_1 \, a_m)(a_1 \, a_{m-1}) \cdots (a_1 \, a_3)(a_1 \, a_2).$$
    <2>3. Direct verification of the action on each element:
        - $a_1 \mapsto a_2$,
        - $a_k \mapsto a_1 \mapsto a_{k+1}$ for all $2 \le k \le m-1$,
        - $a_m \mapsto a_1$.
        This coincides with $\sigma$.

<1>2. Sign computation:
    *Proof:*
    <2>1. The sign map $\operatorname{sgn}: S_n \to \{+1, -1\}$ is a group homomorphism.
    <2>2. The sign of every transposition is $-1$.
    <2>3. Applying $\operatorname{sgn}$ to the product of $m - 1$ transpositions:
        $$\operatorname{sgn}(\sigma) = \prod_{i=1}^{m-1} (-1) = (-1)^{m-1}.$$

<1>3. Parity equivalence:
    *Proof:*
    <2>1. $\sigma$ is an odd permutation if and only if $\operatorname{sgn}(\sigma) = -1$.
    <2>2. $(-1)^{m-1} = -1 \iff m - 1$ is an odd integer $\iff m$ is an even integer.

<1>4. Conclusion:
    An $m$-cycle is an odd permutation if and only if $m$ is even. Q.E.D.
:::
