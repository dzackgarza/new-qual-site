---
schema: qual/card@1
id: P-NYXUQ
kind: problem
title: Conjugacy of stabilizers along an orbit
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
What group-theoretic construct relates the stabilizer of two points in the same orbit under a group action?
:::

::: solution
**Goal:** Prove that if $x, y \in X$ belong to the same orbit under a group action $G \curvearrowright X$, their stabilizer subgroups $\operatorname{Stab}_G(x)$ and $\operatorname{Stab}_G(y)$ are **conjugate subgroups** in $G$.

<1>1. Setting up the group action: *Proof:* <2>1. Let $G$ act on a set $X$.
For $x \in X$, the stabilizer is $G_x = \operatorname{Stab}_G(x) = \{g \in G \mid g \cdot x = x\}$.
<2>2. Suppose $x$ and $y$ are in the same orbit $\mathcal{O}$.
<2>3. By definition of the orbit, there exists an element $g \in G$ such that $g \cdot x = y$.

<1>2. Proof of conjugacy: $G_y = g G_x g^{-1}$: *Proof:* <2>1. Let $h \in G_x$, so $h \cdot x = x$.
<2>2. Consider the conjugated element $g h g^{-1} \in G$.
Acting on $y$: $$(g h g^{-1}) \cdot y = (g h g^{-1}) \cdot (g \cdot x) = (g h) \cdot (g^{-1} g \cdot x) = (g h) \cdot x = g \cdot (h \cdot x) = g \cdot x = y.$$ <2>3. Thus $g h g^{-1} \in G_y$, showing $g G_x g^{-1} \subseteq G_y$.
<2>4. Conversely, let $k \in G_y$, so $k \cdot y = y$.
<2>5. Acting on $x$ with $g^{-1} k g$: $$(g^{-1} k g) \cdot x = g^{-1} \cdot (k \cdot (g \cdot x)) = g^{-1} \cdot (k \cdot y) = g^{-1} \cdot y = g^{-1} \cdot (g \cdot x) = x.$$ <2>6. Thus $g^{-1} k g \in G_x$, so $k = g(g^{-1}kg)g^{-1} \in g G_x g^{-1}$, showing $G_y \subseteq g G_x g^{-1}$.
<2>7. Therefore $G_y = g G_x g^{-1}$.

<1>3. Conclusion: The stabilizers of two points in the same orbit are conjugate subgroups: $\operatorname{Stab}_G(g \cdot x) = g \operatorname{Stab}_G(x) g^{-1}$.
Q.E.D.
:::
