---
schema: qual/card@1
id: D-PTIW0
kind: definition
title: Čech cohomology and the comparison with sheaf cohomology
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Cech Cohomology
relations:
- kind: uses
  target: PR-C9ZEK
review: draft
prompts:
- Define Čech cohomology.
- When does Čech cohomology agree with derived functor cohomology?
- What is the Leray map, and for which covers is it an isomorphism?
- How does Čech cohomology of a Noetherian separated scheme compare with derived functor cohomology, and with singular cohomology?
---

::: {.definition title="Čech complex"}
For an indexed open cover $\mcu = \theset{U_i}$ of a topological space $X$, with an order on its index set, and a sheaf of abelian groups $\mcf$, put
$$
C^p(\mcu, \mcf) = \prod_{i_0 < \cdots < i_p} \mcf(U_{i_0} \intersect \cdots \intersect U_{i_p}) ,
$$
with the alternating-sum differential.
$\check{H}^p(\mcu,\mcf)$ is its cohomology [@Har10a, Chapter III, §4].
:::

::: {.definition title="Leray map"}
For any open cover $\mcu$ of $X$ and sheaf of abelian groups $\mcf$ there is a natural map
$$
\check{H}^p(\mcu, \mcf) \to H^p(X, \mcf),
$$
the \dfn{Leray map}, induced by comparing the Čech resolution of $\mcf$ by the sheaves $\prod j_* \mcf|_{U_{i_0 \cdots i_p}}$ with an injective resolution.
It is always an isomorphism in degree $0$ and injective in degree $1$, and it is an isomorphism in all degrees when $H^q(U_{i_0} \cap \cdots \cap U_{i_p}, \mcf) = 0$ for all $q > 0$ and all finite intersections; see the [Čech comparison theorems](https://stacks.math.columbia.edu/tag/01EO).
:::

::: {.theorem title="Leray"}
If $X$ is a noetherian separated scheme, $\mcu$ is a finite affine open cover, and $\mcf$ is quasi-coherent, then
$$
\check{H}^p(\mcu,\mcf) \cong H^p(X,\mcf)
$$
for all $p$ [@Har10a, Theorem III.4.5].
:::

::: {.proposition title="Affine-cover bound"}
If a noetherian separated scheme $X$ is covered by $n+1$ affine opens, then $H^p(X,\mcf)=0$ for $p>n$ and every quasi-coherent $\mcf$.
The comparison theorem applies because finite intersections of these affine opens are affine; the resulting Čech complex has no terms beyond degree $n$.
In particular the standard cover of $\PP^n$ gives this bound for projective space [@Har10a, Theorem III.4.5].
:::

::: {.example title="The separatedness hypothesis in the bound"}
Glue two copies $V_1,V_2$ of $\AA_k^2$ by the identity on their common punctured plane $W$.
The resulting scheme $X$ is noetherian and has a two-member affine cover.
The open Mayer--Vietoris sequence gives $H^2(X,\OO_X)\cong H^1(W,\OO_W)$, since the positive-degree cohomology of both affine pieces vanishes.
This sequence follows by applying sections to a flasque resolution: in each degree the difference map from sections on $V_1,V_2$ onto sections on $W$ is surjective by flasqueness.
The group on the right is nonzero by [[P-AGH343PUNCTUREDPLANE]].
Thus a two-affine cover alone does not imply vanishing in degree two.
:::

::: {.remark}
An arbitrary open cover need not compute the cohomology, even for a noetherian separated scheme and a quasi-coherent sheaf.
For the cover $\mcu = \{\PP_k^1\}$ of the projective line over a field $k$ by itself, $\check{H}^1(\mcu,\OO(-2))=0$ because the Čech complex has a single term, while $H^1(\PP_k^1,\OO(-2))\cong k$ [@Har10a, Theorem III.5.1].
:::

::: {.remark}
The affine-cover comparison is a statement in the Zariski topology about quasi-coherent sheaves.
On an irreducible topological space, a constant abelian sheaf is flasque: every nonempty open is connected, so its restriction maps are identities or surjections onto zero.
Its positive-degree sheaf cohomology therefore vanishes [@Har10a, Proposition III.2.5].
For a complex variety $X$, singular cohomology is sheaf cohomology of the constant sheaf in the analytic topology, $H^i_{\operatorname{sing}}(X(\CC),\ZZ)\cong H^i(X^{\operatorname{an}},\underline{\ZZ})$, since $X^{\operatorname{an}}$ is locally contractible.
For $X=\PP^1_\CC$, the Zariski group $H^2(X,\underline{\ZZ})$ is $0$, while $H^2(X^{\operatorname{an}},\underline{\ZZ})\cong H^2(S^2,\ZZ)\cong\ZZ$.
:::
