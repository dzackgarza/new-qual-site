---
schema: qual/card@1
id: P-PRACT20-W3-03
kind: problem
title: The integral $\int_0^\infty\lfloor x\rfloor e^{-x}\,dx$
classification:
  areas:
  - prelim
  topics:
  - Improper Integrals
  - Series
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed OCR junk from the integrand, checked against Week3_solns.pdf page 1 (Problem 3).
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 1 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem is the same integral of the floor function against e^{-x} over [0, infinity)
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's split over the intervals [n, n+1), its telescoping cancellation of the two sums, and the geometric series, written out with the interchange justified by absolute convergence.
---

::: {.problem}
Compute $\int_0^\infty \lfloor x \rfloor e^{-x}\,dx$ where $\lfloor x \rfloor$ denotes the largest integer not exceeding $x$.
:::

::: {.solution}

Let $\lfloor x\rfloor$ be the greatest integer not exceeding $x$; the integral
$\int_0^\infty\lfloor x\rfloor e^{-x}\,dx$ is an improper integral of a
nonnegative piecewise-continuous function.

::: pf

::: {.pf-step #split}

$\displaystyle\int_0^\infty\lfloor x\rfloor
e^{-x}\,dx=\sum_{n\ge1}n\big(e^{-n}-e^{-(n+1)}\big)$.

::: pf-proof

On $[n,n+1)$ with $n\in\NN_0$ the integrand is $ne^{-x}$, and the intervals
$[n,n+1)$ tile $[0,\infty)$, so the integral is the sum over $n$ of $ne^{-x}$
integrated over $[n,n+1)$; the term for $n=0$ vanishes because $\lfloor
x\rfloor=0$ on $[0,1)$. Each piece is
$\int_n^{n+1}ne^{-x}dx=n(e^{-n}-e^{-(n+1)})$, and the sum converges since
$\sum n e^{-n}$ does.

:::

:::

::: {.pf-step #telescope}

$\displaystyle\sum_{n\ge1}n\big(e^{-n}-e^{-(n+1)}\big)=\sum_{n\ge1}e^{-n}=\frac{1}{e-1}$.

::: pf-proof

Writing the sum as $\sum_{n\ge1}ne^{-n}-\sum_{n\ge1}ne^{-(n+1)}$ and
reindexing the second as $\sum_{m\ge2}(m-1)e^{-m}$, the difference is
$\sum_{n\ge1}ne^{-n}-\sum_{n\ge2}(n-1)e^{-n}$, whose partial sums are
absolutely convergent, so it equals $1\cdot
e^{-1}+\sum_{n\ge2}\big(n-(n-1)\big)e^{-n}=\sum_{n\ge1}e^{-n}$. That geometric
series with ratio $e^{-1}$ sums to $\frac{e^{-1}}{1-e^{-1}}=\frac{1}{e-1}$.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int_0^\infty\lfloor x\rfloor e^{-x}\,dx=\frac{1}{e-1}}$.

::: pf-proof

Steps [](#split){.pf-ref} and [](#telescope){.pf-ref} compute the integral as
$\frac{1}{e-1}\approx0.582$, which is consistent with the crude bounds
$\int_0^\infty(x-1)e^{-x}dx=0\le I\le\int_0^\infty xe^{-x}dx=1$. The improper
integral therefore converges and has the stated value.

:::

:::

:::


:::
