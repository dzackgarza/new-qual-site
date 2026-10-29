---
schema: qual/card@1
id: P-4TU4Y
kind: problem
title: Entire functions with $|f(z)|\le|z|^{1/2}$ for $|z|>10$ are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
  - Cauchy Estimates
relations: []
review: draft
---

::: {.problem}
Find all entire functions satisfying
$$
\abs{f(z)} \leq \abs{z}^{1\over 2} \quad\text{ for } \abs{z} > 10
.$$
:::

::: {.solution}

Write $f(z)=\sum_{k\geq0}c_kz^k$, the Taylor series at $0$, which converges on $\CC$, with $c_k=f^{(k)}(0)/k!$.

::: pf

::: {.pf-step #higher-vanish}
$c_k=0$ for every $k\geq1$.

::: pf-proof
For $R>10$, the Cauchy estimate on $\abs{\xi}=R$ gives
$$
\abs{c_k}=\abs{\frac1{2\pi i}\oint_{\abs{\xi}=R}\frac{f(\xi)}{\xi^{k+1}}\,d\xi}\leq\frac{R^{1/2}}{R^k}=R^{\frac12-k},
$$
which tends to $0$ as $R\to\infty$ when $k\geq1$.
:::

:::

::: pf-step
The entire functions satisfying the bound are exactly the $\boxed{\text{constants } f\equiv c \text{ with } \abs{c}\leq\sqrt{10}}$.

::: pf-proof
By step [](#higher-vanish){.pf-ref}, $f\equiv c$ is constant.
A constant satisfies the bound iff $\abs{c}\leq\abs{z}^{1/2}$ for all $\abs{z}>10$, that is, iff $\abs{c}\leq\inf_{r>10}r^{1/2}=\sqrt{10}$.
:::

:::

:::

:::
