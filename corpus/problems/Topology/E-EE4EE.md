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

::: exercise
- What is an interior point?
  An isolated point?
  A limit point?
:::

::: {.solution}
<1>1. Let $X$ be a topological space and $A \subseteq X$.
::: {.proof}
setup.
:::

<1>2. A point $x \in A$ is an **interior point** of $A$ if there is an open set $U$ with $x \in U \subseteq A$.
::: {.proof}
definition of interior point.
:::

<1>3. A point $x \in A$ is an **isolated point** of $A$ if there is an open set $U$ with $U \cap A = \{x\}$.
::: {.proof}
definition of isolated point.
:::

<1>4. A point $x \in X$ is a **limit point** (accumulation point) of $A$ if every open set $U$ containing $x$ meets $A$ in a point other than $x$, i.e. $(U \setminus \{x\}) \cap A \neq \varnothing$.
::: {.proof}
definition of limit point.
:::

<1>5. Q.E.D.
::: {.proof}
<1>2, <1>3, <1>4.
:::
:::
