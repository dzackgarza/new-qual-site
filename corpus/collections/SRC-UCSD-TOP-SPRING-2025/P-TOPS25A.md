---
schema: qual/card@1
id: P-TOPS25A
kind: problem
title: Fundamental group of the 2-sphere minus ten points
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
  date: 2026-08-30
- event: source-checked
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Seven steps asserted their claim with no justification and each now carries one: the stereographic
    homeomorphism onto the plane, the passage of a finite complement through it, the disjoint disks and
    the basepoint, the disjoint arcs, the deformation retraction of the disk with nine holes onto its
    spine and the collapse of the tree, the outer collar with no contribution to the homotopy type, and
    Seifert--van Kampen for the wedge together with the invariance of $\pi_1$ under homotopy equivalence.
    Checked while writing: the two ends of the argument are independent, the nine circles giving
    $F_9$ and the collar giving nothing, and the basepoint lies outside the disks so the arcs exist.
    Sources are cited by numbered statement: Seifert--van Kampen, and invariance of the fundamental group
    under homotopy equivalence. No page reference is written in the body of this card or in the event
    above. The statement is unchanged. The collection retains the UCSD topology qualifying exam of
    Spring 2025 and no solution sheet, so the argument is the card's own.
---

::: {.problem}
Let $X = S^2 \setminus \{p_1, p_2, \dots, p_{10}\}$ be the topological space obtained by removing 10 distinct points from the 2-sphere $S^2$.
Compute its **fundamental group** $\pi_1(X, x_0)$.
:::

::: {.solution}

::: pf

::: {.pf-step #project}

$X$ is homeomorphic to the plane with nine points removed.

::: pf-proof

::: pf-step
Stereographic projection gives a homeomorphism
$$
S^2\setminus\{p_{10}\}\cong\RR^2.
$$

::: pf-proof
Stereographic projection from the deleted point sends $p \ne p_{10}$ to the intersection of the line through $p_{10}$ and $p$ with the equatorial plane, and its formula is continuous with a continuous inverse on $\RR^2$; a continuous bijection with continuous inverse is a homeomorphism.
:::

:::

::: pf-step
Under this homeomorphism the other nine deleted points become distinct points $q_1,\dots,q_9\in\RR^2$. Hence
$$
X\cong \RR^2\setminus\{q_1,\dots,q_9\}.
$$

::: pf-proof
A homeomorphism carries the complement of a finite set onto the complement of the image of that set, because it is a bijection that restricts to a bijection of the complements, and the restricted map is still continuous with continuous inverse. The images $q_1, \dots, q_9$ of the nine remaining deleted points are distinct because the projection is injective.
:::

:::

:::

:::

::: pf-step
The punctured plane $\RR^2\setminus\{q_1,\dots,q_9\}$ is homotopy equivalent to a wedge of nine circles.

::: pf-proof

::: pf-step
Choose pairwise disjoint small closed disks $D_i$ centered at $q_i$, and choose a basepoint $x_0$ outside all of them.

::: pf-proof
The nine points are distinct, so the distances between pairs are positive and there is a positive minimum among them; closed disks of radius less than half that minimum are pairwise disjoint. The punctured plane still has points, and any of them outside the disks serves as $x_0$, the disks being bounded.
:::

:::

::: pf-step
Join $x_0$ to one point of each boundary circle $\partial D_i$ by embedded arcs whose interiors are pairwise disjoint and avoid the disks.

::: pf-proof
A finite set of closed disks in the plane can be joined to a point outside them by arcs with pairwise disjoint interiors: take straight segments to chosen points of the boundary circles and perturb them slightly, or use that the plane is locally path connected and the union of the disks is compact, so paths avoid it after a small deformation. The arcs then meet the disks only at their chosen endpoints.
:::

:::

::: pf-step
A sufficiently large closed disk containing this configuration, with the interiors of the $D_i$ removed, deformation retracts onto the union of the nine circles $\partial D_i$ and the connecting arcs. Collapsing the tree formed by the connecting arcs gives a wedge $\bigvee_{i=1}^9 S^1$.

::: pf-proof
Removing the interiors of finitely many disjoint closed disks from a closed disk leaves a compact region whose boundary consists of the outer circle and the inner circles; it deformation retracts onto the graph formed by the inner circles together with the arcs joining them to the basepoint and to the outer boundary. The arcs and the outer circle form a tree, and contracting a tree in a graph does not change its homotopy type, so the region is homotopy equivalent to the wedge of the nine inner circles.
:::

:::

::: pf-step
The complement of the large disk contributes only an outer collar, so the whole punctured plane has the same homotopy type. Therefore
$$
X\simeq \bigvee_{i=1}^9 S^1.
$$

::: pf-proof
The complement of the large closed disk in the plane is homeomorphic to $S^1 \times [1, \infty)$, which deformation retracts onto $S^1 \times \{1\}$, its boundary circle; that circle is part of the region retracted in the previous step. So the whole punctured plane is homotopy equivalent to the region with the large disk, hence to the wedge of nine circles, and the homeomorphism of the first part carries this to $X$.
:::

:::

:::

:::

::: pf-step
By Seifert--van Kampen,
$$
\pi_1(X,x_0)\cong \pi_1\!\left(\bigvee_{i=1}^9 S^1\right)\cong F_9,
$$
the free group on nine generators.


::: pf-proof
For a wedge of finitely many circles, Seifert--van Kampen applies to the cover by the union of the first circle and the wedge of the rest with small open neighbourhoods of the basepoint added: the intersection is contractible, so the fundamental group of the wedge is the free product of the two factors. Induction on the number of summands gives $\pi_1\left(\bigvee_{i=1}^{9} S^1\right) \cong F_9$, the free group on nine generators. A homotopy equivalence induces an isomorphism on fundamental groups, so $\pi_1(X, x_0)$ is that free group.
:::

:::

:::

:::
