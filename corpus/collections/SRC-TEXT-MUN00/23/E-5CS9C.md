---
schema: qual/card@1
id: E-5CS9C
kind: problem
title: Connectedness of $\RR^\omega$ in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §23 Exercise 8, printed p. 152, with the uniform
    metric of §20; the stored statement is the printed question.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.8, PDF p. 2. The bounded and the unbounded
    sequences are disjoint nonempty sets, each a union of uniform balls, hence a separation
    of R^omega in the uniform topology. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the bounded and unbounded sequences
    separate R^omega and that each is open in the uniform topology, an epsilon-ball with
    epsilon <= 1 controlling every coordinate. positron0802, Chapter 3 Exercise 23.8, PDF p.
    2. The printed statement needed no repair.
---

::: {.exercise}

Determine whether or not $\RR^\omega$ is connected in the uniform topology.
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.8, PDF p. 2** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the separation is theirs.

::: pf

::: {.pf-step #sets}
With $A$ the set of bounded elements of $\RR^{\omega}$ and $B$ its complement, $A$ and $B$ are nonempty, disjoint, and $A\cup B=\RR^{\omega}$.

::: pf-proof
Every element of $\RR^{\omega}$ is either bounded or not, so $A\cup B=\RR^{\omega}$ and $A\cap B=\varnothing$; the zero sequence is bounded and the sequence $(n)_{n}$ is not, so both sets are nonempty.
:::

:::

::: {.pf-step #A-open}
$A$ is open in the uniform topology.

::: pf-proof
Let $\mathbf{a}\in A$ and let $B_{\bar\rho}(\mathbf{a},\varepsilon)$ be a uniform ball about it, with $0<\varepsilon\le1$. If $\bar\rho(\mathbf{a},\mathbf{x})<\varepsilon$ then $\min\{\abs{a_{n}-x_{n}},1\}<\varepsilon\le1$, so $\abs{a_{n}-x_{n}}<\varepsilon$ for every $n$; since $\mathbf{a}$ is bounded by $M$, the sequence $\mathbf{x}$ is bounded by $M+\varepsilon$, so $\mathbf{x}\in A$. Hence $B_{\bar\rho}(\mathbf{a},\varepsilon)\subset A$ and $A$ is a union of uniform balls, hence open.
:::

:::

::: {.pf-step #B-open}
$B$ is open in the uniform topology.

::: pf-proof
Let $\mathbf{b}\in B$ and $0<\varepsilon\le1$. If $\mathbf{x}$ satisfied $\bar\rho(\mathbf{b},\mathbf{x})<\varepsilon$, then as in step [](#A-open){.pf-ref} one would have $\abs{b_{n}-x_{n}}<\varepsilon$ for every $n$, and $\mathbf{x}$ bounded by $M$ would make $\mathbf{b}$ bounded by $M+\varepsilon$, contrary to $\mathbf{b}\in B$. So $B_{\bar\rho}(\mathbf{b},\varepsilon)\subset B$ and $B$ is open.
:::

:::

::: {.pf-step}
$\RR^{\omega}$ is not connected in the uniform topology.

::: pf-proof
Steps [](#sets){.pf-ref}, [](#A-open){.pf-ref} and [](#B-open){.pf-ref} exhibit a separation of $\RR^{\omega}$ in the uniform topology, so that space is disconnected.
:::

:::

:::
:::
