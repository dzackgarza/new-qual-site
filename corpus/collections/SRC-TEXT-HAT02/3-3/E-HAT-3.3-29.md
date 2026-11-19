---
schema: qual/card@1
id: E-HAT-3.3-29
kind: problem
title: Retractions of surfaces onto graphs
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 29; the stored statement matches the current online text and diagram where applicable.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 29; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: a retraction makes $r^*$ injective into an isotropic subspace of the
    symplectic $H^1(M_g;F)$, so its dimension is at most $g$; Exercise 13 follows by retracting the
    punctured $M_h$ onto its spine of $2h$ circles, and the wedges of $k$ circles are retracted by
    collapsing the remaining loops, which kills the attaching word.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: a retraction gives $i^*r^*=\id$, so
    $r^*$ is injective; $H^2$ of a graph vanishes, so the image of $r^*$ is isotropic for the cup
    product; $H^1(M_g;F)$ is $2g$-dimensional with a nonsingular skew-symmetric pairing, so Exercise
    28 bounds an isotropic subspace by $g$; Exercise 13 follows by retracting the punctured $M_h$
    onto its spine of $2h$ circles; and the standard CW structure with attaching word
    $\prod[a_i,b_i]$ admits the collapse retraction onto the first $k$ loops, since each commutator
    factor becomes null. Added: the computation of each commutator's image in the last clause, the
    homotopy equivalence behind $H_{n-k}(M-\partial M)\cong H_{n-k}(M)$ (in the companion card), and
    the identification of $\dim H^1(X;\QQ)$ with $\rank H_1(X)$. No defect found in the statement,
    §3.3 Exercise 29. No retained solution set covers it.
---

::: {.problem}
Use the preceding problem to show that if the closed orientable surface $M_g$ of genus $g$ retracts onto a graph $X \subset M_g$, then $H_1(X)$ has rank at most $g$.
Deduce an alternative proof of Exercise 13 from this, and construct a retraction of $M_g$ onto a wedge sum of $k$ circles for each $k \leq g$.
:::

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own; the three clauses follow the printed instruction, using the symplectic structure of $H^1$ of a surface and the cup product of Exercise 28. Write $r\colon M_g\to X$ for the retraction and $i\colon X\hookrightarrow M_g$ for the inclusion.

::: pf

::: {.pf-step #injective}
For every field $F$, $r^*\colon H^1(X;F)\to H^1(M_g;F)$ is injective.

::: pf-proof
$r\circ i=\id_X$, so functoriality gives $i^*r^*=\id_{H^1(X;F)}$, and a map with a left inverse is injective.
:::

:::

::: {.pf-step #isotropic}
The image $V=r^*H^1(X;F)$ is an isotropic subspace of $H^1(M_g;F)$ for the cup-product pairing.

::: pf-proof
$X$ is a graph, so $H^2(X;F)=0$ and hence $u\smile v=0$ for all $u,v\in H^1(X;F)$. By naturality of the cup product, $r^*u\smile r^*v=r^*(u\smile v)=0$, so every two elements of $V$ pair to zero.
:::

:::

::: {.pf-step #bound}
$\dim_F H^1(X;F)\le g$, hence $\rank H_1(X)\le g$.

::: pf-proof
$H^1(M_g;F)$ is $2g$-dimensional and the cup-product pairing on it is nonsingular and skew-symmetric, since $M_g$ is a closed orientable surface. By Exercise 28, an isotropic subspace of a nonsingular skew-symmetric form on a $2g$-dimensional space has dimension at most $g$; so $\dim V\le g$, and $r^*$ is injective by step [](#injective){.pf-ref}, so $\dim H^1(X;F)\le g$. Taking $F=\QQ$ identifies $\dim H^1(X;\QQ)$ with $\rank H_1(X)$.
:::

:::

::: {.pf-step #exercise-thirteen}
There is no retraction $M_g\to M_h$ when $2h>g$.

::: pf-proof
A genus-$h$ surface with one boundary component deformation retracts onto a graph of first Betti number $2h$, a wedge of $2h$ circles. Composing that deformation retraction with a retraction $M_g\to M_h$ would give a retraction of $M_g$ onto a graph with $H_1$ of rank $2h$, which step [](#bound){.pf-ref} forbids when $2h>g$. This is the alternative proof of Exercise 13.
:::

:::

::: {.pf-step}
For every $k\le g$ there is a retraction $M_g\to\bigvee_kS^1$.

::: pf-proof
Use the standard CW structure on $M_g$ with one vertex, $1$-cells $a_1,b_1,\ldots,a_g,b_g$ and one $2$-cell attached along $\prod_i[a_i,b_i]$. Let $X_k$ be the wedge of the circles $a_1,\ldots,a_k$, and define a cellular map on the $1$-skeleton that is the identity on $a_1,\ldots,a_k$ and sends every other $1$-cell to the vertex. The attaching word maps to the product over $i$ of the images of $[a_i,b_i]$: for $i\le k$ the factor becomes $a_i\cdot1\cdot a_i^{-1}\cdot1$, which is null, and for $i>k$ both letters are sent to the vertex, so the word maps to a null loop in $X_k$. Hence the map extends over the $2$-cell, and it restricts to the identity on $X_k$, so it is a retraction. The first two clauses are steps [](#bound){.pf-ref} and [](#exercise-thirteen){.pf-ref}.
:::

:::

:::
:::
