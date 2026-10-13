---
schema: qual/card@1
id: P-C3MKZ
kind: problem
title: 'Convergence of $\sum_{n=1}^\infty \frac{x^n}{1+n|x|^n}$'
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
Determine the values of $x\in\mathbb{R}$ for which $\displaystyle\sum_{n=1}^\infty \frac{x^n}{1+n|x|^n}$ converges, justifying your answer carefully.
:::
::: {.solution}

::: pf

::: {.pf-step #s1}

If $|x|<1$, the series converges absolutely.

::: pf-proof

For every $n\geq1$,
\[
\left|\frac{x^n}{1+n|x|^n}\right|\leq |x|^n.
\]
The geometric series $\sum_{n\geq1}|x|^n$ converges, so comparison gives absolute convergence.

:::

:::

::: {.pf-step #s2}

If $x\geq1$, the series diverges to $+\infty$.

::: pf-proof

Since $0<x^{-n}\leq1$,
\[
\frac{x^n}{1+nx^n}=\frac1{n+x^{-n}}\geq\frac1{n+1}.
\]
The harmonic comparison series diverges, and all terms are nonnegative.

:::

:::

::: {.pf-step #s3}

If $x\leq-1$, the series converges conditionally.

::: pf-proof

Put $r=|x|\geq1$ and $c_n=1/(n+r^{-n})$. The summand is $(-1)^nc_n$. Moreover
\[
(n+1+r^{-(n+1)})-(n+r^{-n})
=1-r^{-n}(1-r^{-1})>0.
\]
Thus $(c_n)$ decreases strictly, and $0<c_n\leq1/n$ gives $c_n\to0$. The alternating-series test proves convergence. Since $r^{-n}\leq1$, however, $c_n\geq1/(n+1)$, so the series of absolute values diverges by harmonic comparison.

:::

:::

::: {.pf-step #s4}

The convergence set is $\boxed{(-\infty,1)}$, with absolute convergence precisely when $|x|<1$.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} cover every real value of $x$ and establish the asserted classifications.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the complete convergence classification.

:::

:::

:::
