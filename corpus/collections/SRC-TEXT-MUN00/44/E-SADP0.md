---
schema: qual/card@1
id: E-SADP0
kind: problem
title: Continuous surjections from the interval onto cubes
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Given $n$, show there is a continuous surjective map $g: I \to I^n$.
[Hint: Consider

$$
f \times f: I \times I \to I^2 \times I^2.]
$$
:::

::: {.solution}
Let \(p:I\to I^2\) be the space-filling curve constructed in this section.

We first obtain surjections onto powers whose dimensions are powers of \(2\). Suppose \(q_k:I\to I^{2^k}\) is continuous and surjective. Then
\[
q_k\times q_k:I^2\longrightarrow I^{2^{k+1}}
\]
is continuous and surjective, so
\[
q_{k+1}=(q_k\times q_k)\circ p:I\longrightarrow I^{2^{k+1}}
\]
is continuous and surjective. Starting with \(q_0=\operatorname{id}_I\), induction gives such a map for every \(2^k\).

Given arbitrary \(n\ge1\), choose \(k\) with \(n\le2^k\) and compose \(q_k\) with the projection
\[
I^{2^k}\longrightarrow I^n
\]
onto the first \(n\) coordinates. The resulting map \(I\to I^n\) is continuous and surjective.
:::
