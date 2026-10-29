---
schema: qual/card@1
id: E-WPGNS
kind: problem
title: Entire functions with $\lim_{z\to\infty}f(z)=\infty$ are polynomials
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Polynomials
  - Liouville's Theorem
  - Zeros
relations: []
review: draft
---

::: {.problem}
Let $f$ be entire and suppose that
$\lim_{z \rightarrow \infty} f(z) = \infty$. Show that $f$ is a polynomial.
:::

::: {.solution}
::: pf

::: {.pf-step #nonvanishing}
There is $R>0$ with $\abs{f(z)}>1$ for $\abs z>R$.

::: pf-proof
This is the hypothesis $\lim_{z\to\infty}f(z) = \infty$.
:::

:::

::: {.pf-step #pole}
$g(w)\definedas f(1/w)$ has a pole at $w=0$.

::: pf-proof
By step [](#nonvanishing){.pf-ref}, $h(w)\definedas 1/g(w)$ is holomorphic on $0<\abs w<1/R$, and $h(w)\to0$ as $w\to0$.
By Riemann's theorem $h$ extends holomorphically with $h(0) = 0$, and $h\not\equiv0$, so $0$ is a zero of $h$ of some finite order $m\ge1$.
Hence $g = 1/h$ has a pole of order $m$ at $0$.
:::

:::

::: pf-step
$f$ is a polynomial of degree $m$.

::: pf-proof
Write $f(z) = \sum_{k\ge0}c_kz^k$ on $\CC$. Then $g(w) = \sum_{k\ge0}c_kw^{-k}$ is the Laurent series of $g$ on $w\neq0$, and by step [](#pole){.pf-ref} its coefficients vanish for $k>m$ and $c_m\neq0$.
:::

:::

:::

:::
