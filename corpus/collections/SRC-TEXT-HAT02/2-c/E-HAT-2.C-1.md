---
schema: qual/card@1
id: E-HAT-2.C-1
kind: problem
title: Minimum number of edges for simplicial map $S^1 \to S^1$ of degree $n$
classification:
  areas:
  - topology
  topics:
  - Simplicial Approximation
  - Degree
  - Graphs
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.C, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the simplicial, Lefschetz-trace, or surface argument against the preceding section results.
---

What is the minimum number of edges in simplicial complex structures $K$ and $L$ on $S^1$ such that there is a simplicial map $K \to L$ of degree $n$?

::: {.solution}
Let $e(K)$ and $e(L)$ denote the numbers of edges of the two simplicial circles.

<1>1. Every simplicial complex structure on $S^1$ has at least three edges.
::: {.proof}
A simplicial complex cannot have a loop edge or two distinct edges with the same pair of endpoints. Hence a simplicial circle needs at least three vertices and therefore at least three edges. The boundary of a $2$-simplex realizes three.
:::

<1>2. If a simplicial map $f:K\to L$ has degree $n\ne0$, then
\[
e(K)\ge |n|e(L).
\]
::: {.proof}
Orient $K$ and $L$. Let
\[
z_K=\sum_{e\subset K}\epsilon_e e,
\qquad
z_L=\sum_{a\subset L}\epsilon_a a
\]
be their fundamental simplicial $1$-cycles. Each edge of $K$ is sent either to a vertex or linearly onto one edge of $L$, with coefficient $0$ or $\pm1$ on chains. Since
\[
f_*(z_K)=n z_L,
\]
each target edge must receive total signed coefficient $n$. Thus at least $|n|$ domain edges must map nondegenerately to each of the $e(L)$ target edges, giving the inequality.
:::

<1>3. The bound is sharp: for $n\ne0$ take $L$ to be a triangle and $K$ a polygon with $3|n|$ edges, mapping its edges successively around the three edges of $L$ exactly $|n|$ times, preserving orientation if $n>0$ and reversing it if $n<0$.
::: {.proof}
The vertex map is periodic with period three and sends adjacent vertices to adjacent vertices, so it extends to a simplicial map. The induced map on the fundamental $1$-cycle is multiplication by $n$.
:::

<1>4. For $n=0$, both $K$ and $L$ can be triangles and the constant simplicial map has degree zero.
::: {.proof}
A constant map sends all $1$-chains to zero, hence has degree zero.
:::

Therefore the minimum numbers are
\[
\boxed{e(L)=3,\qquad e(K)=3\max\{1,|n|\}.}
\]
:::
