---
schema: qual/card@1
id: E-HAT-1.1-1
kind: problem
title: Cancellation property for composition of paths
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that composition of paths satisfies the following cancellation property: If $f_0 \cdot g_0 \simeq f_1 \cdot g_1$ and $g_0 \simeq g_1$ then $f_0 \simeq f_1$.
:::

::: {.solution}
All path homotopies are relative to endpoints. Write $\bar g$ for the reverse of a path $g$, and $c_x$ for the constant path at $x$.

::: pf

::: pf-step
The two paths $f_0\cdot g_0\cdot\bar g_0$ and $f_1\cdot g_1\cdot\bar g_1$ are homotopic.

::: pf-proof
The homotopy $g_0\simeq g_1$ also gives $\bar g_0\simeq\bar g_1$. Concatenating these homotopies with $f_0\cdot g_0\simeq f_1\cdot g_1$ gives the claim.
:::

:::

::: pf-step
The paths $f_0$ and $f_1$ are homotopic.

::: pf-proof
For each $i$, the path $g_i\cdot\bar g_i$ is homotopic relative to endpoints to $c_{g_i(0)}$. Associativity of concatenation up to path homotopy therefore gives $f_i\cdot g_i\cdot\bar g_i\simeq f_i\cdot c_{g_i(0)}\simeq f_i$. Apply these homotopies to the first step.
:::

:::

:::

:::
