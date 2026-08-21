---
schema: qual/card@1
id: E-NUJ7W
kind: exercise
title: Nonzero nilpotent matrices are not diagonalizable
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Diagonalization
  - Jordan Canonical Form
relations: []
review: draft
solved: false
---

::: {.exercise title="?"}
Show that a nonzero nilpotent matrix $A$ is not diagonalizable over any field.
Some useful facts:

- $\spec A = \ts{0}$, since $Ax=\lambda x \implies A^n=\lambda^nx$, so $A^n=0$ forces $\lambda =0$.
  This forces $\JCF(A)$ to be strictly upper-triangular.

- $\min_A(x) = x^n$.

- If $A$ were diagonalizable, $\JCF(A) = 0$.
:::
