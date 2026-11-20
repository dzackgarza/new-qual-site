---
schema: qual/card@1
id: E-L4UAO
kind: problem
title: Separation properties project from products to factors
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 32 Exercise 2, printed p. 205,
    and against Theorem 31.2 (subspaces and finite products of Hausdorff and of regular spaces
    inherit the property) and Exercise 32.1. The argument is the standard one: a slice with all
    other coordinates fixed at chosen base points is a homeomorphic copy of X_alpha; for the
    Hausdorff and regular cases the slice is a subspace of the product; for the normal case the
    product is T1, so the slice, being an intersection of preimages of closed points under the
    continuous projections, is closed, and a closed subspace of a normal space is normal. No
    published solution was located: Orellana's Section 32 covers Exercises 1, 4 and 5 only
    (printed p. 33), "Doug's World" (printed pp. 6-7) covers 32.1, 32.3, 32.4, 32.5, 32.6 and 32.7,
    Rajaraman has no Section 32, and the sets that stop before Chapter 4 are Whitman,
    positron0802, shenapse, 9beach and kyp44. The search is recorded in the COMPLAINTS.md entry for
    this batch.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Checked against the located published solution: dbFin, "Section 32: Problem 2 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-32-normal-spaces/problem-2-solution/ (read
    2026-11-10; kept at tmp/sources/dbfin/section-32-normal-spaces/problem-2-solution.txt), and
    against Munkres, Topology (2000), Section 32 Exercise 2, printed p. 205, Theorem 31.2 and
    Exercise 32.1. What the source proves, and the card's argument agrees with, is the Hausdorff and
    regular cases: a basis element U of the product containing the point p_x with all other
    coordinates fixed at chosen base points has its projection pi_alpha(U) open, and two such basis
    elements are disjoint only if their projections are, since p_z lies in a basis element exactly
    when z lies in its alpha-th coordinate set. The source then says that the T1 requirement "I
    leave this as a very easy exercise" and that "being a normal space is not a hereditary
    property, so we still need to show that each X_alpha is normal". Its own normal step -- that
    disjoint basis neighbourhoods of p_A and p_B "projections into X_alpha separate A and B" --
    does not go through for the arbitrary open sets that normality supplies, and in general
    projections of two disjoint open sets of a product can meet. The card therefore keeps the
    closed-slice argument for the normal case (the product is T1, so the slice is an intersection of
    preimages of closed points, hence closed, and a closed subspace of a normal space is normal), and
    this exercise stays in the COMPLAINTS.md entry for the normal case.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the slice imbedding (Theorem 18.4), inheritance
    of the Hausdorff and regular properties by a subspace (Theorem 31.2), and the normal
    case: the slice is closed because a normal space is T_1 and a closed subspace of a
    normal space is normal (Exercise 32.1). dbFin, Section 32 Problem 2 Solution, as the
    earlier audit note records; Munkres §32 Exercise 2, printed p. 205. The printed
    statement needed no repair.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Read for #169 against Munkres, Topology (2000), Section 32 Exercise 2, printed p. 205, and
    repaired in two places. (i) The imbedding step cited Theorem 18.4 twice. That theorem is
    "Maps into products" for two factors, $f:A\to X\times Y$, and the map here goes into
    $\prod_{\beta}X_{\beta}$ over an arbitrary index set; the statement the step uses is
    Theorem 19.6, printed p. 117, whose proof also records that the projections $\pi_{\beta}$ are
    continuous, which is the second of the two citations. Both now name Theorem 19.6. (ii) The
    normal case concluded that each $\{a_{\beta}\}$ is closed in $X_{\beta}$ from "$X$ is
    normal, hence $T_{1}$", which says nothing about the factors; what supplies it is the
    Hausdorff case already proved on this card, the product being Hausdorff, so the step now cites
    the earlier step. Re-read and unchanged: the slice $S$ is closed as
    $\bigcap_{\beta\ne\alpha}\pi_{\beta}^{-1}(\{a_{\beta}\})$ over an arbitrary index set,
    which is closed being an intersection of closed sets; a closed subspace of a normal space is
    normal, which is Exercise 32.1, printed p. 205, read on the page and exactly that sentence;
    subspaces of Hausdorff and of regular spaces are Hausdorff and regular by Theorem 31.2,
    printed p. 197, whose (a) and (b) say so; and the nonemptiness of the factors is what supplies
    the basepoints $a_{\beta}$. Also checked and kept: dbFin's normal step, projecting arbitrary
    disjoint open sets of the product, is not a proof, since projections of disjoint open sets of a
    product can meet -- the closed-slice argument is the card's and is the one that works. Page
    note: the folios 205, 205, 197 and 117 above were read from a copy of
    `tmp/sources/munkres-2000-topology.md` carrying `<!-- page pdf=N folio=M -->` markers at every
    page, which existed in the checkout during this pass and was replaced afterwards by the
    version carrying only the three page-range markers; the agreement of Exercise 32.2 and
    Exercise 32.1 with printed p. 205, of Theorem 31.2 with p. 197 and of Theorem 19.6 with p. 117
    is therefore an observation of this pass that a later reader cannot repeat from the current
    file.
