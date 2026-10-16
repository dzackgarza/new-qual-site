---
schema: qual/card@1
id: E-USHMH
kind: problem
title: $2^{n-1}\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}=n$ via $n$th roots of unity
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Polynomials
relations: []
review: draft
---

::: {.exercise}
Use $n$th roots of unity to show that $2^{n-1}\sin\frac{\pi}{n}\sin\frac{2\pi}{n}\cdots\sin\frac{(n-1)\pi}{n}=n$.
:::

::: {.solution}
Let $\zeta=e^{2\pi i/n}$. From
\[
z^n-1=(z-1)\prod_{k=1}^{n-1}(z-\zeta^k)
\]
we obtain, after dividing by $z-1$ and setting $z=1$,
\[
n=\prod_{k=1}^{n-1}(1-\zeta^k).
\]
Taking absolute values gives
\[
n=\prod_{k=1}^{n-1}|1-e^{2\pi i k/n}|.
\]
For real $\theta$,
\[
|1-e^{i\theta}|=2\left|\sin\frac\theta2\right|.
\]
Since $0<k\pi/n<\pi$ for $1\le k\le n-1$, all these sines are positive.
Therefore
\[
n=\prod_{k=1}^{n-1}2\sin\frac{k\pi}{n}
=2^{n-1}\prod_{k=1}^{n-1}\sin\frac{k\pi}{n},
\]
as required.
:::