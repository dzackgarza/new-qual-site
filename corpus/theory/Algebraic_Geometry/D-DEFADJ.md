---
schema: qual/card@1
id: D-DEFADJ
kind: definition
title: Adjoint functors
classification:
  areas:
  - algebraic-geometry
  topics:
  - Category Theory
  - Adjunctions
relations:
- kind: uses
  target: D-DEFNATTR
review: draft
prompts:
- What does it mean for $F$ and $G$ to be an adjoint pair?
- What is the force of the word "natural" in the definition?
---

::: {.definition title="adjoint"}
Suppose $\mca$ and $\mcb$ are categories with functors $F: \mca \to \mcb$ and $G: \mcb \to \mca$.
$F$ and $G$ are \dfn{adjoint} if there is a bijection
\[
\tau_{AB}: \Mor_{\mcb}(F(A), B) \to \Mor_{\mca}(A, G(B))
\]
for all $A \in \mca$ and $B \in \mcb$, natural in both arguments.
We call $F$ the **left adjoint** and $G$ the **right adjoint**.

Naturality means that for $f: A' \to A$ in $\mca$ the square formed by $\tau_{AB}$, $\tau_{A'B}$ and the two restriction maps along $f$ commutes, and similarly for $g: B \to B'$ in $\mcb$.
:::

::: {.remark}
Adjoints are unique up to natural isomorphism when they exist, so "the" left adjoint is a well-posed phrase.
The practical content of an adjunction is almost never the bijection itself but the exactness consequence: right adjoints preserve limits and left adjoints preserve colimits, so a functor's position in an adjoint pair already determines whether it is left or right exact.
That is why $\wait \tensor_A N$ is right exact and $\Hom_A(N,\wait)$ left exact, with no computation.
:::
