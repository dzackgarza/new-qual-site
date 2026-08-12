---
schema: qual/card@1
id: PR-UQ3XJ
kind: proposition
title: "Order of $\\GL_n$"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.proposition title="Order of $\GL_n$"}
For $q$ a prime power,
\[
\abs{\GL_n(\FF_q)} = \prod_{k=0}^{n-1}\qty{q^n - q^k} = (q^n-1)(q^n-q)\cdots(q^n - q^{n-1})
.\]
A matrix is invertible exactly when its columns form a basis of $\FF_q^n$, so the columns may be chosen in order: the $(k+1)\dash$st column is any vector outside the span of the previous $k$, a subspace with $q^k$ elements.
:::

:::{.concept}
See Dummit and Foote, §11.1, for the basis criterion.
:::
