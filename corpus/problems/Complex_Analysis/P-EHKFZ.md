---
schema: qual/card@1
id: P-EHKFZ
kind: problem
title: Area of $f(\{r<\abs{z}<R\})$ is $\pi\sum_{n=-\infty}^\infty n\abs{c_n}^2(R^{2n}-r^{2n})$
  for a univalent Laurent series
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Conformal Maps
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $f(z) = \sum_{n=-\infty}^\infty c_n z^n$ be analytic and one-to-one (univalent) in the open annulus $r_0 < \abs{z} < R_0$.
For $r_0 < r < R < R_0$, let $D(r, R) = \{z \in \CC \mid r < \abs{z} < R\}$ be the concentric sub-annulus.
Prove that the area $S$ of the image domain $f(D(r, R))$ is finite and given by the series formula:
$$S = \pi \sum_{n=-\infty}^\infty n \abs{c_n}^2 (R^{2n} - r^{2n}).$$
:::

::: {.solution}

::: pf

::: {.pf-step #area-integral}
$S=\iint_{D(r,R)}\abs{f'(z)}^2\,dA(z)<\infty$.

::: pf-proof
$f$ is univalent and holomorphic, so its real Jacobian determinant is $\abs{f'}^2$ and the change-of-variables formula gives the identity.
$\overline{D(r,R)}$ is a compact subset of the annulus of holomorphy, so $\abs{f'}^2$ is bounded there.
:::

:::

::: {.pf-step #parseval}
For $r\le\rho\le R$, $\int_0^{2\pi}\abs{f'(\rho e^{i\theta})}^2\,d\theta=2\pi\sum_{n\in\ZZ}n^2\abs{c_n}^2\rho^{2n-2}$.

::: pf-proof
The Laurent series may be differentiated termwise, $f'(z)=\sum_{n\in\ZZ}nc_nz^{n-1}$, and on the circle $\abs{z}=\rho$ this is a Fourier series with coefficients $nc_n\rho^{n-1}$; apply Parseval's identity.
:::

:::

::: pf-step
$S=\pi\sum_{n\in\ZZ}n\abs{c_n}^2(R^{2n}-r^{2n})$.

::: pf-proof
By steps [](#area-integral){.pf-ref} and [](#parseval){.pf-ref} in polar coordinates, and Tonelli's theorem for the nonnegative terms,
$$
S=2\pi\sum_{n\in\ZZ}n^2\abs{c_n}^2\int_r^R\rho^{2n-1}\,d\rho=\pi\sum_{n\in\ZZ}n\abs{c_n}^2(R^{2n}-r^{2n}),
$$
where the $n=0$ term is $0$.
:::

:::

:::

:::
