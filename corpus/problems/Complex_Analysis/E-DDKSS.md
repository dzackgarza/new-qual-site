---
schema: qual/card@1
id: E-DDKSS
kind: problem
title: An entire function with $\abs{f(z)}\le M\abs z^n$ for large $\abs z$ is a polynomial
  of degree at most $n$
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
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source reads "for some constants $k$ and $R$", leaving $M$ and $n$ undeclared; the statement now names the constants $M$ and $R$ and an integer $n\ge0$.'
---

::: {.exercise}
Let $n\geq 0$ be an integer.
Suppose that $f$ is entire and has polynomial growth in the following sense:
$$
\abs{f(z)\over z^n} \leq M \text{ for }\abs{z} \geq R,
$$
for some constants $M$ and $R$.
Show that $f$ is a polynomial of degree at most $n$.
:::

::: {.solution}
Write $f(z)=\sum_{k\ge0}c_kz^k$ for the Taylor expansion of $f$ about $0$, which converges on $\CC$ because $f$ is entire.

::: pf

::: {.pf-step #cauchy-estimate}
$\abs{c_k}\le M\rho^{n-k}$ for every $k\ge0$ and every $\rho\ge R$.

::: pf-proof
By the Cauchy integral formula, $c_k=\frac{f^{(k)}(0)}{k!}=\frac1{2\pi i}\int_{\abs\xi=\rho}\frac{f(\xi)}{\xi^{k+1}}\dxi$.
On $\abs\xi=\rho\ge R$ the hypothesis gives $\abs{f(\xi)}\le M\rho^n$, so
$$
\abs{c_k}\le\frac1{2\pi}\cdot\frac{M\rho^n}{\rho^{k+1}}\cdot2\pi\rho=M\rho^{n-k}.
$$
:::

:::

::: pf-step
$f$ is a polynomial of degree at most $n$.

::: pf-proof
For $k>n$, letting $\rho\to\infty$ in step [](#cauchy-estimate){.pf-ref} gives $c_k=0$.
:::

:::

:::

:::

