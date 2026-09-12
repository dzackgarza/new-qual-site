---
schema: qual/card@1
id: P-A6PQA
kind: problem
title: A conformal map from $\CC\setminus[1,\infty)$ onto $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
  - Fractional Linear Transformations
relations: []
review: draft
---

::: problem
Find a conformal map from $\CC\setminus\theset{x\in \RR\suchthat x\geq 1}$ to $\DD$.
:::

::: solution
The map
\[
z\longmapsto 1-z
\]
sends the slit plane $\mathbb C\setminus[1,\infty)$ onto
$\mathbb C\setminus(-\infty,0]$. On this latter domain take the principal
square root, which maps biholomorphically onto the right half-plane. Finally,
the Cayley transform
\[
w\longmapsto\frac{w-1}{w+1}
\]
maps the right half-plane biholomorphically onto $\mathbb D$. Hence one
conformal map is
\[
\boxed{
F(z)=\frac{\sqrt{\,1-z\,}-1}{\sqrt{\,1-z\,}+1},
}
\]
where $\sqrt{\cdot}$ is the principal square root on
$\mathbb C\setminus(-\infty,0]$.
:::
