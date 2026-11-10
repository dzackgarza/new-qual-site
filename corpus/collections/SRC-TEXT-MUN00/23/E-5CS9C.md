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
---

::: {.exercise}

Determine whether or not $\RR^\omega$ is connected in the uniform topology.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.8, PDF p. 2** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the separation is theirs.

$\RR^{\omega}$ is **not** connected in the uniform topology. Let
$$
A=\{\mathbf{x}\mid \mathbf{x}\ \text{is bounded}\},\qquad B=\{\mathbf{x}\mid \mathbf{x}\ \text{is unbounded}\},
$$
so that $A\cup B=\RR^{\omega}$ and $A\cap B=\varnothing$, both nonempty. For $\mathbf{a}\in\RR^{\omega}$ and $0<\varepsilon<1$ put
$$
U(\mathbf{a},\varepsilon)=\prod_{n}(a_{n}-\varepsilon,a_{n}+\varepsilon),
$$
a basis element of the box topology containing $\mathbf{a}$; it contains the uniform ball $B_{\bar\rho}(\mathbf{a},\varepsilon)$ because $\bar\rho(\mathbf{a},\mathbf{x})<\varepsilon$ forces $\abs{a_{n}-x_{n}}<\varepsilon$ for every $n$. If $\mathbf{a}\in A$ then $U(\mathbf{a},\varepsilon)\subset A$: the coordinates of a point of $U$ differ from the bounded sequence $\mathbf{a}$ by less than $\varepsilon$, so it is bounded. If $\mathbf{a}\in B$ then $U(\mathbf{a},\varepsilon)\subset B$ similarly. So each of $A$ and $B$ is a union of balls, hence open in the uniform topology, and they separate it.
:::
