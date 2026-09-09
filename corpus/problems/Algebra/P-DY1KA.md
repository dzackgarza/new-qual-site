---
schema: qual/card@1
id: P-DY1KA
kind: problem
title: Matrices with the same Jordan form are similar
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Matrices
  - Canonical Forms
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
Let $S$ and $T$ be square matrices over an algebraically closed field. Suppose $S$ and $T$ have the same Jordan canonical form. Prove that $S$ and $T$ are similar.
:::


::: {.solution}
Let $J$ denote their common Jordan canonical form.

<1>1. There are invertible matrices $P$ and $Q$ such that
\[
T=PJP^{-1},
\qquad
S=QJQ^{-1}.
\]
::: {.proof}
This is exactly what it means for $J$ to be the Jordan canonical form of $T$ and of $S$.
:::

<1>2. Therefore $S$ is similar to $T$.
::: {.proof}
From the first equality,
\[
J=P^{-1}TP.
\]
Substituting into the expression for $S$ gives
\[
S=QP^{-1}TPQ^{-1}
=(QP^{-1})T(QP^{-1})^{-1}.
\]
Since $QP^{-1}$ is invertible, this is a similarity transformation.
:::
:::
