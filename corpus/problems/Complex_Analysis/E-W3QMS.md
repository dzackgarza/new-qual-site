---
schema: qual/card@1
id: E-W3QMS
kind: problem
title: Holomorphic functions with vanishing derivative are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Contour Integration
relations: []
review: draft
---

::: {.exercise}
Show that $f'=0 \implies f$ is constant using integrals and *primitives* (i.e. antiderivatives).

> See S&S Corollary 3.4.
:::

::: {.solution}
If $f'=0$ on a region $\Omega$, then for any $a,b\in\Omega$ choose a
piecewise $C^1$ path $\gamma$ from $a$ to $b$. Since $f$ is a primitive of
the zero function,
\[
f(b)-f(a)=\int_\gamma f'(z)\,dz=0.
\]
Thus $f$ is constant.
:::