---
schema: qual/card@1
id: E-97HXB
kind: problem
title: Retracts of contractible spaces
classification:
  areas:
  - topology
  topics:
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that a retract of a contractible space is contractible.
:::

::: solution
**Goal:** Prove that if $X$ is a contractible topological space and $A \subseteq X$ is a retract of $X$, then $A$ is contractible.

<1>1. Retraction and contractibility data:
    *Proof:*
    <2>1. Let $i: A \hookrightarrow X$ be the canonical inclusion map.
    <2>2. Since $A$ is a retract of $X$, there exists a continuous map $r: X \to A$ such that:
        $$r \circ i = \operatorname{id}_A.$$
    <2>3. Because $X$ is contractible, the identity map $\operatorname{id}_X$ is nullhomotopic: there exists a point $x_0 \in X$ and a continuous homotopy $H: X \times I \to X$ such that:
        $$H(x, 0) = x \quad \text{and} \quad H(x, 1) = x_0 \quad \text{for all } x \in X.$$

<1>2. Construction of nullhomotopy for $A$:
    Define $K: A \times I \to A$ by:
    $$K(a, t) = r(H(i(a), t)).$$
    *Proof:*
    <2>1. The map $K$ is continuous as the composition of continuous maps $r \circ H \circ (i \times \operatorname{id}_I)$.
    <2>2. At $t = 0$:
        $$K(a, 0) = r(H(i(a), 0)) = r(i(a)) = (r \circ i)(a) = a = \operatorname{id}_A(a).$$
    <2>3. At $t = 1$:
        $$K(a, 1) = r(H(i(a), 1)) = r(x_0) \in A.$$
    <2>4. Setting $a_0 = r(x_0) \in A$, $K(a, 1) = a_0$ is constant for all $a \in A$.

<1>3. Conclusion:
    $K$ is a continuous homotopy between the identity map $\operatorname{id}_A$ and the constant map $c_{a_0}: A \to A$.
    Thus $\operatorname{id}_A$ is nullhomotopic, so $A$ is contractible. Q.E.D.
:::
