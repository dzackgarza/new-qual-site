---
schema: qual/card@1
id: P-PRACT20-W3-05
kind: problem
title: Sum of the power series $\sum n^2x^n$
classification:
  areas:
  - prelim
  topics:
  - Power Series
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
    source used for the statement. the printed problem asks for the value of the same series wherever it converges, and the printed solution gives the same rational function
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's route is transcribed: differentiate the geometric series twice, split n^2 = n(n-1)+n, and reassemble, with the radius of convergence stated.
---

::: {.problem}
Find the value of $\sum_{n=1}^{\infty} n^{2} x^{n}$ wherever the series converges.
:::

::: {.solution}

Write $S(x)=\sum_{n\ge1}n^2x^n$; the answer is that the series converges for
$\abs x<1$ and there equals a rational function.

::: pf

::: {.pf-step #series}

On $\abs x<1$, $\displaystyle\sum_{n\ge0}x^n=\frac{1}{1-x}$,
$\displaystyle\sum_{n\ge1}nx^{n-1}=\frac{1}{(1-x)^2}$ and
$\displaystyle\sum_{n\ge2}n(n-1)x^{n-2}=\frac{2}{(1-x)^3}$.

::: pf-proof

The first is the geometric series. A power series is differentiable term by
term inside its interval of convergence with the radius unchanged, so
differentiating gives
$\frac{d}{dx}\frac{1}{1-x}=\frac{1}{(1-x)^2}=\sum_{n\ge1}nx^{n-1}$, and
differentiating once more gives $\frac{2}{(1-x)^3}=\sum_{n\ge2}n(n-1)x^{n-2}$.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\sum_{n\ge1}n^2x^n=\frac{x+x^2}{(1-x)^3}}$ for $\abs
x<1$.

::: pf-proof

Since $n^2=n(n-1)+n$, the series splits as
$\sum_{n\ge2}n(n-1)x^n+\sum_{n\ge1}nx^n=x^2\sum_{n\ge2}n(n-1)x^{n-2}+x\sum_{n\ge1}nx^{n-1}$,
and by step [](#series){.pf-ref} this is
$\frac{2x^2}{(1-x)^3}+\frac{x}{(1-x)^2}=\frac{2x^2+x(1-x)}{(1-x)^3}=\frac{x+x^2}{(1-x)^3}$.
Both splittings are legitimate because the two series converge absolutely for
$\abs x<1$, and for $\abs x\ge1$ the terms $n^2x^n$ do not tend to $0$, so
there the series diverges.

:::

:::

:::


:::
