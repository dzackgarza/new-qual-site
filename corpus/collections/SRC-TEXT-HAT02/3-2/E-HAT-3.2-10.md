---
schema: qual/card@1
id: E-HAT-3.2-10
kind: problem
title: Failure of the Künneth cross product for infinite discrete spaces
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 10; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the counterexample: for discrete $X$ the cross product in degree zero is
    $\operatorname{Map}(X,\ZZ)\otimes\operatorname{Map}(Y,\ZZ)\to\operatorname{Map}(X\times Y,\ZZ)$,
    and the function $\delta_{ij}$ on a countable rectangle is not a finite sum of products because
    an $N$-term sum has rank at most $N$ on every finite submatrix.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 10 (p.229) including the bracketed remark about Theorem 3.15. Rechecked the counterexample: for discrete X and Y, H^0 is Map(X,Z) = product of copies of Z, the degree-zero cross product is f tensor g -> ((x,y) -> f(x)g(y)), and the function delta_ij on a countable rectangle is not a finite sum of such products since a sum of N terms has rank at most N on each finite submatrix while the (N+1)x(N+1) identity minor has rank N+1. Neither space is finitely generated in degree 0, which is why Theorem 3.15 does not apply. Citations added: the discreteness of the cochain complex and Theorem 3.15 p.216. Not covered: nothing about the higher cross products, cohomology vanishing above degree 0.
---

::: {.problem}
Show that the cross product map $H^*(X; \ZZ) \otimes H^*(Y; \ZZ) \to H^*(X \times Y; \ZZ)$ is not an isomorphism if $X$ and $Y$ are infinite discrete sets.
[This shows the necessity of the hypothesis of finite generation in Theorem 3.15.]
:::

::: {.solution}
For a discrete space $X$, singular cohomology is concentrated in degree $0$ — a singular simplex with $n>0$ is constant, so $C_n(X)$ is free on the points and $\partial = 0$ — and
$$
H^0(X;\ZZ)=\operatorname{Map}(X,\ZZ)=\prod_{x\in X}\ZZ.
$$
Thus for infinite discrete sets $X,Y$ the cross product of Theorem 3.15 (p.216), in degree zero the product of the pullbacks along the two projections, is
$$
\operatorname{Map}(X,\ZZ)\otimes
\operatorname{Map}(Y,\ZZ)
\longrightarrow
\operatorname{Map}(X\times Y,\ZZ),
$$
sending $f\otimes g$ to the function $(x,y)\mapsto f(x)g(y)$.

Take countably infinite subsets $\{x_i\}\subset X$ and $\{y_j\}\subset Y$ and define $h:X\times Y\to\ZZ$ by
$$
h(x_i,y_j)=\delta_{ij},
$$
and $h=0$ elsewhere. If $h$ were in the image, then on this countable rectangle its matrix $(\delta_{ij})$ would be a finite sum
$$
\delta_{ij}=\sum_{r=1}^N a_r(i)b_r(j).
$$
Every finite submatrix of such a matrix has rank at most $N$, whereas the $(N+1)\times(N+1)$ identity submatrix of $(\delta_{ij})$ has rank $N+1$. Contradiction.

Hence the cross product is not surjective, so it is not an isomorphism.
:::
