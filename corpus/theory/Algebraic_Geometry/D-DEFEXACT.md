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
\[
0 \to A \mapsvia{f} B \mapsvia{g} C \to 0
\]
is a **short exact sequence** if $f$ is injective, $g$ is surjective, and $\ker g = \im f$.

An additive functor $F: \mca \to \mcb$ is **left exact** if for every short exact sequence $0 \to A \to B \to C \to 0$ the sequence
\[
0 \to F(A) \to F(B) \to F(C)
\]
is exact, and **right exact** if
\[
F(A) \to F(B) \to F(C) \to 0
\]
is exact.
$F$ is **exact** if it is both, in which case short exact sequences go to short exact sequences.
:::

::: {.remark}
The two standard examples are the two halves of one adjunction: $\Hom_A(N, \wait)$ is left exact and $\wait \tensor_A N$ is right exact, and this is forced by which side of the adjunction each sits on.
Over $A = \ZZ$ with $N = \ZZ/2$, applying either functor to $0 \to \ZZ \mapsvia{2} \ZZ \to \ZZ/2 \to 0$ exhibits the failure of the missing half.

That failure is the input to the theory rather than a defect: $\Ext$ and $\Tor$ are exactly its measurement, and a functor is exact precisely when all of its derived functors vanish.
:::
