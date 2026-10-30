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
The electric field $\vec{E}$ created by a point charge $q$ at a certain distance from it $r$ in vacuum is given by $\vec{E} = k_e q\frac{\vec{r}}{r^3}$, where $k_e$ is a constant.

(a) Consider the charged ring of radius $R$ with the linear charge density $\frac{dq}{dl} \equiv \rho$. Find the total magnitude of the electric field created by this ring at a distance $d$ from its center along the axis orthogonal to it.

(b) Consider the charged disk of radius $R$ with surface charge density $\frac{dq}{dA} \equiv \sigma$. Find the total magnitude of the electric field created by this disk at a distance $d$ from its center along the axis orthogonal to it. Investigate the limit $R \to \infty$.
:::

::: {.solution}

Assume the observation point lies a distance $d>0$ from the center along the
positive symmetry axis.

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

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
Use step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The transverse components cancel around the ring.


::: pf-proof

For every charge element at one point of the ring there is an opposite element
whose field has the opposite transverse component and the same axial
component.

:::

:::

::: {.pf-step #s1-4}

The total charge of the ring is
$$
Q=2\pi R\rho.
$$


::: pf-proof

The circumference is $2\pi R$ and the linear charge density is $\rho$.

:::

:::

::: {.pf-step #s1-5}

Hence the electric-field magnitude on the axis is
$$
\boxed{
E_{\mathrm{ring}}(d)
=
\frac{2\pi k_e\rho R\,d}
{(R^2+d^2)^{3/2}}.
}
$$


::: pf-proof

Integrate step [](#s1-2){.pf-ref} over the ring. Since its coefficient is constant,
$$
E_z
=
k_e\frac d{(R^2+d^2)^{3/2}}
\int dq.
$$
Use step [](#s1-4){.pf-ref} and step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Part (a) follows.


::: pf-proof

This is step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

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

::: {.pf-step #s1-8}

The axial field from this annulus is
$$
dE_z
=
2\pi k_e\sigma d
\frac{r\,dr}{(r^2+d^2)^{3/2}}.
$$


::: pf-proof

Apply the ring formula from step [](#s1-2){.pf-ref} with radius $r$ and charge from step
[](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
E_{\mathrm{disk}}(d)
=
2\pi k_e\sigma d
\int_0^R
\frac{r\,dr}{(r^2+d^2)^{3/2}}.
$$


::: pf-proof

Integrate the annular contributions from step [](#s1-8){.pf-ref} over all radii in the disk.

:::

:::

::: {.pf-step #s1-10}

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

::: {.pf-step #s1-11}

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

Substitute step [](#s1-10){.pf-ref} into step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

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
the result follows from step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

Part (b) follows.


::: pf-proof

Steps [](#s1-11){.pf-ref} through [](#s1-12){.pf-ref} give the disk field and its infinite-radius limit.

:::

:::

::: pf-qed

Steps [](#s1-6){.pf-ref} and [](#s1-13){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
