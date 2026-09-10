---
schema: qual/card@1
id: E-ETKNU
kind: problem
title: The imbedding theorem for m equals one
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

More precisely, for each pair \(i,j\), the set of parameters
\[
T_{ij}=\{\phi_i(x):x\in X,\ \phi_k(x)=0\text{ for }k\ne i,j\}\subset[0,1]
\]
has compact image because \(X\) is compact. Each connected component of the corresponding image on \([z_i,z_j]\) is a closed subsegment, and only finitely many pairs \((i,j)\) occur. Subdivide at all segment endpoints and at all intersection points. General position in \(\mathbb R^3\) guarantees that distinct ambient segments meet only at common vertices unless they arise from the same pair. Hence the finite union containing \(g(X)\), and after deleting unused open subsegments the image \(g(X)\) itself, is a finite linear graph.

Therefore, in the case \(m=1\), the map constructed in part (2) of the embedding theorem maps \(X\) onto a linear graph in \(\mathbb R^3\).
:::
