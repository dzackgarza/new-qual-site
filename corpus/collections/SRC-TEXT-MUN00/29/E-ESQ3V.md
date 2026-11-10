---
schema: qual/card@1
id: E-ESQ3V
kind: problem
title: The Hilbert cube is not locally compact in the uniform topology
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
    Read against Munkres, Topology (2000), §29 Exercise 4, printed p. 186, with Exercise
    28.1 and Theorem 26.2; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.4, PDF p. 22. A uniform ball at the origin is a
    closed box of sequences, compact if the Hilbert cube were locally compact there, but
    homeomorphic to the cube, which has an infinite set without limit points.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that $[0, 1]^\omega$ is not locally compact in the uniform topology.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.4, PDF p. 22** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

Suppose $[0,1]^{\omega}$ in the uniform topology were locally compact at $\mathbf{0}$; then some compact $C$ would contain a ball $B=B_{\bar\rho}(\mathbf{0},\varepsilon)$. Now $B=[0,\varepsilon]^{\omega}$: the uniform distance from $\mathbf{0}$ is the supremum of the coordinates, so the ball consists of all sequences with every coordinate $<\varepsilon$, and its closure is the box $[0,\varepsilon]^{\omega}$. That closed set is contained in $C$, hence compact; but it is homeomorphic to $[0,1]^{\omega}$ (scale each coordinate), which by Exercise 28.1 has an infinite subset with no limit point, so it is not compact. Contradiction.
:::
