---
schema: qual/card@1
id: P-5MZYU
kind: problem
title: Images of the unit circle under linear transformations of $\mathbb{R}^2$
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
What are the possible images of the unit circle under a linear transformation of $\mathbb{R}^2$?
:::

::: {.solution}
Let $T:\mathbb R^2\to\mathbb R^2$ have singular-value decomposition
\[
T=U\begin{pmatrix}\sigma_1&0\\0&\sigma_2\end{pmatrix}V^T,
\qquad \sigma_1\ge\sigma_2\ge0,
\]
with $U,V$ orthogonal. Since $V^T$ preserves the unit circle,
\[
T(S^1)=U\{(\sigma_1\cos\theta,\sigma_2\sin\theta):0\le\theta<2\pi\}.
\]
Thus:

- if $\sigma_2>0$, the image is an ellipse centered at the origin, with semiaxes $\sigma_1,\sigma_2$; it is a circle when $\sigma_1=\sigma_2$;
- if $\sigma_1>0$ and $\sigma_2=0$, the image is a closed line segment centered at the origin, of length $2\sigma_1$;
- if $\sigma_1=\sigma_2=0$, the image is the single point $\{0\}$.

These are exactly the possible images.
:::
