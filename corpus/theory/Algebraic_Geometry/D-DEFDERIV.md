---
schema: qual/card@1
id: D-DEFDERIV
kind: definition
title: Derived functors
classification:
  areas:
  - algebraic-geometry
  topics:
  - Homological Algebra
  - Derived Functors
relations:
- kind: uses
  target: D-DEFINJOB
- kind: uses
  target: D-DEFPROJO
- kind: uses
  target: D-DEFEXACT
review: draft
prompts:
- How are the right derived functors of a left exact functor defined?
- What are the left derived functors, and which hypothesis do they need?
- Why is $R^iF(A)$ independent of the chosen resolution?
---

::: {.definition title="derived functors"}
Let $\mca$ be an abelian category with enough injectives and $F: \mca \to \mcb$ an additive covariant left exact functor.
The \dfn{right derived functors} $R^iF: \mca \to \mcb$ are
\[
R^iF(A) = h^i(F(I^\bullet)) ,
\]
where $A \to I^\bullet$ is any injective resolution of $A$.

If instead $F$ is right exact and $\mca$ has enough projectives, the **left derived functors** are
\[
L^iF(A) = h^i(F(P^\bullet)) ,
\]
where $P^\bullet \to A$ is any projective resolution.

For contravariant $F$ one modifies these, or regards $F$ as a covariant functor on $\mca\op$.
:::

::: {.remark}
$R^0F \cong F$ by left exactness, and $R^iF = 0$ for all $i>0$ exactly when $F$ is exact, so the derived functors measure the failure of exactness.
Independence of the resolution is the homotopy statement: any two injective resolutions are homotopy equivalent, and homotopic maps agree on cohomology.

One never computes with injectives.
The working fact is that any $F$-acyclic resolution computes $R^iF$, which is why flasque resolutions compute sheaf cohomology and free resolutions compute $\Tor$.
:::
