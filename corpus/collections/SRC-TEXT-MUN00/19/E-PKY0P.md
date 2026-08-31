---
schema: qual/card@1
id: E-PKY0P
kind: exercise
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
<1>1. In the product topology, $\overline{\RR^\infty} = \RR^\omega$.
<2>1. A basic open set in the product topology is $\prod_i U_i$ where $U_i = \RR$ for all but finitely many $i$.
::: {.proof}
definition of the product topology.
:::
<2>2. Every such basic open set meets $\RR^\infty$.
::: {.proof}
given finitely many non-$\RR$ factors $U_{i_1}, \ldots, U_{i_k}$, choose $x_{i_j} \in U_{i_j}$ and set all other coordinates to $0$; this gives an eventually-zero sequence in the basic open set.
:::
<2>3. Hence $\RR^\infty$ is dense in $\RR^\omega$.
::: {.proof}
<2>2 shows every nonempty basic open set meets $\RR^\infty$.
:::

<1>2. In the box topology, $\overline{\RR^\infty} = \RR^\infty$.
<2>1. For any $x \notin \RR^\infty$ (i.e. $x_i \neq 0$ for infinitely many $i$), there is a box neighborhood of $x$ disjoint from $\RR^\infty$.
::: {.proof}
choose $U_i = \RR \setminus \{0\}$ for the infinitely many indices $i$ with $x_i \neq 0$, and $U_i = \RR$ otherwise; this is a box neighborhood of $x$, and no eventually-zero sequence lies in it (an eventually-zero sequence has $x_i = 0$ for all but finitely many $i$, so it fails to lie in $U_i$ for some $i$ with $x_i \neq 0$).
:::
<2>2. Hence no point outside $\RR^\infty$ is a limit point, so $\RR^\infty$ is closed in the box topology.
::: {.proof}
<2>1.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
