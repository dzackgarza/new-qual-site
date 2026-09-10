---
schema: qual/card@1
id: E-K89XO
kind: problem
title: Projections from a product are open maps
classification:
  areas:
  - topology
  topics:
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

A map $f: X \to Y$ is said to be an open map if for every open set $U$ of $X$, the set $f(U)$ is open in $Y$.
Show that $\pi_1: X \times Y \to X$ and $\pi_2: X \times Y \to Y$ are open maps.
:::

::: {.solution}
Let $U\subseteq X\times Y$ be open. For every $(x,y)\in U$ there is a basic product $V_{x,y}\times W_{x,y}$ with
\[
(x,y)\in V_{x,y}\times W_{x,y}\subseteq U.
\]
Then
\[
\pi_1(U)=\bigcup_{(x,y)\in U}V_{x,y},
\]
which is open in $X$. Thus $\pi_1$ is open. The same argument, interchanging the factors, gives
\[
\pi_2(U)=\bigcup_{(x,y)\in U}W_{x,y},
\]
so $\pi_2$ is open as well.
:::
