---
schema: qual/card@1
id: P-MQ3H7
kind: problem
title: Square roots of matrices over $\CC$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Matrices
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Does every complex matrix $A$ admit a complex matrix square root $B$ with
\[
B^2=A?
\]
:::

::: {.solution}
No.

Consider the nilpotent Jordan block
\[
A=J_2(0)=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
\]
Suppose $B^2=A$. Every eigenvalue $\mu$ of $B$ would satisfy
\[
\mu^2\in\operatorname{Spec}(A)=\{0\},
\]
so every eigenvalue of $B$ is $0$. Thus a $2\times2$ complex matrix $B$ would be nilpotent, and hence by Cayley--Hamilton
\[
B^2=0.
\]
This contradicts $B^2=A\ne0$.

Therefore not every complex matrix has a square root.

By contrast, every **invertible** complex matrix does have a square root: put it in Jordan form and choose a square root of each nonzero eigenvalue; on a block $J_r(\lambda)=\lambda(I+N/\lambda)$, the finite binomial series for $(I+N/\lambda)^{1/2}$ gives a square root because $N$ is nilpotent.
:::
