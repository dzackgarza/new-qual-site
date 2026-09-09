---
schema: qual/card@1
id: P-EMCA9
kind: problem
title: "Image of nonconstant entire function is dense"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
If $f$ is a non-constant entire function, then $f(\mathbf{C})$ is dense in the plane.
:::

::: solution
Suppose that $f(\mathbb C)$ were not dense in $\mathbb C$. Then there would be
a point $a\in\mathbb C$ and an $r>0$ such that
\[
B(a,r)\cap f(\mathbb C)=\varnothing.
\]
Thus
\[
|f(z)-a|\ge r\qquad\text{for every }z\in\mathbb C.
\]
The function
\[
g(z)=\frac1{f(z)-a}
\]
is therefore entire and bounded by $1/r$. By Liouville's theorem, $g$ is
constant. Hence $f$ is constant, contradicting the hypothesis.

Therefore every nonempty open disk meets $f(\mathbb C)$, so $f(\mathbb C)$ is
dense in the plane.
:::
