---
schema: qual/card@1
id: E-BTA5L
kind: problem
title: $f=0$ a.e. iff $\int_E f=0$ for every measurable $E$
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Show that $f=0$ a.e. iff $\int_E f = 0$ for every measurable set $E$.
:::

::: {.solution}
Let $f$ be a real-valued function in $L^1(\mu)$, so that every integral $\int_E f$ is defined.

<1>1. ($\Rightarrow$) If $f = 0$ a.e. then $\int_E f = 0$ for every measurable $E$.

::: {.proof}
Functions equal a.e. have equal integrals over $E$, and $\int_E 0 = 0$.
:::

<1>2. ($\Leftarrow$) If $\int_E f = 0$ for every measurable $E$, then $f = 0$ a.e.

<2>1. $\mu\theset{f > 0} = 0$.

::: {.proof}
Apply the hypothesis to $E \coloneqq \theset{f > 0}$.
On $E$, $f = f^+ > 0$ and $f^- = 0$, so $0 = \int_E f = \int_E f^+$.
A nonnegative measurable function with zero integral is zero a.e., so $f = 0$ a.e. on $E$; since $f > 0$ on $E$, $\mu(E) = 0$.
:::

<2>2. $\mu\theset{f < 0} = 0$.

::: {.proof}
Apply the hypothesis to $E \coloneqq \theset{f < 0}$: $\int_E f = -\int_E f^- = 0$, so $f^- = 0$ a.e. on $E$; since $f^- > 0$ on $E$, $\mu(E) = 0$.
:::

<2>3. Q.E.D.

::: {.proof}
$\theset{f \neq 0} = \theset{f > 0} \cup \theset{f < 0}$ has measure $0$ by steps <2>1 and <2>2.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 are the two implications.
:::
:::
