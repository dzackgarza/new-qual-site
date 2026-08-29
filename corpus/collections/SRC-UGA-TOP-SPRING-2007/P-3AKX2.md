---
schema: qual/card@1
id: P-3AKX2
kind: problem
title: $p^{-1}(U)$ is connected iff $i_*:\pi_1(U)\to\pi_1(S)$ is surjective
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Connectedness
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $S$ be a connected surface, and let $U$ be a connected open subset of $S$.
Let $p : \tilde S \to  S$ be the universal cover of $S$.
Show that $p\inv (U )$ is connected if and only if the homomorphism $i_\ast : \pi_1 (U ) \to \pi_1 (S)$ induced by the inclusion $i : U \to S$ is onto.
:::

::: {.solution}
<1>1. $p^{-1}(U)$ is a covering space of $U$ (the restriction of the universal cover $p$).
Proof: the preimage of an open set under a covering map is a covering space of that set.

<1>2. The connected components of $p^{-1}(U)$ are in bijection with the cosets of $\operatorname{im} i_*$ in $\pi_1(S)$.
Proof: for a covering space, the components of the preimage of a connected open set correspond to the orbits of $\pi_1(U)$ acting on the fiber, i.e. to the cosets $\pi_1(S)/\operatorname{im} i_*$ (the image of $\pi_1(U)$ under the inclusion).

<1>3. $p^{-1}(U)$ is connected iff it has exactly one component.
Proof: definition of connectedness.

<1>4. By <1>2, $p^{-1}(U)$ has one component iff $\pi_1(S)/\operatorname{im} i_*$ has one element iff $\operatorname{im} i_* = \pi_1(S)$.
Proof: the number of cosets is $1$ exactly when the subgroup is the whole group.

<1>5. Hence $p^{-1}(U)$ is connected iff $i_*$ is surjective.
Proof: <1>3 and <1>4.

<1>6. Q.E.D.
Proof: <1>5.
:::
