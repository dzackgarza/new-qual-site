---
schema: qual/card@1
id: P-TLBS5
kind: problem
title: A non-normal subgroup, and whether $\mathrm{SO}(2)\normal\mathrm{SL}_2(\RR)$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Matrix Groups
  - Counterexamples
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
(1) Give an interesting example of a non-normal subgroup in a familiar group.
(2) Is the rotation subgroup $\operatorname{SO}(2)$ normal inside the special linear group $\operatorname{SL}_2(\mathbb{R})$? Prove your assertion with an explicit calculation.
:::

::: {.solution}
A familiar example is
\[
\langle(12)\rangle\le S_3.
\]
It is not normal because
\[
(123)(12)(123)^{-1}=(23)\notin\langle(12)\rangle.
\]

Likewise, $\operatorname{SO}(2)$ is not normal in $\operatorname{SL}_2(\mathbb R)$. Let
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\in\operatorname{SO}(2),
\qquad
g=\begin{pmatrix}2&0\\0&1/2\end{pmatrix}\in\operatorname{SL}_2(\mathbb R).
\]
Then
\[
gJg^{-1}
=\begin{pmatrix}0&-4\\1/4&0\end{pmatrix}.
\]
Its first column has Euclidean norm $1/4$, so it is not orthogonal. Hence
\[
gJg^{-1}\notin\operatorname{SO}(2),
\]
which proves
\[
\operatorname{SO}(2)\not\trianglelefteq\operatorname{SL}_2(\mathbb R).
\]
:::
