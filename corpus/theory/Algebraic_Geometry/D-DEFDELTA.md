---
schema: qual/card@1
id: D-DEFDELTA
kind: definition
title: $\delta$-functors, universality, and effaceability
classification:
  areas:
  - algebraic-geometry
  topics:
  - Homological Algebra
  - Derived Functors
  - Delta Functors
relations:
- kind: uses
  target: D-DEFDERIV
review: draft
prompts:
- What is a $\delta$-functor?
- What does it mean for a functor to be effaceable, and what does effaceability buy you?
- How do you recognise a given cohomology theory as the derived functor cohomology?
---

::: {.definition title="delta functor"}
Let $\mca, \mcb$ be abelian categories.
A covariant \dfn{$\delta$-functor} from $\mca$ to $\mcb$ is a collection of functors $T = (T^i)_{i\geq 0}$ together with a boundary morphism $\delta^i: T^i(A'') \to T^{i+1}(A')$ for every short exact sequence $0 \to A' \to A \to A'' \to 0$, such that

(i) each short exact sequence gives a long exact sequence
\[
0 \to T^0(A') \to T^0(A) \to T^0(A'') \mapsvia{\delta^0} T^1(A') \to T^1(A) \to \cdots ,
\]

(ii) for each morphism of short exact sequences the induced maps commute with the $\delta^i$.
:::

::: {.definition title="effaceable"}
An additive functor $F: \mca \to \mcb$ is \dfn{effaceable} if for each object $A$ there is a monomorphism $u: A \injects M$ with $F(u) = 0$, and **coeffaceable** if there is an epimorphism $u: P \surjects A$ with $F(u) = 0$.
:::

::: {.remark}
A $\delta$-functor is **universal** if it maps uniquely to every other $\delta$-functor agreeing with it in degree $0$.
Grothendieck's criterion is that a $\delta$-functor whose $T^i$ are effaceable for $i>0$ is universal, and derived functors are effaceable because every $A$ embeds in an injective, which kills the higher $R^iF$.

This is an identification tool, not abstraction for its own sake.
It is how one proves that Čech cohomology on a nice space, or $\Ext$ computed in either variable, agrees with the derived functor definition: check both theories are $\delta$-functors, check they agree in degree $0$, check effaceability.
:::
