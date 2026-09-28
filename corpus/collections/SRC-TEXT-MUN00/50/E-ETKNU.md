---
schema: qual/card@1
id: E-ETKNU
kind: problem
title: The imbedding theorem for $m=1$ and linear graphs in $\RR^3$
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Examine the proof of the imbedding theorem in the case $m = 1$ and show that the map $g$ of part (2) actually maps $X$ onto a linear graph in $\mathbb{R}^3$.
:::

::: {.solution}
In the proof of Theorem 50.5, when \(m=1\) we have \(N=2m+1=3\). The finite open cover \(\{U_i\}_{i=1}^r\) is chosen to have order at most \(m+1=2\), and a partition of unity \(\{\phi_i\}\) dominated by this cover is chosen. The approximating map is
\[
g(x)=\sum_{i=1}^r\phi_i(x)z_i,
\]
where the points \(z_i\in\mathbb R^3\) are in general position.

At each point \(x\in X\), at most two of the numbers \(\phi_i(x)\) are nonzero. Since they are nonnegative and sum to \(1\), either
\[
g(x)=z_i
\]
for some \(i\), or
\[
g(x)=t z_i+(1-t)z_j\qquad(0<t<1)
\]
for some pair \(i\ne j\). Thus
\[
g(X)\subset \bigcup_{1\le i<j\le r}[z_i,z_j],
\]
a finite union of straight line segments.

This finite union of segments is a linear graph with vertices \(z_1,\ldots,z_r\). Points in general position in \(\mathbb R^3\) have every four of them affinely independent. If \(\{i,j\}\cap\{k,l\}=\varnothing\), the segments \([z_i,z_j]\) and \([z_k,z_l]\) are disjoint, since a common point would put \(z_i,z_j,z_k,z_l\) in one plane. If the segments share exactly one endpoint \(z_i\), they meet only at \(z_i\), since \(z_i,z_j,z_l\) are not collinear. So two edges meet at most in a common vertex.

Therefore, in the case \(m=1\), the map constructed in part (2) of the embedding theorem maps \(X\) into a linear graph in \(\mathbb R^3\).
:::

::: {.remark}
The image \(g(X)\) itself need not be a linear graph. For \(X\) a Cantor set, which has dimension \(0\le1\), let \(U_1,U_2\) be overlapping open sets covering \(X\) and let \(\phi_1\) be a partition-of-unity function that takes infinitely many values in \((0,1)\) on \(X\cap U_1\cap U_2\), such as the restriction of a piecewise linear function on \([0,1]\). Then \(g(X)\cap(z_1,z_2)\) is an infinite compact totally disconnected set, which is not a finite union of points and segments. The proof gives \(g(X)\) inside the linear graph \(\bigcup_{i<j}[z_i,z_j]\).
:::
