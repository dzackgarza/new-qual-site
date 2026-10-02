---
schema: qual/card@1
id: FE-ISVDM
kind: example
title: $A^n = B^n$ does not imply $A = B$ for matrices
prompts:
- Does $A^n=B^n$ imply $A=B$?
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Counterexamples
relations: []
review: draft
---

::: {.example}
For square matrices $A,B$ and $n\ge2$, $A^n=B^n$ does not imply $A=B$.
In $\Mat_2(\RR)$, let
$$
M=\matt 0 1 1 0 .
$$
Then $M^2=I=I^2$, but $M\ne I$.
:::
