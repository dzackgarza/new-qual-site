---
schema: qual/card@1
id: E-NNTQB
kind: problem
title: 'Lagrange''s theorem: $|G|/|H|=[G:H]$ for finite $G$'
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Reduced Lagrange index formula to the coset partition.
---

::: {.exercise}
Show that if $G$ is finite and $H\le G$, then
\[
[G:H]=\frac{|G|}{|H|}.
\]
:::

::: {.solution}
The left cosets of $H$ partition $G$. For each $g\in G$, multiplication by $g$ gives a bijection
\[
H\longrightarrow gH,\qquad h\mapsto gh,
\]
so every coset has $|H|$ elements. Since there are $[G:H]$ cosets,
\[
|G|=[G:H]\,|H|.
\]
Therefore
\[
[G:H]=\frac{|G|}{|H|}.
\]
:::
