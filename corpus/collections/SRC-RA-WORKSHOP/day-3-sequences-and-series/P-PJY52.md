---
schema: qual/card@1
id: P-PJY52
kind: problem
title: A conditionally convergent series has radius of convergence 1
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - Series of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
If the series $\sum_{n=0}^\infty a_n$ converges conditionally, show that the radius of convergence of the power series $\sum_{n=0}^\infty a_nx^n$ is 1.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The coefficient sequence $(a_n)$ is bounded.

::: pf-proof

Since $\sum_{n=0}^{\infty}a_n$ converges, the difference of consecutive partial sums gives $a_n\to0$. Every convergent sequence is bounded, so some $C>0$ satisfies $|a_n|\leq C$ for all $n$.

:::

:::

::: {.pf-step #s2}

The radius of convergence $R$ satisfies $R\geq1$.

::: pf-proof

For every $|x|<1$, step [](#s1){.pf-ref} gives $|a_nx^n|\leq C|x|^n$. The geometric comparison series converges. Thus the power series converges absolutely throughout $|x|<1$, proving $R\geq1$.

:::

:::

::: {.pf-step #s3}

The radius satisfies $R\leq1$.

::: pf-proof

If $R>1$, then $x=1$ lies strictly inside the disk of convergence. A power series converges absolutely at every point strictly inside its radius; hence $\sum_n|a_n1^n|=\sum_n|a_n|$ converges. This contradicts the assumption that $\sum_n a_n$ converges only conditionally.

:::

:::

::: {.pf-step #s4}

The radius of convergence is $\boxed{R=1}$.

::: pf-proof

The inequalities of steps [](#s2){.pf-ref} and [](#s3){.pf-ref} imply $1\leq R\leq1$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} establishes the required radius.

:::

:::

:::
