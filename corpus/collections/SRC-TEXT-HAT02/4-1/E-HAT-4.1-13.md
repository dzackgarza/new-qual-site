---
schema: qual/card@1
id: E-HAT-4.1-13
kind: exercise
title: "CW complexes retract onto contractible subcomplexes"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: exercise
Use the **Extension Lemma** (homotopy extension property for CW pairs) to show that a CW complex $X$ **retracts** onto any contractible subcomplex $A \subseteq X$.
:::

::: solution
**Goal:** Prove that if $(X, A)$ is a CW pair with $A$ contractible, there exists a continuous retraction $r: X \to A$ ($r|_A = \operatorname{id}_A$).

<1>1. The Homotopy Extension Property (HEP) / Extension Lemma for CW Pairs:
    *Proof:*
    <2>1. A subcomplex $A$ of a CW complex $X$ forms a **CW pair** $(X, A)$.
    <2>2. By the **Homotopy Extension Property (HEP)** (Hatcher, Lemma 4.15 / Extension Lemma):
        For any CW pair $(X, A)$, the pair has the homotopy extension property with respect to every topological space $Y$.
    <2>3. Specifically: Given a continuous map $f: X \to Y$ and a homotopy $h: A \times I \to Y$ starting at $f|_A$ (i.e. $h(a, 0) = f(a)$ for all $a \in A$), there exists a continuous homotopy $H: X \times I \to Y$ such that:
        - $H(x, 0) = f(x)$ for all $x \in X$, and
        - $H(a, t) = h(a, t)$ for all $(a, t) \in A \times I$.

<1>2. Setup for Contractible Subcomplex $A$:
    *Proof:*
    <2>1. Let $A \subseteq X$ be a contractible subcomplex.
    <2>2. By definition of contractibility, the identity map $\operatorname{id}_A: A \to A$ is homotopic to a constant map $c_{a_0}: A \to A$ (where $c_{a_0}(a) = a_0 \in A$).
    <2>3. That is, there exists a continuous homotopy:
        $$h: A \times [0, 1] \longrightarrow A$$
        such that $h(a, 0) = a = \operatorname{id}_A(a)$ and $h(a, 1) = a_0$ for all $a \in A$.
    <2>4. Reversing the time parameter $t \mapsto 1 - t$, we get a continuous homotopy:
        $$\bar{h}: A \times [0, 1] \longrightarrow A, \qquad \bar{h}(a, t) = h(a, 1 - t)$$
        satisfying $\bar{h}(a, 0) = a_0$ (constant map) and $\bar{h}(a, 1) = a = \operatorname{id}_A(a)$.

<1>3. Extending the Homotopy to $X$:
    *Proof:*
    <2>1. Set the target space to be $Y = A$.
    <2>2. Define the initial map $f_0: X \to A$ to be the constant map:
        $$f_0(x) = a_0 \quad \text{for all } x \in X.$$
    <2>3. Notice that the restriction of $f_0$ to $A$ matches the start of the homotopy $\bar{h}$:
        $$f_0|_A(a) = a_0 = \bar{h}(a, 0) \quad \text{for all } a \in A.$$
    <2>4. Since $(X, A)$ is a CW pair, by the **Homotopy Extension Property** (with target space $Y = A$), there exists a continuous homotopy:
        $$H: X \times [0, 1] \longrightarrow A$$
        such that:
        - $H(x, 0) = f_0(x) = a_0$ for all $x \in X$, and
        - $H(a, t) = \bar{h}(a, t)$ for all $a \in A, t \in [0, 1]$.

<1>4. Constructing the Retraction $r: X \to A$:
    *Proof:*
    <2>1. Define the map $r: X \to A$ by evaluating $H$ at time $t = 1$:
        $$r(x) \coloneqq H(x, 1).$$
    <2>2. Since $H$ is continuous and has image in $A$, $r: X \to A$ is a continuous map.
    <2>3. For any point $a \in A$:
        $$r(a) = H(a, 1) = \bar{h}(a, 1) = \operatorname{id}_A(a) = a.$$
    <2>4. Thus $r|_A = \operatorname{id}_A$, which proves that $r: X \to A$ is a **retraction**.

<1>5. Conclusion:
    $X$ retracts onto the contractible subcomplex $A$. Q.E.D.
:::
