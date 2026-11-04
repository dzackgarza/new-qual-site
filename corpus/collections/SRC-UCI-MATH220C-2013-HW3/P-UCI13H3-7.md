---
schema: qual/card@1
id: P-UCI13H3-7
kind: problem
title: An entire function bounded by $1+\abs z^{\sqrt{2010}}$ is a polynomial of degree at most $44$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Cauchy Estimates
  - Polynomials
relations:
- kind: related-to
  target: E-BPSOU
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
If $f$ is an entire function satisfying the estimate
$$
\abs{f(z)}\le 1+\abs z^{\sqrt{2010}}\quad\text{for every }z\in\CC,
$$
show that $f$ is a polynomial and determine the best upper bound for the degree of $f$.
:::

::: {.solution}
Let $f(z)=\sum_{k\ge0}a_kz^k$ be the Taylor expansion at the origin and write $\alpha=\sqrt{2010}$, so that $44<\alpha<45$.

::: pf

::: {.pf-step #cauchy-estimates}
For every $n\ge0$ and $R>0$, $\abs{f^{(n)}(0)}\le n!\,\dfrac{1+R^{\alpha}}{R^{n}}$.

::: pf-proof
The Cauchy estimates for the circle $\abs z=R$ give $\abs{f^{(n)}(0)}\le n!\,M(R)/R^n$, where $M(R)=\max_{\abs z=R}\abs{f(z)}$.
The hypothesis bounds $M(R)\le1+R^{\alpha}$.
:::

:::

::: {.pf-step #tail-vanishes}
$a_n=0$ for every $n\ge45$.

::: pf-proof
Fix $n\ge45$ and let $R\to\infty$ in step [](#cauchy-estimates){.pf-ref}.
Since $n>\alpha$, the quantity $(1+R^{\alpha})/R^n=R^{\alpha-n}+R^{-n}$ tends to $0$, so $a_n=f^{(n)}(0)/n!=0$.
:::

:::

::: {.pf-step #degree-bound}
$f$ is a polynomial of degree at most $\boxed{44}$, and no smaller bound holds.

::: pf-proof
By step [](#tail-vanishes){.pf-ref} the Taylor series at $0$ terminates, so $f$ agrees with the polynomial $\sum_{k=0}^{44}a_kz^k$ on all of $\CC$ and is a polynomial of degree at most $44$.
The bound is attained: $f(z)=z^{44}$ is entire, and for $\abs z\ge1$ one has $\abs z^{44}\le\abs z^{\alpha}$ while for $\abs z<1$ one has $\abs z^{44}\le1$, so $\abs{f(z)}\le1+\abs z^{\alpha}$ holds everywhere.
:::

:::

:::

:::
