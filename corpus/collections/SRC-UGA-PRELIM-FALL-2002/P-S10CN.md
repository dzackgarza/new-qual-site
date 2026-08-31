---
schema: qual/card@1
id: P-S10CN
kind: problem
title: Definition of series convergence, and $\sum 1/10^n$ converges
classification:
  areas:
  - prelim
  topics:
  - Series
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Define what it means for a series $\sum_{n=1}^\infty a_n$ (of real numbers $a_n$) to converge to a real number $S$.
Prove that the series $\sum_{n=1}^\infty 1/10^n$ converges.
:::

::: {.solution}
<1>1. The series $\sum_{n=1}^{\infty} a_n$ converges to $S$ if the sequence of partial sums $s_N = \sum_{n=1}^{N} a_n$ converges to $S$, i.e. $\lim_{N \to \infty} s_N = S$.
::: {.proof}
definition of series convergence.
:::

<1>2. For $a_n = 1/10^n$, the partial sums are $s_N = \sum_{n=1}^{N} 10^{-n} = \frac{1/10 (1 - 10^{-N})}{1 - 1/10} = \frac{1}{9}(1 - 10^{-N})$.
::: {.proof}
geometric series formula.
:::

<1>3. $\lim_{N \to \infty} s_N = \frac{1}{9}(1 - 0) = \frac{1}{9}$.
::: {.proof}
<1>2 and $10^{-N} \to 0$.
:::

<1>4. Hence $\sum_{n=1}^{\infty} 1/10^n$ converges, to $\frac{1}{9}$.
::: {.proof}
<1>1 and <1>3.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
