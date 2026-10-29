---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-HW3
kind: problem
title: Conditional convergence with divergent square series prevents absolute convergence
  (warm-up)
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Let $\{a_k\}$ be a sequence of real numbers such that the series $\sum_{k=1}^{\infty}a_k$ converges and $\sum_{k=1}^{\infty}a_k^2$ diverges.
Prove that $\sum_{k=1}^{\infty}a_k$ does not converge absolutely.
(See also June 2010 #3a where you are instead told that $\sum_{k=1}^{\infty}a_ka_{k+1}$ diverges and asked to show the same result.
Compare this to June 2009 #3a and January 2005 #1b.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $\sum_{k=1}^{\infty}\abs{a_k}$ converges, then there is $N$ such that $0\leq a_k^2\leq \abs{a_k}$ for all $k\geq N$.

::: pf-proof

Convergence of the nonnegative series implies $\abs{a_k}\to0$. Choose $N$ so that $\abs{a_k}\leq1$ for $k\geq N$. Then $a_k^2=\abs{a_k}^2\leq\abs{a_k}$.

:::

:::

::: pf-step

The series $\sum_{k=1}^{\infty}a_k$ does not converge absolutely.

::: pf-proof

Suppose $\sum_{k=1}^{\infty}\abs{a_k}$ converges. By step [](#s1){.pf-ref} and comparison of nonnegative series, the tail $\sum_{k=N}^{\infty}a_k^2$ converges. Adding the finite initial sum would make $\sum_{k=1}^{\infty}a_k^2$ convergent, contrary to the hypothesis.

:::

:::

:::

:::
