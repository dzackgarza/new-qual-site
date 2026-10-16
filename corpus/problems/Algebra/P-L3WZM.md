---
schema: qual/card@1
id: P-L3WZM
kind: problem
title: $\GF(p^n)$ is the splitting field of $x^{p^n}-x$ over $\FF_p$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Galois Theory
relations: []
review: draft
---

::: {.problem}
Show that $\GF(p^n)$ is the splitting field of $x^{p^n}-x$ over $\FF_p$.
:::

::: {.solution}
The roots of
\[
x^{p^n}-x
\]
in an algebraic closure are exactly the elements fixed by the $n$th iterate of Frobenius. They form the unique field with $p^n$ elements, namely $\GF(p^n)$. Since the derivative is $-1$, the polynomial is squarefree, so $\GF(p^n)$ is its splitting field.
:::