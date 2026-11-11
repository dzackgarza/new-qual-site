---
schema: qual/card@1
id: E-5CC0M
kind: problem
title: The two-fold covering of the figure eight restricted to the axes
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 60 Exercise 3, printed p. 375,
    with the definition of an evenly covered neighbourhood and Lemma 60.5's construction. At a point $(n,0)$ with $n\ne0$ of the restricted fibre a small neighbourhood of $E'$ is an interval whose image lies in the circle $A$, so no neighbourhood of the basepoint is evenly covered; at the origin the cross has four branches and the map is not a local homeomorphism. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
---

::: {.exercise}

Let $p: E \to X$ be the map constructed in the proof of Lemma 60.5. Let $E'$ be the subspace of $E$ that is the union of the $x$-axis and the $y$-axis.
Show that $p \mid E'$ is not a covering map.
:::

::: {.solution}

Write $q = p\restrict_{E'}: E' \to X$, where $E' = (\RR \times \{0\}) \cup (\{0\} \times \RR)$.

::: pf

::: pf-step

Setting and structure of the map $p$:
    *Proof:*

::: pf-proof

::: pf-step

The total space $E = (\RR \times \ZZ) \cup (\ZZ \times \RR) \subset \RR^2$ is the infinite grid in the plane.

:::

::: pf-step

The base space $X = A \vee B$ is the wedge of two circles $A$ and $B$ intersecting at a basepoint $x_0$.

:::

::: pf-step

The covering map $p: E \to X$ wraps each horizontal grid line $\RR \times \{n\}$ around circle $A$ and each vertical grid line $\{m\} \times \RR$ around circle $B$, sending all integer lattice points $\ZZ \times \ZZ$ to $x_0$.

:::

::: pf-step

The subspace $E' = (\RR \times \{0\}) \cup (\{0\} \times \RR)$ is the cross formed by the $x$-axis and $y$-axis.

:::

:::

:::

::: pf-step

Preimage of the basepoint in $E'$:
    *Proof:*

::: pf-proof

::: pf-step

The preimage $q^{-1}(x_0) = E' \cap (\ZZ \times \ZZ) = (\ZZ \times \{0\}) \cup (\{0\} \times \ZZ)$.

:::

::: pf-step

At the origin $(0, 0) \in E'$, both the horizontal and vertical axes meet, forming a 4-branch cross.

:::

::: pf-step

For any non-zero point $(n, 0) \in E'$ ($n \in \ZZ \setminus \{0\}$), $E'$ consists purely of the horizontal segment $(n - \varepsilon, n + \varepsilon) \times \{0\}$, which has 2 branches (homeomorphic to an open interval).

:::

:::

:::

::: pf-step

Failure of local homeomorphy and even covering:
    *Proof:*

::: pf-proof

::: pf-step

Let $n \in \ZZ \setminus \{0\}$ and consider $e = (n, 0) \in q^{-1}(x_0)$.

:::

::: pf-step

Any sufficiently small open neighborhood $V$ of $e$ in $E'$ is a 1-dimensional open interval $(n - \varepsilon, n + \varepsilon) \times \{0\}$ along the $x$-axis.

:::

::: pf-step

Under $q$, the image $q(V)$ lies entirely within the circle $A$, so $q(V) \cap (B \setminus \{x_0\}) = \varnothing$.

:::

::: pf-step

However, every open neighborhood $U$ of $x_0$ in the wedge space $X = A \vee B$ contains points of both $A \setminus \{x_0\}$ and $B \setminus \{x_0\}$.

:::

::: pf-step

Therefore, $q(V)$ cannot contain any open neighborhood of $x_0$ in $X$, so $q$ is not an open map and fails to be a local homeomorphism at $(n, 0)$.

:::

::: pf-step

Consequently, no open neighborhood of $x_0$ in $X$ is evenly covered by $q$.

:::

:::

:::

::: pf-step

Conclusion:

:::

:::

    $q = p\restrict_{E'}$ is not a covering map. Q.E.D.
:::
