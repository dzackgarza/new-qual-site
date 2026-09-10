---
schema: qual/card@1
id: P-TOP-WORKSHOP-D7-G02
kind: problem
title: A complete bipartite graph with 2-cells attached along four-edge cycles
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Fundamental Group
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(Wisconsin Aug ’10) The graph $K$ has six vertices $a_1,a_2,a_3,b_1,b_2,b_3$ and nine edges $a_i b_j$ for $i,j=1,2,3$.
The space $X$ obtained from $K$ by attaching a $2$-cell along each loop formed by a cycle of four edges in $K$.
Find $\pi_1(X)$.
:::

::: {.solution}
Choose the spanning tree
\[
T=\{a_1b_1,a_1b_2,a_1b_3,a_2b_1,a_3b_1\}
\]
of the graph \(K=K_{3,3}\). Since \(K\) has \(9\) edges and \(6\) vertices, its fundamental group is free of rank
\[
9-6+1=4.
\]
The four edges outside \(T\) are
\[
a_2b_2,\quad a_2b_3,\quad a_3b_2,\quad a_3b_3.
\]
For each non-tree edge \(a_i b_j\) (\(i,j\in\{2,3\}\)), the associated fundamental loop is the four-edge cycle
\[
a_i-b_j-a_1-b_1-a_i.
\]
Thus these four four-cycles form a free basis of \(\pi_1(K)\).

By construction, \(X\) is obtained by attaching a \(2\)-cell along every four-edge cycle, in particular along each of these four basis loops. Attaching a \(2\)-cell quotients the fundamental group by the normal closure of its attaching loop. Hence all four free generators are killed, and
\[
\boxed{\pi_1(X)=1}.
\]
:::
