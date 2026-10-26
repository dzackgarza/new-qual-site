---
schema: qual/card@1
id: P-TRIV-RA44
kind: problem
title: Electric field on the axis of a charged ring and a charged disk
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 44, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
The electric field $\vec { E }$ created by a point charge q at a certain distance from it r in vacuum is given by $\vec { E } = k _ { e } q \frac { \vec { r } } { r ^ { 3 } }$ , where $k _ { e }$ is a constant.

(a) Consider the charged ring of radius R with the linear charge density $\frac { d q } { d l } \equiv \rho .$ Find the total magnitude of the electric field created by this ring at a distance d from its center along the axis orthogonal to it.

(b) Consider the charged disk of radius R with surface charge density $\frac { d q } { d A } \equiv \sigma$ Find the total magnitude of the electric field created by this disk at a distance d from its center along the axis orthogonal to it.
Investigate the limit $R \to \infty$
:::

Assume the observation point lies a distance $d>0$ from the center along the
positive symmetry axis.

::: pf

::: pf-step

For the ring, every charge element is at distance
$$
s=\sqrt{R^2+d^2}
$$
from the observation point.


::: pf-proof

The ring lies in a plane perpendicular to the axis. The radial displacement in
that plane has length $R$, while the axial displacement has length $d$.
Pythagoras gives the formula.

:::

:::

::: pf-step

The field contribution of a ring element $dq$ has axial component
$$
dE_z
=
k_e
\frac{d\,dq}{(R^2+d^2)^{3/2}}.
$$


::: pf-proof

The magnitude of the field from $dq$ is
$$
k_e\frac{dq}{s^2}.
$$
The cosine of the angle between the displacement vector and the symmetry axis
is $d/s$. Thus
$$
dE_z
=
k_e\frac{dq}{s^2}\frac d s
=
k_e\frac{d\,dq}{s^3}.
$$
Use step <1>1.

:::

:::

::: pf-step

The transverse components cancel around the ring.


::: pf-proof

For every charge element at one point of the ring there is an opposite element
whose field has the opposite transverse component and the same axial
component.

:::

:::

::: pf-step

The total charge of the ring is
$$
Q=2\pi R\rho.
$$


::: pf-proof

The circumference is $2\pi R$ and the linear charge density is $\rho$.

:::

:::

::: pf-step

Hence the electric-field magnitude on the axis is
$$
\boxed{
E_{\mathrm{ring}}(d)
=
\frac{2\pi k_e\rho R,d}
{(R^2+d^2)^{3/2}}.
}
$$


::: pf-proof

Integrate step <1>2 over the ring. Since its coefficient is constant,
$$
E_z
=
k_e\frac d{(R^2+d^2)^{3/2}}
\int dq.
$$
Use step <1>4 and step <1>3.

:::

:::

::: pf-step

Part (a) follows.


::: pf-proof

This is step <1>5.

:::

:::

::: pf-step

For the disk, decompose it into concentric rings of radius $r$ and
thickness $dr$. Such a ring has charge
$$
dq
=
2\pi r\sigma\,dr.
$$


::: pf-proof

The area of the thin annulus is
$$
2\pi r\,dr,
$$
and multiplying by surface charge density $\sigma$ gives the charge.

:::

:::

::: pf-step

The axial field from this annulus is
$$
dE_z
=
2\pi k_e\sigma d
\frac{r\,dr}{(r^2+d^2)^{3/2}}.
$$


::: pf-proof

Apply the ring formula from step <1>2 with radius $r$ and charge from step
<1>7.

:::

:::

::: pf-step

Therefore
$$
E_{\mathrm{disk}}(d)
=
2\pi k_e\sigma d
\int_0^R
\frac{r\,dr}{(r^2+d^2)^{3/2}}.
$$


::: pf-proof

Integrate the annular contributions from step <1>8 over all radii in the disk.

:::

:::

::: pf-step

The radial integral satisfies
$$
\int_0^R
\frac{r\,dr}{(r^2+d^2)^{3/2}}
=
\frac1d
-
\frac1{\sqrt{R^2+d^2}}.
$$


::: pf-proof

Set
$$
u=r^2+d^2,
\qquad
du=2r\,dr.
$$
Then
$$
\int
\frac{r\,dr}{(r^2+d^2)^{3/2}}
=
-\frac1{\sqrt{r^2+d^2}}.
$$
Evaluate between $0$ and $R$, using $d>0$.

:::

:::

::: pf-step

Hence
$$
\boxed{
E_{\mathrm{disk}}(d)
=
2\pi k_e\sigma
\left(
1
-
\frac{d}{\sqrt{R^2+d^2}}
\right).
}
$$


::: pf-proof

Substitute step <1>10 into step <1>9.

:::

:::

::: pf-step

As $R\to\infty$,
$$
\boxed{
E_{\mathrm{disk}}(d)
\longrightarrow
2\pi k_e\sigma.
}
$$


::: pf-proof

Since
$$
\frac d{\sqrt{R^2+d^2}}
\longrightarrow0,
$$
the result follows from step <1>11.

:::

:::

::: pf-step

Part (b) follows.


::: pf-proof

Steps <1>11--<1>12 give the disk field and its infinite-radius limit.

:::

:::

::: pf-qed

Steps <1>6 and <1>13 establish parts (a) and (b), respectively.

:::

:::
