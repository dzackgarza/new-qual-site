---
schema: qual/card@1
id: E-V7QV9
kind: problem
title: Comparing the nine topologies on a three-point set
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
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

Consider the nine topologies on the set $X = \ts{a, b, c}$ indicated in Example 1 of §12. Compare them; that is, for each pair of topologies, determine whether they are comparable, and if so, which is the finer.
:::

::: {.solution}
Write the nine topologies from §12 Example 1 as
\[
\begin{aligned}
\mathcal T_1&=\{\varnothing,X\},\\
\mathcal T_2&=\{\varnothing,\{a\},\{a,b\},X\},\\
\mathcal T_3&=\{\varnothing,\{b\},\{a,b\},\{b,c\},X\},\\
\mathcal T_4&=\{\varnothing,\{b\},X\},\\
\mathcal T_5&=\{\varnothing,\{a\},\{b,c\},X\},\\
\mathcal T_6&=\{\varnothing,\{b\},\{c\},\{a,b\},\{b,c\},X\},\\
\mathcal T_7&=\{\varnothing,\{a,b\},X\},\\
\mathcal T_8&=\{\varnothing,\{a\},\{b\},\{a,b\},X\},\\
\mathcal T_9&=\mathcal P(X).
\end{aligned}
\]
Write $\mathcal T<\mathcal T'$ when $\mathcal T\subsetneq\mathcal T'$, that is, when $\mathcal T'$ is strictly finer than $\mathcal T$. The strict inclusions are generated transitively by
\[
\mathcal T_1<\mathcal T_4<\mathcal T_3<\mathcal T_6<\mathcal T_9,
\]
\[
\mathcal T_1<\mathcal T_4<\mathcal T_8<\mathcal T_9,
\]
\[
\mathcal T_1<\mathcal T_7<\mathcal T_2<\mathcal T_8<\mathcal T_9,
\]
and
\[
\mathcal T_1<\mathcal T_5<\mathcal T_9.
\]
In addition, $\mathcal T_7<\mathcal T_3$ and hence $\mathcal T_7<\mathcal T_6$. These inclusions and their transitive consequences are all the comparable pairs.

Every other pair is incomparable. For each such pair $(\mathcal T,\mathcal T')$, the table gives a set in $\mathcal T$ but not in $\mathcal T'$, and a set in $\mathcal T'$ but not in $\mathcal T$:

| Pair | In the first only | In the second only |
| --- | --- | --- |
| $\mathcal T_2,\mathcal T_3$ | $\{a\}$ | $\{b\}$ |
| $\mathcal T_2,\mathcal T_4$ | $\{a\}$ | $\{b\}$ |
| $\mathcal T_2,\mathcal T_6$ | $\{a\}$ | $\{b\}$ |
| $\mathcal T_3,\mathcal T_8$ | $\{b,c\}$ | $\{a\}$ |
| $\mathcal T_4,\mathcal T_7$ | $\{b\}$ | $\{a,b\}$ |
| $\mathcal T_6,\mathcal T_8$ | $\{c\}$ | $\{a\}$ |
| $\mathcal T_5,\mathcal T_2$ | $\{b,c\}$ | $\{a,b\}$ |
| $\mathcal T_5,\mathcal T_3$ | $\{a\}$ | $\{b\}$ |
| $\mathcal T_5,\mathcal T_4$ | $\{a\}$ | $\{b\}$ |
| $\mathcal T_5,\mathcal T_6$ | $\{a\}$ | $\{b\}$ |
| $\mathcal T_5,\mathcal T_7$ | $\{a\}$ | $\{a,b\}$ |
| $\mathcal T_5,\mathcal T_8$ | $\{b,c\}$ | $\{b\}$ |
:::
