---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2A-HW4
kind: problem
title: Points joined by a path lie in the same connected component
classification:
  areas:
  - topology
  topics:
  - Connectedness
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
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there. The two ingredients are named as steps: that
    [0,1] is connected, and that a continuous image of a connected set is connected. The passage from the
    image to the component uses the definition of component as the largest connected subset containing the
    point, which is stated. Not checked: the worksheet, which the collection retains as a problem file only;
    the statement is as transcribed on the card. No retained solution set covers the problem, so the
    argument is the card's own. No statement repair.
---

::: {.problem}
Show that if there is a path between two points, they lie in the same connected component.
Why does this show that a path connected space is connected?
:::

::: {.solution}
No retained solution set covers this problem: the collection's provenance is the worksheet alone, so the argument is the card's own. Recall that a connected component of a space $X$ is a maximal connected subset, and that the components partition $X$.

::: pf

::: {.pf-step #interval}
If $\gamma:[0,1]\to X$ is a path with $\gamma(0)=x$ and $\gamma(1)=y$, then $\gamma([0,1])$ is connected and contains both $x$ and $y$.

::: pf-proof
$[0,1]$ is connected. This is the standard connectedness of intervals in $\RR$; here is the argument from the least-upper-bound property. Suppose $[0,1]=U\sqcup V$ with $U,V$ nonempty and both relatively open, and assume $0\in U$. Then $U$ is also relatively closed, its complement $V$ being relatively open. Let $s=\sup U$; since $0\in U$ and $1\notin U$, the set $U$ is nonempty and bounded above by $1$, so $s\in[0,1]$ exists. Because $U$ is relatively open and $s=\sup U$, one has $s\notin U$: a point of $U$ has a relative neighbourhood inside $U$ containing points above it. But every $t<s$ close to $s$ has $t\in U$ by the definition of supremum, so every relative neighbourhood of $s$ meets $U$, making $s$ a limit point of $U$ in $[0,1]$; as $U$ is relatively closed, $s\in U$. The two conclusions contradict each other, so no separation exists. The continuous image of a connected space is connected. And $\gamma([0,1])$ contains $x=\gamma(0)$ and $y=\gamma(1)$.
:::

:::

::: {.pf-step #component}
$x$ and $y$ lie in the same connected component of $X$.

::: pf-proof
Let $C$ be the connected component containing $x$, that is the union of all connected subsets of $X$ that contain $x$; this union is connected because the members share the point $x$, and it is maximal by construction. By step [](#interval){.pf-ref} the set $\gamma([0,1])$ is connected and contains $x$, so it is one of the sets in that union and hence $\gamma([0,1])\subseteq C$. Since $y\in\gamma([0,1])$, $y\in C$; so $x$ and $y$ lie in the same component.
:::

:::

::: {.pf-step #path_connected}
If $X$ is path connected then $X$ is connected.

::: pf-proof
Fix $x_0\in X$. For each $x\in X$ there is a path from $x_0$ to $x$, so by step [](#component){.pf-ref} $x$ lies in the component $C$ containing $x_0$. Hence $X\subseteq C\subseteq X$, that is $C=X$: the whole space is a single connected component. A space with exactly one component is connected, because a separation of $X$ into two disjoint nonempty open pieces would put its two pieces in different components. So $X$ is connected.
:::

:::

:::

:::
