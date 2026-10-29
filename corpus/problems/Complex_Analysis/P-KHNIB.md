---
schema: qual/card@1
id: P-KHNIB
kind: problem
title: $\int_{\RR}\frac{dx}{1+x^4}$ and the poles of $\frac{1}{1+z^4}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Poles
relations: []
review: draft
---

::: {.problem}
Evaluate the integral
$$
\int_\RR {dx \over 1 + x^4}
.$$

What are the poles of ${1\over 1 + z^4}$ ?
:::

::: {.solution}
Let $F(z)=\frac1{1+z^4}$.

::: pf

::: {.pf-step #poles}
The poles of $F$ are the simple poles $\boxed{e^{i\pi/4},\ e^{3i\pi/4},\ e^{5i\pi/4},\ e^{7i\pi/4}}$, and $\operatorname{Res}(F;\zeta) = -\zeta/4$ at each.

::: pf-proof
They are the four distinct roots of $z^4=-1=e^{i\pi}$.
Each is simple because the derivative $4z^3$ does not vanish there, and $\operatorname{Res}(F;\zeta)=\frac1{4\zeta^3} = \frac{\zeta}{4\zeta^4} = -\frac{\zeta}{4}$.
:::

:::

::: pf-step
$$
\int_{-\infty}^{\infty}\frac{dx}{1+x^4} =\boxed{\frac{\pi}{\sqrt2}}.
$$

::: pf-proof
Integrate $F$ over the boundary of the upper half-disc of radius $R > 1$.
On the arc, $\abs{F} \leq \frac{1}{R^4 - 1}$, so the arc integral is at most $\frac{\pi R}{R^4-1} \to 0$.
The enclosed poles are $e^{i\pi/4}$ and $e^{3i\pi/4}$, so by step [](#poles){.pf-ref} and the residue theorem the integral is
$$
2\pi i\cdot\left(-\frac{e^{i\pi/4}+e^{3i\pi/4}}{4}\right) = 2\pi i \cdot\left(-\frac{i\sqrt2}{4}\right) = \frac{\pi}{\sqrt2}.
$$
:::

:::

:::
:::
