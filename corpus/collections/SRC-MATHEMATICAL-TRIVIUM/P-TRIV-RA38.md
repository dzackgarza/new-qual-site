---
schema: qual/card@1
id: P-TRIV-RA38
kind: problem
title: Volume of the ball in $\RR^3$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 38, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the volume of the three-dimensional ball $B ^ { 3 }$
:::

::: {.remark}
The source does not specify a radius. The notation $B^3$ is interpreted as the
unit ball. The same computation gives the radius-$R$ formula as well.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

In spherical coordinates,
$$
dV
=
r^2\sin\theta
\,dr\,d\theta\,d\varphi.
$$


::: pf-proof

The Jacobian determinant of the spherical-coordinate map is
$$
r^2\sin\theta.
$$

:::

:::

::: {.pf-step #s1-2}

The unit ball is described by
$$
0\leq r\leq1,
\qquad
0\leq\theta\leq\pi,
\qquad
0\leq\varphi<2\pi.
$$


::: pf-proof

The radial coordinate runs from the origin to the unit sphere, while the two
angular coordinates cover all directions.

:::

:::

::: pf-step

Therefore
$$
\operatorname{Vol}(B^3)
=
\int_0^{2\pi}
\int_0^\pi
\int_0^1
r^2\sin\theta
\,dr\,d\theta\,d\varphi.
$$


::: pf-proof

Integrate the volume element from step [](#s1-1){.pf-ref} over the region from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The three one-dimensional integrals are
$$
\int_0^1 r^2\,dr
=
\frac13,
$$
$$
\int_0^\pi\sin\theta\,d\theta
=2,
$$
and
$$
\int_0^{2\pi}d\varphi
=2\pi.
$$


::: pf-proof

Evaluate each elementary integral directly.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
\operatorname{Vol}(B^3)
=
\frac{4\pi}{3}.
}
$$


::: pf-proof

Multiply the three factors from step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

More generally, a ball of radius $R$ has volume
$$
\boxed{
\frac{4\pi R^3}{3}.
}
$$


::: pf-proof

Replace the radial upper limit $1$ by $R$, so
$$
\int_0^R r^2\,dr
=
\frac{R^3}{3}.
$$
The angular integrals are unchanged.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the volume of the unit ball, and step [](#s1-6){.pf-ref} records the general
radius formula.

:::

:::

:::
