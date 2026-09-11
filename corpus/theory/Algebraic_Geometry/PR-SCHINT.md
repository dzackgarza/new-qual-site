---
schema: qual/card@1
id: PR-SCHINT
kind: proposition
title: Scheme-theoretic intersection as a fibre product
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fibre Products
  - Subschemes
  - Intersection Theory
relations:
- kind: uses
  target: D-SCHFPR
- kind: uses
  target: D-SCHSUB
review: draft
prompts:
- What is the scheme-theoretic intersection of two closed subschemes?
---

::: {.proposition}
For closed subschemes $X_1, X_2 \subseteq Y$, their **intersection** is $\fiberprod{X_1}{Y}{X_2}$, again a closed subscheme of $Y$.
For $Y = \Spec R$ with $X_i = \Spec(R/J_i)$ this is
\[
\Spec\qty{ R/J_1 \tensor_R R/J_2 } \cong \Spec R/(J_1 + J_2) ,
\]
so intersecting subschemes adds ideals.
:::

::: {.remark}
"Intersect means add the ideals" is the sentence to have ready, and it is the one place where the scheme structure does visible arithmetic.

Intersecting $y = x^2$ with $y = 0$ in $\AA^2$ gives $k[x,y]/(y - x^2, y) \cong k[x]/(x^2)$, the double point: tangency shows up as a length, and Bézout's theorem counts lengths rather than points.
Intersecting $y = x^2$ with $y = 1$ gives $k[x]/(x^2-1)$, two reduced points, and the total length is $2$ either way.

Note that the ideal sum need not be radical even when both $J_i$ are, which is exactly why the reduced induced structure of the intersection is the wrong object for counting.
:::
