---
schema: qual/card@1
id: E-EE4EE
kind: problem
title: Interior, isolated, and limit points
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
- What is an interior point?
  An isolated point?
  A limit point?
:::

::: {.solution}
Let $X$ be a topological space and $A \subseteq X$.

(a) A point $x \in A$ is an interior point of $A$ if there is an open set $U$ with $x \in U \subseteq A$.

(b) A point $x \in A$ is an isolated point of $A$ if there is an open set $U$ with $U \cap A = \{x\}$.

(c) A point $x \in X$ is a limit point, or accumulation point, of $A$ if every open set $U$ containing $x$ satisfies $(U \setminus \{x\}) \cap A \neq \varnothing$.
:::
