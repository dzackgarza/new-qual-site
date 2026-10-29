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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source leaves f and the measure undeclared; the statement takes f to be a real-valued function in L^1(mu).
---

::: {.exercise}
Let $(X,\mathcal M,\mu)$ be a measure space and let $f \in L^1(\mu)$ be real-valued. Show that $f=0$ a.e. iff $\int_E f = 0$ for every measurable set $E$.
:::

::: {.solution}

::: pf

::: pf-step

($\Rightarrow$) If $f = 0$ a.e. then $\int_E f = 0$ for every measurable $E$.

::: pf-proof

Functions equal a.e. have equal integrals over $E$, and $\int_E 0 = 0$.

:::

:::

::: pf-step

($\Leftarrow$) If $\int_E f = 0$ for every measurable $E$, then $f = 0$ a.e.

::: pf-proof

::: {.pf-step #s2-1}

$\mu\theset{f > 0} = 0$.

::: pf-proof

Apply the hypothesis to $E \coloneqq \theset{f > 0}$.
On $E$, $f = f^+ > 0$ and $f^- = 0$, so $0 = \int_E f = \int_E f^+$.
A nonnegative measurable function with zero integral is zero a.e., so $f = 0$ a.e. on $E$; since $f > 0$ on $E$, $\mu(E) = 0$.

:::

:::

::: {.pf-step #s2-2}

$\mu\theset{f < 0} = 0$.

::: pf-proof

Apply the hypothesis to $E \coloneqq \theset{f < 0}$: $\int_E f = -\int_E f^- = 0$, so $f^- = 0$ a.e. on $E$; since $f^- > 0$ on $E$, $\mu(E) = 0$.

:::

:::

::: pf-qed

$\theset{f \neq 0} = \theset{f > 0} \cup \theset{f < 0}$ has measure $0$ by steps [](#s2-1){.pf-ref} and [](#s2-2){.pf-ref}.

:::

:::

:::

:::

:::
