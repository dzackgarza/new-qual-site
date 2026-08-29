---
schema: qual/card@1
id: P-VXX34
kind: problem
title: The stabilizer of a point under a group action is a subgroup
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Subgroups
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Show that if $G \curvearrowright X$ is a group action, then the stabilizer $G_x = \operatorname{Stab}_G(x)$ of any point $x \in X$ is a subgroup of $G$.
:::

::: solution
**Goal:** Prove that for any group action $G \curvearrowright X$ and any $x \in X$, $G_x = \{g \in G \mid g \cdot x = x\} \le G$.

<1>1. Definition and Non-emptiness:
    *Proof:*
    <2>1. By the identity axiom of a group action, $e \cdot x = x$ where $e \in G$ is the identity element.
    <2>2. Thus $e \in G_x$, so $G_x \ne \varnothing$.

<1>2. Closure under group operation:
    *Proof:*
    <2>1. Let $g, h \in G_x$, so $g \cdot x = x$ and $h \cdot x = x$.
    <2>2. By the compatibility axiom of a group action:
        $$(gh) \cdot x = g \cdot (h \cdot x) = g \cdot x = x.$$
    <2>3. Thus $gh \in G_x$.

<1>3. Closure under inverses:
    *Proof:*
    <2>1. Let $g \in G_x$, so $g \cdot x = x$.
    <2>2. Act on both sides with $g^{-1}$:
        $$g^{-1} \cdot (g \cdot x) = g^{-1} \cdot x.$$
    <2>3. Using compatibility and identity axioms:
        $$x = e \cdot x = (g^{-1}g) \cdot x = g^{-1} \cdot (g \cdot x) = g^{-1} \cdot x.$$
    <2>4. Thus $g^{-1} \cdot x = x$, which proves $g^{-1} \in G_x$.

<1>4. Conclusion:
    By the two-step subgroup criterion (or one-step $g h^{-1} \in G_x$), $G_x$ is a subgroup of $G$. Q.E.D.
:::
