---
schema: qual/card@1
id: P-FB5CY
kind: problem
title: A power series whose interval of convergence is exactly $[3,5)$
classification:
  areas:
  - prelim
  topics:
  - Power Series
  - Convergence Tests
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Give an example, with proof, of a power series that converges exactly on the interval $[3,5)$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own example follows, with the radius, the two endpoints and the divergence outside as separate steps.

::: pf

::: {.pf-step #radius}
$\sum_{n\ge1}\dfrac{(x-4)^{n}}{n}$ has radius of convergence $1$ about $4$.

::: pf-proof
With $a_{n}=1/n$ one has $\abs{a_{n}/a_{n+1}}=(n+1)/n\to1$, so the radius is $R=1$ by the ratio test; the series therefore converges absolutely for $\abs{x-4}<1$ and diverges for $\abs{x-4}>1$.
:::

:::

::: {.pf-step #left-endpoint}
At $x=3$ the series converges: $\sum_{n\ge1}\dfrac{(-1)^{n}}{n}$ is the alternating harmonic series.

::: pf-proof
At $x=3$ the terms are $\dfrac{(3-4)^{n}}{n}=\dfrac{(-1)^{n}}{n}$; the terms alternate in sign, decrease in absolute value to $0$, so the series converges by the alternating series test.
:::

:::

::: {.pf-step #right-endpoint}
At $x=5$ the series diverges: it is the harmonic series $\sum_{n\ge1}\dfrac{1}{n}$.

::: pf-proof
At $x=5$ the terms are $\dfrac{1}{n}$, whose partial sums $\sum_{n\le N}1/n$ are unbounded, so the series diverges.
:::

:::

::: {.pf-step #outside}
The series diverges for every $x$ with $\abs{x-4}>1$.

::: pf-proof
If $\abs{x-4}>1$ then $\abs{(x-4)^{n}/n}=\abs{x-4}^{n}/n\to\infty$, so the terms do not tend to $0$ and the series diverges.
:::

:::

::: {.pf-qed}
The set of convergence of $\sum_{n\ge1}(x-4)^{n}/n$ is exactly $[3,5)$: convergence on $(3,5)$ by step [](#radius){.pf-ref}, at the left endpoint by step [](#left-endpoint){.pf-ref}, divergence at the right endpoint by step [](#right-endpoint){.pf-ref} and outside by step [](#outside){.pf-ref}.
:::

:::

:::
