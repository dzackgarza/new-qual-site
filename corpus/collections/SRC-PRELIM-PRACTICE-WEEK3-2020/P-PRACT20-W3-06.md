---
schema: qual/card@1
id: P-PRACT20-W3-06
kind: problem
title: Convergence of $\sum n!\,x^n$ and $\sum n!\,x^{n^2}$
classification:
  areas:
  - prelim
  topics:
  - Power Series
  - Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 2 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem asks exactly the two questions of (a) and (b), with the same two series, and the printed solution gives the same two answers
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's two ratio tests are transcribed: divergence for every nonzero x in (a) because the ratio is (n+1)abs x, and convergence for abs x below 1 in (b) because the ratio is (n+1)abs x to the 2n+1, with the cases abs x at least 1 disposed of by the terms not tending to zero.
---

::: {.problem}
(a) For which $x$ does $\sum_{n=1}^{\infty} n!\, x^{n}$ converge?

(b) For which $x$ does $\sum_{n=1}^{\infty} n!\, x^{n^{2}}$ converge?
:::

::: {.solution}

Consider the two series of numbers attached to $x$.

::: pf

::: {.pf-step #parta}

$\sum_{n\ge1}n!\,x^n$ converges if and only if $x=0$.

::: pf-proof

For $x\ne0$ the ratio of consecutive absolute values is $\frac{(n+1)!\abs
x^{n+1}}{n!\abs x^n}=(n+1)\abs x\to\infty$, so the terms do not tend to $0$
(indeed $\abs{n!x^n}\to\infty$) and the series diverges; the ratio test in
this form proves divergence when the ratio tends to infinity. For $x=0$ every
term is $0$ and the series is $0$.

:::

:::

::: {.pf-step #partb}

$\sum_{n\ge1}n!\,x^{n^2}$ converges if and only if $\abs x<1$.

::: pf-proof

For $\abs x<1$ the ratio of consecutive absolute values is $(n+1)\abs
x^{2n+1}=(n+1)e^{(2n+1)\log\abs x}$, and since $\log\abs x<0$ the exponential
decays faster than any polynomial, so the ratio tends to $0<1$ and the series
converges by the ratio test. For $\abs x\ge1$ the terms satisfy
$\abs{n!x^{n^2}}\ge n!\to\infty$, so they do not tend to $0$ and the series
diverges. Hence the convergence set is the open unit interval, in contrast
with part (a), where it is a single point.

:::

:::

:::


:::
