---
schema: qual/card@1
id: PR-IP6ZG
kind: definition
title: Filtered colimits of sheaves on a Noetherian space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Sheafification
  - Limits And Colimits
relations:
- kind: uses
  target: D-RCCFY
- kind: uses
  target: T-3VX80
review: draft
prompts:
- How is the direct limit of a direct system of sheaves defined?
- On a Noetherian space, why is the presheaf colimit already a sheaf?
- When does $\Gamma$ commute with a direct limit of sheaves?
---

On a Noetherian space, sectionwise filtered colimits are already sheaves and commute with sections and sheaf cohomology.

::: {.definition}
Let $\theset{\mcf_i}_{i\in I}$ be a directed system of sheaves of abelian groups on a topological space $X$.
Its colimit in the category of sheaves is the sheafification of the presheaf
$$
U \longmapsto \colim_i \mcf_i(U) .
$$
For an inverse system of sheaves, the sectionwise presheaf $U\mapsto\lim_i\mcf_i(U)$ is already a sheaf, so inverse limits are computed sectionwise.
:::

::: {.proposition}
If $X$ is a Noetherian topological space, the presheaf $U \mapsto \colim_i \mcf_i(U)$ is already a sheaf, and
$$
\Gamma\qty{X ; \colim_i \mcf_i} \cong \colim_i \Gamma(X ; \mcf_i) .
$$
More generally, for every $q\geq0$,
$$
H^q\qty{X;\colim_i\mcf_i}
\cong
\colim_i H^q(X;\mcf_i)
$$
[@Har77, Proposition III.2.9].
:::

::: {.proof}
On a Noetherian space every open set is quasicompact, so it suffices to verify the sheaf axioms against *finite* covers.
Both axioms together say that
$$
\mcf(U) \to \prod_{i=1}^n \mcf(U_i) \rightrightarrows \prod_{i,j} \mcf(U_i \intersect U_j)
$$
is an equalizer, and for a finite cover these are finite products, so the whole diagram is a finite limit.
Filtered colimits of abelian groups are exact and commute with finite limits, so the colimit of the equalizer diagrams is again an equalizer.
Thus the sectionwise colimit is a sheaf.
Evaluating it on $X$ gives the displayed formula for global sections; the same argument works on every open subset.
A complete proof of this sectionwise statement is given in [[P-AGH326COLIMINJECTIVE]], step 4.
:::

::: {.remark}
The finiteness used above is the quasicompactness of every open subset of a Noetherian space.
Without such a finiteness condition, local representatives of a section of the sheafified colimit can require unbounded indices over an infinite cover, so the sectionwise presheaf need not satisfy the sheaf axiom.

The cohomology statement is stronger than the finite-cover argument for sections.
One proof uses that filtered colimits are exact and that a filtered colimit of injective abelian sheaves on a Noetherian space is injective; the latter is proved in [[P-AGH326COLIMINJECTIVE]]. The resulting derived-functor comparison is the theorem used in [[P-AGH348COHDIM]], step 1.
:::
