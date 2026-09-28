---
schema: qual/card@1
id: P-CQR3X
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
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $G$ be a finite group.
Prove that $G$ is solvable if and only if all of its composition factors are of prime order (i.e. cyclic groups $\mathbb{Z}_p$).
:::

::: {.solution}
Suppose first that \(G\) is finite and solvable. Every subgroup and quotient of a solvable group is solvable, so every composition factor of \(G\) is both simple and solvable. If \(S\) is simple and solvable, then \([S,S]\trianglelefteq S\) and solvability forces \([S,S]\ne S\); hence \([S,S]=1\), so \(S\) is abelian. A finite simple abelian group is cyclic of prime order. Thus every composition factor of \(G\) is \(C_p\) for some prime \(p\).

Conversely, if a composition series
\[
1=G_0\triangleleft G_1\triangleleft\cdots\triangleleft G_r=G
\]
has factors \(G_{i+1}/G_i\) of prime order, then every factor is cyclic and hence abelian. Therefore this is a subnormal series with abelian factors, so \(G\) is solvable.

Thus a finite group is solvable if and only if all of its composition factors have prime order.
:::
