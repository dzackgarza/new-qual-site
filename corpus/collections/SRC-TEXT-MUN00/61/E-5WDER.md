---
schema: qual/card@1
id: E-5WDER
kind: problem
title: Simple closed curves on the torus may or may not separate
classification:
  areas:
  - topology
  topics:
  - Jordan Curve Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Give examples to show that a simple closed curve in the torus may or may not separate the torus.
:::

::: {.solution}
**Goal:** Provide explicit examples of simple closed curves (embedded circles $S^1 \hookrightarrow T^2$) in the torus $T^2 = S^1 \times S^1$ that (1) do not separate $T^2$ and (2) do separate $T^2$.

::: pf

::: pf-step

Example of a non-separating simple closed curve:
    *Proof:*

::: pf-proof

::: pf-step

Identify the torus as $T^2 = S^1 \times S^1$, and fix a point $y_0 \in S^1$.

:::

::: pf-step

Define the curve $C_1 = S^1 \times \{y_0\}$.

:::

::: pf-step

The map $\iota_1: S^1 \to T^2$ given by $\iota_1(\theta) = (\theta, y_0)$ is an embedding, so $C_1$ is a simple closed curve (a longitudinal circle).

:::

::: pf-step

The complement is:
        $$T^2 \setminus C_1 = S^1 \times (S^1 \setminus \{y_0\}).$$

:::

::: pf-step

Since $S^1 \setminus \{y_0\} \cong (0, 1)$ is homeomorphic to an open interval, $T^2 \setminus C_1 \cong S^1 \times (0, 1)$ is homeomorphic to an open cylinder.

:::

::: pf-step

The open cylinder $S^1 \times (0, 1)$ is path-connected (connected).

:::

::: pf-step

Thus $C_1$ does not separate $T^2$.

:::

:::

:::

::: pf-step

Example of a separating simple closed curve:
    *Proof:*

::: pf-proof

::: pf-step

Choose an open coordinate chart $U \subset T^2$ homeomorphic to $\mathbb{R}^2$.

:::

::: pf-step

Inside $U$, let $C_2$ be a small geometric circle of radius $r > 0$ bounding a closed 2-disk $D = \overline{B_r(\mathbf{0})} \subset U$.

:::

::: pf-step

$C_2 = \partial D \subset T^2$ is an embedded simple closed curve (a contractible loop on the torus).

:::

::: pf-step

The complement $T^2 \setminus C_2$ decomposes into two disjoint non-empty open sets:
        $$U_1 = B_r(\mathbf{0}) \quad \text{(the interior open disk)},$$
        $$U_2 = T^2 \setminus D \quad \text{(the exterior punctured torus)}.$$

:::

::: pf-step

Both $U_1$ and $U_2$ are non-empty and open in $T^2 \setminus C_2$, so $T^2 \setminus C_2 = U_1 \cup U_2$ is disconnected.

:::

::: pf-step

Thus $C_2$ separates $T^2$.

:::

:::

:::

::: pf-step

Conclusion:

:::

:::

    $C_1$ is non-separating and $C_2$ is separating on the torus $T^2$. Q.E.D.
:::
