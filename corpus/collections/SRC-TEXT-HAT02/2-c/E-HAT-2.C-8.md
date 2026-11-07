---
schema: qual/card@1
id: E-HAT-2.C-8
kind: problem
title: At most countably many homotopy classes of maps between simplicial spaces
classification:
  areas:
  - topology
  topics:
  - Simplicial Approximation
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.C, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the simplicial, Lefschetz-trace, or surface argument against the preceding section results.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.C Exercise 8, printed page
    184; the statement matches word for word. Proof checked: K is a finite simplicial
    complex and L finite or countable, a simplicial map from a subdivision of K is
    determined by its values on the finitely many vertices, so for each r there are
    at most countably many such maps and the union over r is countable, and every map
    K → L is homotopic to one of these by the simplicial approximation theorem
    (Theorem 2C.1, p. 179). No defect.
- event: solution-written
  by: claude
  date: 2026-11-08
  note: >-
    Makes the published argument explicit in the solution: Theorem 2C.1 on pp.178-179 supplies
    a simplicial representative after finitely many barycentric subdivisions of the finite
    domain. Each sd^rK has finitely many vertices, so there are countably many maps into L for
    each r, and the union over r is countable. Homotopy equivalences X ≃ K and Y ≃ L transfer
    this bound to [X,Y]. The source paragraph is kept with the mathematics, as in Hatcher's
    own remark that a simplicial map is determined by its vertex images.
---
---

::: {.problem}
Let $X$ be homotopy equivalent to a finite simplicial complex and let $Y$ be homotopy equivalent to a finite or countably infinite simplicial complex.
Using the simplicial approximation theorem, show that there are at most countably many homotopy classes of maps $X \to Y$.
:::

::: {.solution}
Use **Hatcher's simplicial approximation theorem, Theorem 2C.1, printed pp. 178--179**, in the form actually proved there: after finitely many barycentric subdivisions of the finite domain, every continuous map is homotopic to a simplicial map. The remaining count is the source's own vertex-map count.

Choose homotopy equivalences
$$
X\simeq K,
\qquad
Y\simeq L,
$$
where $K$ is a finite simplicial complex and $L$ is finite or countable.

::: pf

::: pf-step

For each $r\ge0$, there are only countably many simplicial maps
$$
\operatorname{sd}^rK\to L.
$$

::: pf-proof

The complex $\operatorname{sd}^rK$ has finitely many vertices, while $L$ has at most countably many vertices. A simplicial map is determined by its map on vertices. There are only countably many maps from a finite set to a countable set, hence only countably many simplicial maps.

:::

:::

::: {.pf-step #s2}

The union, over all $r\ge0$, of the sets of such simplicial maps is countable.

::: pf-proof

It is a countable union of countable sets.

:::

:::

::: {.pf-step #s3}

Every homotopy class of maps $K\to L$ is represented by one of these simplicial maps.

::: pf-proof

By the simplicial approximation theorem, every continuous map $K\to L$ is homotopic to a simplicial map after some iterated barycentric subdivision of the finite domain $K$.

:::

:::

::: pf-step

Therefore there are at most countably many homotopy classes of maps $X\to Y$.

::: pf-proof

Composition with fixed homotopy equivalences and their homotopy inverses gives a bijection
$$
[X,Y]\cong[K,L].
$$
By steps [](#s2){.pf-ref} and [](#s3){.pf-ref} the latter set is at most countable.

:::

:::

:::

:::
