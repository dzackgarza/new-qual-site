---
schema: qual/card@1
id: E-HAT-3.D-1
kind: problem
title: "Topological groups with finite CW structure are manifolds"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.D, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that a topological group with a finite-dimensional CW structure is an orientable manifold.
[Consider the homeomorphisms $x \mapsto gx$ or $x \mapsto xg$ for fixed $g$ and varying $x$ in the group.]

::: {.solution}
Let $G$ be a topological group with a finite-dimensional CW structure, and let $d$ be the largest dimension of a cell of $G$.

Choose a $d$-cell $e^d$. Since there are no cells of dimension larger than $d$, the union of all cells other than $e^d$ is a subcomplex, hence closed. Therefore the open cell $e^d$ is an open subset of $G$, homeomorphic to $\mathbb R^d$. Choose a point $x\in e^d$.

For any $y\in G$, left multiplication by
\[
g=yx^{-1}
\]
is a homeomorphism
\[
L_g:G\to G,
\qquad z\mapsto gz,
\]
carrying $x$ to $y$. Hence
\[
L_g(e^d)
\]
is an open neighborhood of $y$ homeomorphic to $\mathbb R^d$. Thus every point of $G$ has a Euclidean $d$-neighborhood, so $G$ is a $d$-manifold.

It remains to orient it. Since a CW complex is locally path-connected, each connected component of $G$ is path-connected. First orient the identity component $G_0$. Choose an orientation at one point, say the identity $e$, and transport it to $g\in G_0$ by the local homeomorphism $L_g$. This is well-defined coherently: if $g,h\in G_0$, then the transition between the translated charts is a left translation
\[
L_hL_g^{-1}=L_{hg^{-1}}.
\]
Because $hg^{-1}\in G_0$, choose a path $\gamma$ from $e$ to $hg^{-1}$. The family
\[
L_{\gamma(t)}
\]
is an isotopy from the identity homeomorphism to $L_{hg^{-1}}$. An isotopy cannot reverse the local orientation class, so all transition maps preserve the transported orientations. Hence $G_0$ is orientable.

Every other component is a left coset $aG_0$ and is homeomorphic to $G_0$ by $L_a$, so transport the orientation of $G_0$ to each component. Therefore the whole manifold $G$ is orientable.

Thus
\[
\boxed{\text{every topological group with a finite-dimensional CW structure is an orientable manifold}.}
\]
:::
