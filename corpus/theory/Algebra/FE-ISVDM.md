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
For every integer $n\ge2$, there are distinct real $2\times2$ matrices with the same $n$th power.
Let
$$
R_n=
\begin{bmatrix}
\cos(2\pi/n)&-\sin(2\pi/n)\\
\sin(2\pi/n)&\cos(2\pi/n)
\end{bmatrix}.
$$
This is rotation through angle $2\pi/n$, so $R_n^n=I_2=I_2^n$, while $R_n\ne I_2$.
:::
