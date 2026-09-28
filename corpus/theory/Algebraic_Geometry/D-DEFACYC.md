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
$$
R^iF(A) = 0 \text{ for all } i > 0 .
$$
The same definition applies to left derived functors and to contravariant $F$.
:::

::: {.proposition}
If $0\to A\to L^\bullet$ is a resolution of $A$ by $F$-acyclic objects, then $R^iF(A)\cong h^i(F(L^\bullet))$ for all $i\ge0$ [@Har10a, Proposition III.1.2A].
:::

::: {.remark}
Injective objects are $F$-acyclic for every left exact $F$, and projective objects are acyclic for the left derived functors of every right exact functor.
An acyclic object need not be injective: on a one-point space every sheaf is $\Gamma$-acyclic, and the constant sheaf $\ZZ$ is not an injective abelian group.

Flasque sheaves are $\Gamma$-acyclic, so a flasque resolution computes $H^i(X;\mcf)$.
Free and projective modules are acyclic for $\wait \tensor_A N$, so a free resolution computes $\Tor$.
Quasicoherent sheaves on an affine scheme are $\Gamma$-acyclic by Serre's theorem; hence for a Noetherian separated scheme $X$, an open affine cover $\mathfrak U$, and a quasicoherent sheaf $\mcf$, the Čech complex of $\mathfrak U$ computes $H^i(X,\mcf)$ [@Har10a, Theorem III.4.5].
:::
