---
schema: qual/card@1
id: E-XFXGM
kind: problem
title: Product metrics, finite and countable
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Product Topology
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

Let $X_n$ be a metric space with metric $d_n$, for $n \in \mathbb{Z}_+$.

(a) Show that

$$
\rho(x, y) = \max\theset{d_1(x_1, y_1), \dots, d_n(x_n, y_n)}
$$

is a metric for the product space $X_1 \times \cdots \times X_n$.

(b) Let $\bar{d}_i = \min\theset{d_i, 1}$.
Show that

$$
D(x, y) = \sup\theset{\bar{d}_i(x_i, y_i)/i}
$$

is a metric for the product space $\prod X_i$.
:::

::: {.solution}
(a) Let
\[
\rho(x,y)=\max_{1\le i\le n}d_i(x_i,y_i).
\]
Nonnegativity, symmetry, and definiteness are immediate. For each $i$,
\[
d_i(x_i,z_i)\le d_i(x_i,y_i)+d_i(y_i,z_i)\le \rho(x,y)+\rho(y,z),
\]
so taking the maximum gives the triangle inequality.

A $\rho$-ball of radius $r$ is exactly
\[
\prod_{i=1}^n B_{d_i}(x_i,r),
\]
so the metric topology equals the finite product topology.

(b) Put $\bar d_i=\min(d_i,1)$ and
\[
D(x,y)=\sup_i\frac{\bar d_i(x_i,y_i)}{i}.
\]
Each $\bar d_i$ is a metric, and the same coordinatewise triangle inequality followed by supremum proves the triangle inequality for $D$. Definiteness follows because $D(x,y)=0$ forces every coordinate distance to vanish.

We compare topologies. Given $\varepsilon>0$, choose $N$ so large that $1/i<\varepsilon$ for $i>N$. The set of $y$ with
\[
d_i(x_i,y_i)<i\varepsilon\qquad(1\le i\le N)
\]
is a basic product neighborhood of $x$. For such $y$, $\bar d_i(x_i,y_i)/i<\varepsilon$ for $i\le N$, and $\bar d_i(x_i,y_i)/i\le1/i\le1/(N+1)<\varepsilon$ for $i>N$, so $D(x,y)<\varepsilon$. Hence this neighborhood lies in the $D$-ball of radius $\varepsilon$ about $x$.

Conversely, let
\[
U=\prod_iU_i
\]
be a basic product neighborhood of $x$, with $U_i=X_i$ except for the finite set $F$. For each $i\in F$, choose $r_i\in(0,1]$ such that
\[
B_{d_i}(x_i,r_i)\subseteq U_i.
\]
Choose
\[
0<\varepsilon<\min_{i\in F}\frac{r_i}{i}.
\]
If $D(x,y)<\varepsilon$, then for $i\in F$,
\[
d_i(x_i,y_i)=\bar d_i(x_i,y_i)<i\varepsilon<r_i,
\]
so $y\in U$. Thus the $D$-topology is exactly the product topology.
:::
