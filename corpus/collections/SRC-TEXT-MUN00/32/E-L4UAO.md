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
---

::: {.exercise}

Show that if $\prod X_\alpha$ is Hausdorff, or regular, or normal, then so is $X_\alpha$.
(Assume that each $X_\alpha$ is nonempty.)
:::

::: {.solution}
Fix an index $\alpha$, and choose basepoints $a_\beta\in X_\beta$ for every $\beta\ne\alpha$. The map
$$
i:X_\alpha\to\prod_\beta X_\beta,
\qquad
 i(x)_\alpha=x,\quad i(x)_\beta=a_\beta\ (\beta\ne\alpha)
$$
is a homeomorphism from $X_\alpha$ onto the corresponding slice $S$.

Hausdorffness and regularity are hereditary to subspaces, so if the product is Hausdorff or regular, then $S$, hence $X_\alpha$, has the same property.

If the product is normal, then it is $T_1$, so every singleton $\{a_\beta\}$ is closed. Hence
$$
S=\bigcap_{\beta\ne\alpha}\pi_\beta^{-1}(\{a_\beta\})
$$
is closed in the product. Closed subspaces of normal spaces are normal. Therefore $X_\alpha$ is normal as well.
:::
