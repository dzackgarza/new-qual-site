---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-12
kind: problem
title: A two-sided sequence quotient converges to the derivative
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Sequences of Numbers
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(January 2010 #4) Suppose that $f:\RR\to\RR$ is differentiable at $a\in\RR$.
If $\{x_n\}$ is a nondecreasing sequence of real numbers converging to $a$ and $\{y_n\}$ is a nonincreasing sequence of real numbers converging to $a$, and $x_n\ne y_n$ for all sufficiently large $n$, prove that $$\lim_{n\to\infty}\frac{f(y_n)-f(x_n)}{y_n-x_n}=f'(a).$$
:::

::: {.solution}
Define $r:\RR\to\RR$ by
$$
r(t)=\begin{cases}\dfrac{f(t)-f(a)}{t-a}-f'(a),&t\ne a,\\0,&t=a.\end{cases}
$$

::: pf

::: {.pf-step #s1}

The function $r$ is continuous at $a$ and satisfies
$$
f(t)=f(a)+(t-a)(f'(a)+r(t))\qquad(t\in\RR).
$$

::: pf-proof

The defining limit for $f'(a)$ gives $\lim_{t\to a}r(t)=0=r(a)$. The identity follows by multiplication when $t\ne a$ and holds at $t=a$ because both sides equal $f(a)$.

:::

:::

::: {.pf-step #s2}

For every sufficiently large $n$, the secant quotient satisfies
$$
\abs{\frac{f(y_n)-f(x_n)}{y_n-x_n}-f'(a)}
\leq\max\{\abs{r(x_n)},\abs{r(y_n)}\}.
$$

::: pf-proof

Monotonicity and convergence imply $x_n\leq a\leq y_n$. For all sufficiently large $n$ the additional hypothesis gives $x_n<y_n$. By step [](#s1){.pf-ref},
$$
\frac{f(y_n)-f(x_n)}{y_n-x_n}-f'(a)
=\frac{y_n-a}{y_n-x_n}r(y_n)
+\frac{a-x_n}{y_n-x_n}r(x_n).
$$
The coefficients are nonnegative and sum to one, so the triangle inequality gives the claimed bound, including when either endpoint equals $a$.

:::

:::

::: pf-step

$$
\lim_{n\to\infty}\frac{f(y_n)-f(x_n)}{y_n-x_n}=f'(a).
$$

::: pf-proof

Since $x_n\to a$ and $y_n\to a$, continuity of $r$ at $a$ from step [](#s1){.pf-ref} gives $r(x_n)\to0$ and $r(y_n)\to0$. The bound in step [](#s2){.pf-ref} therefore tends to zero.

:::

:::

:::

:::
