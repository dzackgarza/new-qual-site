---
schema: qual/card@1
id: P-QX43E
kind: problem
title: Solving $\exp(A)=B$ over $\CC$ and over $\RR$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Jordan Canonical Form
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
When and how can we solve the matrix equation $\exp(A) = B$?
Do it over the complex numbers and over the real numbers.
Give a counterexample with real entries.
:::

::: {.solution}
Over $\mathbb C$, the equation $e^A=B$ has a solution exactly when $B$ is invertible. Necessity follows from
\[
\det(e^A)=e^{\operatorname{tr}A}\neq0.
\]
For sufficiency, put $B$ in Jordan form. For a block
\[
J=\lambda(I+N),\qquad \lambda\neq0,\quad N^m=0,
\]
choose any complex logarithm $\ell$ of $\lambda$ and set
\[
\log J=\ell I+\sum_{r=1}^{m-1}\frac{(-1)^{r+1}}rN^r.
\]
The sum is finite, and exponentiating gives $J$. Conjugating the block logarithms back yields a logarithm of $B$.

Over $\mathbb R$, invertibility and positive determinant are necessary but not sufficient. Culver's criterion says that a real invertible matrix has a real logarithm iff, for every negative real eigenvalue, the Jordan blocks of each size occur with even multiplicity. Positive real Jordan blocks use the same finite nilpotent logarithm as above; nonreal conjugate blocks are paired, and equal negative blocks are paired to obtain real logarithm blocks.

For example,
\[
B=\begin{pmatrix}-1&0\\0&-2\end{pmatrix}
\]
has positive determinant but no real logarithm: each negative eigenvalue occurs in a single $1\times1$ Jordan block, violating Culver's criterion.
:::
