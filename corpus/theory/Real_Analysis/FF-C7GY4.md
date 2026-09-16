---
schema: qual/card@1
id: FF-C7GY4
kind: fact
title: Integrability of $1/x^p$ on $(0,1)$ and $(1,\infty)$
prompts:
- Where is ${1\over x^p}$ integrable in $\RR$? (Depending on $p$)
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Lp Spaces
relations: []
review: draft
---

::: {.fact}
Let $p\in\RR$ and let $f(x)\coloneqq x^{-p}$ for $x>0$.

- $f\in L^1((0, 1))$ if and only if $p < 1$.

- $f\in L^1((1, \infty))$ if and only if $p > 1$.
:::

::: {.proof}
For $0<a<b$, $\int_a^b x^{-p}\dx$ equals $\frac{b^{1-p} - a^{1-p}}{1-p}$ if $p\neq 1$ and $\log b - \log a$ if $p = 1$.
By monotone convergence, $\int_{(0,1)}x^{-p}\dx = \lim_{a\to 0^+}\int_a^1 x^{-p}\dx$, which is finite exactly when $1-p>0$, and $\int_{(1,\infty)}x^{-p}\dx = \lim_{b\to\infty}\int_1^b x^{-p}\dx$, which is finite exactly when $1-p<0$.
:::
