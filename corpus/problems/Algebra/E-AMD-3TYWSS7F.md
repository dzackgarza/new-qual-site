---
schema: qual/card@1
id: E-AMD-3TYWSS7F
kind: problem
title: Nilpotent groups are solvable
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Solvable Groups
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
Show that $G$ nilpotent $\implies G$ solvable.
:::

::: {.solution}
Let \(G\) be nilpotent. Then \(G\) has a finite central series
\[
1=Z_0\trianglelefteq Z_1\trianglelefteq\cdots\trianglelefteq Z_c=G
\]
with
\[
Z_{i+1}/Z_i\le Z(G/Z_i)
\]
for every \(i\).

Each quotient \(Z_{i+1}/Z_i\) is therefore abelian. Hence this central series is, in particular, a finite subnormal series with abelian successive quotients. By the standard criterion for solvability, \(G\) is solvable.
:::
