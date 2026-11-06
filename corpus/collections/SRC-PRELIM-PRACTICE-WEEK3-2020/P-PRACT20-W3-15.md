---
schema: qual/card@1
id: P-PRACT20-W3-15
kind: problem
title: Plane through the origin perpendicular to the intersection line of two planes
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
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the line name ell lost as a backtick and the unit vectors in the displayed determinant, checked against Week3_solns.pdf (Problem 15).
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 5 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem names the same two planes and the same required plane, and the printed solution gives x = z
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's cross product of the two normals is transcribed, with the direction divided by 2, and the plane equation read off from the normal and the origin, plus the closing computation of the line itself.
---

::: {.problem}
Let $\ell$ be the line of intersection for the planes $x + y + z = 3$ and $x - y + z = 5$. Find the equation for the plane containing $(0, 0, 0)$ and perpendicular to $\ell$.
:::

::: {.solution}

Let $\ell$ be the intersection of the planes $x+y+z=3$ and $x-y+z=5$, and seek
the plane through the origin perpendicular to $\ell$.

::: pf

::: {.pf-step #direction}

$\ell$ has direction $(2,0,-2)$, so its direction is parallel to $(1,0,-1)$.

::: pf-proof

The two planes have normal vectors $n_1=(1,1,1)$ and $n_2=(1,-1,1)$, and
$\ell$ lies in both, so its direction is orthogonal to both normals. The cross
product $n_1\times n_2=\big(1\cdot1-1\cdot(-1),\ 1\cdot1-1\cdot1,\
1\cdot(-1)-1\cdot1\big)=(2,0,-2)$ is nonzero and orthogonal to both, so it
spans the direction of the intersection line; dividing by $2$ gives
$(1,0,-1)$.

:::

:::

::: {.pf-step #normal}

The required plane has normal $(2,0,-2)$, hence equation $\boxed{x=z}$.

::: pf-proof

A plane perpendicular to $\ell$ has $\ell$'s direction as a normal vector, so
its normal is $(2,0,-2)$, and passing through the origin its equation is
$2x+0y-2z=0$, that is $x=z$. Conversely $x-z=0$ is a plane with normal
$(1,0,-1)\parallel(2,0,-2)$, so it is perpendicular to $\ell$ and contains the
origin. The line $\ell$ itself consists of the points with $x+y+z=3$,
$x-y+z=5$, e.g. solving: subtracting gives $2y=-2$, $y=-1$, and then $x+z=4$.

:::

:::

:::


:::
