---
schema: qual/card@1
id: E-2M0XQ
kind: problem
title: Fundamental groups of twelve standard spaces
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
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
    Checked line by line against Munkres, Topology (2000), Section 58 Exercise 2, printed p. 366,
    with Theorem 58.7, that a homotopy equivalence induces an isomorphism on fundamental groups, and Theorem 59.3. Each of the twelve answers is a deformation retraction onto a circle, a point, or a wedge of two circles, or a homeomorphism onto one of those. What was corrected: the reason given for (j), $S^1\cup(\RR_+\times\RR)$, was a radial formula that is undefined at the origin and on the part of the $y$-axis outside the circle. The half-plane part is contractible, its intersection with the circle is the right semicircle, an arc, and collapsing that arc turns the union into a wedge of $S^1$ with a contractible space; the answer $\ZZ$ is unchanged and the card now gives that reason. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
---

::: {.exercise}

For each of the following spaces, the fundamental group is either trivial, infinite cyclic, or isomorphic to the fundamental group of the figure eight.
Determine for each space which of the three alternatives holds.

(a) The "solid torus," $B^2 \times S^1$.

(b) The torus $T$ with a point removed.

(c) The cylinder $S^1 \times I$.

(d) The infinite cylinder $S^1 \times \RR$.

(e) $\RR^3$ with the nonnegative $x$, $y$, and $z$ axes deleted.

The following subsets of $\RR^2$:

(f) $\theset{x \mid \norm{x} > 1}$

(g) $\theset{x \mid \norm{x} \geq 1}$

(h) $\theset{x \mid \norm{x} < 1}$

(i) $S^1 \cup (\RR_+ \times 0)$

(j) $S^1 \cup (\RR_+ \times \RR)$

(k) $S^1 \cup (\RR \times 0)$

(l) $\RR^2 - (\RR_+ \times 0)$
:::

::: {.solution}

::: pf

::: pf-step

Spaces with fundamental group $\pi_1 \cong \ZZ$ (infinite cyclic):
    *Proof:*

::: pf-proof

::: pf-step

**(a) Solid torus $B^2 \times S^1$:** $B^2$ is contractible to $\{0\}$, so $B^2 \times S^1$ deformation retracts onto $\{0\} \times S^1 \cong S^1$. Hence $\pi_1(B^2 \times S^1) \cong \pi_1(S^1) \cong \ZZ$.

:::

::: pf-step

**(c) Cylinder $S^1 \times I$:** The interval $I = [0, 1]$ is contractible, so $S^1 \times I$ deformation retracts onto $S^1 \times \{0\} \cong S^1$, giving $\pi_1(S^1 \times I) \cong \ZZ$.

:::

::: pf-step

**(d) Infinite cylinder $S^1 \times \RR$:** Deformation retracts onto $S^1 \times \{0\} \cong S^1$, giving $\pi_1(S^1 \times \RR) \cong \ZZ$.

:::

::: pf-step

**(f) $\{x \in \RR^2 : \norm{x} > 1\}$:** Deformation retracts radially onto the circle of radius 2 (or any circle of radius $r > 1$), so $\pi_1 \cong \ZZ$.

:::

::: pf-step

**(g) $\{x \in \RR^2 : \norm{x} \ge 1\}$:** Deformation retracts radially onto the unit circle $S^1$, so $\pi_1 \cong \ZZ$.

:::

::: pf-step

**(i) $S^1 \cup (\RR_+ \times \{0\})$:** The attached half-line $[1, \infty) \times \{0\}$ deformation retracts linearly into $(1, 0) \in S^1$, so the entire space deformation retracts onto $S^1$, giving $\pi_1 \cong \ZZ$.

:::

::: pf-step

**(j) $S^1\cup(\RR_+\times\RR)$:** the closed right half-plane $H$ is contractible and $S^1\cap H$ is the right semicircle, an arc, so $S^1\cup H$ is homotopy equivalent to $S^1$: collapsing that arc in $H$ leaves a contractible space, and collapsing it in $S^1$ leaves a circle, so the union is homotopy equivalent to the wedge of a circle with a contractible space, which is a circle. Hence $\pi_1\cong\ZZ$. (A radial formula does not give the deformation retraction here: a point on the $y$-axis away from $(0,\pm1)$ has no image under $z\mapsto z/\norm z$, and the map is undefined at the origin.)

:::

:::

:::

::: pf-step

Spaces with fundamental group $\pi_1 \cong \ZZ * \ZZ$ (figure eight):
    *Proof:*

::: pf-proof

::: pf-step

**(b) Punctured torus $T^2 \setminus \{p\}$:** Representing $T^2$ as a square with identified edges $aba^{-1}b^{-1}$, removing the center point allows the open punctured 2-cell to deformation retract onto the boundary 1-skeleton $S^1 \vee S^1$. Hence $\pi_1(T^2 \setminus \{p\}) \cong \pi_1(S^1 \vee S^1) \cong \ZZ * \ZZ$.

:::

::: pf-step

**(e) $\RR^3 \setminus (\text{nonnegative axes})$:** Radially deformation retracts onto $S^2$ minus three points $(1,0,0), (0,1,0), (0,0,1)$. By stereographic projection from one puncture, $S^2$ minus 3 points is homeomorphic to the twice-punctured plane $\RR^2 \setminus \{p, q\}$, which deformation retracts onto $S^1 \vee S^1$. Hence $\pi_1 \cong \ZZ * \ZZ$.

:::

::: pf-step

**(k) $S^1 \cup (\RR \times \{0\})$:** The external rays $(-\infty, -1] \times \{0\}$ and $[1, \infty) \times \{0\}$ deformation retract onto their endpoints. The remaining theta graph has two vertices, $(\pm1,0)$, and three edges: the two semicircles and the diameter. The diameter is a maximal tree. Collapsing it is a homotopy equivalence of graphs and gives $S^1\vee S^1$. Hence $\pi_1\cong\ZZ*\ZZ$.

:::

:::

:::

::: pf-step

Spaces with fundamental group $\pi_1 \cong \{1\}$ (trivial):
    *Proof:*

::: pf-proof

::: pf-step

**(h) $\{x \in \RR^2 : \norm{x} < 1\}$:** The open unit disk is convex, hence contractible to the origin $\{0\}$, so $\pi_1 \cong \{1\}$.

:::

::: pf-step

**(l) $\RR^2 \setminus (\RR_+ \times \{0\})$:** The slit plane is star convex about $(-1,0)$. For a point off the $x$-axis, the open segment toward $(-1,0)$ keeps the same nonzero sign of its second coordinate; points on the retained part of the axis stay there. Straight-line contraction to $(-1,0)$ therefore remains in the slit plane, so $\pi_1\cong\{1\}$.

:::

:::

:::

::: pf-step

Summary Table:

:::

:::

    - **Trivial ($\{1\}$):** (h), (l).
    - **Infinite cyclic ($\ZZ$):** (a), (c), (d), (f), (g), (i), (j).
    - **Figure eight ($\ZZ * \ZZ$):** (b), (e), (k).
    Q.E.D.
:::
