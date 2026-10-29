---
schema: qual/card@1
id: P-OND4D
kind: problem
title: Analyticity of $\int_\gamma\frac{g(w)}{w-z}\,dw$ off a smooth curve $\gamma$
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Contour Integration
  - Cauchy Integral Formula
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source does not say what g is; the statement adds that g is continuous on gamma.'
---

::: {.problem}
Let $\gamma$ be a smooth curve joining two distinct points $a, b\in \CC$, and let $g$ be continuous on $\gamma$.

Prove that the function
$$
f(z) \definedas \int_\gamma {g(w) \over w-z} \,dw
$$
is analytic in $\CC\setminus\gamma$.
:::

::: {.solution}
Fix $z_0\notin\gamma$. Since $\gamma$ is compact, $d\definedas\operatorname{dist}(z_0,\gamma)>0$; let $r=d/2$ and $M=\max_\gamma\abs{g}$.

::: pf

::: {.pf-step #geometric}
For $\abs{z-z_0}<r$, $\frac{1}{w-z}=\sum_{n\ge0}\frac{(z-z_0)^n}{(w-z_0)^{n+1}}$ uniformly in $w\in\gamma$.

::: pf-proof
For $w\in\gamma$, $\abs{w-z_0}\ge 2r$, so $\abs{\frac{z-z_0}{w-z_0}}\le\frac12$ and the $n$th term is at most $\frac{2^{-n}}{2r}$. The Weierstrass $M$-test gives uniform convergence of the geometric series $\frac{1}{w-z}=\frac{1}{w-z_0}\cdot\frac{1}{1-\frac{z-z_0}{w-z_0}}$.
:::

:::

::: pf-step
$f(z)=\sum_{n\ge0}c_n(z-z_0)^n$ for $\abs{z-z_0}<r$, where $c_n=\int_\gamma\frac{g(w)}{(w-z_0)^{n+1}}\,dw$. Hence $f$ is analytic at $z_0$, and since $z_0\notin\gamma$ was arbitrary, on $\CC\setminus\gamma$.

::: pf-proof
Multiply the expansion of step [](#geometric){.pf-ref} by the bounded function $g$; the series still converges uniformly on $\gamma$, so it may be integrated term by term over the curve $\gamma$ of finite length.
:::

:::

:::
:::
