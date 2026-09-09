---
schema: qual/card@1
id: P-HGRO45
kind: problem
title: Highly transitive finite permutation groups
classification:
  areas: [algebra]
  topics: [Group Actions, Permutation Groups]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction; the finite sharply k-transitive classification was independently checked against standard permutation-group references.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Which groups admit sharply $k$-transitive actions for large values of $k$?
:::

::: solution
For finite permutation groups, the sharply $k$-transitive groups with $k\ge4$
are the expected symmetric and alternating actions together with two Mathieu
exceptions.

More precisely, if $G\le S_n$ acts sharply $k$-transitively and $k\ge4$, then
one of the following holds:
\[
\begin{array}{c|c}
G & k \\
\hline
S_n & n-1\text{ or }n \\
A_n & n-2 \\
M_{11} & 4\quad(n=11) \\
M_{12} & 5\quad(n=12).
\end{array}
\]

<1>1. The symmetric and alternating examples are sharp in the stated degrees.
::: proof
An element of $S_n$ is uniquely determined by the images of $n-1$ distinct
points, since the last image is forced. Hence the natural action of $S_n$ is
sharply $(n-1)$-transitive, and therefore also sharply $n$-transitive.

The group $A_n$ is $(n-2)$-transitive. Once the images of $n-2$ points are
specified, there are two permutations in $S_n$ extending that partial map, and
exactly one is even. Hence the extension in $A_n$ is unique, so the action is
sharply $(n-2)$-transitive.
:::

<1>2. The exceptional Mathieu actions are sharply $4$- and $5$-transitive.
::: proof
The natural action of $M_{11}$ has degree $11$ and
\[
|M_{11}|=11\cdot10\cdot9\cdot8,
\]
the number of ordered $4$-tuples of distinct points. Since the action is
$4$-transitive, it is therefore sharp.

Likewise the natural action of $M_{12}$ has degree $12$ and
\[
|M_{12}|=12\cdot11\cdot10\cdot9\cdot8,
\]
the number of ordered $5$-tuples of distinct points. Its $5$-transitivity is
therefore sharp.
:::

<1>3. There are no further finite examples for $k\ge4$.
::: proof
This is the classical Jordan classification of sharply multiply transitive
finite permutation groups: outside the symmetric and alternating families, the
only possibilities are $M_{11}$ in degree $11$ with $k=4$ and $M_{12}$ in
degree $12$ with $k=5$.
:::
:::
