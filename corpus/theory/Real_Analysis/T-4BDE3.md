---
schema: qual/card@1
id: T-4BDE3
kind: theorem
title: Bessel's inequality
slogan: 'For an orthonormal sequence $(u_n)$, $\sum_n\abs{\inner{x}{u_n}}^2\le\norm{x}^2$.'
prompts:
- State Bessel's inequality for an orthonormal sequence in a Hilbert space.
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - L²
relations: []
review: draft
---

::: {.theorem}
Let $\mch$ be a [[D-7QQUO|Hilbert space]], let $(u_n)_{n\geq1}$ be an [[D-4IXAO|orthonormal]] sequence in $\mch$, and let $x\in\mch$.
For every $N\geq1$,
$$
\norm{x-\sum_{n=1}^{N}\inner{x}{u_n}u_n}^{2}=\norm{x}^{2}-\sum_{n=1}^{N}\abs{\inner{x}{u_n}}^{2},
$$
and consequently
$$
\sum_{n=1}^{\infty}\abs{\inner{x}{u_n}}^{2} \leq\norm{x}^{2}.
$$
:::

::: {.remark title="Variations"}
The statement holds in every inner product space, complete or not.
:::

::: {.remark}
The inequality extends to an orthonormal family $(u_i)_{i\in I}$ indexed by an arbitrary, possibly uncountable, set $I$: for every $x\in\mch$,
$$
\sum_{i\in I}\abs{\inner{x}{u_i}}^2\coloneqq\sup_{\substack{F\subseteq I\\ F\text{ finite}}}\sum_{i\in F}\abs{\inner{x}{u_i}}^2\leq\norm{x}^2 .
$$
Consequently, for each $x$ only countably many of the coefficients $\inner{x}{u_i}$ are nonzero [@Fol13].
:::
