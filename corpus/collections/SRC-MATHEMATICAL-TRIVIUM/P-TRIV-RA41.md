---
schema: qual/card@1
id: P-TRIV-RA41
kind: problem
title: Components of $\nabla\log\frac1r$ in Cartesian, cylindrical and spherical coordinates
classification:
  areas: [real-analysis]
  topics:
  - Gradient
  - Curvilinear Coordinates
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 41, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed a stray extraction digit against Real Analysis Problem 41 on page 11 of the source PDF.
---

::: {.problem}
Consider the vector field $\vec{A} = \vec{\nabla}\log\frac{1}{r}$, where $r = \sqrt{x^2 + y^2 + z^2}$.
Write the components of this field

(a) in Cartesian coordinates $(x, y, z)$,

(b) in cylindrical coordinates $(r, \phi, z)$,

(c) in spherical coordinates $(r, \theta, \phi)$.
:::

::: {.remark}
The source uses $r$ both for the Euclidean distance
$\sqrt{x^2+y^2+z^2}$ and for the cylindrical radial coordinate. In the
solution, write
$$
R=\sqrt{x^2+y^2+z^2}
$$
for the Euclidean distance and $\rho$ for the cylindrical radius.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Since
$$
\log\frac1R=-\log R,
$$
one has
$$
\nabla\log\frac1R
=
-\frac1R\nabla R.
$$


::: pf-proof

Apply the chain rule to $-\log R$.

:::

:::

::: {.pf-step #s1-2}

In Cartesian coordinates,
$$
\nabla R
=
\left(
\frac{x}{R},
\frac{y}{R},
\frac{z}{R}
\right).
$$


::: pf-proof

Differentiate
$$
R=(x^2+y^2+z^2)^{1/2}
$$
with respect to $x,y,z$.

:::

:::

::: {.pf-step #s1-3}

Therefore the Cartesian components are
$$
\boxed{
\vec A
=
\left(
-\frac{x}{R^2},
-\frac{y}{R^2},
-\frac{z}{R^2}
\right).
}
$$


::: pf-proof

Substitute step [](#s1-2){.pf-ref} into step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Part (a) follows.


::: pf-proof

This is step [](#s1-3){.pf-ref}.

:::

:::

::: pf-step

In cylindrical coordinates,
$$
x=\rho\cos\phi,
\qquad
y=\rho\sin\phi,
\qquad
R=\sqrt{\rho^2+z^2}.
$$


::: pf-proof

These are the standard cylindrical-coordinate relations.

:::

:::

::: {.pf-step #s1-6}

The function $\log(1/R)$ is independent of $\phi$, and
$$
\frac{\partial}{\partial\rho}
\log\frac1R
=
-\frac{\rho}{\rho^2+z^2},
$$
$$
\frac{\partial}{\partial z}
\log\frac1R
=
-\frac{z}{\rho^2+z^2}.
$$


::: pf-proof

Since
$$
\log\frac1R
=
-\frac12\log(\rho^2+z^2),
$$
differentiate with respect to $\rho$ and $z$.

:::

:::

::: {.pf-step #s1-7}

Hence the cylindrical components are
$$
\boxed{
(A_\rho,A_\phi,A_z)
=
\left(
-\frac{\rho}{\rho^2+z^2},
0,
-\frac{z}{\rho^2+z^2}
\right).
}
$$


::: pf-proof

For a scalar function $f(\rho,\phi,z)$,
$$
\nabla f
=
e_\rho\frac{\partial f}{\partial\rho}
+
e_\phi\frac1\rho\frac{\partial f}{\partial\phi}
+
e_z\frac{\partial f}{\partial z}.
$$
Use step [](#s1-6){.pf-ref} and $\partial f/\partial\phi=0$.

:::

:::

::: {.pf-step #s1-8}

Part (b) follows.


::: pf-proof

This is step [](#s1-7){.pf-ref}.

:::

:::

::: pf-step

In spherical coordinates, the scalar function depends only on the radial
coordinate:
$$
\log\frac1R=-\log R.
$$


::: pf-proof

The Euclidean distance from the origin is precisely the spherical radial
coordinate.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\frac{\partial}{\partial R}
\log\frac1R
=
-\frac1R,
$$
while both angular derivatives vanish.


::: pf-proof

Differentiate $-\log R$ and note that there is no dependence on
$\theta$ or $\phi$.

:::

:::

::: {.pf-step #s1-11}

Hence the spherical components are
$$
\boxed{
(A_R,A_\theta,A_\phi)
=
\left(
-\frac1R,
0,
0
\right).
}
$$


::: pf-proof

Use the standard spherical-coordinate gradient formula and step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

Part (c) follows.


::: pf-proof

This is step [](#s1-11){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} and [](#s1-8){.pf-ref}, and [](#s1-12){.pf-ref} give the components in Cartesian, cylindrical,
and spherical coordinates.

:::

:::

:::
