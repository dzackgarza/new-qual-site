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
---

::: {.exercise}

Give $[0, 1]^\omega$ the uniform topology.
Find an infinite subset of this space that has no limit point.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.1, PDF p. 18** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

Let $Y=\{0,1\}^{\omega}\subset[0,1]^{\omega}$, infinite, with the uniform metric $\bar\rho$.

If $\mathbf{x}\notin Y$ then some $x_{i}\notin\{0,1\}$, and with $\delta=\min\{1-x_{i},x_{i}\}>0$ the ball $B_{\bar\rho}(\mathbf{x},\delta)$ meets $Y$ in nothing, since a point of $Y$ has all coordinates in $\{0,1\}$ and differs from $\mathbf{x}$ by at least $\delta$ in the $i$-th coordinate. So $\mathbf{x}$ is not a limit point.

If $\mathbf{x}\in Y$ and $0<\varepsilon<1$, then for any $\mathbf{y}\in Y$ with $\mathbf{y}\ne\mathbf{x}$ some coordinate differs by $1$, so $\bar\rho(\mathbf{x},\mathbf{y})=1\ge\varepsilon$; hence $B_{\bar\rho}(\mathbf{x},\varepsilon)\cap Y=\{\mathbf{x}\}$ and $\mathbf{x}$ is not a limit point of $Y$.

So $Y$ is an infinite subset of $[0,1]^{\omega}$ with no limit point, and $[0,1]^{\omega}$ is not limit point compact in the uniform topology.
:::
