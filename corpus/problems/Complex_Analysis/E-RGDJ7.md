---
schema: qual/card@1
id: E-RGDJ7
kind: problem
title: Cauchy formula and $\sinh$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Contour Integration
  - Hyperbolic Functions
relations: []
review: draft
---

::: {.exercise}
Compute
$$
\int_{S^1} {2 \sinh(z) \over z^n}\dz.
$$
:::

::: {.solution}
Let $f(z) \coloneqq 2\sinh(z) = e^{z} - e^{-z}$, which is entire, and orient $S^1$ positively.

::: pf

::: pf-step
For $n\leq 0$ the integral is $0$.

::: pf-proof
For $n\leq 0$ the integrand $z^{-n}f(z)$ is entire, so the integral vanishes by Cauchy's theorem.
:::

:::

::: pf-step
For $n\geq 1$, $f^{(n-1)}(0) = 1+(-1)^n$.

::: pf-proof
For $k\geq 0$, $f^{(k)}(z) = e^z - (-1)^k e^{-z}$, so $f^{(k)}(0) = 1-(-1)^k$. Put $k=n-1$.
:::

:::

::: pf-step
For $n\geq 1$,
$$
\int_{S^1}{2\sinh(z)\over z^n}\dz = \boxed{\begin{cases} \dfrac{4\pi i}{(n-1)!} & n \text{ even}, \\ 0 & n \text{ odd}. \end{cases}}
$$

::: pf-proof
By the Cauchy integral formula for derivatives,
$$
\int_{S^1}{f(z)\over z^n}\dz = {2\pi i \over (n-1)!} f^{(n-1)}(0) = {2\pi i \over (n-1)!}\left(1+(-1)^n\right),
$$
by the preceding computation of $f^{(n-1)}(0)$.
:::

:::

:::

:::
