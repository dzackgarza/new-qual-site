---
schema: qual/card@1
id: E-BPSOU
kind: problem
title: Entire $O(\abs{z}^p)$ functions are polynomials of degree at most $\lfloor p\rfloor$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Cauchy Estimates
  - Polynomials
  - Liouville's Theorem
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is entire and $\abs{f(z)} \in \bigo(\abs{z}^p)$ for $\abs{z}$ sufficiently large, then $f$ is a polynomial of degree at most $\floor{p}$.
:::

::: {.solution}
Write $f(z)=\sum_{k\geq0}c_kz^k$, and choose $C$ and $R_0$ with $\abs{f(\xi)}\le C\abs\xi^p$ for $\abs\xi\ge R_0$.

::: pf

::: {.pf-step #cauchy}
$\abs{c_k}\le CR^{p-k}$ for every $k\ge0$ and $R\ge R_0$.

::: pf-proof
By Cauchy's integral formula for $c_k=f^{(k)}(0)/k!$,
$$
\abs{c_k}
\leq \frac{1}{2\pi}\int_{\abs{\xi} = R} \frac{\abs{f(\xi)}}{\abs{\xi}^{k+1}}\abs{\dxi}
\leq \frac{1}{2\pi}\cdot\frac{CR^p}{R^{k+1}}\cdot 2\pi R
= C R^{p-k}.
$$
:::

:::

::: pf-step
$f$ is a polynomial of degree at most $\floor p$.

::: pf-proof
For $k>p$, that is, $k\geq \floor{p}+1$, letting $R\to\infty$ in step [](#cauchy){.pf-ref} gives $c_k=0$.
:::

:::

:::

:::
