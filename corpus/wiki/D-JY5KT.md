---
schema: qual/card@1
id: D-JY5KT
kind: definition
title: "Companion Matrix"
classification:
  areas:
  - algebra
  topics:
  - rational-canonical-form
  - matrices
  - minimal-and-characteristic-polynomials
relations: []
review: draft
---
:::{.definition title="Companion Matrix"}
Given a monic $p(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_{n-1} x^{n-1} + x^n$, the **companion matrix** of $p$ is given by
\[
C_p \definedas 
\begin{bmatrix}
0 & 0 & \dots & 0 &-a_0 \\ 
1 & 0 & \dots & 0 & -a_1 \\ 
0 & 1 & \dots & 0 & -a_2 \\ 
\vdots & & \ddots & & \vdots \\ 
0 & 0 & \dots & 1 & -a_{n-1} 
\end{bmatrix}
.\]
:::
