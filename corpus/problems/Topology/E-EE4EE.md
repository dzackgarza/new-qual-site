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

::: pf

::: pf-step

Let $X$ be a topological space and $A \subseteq X$.

::: pf-proof

setup.

:::

:::

::: {.pf-step #s2}

A point $x \in A$ is an **interior point** of $A$ if there is an open set $U$ with $x \in U \subseteq A$.

::: pf-proof

definition of interior point.

:::

:::

::: {.pf-step #s3}

A point $x \in A$ is an **isolated point** of $A$ if there is an open set $U$ with $U \cap A = \{x\}$.

::: pf-proof

definition of isolated point.

:::

:::

::: {.pf-step #s4}

A point $x \in X$ is a **limit point** (accumulation point) of $A$ if every open set $U$ containing $x$ meets $A$ in a point other than $x$, i.e. $(U \setminus \{x\}) \cap A \neq \varnothing$.

::: pf-proof

definition of limit point.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::
