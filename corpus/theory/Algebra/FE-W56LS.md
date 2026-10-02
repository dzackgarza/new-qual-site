---
schema: qual/card@1
id: FE-W56LS
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
relations:
- kind: variant-of
  target: FE-ISVDM
review: draft
---

::: {.example}
For square matrices $A,B$ and $n\ge2$, $A^n=B^n$ does not imply $A=B$.
In $\Mat_2(\RR)$, the matrix $M=\matt 0 1 1 0$ satisfies $M^2=I_2=I_2^2$, and $M\ne I_2$.
:::
