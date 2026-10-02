---
schema: qual/card@1
id: T-DEFFHHF
kind: theorem
title: The FHHF theorem, on functors and cohomology
slogan: 'Exact functors commute with cohomology; right exactness gives $F(H^i)\to H^i(F(C^\bullet))$, and left exactness gives the reverse map.'
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
Comparing with the corresponding sequence for $F(C^\bullet)$ uses the natural monomorphism
$$
\im F(f)\hookrightarrow F(\im f).
$$
Indeed, if $f\colon A\to B$ and $q\colon B\to\coker f$, then left exactness gives
$$
F(\ker q)\cong\ker F(q),
$$
while $F(q)\circ F(f)=0$, so $\im F(f)\subseteq\ker F(q)=F(\im f)$.
The resulting diagram induces the map by universal properties.
Part (i) is the same argument on $0 \to H^i \to \coker\delta^{i-1}\to \im\delta^i \to 0$ with the arrows reversed.
For (iii), an exact $F$ commutes with both kernels and cokernels, so $F(\ker\delta^i) = \ker F(\delta^i)$ and $F(\im\delta^{i-1}) = \im F(\delta^{i-1})$, and the quotients agree.

Exact functors commute with cohomology; for one-sided exact functors, the direction of the natural map is determined by which kernels or cokernels the functor preserves.
For complexes of $A$-modules, exactness of filtered colimits therefore gives
$$
\colim_j H^i(C_j^\bullet)\cong H^i\!\left(\colim_j C_j^\bullet\right).
$$
For sheaf cohomology an additional geometric hypothesis is needed: on a Noetherian space, filtered colimits of sheaves commute with $H^i(X,-)$ by [[PR-IP6ZG]].
:::