---

::: {.exercise}

Show that if $\prod X_\alpha$ is Hausdorff, or regular, or normal, then so is $X_\alpha$.
(Assume that each $X_\alpha$ is nonempty.)
:::

::: {.solution}
The published solution is reported on this card's earlier audit note from **dbFin, "Section 32: Problem 2 Solution"** (`tmp/sources/dbfin/section-32-normal-spaces/problem-2-solution.txt`); the slice argument below is the standard one and is checked against Munkres §32 Exercise 2, printed p. 205, Theorem 31.2 and Exercise 32.1.

Fix an index $\alpha$ and choose a basepoint $a_{\beta}\in X_{\beta}$ for every $\beta\ne\alpha$; the spaces are nonempty.

::: pf

::: {.pf-step #slice}
The map $i:X_{\alpha}\to\prod_{\beta}X_{\beta}$, with $i(x)_{\alpha}=x$ and $i(x)_{\beta}=a_{\beta}$ for $\beta\ne\alpha$, is an imbedding onto the slice $S=i(X_{\alpha})$.

::: pf-proof
$i$ is injective, since $x$ is recovered as the $\alpha$-coordinate of $i(x)$. It is continuous because each coordinate function $\pi_{\beta}\circ i$ is either the identity of $X_{\alpha}$ or a constant map, and a map into a product with the product topology is continuous as soon as all its coordinate functions are: that is Theorem 19.6, printed p. 117, and its two-factor case, Theorem 18.4, does not cover an arbitrary index set. Its inverse on $S$ is the restriction of $\pi_{\alpha}$, which is continuous, the projections of a product being continuous, as the proof of the same theorem records; so $i$ is a homeomorphism onto $S$ and an imbedding.
:::

:::

::: {.pf-step #hausdorff-regular}
If the product is Hausdorff, or regular, then so is $X_{\alpha}$.

::: pf-proof
$S$ is a subspace of the product, and subspaces of Hausdorff spaces are Hausdorff and subspaces of regular spaces are regular (Theorem 31.2). Since $X_{\alpha}$ is homeomorphic with $S$ by step [](#slice){.pf-ref}, it has the same property.
:::

:::

::: {.pf-step #normal}
If the product is normal, then so is $X_{\alpha}$.

:::: pf-proof

::: {.pf-step #slice-closed}
$S$ is closed in the product.

::: pf-proof
A normal space is $T_{1}$ and hence Hausdorff, and by step [](#hausdorff-regular){.pf-ref} each factor $X_{\beta}$ is Hausdorff as well, so each singleton $\{a_{\beta}\}$ is closed in $X_{\beta}$. Then
$$
S=\bigcap_{\beta\ne\alpha}\pi_{\beta}^{-1}\big(\{a_{\beta}\}\big)
$$
is an intersection of preimages of closed sets under the continuous maps $\pi_{\beta}$, hence closed.
:::

:::

::: {.pf-step}
$X_{\alpha}$ is normal.

::: pf-proof
A closed subspace of a normal space is normal (Exercise 32.1), so $S$ is normal; by step [](#slice){.pf-ref} $X_{\alpha}$ is homeomorphic with $S$, hence normal.
:::

:::

:::

:::

::: {.pf-step}
The property passes to every factor.

::: pf-proof
Steps [](#hausdorff-regular){.pf-ref} and [](#normal){.pf-ref} cover the three cases, and $\alpha$ was arbitrary.
:::

:::

:::
:::
