---
schema: qual/card@1
id: P-BKF18-8B
kind: problem
title: No positive integer solutions to $x^2+y^2=7xy$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Show that there are no natural numbers $x,y\ge1$ such that
$$
x^2+y^2=7xy.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $x,y\ge1$ satisfy $x^2+y^2=7xy$, then $7\mid x$ and $7\mid y$.

::: pf-proof

Reduce modulo $7$: $x^2+y^2\equiv0\pmod 7$. The squares modulo $7$ are $0,1,2,4$, and the only pair of them with sum $\equiv0$ is $0,0$. So $x^2\equiv y^2\equiv0$, and since $7$ is prime, $7\mid x$ and $7\mid y$.

:::

:::

::: {.pf-step #s2}

If $(x,y)$ is a solution, then $(x/7,y/7)$ is a solution in positive integers.

::: pf-proof

By step [](#s1){.pf-ref}, $x=7x_1$, $y=7y_1$ with $x_1,y_1\ge1$. Dividing the equation by $49$ gives $x_1^2+y_1^2=7x_1y_1$.

:::

:::

::: pf-qed

Take a solution with $x$ minimal. Step [](#s2){.pf-ref} gives a solution with first coordinate $x/7<x$, a contradiction. So there is no solution.

:::

:::

:::
