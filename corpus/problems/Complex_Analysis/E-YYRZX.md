---
schema: qual/card@1
id: E-YYRZX
kind: problem
title: $\int_\RR e^{x/2}/(1+e^x)\,dx$ by a rectangular contour
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: {.exercise}
Compute
$$
I \coloneqq \int_\RR \frac{e^{x/2}}{1+e^x}\,dx.
$$
:::

::: {.solution}
Let $f(z)\coloneqq\dfrac{e^{z/2}}{1+e^z}$ and let $\Gamma_R$ be the positively oriented boundary of the rectangle with vertices $\pm R$ and $\pm R + 2\pi i$: the bottom edge $H_+$ on $\RR$, the top edge $H_-$ on $\RR + 2\pi i$, and the vertical sides $V_\pm$ at $\Re z = \pm R$.

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-21_21-25-04.png)

::: pf

::: {.pf-step #horizontal}
$\displaystyle\int_{H_+}f + \int_{H_-}f = 2\int_{-R}^R f(x)\,dx$.

::: pf-proof
$f(z+2\pi i) = e^{i\pi}f(z) = -f(z)$, and $H_-$ is traversed from $R+2\pi i$ to $-R+2\pi i$, so $\int_{H_-}f = -\int_{-R}^R f(x+2\pi i)\,dx = \int_{-R}^R f(x)\,dx$.
:::

:::

::: {.pf-step #vertical}
$\displaystyle\int_{V_\pm}f\to0$ as $R\to\infty$.

::: pf-proof
Each side has length $2\pi$.
On $V_+$, $\abs{f(R+it)}\le\dfrac{e^{R/2}}{e^R-1}$, and on $V_-$, $\abs{f(-R+it)}\le\dfrac{e^{-R/2}}{1-e^{-R}}$; both bounds are $O(e^{-R/2})$.
:::

:::

::: {.pf-step #residue}
The only pole of $f$ inside $\Gamma_R$ is $i\pi$, with $\operatorname{Res}_{z=i\pi}f = -i$.

::: pf-proof
$1+e^z = 0$ exactly when $z = (2k+1)\pi i$ with $k\in\ZZ$, and only $k=0$ lies in $0<\Im z<2\pi$.
The zero is simple, so the residue is $\dfrac{e^{z/2}}{e^z}\Big|_{z=i\pi} = \dfrac{i}{-1}$.
:::

:::

::: pf-step
$I = \boxed{\pi}$.

::: pf-proof
By the residue theorem and step [](#residue){.pf-ref}, $\oint_{\Gamma_R}f = 2\pi i\cdot(-i) = 2\pi$ for $R>0$.
Letting $R\to\infty$, steps [](#horizontal){.pf-ref} and [](#vertical){.pf-ref} give $2I = 2\pi$; the integral $I$ converges absolutely since $f(x) = O(e^{-\abs x/2})$.
:::

:::

:::

:::
