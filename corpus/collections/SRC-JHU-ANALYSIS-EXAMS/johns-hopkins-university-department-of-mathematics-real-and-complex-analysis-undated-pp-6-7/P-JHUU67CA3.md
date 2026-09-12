---
schema: qual/card@1
id: P-JHUU67CA3
kind: problem
title: Holomorphic function in annulus approximable by polynomials extends to disc
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the compact-uniform polynomial approximation and extension to the full outer disk with Problem 6 of the undated JHU exam on pages 6–7."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked that the maximum principle is applied to polynomial differences, obtained the uniform Cauchy property on every compact subset of the disk, and identified the limit with the original annular function."
---

Suppose $f$ is holomorphic in an annulus $r < |z| < R$, and there exists a sequence of holomorphic polynomials $p_n$ converging to $f$ uniformly on compact subsets of the annulus.
Show that $f$ can be extended to the disc $\{|z| < R\}$ as a holomorphic function.

::: solution
Let $D_R=\{z:|z|<R\}$ and $A=\{z:r<|z|<R\}$.

<1>1. The sequence $(p_n)$ is uniformly Cauchy on each compact subset of $D_R$.

::: proof
Fix a nonempty compact set $K\subset D_R$. Choose a radius
$\rho$ satisfying
$$
\max\{r,\max_{z\in K}|z|\}<\rho<R.
$$
The circle $|z|=\rho$ is a compact subset of $A$.
Uniform convergence to $f$ there implies that $(p_n)$
is uniformly Cauchy on that circle. Each difference
$p_n-p_m$ is holomorphic on a neighborhood of the closed
disk $|z|\leq\rho$. The maximum modulus principle gives
$$
\sup_{z\in K}|p_n(z)-p_m(z)|
\leq\max_{|z|\leq\rho}|p_n(z)-p_m(z)|
=\max_{|z|=\rho}|p_n(z)-p_m(z)|\longrightarrow0
$$
as $n,m\to\infty$ [@SS03]. The assertion for the empty
compact set requires no estimate.
:::

<1>2. The limit on the disk is a holomorphic extension of $f$.

::: proof
By completeness of $\mathbb C$, step <1>1 first gives
the pointwise limit $F(z)=\lim_n p_n(z)$ at each $z\in D_R$.
For a compact $K\subset D_R$, let $m\to\infty$ in the
uniform Cauchy estimate. It follows that $p_n\to F$
uniformly on $K$. Thus convergence is locally uniform
on the whole disk. The local uniform limit theorem makes
$F$ holomorphic there [@SS03].

For every $z\in A$, the hypothesis already gives
$p_n(z)\to f(z)$. Uniqueness of limits in $\mathbb C$
therefore gives $F(z)=f(z)$ on $A$. Hence $F$ is the
required extension to all of $D_R$.
:::
:::
