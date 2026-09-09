---
schema: qual/card@1
id: E-AMD-2MV56W7X
kind: problem
title: The stabilizer of a point under a group action is a subgroup
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Subgroups
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that the stabilizer of an element $G_x$ is a subgroup of $G$.
:::

::: {.solution}
Let
\[
G_x=\{g\in G:g\cdot x=x\}.
\]
We use the subgroup test.

<1>1. The set \(G_x\) is nonempty.
::: {.proof}
The identity satisfies \(e\cdot x=x\), so \(e\in G_x\).
:::

<1>2. If \(g,h\in G_x\), then \(gh^{-1}\in G_x\).
::: {.proof}
Since \(h\cdot x=x\), applying \(h^{-1}\) gives \(h^{-1}\cdot x=x\). Hence
\[
(gh^{-1})\cdot x=g\cdot(h^{-1}\cdot x)=g\cdot x=x.
\]
Therefore \(gh^{-1}\in G_x\).
:::

By the subgroup criterion, \(G_x\le G\).
:::
