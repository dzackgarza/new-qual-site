---
schema: qual/card@1
id: P-JOGPB
kind: problem
title: $\lim_{r\to 0}\int_{\gamma_r}f=iA\beta_0$ when $(z-a)f(z)\to A$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Laurent Series
  - Poles
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
---

::: {.problem}
Assume $f$ is continuous in the region:
$$
0 < \abs{z-a} \leq R,\quad 0 \leq \Arg(z-a) \leq \beta_0 \qquad \beta_0\in (0, 2\pi]
$$
and the following limit exists:
$$
\lim_{z\to a}(z-a)f(z) = A
.$$
Show that
$$
\lim_{r \rightarrow 0} \int_{\gamma_r} f(z)\, dz = i A \beta_0,
$$
where
$$
\gamma_r \coloneqq \{ z \mid z = a + r e^{it},\ 0 \leq t \leq \beta_0 \}.
$$
:::

::: {.solution}
Let $S$ be the region in the statement, and let $g(z) = (z-a)f(z) - A$ on $S$, so that $g(z) \to 0$ as $z \to a$ and $f(z) = \frac{A}{z-a} + \frac{g(z)}{z-a}$.

::: pf

::: {.pf-step #main-term}
$\int_{\gamma_r} \frac{A}{z-a}\, dz = iA\beta_0$ for every $0 < r \leq R$.

::: pf-proof
With $z = a + re^{it}$ and $dz = ire^{it}\,dt$,
$$
\int_{\gamma_r} \frac{A}{z-a} \, dz = \int_0^{\beta_0} \frac{A}{r e^{it}}\, i r e^{it} \, dt = i A \beta_0.
$$
:::

:::

::: {.pf-step #error-term}
$\int_{\gamma_r} \frac{g(z)}{z-a}\, dz \to 0$ as $r \to 0$.

::: pf-proof
Let $\varepsilon > 0$ and choose $0 < \delta \leq R$ with $\abs{g(z)} < \varepsilon/\beta_0$ for $z \in S$, $\abs{z-a} < \delta$.
For $0 < r < \delta$, the arc $\gamma_r$ lies in $S$, has length $r\beta_0$, and carries $\abs{g(z)/(z-a)} < \varepsilon/(\beta_0 r)$, so
$$
\abs{\int_{\gamma_r} \frac{g(z)}{z-a} \, dz} \leq \frac{\varepsilon}{\beta_0 r}\cdot r\beta_0 = \varepsilon.
$$
:::

:::

::: pf-step
$\lim_{r \to 0} \int_{\gamma_r} f(z)\,dz = i A \beta_0$.

::: pf-proof
$\int_{\gamma_r} f(z)\,dz = iA\beta_0 + \int_{\gamma_r} \frac{g(z)}{z-a}\,dz$ by step [](#main-term){.pf-ref}, and the last term tends to $0$ by step [](#error-term){.pf-ref}.
:::

:::

:::
:::
