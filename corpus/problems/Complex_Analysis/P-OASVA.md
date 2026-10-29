---
schema: qual/card@1
id: P-OASVA
kind: problem
title: Entire functions with a pole at $\infty$ are the nonconstant polynomials
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Polynomials
  - Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'Corrected the typo "with have poles" to "that have a pole".'
---

::: {.problem}
Find all entire functions that have a pole at $\infty$.
:::

::: {.solution}
Recall that $f$ has a pole at $\infty$ when $g(w)\definedas f(1/w)$ has a pole at $w=0$. Write $f(z)=\sum_{k\ge0}a_kz^k$, the Taylor series of $f$, which converges on all of $\CC$.

::: pf

::: {.pf-step #forward}
If $f$ is entire with a pole at $\infty$, then $f$ is a nonconstant polynomial.

::: pf-proof
For $w\neq0$, $g(w)=\sum_{k\ge0}a_kw^{-k}$, and by uniqueness this is the Laurent series of $g$ on $0<\abs{w}<\infty$. A pole at $0$ of order $N\ge1$ means $a_k=0$ for $k>N$ and $a_N\neq0$, so $f(z)=\sum_{k=0}^Na_kz^k$ has degree $N\ge1$.
:::

:::

::: {.pf-step #converse}
Every nonconstant polynomial has a pole at $\infty$.

::: pf-proof
If $f(z)=a_Nz^N+\cdots+a_0$ with $N\ge1$ and $a_N\neq0$, then $g(w)=a_Nw^{-N}+\cdots+a_0$ has a pole of order $N$ at $0$.
:::

:::

::: pf-step
The entire functions with a pole at $\infty$ are $\boxed{\text{the nonconstant polynomials}}$.

::: pf-proof
Combine steps [](#forward){.pf-ref} and [](#converse){.pf-ref}.
:::

:::

:::
:::
