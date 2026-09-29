---
schema: qual/card@1
id: E-79XXG
kind: problem
title: Covering transformations of four coverings of the figure eight
classification:
  areas:
  - topology
  topics:
  - Covering Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $X = A \vee B$ be the wedge of two circles.

(a) Let $E$ be the space pictured in Figure 81.4; let $p: E \to X$ wrap each arc $A_1$ and $A_2$ around $A$ and map $B_1$ and $B_2$ homeomorphically onto $B$.
Show that $p$ is a regular covering map.

(b) Determine the group of covering transformations of the covering of $X$ indicated in Figure 81.5. Is this covering regular?

(c) Repeat (b) for the covering pictured in Figure 81.6.

(d) Repeat (b) for the covering pictured in Figure 81.7.
:::

::: {.solution}
**Goal:** Determine the groups of covering transformations (deck transformations) $\mathcal{C}(E, p, X)$ and regularity status for the four graph coverings of the figure-eight space $X = A \vee B$.

::: pf

::: pf-step

General principles for covering transformations of graphs:
    *Proof:*

::: pf-proof

::: pf-step

A covering transformation $h \in \mathcal{C}(E, p, X)$ is a homeomorphism $h: E \to E$ satisfying $p \circ h = p$.

:::

::: pf-step

For graph coverings, $h$ is a directed-graph automorphism of the 1-skeleton $E$ that preserves edge orientations and edge labels ($a$-edges and $b$-edges).

:::

::: pf-step

A covering map of degree $d$ is **regular** (normal) if and only if $\mathcal{C}(E, p, X)$ acts transitively on the fiber $p^{-1}(x_0)$, which is equivalent to $|\mathcal{C}(E, p, X)| = d = [F_2 : p_*(\pi_1(E))]$.

:::

:::

:::

::: pf-step

Part (a) (Figure 81.4 - 2-fold covering):
    *Proof:*

::: pf-proof

::: pf-step

The total space $E$ has 2 vertices $\{v_1, v_2\}$, two $a$-arcs $A_1, A_2$ connecting $v_1$ and $v_2$, and two loops $B_1$ at $v_1$ and $B_2$ at $v_2$.

:::

::: pf-step

The map $\tau: E \to E$ swapping $v_1 \leftrightarrow v_2$, $A_1 \leftrightarrow A_2$, and $B_1 \leftrightarrow B_2$ preserves orientations and labels.

:::

::: pf-step

Thus $\mathcal{C}(E, p, X) = \{\operatorname{id}, \tau\} \cong \mathbb{Z}/2\mathbb{Z}$.

:::

::: pf-step

Since the deck transformation group has order $2$ equal to the degree of the covering, it acts transitively on the 2-point fiber.

:::

::: pf-step

Therefore, $p$ is a regular covering map.

:::

:::

:::

::: pf-step

Part (b) (Figure 81.5 - 3-fold cyclic covering):
    *Proof:*

::: pf-proof

::: pf-step

The total space has 3 vertices $\{v_1, v_2, v_3\}$ arranged in a 3-fold rotational cyclic symmetry where $a$ and $b$ edges cyclically permute the vertices ($v_1 \to v_2 \to v_3 \to v_1$).

:::

::: pf-step

The 3-fold cyclic rotation $\rho$ generates the group of label-preserving automorphisms: $\mathcal{C}(E, p, X) = \{\operatorname{id}, \rho, \rho^2\} \cong \mathbb{Z}/3\mathbb{Z}$.

:::

::: pf-step

Since $|\mathcal{C}(E, p, X)| = 3$ equals the degree of the covering, the action on the fiber is transitive.

:::

::: pf-step

Hence, the covering is **regular**.

:::

:::

:::

::: pf-step

Part (c) (Figure 81.6 - 3-fold non-regular covering):
    *Proof:*

::: pf-proof

::: pf-step

The 3-fold covering in Figure 81.6 has an asymmetric vertex structure: one vertex $v_1$ has a $b$-loop, while $v_2$ and $v_3$ are connected by a pair of $b$-edges.

:::

::: pf-step

Any label-preserving automorphism must map $v_1$ to a vertex carrying a $b$-loop, which forces $h(v_1) = v_1$.

:::

::: pf-step

Because a covering transformation of a connected covering space that fixes a point must be the identity map, $h = \operatorname{id}_E$.

:::

::: pf-step

Thus the group of covering transformations is trivial: $\mathcal{C}(E, p, X) = \{\operatorname{id}\}$.

:::

::: pf-step

Since $|\mathcal{C}(E, p, X)| = 1 < 3$, the action is not transitive, and the covering is **not regular**.

:::

:::

:::

::: pf-step

Part (d) (Figure 81.7 - 4-fold covering):
    *Proof:*

::: pf-proof

::: pf-step

The 4-fold covering in Figure 81.7 has 4 vertices with a central 180-degree rotational symmetry $\sigma$ exchanging opposite vertices and edges.

:::

::: pf-step

No 90-degree rotational symmetry preserves the alternating edge labeling.

:::

::: pf-step

Thus the group of covering transformations is $\mathcal{C}(E, p, X) = \{\operatorname{id}, \sigma\} \cong \mathbb{Z}/2\mathbb{Z}$.

:::

::: pf-step

Since $|\mathcal{C}(E, p, X)| = 2 < 4$, the deck group has order strictly less than the index $4$, so it does not act transitively on the fiber.

:::

::: pf-step

Therefore, the covering is **not regular**. Q.E.D.

:::

:::

:::

:::

:::
