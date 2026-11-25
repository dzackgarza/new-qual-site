---
schema: qual/card@1
id: T-JACOB
kind: theorem
title: The Jacobian determinant of a holomorphic map is $\abs{f'}^2$
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Conformal Maps
relations: []
review: draft
---

::: {.theorem}
Let $f=u+iv$ be [[D-E7A5W|holomorphic]] at $z$, and regard $f$ as a map $\RR^2\to\RR^2$ of $(x,y)$.
Then $f$ is real differentiable at $z$, with Jacobian determinant
$$
\det J_f(z)=\abs{f'(z)}^2,
$$
so $f$ scales area infinitesimally by $\abs{f'}^2$ and preserves orientation wherever $f'(z)\neq0$.

This is [@SS03, ch. 1, Proposition 2.3], which states the identity for a holomorphic $f$; the area and orientation readings are the usual reading of the determinant.
:::
