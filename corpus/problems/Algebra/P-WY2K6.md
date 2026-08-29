---
schema: qual/card@1
id: P-WY2K6
kind: problem
title: Lagrange's theorem
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
State and prove **Lagrange's Theorem** for finite groups: if $G$ is a finite group and $H \le G$ is a subgroup, then $|H|$ divides $|G|$ and $|G| = [G : H] \cdot |H|$.
:::

::: solution
**Goal:** Prove Lagrange's Theorem by partitioning $G$ into mutually disjoint left cosets of equal size $|H|$.

<1>1. Definition of Left Cosets and Equivalence Relation:
    *Proof:*
    <2>1. Let $G$ be a group and $H \le G$ a subgroup.
    <2>2. Define a relation $\sim_L$ on $G$ by:
        $$x \sim_L y \iff x^{-1} y \in H.$$
    <2>3. $\sim_L$ is an **equivalence relation**:
        - **Reflexive:** $x^{-1} x = e \in H \implies x \sim_L x$.
        - **Symmetric:** $x^{-1} y \in H \implies (x^{-1} y)^{-1} = y^{-1} x \in H \implies y \sim_L x$.
        - **Transitive:** If $x^{-1} y \in H$ and $y^{-1} z \in H$, then $(x^{-1} y)(y^{-1} z) = x^{-1} z \in H \implies x \sim_L z$.
    <2>4. The equivalence class containing $g \in G$ is the **left coset** of $H$:
        $$[g]_{\sim_L} = \{x \in G \mid g \sim_L x\} = \{x \in G \mid g^{-1} x \in H\} = g H = \{g h \mid h \in H\}.$$

<1>2. Partition of $G$ into Disjoint Cosets:
    *Proof:*
    <2>1. Since equivalence classes form a partition of the underlying set, $G$ is the disjoint union of distinct left cosets:
        $$G = \bigsqcup_{i=1}^k g_i H$$
        where $\{g_1, \dots, g_k\}$ is a set of distinct coset representatives, and $k = [G : H]$ is the index of $H$ in $G$.

<1>3. Bijection between $H$ and Any Coset $g H$:
    *Proof:*
    <2>1. For any fixed $g \in G$, define the map $\phi_g: H \to g H$ by $\phi_g(h) = g h$.
    <2>2. **Injective:** If $\phi_g(h_1) = \phi_g(h_2)$, then $g h_1 = g h_2$. Left cancellation gives $h_1 = h_2$.
    <2>3. **Surjective:** Any element of $g H$ has the form $g h = \phi_g(h)$ for some $h \in H$.
    <2>4. Thus $\phi_g$ is a bijection, so:
        $$|g H| = |H| \quad \text{for every } g \in G.$$

<1>4. Counting Elements and Divisibility:
    *Proof:*
    <2>1. Taking the cardinality of the disjoint union $G = \bigsqcup_{i=1}^k g_i H$:
        $$|G| = \sum_{i=1}^k |g_i H| = \sum_{i=1}^k |H| = k \cdot |H| = [G : H] \cdot |H|.$$
    <2>2. Since $k = [G : H]$ is an integer, $|H|$ divides $|G|$ and $[G : H] = |G| / |H|$.

<1>5. Conclusion:
    $|G| = [G : H] \cdot |H|$, so the order of every subgroup divides the order of the group. Q.E.D.
:::
