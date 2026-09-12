---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS4A-HW1
kind: problem
title: A Δ-complex structure and chain complex for the standard 2-simplex
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Give a $\Delta$-complex structure for a standard 2-simplex $\Delta$ and write down its chain complex.
Explicitly describe the boundary homomorphisms.
:::

::: {.solution}
Let the vertices of the standard \(2\)-simplex be \(v_0,v_1,v_2\), orient the edges by increasing indices, and let
\[
e_{01}=[v_0,v_1],\quad e_{02}=[v_0,v_2],\quad e_{12}=[v_1,v_2],
\]
with oriented \(2\)-simplex \(\sigma=[v_0,v_1,v_2]\). This is the standard \(\Delta\)-complex structure.

The chain complex is
\[
0\to\mathbb Z\langle\sigma\rangle
\xrightarrow{\partial_2}
\mathbb Z\langle e_{01},e_{02},e_{12}\rangle
\xrightarrow{\partial_1}
\mathbb Z\langle v_0,v_1,v_2\rangle
\to0,
\]
where
\[
\partial_2\sigma=e_{12}-e_{02}+e_{01}
\]
and
\[
\partial_1e_{01}=v_1-v_0,
\qquad
\partial_1e_{02}=v_2-v_0,
\qquad
\partial_1e_{12}=v_2-v_1.
\]
These satisfy \(\partial_1\partial_2=0\), as required.
:::
