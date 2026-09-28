---
schema: qual/card@1
id: D-0QSI0
kind: definition
title: Stalks and germs
classification:
  areas:
  - algebraic-geometry
  topics:
  - Stalks
  - Sheaves
relations:
- kind: uses
  target: D-RCCFY
review: draft
prompts:
- What is the stalk of a sheaf?
- What is a germ?
- Show that the stalk at $p$ of the sheaf of holomorphic functions on an $n$-dimensional complex manifold is the ring $\CC\{z_1, \ldots, z_n\}$ of convergent power series.
- Show that for a real smooth manifold the Taylor map from the stalk of $C^\infty$ functions at $p$ to $\RR[[x_1, \ldots, x_n]]$ has a nonzero kernel.
- For an affine variety $X$ and $p \in X$, show that $\OO_{X,p} \cong A(X)_{\mfm_p}$.
- Give a morphism of sheaves that is surjective on stalks but not on global sections.
---

::: {.definition title="Stalk"}
For a presheaf $\mcf$ on $X$ and a point $p$,
$$
\mcf_p \da \colim_{U \ni p} \mcf(U) ,
$$
the colimit over open neighbourhoods of $p$ ordered by reverse inclusion.
An element of $\mcf_p$ is a \dfn{germ} of a section at $p$: a pair $(U, s)$ with $s \in \mcf(U)$, where two pairs are identified when the sections agree on some smaller neighbourhood.
:::

::: {.remark}
The open neighbourhoods of $p$ form a directed set under reverse inclusion, so the colimit is filtered.
Filtered colimits of abelian groups are exact, so $\mcf\mapsto\mcf_p$ is an exact functor on sheaves of abelian groups.
A sequence of sheaves of abelian groups on $X$ is exact if and only if it is exact on the stalk at every point of $X$; in particular, a morphism of sheaves is injective, surjective, or an isomorphism if and only if it is so on every stalk.

For the sheaf $C^\infty$ of smooth functions on $\RR$, the map $C^\infty(\RR)\to C^\infty_0$ is not injective: a nonzero smooth function supported in $[1,2]$ has germ $0$ at $0$.
The germ of $f$ at $0$ determines every derivative $f^{(k)}(0)$, but the derivatives do not determine the germ: the function equal to $e^{-1/x^2}$ for $x>0$ and to $0$ for $x\le0$ has Taylor series $0$ at $0$ and a nonzero germ at $0$.
:::
