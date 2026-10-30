---
schema: qual/card@1
id: E-SS10.EX-3
kind: problem
title: Solving $u_n=au_{n-1}+bu_{n-2}$ by generating functions
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Generating Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
More generally, consider the difference equation given by the initial values $u_0$ and $u_1$, and the recurrence relation $u_n = a u_{n-1} + b u_{n-2}$ for $n \geq 2$. Define the generating function associated to $\{u_n\}_{n=0}^{\infty}$ by $U(x) = \sum_{n=0}^{\infty} u_n x^n$. The recurrence relation implies that $U(x)(1 - ax - bx^2) = u_0 + (u_1 - a u_0) x$ in a neighborhood of the origin. If $\alpha$ and $\beta$ denote the roots of the polynomial $p(x) = x^2 - ax - b$, then we may write
$$
U(x) = \frac{u_0 + (u_1 - a u_0) x}{(1 - \alpha x)(1 - \beta x)} = \frac{A}{1 - \alpha x} + \frac{B}{1 - \beta x} = A \sum_{n=0}^{\infty} \alpha^n x^n + B \sum_{n=0}^{\infty} \beta^n x^n,
$$
where it is an easy matter to solve for $A$ and $B$. Finally, this gives $u_n = A\alpha^n + B\beta^n$. Note that this approach yields a solution to our problem if the roots of $p$ are distinct, namely $\alpha \neq \beta$. A variant of the formula holds if $\alpha = \beta$.
:::

::: {.solution}
Let $U(x) = \sum_{n \ge 0} u_n x^n$ and let $\alpha, \beta$ be the roots of $x^2 - ax - b$. By induction $\abs{u_n}\le C M^n$ with $M=\max(1,\abs a+\abs b)$ and $C=\max(\abs{u_0},\abs{u_1})$, so $U$ converges for $\abs x<1/M$.

::: pf

::: {.pf-step #s1}

$U(x) = \dfrac{u_0 + (u_1 - a u_0)x}{(1 - \alpha x)(1 - \beta x)}$ near $0$.

::: pf-proof

Multiplying the recurrence by $x^n$ and summing over $n \ge 2$ gives $U(x) - u_0 - u_1x = ax\bigl(U(x) - u_0\bigr) + bx^2U(x)$, that is, $U(x)(1 - ax - bx^2) = u_0 + (u_1 - a u_0)x$. Since $x^2 - ax - b = (x - \alpha)(x - \beta)$, we have $1 - ax - bx^2 = (1 - \alpha x)(1 - \beta x)$.

:::

:::

::: pf-step

If $\alpha \neq \beta$, then $u_n = A \alpha^n + B \beta^n$ for constants $A,B$.

::: pf-proof

Partial fractions in step [](#s1){.pf-ref} give $U(x) = \frac{A}{1 - \alpha x} + \frac{B}{1 - \beta x}$. Expanding both geometric series near $0$ and comparing coefficients gives the formula.

:::

:::

::: pf-step

If $\alpha = \beta$, then $u_n = \bigl(A + B(n+1)\bigr)\alpha^n$ for constants $A,B$.

::: pf-proof

The partial fraction decomposition with a repeated root gives $U(x) = \frac{A}{1 - \alpha x} + \frac{B}{(1 - \alpha x)^2}$, and $\frac{1}{(1-\alpha x)^2}=\sum_{n\ge0}(n+1)\alpha^nx^n$.

:::

:::

:::

:::
