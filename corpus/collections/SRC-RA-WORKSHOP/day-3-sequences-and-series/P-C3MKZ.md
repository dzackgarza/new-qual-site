---
schema: qual/card@1
id: P-C3MKZ
kind: problem
title: 'Convergence of $\sum_{n=1}^\infty \frac{x^n}{1+n\abs{x}^n}$'
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - Convergence of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Determine the values of $x\in\RR$ for which $\displaystyle\sum_{n=1}^\infty \frac{x^n}{1+n\abs{x}^n}$ converges, justifying your answer carefully.
:::
::: {.solution}

::: pf

::: {.pf-step #s1}

If $\abs{x}<1$, the series converges absolutely.

::: pf-proof

For every $n\geq1$,
$$
\abs{\frac{x^n}{1+n\abs{x}^n}}\leq \abs{x}^n.
$$
The geometric series $\sum_{n\geq1}\abs{x}^n$ converges, so comparison gives absolute convergence.

:::

:::

::: {.pf-step #s2}

If $x\geq1$, the series diverges to $+\infty$.

::: pf-proof

Since $0<x^{-n}\leq1$,
$$
\frac{x^n}{1+nx^n}=\frac1{n+x^{-n}}\geq\frac1{n+1}.
$$
The harmonic comparison series diverges, and all terms are nonnegative.

:::

:::

::: {.pf-step #s3}

If $x\leq-1$, the series converges conditionally.

::: pf-proof

Put $r=\abs{x}\geq1$ and $c_n=1/(n+r^{-n})$. The summand is $(-1)^nc_n$. Moreover
$$
(n+1+r^{-(n+1)})-(n+r^{-n})
=1-r^{-n}(1-r^{-1})>0.
$$
Thus $(c_n)$ decreases strictly, and $0<c_n\leq1/n$ gives $c_n\to0$. The alternating-series test proves convergence. Since $r^{-n}\leq1$, however, $c_n\geq1/(n+1)$, so the series of absolute values diverges by harmonic comparison.

:::

:::

::: pf-step

The convergence set is $\boxed{(-\infty,1)}$, with absolute convergence precisely when $\abs{x}<1$.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} cover every real value of $x$: the series converges absolutely for $\abs{x}<1$, conditionally for $x\leq-1$, and diverges for $x\geq1$.

:::

:::

:::

:::
