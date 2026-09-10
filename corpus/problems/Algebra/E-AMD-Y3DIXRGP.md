---
schema: qual/card@1
id: E-AMD-Y3DIXRGP
kind: problem
title: The stabilizer of an element need not be a normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Normal Subgroups
  - Counterexamples
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

::: {.exercise}
Show that the stabilizer of an element need not be a normal subgroup.
:::


::: {.solution}
Consider the natural action of $S_3$ on $X=\{1,2,3\}$.

<1>1. The stabilizer of $1$ is
\[
(S_3)_1=\{1,(23)\}.
\]
::: {.proof}
A permutation fixes $1$ exactly when it permutes only $2$ and $3$. Hence the only possibilities are the identity and $(23)$.
:::

<1>2. This stabilizer is not normal in $S_3$.
::: {.proof}
Conjugating its nonidentity element by $(12)$ gives
\[
(12)(23)(12)^{-1}=(13),
\]
and $(13)\notin\{1,(23)\}$. Therefore
\[
(12)(S_3)_1(12)^{-1}\neq(S_3)_1,
\]
so $(S_3)_1$ is not normal in $S_3$.
:::

<1>3. Thus a point stabilizer need not be a normal subgroup.
::: {.proof}
The action above supplies the required counterexample.
:::
:::
