---
schema: qual/card@1
id: P-WESRA04-T3
kind: problem
title: State Lusin's theorem on continuous approximation of measurable functions
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.1, item 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
State a theorem describing how Lebesgue measurable functions on $[0,1]$ can be approximated by continuous functions.
:::

::: {.solution}
One standard answer is Lusin's theorem.
If $f:[0,1]\to\mathbb R$ is Lebesgue measurable and finite almost everywhere, then for every $\varepsilon>0$ there exists a compact set $K\subset[0,1]$ such that
\[
m([0,1]\setminus K)<\varepsilon
\]
and the restriction
\[
f|_K
\]
is continuous.

Equivalently, using the Tietze extension theorem, for every $\varepsilon>0$ there exists $g\in C([0,1])$ such that
\[
\boxed{m\{x\in[0,1]:f(x)\ne g(x)\}<\varepsilon.}
\]
:::
