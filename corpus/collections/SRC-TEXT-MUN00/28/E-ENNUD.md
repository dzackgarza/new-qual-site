---
schema: qual/card@1
id: E-ENNUD
kind: problem
title: An infinite set without limit points in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §28 Exercise 1, printed p. 181, with the uniform
    metric of §20 and the definition of limit point compactness printed there.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 28.1, PDF p. 18. The 0-1 sequences form an
    infinite subset of the Hilbert cube with no limit point: coordinates are separated by 1,
    and a point off the set is at positive uniform distance from it. (tmp/sources/munkres-
    solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained positron0802 solution (Chapter 3,
    Exercise 28.1, PDF p. 18). Checked against the book: §28 Exercise 1 as printed
    (p. 181); the uniform metric of §20 (p. 124); the definition of a limit point (§17,
    p. 97). Both witnesses are now computed rather than asserted: the distance from a
    point of Y to a point outside Y is at least min{delta,1} with delta = min{x_i,1-x_i},
    and two distinct points of Y are at uniform distance exactly 1. The subset used is
    Y = {0,1}^omega, infinite because the unit vectors are pairwise at distance 1. No
    repair to the printed statement.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Citation repair found in the same review pass: the uniform metric of §20 is defined on
    printed p. 124 (PDF 139), not p. 122. No change to the mathematics.
---

::: {.exercise}

Give $[0, 1]^\omega$ the uniform topology.
Find an infinite subset of this space that has no limit point.
:::

::: {.solution}
The argument is the retained published solution, **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.1** (`tmp/sources/munkres-solutions-positron-ch3.pdf`), restructured into steps.

Throughout, $[0,1]^\omega$ carries the uniform topology, whose metric is $\bar\rho(\mathbf{x},\mathbf{y})=\sup_i\min\{\abs{x_i-y_i},1\}$ (§20), $Y=\{0,1\}^\omega$ is the set of sequences with every coordinate $0$ or $1$, and a limit point of $Y$ is a point whose every neighbourhood meets $Y$ in a point other than itself (§17).

::: pf

::: {.pf-step #infinite}
$Y$ is an infinite subset of $[0,1]^\omega$.

::: pf-proof
Every sequence of zeros and ones lies in $[0,1]^\omega$. For $n\in\ZZ_+$ let $\mathbf{e}^{(n)}$ have $n$-th coordinate $1$ and all other coordinates $0$; then $\mathbf{e}^{(n)}\in Y$, and $\bar\rho(\mathbf{e}^{(m)},\mathbf{e}^{(n)})=1$ for $m\ne n$, so the $\mathbf{e}^{(n)}$ are pairwise distinct points of $Y$. Hence $Y$ is infinite.
:::

:::

::: {.pf-step #no-limit}
No point of $[0,1]^\omega$ is a limit point of $Y$, so $Y$ is an infinite subset without limit points.

::: pf-proof

::: {.pf-step #outside}
A point $\mathbf{x}\notin Y$ is not a limit point of $Y$.

::: pf-proof
Some coordinate $x_i$ is neither $0$ nor $1$, and since $0\le x_i\le1$ we have $\delta=\min\{x_i,1-x_i\}>0$. A point $\mathbf{y}\in Y$ has $y_i\in\{0,1\}$, so $\abs{x_i-y_i}\ge\delta$ and hence $\bar\rho(\mathbf{x},\mathbf{y})\ge\min\{\delta,1\}=\delta$ because $\delta\le1/2$. Thus $B_{\bar\rho}(\mathbf{x},\delta)\cap Y$ is empty, and $\mathbf{x}$ is not a limit point of $Y$.
:::

:::

::: {.pf-step #inside}
A point $\mathbf{x}\in Y$ is not a limit point of $Y$.

::: pf-proof
Let $0<\varepsilon<1$, so that $B_{\bar\rho}(\mathbf{x},\varepsilon)$ is a neighbourhood of $\mathbf{x}$. If $\mathbf{y}\in Y$ and $\mathbf{y}\ne\mathbf{x}$, some coordinate satisfies $\abs{x_i-y_i}=1$, so $\bar\rho(\mathbf{x},\mathbf{y})=\min\{1,1\}=1\ge\varepsilon$ and $\mathbf{y}\notin B_{\bar\rho}(\mathbf{x},\varepsilon)$. Hence $B_{\bar\rho}(\mathbf{x},\varepsilon)\cap Y=\{\mathbf{x}\}$, a neighbourhood of $\mathbf{x}$ meeting $Y$ only in $\mathbf{x}$ itself, so $\mathbf{x}$ is not a limit point of $Y$. Together with step [](#outside){.pf-ref} this proves that $Y$ has no limit point at all, and $Y$ is infinite by step [](#infinite){.pf-ref}.
:::

:::

:::

:::

:::
:::
