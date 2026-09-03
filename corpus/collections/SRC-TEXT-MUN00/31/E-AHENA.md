---
schema: qual/card@1
id: E-AHENA
kind: problem
title: Closed continuous surjections preserve normality
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $p: X \to Y$ be a closed continuous surjective map.
Show that if $X$ is normal, then so is $Y$.
[Hint: If $U$ is an open set containing $p^{-1}(\ts{y})$, show there is a neighborhood $W$ of $y$ such that $p^{-1}(W) \subset U$.]
:::

::: solution
**Goal:** Prove that if $X$ is a normal space and $p: X \to Y$ is a closed continuous surjection, then $Y$ is a normal space.

<1>1. $T_1$ separation axiom on $Y$:
    *Proof:*
    <2>1. For any $y \in Y$, the singleton $\{y\} \subset Y$ is closed:
        - Since $X$ is $T_1$ (normal implies $T_1$), and $p$ is continuous, the fiber $p^{-1}(\{y\})$ is closed in $X$.
        - Because $p$ is a closed map and $p$ is surjective, the image $p(p^{-1}(\{y\})) = \{y\}$ is closed in $Y$.
    <2>2. Hence $Y$ satisfies the $T_1$ axiom.

<1>2. Pushing open saturated neighborhoods down via closed maps:
    *Proof:*
    <2>1. For any open set $U \subseteq X$, define the saturated open set:
        $$W_U = Y \setminus p(X \setminus U).$$
    <2>2. Since $X \setminus U$ is closed in $X$ and $p$ is a closed map, $p(X \setminus U)$ is closed in $Y$.
    <2>3. Therefore, $W_U$ is an open subset of $Y$.
    <2>4. For any $y \in Y$, $y \in W_U \iff y \notin p(X \setminus U) \iff p^{-1}(\{y\}) \subseteq U$.
    <2>5. Thus $p^{-1}(W_U) \subseteq U$.

<1>3. Separation of disjoint closed sets in $Y$:
    *Proof:*
    <2>1. Let $A$ and $B$ be disjoint closed subsets of $Y$.
    <2>2. By continuity of $p$, the preimages $p^{-1}(A)$ and $p^{-1}(B)$ are closed subsets of $X$.
    <2>3. Since $A \cap B = \varnothing$, $p^{-1}(A) \cap p^{-1}(B) = p^{-1}(A \cap B) = \varnothing$.
    <2>4. Since $X$ is normal, there exist disjoint open sets $U, V \subset X$ such that:
        $$p^{-1}(A) \subseteq U \quad \text{and} \quad p^{-1}(B) \subseteq V.$$
    <2>5. Applying the construction from <1>2, let $W_U = Y \setminus p(X \setminus U)$ and $W_V = Y \setminus p(X \setminus V)$.
    <2>6. Both $W_U$ and $W_V$ are open in $Y$.
    <2>7. For any $a \in A$, $p^{-1}(\{a\}) \subseteq p^{-1}(A) \subseteq U$, so $a \in W_U$; thus $A \subseteq W_U$.
    <2>8. Symmetrically, $B \subseteq W_V$.
    <2>9. **Disjointness:** $p^{-1}(W_U \cap W_V) = p^{-1}(W_U) \cap p^{-1}(W_V) \subseteq U \cap V = \varnothing$.
    <2>10. Since $p$ is surjective, the empty preimage implies $W_U \cap W_V = \varnothing$.

<1>4. Conclusion:
    $A$ and $B$ are separated by disjoint open sets $W_U$ and $W_V$, so $Y$ is normal. Q.E.D.
:::
