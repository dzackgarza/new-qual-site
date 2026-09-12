---
schema: qual/card@1
id: E-XDJRZ
kind: problem
title: The l2 space is a vector space with the l2 metric
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $X$ denote the subset of $\mathbb{R}^\omega$ consisting of all sequences $(x_1, x_2, \ldots)$ such that $\sum x_i^2$ converges.
(You may assume the standard facts about infinite series.
In case they are not familiar to you, we shall give them in Exercise 11 of the next section.)

(a) Show that if $\mathbf{x}, \mathbf{y} \in X$, then $\sum \abs{x_i y_i}$ converges.
[Hint: Use (b) of Exercise 9 to show that the partial sums are bounded.]

(b) Let $c \in \mathbb{R}$.
Show that if $\mathbf{x}, \mathbf{y} \in X$, then so are $\mathbf{x} + \mathbf{y}$ and $c\mathbf{x}$.

(c) Show that

$$
d(\mathbf{x}, \mathbf{y}) = \left[ \sum_{i=1}^{\infty} (x_i - y_i)^2 \right]^{1/2}
$$

is a well-defined metric on $X$.
:::

::: {.solution}
Let
\[
X=\left\{\mathbf x=(x_i):\sum_i x_i^2<\infty\right\}.
\]

(a) For each $n$, finite-dimensional Cauchy--Schwarz gives
\[
\sum_{i=1}^n|x_iy_i|
\le\left(\sum_{i=1}^n x_i^2\right)^{1/2}
   \left(\sum_{i=1}^n y_i^2\right)^{1/2}
\le \|\mathbf x\|_2\|\mathbf y\|_2.
\]
The partial sums on the left are increasing and bounded, hence converge. Thus $\sum|x_iy_i|$ converges.

(b) For scalars $c$,
\[
\sum_i(cx_i)^2=c^2\sum_i x_i^2<\infty.
\]
Also
\[
(x_i+y_i)^2\le2x_i^2+2y_i^2,
\]
so
\[
\sum_i(x_i+y_i)^2\le2\sum_i x_i^2+2\sum_i y_i^2<\infty.
\]
Hence $X$ is closed under scalar multiplication and addition.

(c) Part (b) shows $\mathbf x-\mathbf y\in X$, so
\[
d(\mathbf x,\mathbf y)=\left(\sum_i(x_i-y_i)^2\right)^{1/2}
\]
is finite. Nonnegativity, symmetry, and definiteness are immediate. For the triangle inequality, part (a) gives the infinite Cauchy--Schwarz inequality, so for $u,v\in X$,
\[
\|u+v\|_2^2
=\|u\|_2^2+2\sum_i u_iv_i+\|v\|_2^2
\le(\|u\|_2+\|v\|_2)^2.
\]
Thus $\|u+v\|_2\le\|u\|_2+\|v\|_2$. Applying this to
\[
u=\mathbf x-\mathbf y,\qquad v=\mathbf y-\mathbf z
\]
gives the triangle inequality for $d$. Hence $d$ is a metric on $X$.
:::
