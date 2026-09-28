---
schema: qual/card@1
id: D-DEFEXACT
kind: definition
title: Exactness, and left, right, and exact functors
classification:
  areas:
  - algebraic-geometry
  topics:
  - Homological Algebra
  - Abelian Categories
  - Exact Functors
relations:
- kind: uses
  target: D-DEFABCAT
review: draft
prompts:
- What does it mean for a sequence to be exact at an object, and what is a short exact sequence?
- Define left exact, right exact, and exact for an additive functor.
- Give a left exact functor that is not exact, and a right exact one that is not exact.
---

::: {.definition title="exact sequences and exact functors"}
In an abelian category $\mca$, a sequence $A \mapsvia{f} B \mapsvia{g} C$ is \dfn{exact at $B$} if $\ker g = \im f$.
A sequence
$$
0 \to A \mapsvia{f} B \mapsvia{g} C \to 0
$$
is a \dfn{short exact sequence} if $f$ is injective, $g$ is surjective, and $\ker g = \im f$.

An additive functor $F: \mca \to \mcb$ is \dfn{left exact} if for every short exact sequence $0 \to A \to B \to C \to 0$ the sequence
$$
0 \to F(A) \to F(B) \to F(C)
$$
is exact, and \dfn{right exact} if
$$
F(A) \to F(B) \to F(C) \to 0
$$
is exact.
$F$ is \dfn{exact} if it is both, in which case short exact sequences go to short exact sequences.
:::

::: {.remark}
The functor $\Hom_A(N, \wait)$ is left exact and $\wait \tensor_A N$ is right exact, since $\wait\tensor_AN$ is left adjoint to $\Hom_A(N,\wait)$ ([[D-DEFADJ]]).
Over $A = \ZZ$ with $N = \ZZ/2$, apply both to $0 \to \ZZ \mapsvia{2} \ZZ \to \ZZ/2 \to 0$.
The map $\Hom(\ZZ/2,\ZZ)=0\to\Hom(\ZZ/2,\ZZ/2)=\ZZ/2$ is not surjective, and the map $\ZZ\tensor\ZZ/2\to\ZZ\tensor\ZZ/2$ induced by multiplication by $2$ is the zero map $\ZZ/2\to\ZZ/2$, which is not injective.
The long exact sequences of $\Ext^i_\ZZ(\ZZ/2,\wait)$ and $\Tor_i^\ZZ(\wait,\ZZ/2)$ continue these sequences, with $\Ext^1_\ZZ(\ZZ/2,\ZZ)\cong\ZZ/2$ and $\Tor_1^\ZZ(\ZZ/2,\ZZ/2)\cong\ZZ/2$.
:::
