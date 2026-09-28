---
schema: qual/card@1
id: D-HGMOW
kind: definition
title: Nilpotent matrix
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Matrices
relations: []
review: draft
---

::: {.definition}
Let $k$ be a field and $n\geq 1$.
A matrix $A\in\Mat_{n\times n}(k)$ is \dfn{nilpotent} if there exists an integer $m\geq 1$ such that $A^m = 0$.
:::

::: {.example}
A strictly upper triangular matrix $A\in\Mat_{n\times n}(k)$ is nilpotent, with $A^n=0$: if $e_1,\ldots,e_n$ is the standard basis, then $A$ maps $\spanof\theset{e_1,\ldots,e_j}$ into $\spanof\theset{e_1,\ldots,e_{j-1}}$ for each $j$.
Conversely, every nilpotent $A\in\Mat_{n\times n}(k)$ is [[D-JIGMN|similar]] to a strictly upper triangular matrix: every eigenvalue $\lambda$ of $A$ in an algebraic closure of $k$ satisfies $\lambda^m=0$, so the [[D-QFYAC|characteristic polynomial]] of $A$ is $\pm x^n$, which splits over $k$, and a matrix whose characteristic polynomial splits is similar to an upper triangular matrix whose diagonal entries are its eigenvalues.
:::
