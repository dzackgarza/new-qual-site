---
schema: qual/card@1
id: E-CGVE4
kind: problem
title: Countable unions of null sets are null
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Show that a countable union of null sets is null.
:::

::: {.solution}
Let $(N_n)_{n\ge1}$ be measurable sets with $\mu(N_n) = 0$ for all $n$.

<1>1. $\mu\!\left(\bigcup_n N_n\right) \leq \sum_n \mu(N_n)$.

::: {.proof}
This is countable subadditivity of the measure $\mu$.
:::

<1>2. Q.E.D.

::: {.proof}
Each term of $\sum_n \mu(N_n)$ is $0$, so step <1>1 gives $\mu(\bigcup_n N_n) \leq 0$. Since $\mu$ is nonnegative, $\mu(\bigcup_n N_n) = 0$.
:::
:::
