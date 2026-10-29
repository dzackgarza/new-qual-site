---
schema: qual/card@1
id: P-GGJ5N
kind: problem
title: $\sum\frac{a_n}{\beta+a_n}$ diverges whenever $\sum a_n$ diverges, for $a_n>0$
  and $\beta>0$
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
Assume $\beta >0$, $a_n>0$, $n=1,2,\ldots$, and the series $\sum a_n$ is divergent.
Show that $\displaystyle \sum \frac{a_n}{\beta + a_n}$ is also divergent.
:::
::: {.solution}

::: pf

::: {.pf-step #s1}

For every $n$,
$$
\frac{a_n}{\beta+a_n}\geq
\frac12\min\left\{\frac{a_n}{\beta},1\right\}.
$$

::: pf-proof

If $a_n\leq\beta$, then $\beta+a_n\leq2\beta$, so the left side is at least $a_n/(2\beta)$. If $a_n>\beta$, then $\beta+a_n<2a_n$, so the left side exceeds $1/2$. These inequalities give the stated bound in both cases.

:::

:::

::: {.pf-step #s2}

The series $\sum_{n=1}^{\infty}\min\{a_n/\beta,1\}$ diverges.

::: pf-proof

Let $I=\{n\geq1:a_n\geq\beta\}$. If $I$ is infinite, the summand equals $1$ at every index in $I$, so the partial sums are unbounded. If $I$ is finite, the summand equals $a_n/\beta$ at every sufficiently large index. Its series then diverges because $\sum_n a_n$ diverges and $\beta>0$.

:::

:::

::: pf-step

The series $\sum_{n=1}^{\infty}\frac{a_n}{\beta+a_n}$ diverges to $+\infty$.

::: pf-proof

The terms are positive. By step [](#s1){.pf-ref}, their partial sums dominate half the corresponding partial sums of the divergent nonnegative series in step [](#s2){.pf-ref}. They are therefore unbounded and tend to $+\infty$.

:::

:::

:::

:::
