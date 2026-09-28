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
---

::: {.problem}
Find all real numbers $x$ for which the series $\displaystyle\sum_{n=1}^{\infty} \frac{x^n}{\sqrt{n^2+1}}$ converges.
[Be sure to justify your analysis.]
:::

::: {.solution}
Consider
\[
\sum_{n=1}^\infty \frac{x^n}{\sqrt{n^2+1}}.
\]
If $|x|<1$, then
\[
0\le \frac{|x|^n}{\sqrt{n^2+1}}\le |x|^n,
\]
so the series converges absolutely by comparison with a geometric series.

If $|x|>1$, then
\[
\frac{|x|^n}{\sqrt{n^2+1}}
\sim \frac{|x|^n}{n},
\]
which does not tend to $0$; hence the series diverges.

At $x=1$,
\[
\frac1{\sqrt{n^2+1}}\ge \frac1{\sqrt2\,n},
\]
so the series diverges by comparison with the harmonic series.

At $x=-1$, the series is
\[
\sum_{n=1}^\infty \frac{(-1)^n}{\sqrt{n^2+1}}.
\]
The positive terms $1/\sqrt{n^2+1}$ decrease to $0$, so the alternating-series test gives convergence.

Therefore the set of real $x$ for which the series converges is
\[
[-1,1).
\]
:::
