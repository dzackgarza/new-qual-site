---
schema: qual/card@1
id: E-LP6WS
kind: exercise
title: The closed topologist's sine curve separates the sphere
classification:
  areas:
  - topology
  topics:
  - Jordan Separation Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Let $A$ be the subset of $\mathbb{R}^2$ consisting of the union of the topologist's sine curve and the broken-line path from $(0, -1)$ to $(0, -2)$ to $(1, -2)$ to $(1, \sin 1)$.
See Figure 61.4. We call $A$ the closed topologist's sine curve.
Show that if $C$ is a subspace of $S^2$ homeomorphic to the closed topologist's sine curve, then $C$ separates $S^2$.
:::

::: {.solution}
<1>1. The closed topologist's sine curve $A$ is a simple closed curve (a Jordan curve) in $\mathbb{R}^2$.
::: {.proof}
$A$ is the union of the topologist's sine curve $\{(x, \sin(1/x)) : 0 < x \le 1\}$ with the broken-line path from $(0,-1)$ to $(0,-2)$ to $(1,-2)$ to $(1, \sin 1)$, together with the limiting segment $\{0\} \times [-1, 1]$; this forms a simple closed curve (a homeomorphic image of $S^1$).
:::

<1>2. By the Jordan curve theorem, a simple closed curve in $S^2$ separates $S^2$ into two components.
::: {.proof}
the Jordan curve theorem.
:::

<1>3. Since $C$ is homeomorphic to $A$ (a simple closed curve), $C$ is itself a simple closed curve in $S^2$.
::: {.proof}
hypothesis and <1>1.
:::

<1>4. Hence $C$ separates $S^2$.
::: {.proof}
<1>2 and <1>3.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
