---
schema: qual/card@1
id: T-COHAFF
kind: theorem
title: Higher cohomology vanishes on an affine scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Affine Schemes
  - Quasicoherent Sheaves
relations:
- kind: uses
  target: D-COHFLQ
- kind: related-to
  target: T-5IOUR
review: draft
prompts:
- Compute the cohomology of a quasicoherent sheaf on an affine scheme.
- Which hypothesis in affine vanishing is load-bearing?
---

::: {.theorem}
Let $X = \Spec A$ with $A$ Noetherian and $\mcf \in \QCoh(X)$.
Then $H^0(X, \mcf) = \globsec{X;\mcf}$ and $H^i(X, \mcf) = 0$ for all $i > 0$.
:::

::: {.remark title="The proof in one line"}
Put $M = \globsec{X;\mcf}$, so $\mcf \cong \tilde M$.
Take an injective resolution $M \injects I^\bullet$ in $\amod$ and sheafify: each $\tilde{I^j}$ is flasque, hence acyclic, so $\tilde{I^\bullet}$ computes the cohomology.
Applying $\globsec{X;\wait}$ returns the original exact complex $M \injects I^\bullet$, and its higher cohomology is zero.
:::

::: {.remark title="Hypotheses"}
Quasicoherence is the load-bearing hypothesis, and it is where the whole argument lives: the theorem is false for general sheaves of abelian groups, which see the topology of $X$ rather than the module $M$.
Noetherianness is only used to know that $\tilde I$ is flasque for $I$ injective; the statement is true for any affine scheme, but that version is harder.

This is the direction of Serre's criterion that is a theorem about affines, and the other direction is the criterion proper.
It is also the reason every computation is done on an affine cover: on the pieces of the cover there is nothing above degree $0$, so all the cohomology comes from the gluing, which is exactly what the Čech complex records.
:::
