---
schema: qual/card@1
id: D-VARNCROSS
kind: definition
title: Normal crossing singularities
classification:
  areas:
  - algebraic-geometry
  topics:
  - Singularities
  - Normal Crossings
  - Divisors
relations:
- kind: uses
  target: D-0SYCY
review: draft
prompts:
- What is a normal crossing singularity?
- What is a simple normal crossing divisor?
---

::: {.definition title="Normal crossings"}
Let $k$ be an algebraically closed field.
A variety $Y$ of dimension $n$ has a \dfn{normal crossing singularity} at a closed point $p$ if there is an isomorphism of complete local rings
\[
\hat{\OO}_{Y,p} \cong k[[x_0, \ldots, x_n]] / (x_0 x_1 \cdots x_r)
\]
for some $0 \leq r \leq n$.
So near $p$, analytically, $Y$ looks like $r+1$ coordinate hyperplanes meeting in $\AA^{n+1}$.
$Y$ has \dfn{normal crossings} if it has a normal crossing singularity or a smooth point at every closed point; the case $r = 0$ is a smooth point.
:::

::: {.definition title="Simple normal crossing divisor"}
Let $X$ be a smooth variety and $D = \sum_i D_i$ a reduced effective divisor.
$D$ is a \dfn{normal crossing divisor} if at each closed point $p \in D$ there are local parameters $x_1, \ldots, x_n$ of $\hat{\OO}_{X,p}$ with $D$ defined by $x_1 \cdots x_r = 0$.
$D$ is a \dfn{simple normal crossing divisor} if moreover every component $D_i$ is smooth, and at each point the components through $p$ are cut out by distinct members of a single system of local parameters in $\OO_{X,p}$ itself.
:::

::: {.example}
In characteristic not $2$, the node $y^2 = x^2(x+1)$ in $\AA^2$ has a normal crossing singularity at the origin: $x\sqrt{x+1}$ is a power series, and $y^2 - x^2(x+1) = (y - x\sqrt{x+1})(y + x\sqrt{x+1})$ is a product of two parameters.
As a divisor on $\AA^2$ it is normal crossing but not simple normal crossing, since its one component is singular.
The cusp $y^2 = x^3$ is not a normal crossing singularity, since its tangent cone $y^2 = 0$ is not a pair of distinct lines.
:::
