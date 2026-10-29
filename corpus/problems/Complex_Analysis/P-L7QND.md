---
schema: qual/card@1
id: P-L7QND
kind: problem
title: Constructing a harmonic conjugate by a path-independent integral
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
relations: []
review: draft
---

::: {.problem}
Let $u$ be harmonic on an open disk of radius $R>0$, with continuous second partial derivatives. Fix $(a,b)$ in the disk and define
$$
v(x,y)=\int_{(a,b)}^{(x,y)}(-u_y\,dx+u_x\,dy).
$$

(a) Show that the integral is path-independent.

(b) Show that $u+iv$ is analytic.

(c) Show that $v$ is harmonic.
:::

::: {.solution}
Let $\eta=-u_y\,dx+u_x\,dy$, a one-form with continuously differentiable coefficients on the disk.

::: pf

::: {.pf-step #path-independent}
(a) The integral of $\eta$ is path-independent in the disk.

::: pf-proof
$\eta$ is closed: $\frac{\partial(-u_y)}{\partial y} =-u_{yy}=u_{xx} =\frac{\partial u_x}{\partial x}$, by $u_{xx}+u_{yy}=0$.
A closed $C^1$ one-form on a disk is exact, by the Poincaré lemma, so its line integrals depend only on the endpoints.
:::

:::

::: {.pf-step #cauchy-riemann}
(b) $v_x=-u_y$ and $v_y=u_x$, and $u+iv$ is analytic.

::: pf-proof
By step [](#path-independent){.pf-ref}, $v(x+h,y) - v(x,y) = \int_x^{x+h} -u_y(t,y)\,dt$ along a horizontal segment, so $v_x = -u_y$; a vertical segment gives $v_y = u_x$.
These are the Cauchy--Riemann equations for $u + iv$, whose partial derivatives are continuous, so $u+iv$ is analytic.
:::

:::

::: pf-step
(c) $v$ is harmonic.

::: pf-proof
By step [](#cauchy-riemann){.pf-ref}, $v$ has continuous second partial derivatives and $v_{xx}+v_{yy}=-u_{yx}+u_{xy}=0$.
:::

:::

:::
:::
