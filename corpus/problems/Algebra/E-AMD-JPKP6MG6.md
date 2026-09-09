---
schema: qual/card@1
id: E-AMD-JPKP6MG6
kind: problem
title: Every permutation is a product of disjoint cycles
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the orbit decomposition directly and included the usual uniqueness statement.
---

::: {.exercise}
Show that every permutation in $S_n$ is a product of disjoint cycles.
:::

::: {.solution}
Let $\sigma\in S_n$ act on $\{1,\dots,n\}$. Its orbits partition this finite set.

For an orbit containing $a$, choose the least $m>0$ with $\sigma^m(a)=a$. Then
\[
a,\sigma(a),\dots,\sigma^{m-1}(a)
\]
are distinct and form the entire orbit, and on this orbit $\sigma$ acts as the cycle
\[
(a\ \sigma(a)\ \dots\ \sigma^{m-1}(a)).
\]
Distinct orbits are disjoint, so the corresponding cycles are pairwise disjoint. Their product agrees with $\sigma$ on every point, hence equals $\sigma$.

The decomposition is unique up to reordering the disjoint cycles and inserting or deleting $1$-cycles, because the supports of the nontrivial cycles are precisely the nontrivial orbits of the cyclic group $\langle\sigma\rangle$.
:::
