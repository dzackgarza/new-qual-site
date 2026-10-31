---
schema: qual/card@1
id: E-HAT-1.A-7
kind: problem
title: Nontrivial normal subgroup of infinite index in finitely generated free group is not finitely generated
classification:
  areas:
  - topology
  topics:
  - Free Groups
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-reviewed
  by: claude-opus-5.5
  date: 2026-10-31
  note: The old proof claimed every infinite graph has non-finitely-generated fundamental group, which is false; rewritten with a finite core subgraph and a deck translate of an embedded circle disjoint from it.
---

::: {.problem}
If $F$ is a finitely generated free group and $N$ is a nontrivial normal subgroup of infinite index, show, using covering spaces, that $N$ is not finitely generated.
:::

::: {.solution}
Let $X$ be a finite wedge of circles with $\pi_1(X)=F$, and let $p:\widetilde X\to X$ be the connected covering with $p_*\pi_1(\widetilde X)=N$.
Then $\widetilde X$ is a graph, $\pi_1(\widetilde X)\cong N$, and since $N$ is normal the cover is normal with deck group $F/N$, which is infinite.
The deck group acts freely and transitively on the vertices of $\widetilde X$, all of which lie over the single vertex of $X$.

::: pf

::: {.pf-step #s1}

If $N$ is finitely generated, then there are a finite connected subgraph $Y\subseteq\widetilde X$ and a maximal tree $T\subseteq\widetilde X$ such that every edge of $\widetilde X$ outside $T$ lies in $Y$.

::: pf-proof

Represent a finite generating set of $\pi_1(\widetilde X,\tilde x_0)$ by finitely many edge loops, and let $Y$ be the finite connected subgraph they cover.
Then $\pi_1(Y)\to\pi_1(\widetilde X)$ is surjective.
Choose a maximal tree $T_Y$ of $Y$ and extend it to a maximal tree $T$ of $\widetilde X$; the extension adds no edge of $Y$, because $T_Y$ already contains every vertex of $Y$ and an added edge of $Y$ would close a cycle.
The edges of $Y$ outside $T_Y$ are edges of $\widetilde X$ outside $T$, so the free basis of $\pi_1(Y)$ given by $T_Y$ maps to part of the free basis of $\pi_1(\widetilde X)$ given by $T$.
Surjectivity forces this part to be the whole basis, so every edge outside $T$ lies in $Y$.

:::

:::

::: {.pf-step #s2}

There is an embedded circle $C\subseteq\widetilde X$.

::: pf-proof

$\pi_1(\widetilde X)\cong N$ is nontrivial, so $\widetilde X$ is not a tree, and a connected graph that is not a tree contains a subgraph homeomorphic to a circle.

:::

:::

::: {.pf-step #s3}

If $N$ is finitely generated, some deck transformation $g$ satisfies $gC\cap Y=\varnothing$.

::: pf-proof

The circle $C$ and the subgraph $Y$ have finitely many vertices.
For a vertex $v$ of $C$ and a vertex $w$ of $Y$, at most one deck transformation sends $v$ to $w$, because the action on vertices is free.
So only finitely many deck transformations move $C$ to meet $Y$, while the deck group is infinite.

:::

:::

::: pf-step

Hence $N$ is not finitely generated.

::: pf-proof

Suppose $N$ were finitely generated and take $Y$, $T$ and $g$ from steps [](#s1){.pf-ref} and [](#s3){.pf-ref}.
The circle $gC$ is disjoint from $Y$, so by step [](#s1){.pf-ref} all of its edges lie in $T$.
A tree contains no circle, a contradiction.

:::

:::

:::

:::
