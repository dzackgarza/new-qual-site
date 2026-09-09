---
schema: qual/card@1
id: E-AMD-UXMX7R25
kind: problem
title: $\QQ$ is not finitely generated as a group
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the common-denominator obstruction directly.
---

::: {.exercise}
Show that $(\mathbb Q,+)$ is not finitely generated as an abelian group.
:::

::: {.solution}
Suppose
\[
\mathbb Q=\langle a_1/b_1,\dots,a_r/b_r\rangle
\]
with $a_i\in\mathbb Z$ and $b_i>0$. Let
\[
M=\operatorname{lcm}(b_1,\dots,b_r).
\]
Every integer linear combination of the proposed generators lies in
\[
\frac1M\mathbb Z.
\]
But
\[
\frac1{2M}\notin\frac1M\mathbb Z,
\]
since $1/(2M)=k/M$ would imply $1=2k$ for some $k\in\mathbb Z$. This contradiction proves that $(\mathbb Q,+)$ is not finitely generated.
:::
