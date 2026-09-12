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

::: exercise
Let $A \subset X$ be a connected subspace.

Show that if $B\subset X$ satisfies $A\subseteq B \subseteq \bar{A}$, then $B$ is connected.
:::

::: {.solution}
<1>1. Suppose $B=U\sqcup V$ were a separation of $B$.
::: {.proof}
We show one side must be empty.
:::

<1>2. Since $A$ is connected and $A\subseteq B$, all of $A$ lies in one side, say $A\subseteq U$.
::: {.proof}
The intersections $A\cap U$ and $A\cap V$ would otherwise separate $A$.
:::

<1>3. No point of $V$ can lie in $\overline A$.
::: {.proof}
Because $V$ is open in $B$, for each $v\in V$ there is an open set $O\subset X$ with $v\in O$ and $O\cap B\subseteq V$. Since $A\subseteq U$, this gives $O\cap A=\varnothing$, so $v\notin\overline A$.
:::

<1>4. But $B\subseteq\overline A$, so $V=\varnothing$, a contradiction. Thus $B$ is connected.
::: {.proof}
Combine the hypothesis with <1>3.
:::
:::
