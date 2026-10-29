---
schema: qual/card@1
id: P-JICG7
kind: problem
title: An entire function with $f(z)/z^n\to 0$ at infinity is a polynomial of degree
  at most $n-1$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Polynomials
  - Liouville's Theorem
  - Cauchy Estimates
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Suppose $f$ is entire and suppose that for some integer $n\geq 1$,
$$
\lim_{z\to \infty} {f(z) \over z^n} = 0
.$$

Prove that $f$ is a polynomial of degree at most $n-1$.
:::

::: {.solution}
::: pf

::: {.pf-step #high-coeffs-zero}
$f^{(k)}(0) = 0$ for every $k \geq n$.

::: pf-proof
Let $\varepsilon > 0$.
By hypothesis there is $R_\varepsilon$ with $\abs{f(z)} \leq \varepsilon \abs{z}^n$ for $\abs{z} \geq R_\varepsilon$.
The Cauchy estimates on $\abs{z} = R \geq R_\varepsilon$ give
$$
\abs{f^{(k)}(0)} \leq \frac{k!}{R^k} \max_{\abs{z} = R}\abs{f(z)} \leq k!\, \varepsilon R^{n-k} \leq k!\,\varepsilon R_\varepsilon^{n-k}
$$
for $k \geq n$.
For $k > n$ let $R \to \infty$; for $k = n$ the bound is $n!\,\varepsilon$ for every $\varepsilon$.
In both cases $f^{(k)}(0) = 0$.
:::

:::

::: pf-step
$f(z) = \sum_{k=0}^{n-1} \frac{f^{(k)}(0)}{k!} z^k$, a polynomial of degree at most $n-1$.

::: pf-proof
The Taylor series of the entire function $f$ about $0$ converges to $f$ on $\CC$, and by step [](#high-coeffs-zero){.pf-ref} its terms with $k \geq n$ vanish.
:::

:::

:::
:::
