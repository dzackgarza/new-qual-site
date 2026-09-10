---
schema: qual/card@1
id: E-WVVWW
kind: problem
title: Continuous surjections from the line onto euclidean space
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

Show there is a continuous surjective map $f: \mathbb{R} \to \mathbb{R}^n$.
:::

::: {.solution}
By the preceding exercise, every compact cube \([-m,m]^n\) is a continuous image of \(I\). We may choose a continuous surjection
\[
q_m:I\to[-m,m]^n
\]
and modify its parametrization so that it starts and ends at the origin: use the first third of \(I\) for a straight path from \(0\) to \(q_m(0)\), the middle third to traverse \(q_m\), and the last third for a straight path from \(q_m(1)\) back to \(0\). The resulting map, still denoted \(q_m\), is surjective and satisfies
\[
q_m(0)=q_m(1)=0.
\]

Define \(F:[0,\infty)\to\mathbb R^n\) by setting \(F(0)=0\) and, for each integer \(m\ge1\),
\[
F(t)=q_m(t-m+1)\qquad(m-1\le t\le m).
\]
The definitions agree at integer endpoints, so the pasting lemma gives continuity. Since the cubes \([-m,m]^n\) exhaust \(\mathbb R^n\), \(F\) is surjective. Finally define
\[
f(t)=F(|t|),\qquad t\in\mathbb R.
\]
Then \(f:\mathbb R\to\mathbb R^n\) is continuous and surjective.
:::
