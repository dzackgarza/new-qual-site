---
schema: qual/card@1
id: P-VBLYF
kind: problem
title: Conjugacy classes in $\mathrm{GL}_2(\CC)$
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

::: problem
What are the conjugacy classes in $\operatorname{GL}_2(\mathbb{C})$?
:::

::: solution
By Jordan canonical form, every element of $\operatorname{GL}_2(\mathbb C)$ is conjugate to exactly one of the following types, up to permuting diagonal entries:

1. Distinct eigenvalues:
\[
\begin{pmatrix}\lambda&0\\0&\mu\end{pmatrix},
\qquad \lambda,\mu\in\mathbb C^\times,
\quad \lambda\ne\mu.
\]
The class depends only on the unordered pair $\{\lambda,\mu\}$.

2. A scalar matrix:
\[
\lambda I_2,
\qquad \lambda\in\mathbb C^\times.
\]
Since scalar matrices are central, each such conjugacy class is a singleton.

3. A nontrivial Jordan block:
\[
\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix},
\qquad \lambda\in\mathbb C^\times.
\]

These are all possibilities because an invertible $2\times2$ complex matrix has either two distinct nonzero eigenvalues or one repeated nonzero eigenvalue, and in the repeated case it is either diagonalizable or has one Jordan block of size $2$.
:::
