---
schema: qual/card@1
id: P-AGH345PICH1
kind: problem
title: The Picard group as first cohomology of the sheaf of units
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Picard Group
  - Invertible Sheaves
relations: []
review: draft
---

::: {.problem}
For any ringed space $(X, \mco_X)$, let $\Pic X$ be the group of isomorphism classes of invertible sheaves (II, §6). Show that $\Pic X \cong H^1(X, \mco_X^*)$, where $\mco_X^*$ denotes the sheaf whose sections over an open set $U$ are the units in the ring $\Gamma(U, \mco_X)$, with multiplication as the group operation.

Hint: For any invertible sheaf $\mcl$ on $X$, cover $X$ by open sets $U_i$ on which $\mcl$ is free, and fix isomorphisms $\varphi_i: \mco_{U_i} \iso \ro{\mcl}{U_i}$.
Then on $U_i \intersect U_j$, we get an isomorphism $\varphi_i\inv \circ \varphi_j$ of $\mco_{U_i \intersect U_j}$ with itself.
These isomorphisms give an element of $\check{H}^1(\mathfrak{U}, \mco_X^*)$.
Now use (Ex.
4.4).
:::

::::: {.solution}
<1>1. For an open cover $\mathfrak{U} = \{U_i\}$ of $X$, isomorphism classes of invertible sheaves free on every $U_i$ correspond bijectively to $\check{H}^1(\mathfrak{U}, \mco_X^*)$, compatibly with tensor products.

::: {.proof}
For such $\mcl$ fix $\varphi_i \colon \mco_{U_i} \iso \mcl|_{U_i}$ as in the hint.
On $U_i \cap U_j$ the automorphism $\varphi_i^{-1} \circ \varphi_j$ of $\mco_{U_i \cap U_j}$ is multiplication by a unit $g_{ij} \in \Gamma(U_i \cap U_j, \mco_X^*)$, and $g_{ij} g_{jk} = g_{ik}$ on $U_i \cap U_j \cap U_k$, so $(g_{ij})$ is a Čech $1$-cocycle.
Replacing each $\varphi_i$ by $\varphi_i \circ h_i$ with $h_i \in \Gamma(U_i, \mco_X^*)$, or $\mcl$ by an isomorphic sheaf, changes $(g_{ij})$ by the coboundary of $(h_i)$; a cocycle that is a coboundary allows the $\varphi_i$ to be chosen compatibly, so they glue to an isomorphism $\mco_X \iso \mcl$.
Every cocycle arises by gluing the sheaves $\mco_{U_i}$ along multiplication by $g_{ij}$, and the cocycle of $\mcl \otimes \mcl'$ is the product of the cocycles.
:::

<1>2. $\Pic X \cong \check{H}^1(X, \mco_X^*) = \varinjlim_{\mathfrak{U}} \check{H}^1(\mathfrak{U}, \mco_X^*)$.

::: {.proof}
Every invertible sheaf is free on the members of some open cover, and the bijections of step <1>1 commute with the refinement maps.
:::

<1>3. Q.E.D.

::: {.proof}
By Exercise III.4.4 the natural map $\check{H}^1(X, \mcf) \to H^1(X, \mcf)$ is an isomorphism for every sheaf of abelian groups $\mcf$; with step <1>2 this gives $\Pic X \cong H^1(X, \mco_X^*)$.
The comparison is needed because $\mco_X^*$ is not a quasicoherent sheaf, so the equality of Čech and derived-functor cohomology for affine covers of Noetherian separated schemes does not apply to it.
:::
:::::
