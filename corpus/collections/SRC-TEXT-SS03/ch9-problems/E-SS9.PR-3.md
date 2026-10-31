---
schema: qual/card@1
id: E-SS9.PR-3
kind: problem
title: Inversion of an elliptic integral by the Weierstrass function
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Elliptic Integrals
relations: []
review: draft
---

::: {.exercise}
Let $\Omega$ be a simply connected domain excluding the three roots of $4z^3-g_2z-g_3$. Fix $\omega_0\in\Omega$ and define
$$
I(\omega)=\int_{\omega_0}^{\omega}
\frac{dz}{\sqrt{4z^3-g_2z-g_3}},\qquad \omega\in\Omega.
$$
Show that an inverse of $I$ is given by $\wp(z+\alpha)$ for some constant $\alpha$; that is, $I(\wp(z+\alpha))=z$ for an appropriate $\alpha$.
:::

::: {.hint}
Show that $\bigl(I(\wp(z+\alpha))\bigr)'=\pm1$ and use that $\wp$ is even.
:::

::: {.remark}
The inverse identity is local: it holds on a neighborhood where $\wp(z+\alpha)$ takes values in $\Omega$ and the chosen branch of the square root gives the required sign. The statement does not specify a global domain for the inverse.
:::
