---
schema: qual/card@1
id: E-AMD-2MV56W7X
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
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that the stabilizer of an element $G_x$ is a subgroup of $G$.
:::

::: {.solution}
Let a group $G$ act on a set $X$, and let $x \in X$.
The stabilizer of $x$ is defined as:
$$
G_x = \{g \in G \mid g \cdot x = x\}.
$$

We verify the standard subgroup criteria (non-emptiness, closure under group multiplication, and closure under inverses):

1. **Identity element (Non-emptiness):** By the definition of a group action, the identity element $e \in G$ satisfies:
   $$
   e \cdot x = x.
   $$
   Thus $e \in G_x$, so $G_x \neq \emptyset$.

2. **Closure under multiplication:** Let $g, h \in G_x$.
   Then $g \cdot x = x$ and $h \cdot x = x$.
   Using the compatibility axiom of the group action:
   $$
   (g h) \cdot x = g \cdot (h \cdot x) = g \cdot x = x.
   $$
   Thus $gh \in G_x$.

3. **Closure under inverses:** Let $g \in G_x$, so $g \cdot x = x$.
   Applying $g^{-1}$ to both sides:
   $$
   g^{-1} \cdot (g \cdot x) = g^{-1} \cdot x.
   $$
   Using $(g^{-1} g) \cdot x = e \cdot x = x$, we obtain:
   $$
   g^{-1} \cdot x = x.
   $$
   Thus $g^{-1} \in G_x$.

Since $G_x$ contains the identity and is closed under multiplication and inverses, $G_x$ is a subgroup of $G$ ($G_x \leq G$).
:::
