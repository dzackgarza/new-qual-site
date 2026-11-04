---
schema: qual/card@1
id: E-HAT-3.3-30
kind: problem
title: Boundary of orientable manifold is orientable
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 30; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 30; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: in a collar the local orientation module of $M$ splits as the tensor product
    of the local orientation module of $\partial M$ with the orientation module of the interval
    factor, and dividing by the interval generator gives boundary orientations that agree on
    overlaps.
---

::: {.problem}
Show that the boundary of an $R$-orientable manifold is also $R$-orientable.
:::

::: {.solution}
Let $c:\partial M\times[0,\varepsilon)\to M$ be a collar. At a point $(x,t)$ with $t>0$, the local homology product isomorphism identifies the orientation module of the interior of $M$ with
$$
H_{n-1}(\partial M,\partial M\setminus\{x\};R)
\otimes_R H_1((0,\varepsilon),(0,\varepsilon)\setminus\{t\};R).
$$
The increasing coordinate on $(0,\varepsilon)$ gives a consistent generator of the second factor. Divide the given local $R$-orientation of $M$ by this generator to obtain a generator of $H_{n-1}(\partial M,\partial M\setminus\{x\};R)$.

The product isomorphism is natural under restriction to smaller collar charts. Since the local orientations of $M$ agree on overlaps, the resulting boundary generators agree on overlaps as well. They therefore define an $R$-orientation of $\partial M$.
:::
