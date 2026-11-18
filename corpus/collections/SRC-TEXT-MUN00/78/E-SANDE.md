---
schema: qual/card@1
id: E-SANDE
kind: problem
title: Classification of compact connected triangulable surfaces with boundary
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §78 Exercise 5, printed p. 476. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md. No source was saved. The queries were the Stack Exchange advanced
    searches "compact connected triangulable 2-manifold with boundary k holes" and "X-with-k-holes Munkres"
    (neither with hits) and the similar-question search from "Classification of compact surfaces with
    boundary" (15 items), whose threads state the classification without proof; the GitHub code search
    "munkres "Section 78"" returned no solutions file, and no course page found treats the section. The card
    keeps its own proof, which is the capping argument of the exercise's hint: each boundary circle is
    capped by a disk and Theorem 77.5 applied to the closed surface, the capping disks then removed.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 78 Exercise 5, printed pp. 476-477. Capping the k boundary circles by discs gives a closed surface X, classified by Theorem 77.5; removing the interiors of the caps returns Y as X-with-k-holes. Checked against the printed hint that each boundary component is a circle, which the preceding exercise supplies. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

Prove the following.

Theorem.
Given a compact connected triangulable 2-manifold $Y$ with boundary, such that $\partial Y$ has $k$ components, then $Y$ is homeomorphic to X-with-$k$-holes, where $X$ is either $S^2$ or the $n$-fold torus $T_n$ or the $m$-fold projective plane $P_m$.

[Hint: Each component of $\partial Y$ is homeomorphic to a circle.]
:::

::: {.solution}

No retained solution set covers this theorem: the card's own capping argument is set out here as separate steps, the cap being the construction that turns a bounded surface into a closed one.

Let $Y$ be a compact connected triangulable $2$-manifold with boundary, $\partial Y$ having components $C_{1},\dots,C_{k}$.

::: pf

::: {.pf-step #circles}
Each $C_{i}$ is homeomorphic to $S^{1}$.

::: pf-proof
$\partial Y$ is a compact $1$-manifold without boundary (card [[E-RKSXA]]), so each component is a connected compact $1$-manifold, and such a space is homeomorphic to $S^{1}$ (the circle is the only connected compact $1$-manifold).
:::

:::

::: {.pf-step #cap}
Let $X=Y\cup_{\phi_{1}}D_{1}^{2}\cup\cdots\cup_{\phi_{k}}D_{k}^{2}$, attaching a closed disk along each boundary circle by a homeomorphism $\phi_{i}:S^{1}\to C_{i}$.

::: pf-proof
Each $\phi_{i}$ is a homeomorphism onto the closed subset $C_{i}$ of $Y$, and the disks are disjoint from $Y$ and from each other, so the quotient of the compact space $Y\sqcup D_{1}^{2}\sqcup\cdots\sqcup D_{k}^{2}$ by the identifications $z\sim\phi_{i}(z)$ is well defined; this quotient is $X$.
:::

:::

::: {.pf-step #basic}
$X$ is compact, Hausdorff and connected.

::: pf-proof
It is a quotient of a compact space, hence compact. The identifications are made along closed subsets by homeomorphisms, so the quotient is Hausdorff (the graph of the equivalence relation is closed in the compact Hausdorff square). $Y$ is connected and each $D_{i}^{2}$ meets $Y$ along the whole circle $C_{i}\ne\varnothing$, so the union is connected.
:::

:::

::: {.pf-step #manifold}
$X$ is a $2$-manifold without boundary.

::: pf-proof
Away from the seams the charts are those of $\operatorname{int}Y$ or of the disk interiors. At a seam point $p\in C_{i}$, take a half-disk chart of $Y$ at $p$ with its diameter on $C_{i}$ and the matching half-disk chart of $D_{i}^{2}$; their union is a disk chart of $X$ at $p$.
:::

:::

::: {.pf-step #triangulable}
$X$ is triangulable.

::: pf-proof
Subdivide a triangulation of $Y$ so that each $C_{i}$ is a subcomplex (possible because the $C_{i}$ are compact and finitely many simplices meet each), then triangulate each $D_{i}^{2}$ compatibly with the boundary triangulation of $C_{i}$; the pieces agree on their intersections, so they assemble into a triangulation of $X$.
:::

:::

::: {.pf-step #classify}
$X$ is homeomorphic to one of $S^{2}$, $T_{n}$ $(n\ge1)$, $P_{m}$ $(m\ge1)$.

::: pf-proof
$X$ is a compact connected triangulable surface without boundary, so the classification theorem for closed surfaces applies.
:::

:::

::: {.pf-step #holes}
$Y\cong X$ with $k$ open disks removed.

::: pf-proof
In each $D_{i}^{2}$ choose an open concentric disk $E_{i}$ with $\overline{E_{i}}\subseteq\operatorname{int}D_{i}^{2}$. The annulus $D_{i}^{2}\setminus E_{i}$ carries a collar of $C_{i}$, and pushing it radially into the boundary collar of $Y$ gives a homeomorphism $X\setminus\bigcup_{i}E_{i}\cong Y$ that is the identity outside the collars. So $Y$ is $X$ with $k$ holes.
:::

:::

::: {.pf-qed}
$Y$ is homeomorphic to $X$-with-$k$-holes for $X$ one of the closed surfaces listed, by steps [](#cap){.pf-ref}, [](#manifold){.pf-ref}, [](#triangulable){.pf-ref}, [](#classify){.pf-ref} and [](#holes){.pf-ref}.
:::

:::

:::
