---
schema: qual/card@1
id: D-SCHSUB
kind: definition
title: Open and closed subschemes, and closed immersions
classification:
  areas:
  - algebraic-geometry
  topics:
  - Subschemes
  - Closed Immersions
  - Ideal Sheaves
relations:
- kind: uses
  target: D-AN662
review: draft
prompts:
- What is an open subscheme? A closed subscheme?
- What do closed subschemes of an affine scheme correspond to?
- Give an irreducible scheme that is not reduced, and two distinct schemes with the same support.
- What is the $n$th infinitesimal neighbourhood of a prime $\mfp \in \Spec A$?
- Show that a scheme is reduced if and only if all its stalks are reduced.
---

::: {.definition}
An \dfn{open subscheme} of $X$ is an open $U \subseteq \abs{X}$ with $\OO_U \da \ro{\OO_X}{U}$; every open subset of a scheme is a scheme in exactly one way.

A \dfn{closed immersion} $i: Z \to X$ is a morphism which is a homeomorphism onto a closed subset and for which $i^\sharp: \OO_X \to i_* \OO_Z$ is surjective.
A \dfn{closed subscheme} is an equivalence class of closed immersions into $X$.
:::

::: {.proposition}
Closed subschemes of $\Spec A$ correspond exactly to ideals $\mfa \normal A$, via $Z = \Spec(A/\mfa)$.
In general, closed subschemes of $X$ correspond to quasicoherent ideal sheaves $\mci \subseteq \OO_X$, with $\OO_Z = \OO_X/\mci$.
:::

::: {.proposition title="Closed subscheme sequences"}
For a closed immersion $i: Z \to X$ with ideal sheaf $\mci$ there is an exact sequence of $\OO_X$-modules
$$
0 \to \mci \to \OO_X \to i_* \OO_Z \to 0 ,
$$
and tensoring with a locally free $\OO_X$-module $\mce$ keeps it exact: $0 \to \mci \tensor \mce \to \mce \to i_*(i^* \mce) \to 0$.
If $Z = D$ is an effective Cartier divisor, then $\mci = \OO_X(-D) = \OO_X(D)^\vee$, giving
$$
0 \to \OO_X(-D) \to \OO_X \to \OO_D \to 0 , \qquad 0 \to \mcl(-D) \to \mcl \to \ro{\mcl}{D} \to 0
$$
for every invertible sheaf $\mcl$.
[@Har10a, Proposition II.6.18]
:::

::: {.remark}
An open subset carries a unique induced scheme structure, while a closed subset can carry many closed-subscheme structures: $V(x)$ and $V(x^2)$ in $\AA^1$ have the same support and different ideal sheaves.

For a closed immersion $i$, the map on global sections $\OO_X(X) \to \OO_Z(Z)$ need not be surjective: for $Z=\ts{0,\infty}\subseteq\PP^1_k$ with its reduced structure, it is the diagonal $k\to k\times k$.

A closed subscheme of an open subscheme is a \dfn{locally closed subscheme}; an immersion is a morphism that is an isomorphism onto a locally closed subscheme ([[D-MORIMM]]).
:::
