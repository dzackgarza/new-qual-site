---
schema: qual/card@1
id: E-AMD-2I76LR6O
kind: exercise
title: Stabilizers of points in the same orbit are conjugate
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Conjugacy
  - Group Actions
relations: []
review: draft
---

::: {.exercise}
Show that if $x, y$ are in the same orbit, then their stabilizers are conjugate.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let a group $G$ act on a set $X$.
Recall the definition of the stabilizer of a point $z \in X$:
$$
G_z = \{g \in G \mid g \cdot z = z\}.
$$

Suppose $x, y \in X$ belong to the same orbit.
By definition, there exists an element $g \in G$ such that:
$$
y = g \cdot x.
$$

We claim that $G_y = g G_x g^{-1}$, meaning $G_y$ and $G_x$ are conjugate subgroups in $G$.

1. **Show $g G_x g^{-1} \subseteq G_y$:** Let $h \in G_x$, so $h \cdot x = x$.
   Consider the element $g h g^{-1} \in g G_x g^{-1}$.
   Acting on $y$:
   $$
   (g h g^{-1}) \cdot y = (g h g^{-1}) \cdot (g \cdot x) = (g h) \cdot (g^{-1} \cdot (g \cdot x)) = (g h) \cdot x = g \cdot (h \cdot x) = g \cdot x = y.
   $$
   Thus $g h g^{-1} \in G_y$.
   This proves that $g G_x g^{-1} \subseteq G_y$.

2. **Show $G_y \subseteq g G_x g^{-1}$:** Let $k \in G_y$, so $k \cdot y = y$.
   Consider the element $g^{-1} k g$.
   Acting on $x$:
   $$
   (g^{-1} k g) \cdot x = g^{-1} \cdot (k \cdot (g \cdot x)) = g^{-1} \cdot (k \cdot y) = g^{-1} \cdot y = g^{-1} \cdot (g \cdot x) = x.
   $$
   Thus $g^{-1} k g \in G_x$.
   Multiplying by $g$ on the left and $g^{-1}$ on the right:
   $$
   k = g (g^{-1} k g) g^{-1} \in g G_x g^{-1}.
   $$
   This proves that $G_y \subseteq g G_x g^{-1}$.

Combining both inclusions:
$$
G_y = g G_x g^{-1}.
$$
Therefore, the stabilizers $G_x$ and $G_y$ are conjugate subgroups in $G$.
:::
