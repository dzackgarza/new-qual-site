---
schema: qual/card@1
id: P-2V6GL
kind: problem
title: Connected versus locally connected spaces
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Find a space that is connected but not locally connected.
  Can there be a space that is locally connected but not connected?
:::

::: {.solution}
**Goal.** Find a connected but not locally connected space, and answer the converse question.

<1>1. A connected but not locally connected space: the topologist's sine curve.
<2>1. $X = \theset{(x, \sin(1/x)) : x > 0} \cup \theset{(0, y) : -1 \le y \le 1}$.
Proof: the topologist's sine curve.
<2>2. $X$ is connected.
Proof: the graph $\theset{(x, \sin(1/x)) : x > 0}$ is connected (continuous image of $(0,\infty)$), and its closure is $X$, so $X$ is connected.
<2>3. $X$ is not locally connected.
Proof: at any point $(0, y)$ on the vertical segment, no small neighborhood is connected (every neighborhood contains infinitely many "oscillations" of the sine curve, which are disconnected from each other).

<1>2. A locally connected but not connected space exists.
<2>1. Example: the disjoint union of two intervals, $X = (0,1) \cup (2,3)$.
Proof: a disjoint union of two open intervals.
<2>2. $X$ is locally connected.
Proof: each point has a connected neighborhood (a small interval around it).
<2>3. $X$ is not connected.
Proof: it is a disjoint union of two nonempty open sets.

<1>3. Q.E.D. Proof: <1>1 gives a connected but not locally connected space; <1>2 gives a locally connected but not connected space (yes, such spaces exist).
:::
