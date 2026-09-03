---
schema: qual/card@1
id: E-ZN7P4
kind: problem
title: Continuous images of connected sets are connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: exercise
Prove that if $f: X \to Y$ is a continuous map between topological spaces and $X$ is connected, then the image $f(X)$ is connected in $Y$.
:::

::: solution
**Goal:** Prove that the continuous image of a connected space is connected.

<1>1. Strategy: Proof by contradiction via clopen / separation decomposition:
    *Proof:*
    <2>1. Endow $Z = f(X) \subseteq Y$ with the subspace topology.
    <2>2. Suppose, for contradiction, that $f(X)$ is disconnected.
    <2>3. Then there exists a separation of $f(X)$: two non-empty, disjoint open subsets $U, V$ in the subspace topology of $f(X)$ such that:
        $$f(X) = U \cup V, \qquad U \cap V = \varnothing, \qquad U \ne \varnothing, \quad V \ne \varnothing.$$

<1>2. Pulling back the separation to $X$:
    *Proof:*
    <2>1. By definition of the subspace topology, there exist open sets $A, B \subseteq Y$ such that $U = A \cap f(X)$ and $V = B \cap f(X)$.
    <2>2. Consider the preimages $U' = f^{-1}(U) = f^{-1}(A)$ and $V' = f^{-1}(V) = f^{-1}(B)$ in $X$.
    <2>3. **$U'$ and $V'$ are open in $X$:** Because $f: X \to Y$ is continuous, the preimage of any open set in $Y$ is open in $X$. Thus $U'$ and $V'$ are open in $X$.
    <2>4. **$U'$ and $V'$ cover $X$:**
        $$U' \cup V' = f^{-1}(U) \cup f^{-1}(V) = f^{-1}(U \cup V) = f^{-1}(f(X)) = X.$$
    <2>5. **$U'$ and $V'$ are disjoint:**
        $$U' \cap V' = f^{-1}(U) \cap f^{-1}(V) = f^{-1}(U \cap V) = f^{-1}(\varnothing) = \varnothing.$$
    <2>6. **$U'$ and $V'$ are non-empty:**
        - Since $U \ne \varnothing$, choose $u \in U \subseteq f(X)$. By definition of the image, there exists $x \in X$ such that $f(x) = u \in U$, so $x \in f^{-1}(U) = U'$, hence $U' \ne \varnothing$.
        - Since $V \ne \varnothing$, choose $v \in V \subseteq f(X)$. There exists $y \in X$ such that $f(y) = v \in V$, so $y \in f^{-1}(V) = V'$, hence $V' \ne \varnothing$.

<1>3. Deriving the Contradiction:
    *Proof:*
    <2>1. $\{U', V'\}$ forms a separation of $X$ into two non-empty, disjoint open subsets whose union is $X$.
    <2>2. This contradicts the hypothesis that $X$ is connected!

<1>4. Conclusion:
    $f(X)$ cannot be disconnected; thus $f(X)$ is connected. Q.E.D.
:::
