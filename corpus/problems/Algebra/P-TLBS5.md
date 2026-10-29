---
schema: qual/card@1
id: P-TLBS5
kind: problem
title: A non-normal subgroup, and whether $\SO(2)\normal\SL_2(\RR)$
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

(2) Is the rotation subgroup $\SO(2)$ normal inside the special linear group $\SL_2(\RR)$? Prove your assertion with an explicit calculation.
:::

::: {.solution}

::: pf

::: pf-step
(1) The subgroup $\langle(12)\rangle$ of $S_3$ is not normal.

::: pf-proof
$(123)(12)(123)^{-1}=(23)\notin\langle(12)\rangle$.
:::

:::

::: pf-step
(2) $\SO(2)$ is not normal in $\SL_2(\RR)$.

::: pf-proof
Let
$$
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\in\SO(2),
\qquad
g=\begin{pmatrix}2&0\\0&1/2\end{pmatrix}\in\SL_2(\RR).
$$
Then
$$
gJg^{-1}=\begin{pmatrix}0&-4\\1/4&0\end{pmatrix}.
$$
Its first column has Euclidean norm $1/4$, so $gJg^{-1}$ is not orthogonal and $gJg^{-1}\notin\SO(2)$.
:::

:::

:::

:::
