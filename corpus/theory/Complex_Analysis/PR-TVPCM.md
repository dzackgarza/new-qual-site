---
schema: qual/card@1
id: PR-TVPCM
kind: proposition
title: Complex differentiable at a point if and only if $\bar\partial f$ vanishes there
slogan: 'For a real-differentiable map, complex differentiability is exactly the equation $\bar\partial f=0$.'
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

::: {.proposition}
Let $f=u+iv$ be defined on a neighborhood of $z_0\in\CC$, with $u,v$ real-valued and [[D-KLTBZ|real-differentiable]] at $z_0$.
Then $f$ is complex differentiable at $z_0$ if and only if
$$
\delbar f(z_0)=\frac12(\del_x+i\del_y)f(z_0)=0.
$$

The implication from complex differentiability is [@SS03, ch. 1, Proposition 2.3], where the condition is written $\partial f/\partial\overline z(z_0)=0$ with $f'(z_0)=\partial f/\partial z(z_0)$; the converse is [@SS03, ch. 1, Theorem 2.4], which obtains holomorphy from the Cauchy--Riemann equations for a function with continuously differentiable parts. The $\bar\partial$ operator is $\partial/\partial\overline z$ of the first of those.
:::
