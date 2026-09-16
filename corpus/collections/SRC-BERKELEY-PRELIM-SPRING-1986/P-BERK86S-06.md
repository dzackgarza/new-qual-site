---
schema: qual/card@1
id: P-BERK86S-06
kind: problem
title: Two square-zero operators satisfying $AB+BA=I$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $V$ be finite-dimensional and let $A,B\in\operatorname{End}(V)$ satisfy
\[
A^2=B^2=0,
\qquad
AB+BA=I.
\]
Let $N_A,N_B$ denote their null spaces.

1. Prove that
   \[
   N_A=A(N_B),
   \qquad
   N_B=B(N_A),
   \qquad
   V=N_A\oplus N_B.
   \]
2. Prove that $\dim V$ is even.
3. If $\dim V=2$, prove that there is a basis in which
   \[
   A=\begin{pmatrix}0&1\\0&0\end{pmatrix},
   \qquad
   B=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
   \]
:::
