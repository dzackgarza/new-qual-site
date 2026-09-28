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
$$
0 \to T^0(A') \to T^0(A) \to T^0(A'') \mapsvia{\delta^0} T^1(A') \to T^1(A) \to \cdots ,
$$

(ii) for each morphism of short exact sequences the induced maps commute with the $\delta^i$.
:::

::: {.definition title="effaceable"}
An additive functor $F: \mca \to \mcb$ is \dfn{effaceable} if for each object $A$ there is a monomorphism $u: A \injects M$ with $F(u) = 0$, and \dfn{coeffaceable} if for each object $A$ there is an epimorphism $u: P \surjects A$ with $F(u) = 0$.
:::

::: {.definition title="universal delta functor"}
A covariant $\delta$-functor $T=(T^i)$ from $\mca$ to $\mcb$ is \dfn{universal} if for every $\delta$-functor $T'=(T'^i)$ from $\mca$ to $\mcb$, every natural transformation $f^0\colon T^0\to T'^0$ extends uniquely to a sequence of natural transformations $f^i\colon T^i\to T'^i$ commuting with the $\delta^i$.
:::

::: {.theorem title="Grothendieck"}
A covariant $\delta$-functor $T$ with $T^i$ effaceable for every $i>0$ is universal [@Har10a, Theorem III.1.3A].
If $\mca$ has enough injectives and $F$ is left exact, then $(R^iF)_{i\ge0}$ is a universal $\delta$-functor with $R^0F\cong F$, since every $A$ embeds in an injective object $I$ and $R^iF(I)=0$ for $i>0$.
:::

::: {.remark}
Two universal $\delta$-functors with isomorphic degree-$0$ functors are isomorphic.
For $A$-modules $M,N$, the groups $\Ext^i_A(M,N)$ computed from a projective resolution of $M$ form, as functors of $N$, a $\delta$-functor with $\Ext^0_A(M,\wait)=\Hom_A(M,\wait)$ that vanishes on injective $N$ in positive degrees; so they are the right derived functors of $\Hom_A(M,\wait)$.
:::
