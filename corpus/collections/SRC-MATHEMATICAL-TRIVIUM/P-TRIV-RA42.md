---
schema: qual/card@1
id: P-TRIV-RA42
kind: problem
title: Divergence, Laplacian and curl of $\nabla\frac1r$
classification:
  areas: [real-analysis]
  topics:
  - Divergence
  - Curl
  - Laplacian
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 42, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Repaired the garbled curl and div notation against Real Analysis Problem 42 on page 11 of the source PDF.
---

::: {.problem}
Consider the vector field $\vec{A} = \vec{\nabla}\frac{1}{r}$, where $r = \sqrt{x^2 + y^2 + z^2}$.

(a) Find $\mathbf{div}\,\vec{A}$, $\triangle\vec{A}$, $\mathbf{curl}\,\vec{A}$.

(b) How do the values of $\mathbf{div}\,\vec{A}$ and $\triangle\vec{A}$ depend on the choice of coordinate system?
:::

::: {.remark}
The field is classically defined on $\RR^3\setminus\{0\}$. All
differential identities below are classical identities on that domain. If one
extends the calculation distributionally across the origin, then
$$
\Delta\frac1r=-4\pi\delta_0,
$$
so the divergence acquires a point-source term at $0$.
:::

::: {.solution}

Put
$$
u(x,y,z)=\frac1r.
$$
Then
$$
\vec A=\nabla u.
$$

::: pf

::: pf-step

In Cartesian coordinates,
$$
\boxed{
\vec A
=
-\frac1{r^3}(x,y,z).
}
$$


::: pf-proof

Since
$$
r=(x^2+y^2+z^2)^{1/2},
$$
one has
$$
\frac{\partial}{\partial x}\frac1r
=
-\frac{x}{r^3},
$$
and similarly for $y,z$.

:::

:::

::: {.pf-step #s1-2}

The divergence satisfies
$$
\operatorname{div}\vec A
=
\Delta u.
$$


::: pf-proof

By definition,
$$
\operatorname{div}(\nabla u)=\Delta u.
$$

:::

:::

::: {.pf-step #s1-3}

For $r>0$,
$$
\Delta\frac1r=0.
$$


::: pf-proof

For a radial scalar function $f(r)$ in $\RR^3$,
$$
\Delta f
=
\frac1{r^2}
\frac{d}{dr}
\left(
r^2\frac{df}{dr}
\right).
$$
For $f(r)=1/r$,
$$
\frac{df}{dr}=-\frac1{r^2},
$$
so
$$
r^2\frac{df}{dr}=-1,
$$
whose derivative is zero.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{\operatorname{div}\vec A=0}
$$
for $r>0$.


::: pf-proof

Combine steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

The curl vanishes:
$$
\boxed{\operatorname{curl}\vec A=0}.
$$


::: pf-proof

Since
$$
\vec A=\nabla u
$$
and $u=1/r$ is smooth on $\RR^3\setminus\{0\}$,
$$
\nabla\times\nabla u=0.
$$

:::

:::

::: {.pf-step #s1-6}

The vector Laplacian satisfies
$$
\Delta\vec A
=
\nabla(\Delta u).
$$


::: pf-proof

In Cartesian coordinates the vector Laplacian is applied componentwise, and
partial derivatives commute on the smooth function $u$:
$$
\Delta(\nabla u)=\nabla(\Delta u).
$$

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{\Delta\vec A=0}
$$
for $r>0$.


::: pf-proof

Use step [](#s1-3){.pf-ref} in step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Part (a) follows.


::: pf-proof

Steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref}, and [](#s1-7){.pf-ref} give the divergence, curl, and vector Laplacian.

:::

:::

::: {.pf-step #s1-9}

The geometric values of
$$
\operatorname{div}\vec A
$$
and
$$
\Delta\vec A
$$
do not depend on the coordinate system.


::: pf-proof

Divergence and the Euclidean vector Laplacian are intrinsic differential
operators determined by the Euclidean metric. Their coordinate formulas change
when Cartesian coordinates are replaced by cylindrical or spherical
coordinates, but the resulting scalar or vector field is the same geometric
object.

:::

:::

::: {.pf-step #s1-10}

In particular, their values remain zero in every regular coordinate
chart on $\RR^3\setminus\{0\}$.


::: pf-proof

Steps [](#s1-4){.pf-ref} and [](#s1-7){.pf-ref} show that the geometric fields are identically zero.
Changing coordinates cannot change the zero scalar field or zero vector field.

:::

:::

::: {.pf-step #s1-11}

Part (b) follows.


::: pf-proof

Steps [](#s1-9){.pf-ref} through [](#s1-10){.pf-ref} give the requested coordinate-independence statement.

:::

:::

::: pf-qed

Steps [](#s1-8){.pf-ref} and [](#s1-11){.pf-ref} establish parts (a) and (b).

:::

:::

:::
