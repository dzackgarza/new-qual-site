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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the spanning tree and the rank count, the four
    fundamental loops identified as four-cycles, and the conclusion that attaching the $2$-cells kills
    every generator. No retained solution set covers this exercise (the collection retains the problem
    packets, not solutions), so the argument is the card's own; the tree and the four loops were checked
    graph-theoretically for this pass.
---

::: {.problem}
(Wisconsin Aug ’10) The graph $K$ has six vertices $a_1,a_2,a_3,b_1,b_2,b_3$ and nine edges $a_i b_j$ for $i,j=1,2,3$.
The space $X$ obtained from $K$ by attaching a $2$-cell along each loop formed by a cycle of four edges in $K$.
Find $\pi_1(X)$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, and the spanning tree and the four loops below were checked for this pass.

Let $K=K_{3,3}$ have vertices $a_{1},a_{2},a_{3},b_{1},b_{2},b_{3}$ and the nine edges $a_{i}b_{j}$, and let $X$ be obtained from $K$ by attaching a $2$-cell along each loop of $K$ that is a cycle of four edges.

::: pf

::: {.pf-step #tree}
$T=\{a_{1}b_{1},a_{1}b_{2},a_{1}b_{3},a_{2}b_{1},a_{3}b_{1}\}$ is a spanning tree of $K$, and $\pi_{1}(K)$ is free of rank $9-6+1=4$.

::: pf-proof
$T$ has $5$ edges on $6$ vertices and is connected: $a_{2}$ and $a_{3}$ meet $b_{1}$, while $b_{2}$ and $b_{3}$ meet $a_{1}$, and $a_{1}b_{1}$ joins the two groups. A connected graph on $n$ vertices with $n-1$ edges is a tree, so $T$ is a spanning tree. For a connected graph, $\pi_{1}$ is free of rank $E-V+1$, here $9-6+1=4$.
:::

:::

::: {.pf-step #loops}
The four edges of $K$ outside $T$ are $a_{2}b_{2}$, $a_{2}b_{3}$, $a_{3}b_{2}$, $a_{3}b_{3}$, and the fundamental loop of each is the four-edge cycle $a_{i}-b_{j}-a_{1}-b_{1}-a_{i}$.

::: pf-proof
The nine edges minus the five in $T$ leave exactly those four. For the non-tree edge $a_{i}b_{j}$ with $i,j\in\{2,3\}$, the fundamental loop is that edge followed by the path in $T$ from $b_{j}$ back to $a_{i}$: the path is $b_{j}\to a_{1}$ (tree edge $a_{1}b_{j}$), $a_{1}\to b_{1}$ (tree edge $a_{1}b_{1}$), $b_{1}\to a_{i}$ (tree edge $a_{i}b_{1}$). That path has three edges, so the loop has four, namely the cycle displayed. These four fundamental loops form a free basis of $\pi_{1}(K)$.
:::

:::

::: {.pf-step #kill}
Attaching a $2$-cell along a loop kills the class of that loop, and each of the four free generators is the class of one of these loops.

::: pf-proof
If $Y$ is obtained from $Z$ by attaching a $2$-cell along a loop $\gamma$ in $Z$, then $\pi_{1}(Y)\cong\pi_{1}(Z)/\langle\!\langle[\gamma]\rangle\!\rangle$ by van Kampen, the normal closure of the attaching class. Here each of the four four-cycles carries, in particular, one of the basis loops of step [](#loops){.pf-ref} as its own class, so $X$ is obtained from $K$ by attaching cells that kill all four generators of the free group.
:::

:::

::: {.pf-step}
$\pi_{1}(X)$ is trivial.

::: pf-proof
By steps [](#tree){.pf-ref} and [](#loops){.pf-ref} the group $\pi_{1}(K)$ is free on four generators, each the class of a four-edge cycle of $K$; by step [](#kill){.pf-ref} the $2$-cells attached along those cycles impose the relations that those generators are trivial. The quotient of a free group by the normal closure of all of its free generators is trivial, so $\pi_{1}(X)=1$.
:::

:::

:::
:::
