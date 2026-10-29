---
schema: qual/card@1
id: P-DU7X7
kind: problem
title: Hilbert's theorem 90
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
What's Hilbert's theorem 90?
:::

::: {.solution}
Let $L/K$ be a finite Galois extension with Galois group $G$.

::: pf

::: pf-step
Hilbert's theorem 90 is the statement $\boxed{H^1(G,L^\times)=0}$.

::: pf-proof
This is the cohomological form of the theorem.
:::

:::

::: pf-step
If $G=\langle\sigma\rangle$ is cyclic of order $n$, the theorem is equivalent to: $N_{L/K}(a)=1$ if and only if $a=b/\sigma(b)$ for some $b\in L^\times$.

::: pf-proof
For a cyclic group, a $1$-cocycle is determined by its value at $\sigma$, and a value defines a cocycle exactly when its norm is $1$.
The coboundaries take the values $\sigma(b)/b$ at $\sigma$, and replacing $b$ by $b^{-1}$ writes these as $b/\sigma(b)$.
:::

:::

::: pf-step
The additive analogue is $H^1(G,L)=0$; for cyclic $G=\langle\sigma\rangle$ it says $\Tr_{L/K}(a)=0$ if and only if $a=b-\sigma(b)$ for some $b\in L$.

::: pf-proof
The same description of cocycles and coboundaries for a cyclic group, written additively, replaces the norm by the trace.
:::

:::

:::

:::
