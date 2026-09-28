---
schema: qual/card@1
id: E-MD9QR
kind: problem
title: The ordered square is locally connected but not locally path connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Order Topology
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.exercise}

Show that the ordered square is locally connected but not locally path connected.
What are the path components of this space?
:::

::: {.solution}
Write $I_o^2$ for $[0,1]\times[0,1]$ in the dictionary order topology and $(x,y)$ for $x\times y$. The ordered set $I_o^2$ is a linear continuum: its order is dense and it has the least upper bound property.

<1>1. $I_o^2$ is locally connected.

::: {.proof}
Every point has a neighborhood basis of open intervals, together with the intervals $[(0,0),q)$ and $(q,(1,1)]$ at the endpoints.
These are convex subsets of the linear continuum $I_o^2$, hence connected.
:::

<1>2. Each vertical fiber $\{x\}\times[0,1]$ is path connected.

::: {.proof}
The fiber is the closed interval $[(x,0),(x,1)]$, whose subspace topology is its order topology, and $t\mapsto(x,t)$ is an order isomorphism from $[0,1]$ onto it, hence a homeomorphism.
:::

<1>3. A path in $I_o^2$ lies in a single vertical fiber.

::: {.proof}
Let $\gamma\colon[0,1]\to I_o^2$ be a path from $(x,y)$ to $(x',y')$ with $x<x'$.
Its image is connected, so it contains the interval between its endpoints, and in particular the point $(t,\frac12)$ for every $t\in(x,x')$.
The sets $\{t\}\times(0,1)$ for $x<t<x'$ are uncountably many pairwise disjoint open sets in $I_o^2$, and their preimages under $\gamma$ are pairwise disjoint nonempty open subsets of $[0,1]$.
Each contains a rational number, which is impossible for uncountably many disjoint sets.
:::

<1>4. The path components of $I_o^2$ are the vertical fibers $\boxed{\{x\}\times[0,1]}$, $0\le x\le1$.

::: {.proof}
Steps <1>2 and <1>3.
:::

<1>5. $I_o^2$ is not locally path connected.

::: {.proof}
Let $0<x\le1$.
Every neighborhood of $(x,0)$ contains an interval $((a,b),(x,0)]$ with $a<x$, hence points $(t,\frac12)$ with $a<t<x$.
By step <1>3 such a point is not joined to $(x,0)$ by a path, so no neighborhood of $(x,0)$ is path connected.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1, <1>5, and <1>4.
:::
:::
