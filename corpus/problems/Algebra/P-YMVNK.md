---
schema: qual/card@1
id: P-YMVNK
kind: problem
title: Stabilizer subgroups of two points in a $G$-set are conjugate
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Conjugacy
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $X$ be a $G$-set with group action $G \times X \to X$.
(1) Prove that if $x_1, x_2 \in X$ belong to the same $G$-orbit ($x_2 = g \cdot x_1$ for some $g \in G$), then their stabilizer subgroups $\operatorname{Stab}_G(x_1)$ and $\operatorname{Stab}_G(x_2)$ are **conjugate** in $G$:
$$\operatorname{Stab}_G(g \cdot x_1) = g \operatorname{Stab}_G(x_1) g^{-1}.$$
(2) Note that if $x_1, x_2$ lie in different orbits, their stabilizers need not be conjugate.
:::

::: solution
**Goal:** Prove that translating a point by a group element conjugates its stabilizer subgroup by that element.

<1>1. Setting and Definitions:
    *Proof:*
    <2>1. Let $G$ act on the set $X$.
    <2>2. For any point $x \in X$, its stabilizer subgroup is defined by:
        $$\operatorname{Stab}_G(x) \coloneqq \{ h \in G \mid h \cdot x = x \}.$$
    <2>3. Let $x_1 \in X$ and let $x_2 = g \cdot x_1$ for some $g \in G$.

<1>2. Proof of Conjugacy $\operatorname{Stab}_G(x_2) = g \operatorname{Stab}_G(x_1) g^{-1}$:
    *Proof:*
    <2>1. Let $h \in G$. We establish a chain of logical equivalences:
        $$h \in \operatorname{Stab}_G(x_2) \iff h \cdot x_2 = x_2.$$
    <2>2. Substituting $x_2 = g \cdot x_1$:
        $$h \cdot (g \cdot x_1) = g \cdot x_1.$$
    <2>3. Using the group action axiom $(h g) \cdot x_1 = h \cdot (g \cdot x_1)$:
        $$(h g) \cdot x_1 = g \cdot x_1.$$
    <2>4. Acting on both sides by the group element $g^{-1}$:
        $$g^{-1} \cdot ((h g) \cdot x_1) = g^{-1} \cdot (g \cdot x_1) \iff (g^{-1} h g) \cdot x_1 = (g^{-1} g) \cdot x_1 = e \cdot x_1 = x_1.$$
    <2>5. By definition of the stabilizer of $x_1$:
        $$(g^{-1} h g) \cdot x_1 = x_1 \iff g^{-1} h g \in \operatorname{Stab}_G(x_1).$$
    <2>6. Conjugating by $g$:
        $$g^{-1} h g \in \operatorname{Stab}_G(x_1) \iff h \in g \operatorname{Stab}_G(x_1) g^{-1}.$$

<1>3. Conclusion for Transitive Actions / Orbits:
    *Proof:*
    <2>1. Since $h \in \operatorname{Stab}_G(x_2) \iff h \in g \operatorname{Stab}_G(x_1) g^{-1}$, we have the exact set equality:
        $$\operatorname{Stab}_G(x_2) = g \operatorname{Stab}_G(x_1) g^{-1}.$$
    <2>2. Thus, the stabilizer subgroups of any two points in the same orbit are conjugate in $G$.

<1>4. Remark on Disjoint Orbits:
    *Proof:*
    <2>1. If $X$ is a union of disjoint orbits (non-transitive action), stabilizers of points in different orbits need not be conjugate (e.g. $G = S_3$ acting on $X = \{1, 2, 3\} \sqcup \{*\}$ where $*$ is fixed has $\operatorname{Stab}(1) \cong \mathbb{Z}_2$ while $\operatorname{Stab}(*) = S_3$).

<1>5. Conclusion:
    $\operatorname{Stab}_G(g \cdot x) = g \operatorname{Stab}_G(x) g^{-1}$. Q.E.D.
:::
