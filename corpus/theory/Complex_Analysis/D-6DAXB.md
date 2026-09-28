---
schema: qual/card@1
id: D-6DAXB
kind: definition
title: Contour integral
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: {.definition}
Let $\gamma\colon[a,b]\to\CC$ be a piecewise $C^1$ curve and let $f$ be a continuous complex-valued function on $\gamma([a,b])$.
The \dfn{contour integral} of $f$ along $\gamma$ is
$$
\int_{\gamma}f\dz\coloneqq\int_a^b f(\gamma(t))\,\gamma'(t)\dt.
$$
:::

::: {.remark}
Write $f=u+iv$ with $u,v$ real-valued and $z=x+iy$, so that $dz=dx+i\,dy$.
Then $f\dz=(u+iv)\dx+(-v+iu)\dy$, and the contour integral is the line integral of this complex-valued $1$-form:
$$
\int_{\gamma}f\dz=\int_\gamma (u+iv)\dx+(-v+iu)\dy.
$$
:::
