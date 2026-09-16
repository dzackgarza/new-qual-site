---
schema: qual/card@1
id: D-DEFACYC
kind: definition
title: Acyclic objects, and computing derived functors without injectives
classification:
  areas:
  - algebraic-geometry
  topics:
  - Homological Algebra
  - Derived Functors
  - Acyclicity
relations:
- kind: uses
  target: D-DEFDERIV
review: draft
prompts:
- What is an $F$-acyclic object?
- Can a resolution by non-injective objects compute $R^iF$?
---

::: {.definition title="acyclic"}
Let $\mca$ be an abelian category with enough injectives and $F: \mca \to \mcb$ a left exact additive functor, so that the $R^iF$ exist.
An object $A \in \mca$ is \dfn{$F$-acyclic} if the higher right derived functors vanish:
\[
R^iF(A) = 0 \text{ for all } i > 0 .
\]
The same definition applies to left derived functors and to contravariant $F$.
:::

::: {.remark}
Injective objects are $F$-acyclic for every $F$, and dually projectives are acyclic for left derived functors, but acyclicity is strictly weaker --- and that weakness is the point, because an $F$-acyclic resolution computes $R^iF$ just as well as an injective one does.

Every concrete cohomology computation on this exam runs on that fact.
Flasque sheaves are $\Gamma$-acyclic, so a flasque resolution computes $H^i(X;\mcf)$.
Free and projective modules are acyclic for $\wait \tensor_A N$, so a free resolution computes $\Tor$.
Quasicoherent sheaves on an affine scheme are $\Gamma$-acyclic, which is Serre's theorem and the reason Čech cohomology on an affine cover gives the right answer.
:::
