---
schema: qual/card@1
id: E-PMURO
kind: problem
title: Dirichlet integral $\int_0^\infty \frac{\sin x}{x}\,dx = \frac{\pi}{2}$
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
Show
$$
\int_{(0, \infty)} {\sin(x) \over x }\dx = {\pi \over 2}.
$$
:::

::: {.hint}
Integrate $e^{iz}/z$ over a semicircle in the upper half-plane indented at $0$.
:::

::: {.solution}

Let $f(z)\coloneqq e^{iz}/z$.
For $0<\varepsilon<R$, let $C_R$ be the semicircle $Re^{i\theta}$, $0\leq\theta\leq\pi$, and $c_\varepsilon$ the semicircle $\varepsilon e^{i\theta}$ traversed from $\theta=\pi$ to $\theta=0$.
The integral is the improper integral $\lim_{R\to\infty}\int_0^R$.

::: pf

::: {.pf-step #contour}
$\displaystyle\int_{\varepsilon<\abs{x}<R}\frac{e^{ix}}{x}\,dx + \int_{C_R}f + \int_{c_\varepsilon}f = 0$.

::: pf-proof
The closed contour formed by $[-R,-\varepsilon]$, $c_\varepsilon$, $[\varepsilon,R]$ and $C_R$ bounds a region on whose closure $f$ is holomorphic, so Cauchy's theorem applies.
:::

:::

::: {.pf-step #big}
$\int_{C_R}f\to0$ as $R\to\infty$.

::: pf-proof
On $C_R$, $\abs{e^{iz}}=e^{-R\sin\theta}$, and $\sin\theta\geq 2\theta/\pi$ on $[0,\pi/2]$, so
$$
\abs{\int_{C_R}f}\leq\int_0^\pi e^{-R\sin\theta}\,d\theta = 2\int_0^{\pi/2}e^{-R\sin\theta}\,d\theta\leq 2\int_0^{\pi/2}e^{-2R\theta/\pi}\,d\theta\leq\frac{\pi}{R}.
$$
:::

:::

::: {.pf-step #small}
$\int_{c_\varepsilon}f\to-\pi i$ as $\varepsilon\to0$.

::: pf-proof
$f(z) = \frac1z + h(z)$ with $h$ entire, so $\int_{c_\varepsilon}h\to0$, and $\int_{c_\varepsilon}\frac{dz}{z} = \int_\pi^0 i\,d\theta = -\pi i$.
:::

:::

::: pf-step
$\displaystyle\int_0^\infty\frac{\sin x}{x}\,dx = \boxed{\frac{\pi}{2}}$.

::: pf-proof
Since $\cos x/x$ is odd and $\sin x/x$ is even, $\int_{\varepsilon<\abs{x}<R}\frac{e^{ix}}{x}\,dx = 2i\int_\varepsilon^R\frac{\sin x}{x}\,dx$.
By steps [](#contour){.pf-ref}, [](#big){.pf-ref} and [](#small){.pf-ref}, letting $\varepsilon\to0$ and $R\to\infty$ gives $2i\int_0^\infty\frac{\sin x}{x}\,dx = \pi i$; the integrand is continuous at $0$, so the limit $\varepsilon\to0$ is harmless.
:::

:::

:::

:::

::: {.remark title="Variations"}
The integrand is even, so $\int_\RR \frac{\sin x}{x}\,dx=\pi$.
:::
