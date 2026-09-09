---
schema: qual/card@1
id: E-HAT-3.2-10
kind: problem
title: Hatcher Section 3.2 Exercise 10
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 10; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

# E-HAT-3.2-10

Show that the cross product map $H^*(X; \mathbb{Z}) \otimes H^*(Y; \mathbb{Z}) \to H^*(X \times Y; \mathbb{Z})$ is not an isomorphism if $X$ and $Y$ are infinite discrete sets.
[This shows the necessity of the hypothesis of finite generation in Theorem 3.15.]

::: {.solution}
For a discrete space $X$, singular cohomology is concentrated in degree $0$ and
\[
H^0(X;\mathbb Z)=\operatorname{Map}(X,\mathbb Z)=\prod_{x\in X}\mathbb Z.
\]
Thus for infinite discrete sets $X,Y$, the cross product in degree zero is
\[
\operatorname{Map}(X,\mathbb Z)\otimes
\operatorname{Map}(Y,\mathbb Z)
\longrightarrow
\operatorname{Map}(X\times Y,\mathbb Z),
\]
sending $f\otimes g$ to the function $(x,y)\mapsto f(x)g(y)$.

Take countably infinite subsets $\{x_i\}\subset X$ and $\{y_j\}\subset Y$ and define $h:X\times Y\to\mathbb Z$ by
\[
h(x_i,y_j)=\delta_{ij},
\]
and $h=0$ elsewhere. If $h$ were in the image, then on this countable rectangle its matrix $(\delta_{ij})$ would be a finite sum
\[
\delta_{ij}=\sum_{r=1}^N a_r(i)b_r(j).
\]
Every finite submatrix of such a matrix has rank at most $N$, whereas the $(N+1)\times(N+1)$ identity submatrix of $(\delta_{ij})$ has rank $N+1$. Contradiction.

Hence the cross product is not surjective, so it is not an isomorphism.
:::
