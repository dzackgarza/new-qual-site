---
schema: qual/card@1
id: P-YYEUK
kind: problem
title: An entire function with $\abs{f(z)}\leq M\abs{z}^2$ outside a disk is a polynomial
  of degree at most $2$
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
Let $f(z)$ be entire and assume that $\abs{f(z)} \leq M \abs{z}^2$ outside of some disk for some constant $M$.
Show that $f(z)$ is a polynomial in $z$ of degree $\leq 2$.
:::

::: {.solution}
Write $f(z)=\sum_{k\ge0}c_kz^k$, which converges on $\CC$ since $f$ is entire, and let $\abs{f(z)}\le M\abs{z}^2$ for $\abs{z}\ge R_0$.

::: pf

::: {.pf-step #cauchy}
$\abs{c_k}\le MR^{2-k}$ for every $R\ge R_0$.

::: pf-proof
By Cauchy's estimate on the circle $\abs{z}=R$, $\abs{c_k}=\abs{f^{(k)}(0)}/k!\le R^{-k}\sup_{\abs{z}=R}\abs{f(z)}\le MR^{2-k}$.
:::

:::

::: pf-step
$c_k=0$ for $k\ge3$, so $f$ is a polynomial of degree at most $2$.

::: pf-proof
For $k\ge3$, the bound of step [](#cauchy){.pf-ref} tends to $0$ as $R\to\infty$.
:::

:::

:::

:::
