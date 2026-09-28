---
schema: qual/card@1
id: P-KCN2B
kind: problem
title: $X$ is Hausdorff iff the diagonal is closed in $X\times X$
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 1 of the official UGA Spring 2021 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Rewrote and verified both implications directly from the Hausdorff condition and the product-topology basis.
---

::: {.problem}
Let $X$ be a topological space and let
$$\Delta = \theset{(x, y) \in X \times X \mid x = y}.$$

Show that $X$ is a Hausdorff space if and only if $\Delta$ is closed in $X \times X$.
:::

::: {.solution}
<1>1. If $X$ is Hausdorff, then $\Delta$ is closed in $X\times X$.

::: {.proof}
Let $(x,y)\notin\Delta$, so $x\neq y$.
Choose disjoint open $U\ni x$ and $V\ni y$.
Then $U\times V$ is an open neighborhood of $(x,y)$, and it misses $\Delta$: if $(z,z)\in U\times V$, then $z\in U\cap V=\varnothing$.
So $(X\times X)\setminus\Delta$ is open.
:::

<1>2. If $\Delta$ is closed in $X\times X$, then $X$ is Hausdorff.

::: {.proof}
Let $x\neq y$.
Then $(x,y)$ lies in the open set $(X\times X)\setminus\Delta$, so there are open $U\ni x$ and $V\ni y$ with $U\times V\subseteq(X\times X)\setminus\Delta$.
If $z\in U\cap V$, then $(z,z)\in(U\times V)\cap\Delta=\varnothing$; so $U\cap V=\varnothing$.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 give the two implications.
:::
:::
