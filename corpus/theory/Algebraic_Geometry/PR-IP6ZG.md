---
schema: qual/card@1
id: PR-IP6ZG
kind: proposition
title: Direct limits of sheaves, and the Noetherian hypothesis that removes the sheafification
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

::: {.definition}
For a direct system $\ts{\mcf_i}$ of sheaves on $X$ over a directed index set, $\colim_i \mcf_i$ is the sheafification of
\[
U \longmapsto \colim_i \mcf_i(U) .
\]
Inverse limits are defined the same way, and there the presheaf $U \mapsto \lim_i \mcf_i(U)$ is already a sheaf.
:::

::: {.proposition}
If $X$ is a Noetherian topological space, the presheaf $U \mapsto \colim_i \mcf_i(U)$ is already a sheaf, and
\[
\Gamma\qty{X ; \colim_i \mcf_i} = \colim_i \Gamma(X ; \mcf_i) .
\]
:::

::: {.proof}
On a Noetherian space every open set is quasicompact, so it suffices to verify the sheaf axioms against *finite* covers.
Both axioms together say that
\[
\mcf(U) \to \prod_{i=1}^n \mcf(U_i) \rightrightarrows \prod_{i,j} \mcf(U_i \intersect U_j)
\]
is an equalizer, and for a finite cover these are finite products, so the whole diagram is a finite limit.
Filtered colimits of abelian groups are exact and commute with finite limits, so the colimit of the equalizer diagrams is again an equalizer.
The displayed identity is that statement for the cover consisting of $X$ itself, once the presheaf colimit is known to be the sheaf colimit.
:::

::: {.remark}
Both the hypothesis and its absence are the point.
$\Gamma$ is only left exact in general, and a colimit is a right-exact operation, so there is no reason for them to commute; the Noetherian condition supplies quasicompactness, which converts the sheaf axioms into a finite limit, and filtered colimits commute with those.

Dropping the hypothesis breaks the conclusion.
A section of the colimit is locally a section of some $\mcf_i$, but the index $i$ may depend on the open set, and with infinitely many opens in an irreducible cover there need be no single $i$ working everywhere — so the glued section lives in the sheafification and in no $\mcf_i$.
Quasicompactness is exactly what bounds the number of indices to be reconciled.

The same argument, run on Čech complexes, gives the cohomological version: on a Noetherian space $H^k(X ; \wait)$ commutes with filtered direct limits of sheaves.
:::
