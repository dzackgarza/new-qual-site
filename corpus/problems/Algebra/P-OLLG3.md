---
schema: qual/card@1
id: P-OLLG3
kind: problem
title: Elementary matrices preserve solutions of $Ax=b$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Matrices
relations: []
review: draft
---

::: problem
Let $A\in M_{m\times n}(F)$ and $b\in F^m$. Show that applying the same sequence of elementary row operations to $A$ and $b$ does not change the solution set of
\[
Ax=b.
\]
:::

::: {.solution}
Let
\[
E=E_k\cdots E_1
\]
be a product of elementary matrices, and set
\[
A'=EA,\qquad b'=Eb.
\]
Every elementary matrix is invertible, hence so is $E$.

For any $x\in F^n$,
\[
Ax=b
\iff EAx=Eb
\iff A'x=b'.
\]
The reverse implication uses multiplication by $E^{-1}$.

Thus $Ax=b$ and $A'x=b'$ have exactly the same solutions.
:::
