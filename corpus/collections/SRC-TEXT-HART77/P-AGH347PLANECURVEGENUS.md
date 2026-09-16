---
schema: qual/card@1
id: P-AGH347PLANECURVEGENUS
kind: problem
title: Cech computation of the cohomology of a plane curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Plane Curves
  - Arithmetic Genus
relations: []
review: draft
---

::: {.problem}
Let $X$ be a subscheme of $\PP_k^2$ defined by a single homogeneous equation $f(x_0, x_1, x_2)=0$ of degree $d$.
(Do not assume $f$ is irreducible.)
Assume that $(1,0,0)$ is not on $X$.
Then show that $X$ can be covered by the two open affine subsets $U=X \intersect \ts{x_1 \neq 0}$ and $V=X \intersect \ts{x_2 \neq 0}$.
Now calculate the Čech complex
\[
\Gamma(U, \mco_X) \oplus \Gamma(V, \mco_X) \to \Gamma(U \intersect V, \mco_X)
\]
explicitly, and thus show that
\[
\begin{aligned}
\dim H^0(X, \mco_X)&=1, \\
\dim H^1(X, \mco_X)&=\frac{1}{2}(d-1)(d-2).
\end{aligned}
\]
:::
