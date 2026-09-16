---
schema: qual/card@1
id: P-CAFA23E
kind: problem
title: "Continuous function analytic off the real line is entire"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $f$ be continuous on $\mathbb{C}$ and analytic on $\mathbb{C} \setminus \mathbb{R}$.
Prove that $f$ is analytic on $\mathbb{C}$.
:::

::: {.solution}
We use Morera's theorem. Let $T$ be any triangle in $\mathbb C$. If $T$ lies
entirely in one of the two half-planes, then
\[
\int_{\partial T}f(z)\,dz=0
\]
by Cauchy's theorem.

In general, split $T$ along its intersections with the real axis into finitely
many polygonal pieces lying in the closed upper and lower half-planes. Approximate
each real-axis edge by a parallel edge at height $\pm\varepsilon$. Cauchy's
theorem applies to the shifted pieces, and continuity of $f$ lets
$\varepsilon\downarrow0$. The integrals along the internal real-axis segments
cancel with opposite orientations. Thus
\[
\int_{\partial T}f(z)\,dz=0
\]
for every triangle $T$. Morera's theorem now implies that $f$ is holomorphic
on all of $\mathbb C$.
:::
