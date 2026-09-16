---
schema: qual/card@1
id: T-4BDE3
kind: theorem
title: Bessel's inequality
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

::: {.proof}
Fix $N\geq 1$ and put $s_N\coloneqq\sum_{k=1}^{N}\inner{x}{u_k}u_k$.
By orthonormality, $\inner{x}{s_N} = \inner{s_N}{s_N} = \sum_{k=1}^{N}\abs{\inner{x}{u_k}}^2$, so
$$
0\leq\norm{x - s_N}^2 = \norm{x}^2 - 2\operatorname{Re}\inner{x}{s_N} + \norm{s_N}^2 = \norm{x}^2 - \sum_{k=1}^{N}\abs{\inner{x}{u_k}}^2.
$$
Letting $N\to\infty$ gives the inequality.
:::

::: {.remark}
The inequality extends to an orthonormal family $(u_i)_{i\in I}$ indexed by an arbitrary, possibly uncountable, set $I$: for every $x\in\mch$,
$$
\sum_{i\in I}\abs{\inner{x}{u_i}}^2\coloneqq\sup_{\substack{F\subseteq I\\ F\text{ finite}}}\sum_{i\in F}\abs{\inner{x}{u_i}}^2\leq\norm{x}^2 .
$$
Consequently, for each $x$ only countably many of the coefficients $\inner{x}{u_i}$ are nonzero [@Fol13].
:::
