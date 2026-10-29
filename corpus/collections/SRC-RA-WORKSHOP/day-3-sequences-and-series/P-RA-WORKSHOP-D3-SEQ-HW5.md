---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-HW5
kind: problem
title: Limit of the Babylonian square-root iteration
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
  - Fixed Points
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(c.f. [Abb01, Exercise 2.4.5]) Let $x_1=2$ and define
$$
x_{n+1}=\frac12\left(x_n+\frac{2}{x_n}\right).
$$
Find $\lim_{n\to\infty}x_n$.
Hint: Show that $\{x_n\}$ is decreasing.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every iterate satisfies $x_n\geq\sqrt2>0$.

::: pf-proof

The initial value is $x_1=2>\sqrt2$. If $x_n>0$, the arithmetic–geometric mean inequality yields
\[
x_{n+1}=\frac12\left(x_n+\frac2{x_n}\right)
\geq\sqrt{x_n\frac2{x_n}}=\sqrt2.
\]
Induction proves the assertion and shows the recurrence is defined for every $n$.

:::

:::

::: {.pf-step #s2}

The sequence $(x_n)$ is nonincreasing.

::: pf-proof

By step [](#s1){.pf-ref}, $x_n^2\geq2$. Consequently
\[
x_{n+1}-x_n=\frac{2-x_n^2}{2x_n}\leq0
\]
for every $n$.

:::

:::

::: {.pf-step #s3}

The sequence converges to $\boxed{\sqrt2}$.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} show that $(x_n)$ is bounded below and nonincreasing, so it converges to some $L\geq\sqrt2$. Since $L>0$, continuity of $t\mapsto(t+2/t)/2$ for positive $t$ permits passage to the limit:
\[
L=\frac12\left(L+\frac2L\right).
\]
Multiplying by $2L$ gives $L^2=2$. The inequality $L>0$ therefore yields $L=\sqrt2$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} identifies the requested limit.

:::

:::

:::
