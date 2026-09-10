---
schema: qual/card@1
id: E-TMOKI
kind: problem
title: The subspace of $\RR^2$ with at least one rational coordinate is connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Euclidean Spaces
  - Subspace Topology
relations: []
review: draft
---

::: exercise
Show that the set $(x, y) \in \RR^2$ such that at least one of $x, y$ is rational with the subspace topology is a connected space.
:::

::: {.solution}
<1>1. Let
$$X=(\mathbb Q\times\mathbb R)\cup(\mathbb R\times\mathbb Q).$$
For each $q\in\mathbb Q$, the horizontal line $H_q=\mathbb R\times\{q\}$ and vertical line $V_q=\{q\}\times\mathbb R$ are connected.
::: {.proof}
Each is homeomorphic to $\mathbb R$.
:::

<1>2. The union
$$Y=V_0\cup\bigcup_{q\in\mathbb Q}H_q$$
is connected.
::: {.proof}
Every $H_q$ meets the connected set $V_0$ at $(0,q)$. A union of connected sets all meeting a fixed connected set is connected.
:::

<1>3. Every vertical line $V_q$ meets $Y$ at $(q,0)$, since $H_0\subseteq Y$.
::: {.proof}
Both coordinates $q,0$ are rational where needed, so the point lies in the indicated sets.
:::

<1>4. Hence
$$X=Y\cup\bigcup_{q\in\mathbb Q}V_q$$
is connected.
::: {.proof}
Again use that adjoining connected sets each meeting an already connected set preserves connectedness.
:::
:::
