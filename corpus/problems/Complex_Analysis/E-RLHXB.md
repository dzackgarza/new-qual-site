---
schema: qual/card@1
id: E-RLHXB
kind: problem
title: $\int_{\RR} \frac{dx}{x^4+16}$ by the Cauchy integral formula
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

::: {.exercise}
Without using the residue formula, compute
$$
\int_\RR f(x) \dx, \qquad f(x) \coloneqq {1\over x^4 + 16}.
$$
:::

::: {.solution}
The zeros of $z^4+16$ are $z_k = 2e^{i\pi(2k+1)/4}$ for $k=0,1,2,3$. Only $z_0 = \sqrt 2 + i\sqrt 2$ and $z_1 = -\sqrt 2 + i\sqrt 2$ lie in the upper half-plane.
For $R>2$ let $\Gamma_R$ be the boundary of the upper half-disc of radius $R$, positively oriented, and let $C_R$ be its semicircular arc.

::: pf

::: {.pf-step #arc}
$\int_{C_R} f(z)\dz \to 0$ as $R\to\infty$.

::: pf-proof
On $C_R$ the reverse triangle inequality gives $\abs{z^4+16}\geq R^4-16$, so
$$
\abs{\int_{C_R} f(z)\dz} \leq \frac{\pi R}{R^4-16} \to 0.
$$
:::

:::

::: {.pf-step #contour}
$\int_{\Gamma_R} f(z)\dz = \frac{2\pi i}{4z_0^3} + \frac{2\pi i}{4z_1^3}$ for $R>2$.

::: pf-proof
Small circles $\gamma_0$, $\gamma_1$ about $z_0$, $z_1$ give $\int_{\Gamma_R} f = \int_{\gamma_0} f + \int_{\gamma_1} f$ by Cauchy's theorem.
Near $z_j$ write $f(z) = g_j(z)/(z-z_j)$ with $g_j(z) = \prod_{k\neq j}(z-z_k)^{-1}$ holomorphic near $z_j$.
The Cauchy integral formula gives $\int_{\gamma_j} f = 2\pi i\, g_j(z_j)$, and $g_j(z_j) = 1/p'(z_j) = 1/(4z_j^3)$ for $p(z) = z^4+16$.
:::

:::

::: {.pf-step #value}
$\frac{2\pi i}{4z_0^3} + \frac{2\pi i}{4z_1^3} = \frac{\pi\sqrt 2}{16}$.

::: pf-proof
Since $z_j^4=-16$, $\frac{1}{4z_j^3} = \frac{z_j}{4z_j^4} = -\frac{z_j}{64}$. So the sum is $-\frac{2\pi i}{64}(z_0+z_1) = -\frac{2\pi i}{64}\cdot 2\sqrt2\, i = \frac{\pi\sqrt2}{16}$.
:::

:::

::: pf-step
$\int_\RR \frac{dx}{x^4+16} = \boxed{\frac{\pi\sqrt 2}{16}}$.

::: pf-proof
For $R>2$, $\int_{-R}^R f(x)\dx = \int_{\Gamma_R} f - \int_{C_R} f$. Let $R\to\infty$ and apply steps [](#arc){.pf-ref}, [](#contour){.pf-ref} and [](#value){.pf-ref}.
:::

:::

:::

:::
