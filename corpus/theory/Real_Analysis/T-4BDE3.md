---
schema: qual/card@1
id: T-4BDE3
kind: theorem
title: Bessel's inequality
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
Put $s_N\coloneqq\sum_{n=1}^N\inner{x}{u_n}u_n$.
By orthonormality, $\inner{x}{s_N}=\inner{s_N}{s_N}=\sum_{n=1}^N\abs{\inner{x}{u_n}}^2$, so
$$
\norm{x-s_N}^2=\norm{x}^2-2\operatorname{Re}\inner{x}{s_N}+\norm{s_N}^2=\norm{x}^2-\sum_{n=1}^N\abs{\inner{x}{u_n}}^2 .
$$
The left side is nonnegative, so every partial sum of $\sum_n\abs{\inner{x}{u_n}}^2$ is at most $\norm{x}^2$; letting $N\to\infty$ gives the inequality.
:::
