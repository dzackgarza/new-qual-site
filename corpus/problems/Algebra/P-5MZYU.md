---
schema: qual/card@1
id: P-5MZYU
kind: problem
title: Images of the unit circle under linear transformations of $\RR^2$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Matrices
  - Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What are the possible images of the unit circle under a linear transformation of $\RR^2$?
:::

::: {.solution}
Let $T\colon\RR^2\to\RR^2$ be linear and let $S^1$ be the unit circle.

::: pf

::: {.pf-step #svd-image}
$T(S^1)=U\{(\sigma_1\cos\theta,\sigma_2\sin\theta):0\le\theta<2\pi\}$ for an orthogonal $U$ and singular values $\sigma_1\ge\sigma_2\ge0$ of $T$.

::: pf-proof
The singular-value decomposition writes
$$
T=U\begin{pmatrix}\sigma_1&0\\0&\sigma_2\end{pmatrix}V^T
$$
with $U,V$ orthogonal. The orthogonal map $V^T$ maps $S^1$ onto $S^1$.
:::

:::

::: pf-step
The possible images are exactly
$$
\boxed{\text{an ellipse centered at }0\text{ (possibly a circle), a closed segment centered at }0\text{, or the point }\{0\}.}
$$

::: pf-proof
By step [](#svd-image){.pf-ref}: if $\sigma_2>0$, the image is the ellipse with semiaxes $\sigma_1,\sigma_2$ rotated by $U$, a circle when $\sigma_1=\sigma_2$; if $\sigma_1>0=\sigma_2$, it is the segment of length $2\sigma_1$ along $U e_1$; if $\sigma_1=\sigma_2=0$, it is $\{0\}$. Every ellipse centered at $0$, every such segment and the point arise, because $U$ and $\sigma_1\ge\sigma_2\ge0$ can be chosen freely and $T=U\operatorname{diag}(\sigma_1,\sigma_2)$ realizes them.
:::

:::

:::

:::
