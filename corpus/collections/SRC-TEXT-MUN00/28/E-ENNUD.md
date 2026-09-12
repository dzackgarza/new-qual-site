---
schema: qual/card@1
id: E-ENNUD
kind: problem
title: An infinite set without limit points in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise}

Give $[0, 1]^\omega$ the uniform topology.
Find an infinite subset of this space that has no limit point.
:::

::: {.solution}
For each \(n\ge1\), let
\[
e_n=(0,\dots,0,1,0,\dots)\in[0,1]^\omega
\]
with the \(1\) in the \(n\)-th coordinate, and set
\[
A=\{e_n:n\in\mathbb Z_+\}.
\]
For \(m\ne n\), the uniform distance is
\[
\bar\rho(e_m,e_n)=1,
\]
since in coordinate \(m\) the two sequences differ by \(1\). Hence the open uniform balls
\[
B_{\bar\rho}(e_n,1/3)
\]
are pairwise disjoint.

More generally, no point \(x\in[0,1]^\omega\) can be a limit point of \(A\). If \(x\) were a limit point, every ball \(B(x,1/3)\) would contain infinitely many \(e_n\). Pick distinct \(e_m,e_n\) in this ball. Then the triangle inequality gives
\[
1=\bar\rho(e_m,e_n)<2/3,
\]
a contradiction. Thus \(A\) is infinite and has no limit point.
:::
