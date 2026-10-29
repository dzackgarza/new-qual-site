---
schema: qual/card@1
id: E-XIT36
kind: problem
title: Convergence of $\sum \sin(n)/n$ by summation by parts
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Series of Numbers
  - Trigonometry
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source printed "show that sin(n)/n converges", which as a sequence is immediate and needs no summation by parts; the statement now asks for convergence of the series sum_{n>=1} sin(n)/n.'
---

::: {.exercise}
Use summation by parts to show that $\displaystyle\sum_{n=1}^\infty \frac{\sin(n)}{n}$ converges.
:::

::: {.solution}
Write $B_N \coloneqq \sum_{n=1}^N \sin n$ and $B_0 \coloneqq 0$.

::: pf

::: {.pf-step #bounded}
$\abs{B_N} \le C \coloneqq \dfrac{2}{\abs{1-e^i}}$ for all $N$.

::: pf-proof
$B_N$ is the imaginary part of the geometric sum
$$
\sum_{n=1}^N e^{in} = e^i\,\frac{1-e^{iN}}{1-e^i},
$$
whose modulus is at most $2/\abs{1-e^i}$.
:::

:::

::: {.pf-step #abel}
For $N>M\ge1$,
$$
\sum_{n=M}^N \frac{\sin n}{n} = \frac{B_N}{N} - \frac{B_{M-1}}{M} + \sum_{n=M}^{N-1} B_n\qty{\frac1n - \frac{1}{n+1}}.
$$

::: pf-proof
Substitute $\sin n = B_n - B_{n-1}$ and regroup the terms by $B_n$.
:::

:::

::: pf-step
The series converges.

::: pf-proof
By steps [](#bounded){.pf-ref} and [](#abel){.pf-ref}, and since $\frac1n - \frac1{n+1} > 0$ telescopes,
$$
\abs{\sum_{n=M}^N \frac{\sin n}{n}} \le \frac CN + \frac CM + C\qty{\frac1M - \frac1N} \le \frac{3C}{M},
$$
which tends to $0$ as $M\to\infty$.
So the partial sums are Cauchy, and the series converges.
:::

:::

:::

:::
