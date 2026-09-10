---
schema: qual/card@1
id: E-RKSXA
kind: problem
title: The boundary of a surface with boundary is intrinsic
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
---

::: {.exercise}

Let $H^2$ be the subspace of $\mathbb{R}^2$ consisting of all points $(x_1, x_2)$ with $x_2 \geq 0$.
A 2-manifold with boundary (or surface with boundary) is a Hausdorff space $X$ with a countable basis such that each point $x$ of $X$ has a neighborhood homeomorphic with an open set of $\mathbb{R}^2$ or $H^2$.
The boundary of $X$ (denoted $\partial X$) consists of those points $x$ such that $x$ has no neighborhood homeomorphic with an open set of $\mathbb{R}^2$.

(a) Show that no point of $H^2$ of the form $(x_1, 0)$ has a neighborhood (in $H^2$) that is homeomorphic to an open set of $\mathbb{R}^2$.

(b) Show that $x \in \partial X$ if and only if there is a homeomorphism $h$ mapping a neighborhood of $x$ onto an open set of $H^2$ such that $h(x) \in \mathbb{R} \times 0$.

(c) Show that $\partial X$ is a 1-manifold.
:::

::: {.solution}
(a) Let \(q=(q_1,0)\in\partial H^2\). We use local homology. For a sufficiently small half-disk \(D_+\) about \(q\), both \(D_+\) and \(D_+-\{q\}\) are contractible: the punctured half-disk deformation retracts onto its semicircular boundary arc. Hence the long exact sequence of the pair gives
\[
H_2(D_+,D_+-\{q\})=0.
\]
By excision this is the local group
\[
H_2(H^2,H^2-\{q\})=0.
\]

By contrast, if \(z\) lies in an open subset \(V\subset\mathbb R^2\), excision to a small disk about \(z\) gives
\[
H_2(V,V-\{z\})\cong H_2(D^2,D^2-\{0\})\cong\mathbb Z.
\]
Local homology is preserved by homeomorphisms. Therefore no neighborhood of \(q\) in \(H^2\) can be homeomorphic to an open subset of \(\mathbb R^2\).

(b) Suppose first that a chart
\[
h:U\longrightarrow V\subset H^2
\]
satisfies \(h(x)\in\mathbb R\times\{0\}\). By part (a), \(h(x)\) has no neighborhood in \(H^2\) homeomorphic to an open subset of \(\mathbb R^2\); transporting this statement through \(h\), neither does \(x\). Hence \(x\in\partial X\).

Conversely, let \(x\in\partial X\). By the definition of a manifold with boundary, \(x\) has a chart to an open subset of either \(\mathbb R^2\) or \(H^2\). The first possibility is excluded by the definition of \(\partial X\). Thus there is a half-plane chart \(h:U\to V\subset H^2\). If \(h(x)\) had positive second coordinate, a small Euclidean disk about \(h(x)\) would lie in \(H^2\), giving an ordinary \(\mathbb R^2\)-neighborhood of \(x\), again a contradiction. Therefore \(h(x)\in\mathbb R\times\{0\}\).

(c) Let \(x\in\partial X\) and choose a chart as in (b), with \(h(x)=(a,0)\). Shrinking the chart if necessary, take
\[
V=(a-\varepsilon,a+\varepsilon)\times[0,\varepsilon)
\]
inside its image. By part (b),
\[
h(U\cap\partial X)=V\cap(\mathbb R\times\{0\})
=(a-\varepsilon,a+\varepsilon)\times\{0\}.
\]
Hence \(U\cap\partial X\) is an open neighborhood of \(x\) in \(\partial X\) homeomorphic to an open interval. Since \(\partial X\) is a subspace of the Hausdorff second-countable space \(X\), it is Hausdorff and second countable. Thus \(\partial X\) is a 1-manifold.
:::
