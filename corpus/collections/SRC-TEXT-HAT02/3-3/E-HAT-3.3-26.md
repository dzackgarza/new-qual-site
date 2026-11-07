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
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Replaced the undeclared symbol u with the orientation class nu declared in the solution, so
    the two top-class formulas now read ab = cd = nu. Rechecked the connected-sum collapse maps,
    the cross-summand vanishing, and the zero squares; no change to the product computation and
    no new published-solution claim is made.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Reorganized the same verified computation into STYLE-08 steps: the collapse maps give
    ab = cd = nu, cross-summand products and the squares a^2 and c^2 vanish, and all remaining
    positive-degree products are excluded by the summands or by degree count.
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

The connected-sum collapse maps to the two summands preserve the top class.

::: pf

::: {.pf-step #top-products}
Hence the product structures on the summands give
$$
a\smile b=\nu,
\qquad
c\smile d=\nu
$$
after choosing the generators compatibly with orientation.

::: pf-proof
The collapse maps preserve the top class $\nu$. Since all four degrees are even, the reversed products are the same.
:::

:::

::: pf-step
Products between classes coming from different connected-sum summands vanish, and
$$
a^2=c^2=0.
$$

::: pf-proof
Cross-summand products vanish. Within each product-of-spheres summand, the square of either positive-dimensional generator is zero.
:::

:::

::: pf-step
The only nonzero positive-dimensional cup products are exactly the Poincaré-dual pairings.

::: pf-proof
Every other product of positive-dimensional generators vanishes either within its summand or by degree count. Thus the complete list is
$$
\boxed{ab=cd=\nu,}
$$
which is step [](#top-products){.pf-ref}.
:::

:::

:::
:::
