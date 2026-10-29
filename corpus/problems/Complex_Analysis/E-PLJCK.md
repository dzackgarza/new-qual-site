---
schema: qual/card@1
id: E-PLJCK
kind: problem
title: Entire functions with $f(z)/z^{n}\to 0$ at infinity are polynomials of degree
  at most $n-1$
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

::: {.problem}
Suppose $f$ is entire and suppose that for some integer $n\geq 1$,
$$
\lim_{z\to \infty} {f(z) \over z^n} = 0.
$$

Prove that $f$ is a polynomial of degree at most $n-1$.
:::

::: {.solution}

Write $f(z) = \sum_{k\geq 0} c_k z^k$, the Taylor series of $f$ at $0$, which converges on $\CC$, and let $M(R)\coloneqq\max_{\abs{z}=R}\abs{f(z)}$.

::: pf

::: {.pf-step #cauchy}
For every $k\geq0$ and $R>0$, $\abs{c_k}\leq M(R)R^{-k}$.

::: pf-proof
By the Cauchy integral formula,
$$
\abs{c_k} = \abs{\frac{1}{2\pi i}\oint_{\abs{\xi}=R}\frac{f(\xi)}{\xi^{k+1}}\,d\xi}\leq\frac{1}{2\pi}\cdot 2\pi R\cdot\frac{M(R)}{R^{k+1}}.
$$
:::

:::

::: pf-step
$c_k=0$ for every $k\geq n$, so $f$ is a polynomial of degree at most $n-1$.

::: pf-proof
Let $\varepsilon>0$.
By hypothesis there is an $R_0$ with $\abs{f(z)}\leq\varepsilon\abs{z}^n$ for $\abs{z}\geq R_0$, so $M(R)\leq\varepsilon R^n$ for $R\geq R_0$.
For $k\geq n$ and $R\geq\max(R_0,1)$, step [](#cauchy){.pf-ref} gives $\abs{c_k}\leq\varepsilon R^{n-k}\leq\varepsilon$.
Since $\varepsilon$ is arbitrary, $c_k=0$.
:::

:::

:::

:::
