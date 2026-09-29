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
---

::: {.problem}
Let $X$ be homotopy equivalent to a finite simplicial complex and let $Y$ be homotopy equivalent to a finite or countably infinite simplicial complex.
Using the simplicial approximation theorem, show that there are at most countably many homotopy classes of maps $X \to Y$.
:::

::: {.solution}
Choose homotopy equivalences
\[
X\simeq K,
\qquad
Y\simeq L,
\]
where $K$ is a finite simplicial complex and $L$ is finite or countable.

::: pf

::: pf-step

For each $r\ge0$, there are only countably many simplicial maps
\[
\operatorname{sd}^rK\to L.
\]

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
\[
[X,Y]\cong[K,L].
\]
By steps [](#s2){.pf-ref} and [](#s3){.pf-ref} the latter set is at most countable.

:::

:::

:::

:::
