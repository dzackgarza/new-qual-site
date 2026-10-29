---
schema: qual/card@1
id: D-GIGM2
kind: definition
title: Nilpotent element
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Rings
  - Matrices
relations: []
review: draft
---

::: {.definition}
Let $R$ be a [[D-GURUB|ring]].
An element $r\in R$ is \dfn{nilpotent} if $r^n = 0$ for some integer $n \geq 1$.
:::

::: {.example}
For $R=\Mat_{n\times n}(k)$ with $k$ a field: a strictly upper triangular matrix $A\in\Mat_{n\times n}(k)$ is nilpotent, with $A^n=0$: if $e_1,\ldots,e_n$ is the standard basis, then $A$ maps $\spanof\theset{e_1,\ldots,e_j}$ into $\spanof\theset{e_1,\ldots,e_{j-1}}$ for each $j$.
Conversely, every nilpotent $A\in\Mat_{n\times n}(k)$ is [[D-JIGMN|similar]] to a strictly upper triangular matrix: every eigenvalue $\lambda$ of $A$ in an algebraic closure of $k$ satisfies $\lambda^m=0$, so the [[D-QFYAC|characteristic polynomial]] of $A$ is $x^n$, which splits over $k$, and a matrix whose characteristic polynomial splits is similar to an upper triangular matrix whose diagonal entries are its eigenvalues.
:::
