---
schema: qual/card@1
id: E-UDJ3C
kind: problem
title: Sets between a connected subspace and its closure are connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Closure
relations: []
review: draft
---

::: {.exercise}
Let $A \subset X$ be a connected subspace.

Show that if $B\subset X$ satisfies $A\subseteq B \subseteq \bar{A}$, then $B$ is connected.
:::

::: {.solution}

Suppose $B=U\sqcup V$, where $U$ and $V$ are disjoint and open in $B$.

::: pf

::: {.pf-step #a-in-u}

After renaming, $A\subseteq U$.

::: pf-proof

Since $A\subseteq B$, the sets $A\cap U$ and $A\cap V$ are disjoint, open in $A$, and cover $A$. As $A$ is connected, one of them is empty.

:::

:::

::: {.pf-step #v-misses-closure}

$V\cap\overline A=\varnothing$.

::: pf-proof

Because $V$ is open in $B$, for each $v\in V$ there is an open set $O\subseteq X$ with $v\in O$ and $O\cap B\subseteq V$. By step [](#a-in-u){.pf-ref}, $O\cap A\subseteq V\cap U=\varnothing$, so $v\notin\overline A$.

:::

:::

::: pf-step

$B$ is connected.

::: pf-proof

Since $V\subseteq B\subseteq\overline A$, step [](#v-misses-closure){.pf-ref} gives $V=\varnothing$. So $B$ admits no separation.

:::

:::

:::

:::
