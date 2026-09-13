---
schema: qual/card@1
id: T-DEFRAPL
kind: theorem
title: RAPL and LAPC, and the exactness of $\Hom$ and $\tensor$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Category Theory
  - Adjunctions
  - Limits and Colimits
  - Exact Functors
relations:
- kind: uses
  target: D-DEFADJ
- kind: uses
  target: D-DEFEXACT
review: draft
prompts:
- State RAPL and LAPC.
- Deduce that $\Hom_A(N,\wait)$ is left exact and $\wait\tensor_A N$ is right exact.
- Why does knowing which side of an adjunction a functor sits on settle its exactness?
---

::: {.theorem title="RAPL, LAPC"}
Let $(F,G)$ be an adjoint pair between categories in which limits and colimits exist, with $F$ the left adjoint.
Then **right adjoints preserve limits**,
\[
G\qty( \inverselim_i B_i ) \cong \inverselim_i G(B_i) ,
\]
and **left adjoints preserve colimits**,
\[
F\qty( \directlim_i A_i ) \cong \directlim_i F(A_i) .
\]
:::

::: {.remark}
The proof is a universal property check: applying $G$ to a diagram $B_i$ gives a diagram $G(B_i)$, and adjointness converts a cone on $G(B_i)$ with vertex $T$ into a cone on $B_i$ with vertex $F(T)$, hence a unique map $F(T) \to \inverselim B_i$, hence a unique $T \to G(\inverselim B_i)$.
That is exactly the universal property of $\inverselim G(B_i)$.
The colimit statement is the same argument run the other way.

The payoff is the exactness of the tensor-hom pair, with no diagram chase.
Kernels are limits and cokernels are colimits, so for the adjunction with $\wait\tensor_A N$ on the left and $\Hom_A(N,\wait)$ on the right: given $0 \to M' \to M \to M''$, one has $M' \cong \ker(M \to M'')$, so
\[
\Hom(N,M') \cong \Hom(N, \ker(M \to M'')) \cong \ker\qty( \Hom(N,M) \to \Hom(N,M'') ) ,
\]
which is left exactness of $\Hom_A(N,\wait)$.
Symmetrically, $\wait \tensor_A N$ preserves the cokernel and is therefore right exact.

This is the reason to remember which adjoint is which for every pair on this exam: $\pi^{-1}$ and $\pi^*$ are left adjoints and hence right exact, while $\pi_*$ is a right adjoint and hence only left exact --- and that one-sidedness of $\pi_*$ is precisely what higher direct images measure.
:::
