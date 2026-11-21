---
schema: qual/card@1
id: P-AOZMW
kind: problem
title: Real $x$ for which $\sum_{n=1}^\infty \frac{x^n}{\sqrt{n^2+1}}$ converges
classification:
  areas:
  - prelim
  topics:
  - Series of Numbers
  - Convergence Tests
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked absolute convergence for |x| < 1 by comparison
    with the geometric series, divergence for |x| > 1 through |x|^n/(n+1) tending to
    infinity (the ratio test on that comparison sequence, replacing the prose's asymptotic
    notation), divergence at x = 1 through sqrt(n^2+1) <= sqrt2 n and the harmonic series,
    and convergence at x = -1 by the alternating series test with 1/sqrt(n^2+1) decreasing
    to 0. The answer [-1,1) is unchanged. The argument is the card's own; no retained set is
    cited.
---

::: {.problem}
Find all real numbers $x$ for which the series $\displaystyle\sum_{n=1}^{\infty} \frac{x^n}{\sqrt{n^2+1}}$ converges.
[Be sure to justify your analysis.]
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. Write $a_{n}(x)=x^{n}/\sqrt{n^{2}+1}$.

::: pf

::: {.pf-step #inside}
For $\abs{x}<1$ the series converges absolutely.

::: pf-proof
$\sqrt{n^{2}+1}\ge1$ gives $\abs{a_{n}(x)}\le\abs{x}^{n}$, and $\sum\abs{x}^{n}$ is a convergent geometric series because $\abs{x}<1$; comparison gives absolute convergence.
:::

:::

::: {.pf-step #outside}
For $\abs{x}>1$ the series diverges.

::: pf-proof
$\sqrt{n^{2}+1}\le n+1$ gives $\abs{a_{n}(x)}\ge\abs{x}^{n}/(n+1)$. With $r=\abs{x}>1$ one has $r^{n}/(n+1)\to\infty$: the ratio of consecutive terms is $r\,(n+1)/(n+2)\to r>1$, so the sequence is eventually increasing and unbounded. Hence $\abs{a_{n}(x)}\to\infty$, the terms do not tend to $0$, and the series diverges.
:::

:::

::: {.pf-step #plus-one}
At $x=1$ the series diverges.

::: pf-proof
For $n\ge1$, $n^{2}+1\le2n^{2}$, so $\sqrt{n^{2}+1}\le\sqrt2\,n$ and $a_{n}(1)\ge1/(\sqrt2\,n)$. The harmonic series diverges, so by comparison the series of positive terms diverges.
:::

:::

::: {.pf-step #minus-one}
At $x=-1$ the series converges.

::: pf-proof
The series is $\sum(-1)^{n}b_{n}$ with $b_{n}=1/\sqrt{n^{2}+1}>0$, which decreases to $0$: $b_{n}\to0$, and $b_{n+1}<b_{n}$ because $n\mapsto n^{2}+1$ is increasing. The alternating series test then gives convergence.
:::

:::

::: {.pf-step}
The series converges exactly for $x\in[-1,1)$.

::: pf-proof
Steps [](#inside){.pf-ref}, [](#outside){.pf-ref}, [](#plus-one){.pf-ref} and [](#minus-one){.pf-ref} settle $\abs{x}<1$, $\abs{x}>1$, $x=1$ and $x=-1$, which together with $\abs{x}=1$ exhaust the real line; convergence holds at $-1$ and at every point of $(-1,1)$, and fails at $1$ and outside $[-1,1]$.
:::

:::

:::
:::
