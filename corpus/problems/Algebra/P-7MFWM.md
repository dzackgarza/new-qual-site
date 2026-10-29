---
schema: qual/card@1
id: P-7MFWM
kind: problem
title: 'Real logarithms of matrices in $\SL_n(\RR)$ are traceless'
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Determinants
  - Trace
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
Say we can find a matrix $A \in M_n(\RR)$ such that $\exp(A) = B$ for $B \in \SL_n(\RR)$.
Does $A$ also have to be in $\SL_n(\RR)$?
Does $A$ have to satisfy $\tr(A) = 0$ (i.e. $A \in \mathfrak{sl}_n(\RR)$)?
:::

::: {.solution}

::: pf

::: pf-step

If $e^A\in\SL_n(\RR)$, then $\boxed{\tr A=0}$, so $A\in\mathfrak{sl}_n(\RR)$.

::: pf-proof

For every real matrix $A$, $\det(e^A)=e^{\tr A}$. Hence $1=\det(e^A)=e^{\tr A}$, and since $\tr A\in\RR$ and the real exponential is injective, $\tr A=0$.

:::

:::

::: pf-step

$A$ need $\boxed{\text{not}}$ lie in $\SL_n(\RR)$.

::: pf-proof

The zero matrix satisfies $e^0=I_n\in\SL_n(\RR)$, while $\det 0=0\ne1$.

:::

:::

:::

:::
