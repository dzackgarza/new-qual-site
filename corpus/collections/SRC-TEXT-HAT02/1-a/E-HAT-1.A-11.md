---
schema: qual/card@1
id: E-HAT-1.A-11
kind: problem
title: Free groups are residually finite
classification:
  areas:
  - topology
  topics:
  - Free Groups
  - Covering Spaces
  - Finite Quotients
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Apply the two preceding problems to show that if $F$ is a finitely generated free group and $x \in F$ is not the identity element, then there is a normal subgroup $H \subset F$ of finite index such that $x \notin H$.
Hence $x$ has nontrivial image in a finite quotient group of $F$.
In this situation one says $F$ is residually finite.
:::

::: {.solution}
Write $F=\langle a_1,\ldots,a_n\rangle$ and represent it as the fundamental group of the rose $X=\bigvee_{i=1}^n S^1$.
Let $x\ne1$ be represented by a reduced word $s_1\cdots s_k$, where each $s_j$ is some $a_i$ or $a_i^{-1}$.

::: pf

::: {.pf-step #s1}

There is a finite connected labeled path $Y$ with distinct vertices $v_0,\ldots,v_k$ whose path from $v_0$ to $v_k$ reads $s_1\cdots s_k$ and whose label map to $X$ is locally injective on oriented edge germs.

::: pf-proof

For $s_j=a_i$, insert an $a_i$-edge oriented from $v_{j-1}$ to $v_j$.
For $s_j=a_i^{-1}$, insert an $a_i$-edge oriented from $v_j$ to $v_{j-1}$.
At an interior vertex, two edges could have the same outgoing $a_i$-label only if consecutive letters were $a_i^{-1}a_i$; they could have the same incoming $a_i$-label only if the letters were $a_i a_i^{-1}$.
Neither occurs in a reduced word.
Thus for each $i$ the $a_i$-edges of $Y$ define a partial bijection between its initial and terminal vertices.

:::

:::

::: {.pf-step #s2}

There is a finite-sheeted covering $p:Z\to X$ containing $Y$, and the lift of the loop $x$ from $v_0$ is not closed.

::: pf-proof

Complete each partial bijection from step [](#s1){.pf-ref} to a permutation of the finite vertex set, as in Exercise 1.A.10. Add the missing labeled edges to obtain a finite covering graph $Z$ with the same vertices as $Y$.
The lift of $x$ follows the original path in $Y$ and ends at $v_k\ne v_0$.
Consequently, if $K=p_*\pi_1(Z,v_0)$, then $x\notin K$ and $[F:K]$ is the finite number of vertices of $Z$.

:::

:::

::: {.pf-step #s3}

There is a finite-index normal subgroup $H\trianglelefteq F$ with $x\notin H$.

::: pf-proof

Apply Exercise 1.A.9 to $K$: its normal core
$$
H=\bigcap_{g\in F}gKg^{-1}
$$
has finite index and lies in $K$.
Since $x\notin K$, also $x\notin H$.
The finite quotient $F/H$ therefore has a nonidentity image of $x$.

:::

:::

:::
:::
