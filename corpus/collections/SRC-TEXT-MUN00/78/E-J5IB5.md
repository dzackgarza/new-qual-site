---
schema: qual/card@1
id: E-J5IB5
kind: problem
title: Surfaces with k holes
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §78 Exercise 4, printed p. 476. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md. No source was saved. The queries were the Stack Exchange advanced
    search "X-with-k-holes" (15 items) and the similar-question search from "Removing k open discs from a
    surface gives a manifold with boundary with k boundary components" (15 items); the threads they return
    state the result for a surface minus discs and prove none of the three parts, and the GitHub code search
    "munkres "Section 78"" returned no solutions file. The card keeps its own proof, which exhibits the
    half-plane charts on the boundary spheres and shows the boundary to be the disjoint union of k circles.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 78 Exercise 4, printed p. 476. The punctured surface Y with annular collars, the boundary identified intrinsically with the k circles, which are disjoint because the U_i are. Uses the boundary criterion of the preceding card. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Munkres, *Topology* (2000), §78 Exercise 4, printed p. 476, the construction and both conclusions matching the printed text. No retained solution set covers this exercise; the argument is the card's own. Checked: the removed sets $h_i(B_{1/2})$ are open disks with pairwise disjoint closures inside the disjoint open $U_i$; the charts away from the circles and the half-plane charts at them; and that the boundary is exactly the disjoint union of the $k$ circles $C_i$, each homeomorphic to $S^1$.
---

::: {.exercise}

Let $X$ be a 2-manifold; let $U_1, \ldots, U_k$ be a collection of disjoint open sets in $X$; and suppose that for each $i$, there is a homeomorphism $h_i$ of the open unit ball $B^2$ with $U_i$.
Let $\epsilon = 1/2$ and let $B_\epsilon$ be the open ball of radius $\epsilon$.
Show that the space $Y = X - \bigcup h_i(B_\epsilon)$ is a 2-manifold with boundary, and that $\partial Y$ has $k$ components.
The space $Y$ is called "X-with-$k$-holes."
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, checked against Munkres, *Topology* (2000), §78 Exercise 4, printed p. 476.

::: pf

::: {.pf-step #removed}
$D_i\coloneqq h_i(B_{1/2})$ are pairwise disjoint open disks in $X$ and $Y=X-\bigcup_iD_i$ is a closed subspace of $X$.

::: pf-proof
Each $h_i$ is a homeomorphism of the open ball with $U_i$, so $D_i\subset U_i$ is open in $X$ and homeomorphic to $B_{1/2}$; the $U_i$ are pairwise disjoint, hence so are the $D_i$. A finite union of open sets is open, so its complement $Y$ is closed.
:::
:::

::: {.pf-step #separation}
$Y$ is Hausdorff and second countable.

::: pf-proof
$X$ is a 2-manifold, hence Hausdorff and second countable; a subspace of a Hausdorff space is Hausdorff, and a subspace of a second-countable space is second countable.
:::
:::

::: {.pf-step #interior}
Every point of $Y$ off the circles $C_i=h_i(\{z:\norm z=1/2\})$ has a chart to an open subset of the plane.

::: pf-proof
Each such point lies in $X-\bigcup_i\overline{D_i}$ or in the open annulus $h_i(\{1/2<\norm z<1\})$, both open in $X$ and containing no point of $\partial D_i$; the original surface chart of $X$ at the point, restricted to that open set, is a chart of $Y$.
:::
:::

::: {.pf-step #boundary}
Every point of $C_i$ has a chart of $Y$ onto an open subset of the half-plane $H^2$ carrying $C_i$ to the boundary line.

::: pf-proof
On the annulus $h_i(\{1/2\le\norm z<3/4\})$ use polar coordinates about the centre $h_i(0)$: the condition of lying in $Y$ is $r\ge1/2$, which in the coordinates $(r-1/2,\theta)$ is a half-plane condition, and the chart is a homeomorphism onto an open subset of $H^2$ sending $C_i$ to $\{x_2=0\}$.
:::
:::

::: {.pf-step #manifold}
$Y$ is a 2-manifold with boundary.

::: pf-proof
Steps [](#separation){.pf-ref}, [](#interior){.pf-ref} and [](#boundary){.pf-ref} give a Hausdorff second-countable space in which every point has a chart to an open subset of $\RR^2$ or of $H^2$.
:::
:::

::: {.pf-step #components}
$\partial Y=C_1\sqcup\cdots\sqcup C_k$ has exactly $k$ connected components.

::: pf-proof
By step [](#boundary){.pf-ref} the boundary points of $Y$ are exactly the points of the circles $C_i$, and each $C_i$ is the image under the homeomorphism $h_i$ of the circle $\{z:\norm z=1/2\}$, hence is connected and homeomorphic to $S^1$. The $C_i$ lie in the pairwise disjoint $U_i$, so they are pairwise disjoint; hence each $C_i$ is a component of $\partial Y$ and there are $k$ of them.
:::
:::

:::
:::
