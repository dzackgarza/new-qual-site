---
schema: qual/card@1
id: E-EDUVQ
kind: problem
title: Box products of the line are completely regular
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Product Topology
relations: []
review: draft
---

::: {.exercise}

Show that $\mathbb{R}^J$ in the box topology is completely regular.
[Hint: Show that it suffices to consider the case where the box neighborhood $(-1, 1)^J$ is disjoint from $A$ and the point is the origin. Then use the fact that a function continuous in the uniform topology is also continuous in the box topology.]
:::

::: {.solution}
The box topology is Hausdorff. To prove complete regularity, let \(A\subset\mathbb R^J\) be closed and \(x\notin A\). Choose a basic box neighborhood
\[
U=\prod_{\alpha\in J}(x_\alpha-\varepsilon_\alpha,x_\alpha+\varepsilon_\alpha)
\]
of \(x\) disjoint from \(A\), with each \(\varepsilon_\alpha>0\). The coordinatewise affine homeomorphism
\[
h(y)_\alpha=\frac{y_\alpha-x_\alpha}{\varepsilon_\alpha}
\]
is a homeomorphism for the box topology, sends \(x\) to \(0\), and sends \(U\) to \((-1,1)^J\).

Thus it suffices to separate \(0\) from the complement of \((-1,1)^J\). Define
\[
g(y)=\sup_{\alpha\in J}\min\{|y_\alpha|,1\}.
\]
This is the distance from \(y\) to \(0\) in the uniform metric on \(\mathbb R^J\), hence is continuous in the uniform topology. The box topology is finer than the uniform topology, so \(g\) is also box-continuous. We have \(g(0)=0\), while \(g(y)=1\) whenever \(y\notin(-1,1)^J\). Therefore
\[
f=g\circ h
\]
is continuous, \(f(x)=0\), and \(f(A)=\{1\}\). Hence \(\mathbb R^J\) with the box topology is completely regular.
:::
