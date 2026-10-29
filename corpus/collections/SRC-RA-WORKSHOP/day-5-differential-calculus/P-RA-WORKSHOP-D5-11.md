---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-11
kind: problem
title: A function vanishing at both endpoints has a large derivative
classification:
  areas:
  - real-analysis
  topics:
  - Mean Value Theorem
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Assume that $f:[0,1]\to\RR$ is continuous on $[0,1]$ and differentiable on $(0,1)$ with $f(0)=f(1)=0$ and $f(c)=1$ for some $c\in(0,1)$.
Prove that there exists some $s\in(0,1)$ such that $\abs{f'(s)}>2$.
:::

::: {.solution}

::: pf

::: {.pf-step #off-center}

If $c \ne 1/2$, there is $s\in(0,1)$ with $\abs{f'(s)}>2$.

::: pf-proof

If $c < 1/2$, the mean value theorem on $[0,c]$ gives $s \in (0,c)$ with $f'(s) = (f(c) - f(0))/c = 1/c > 2$.
If $c > 1/2$, the mean value theorem on $[c,1]$ gives $s\in(c,1)$ with $f'(s) = (f(1) - f(c))/(1 - c) = -1/(1-c)$, and $1/(1-c) > 2$, so $\abs{f'(s)} > 2$.

:::

:::

::: {.pf-step #tent}

If $c=1/2$ and $\abs{f'(x)} \le 2$ for all $x \in (0,1)$, then $f(x)=2x$ on $[0,1/2]$ and $f(x)=2-2x$ on $[1/2,1]$.

::: pf-proof

For $0 < x < 1/2$, the mean value theorem on $[0,x]$ gives $f(x) = f'(\xi)x$ with $\abs{f'(\xi)} \le 2$, so $f(x) \le 2x$. The mean value theorem on $[x, 1/2]$ gives $1 - f(x) = f'(\eta)(1/2 - x)$ with $\abs{f'(\eta)} \le 2$, so $f(x) \ge 1 - 2(1/2 - x) = 2x$. Hence $f(x) = 2x$ on $(0,1/2)$, and at the endpoints by $f(0)=0$ and $f(1/2)=1$.

For $1/2 < x < 1$, the same argument on $[1/2, x]$ and $[x,1]$ gives $f(x) \geq 2-2x$ and $f(x)\leq 2-2x$, so $f(x) = 2 - 2x$ on $[1/2,1]$.

:::

:::

::: pf-step

There is $s\in(0,1)$ with $\abs{f'(s)}>2$.

::: pf-proof

If $c\neq1/2$, step [](#off-center){.pf-ref} gives $s$. If $c=1/2$, suppose $\abs{f'(x)}\leq2$ on $(0,1)$. By step [](#tent){.pf-ref}, the left derivative of $f$ at $1/2$ is $2$ and the right derivative is $-2$. They differ, so $f$ is not differentiable at $1/2 \in (0,1)$, which contradicts the hypothesis.

:::

:::

:::

:::
