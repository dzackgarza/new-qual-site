---
schema: qual/card@1
id: E-5CC0M
kind: exercise
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
---

::: {.exercise}

Let $p: E \to X$ be the map constructed in the proof of Lemma 60.5. Let $E'$ be the subspace of $E$ that is the union of the $x$-axis and the $y$-axis.
Show that $p \mid E'$ is not a covering map.
:::

::: solution
**Goal:** Prove that the restriction $q = p|_{E'}: E' \to X = A \vee B$ of the grid covering map to the union of the coordinate axes $E' = (\mathbb{R} \times \{0\}) \cup (\{0\} \times \mathbb{R})$ is not a covering map.

<1>1. Setting and structure of the map $p$:
    *Proof:*
    <2>1. The total space $E = (\mathbb{R} \times \mathbb{Z}) \cup (\mathbb{Z} \times \mathbb{R}) \subset \mathbb{R}^2$ is the infinite grid in the plane.
    <2>2. The base space $X = A \vee B$ is the wedge of two circles $A$ and $B$ intersecting at a basepoint $x_0$.
    <2>3. The covering map $p: E \to X$ wraps each horizontal grid line $\mathbb{R} \times \{n\}$ around circle $A$ and each vertical grid line $\{m\} \times \mathbb{R}$ around circle $B$, sending all integer lattice points $\mathbb{Z} \times \mathbb{Z}$ to $x_0$.
    <2>4. The subspace $E' = (\mathbb{R} \times \{0\}) \cup (\{0\} \times \mathbb{R})$ is the cross formed by the $x$-axis and $y$-axis.

<1>2. Preimage of the basepoint in $E'$:
    *Proof:*
    <2>1. The preimage $q^{-1}(x_0) = E' \cap (\mathbb{Z} \times \mathbb{Z}) = (\mathbb{Z} \times \{0\}) \cup (\{0\} \times \mathbb{Z})$.
    <2>2. At the origin $(0, 0) \in E'$, both the horizontal and vertical axes meet, forming a 4-branch cross.
    <2>3. For any non-zero point $(n, 0) \in E'$ ($n \in \mathbb{Z} \setminus \{0\}$), $E'$ consists purely of the horizontal segment $(n - \varepsilon, n + \varepsilon) \times \{0\}$, which has 2 branches (homeomorphic to an open interval).

<1>3. Failure of local homeomorphy and even covering:
    *Proof:*
    <2>1. Let $n \in \mathbb{Z} \setminus \{0\}$ and consider $e = (n, 0) \in q^{-1}(x_0)$.
    <2>2. Any sufficiently small open neighborhood $V$ of $e$ in $E'$ is a 1-dimensional open interval $(n - \varepsilon, n + \varepsilon) \times \{0\}$ along the $x$-axis.
    <2>3. Under $q$, the image $q(V)$ lies entirely within the circle $A$, so $q(V) \cap (B \setminus \{x_0\}) = \varnothing$.
    <2>4. However, every open neighborhood $U$ of $x_0$ in the wedge space $X = A \vee B$ contains points of both $A \setminus \{x_0\}$ and $B \setminus \{x_0\}$.
    <2>5. Therefore, $q(V)$ cannot contain any open neighborhood of $x_0$ in $X$, so $q$ is not an open map and fails to be a local homeomorphism at $(n, 0)$.
    <2>6. Consequently, no open neighborhood of $x_0$ in $X$ is evenly covered by $q$.

<1>4. Conclusion:
    $q = p|_{E'}$ is not a covering map. Q.E.D.
:::
