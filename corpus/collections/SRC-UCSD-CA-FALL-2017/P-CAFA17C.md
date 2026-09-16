---
schema: qual/card@1
id: P-CAFA17C
kind: problem
title: "Bijective analytic map from a half-disk to the upper half-plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Find a bijective analytic function $f$ from $\{z : |z| < 1, \operatorname{Re} z > 0\}$ to $\{z : \operatorname{Im} z > 0\}$.
:::

::: {.solution}
Set
\[
T(z)=\frac{z-i}{z+i}.
\]
The two boundary arcs of the right half-disk meet at $\pm i$. The diameter segment on the imaginary axis is sent by $T$ to the negative real axis, while the right semicircle is sent to the negative imaginary axis. Since $T(1)=-i$ and $T(1/2)$ lies in the third quadrant, $T$ maps the right half-disk conformally onto
\[
Q=\{w:\operatorname{Re}w<0,\ \operatorname{Im}w<0\}.
\]

The squaring map is conformal and injective on $Q$, and it doubles arguments from $(-\pi,-\pi/2)$ to $(-2\pi,-\pi)$, which modulo $2\pi$ is $(0,\pi)$. Thus it maps $Q$ bijectively onto the upper half-plane.

Therefore
\[
\boxed{f(z)=\left(\frac{z-i}{z+i}\right)^2}
\]
is the desired bijective analytic map.
:::
