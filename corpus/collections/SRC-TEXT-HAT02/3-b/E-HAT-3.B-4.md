---
schema: qual/card@1
id: E-HAT-3.B-4
kind: problem
title: "Cross product of fundamental classes"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.B, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that the cross product of fundamental classes for closed $\mathbb{R}$-orientable manifolds $M$ and $N$ is a fundamental class for $M \times N$.
:::

::: {.solution}
Let $M^m$ and $N^n$ be closed $\mathbb R$-orientable manifolds with chosen fundamental classes
\[
[M]\in H_m(M;\mathbb R),
\qquad
[N]\in H_n(N;\mathbb R).
\]
We show that
\[
[M]\times[N]\in H_{m+n}(M\times N;\mathbb R)
\]
is a fundamental class.

Fix $(x,y)\in M\times N$. The images of $[M]$ and $[N]$ in local homology are the chosen local orientation generators
\[
[M]_x\in H_m(M,M-\{x\};\mathbb R),
\qquad
[N]_y\in H_n(N,N-\{y\};\mathbb R).
\]
By naturality of cross products, the image of $[M]\times[N]$ in local homology at $(x,y)$ is the image of
\[
[M]_x\times[N]_y
\]
under
\[
H_m(M,M-x)\otimes H_n(N,N-y)
\longrightarrow
H_{m+n}\bigl(M\times N,
(M-x)\times N\cup M\times(N-y)\bigr).
\]
The subspace on the right is exactly $M\times N-\{(x,y)\}$.

Choose orientation-preserving coordinate balls about $x$ and $y$. By excision the preceding local cross product identifies with
\[
H_m(\mathbb R^m,\mathbb R^m-0;\mathbb R)
\otimes
H_n(\mathbb R^n,\mathbb R^n-0;\mathbb R)
\longrightarrow
H_{m+n}(\mathbb R^{m+n},\mathbb R^{m+n}-0;\mathbb R).
\]
The cross product of the two standard local generators is the standard generator in dimension $m+n$; this follows directly from the relative Künneth theorem, or from the product orientation on Euclidean space. Hence the image of $[M]\times[N]$ is a generator of local homology at every $(x,y)$.

Therefore $[M]\times[N]$ is a fundamental class of $M\times N$.
:::
