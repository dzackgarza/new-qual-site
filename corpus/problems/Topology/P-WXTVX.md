---
schema: qual/card@1
id: P-WXTVX
kind: problem
title: A space is connected iff its only clopen subsets are $\emptyset$ and $X$
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $X$ be a topological space.
Prove that $X$ is **connected** if and only if the only subsets of $X$ that are both open and closed (clopen) are $\varnothing$ and $X$.
:::

::: solution
**Goal:** Prove that the absence of non-trivial clopen sets is logically equivalent to the definition of connectedness (no disconnection by two disjoint non-empty open sets).

<1>1. Definition of Connectedness:
    *Proof:*
    <2>1. A topological space $X$ is defined to be **connected** if there do not exist two non-empty, disjoint open subsets $U, V \subset X$ such that $X = U \cup V$.
    <2>2. Such a pair $(U, V)$ is called a **separation** (or disconnection) of $X$.

<1>2. Direction $(\implies)$: Connected $\implies$ only clopens are $\varnothing, X$:
    *Proof:*
    <2>1. We prove the contrapositive: suppose there exists a subset $A \subseteq X$ that is clopen, and $A \ne \varnothing$ and $A \ne X$.
    <2>2. Define $U = A$ and $V = X \setminus A$.
    <2>3. Since $A \ne \varnothing$, $U$ is non-empty.
    <2>4. Since $A \ne X$, $V = X \setminus A$ is non-empty.
    <2>5. Since $A$ is open in $X$, $U = A$ is open in $X$.
    <2>6. Since $A$ is closed in $X$, $V = X \setminus A$ is open in $X$.
    <2>7. We have $U \cap V = A \cap (X \setminus A) = \varnothing$ (no point lies both in $A$ and in its complement) and $U \cup V = A \cup (X \setminus A) = X$ (every point of $X$ lies in $A$ or in its complement).
    <2>8. Thus $\{U, V\}$ forms a separation of $X$, so $X$ is **disconnected** (not connected).
    <2>9. Therefore, if $X$ is connected, the only clopen subsets must be $\varnothing$ and $X$.

<1>3. Direction $(\impliedby)$: Only clopens are $\varnothing, X \implies$ Connected:
    *Proof:*
    <2>1. We prove the contrapositive: suppose $X$ is disconnected.
    <2>2. Then there exists a separation $\{U, V\}$ of $X$, where $U, V \subset X$ are non-empty, disjoint open sets with $X = U \cup V$.
    <2>3. Since $U \cap V = \varnothing$ and $U \cup V = X$, the complement of $U$ is:
        $$X \setminus U = V.$$
    <2>4. Since $V$ is open, its complement $U$ is **closed** in $X$.
    <2>5. Since $U$ was given to be open, $U$ is **both open and closed (clopen)** in $X$.
    <2>6. Since $U$ is non-empty and $V$ is non-empty (so $U \ne X$), $U$ is a **non-trivial clopen subset** ($U \ne \varnothing$ and $U \ne X$).
    <2>7. Therefore, if $X$ has no non-trivial clopen subsets, $X$ must be connected.

<1>4. Conclusion:
    $X$ is connected $\iff$ the only clopen subsets of $X$ are $\varnothing$ and $X$. Q.E.D.
:::
