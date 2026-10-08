---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-HW5
kind: problem
title: Analyze the Babylonian square-root iteration (warm-up)
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
<1>1. Every iterate satisfies $x_n\geq\sqrt2>0$.

::: {.proof}
The initial value is $x_1=2>\sqrt2$. If $x_n>0$, the arithmetic–geometric mean inequality yields
\[
x_{n+1}=\frac12\left(x_n+\frac2{x_n}\right)
\geq\sqrt{x_n\frac2{x_n}}=\sqrt2.
\]
Induction proves the assertion and shows the recurrence is defined for every $n$.
:::

<1>2. The sequence $(x_n)$ is nonincreasing.

::: {.proof}
By step <1>1, $x_n^2\geq2$. Consequently
\[
x_{n+1}-x_n=\frac{2-x_n^2}{2x_n}\leq0
\]
for every $n$.
:::

<1>3. The sequence converges to $\boxed{\sqrt2}$.

::: {.proof}
Steps <1>1 and <1>2 show that $(x_n)$ is bounded below and nonincreasing, so it converges to some $L\geq\sqrt2$. Since $L>0$, continuity of $t\mapsto(t+2/t)/2$ for positive $t$ permits passage to the limit:
\[
L=\frac12\left(L+\frac2L\right).
\]
Multiplying by $2L$ gives $L^2=2$. The inequality $L>0$ therefore yields $L=\sqrt2$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 identifies the requested limit.
:::
:::
