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
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The source says g maps X onto a linear graph. The proof gives only containment in one: a Cantor-set domain can have an infinite totally disconnected image inside an edge.'
---

::: {.exercise}

Examine the proof of the imbedding theorem in the case $m = 1$ and show that the map $g$ of part (2) maps $X$ into a linear graph in $\RR^3$.
:::

::: {.solution}
In the proof of Theorem 50.5, when $m=1$ we have $N=2m+1=3$. The finite open cover $\{U_i\}_{i=1}^r$ is chosen to have order at most $m+1=2$, and a partition of unity $\{\phi_i\}$ dominated by this cover is chosen. The approximating map is
$$
g(x)=\sum_{i=1}^r\phi_i(x)z_i,
$$
where the points $z_i\in\RR^3$ are in general position.

At each point $x\in X$, at most two of the numbers $\phi_i(x)$ are nonzero. Since they are nonnegative and sum to $1$, either
$$
g(x)=z_i
$$
for some $i$, or
$$
g(x)=t z_i+(1-t)z_j\qquad(0<t<1)
$$
for some pair $i\ne j$. Thus
$$
g(X)\subset \bigcup_{1\le i<j\le r}[z_i,z_j],
$$
a finite union of straight line segments.

This finite union of segments is a linear graph with vertices $z_1,\ldots,z_r$. Points in general position in $\RR^3$ have every four of them affinely independent. If $\{i,j\}\cap\{k,l\}=\varnothing$, the segments $[z_i,z_j]$ and $[z_k,z_l]$ are disjoint, since a common point would put $z_i,z_j,z_k,z_l$ in one plane. If the segments share exactly one endpoint $z_i$, they meet only at $z_i$, since $z_i,z_j,z_l$ are not collinear. So two edges meet at most in a common vertex.

Therefore, in the case $m=1$, the map constructed in part (2) of the embedding theorem maps $X$ into a linear graph in $\RR^3$.
:::

