---
schema: qual/card@1
id: E-HAT-3.3-26
kind: problem
title: Cup product on connected sums of products
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 26; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 26; it matches the printed text. The printed bracketed sentence "[See Exercise 6. The result has an evident generalization ...]" was missing and is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the computation: the collapse maps to the two summands preserve the top class, so
    $a\smile b=u$ and $c\smile d=u$; products of classes from different summands and squares of a
    single positive-degree generator on a product of spheres vanish, and the remaining products are
    impossible for degree reasons.
---

::: {.problem}
Compute the cup product structure in $H^*(S^2 \times S^8 \sharp S^4 \times S^6; \ZZ)$, and in particular show that the only nontrivial cup products are those dictated by Poincaré duality.
[See Exercise 6. The result has an evident generalization to connected sums of $S^i \times S^{n-i}$'s for fixed $n$ and varying $i$.]
:::

::: {.solution}
Let
$$
M=(S^2\times S^8)\#(S^4\times S^6)
$$
with the connected-sum orientation. In degrees strictly between $0$ and $10$, reduced cohomology is the direct sum of that of the two summands. Choose generators
$$
a\in H^2(M),\quad b\in H^8(M),\quad
c\in H^4(M),\quad d\in H^6(M),
$$
coming respectively from the $S^2,S^8,S^4,S^6$ factors, and let
$$
u\in H^{10}(M)\cong\ZZ
$$
be the orientation class.

The connected-sum collapse maps to the two summands preserve the top class. Hence the product structures on the summands give
$$
a\smile b=u,
\qquad
c\smile d=u
$$
after choosing the generators compatibly with orientation. Since all four degrees are even, the reversed products are the same.

Products between classes coming from different connected-sum summands vanish. Within each product-of-spheres summand, the square of either positive-dimensional generator is zero. Therefore
$$
a^2=c^2=0,
$$
and every other product of positive-dimensional generators vanishes for either this reason or degree reasons, except
$$
\boxed{ab=cd=u.}
$$
Thus the only nonzero positive-dimensional cup products are exactly the Poincaré-dual pairings.
:::
