---
schema: qual/card@1
id: P-CASP21F
kind: problem
title: "Uniform convergence of harmonic functions implies convergence of partial derivatives"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Uniform Convergence
  - Partial Derivatives
relations: []
review: draft
---

::: {.problem}
Let $\{u_n(x, y)\}$ be a sequence of harmonic functions in an open connected set $G \subset \mathbb{R}^2$, converging uniformly on compact subsets of $G$.
Show that the sequence of partial derivatives $\frac{\partial u_n}{\partial x}$ converges uniformly on compact subsets of $G$.
:::

::: {.solution}
Let $K\Subset G$. Choose a compact set $K_1$ with
\[
K\Subset \operatorname{int}K_1\Subset G.
\]
For harmonic functions there are interior derivative estimates: if
$B(a,r)\subset G$, then
\[
|u_x(a)|\le \frac{C}{r}\sup_{B(a,r)}|u|
\]
for an absolute constant $C$. Applying this estimate to
$u_n-u_m$ on finitely many disks covering $K$ and contained in $K_1$ gives
\[
\sup_K |(u_n-u_m)_x|
\le C_K\sup_{K_1}|u_n-u_m|.
\]
Because $u_n$ converges uniformly on compact subsets of $G$, the right-hand
side tends to $0$ as $n,m\to\infty$. Hence $(u_n)_x$ is uniformly Cauchy on
$K$, and therefore converges uniformly there.

Since $K\Subset G$ was arbitrary,
\[
\frac{\partial u_n}{\partial x}
\]
converges uniformly on compact subsets of $G$.
:::
