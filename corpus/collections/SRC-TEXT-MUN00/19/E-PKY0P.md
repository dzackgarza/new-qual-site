---
schema: qual/card@1
id: E-PKY0P
kind: problem
title: Closure of the eventually-zero sequences in box and product topologies
classification:
  areas:
  - topology
  topics:
  - Closure
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Let $\mathbb{R}^\infty$ be the subset of $\mathbb{R}^\omega$ consisting of all sequences that are "eventually zero," that is, all sequences $(x_1, x_2, \ldots)$ such that $x_i \neq 0$ for only finitely many values of $i$.
What is the closure of $\mathbb{R}^\infty$ in $\mathbb{R}^\omega$ in the box and product topologies?
Justify your answer.
:::

::: {.solution}
<1>1. In the product topology, $\overline{\RR^\infty}=\boxed{\RR^\omega}$.

::: {.proof}
A nonempty basic open set is $\prod_iU_i$ with $U_i$ open and nonempty, and $U_i=\RR$ except for $i$ in a finite set $F$.
Choose $z_i\in U_i$ for $i\in F$ and $z_i=0$ for $i\notin F$.
Then $z=(z_i)$ is eventually zero and lies in $\prod_iU_i$, so every nonempty open set meets $\RR^\infty$.
:::

<1>2. In the box topology, $\overline{\RR^\infty}=\boxed{\RR^\infty}$.

::: {.proof}
Let $x\notin\RR^\infty$, so the set $S=\{i:x_i\ne0\}$ is infinite.
Put $U_i=\RR-\{0\}$ for $i\in S$ and $U_i=\RR$ for $i\notin S$.
Then $\prod_iU_i$ is a box neighborhood of $x$.
An eventually-zero sequence $z$ has $z_i=0$ for some $i\in S$, because $S$ is infinite, so $z\notin\prod_iU_i$.
Hence the complement of $\RR^\infty$ is box-open.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 give the closure in the two topologies.
:::
:::
