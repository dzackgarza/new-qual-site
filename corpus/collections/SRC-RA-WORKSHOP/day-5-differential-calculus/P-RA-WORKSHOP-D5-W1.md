---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-W1
kind: problem
title: A function with zero derivative is constant
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Mean Value Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
(June 1999 #10) Show that if $f$ is differentiable on $(a,b)$ with $f'(x)=0$ on $(a,b)$, then $f$ is constant on $(a,b)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $a<x<y<b$, one has $f(y)=f(x)$.

::: pf-proof

Differentiability of $f$ on $(a,b)$ implies continuity on $[x,y]$ and differentiability on $(x,y)$. The mean value theorem therefore supplies $\xi\in(x,y)$ such that
$$
f(y)-f(x)=f'(\xi)(y-x)=0,
$$
because $f'$ vanishes throughout $(a,b)$.

:::

:::

::: pf-step

The function $f$ is constant on $(a,b)$.

::: pf-proof

Choose any $x_0\in(a,b)$. For each $x\in(a,b)$ with $x\ne x_0$, step [](#s1){.pf-ref} applied to the smaller and larger of $x,x_0$ gives $f(x)=f(x_0)$. The equality also holds when $x=x_0$.

:::

:::

:::

:::
