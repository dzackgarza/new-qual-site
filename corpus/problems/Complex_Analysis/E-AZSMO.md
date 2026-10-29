---
schema: qual/card@1
id: E-AZSMO
kind: problem
title: An entire function with $f(z)/z\to0$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Cauchy Estimates
relations: []
review: draft
---
::: {.exercise}
Suppose that $f$ is entire and $f$ has sublinear growth in the following sense:
$$
\abs{\frac{f(z)}{z}}\to 0
\text{ as } \abs{z}\to \infty.
$$
Show that $f$ must be constant.
:::

::: {.solution title="Direct bound"}
Let $g(z) \coloneqq \frac{f(z) - f(0)}{z}$ for $z\neq0$ and $g(0)\coloneqq f'(0)$.

::: pf

::: {.pf-step #entire}
$g$ is entire and $g(z)\to0$ as $\abs z\to\infty$.

::: pf-proof
$g$ is entire because $f(z)-f(0)$ vanishes at $0$.
For $z\neq 0$, $\abs{g(z)} \leq \abs{\frac{f(z)}{z}} + \abs{\frac{f(0)}{z}}$, and both terms tend to $0$ by hypothesis.
:::

:::

::: pf-step
$f$ is constant.

::: pf-proof
Fix $z\in\CC$ and $\varepsilon>0$.
By step [](#entire){.pf-ref} there is $R\ge\abs z$ with $\abs{g}<\varepsilon$ on the circle of radius $R$, so $\abs{g(z)}<\varepsilon$ by the maximum modulus principle.
Hence $g\equiv0$, so $f(z)=f(0)$ for all $z$.
:::

:::

:::

:::

::: {.solution title="Cauchy bound"}

::: pf

::: {.pf-step #derivative}
$f'(z)=0$ for every $z\in\CC$.

::: pf-proof
Fix $z$ and $\varepsilon>0$, and choose $R \geq 2\abs z$ with $\abs{f(\xi)} \leq \varepsilon \abs{\xi}$ for $\abs{\xi} \geq R$.
By Cauchy's formula, using $\abs{\xi-z}\ge R-\abs z\geq R/2$ on $\abs\xi=R$,
$$
\abs{f'(z)}
= \abs{\frac{1}{2\pi i} \int_{\abs \xi = R} \frac{f(\xi)}{(\xi - z)^2}\dxi}
\leq \frac{1}{2\pi}\cdot\frac{\varepsilon R}{(R/2)^2}\cdot 2\pi R
= 4\varepsilon.
$$
Since $\varepsilon$ is arbitrary, $f'(z)=0$.
:::

:::

::: pf-step
$f$ is constant.

::: pf-proof
$\CC$ is connected and $f'\equiv0$ by step [](#derivative){.pf-ref}.
:::

:::

:::

:::
