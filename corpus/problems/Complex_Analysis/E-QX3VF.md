---
schema: qual/card@1
id: E-QX3VF
kind: problem
title: Entire functions with poles at infinity
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Polynomials
  - Singularities
  - Poles
relations: []
review: draft
---

::: {.exercise}
Characterize all entire functions with a pole of order $m$ at $\infty$.
:::

::: {.solution}
Let $f$ be entire, and let $f(z) = \sum_{k\geq 0} c_k z^k$ be its Taylor series, which converges on all of $\CC$.

::: pf

::: pf-step
$f$ has a pole of order $m$ at $\infty$ if and only if $c_m\neq 0$ and $c_k = 0$ for all $k>m$.

::: pf-proof
By definition, $f$ has a pole of order $m$ at $\infty$ when $g(w) \coloneqq f(1/w)$ has a pole of order $m$ at $w=0$.
On $\CC\sm\{0\}$, $g(w) = \sum_{k\geq 0} c_k w^{-k}$ is the Laurent series of $g$ about $0$, with principal part $\sum_{k\geq 1} c_k w^{-k}$.
The pole has order $m$ exactly when this principal part ends at the term $c_m w^{-m}$ with $c_m\neq 0$.
:::

:::

::: pf-step
The entire functions with a pole of order $m$ at $\infty$ are $\boxed{\text{the polynomials of degree exactly } m}$.

::: pf-proof
By the first step, such an $f$ is $\sum_{k=0}^{m} c_k z^k$ with $c_m\neq 0$, and every such polynomial satisfies the condition of that step.
:::

:::

:::

:::
