---
schema: qual/card@1
id: FT-5MASA
kind: theorem
title: Cauchy inequalities
slogan: 'If $\abs{f}\le M$ on the circle $\abs{z-z_0}=R$, then $\abs{f^{(n)}(z_0)}\le n!M/R^n$.'
prompts:
- State the Cauchy inequalities for $f^{(n)}(z_0)$.
- State the Cauchy estimate for $\abs{f^{(n)}(0)}$.
- State the Cauchy inequalities in the form bounding $\abs{f^{(n)}(z_0)/n!}$.
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Cauchy Integral Formula
relations: []
review: draft
---

::: {.theorem}
Let $z_0\in\CC$ and $R>0$, let $f$ be [[D-E7A5W|holomorphic]] on an open set containing the closed disc $\abs{z-z_0}\le R$, and let $\gamma$ be the circle $\abs{z-z_0}=R$.
Then for every integer $n\ge0$,
$$
\abs{f^{(n)}(z_0)} \leq \frac{n!\, \sup_{z\in\gamma} \abs{f(z)}}{R^{n}}.
$$
:::

::: {.remark title="Variations"}
Dividing by $n!$ gives the form for Taylor coefficients: the $n$th Taylor coefficient $f^{(n)}(z_0)/n!$ of $f$ at $z_0$ has modulus at most $R^{-n}\sup_{\abs{z-z_0}=R}\abs{f(z)}$.
:::
