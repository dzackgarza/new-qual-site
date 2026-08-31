---
schema: qual/card@1
id: E-MUN-6-5
kind: exercise
title: Finiteness of Cartesian products
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
If $A \times B$ is finite, does it follow that $A$ and $B$ are finite?
:::

::: solution
**Goal:** Determine whether finiteness of $A \times B$ implies finiteness of $A$ and $B$.

<1>1. The claim is FALSE in general if one of the sets is empty.
    *Proof:*
    <2>1. Suppose $B = \emptyset$.
    <2>2. By definition of the Cartesian product, $A \times \emptyset = \emptyset$.
    <2>3. The empty set $\emptyset$ has cardinality $0$, which is finite.
    <2>4. However, $A$ can be chosen to be an arbitrary infinite set (for example, $A = \mathbb{N}$).
    <2>5. Thus $A \times B$ is finite while $A$ is infinite.

<1>2. If both $A$ and $B$ are nonempty, then BOTH $A$ and $B$ must be finite.
    *Proof:*
    <2>1. Since $B \neq \emptyset$, fix an element $b_0 \in B$.
    <2>2. Define the inclusion map $\iota: A \to A \times B$ by $\iota(a) = (a, b_0)$.
    <2>3. The map $\iota$ is injective: if $\iota(a_1) = \iota(a_2)$, then $(a_1, b_0) = (a_2, b_0)$, so $a_1 = a_2$.
    <2>4. Since $A \times B$ is finite and $\iota(A) \subseteq A \times B$, the image $\iota(A)$ is finite.
    <2>5. Since $\iota: A \to \iota(A)$ is a bijection, $A$ is finite.
    <2>6. Symmetrically, fixing $a_0 \in A$ and considering $b \mapsto (a_0, b)$ shows that $B$ is finite.

<1>3. Conclusion:
    *Proof:*
    It does not follow in general, because if one factor is empty the other may be infinite. It does follow whenever both $A$ and $B$ are nonempty.
:::
