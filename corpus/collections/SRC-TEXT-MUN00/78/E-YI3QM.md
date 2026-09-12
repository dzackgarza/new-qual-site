---
schema: qual/card@1
id: E-YI3QM
kind: problem
title: The closed disk as a surface with boundary
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
---

::: {.exercise}

Show that the closed unit ball in $\mathbb{R}^2$ is a 2-manifold with boundary.
:::

::: {.solution}
Let
\[
D^2=\{(x,y)\in\mathbb R^2:x^2+y^2\le1\}.
\]
It is Hausdorff and second countable as a subspace of \(\mathbb R^2\).

If \(p\in D^2\) satisfies \(\|p\|<1\), choose \(\varepsilon>0\) with \(B(p,\varepsilon)\subset D^2\). This is an open neighborhood of \(p\) in \(D^2\) homeomorphic to an open subset of \(\mathbb R^2\).

Now let \(p\in\partial D^2=S^1\). After a rotation we may assume \(p=(1,0)\). For sufficiently small \(\varepsilon\), the neighborhood \(D^2\cap B(p,\varepsilon)\) is carried homeomorphically to an open subset of the closed half-plane
\[
H^2=\{(u,v):v\ge0\}.
\]
One explicit chart is obtained by polar coordinates near \(p\): write a nearby point uniquely as
\[
(r\cos\theta,r\sin\theta),
\]
with \(r\le1\) and \(|\theta|<\delta\), and send it to
\[
(\theta,1-r).
\]
For sufficiently small \(\delta\) this is a homeomorphism onto an open subset of \(H^2\), with \(p\mapsto(0,0)\).

Thus every point has a neighborhood modeled on \(\mathbb R^2\) or \(H^2\), so \(D^2\) is a 2-manifold with boundary. Its boundary in this sense is the usual circle \(S^1\).
:::
