---
schema: qual/card@1
id: E-AMD-5LBXBRCH
kind: problem
title: A finite group is solvable iff its composition factors have prime order
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Subgroup Series
  - Classification
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
Show that a finite group $G$ is solvable if and only if all of its composition factors are cyclic groups of prime order.
:::

::: {.solution}
Let \(G\) be finite.

Suppose first that \(G\) is solvable. Every quotient and subgroup of a solvable group is solvable, so every composition factor of \(G\) is a finite simple solvable group. If \(S\) is simple and solvable, then its commutator subgroup \([S,S]\) is a normal subgroup of \(S\). It cannot equal \(S\), since then the derived series would never descend, so \([S,S]=1\). Thus \(S\) is abelian. A finite simple abelian group is cyclic of prime order.

Conversely, suppose every composition factor of \(G\) is cyclic of prime order. A composition series
\[
1=G_0\trianglelefteq G_1\trianglelefteq\cdots\trianglelefteq G_r=G
\]
then has abelian successive quotients \(G_{i+1}/G_i\). Hence it is a subnormal series with abelian factors, so \(G\) is solvable.

Therefore a finite group is solvable exactly when all of its composition factors are cyclic of prime order.
:::
