---
schema: qual/card@1
id: FF-VKYM3
kind: fact
title: $A^n = B^n$ does not imply $A = B$ for matrices
prompts:
- For matrices, does $A^n=B^n\implies A=B$?
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Counterexamples
relations: []
review: draft
---

::: {.fact}
For square matrices $A,B$ and $n\ge2$, $A^n=B^n$ does not imply $A=B$.
In $\Mat_2(\RR)$, let
$$
A=\begin{bmatrix}0&1\\-1&0\end{bmatrix}.
$$
Then
$$
A^2=\begin{bmatrix}-1&0\\0&-1\end{bmatrix}=(-A)^2,
$$
but $A\ne-A$.
:::
