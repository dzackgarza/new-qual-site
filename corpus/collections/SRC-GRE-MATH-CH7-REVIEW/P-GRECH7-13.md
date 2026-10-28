---
schema: qual/card@1
id: P-GRECH7-13
kind: problem
title: Most edges removable from a graph keeping it connected
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 13 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The figure was not recovered by either extraction.
---

::: {.problem}
Given the undirected graph below, what is the maximum number of edges that can be removed that still leaves a connected subgraph?

(A) $3$
(B) $4$
(C) $5$
(D) $6$
(E) $7$
:::

::: {.remark}
The source shows the undirected graph in a figure that is not reproduced here.
:::

::: {.solution}

::: pf

::: pf-step

The source graph has $5$ vertices and $8$ edges.


::: pf-proof

Its vertices are $J,K,L,M,N$. The edges shown are
$$
KJ,\ KL,\ JL,\ JN,\ LN,\ LM,\ MN,
$$
together with one loop at $M$, giving eight edges in total.

:::

:::

::: {.pf-step #s1-2}

Any connected subgraph containing all five vertices must retain at least $4$ edges.


::: pf-proof

Every connected graph on $v$ vertices contains a spanning tree, and every tree on $v$ vertices has $v-1$ edges. With $v=5$, a connected spanning subgraph therefore has at least $4$ edges.

:::

:::

::: {.pf-step #s1-3}

Four edges can in fact be retained while keeping all five vertices connected.


::: pf-proof

Retain the four edges
$$
KJ,\ JN,\ NM,\ ML.
$$
They form the path
$$
K-J-N-M-L,
$$
which contains all five vertices and is connected.

:::

:::

::: {.pf-step #s1-4}

Hence the maximum number of removable edges is
$$
8-4=\boxed{4},
$$
so the answer is (B).


::: pf-proof

Step [](#s1-2){.pf-ref} shows that at most $8-4=4$ edges can be removed, while step [](#s1-3){.pf-ref} exhibits a connected spanning subgraph obtained by retaining only four edges. Thus the bound is attained.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested maximum.

:::

:::

:::
