---
schema: qual/card@1
id: E-BTA5L
kind: exercise
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

::: exercise
- Show that $f=0$ a.e. iff $\int_E f = 0$ for every measurable set $E$.
:::

::: {.solution}
**Goal:** For a measurable $f$ (say $f \in L^1$, so all the integrals are defined), show $f = 0$ a.e. iff $\int_E f = 0$ for every measurable set $E$.

<1>1. ($\Rightarrow$) If $f = 0$ a.e. then $\int_E f = 0$ for every measurable $E$.
Proof: two functions equal a.e. have equal integrals; $\int_E 0 = 0$.

<1>2. ($\Leftarrow$) If $\int_E f = 0$ for every measurable $E$, then $f = 0$ a.e. <2>1. $\mu\theset{f > 0} = 0$.
Proof: apply the hypothesis to $E := \theset{f > 0}$: $\int_E f = 0$.
On $E$, $f = f^+ > 0$ and $f^- = 0$, so $0 = \int_E f = \int_E f^+$.
A nonnegative measurable function with zero integral is zero a.e. on $E$, so $f = 0$ a.e. on $E$; but $f > 0$ on $E$, forcing $\mu(E) = 0$.
<2>2. $\mu\theset{f < 0} = 0$.
Proof: the same argument with $E := \theset{f < 0}$: $\int_E f = \int_E (-f^-) = 0$, so $\int_E f^- = 0$ and $f^- = 0$ a.e. on $E$, forcing $\mu(E) = 0$.
<2>3. $f = 0$ a.e. Proof: $\theset{f \neq 0} = \theset{f > 0} \cup \theset{f < 0}$ has measure $0$ by <2>1 and <2>2. <1>3. Q.E.D. Proof: <1>1 and <1>2 are the two implications.
:::
