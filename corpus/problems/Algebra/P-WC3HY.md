---
schema: qual/card@1
id: P-WC3HY
kind: problem
title: Group action, orbit, stabilizer, and fixed points
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Orbit-Stabilizer
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
- State definitions of the following:

  - Group action

  - Orbit

  - Stabilizer

  - Fixed points
:::

::: {.solution}
Let $G$ be a group acting on a set $X$.

A **group action** is a map
\[
G\times X\to X,\qquad (g,x)\mapsto g\cdot x,
\]
such that
\[
e\cdot x=x,
\qquad
(gh)\cdot x=g\cdot(h\cdot x).
\]

The **orbit** of $x\in X$ is
\[
Gx=\{g\cdot x:g\in G\}.
\]

The **stabilizer** of $x$ is
\[
G_x=\{g\in G:g\cdot x=x\}.
\]

For $g\in G$, its fixed-point set is
\[
X^g=\{x\in X:g\cdot x=x\}.
\]
The fixed points of the whole action are
\[
X^G=\{x\in X:g\cdot x=x\text{ for every }g\in G\}.
\]
:::
