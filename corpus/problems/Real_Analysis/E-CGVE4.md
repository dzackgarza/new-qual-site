---
schema: qual/card@1
id: E-CGVE4
kind: exercise
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

::: exercise
- Show that a countable union of null sets is null.
:::

::: {.solution}
**Goal:** Show that a countable union of null sets is null.

<1>1. Let $\{N_n\}$ be null sets, i.e. $\mu(N_n) = 0$ for all $n$.
::: {.proof}
setup.
:::
<1>2. $\mu\!\left(\bigcup_n N_n\right) \leq \sum_n \mu(N_n)$.
::: {.proof}
countable subadditivity of the measure.
:::
<1>3. $\sum_n \mu(N_n) = 0$, so $\mu(\bigcup_n N_n) = 0$.
::: {.proof}
each term is $0$ by hypothesis; a measure is nonnegative, so $\mu(\bigcup_n N_n) \geq 0$ and <1>2 forces it to be $0$.
:::
<1>4. Q.E.D.
::: {.proof}
<1>3 says the union is null.
:::
:::
