---
schema: qual/card@1
id: P-6QME4
kind: problem
title: Proper nontrivial normal subgroups of $S_4$ are $A_4$ and $\ZZ_2^2$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
- Show that $S_4$ has two normal subgroups: $A_4, \ZZ_2^2$.
:::

::: solution
The proper nontrivial normal subgroups of $S_4$ are
\[
V_4=\{e,(12)(34),(13)(24),(14)(23)\}
\]
and $A_4$.

Both are normal: $A_4$ is the kernel of the sign map, and $V_4$ is the identity together with the entire conjugacy class of double transpositions.

To see there are no others, use the conjugacy classes of $S_4$, whose sizes are
\[
1,\ 6,\ 3,\ 8,\ 6
\]
for cycle types
\[
1^4,\quad 2\,1^2,\quad 2^2,\quad 3\,1,\quad 4,
\]
respectively. A normal subgroup is a union of conjugacy classes containing the identity, and its order must divide $24$.

The only such class-size sums that can be orders of proper nontrivial subgroups are
\[
1+3=4
\]
and
\[
1+3+8=12.
\]
These give $V_4$ and $A_4$, respectively. All other unions containing the identity have sizes not dividing $24$, except the full union of size $24$.

Hence the normal subgroups of $S_4$ are exactly
\[
\{e\},\quad V_4,\quad A_4,\quad S_4,
\]
so the proper nontrivial ones are precisely $V_4$ and $A_4$.
:::
