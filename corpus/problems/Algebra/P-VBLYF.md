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
::: pf

::: pf-step
Two matrices in $\GL_2(\CC)$ are conjugate exactly when they have the same Jordan canonical form, up to the order of the blocks.

::: pf-proof
This is the uniqueness of the Jordan canonical form over the algebraically closed field $\CC$.
:::

:::

::: pf-step
Each conjugacy class contains exactly one matrix of one of three types: $\begin{pmatrix}\lambda&0\\0&\mu\end{pmatrix}$ with $\lambda,\mu\in\CC^\times$, $\lambda\ne\mu$, determined by the unordered pair $\{\lambda,\mu\}$; the scalar matrix $\lambda I_2$ with $\lambda\in\CC^\times$; or the Jordan block $\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}$ with $\lambda\in\CC^\times$.

::: pf-proof
An invertible $2\times2$ complex matrix has either two distinct nonzero eigenvalues or one repeated nonzero eigenvalue.
In the repeated case it is either diagonalizable, hence scalar, or has one Jordan block of size $2$.
Scalar matrices are central, so each class of the second type is a singleton.
:::

:::

:::
:::
