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
Comparison means inclusion of these collections. The strict inclusions are generated transitively by
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

To see that no others occur, for each alleged missing inclusion one can exhibit an open set present in the first topology and absent from the second. For example, $\{a\}$ separates $\mathcal T_2$ from $\mathcal T_3$, while $\{b\}$ separates $\mathcal T_3$ from $\mathcal T_2$; similarly $\mathcal T_5$ is incomparable with every $\mathcal T_i$ for $i=2,3,4,6,7,8$ because it contains $\{a\}$ and $\{b,c\}$, whereas each of those topologies omits at least one of these, and conversely each contains a set not in $\mathcal T_5$. Thus the displayed relations give the complete comparison poset.
:::
