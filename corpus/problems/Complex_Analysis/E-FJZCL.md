---
schema: qual/card@1
id: E-FJZCL
kind: problem
title: Convergence of $\frac1z\sum_{k=1}^\infty\frac{z^k}{k}$ on $S^1\setminus\{1\}$
  by summation by parts
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Power Series
  - Series of Functions
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

::: {.exercise}
Show that $\frac{1}{z}\sum_{k=1}^\infty \frac{z^k}{k}$ converges for all $z \in S^1 \setminus \{1\}$ using summation by parts.
:::

::: {.solution}
Fix $z\in S^1\setminus\{1\}$ and put $A_N\coloneqq\sum_{k=1}^Nz^k$.

::: pf

::: {.pf-step #bounded-partial-sums}
$\abs{A_N}\le\frac2{\abs{1-z}}$ for all $N$.

::: pf-proof
$A_N=z\frac{1-z^N}{1-z}$ and $\abs{1-z^N}\le2$.
:::

:::

::: {.pf-step #abel}
$\sum_{k=1}^N\frac{z^k}k=\frac{A_N}N+\sum_{k=1}^{N-1}A_k\qty(\frac1k-\frac1{k+1})$.

::: pf-proof
This is summation by parts with $z^k=A_k-A_{k-1}$ and $A_0=0$.
:::

:::

::: pf-step
$\frac1z\sum_{k\ge1}\frac{z^k}k$ converges.

::: pf-proof
By step [](#bounded-partial-sums){.pf-ref}, $\frac{A_N}N\to0$ and $\sum_{k\ge1}\abs{A_k}\qty(\frac1k-\frac1{k+1})\le\frac2{\abs{1-z}}\sum_{k\ge1}\frac1{k(k+1)}<\infty$, so the right side of step [](#abel){.pf-ref} converges as $N\to\infty$.
Multiplication by $\frac1z$, which is defined since $z\neq0$, preserves convergence.
:::

:::

:::

:::
