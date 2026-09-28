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
$$
\tau_{AB}: \Mor_{\mcb}(F(A), B) \to \Mor_{\mca}(A, G(B))
$$
for all $A \in \mca$ and $B \in \mcb$, natural in both arguments.
We call $F$ the \dfn{left adjoint} and $G$ the \dfn{right adjoint}.

Naturality means that for $f: A' \to A$ in $\mca$ the square formed by $\tau_{AB}$, $\tau_{A'B}$ and the two restriction maps along $f$ commutes, and similarly for $g: B \to B'$ in $\mcb$.
:::

::: {.remark}
A left adjoint of $G$, if it exists, is unique up to unique natural isomorphism, and likewise for right adjoints.
Right adjoints preserve limits and left adjoints preserve colimits; so an additive left adjoint between abelian categories is right exact, and an additive right adjoint is left exact.
Since $\wait \tensor_A N$ is left adjoint to $\Hom_A(N,\wait)$, the first is right exact and the second left exact.
:::
