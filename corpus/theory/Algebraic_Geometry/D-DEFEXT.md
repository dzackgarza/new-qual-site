---
schema: qual/card@1
id: D-DEFEXT
kind: definition
title: The $\Ext$ functors, in either variable
classification:
  areas:
  - algebraic-geometry
  topics:
  - Homological Algebra
  - Derived Functors
  - Ext
relations:
- kind: uses
  target: D-DEFDERIV
review: draft
prompts:
- Give the two definitions of $\Ext^i_A(M,N)$, and say why they agree.
- What does $\Ext^1$ classify?
- Compute $\Ext^1_\ZZ(\ZZ/n, N)$.
---

::: {.definition title="Ext"}
There are two definitions of the $\Ext$ functors, which are seen to agree by a spectral sequence argument.
Fixing an $A$-module $M$, define $\Ext^i_A(M, N)$ to be the right derived functors of the left exact functor $\Hom_A(M, \wait)$; this gives the usual long exact sequence in the second variable.

Alternatively, fixing $N$, take the right derived functors of the contravariant left exact functor $\Hom_A(\wait, N)$ to be $\Ext^i_A(\wait, N)$; this gives a long exact sequence in the first variable.
:::

::: {.remark}
$\Ext^0_A(M,N) = \Hom_A(M,N)$, and $\Ext^i_A(M,N) = 0$ for $i>0$ whenever $M$ is projective or $N$ is injective.
Since the two definitions agree, $\Ext$ can be computed from a projective resolution of $M$ or from an injective resolution of $N$: over $\ZZ$, the resolution $0 \to \ZZ \mapsvia{n} \ZZ \to \ZZ/n \to 0$ gives $\Ext^1_\ZZ(\ZZ/n, N) = N/nN$.

$\Ext^1(M,N)$ classifies extensions $0 \to N \to E \to M \to 0$ up to equivalence, with the split extension as the zero class.
For $X$ projective, Cohen--Macaulay, and equidimensional of dimension $n$ over an algebraically closed field $k$, with dualizing sheaf $\omega_X$, and for $\mcf$ coherent, Serre duality gives $\Ext^i(\mcf, \omega_X)\cong H^{n-i}(X,\mcf)^\vee$ [@Har10a, Theorem III.7.6].
:::
