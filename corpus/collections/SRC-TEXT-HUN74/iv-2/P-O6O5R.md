---
schema: qual/card@1
id: P-O6O5R
kind: problem
title: Rank is additive under direct sums of free modules
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Bases
  - Direct Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against an independent statement explicitly identifying the problem as Hungerford IV.2.9.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
If $F_1, F_2$ are free modules of a ring with the invariant dimension property, then $$\mathrm{rank}(F_1 \oplus F_2) = \mathrm{rank} F_1 + \mathrm{rank} F_2.$$
:::

::: solution
Let $X$ be a basis of $F_1$ and $Y$ a basis of $F_2$. Define
\[
B=\{(x,0):x\in X\}\cup\{(0,y):y\in Y\}
\subseteq F_1\oplus F_2.
\]

<1>1. The set $B$ spans $F_1\oplus F_2$.
::: proof
Let $(u,v)\in F_1\oplus F_2$. Since $X$ and $Y$ are bases, there are finite
expressions
\[
u=\sum_{i=1}^m r_i x_i,
\qquad
v=\sum_{j=1}^n s_j y_j.
\]
Hence
\[
(u,v)
=\sum_{i=1}^m r_i(x_i,0)
+\sum_{j=1}^n s_j(0,y_j),
\]
so $(u,v)$ lies in the span of $B$.
:::

<1>2. The set $B$ is linearly independent.
::: proof
Suppose
\[
\sum_{i=1}^m r_i(x_i,0)
+\sum_{j=1}^n s_j(0,y_j)
=(0,0).
\]
Comparing coordinates gives
\[
\sum_{i=1}^m r_i x_i=0
\qquad\text{and}\qquad
\sum_{j=1}^n s_j y_j=0.
\]
Linear independence of $X$ and $Y$ forces every $r_i$ and $s_j$ to be zero.
Thus $B$ is linearly independent.
:::

<1>3. Therefore $B$ is a basis of $F_1\oplus F_2$ and
\[
\operatorname{rank}(F_1\oplus F_2)
=\operatorname{rank}F_1+\operatorname{rank}F_2.
\]
::: proof
By <1>1 and <1>2, $B$ is a basis. The two subsets defining $B$ are disjoint and
are in bijection with $X$ and $Y$, respectively, so
\[
|B|=|X|+|Y|.
\]
Because the ring has the invariant dimension property, the rank of a free module
is the cardinality of any basis. Hence
\[
\operatorname{rank}(F_1\oplus F_2)
=|B|
=|X|+|Y|
=\operatorname{rank}F_1+\operatorname{rank}F_2.
\]
:::
:::
