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
Show that $(\QQ,+)$ is not finitely generated as an abelian group.
:::

::: {.solution}
Suppose
$$
\QQ=\langle a_1/b_1,\ldots,a_r/b_r\rangle
$$
with $a_i\in\ZZ$ and positive integers $b_i$. Let
$$
M=\lcm(b_1,\ldots,b_r).
$$
Every integer linear combination of the proposed generators lies in
$$
\frac1M\ZZ.
$$
But
$$
\frac1{2M}\notin\frac1M\ZZ,
$$
since $1/(2M)=k/M$ would imply $1=2k$ for some $k\in\ZZ$. This contradiction proves that $(\QQ,+)$ is not finitely generated.
:::
