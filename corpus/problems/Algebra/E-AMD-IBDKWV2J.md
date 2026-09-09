---
schema: qual/card@1
id: E-AMD-IBDKWV2J
kind: problem
title: Abelian groups are nilpotent
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Nilpotent Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that every abelian group is nilpotent.
:::

::: {.solution}
If $G$ is abelian, then every commutator is trivial:
\[
[x,y]=xyx^{-1}y^{-1}=1.
\]
Hence
\[
[G,G]=1.
\]
Therefore the lower central series
\[
G\supseteq [G,G]\supseteq\cdots
\]
reaches the trivial subgroup after one step. Thus every abelian group is nilpotent, of nilpotency class at most $1$.
:::
