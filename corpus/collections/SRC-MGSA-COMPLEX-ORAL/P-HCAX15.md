---
schema: qual/card@1
id: P-HCAX15
kind: problem
title: Schwarz--Christoffel map from the disk to a polygon
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz--Christoffel Formula
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the statement of the formula into Lamport steps and checked it: with
    interior angles alpha_i pi = (2 - beta_i) pi the disc form is
    f'(z) = C prod (1 - z/zeta_i)^(alpha_i - 1) = C prod (1 - z/zeta_i)^(1 - beta_i), which is
    the standard formula, and the primitive gives f up to A. Added the compatibility condition
    sum beta_i = n + 2, equivalently sum (alpha_i - 1) = -2, which the card omitted and which
    the formula's validity requires; it is derived from the angle sum of the polygon. The
    angle bookkeeping is now stated with the sign made explicit: the factor contributes an
    argument change of magnitude (alpha_i - 1) pi, so the boundary turns by (1 - alpha_i) pi =
    (beta_i - 1) pi and the interior angle is pi minus that, namely (2 - beta_i) pi. The
    statement is true as printed. The collection's provenance is the examination paper only,
    so no retained solution set covers the exercise and the argument is the card's own.
---

::: {.problem}
State the formula for a conformal map from the unit disk onto the interior of a polygon whose angles are $(2-\beta_i)\pi$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #setup}
Let the polygon have $n$ vertices, in cyclic order, with interior angle $\alpha_i\pi=(2-\beta_i)\pi$ at the $i$th, and let $\zeta_1,\dots,\zeta_n\in\partial\DD$ be the corresponding prevertices, also in cyclic order. Then $\sum_{i=1}^n\beta_i=n+2$, equivalently $\sum_{i=1}^n(\alpha_i-1)=-2$.

::: pf-proof
The angle sum of an $n$-gon is $(n-2)\pi$, so $\sum_i\alpha_i\pi=(n-2)\pi$, that is $\sum_i\alpha_i=n-2$; substituting $\alpha_i=2-\beta_i$ gives $2n-\sum_i\beta_i=n-2$, which is $\sum_i\beta_i=n+2$. The second form is $\sum_i(\alpha_i-1)=\sum_i\alpha_i-n=-2$.
:::

:::

::: {.pf-step #derivative}
The Schwarz--Christoffel formula for the disc reads
$$
f'(z)=C\prod_{i=1}^{n}\left(1-\frac{z}{\zeta_i}\right)^{\alpha_i-1}
=C\prod_{i=1}^{n}\left(1-\frac{z}{\zeta_i}\right)^{1-\beta_i},
\qquad C\ne0,
$$
the powers being taken with the branches that are holomorphic on $\DD$ and equal $1$ at $z=0$.

::: pf-proof
The general Schwarz--Christoffel formula for a conformal map of the disc onto a polygon with interior angles $\alpha_i\pi$ and prevertices $\zeta_i$ gives the first product; each factor $1-z/\zeta_i$ is zero-free on the disc, so a holomorphic branch of each power exists there and is fixed by its value at $0$. The second display substitutes $\alpha_i-1=1-\beta_i$, which is the identity $\alpha_i=2-\beta_i$ of the problem.
:::

:::

::: {.pf-step #integral}
$\displaystyle f(z)=A+C\int_{z_0}^{z}\prod_{i=1}^{n}\left(1-\frac{w}{\zeta_i}\right)^{1-\beta_i}\,dw$ for constants $A,C$ and a base point $z_0\in\DD$.

::: pf-proof
$\DD$ is simply connected, so the integrand, which is holomorphic and nowhere zero on $\DD$, has a holomorphic primitive there; $f'$ equals the integrand up to the constant factor, so integrating from a fixed $z_0$ recovers $f$ up to the additive constant $A$.
:::

:::

::: {.pf-step #angles}
At the prevertex $\zeta_i$ the image boundary turns through $(1-\alpha_i)\pi=(\beta_i-1)\pi$, so the interior angle of the image is $(2-\beta_i)\pi$.

::: pf-proof
Write the factor as $(1-z/\zeta_i)^{\alpha_i-1}$. As $z$ crosses $\zeta_i$ along the boundary circle, this factor's argument changes by $\pm(\alpha_i-1)\pi$ and the other factors' arguments change continuously, so the tangent direction of the image boundary turns through the angle $(1-\alpha_i)\pi$, of magnitude $(\beta_i-1)\pi$ after substituting $\alpha_i=2-\beta_i$. The interior angle together with the turning angle makes $\pi$, so the interior angle is $\pi-(1-\alpha_i)\pi=\alpha_i\pi=(2-\beta_i)\pi$, as required.
:::

:::

::: {.pf-step}
The constants are chosen as follows: $A$ places one image point, $C$ fixes the size and rotation of the polygon, and the three real parameters of the disc automorphism are spent on the prevertices, so the data $A,C,\zeta_1,\dots,\zeta_n$ — with $\sum\beta_i=n+2$ and the $\zeta_i$ in the prescribed cyclic order — determine the map.

::: pf-proof
Composing $f$ with a disc automorphism changes the prevertices and the constants without changing the image polygon, which is why the counting is three real dimensions of freedom on both sides; the side lengths of the polygon then fix $C$ and the positions of the $\zeta_i$ in the standard way described in the Schwarz--Christoffel theory.
:::

:::

:::
:::
