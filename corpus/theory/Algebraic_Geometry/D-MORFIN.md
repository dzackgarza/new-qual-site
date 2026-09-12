---
schema: qual/card@1
id: D-MORFIN
kind: definition
title: Finite morphisms, and finite against finite type
classification:
  areas:
  - algebraic-geometry
  topics:
  - Finite Morphisms
  - Finite Type Morphisms
  - Branched Covers
relations:
- kind: uses
  target: D-MORAFF
- kind: related-to
  target: D-MORFT
review: draft
prompts:
- What is a finite morphism?
- How does finite differ from finite type?
- What are the consequences of a morphism being finite?
---

::: {.definition title="Finite"}
$f : X \to Y$ is **finite** if $Y$ has an affine cover by $\Spec B_i$ with $f^{-1}(\Spec B_i) = \Spec A_i$ affine and $A_i$ a finitely generated $B_i$-**module**.
:::

::: {.remark}
Finitely generated as a module is strictly stronger than finitely generated as an algebra.
$k[x]$ has one algebra generator over $k$ and infinite rank as a $k$-module, so $\AA^1_k \to \Spec k$ is of finite type and not finite.
Hence finite implies finite type, but the converse fails.

Finite morphisms are affine, proper, closed, and have finite fibres. For a finite locally free morphism, the dimension of each fibre algebra over its residue field is locally constant.
A nonconstant morphism of smooth projective integral curves is finite and induces a finite extension of function fields.
Closedness follows from the going up theorem on affine opens.
:::
