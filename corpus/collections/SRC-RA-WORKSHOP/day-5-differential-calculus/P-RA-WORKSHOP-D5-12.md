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
(January 2010 #4) Suppose that $f:\mathbb R\to\mathbb R$ is differentiable at $a\in\mathbb R$.
If $\{x_n\}$ is a nondecreasing sequence of real numbers converging to $a$ and $\{y_n\}$ is a nonincreasing sequence of real numbers converging to $a$, and $x_n\ne y_n$ for all sufficiently large $n$, prove that $$\lim_{n\to\infty}\frac{f(y_n)-f(x_n)}{y_n-x_n}=f'(a).$$
:::

::: {.solution}
Define $r:\mathbb R\to\mathbb R$ by
\[
r(t)=\begin{cases}\dfrac{f(t)-f(a)}{t-a}-f'(a),&t\ne a,\\0,&t=a.\end{cases}
\]

<1>1. The function $r$ is continuous at $a$ and satisfies
\[
f(t)=f(a)+(t-a)(f'(a)+r(t))\qquad(t\in\mathbb R).
\]

::: {.proof}
The defining limit for $f'(a)$ gives $\lim_{t\to a}r(t)=0=r(a)$. The identity follows by multiplication when $t\ne a$ and holds at $t=a$ because both sides equal $f(a)$.
:::

<1>2. For every sufficiently large $n$, the secant quotient satisfies
\[
\left|\frac{f(y_n)-f(x_n)}{y_n-x_n}-f'(a)\right|
\leq\max\{|r(x_n)|,|r(y_n)|\}.
\]

::: {.proof}
Monotonicity and convergence imply $x_n\leq a\leq y_n$. For all sufficiently large $n$ the additional hypothesis gives $x_n<y_n$. By step <1>1,
\[
\frac{f(y_n)-f(x_n)}{y_n-x_n}-f'(a)
=\frac{y_n-a}{y_n-x_n}r(y_n)
+\frac{a-x_n}{y_n-x_n}r(x_n).
\]
The coefficients are nonnegative and sum to one, so the triangle inequality gives the claimed bound, including when either endpoint equals $a$.
:::

<1>3. The limit is
\[
\boxed{\lim_{n\to\infty}\frac{f(y_n)-f(x_n)}{y_n-x_n}=f'(a)}.
\]

::: {.proof}
Since $x_n\to a$ and $y_n\to a$, continuity of $r$ at $a$ from step <1>1 gives $r(x_n)\to0$ and $r(y_n)\to0$. The bound in step <1>2 therefore tends to zero.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the asserted limit wherever the quotient is eventually defined.
:::
:::
