---
schema: qual/card@1
id: P-AGH398TONEMODULE
kind: problem
title: The module $T^1$ classifies infinitesimal deformations of an algebra
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Infinitesimal Deformations
  - Sheaves of Differentials
  - Dual Numbers
relations: []
review: draft
---

::: problem
Let $A$ be a finitely generated $k\dash$algebra. Write $A$ as a quotient of a polynomial ring $P$ over $k$, and let $J$ be the kernel:
\[
0 \to J \to P \to A \to 0
.\]
Consider the exact sequence of (II, 8.4A),
\[
J/J^2 \to \Omega_{P/k} \tensor_P A \to \Omega_{A/k} \to 0
.\]
Apply the functor $\Hom_A(\cdot, A)$, and let $T^1(A)$ be the cokernel:
\[
\Hom_A(\Omega_{P/k} \tensor A, A) \to \Hom_A(J/J^2, A) \to T^1(A) \to 0
.\]

Now use the construction of (II, Ex. 8.6) to show that $T^1(A)$ classifies infinitesimal deformations of $A$, that is, algebras $A'$ flat over $D = k[t]/t^2$ with $A' \tensor_D k \cong A$. It follows that $T^1(A)$ is independent of the given representation of $A$ as a quotient of a polynomial ring $P$.
:::
