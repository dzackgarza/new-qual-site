---
schema: qual/card@1
id: D-COHGODEMENT
kind: definition
title: The Godement resolution
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flasque Sheaves
  - Resolutions
  - Sheaf Cohomology
relations:
- kind: uses
  target: D-COHFLQ
review: draft
prompts:
- What is the Godement resolution?
---

::: {.definition title="Godement resolution"}
Let $\mcf$ be a sheaf of abelian groups on a topological space $X$.
Put
\[
\mathcal{G}^0(\mcf)(U) = \prod_{x \in U} \mcf_x ,
\]
the sheaf of all, not necessarily continuous, sections of the espace étalé, with the injection $\mcf \to \mathcal{G}^0(\mcf)$ sending $s$ to its germs.
Inductively, with $\mathcal{Z}^0 = \mcf$ and $\mathcal{Z}^{n+1} = \operatorname{coker}\big(\mathcal{Z}^{n} \to \mathcal{G}^0(\mathcal{Z}^{n})\big)$, set $\mathcal{G}^n(\mcf) = \mathcal{G}^0(\mathcal{Z}^n)$ with differential $\mathcal{G}^n(\mcf) \to \mathcal{Z}^{n+1} \to \mathcal{G}^{n+1}(\mcf)$.
The complex $0 \to \mcf \to \mathcal{G}^0(\mcf) \to \mathcal{G}^1(\mcf) \to \cdots$ is the \dfn{Godement resolution}.
:::

::: {.proposition}
1. Each $\mathcal{G}^n(\mcf)$ is flasque, since a product of stalks over a smaller open set extends by zero to a larger one.

2. The Godement resolution is exact and functorial in $\mcf$, and exact as a functor of $\mcf$, because it is built from stalks.

3. Flasque sheaves are acyclic, so $H^i(X, \mcf) = H^i\big(\Gamma(X, \mathcal{G}^\bullet(\mcf))\big)$.
:::

::: {.remark}
Functoriality is what makes the Godement resolution useful beyond computing cohomology: it gives canonical complexes, compatible with morphisms and pushforwards, that represent $R\Gamma$ and $Rf_*$ without choosing injective resolutions.
:::
