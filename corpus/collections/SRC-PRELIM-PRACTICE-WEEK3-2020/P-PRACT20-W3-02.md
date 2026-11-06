---
schema: qual/card@1
id: P-PRACT20-W3-02
kind: problem
title: Convergence of $\sum n!\,x^{2n}/(n^n(1+x^{2n}))$
classification:
  areas:
  - prelim
  topics:
  - Series
  - Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 1 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem asks for the same set of x, which the printed solution identifies as all of R
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's comparison with sum n!/n^n, the bound x^{2n}/(1+x^{2n}) <= 1, and the ratio test limit 1/e, with the argument spelled out.
---

::: {.problem}
For which values of $x$ does $\displaystyle \sum_{n=1}^{\infty} \frac{n!\, x^{2n}}{n^{n} (1 + x^{2n})}$ converge?
:::

::: {.solution}

Consider $\sum_{n\ge1}\dfrac{n!\,x^{2n}}{n^n(1+x^{2n})}$ for real $x$; the
answer is that it converges for every $x$.

::: pf

::: {.pf-step #absolutesummable}

For every $x$,
$\displaystyle\sum_{n\ge1}\left|\frac{n!x^{2n}}{n^n(1+x^{2n})}\right|\le\sum_{n\ge1}\frac{n!}{n^n}$,
and the latter converges.

::: pf-proof

Since $1+x^{2n}\ge1$ we have
$\left|\frac{n!x^{2n}}{n^n(1+x^{2n})}\right|\le\frac{n!x^{2n}}{n^n
x^{2n}}\cdot\frac{x^{2n}}{1+x^{2n}}\le\frac{n!}{n^n}$, because
$\frac{x^{2n}}{1+x^{2n}}\le1$ for $x\ne0$ and the term is $0$ for $x=0$. For
$\sum\frac{n!}{n^n}$ the ratio test gives
$\frac{a_{n+1}}{a_n}=\frac{(n+1)!n^n}{n!(n+1)^{n+1}}=\frac{1}{(1+1/n)^n}\to\frac1e<1$,
so the series converges; the limit $\frac1e$ is the standard limit of
$(1+1/n)^n$.

:::

:::

::: {.pf-step #conclusion}

The series converges absolutely, hence converges, for all $x\in\RR$.

::: pf-proof

Step [](#absolutesummable){.pf-ref} bounds the terms by those of a convergent
positive series independent of $x$, and the comparison test for absolute
convergence gives absolute convergence at every $x$. So the set of $x$ for
which the series converges is all of $\RR$; note that this is convergence of
the series of numbers for each fixed $x$, the bound being uniform in $x$ but
the terms depending on $x$.

:::

:::

:::


:::
