---
schema: qual/card@1
id: T-DEFFHHF
kind: theorem
title: The FHHF theorem, on functors and cohomology
classification:
  areas:
  - algebraic-geometry
  topics:
  - Homological Algebra
  - Exact Functors
  - Complexes
relations:
- kind: uses
  target: D-DEFCPLX
- kind: uses
  target: D-DEFEXACT
review: draft
prompts:
- State the FHHF theorem.
- Why do exact functors commute with cohomology?
- Give a use of it in computing sheaf cohomology.
---

::: {.theorem title="FHHF"}
Let $F: \mca \to \mcb$ be an additive functor of abelian categories and $C^\bullet$ a complex in $\mca$, so that $F(C^\bullet)$ is a complex in $\mcb$.

(i) If $F$ is right exact there is a natural morphism $F(H^i(C^\bullet)) \to H^i(F(C^\bullet))$.

(ii) If $F$ is left exact there is a natural morphism the other way, $H^i(F(C^\bullet)) \to F(H^i(C^\bullet))$.

(iii) If $F$ is exact both are isomorphisms, $F(H^i(C^\bullet)) \cong H^i(F(C^\bullet))$.
:::

::: {.remark}
For (ii): from $H^i(C^\bullet) = \ker\delta^i/\im\delta^{i-1}$ one has $0 \to \im\delta^{i-1} \to \ker\delta^i \to H^i \to 0$, and applying the left exact $F$ gives $0 \to F(\im\delta^{i-1}) \to F(\ker\delta^i) \to FH^i$.
Comparing with the corresponding sequence for $F(C^\bullet)$ needs one intermediate fact: a left exact $F$ commutes with kernels, giving a natural monomorphism $\im F(f) \to F(\im f)$ via $\coker F(f) \to F(\coker f)$, and
\[
\im F(f) = \ker\qty(\coker F(f)) \to \ker\qty(F(\coker f)) \cong F(\ker \coker f) = F(\im f) .
\]
The resulting diagram induces the map by universal properties.
Part (i) is the same argument on $0 \to H^i \to \coker\delta^{i-1}\to \im\delta^i \to 0$ with the arrows reversed.
For (iii), an exact $F$ commutes with both kernels and cokernels, so $F(\ker\delta^i) = \ker F(\delta^i)$ and $F(\im\delta^{i-1}) = \im F(\delta^{i-1})$, and the quotients agree.

The slogan is that exact functors commute with cohomology, and the direction of the map in the inexact cases is worth memorising rather than re-deriving.
The standard application is that filtered colimits are exact in $\mods{A}$, so $H^i$ commutes with filtered direct systems of sheaves --- which is how one reduces cohomology computations to finitely generated pieces.
:::
