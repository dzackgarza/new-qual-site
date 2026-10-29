---
schema: qual/card@1
id: P-VBLYF
kind: problem
title: Conjugacy classes in $\GL_2(\CC)$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Jordan Canonical Form
  - Matrix Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What are the conjugacy classes in $\GL_2(\CC)$?
:::

::: {.solution}
Two matrices in $\GL_2(\CC)$ are conjugate exactly when they have the same Jordan canonical form, and the Jordan form is unique up to the order of the blocks. An invertible $2\times2$ complex matrix has either two distinct nonzero eigenvalues or one repeated nonzero eigenvalue, and in the repeated case it is either diagonalizable or has one Jordan block of size $2$. So each conjugacy class contains exactly one matrix of one of the following three types.

Distinct eigenvalues:
$$
\begin{pmatrix}\lambda&0\\0&\mu\end{pmatrix},
\qquad \lambda,\mu\in\CC^\times,
\quad \lambda\ne\mu,
$$
where the class depends only on the unordered pair $\{\lambda,\mu\}$.

A scalar matrix:
$$
\lambda I_2,
\qquad \lambda\in\CC^\times.
$$
Scalar matrices are central, so each such class is a singleton.

A nontrivial Jordan block:
$$
\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix},
\qquad \lambda\in\CC^\times.
$$
:::
