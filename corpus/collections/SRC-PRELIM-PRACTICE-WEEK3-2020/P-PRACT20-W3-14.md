---
schema: qual/card@1
id: P-PRACT20-W3-14
kind: problem
title: Plane through the origin, $(2,0,0)$ and $(0,0,1)$
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Planes
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 5 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem asks for the plane through the same three points, and the printed solution gives y = 0
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's observation that all three points satisfy y = 0 is transcribed and completed by the uniqueness of the plane through three non-collinear points.
---

::: {.problem}
Find the equation of the plane containing the origin and the points $(2,0,0)$ and $(0,0,1)$.
:::

::: {.solution}

Find the affine plane through the three given points.

::: pf

::: {.pf-step #points}

All three points have second coordinate $0$.

::: pf-proof

The origin is $(0,0,0)$, the second point is $(2,0,0)$ and the third is
$(0,0,1)$; in each the $y$-coordinate is $0$.

:::

:::

::: {.pf-step #plane}

The plane is $\boxed{y=0}$.

::: pf-proof

$y=0$ is the zero set of the nonzero affine function $(x,y,z)\mapsto y$, hence
a plane; it contains all three points by step [](#points){.pf-ref}. Three
non-collinear points determine a plane, and these are non-collinear since the
two difference vectors $(2,0,0)$ and $(0,0,1)$ are linearly independent, so
$y=0$ is the plane required. It is the $xz$-plane, with normal $(0,1,0)$.

:::

:::

:::


:::
