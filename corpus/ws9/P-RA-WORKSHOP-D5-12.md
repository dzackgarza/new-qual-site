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
---

::: {.problem title="?"}
(January 2010 #4) Suppose that $f:\mathbb R\to\mathbb R$ is differentiable at $a\in\mathbb R$.
If $\{x_n\}$ is an increasing sequence of real numbers converging to $a$ and $\{y_n\}$ is a decreasing sequence of real numbers converging to $a$, prove that $$\lim_{n\to\infty}\frac{f(y_n)-f(x_n)}{y_n-x_n}=f'(a).$$
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Decompose the quotient.
Proof: write $x_n \nearrow a$, $y_n \searrow a$ with $x_n < a < y_n$ for all $n$.
Then \[\frac{f(y_n) - f(x_n)}{y_n - x_n} = \frac{(f(y_n) - f(a)) + (f(a) - f(x_n))}{y_n - x_n} = \frac{y_n - a}{y_n - x_n}\cdot\frac{f(y_n) - f(a)}{y_n - a} + \frac{a - x_n}{y_n - x_n}\cdot\frac{f(a) - f(x_n)}{a - x_n}.\] <1>2. The coefficients are a convex combination.
Proof: $\lambda_n = \frac{y_n - a}{y_n - x_n} \in (0,1)$ and $\frac{a - x_n}{y_n - x_n} = 1 - \lambda_n$; indeed $(y_n - a) + (a - x_n) = y_n - x_n$.
<1>3. Both difference quotients tend to $f'(a)$.
Proof: $\frac{f(y_n) - f(a)}{y_n - a} \to f'(a)$ as $y_n \to a^+$ (subsequence of the defining limit), and $\frac{f(a) - f(x_n)}{a - x_n} = \frac{f(x_n) - f(a)}{x_n - a} \to f'(a)$ as $x_n \to a^-$.
<1>4. Conclude.
Proof: the quotient is $\lambda_n A_n + (1-\lambda_n)B_n$ with $A_n, B_n \to f'(a)$ and $0 \le \lambda_n \le 1$; hence \[\lim_{n\to\infty}\frac{f(y_n) - f(x_n)}{y_n - x_n} = f'(a).\] <1>5. Q.E.D.
:::
