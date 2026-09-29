---
schema: qual/card@1
id: E-HAT-1.2-7
kind: problem
title: Fundamental group of $S^2$ with north and south poles identified
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
  - CW Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $X$ be the quotient space of $S^2$ obtained by identifying the north and south poles to a single point.
Put a cell complex structure on $X$ and use this to compute $\pi_1(X)$.
:::

::: {.solution}
**Goal.** Compute $\pi_1(X)$ for $X = S^2$ with north and south poles identified.

::: pf

::: pf-step
$X$ is homeomorphic to $S^1 \vee S^2$.

::: pf-proof

::: pf-step
Identifying the two poles of $S^2$ gives a space with a single "pinch" point.

::: pf-proof
the quotient collapses the two poles to one point.
:::

:::

::: {.pf-step #s1-2}
This space is $S^1 \vee S^2$ (a circle wedged with a sphere).

::: pf-proof
the arc from north to south pole becomes a circle (the two poles identified), and the rest of $S^2$ becomes a sphere attached at the pinch point; the result is $S^1 \vee S^2$.
:::

:::

:::

:::

::: pf-step
Cell structure of $S^1 \vee S^2$.

::: pf-proof

::: pf-step
$S^1$ has one $0$-cell and one $1$-cell; $S^2$ has one $0$-cell and one $2$-cell.

::: pf-proof
standard cell structures.
:::

:::

::: pf-step
$S^1 \vee S^2$ has one $0$-cell (the wedge point), one $1$-cell, and one $2$-cell.

::: pf-proof
the two $0$-cells are identified at the wedge point.
:::

:::

:::

:::

::: {.pf-step #s3}
Compute $\pi_1(X)$.

::: pf-proof

::: {.pf-step #s3-1}
$\pi_1(S^1 \vee S^2) = \pi_1(S^1) * \pi_1(S^2) = \ZZ * 0 = \ZZ$.

::: pf-proof
van Kampen (or the fact that $\pi_1$ of a wedge is the free product of the $\pi_1$'s), and $\pi_1(S^2) = 0$.
:::

:::

::: pf-step
Hence $\pi_1(X) = \ZZ$.

::: pf-proof
step [](#s1-2){.pf-ref} and step [](#s3-1){.pf-ref}.
:::

:::

:::

:::

::: pf-qed
$\pi_1(X) = \ZZ$.
:::

:::
:::
