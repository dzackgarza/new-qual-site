---
schema: qual/card@1
id: E-YI3QM
kind: problem
title: The closed disk as a surface with boundary
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
    Munkres §78 Exercise 3, printed p. 476. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved thread is tmp/sources/mse-1522925-E-YI3QM.md, read whole.
    Math Stack Exchange 1522925 has two answers. 1522970 by levap (2015-11-10) proves the exercise in general
    dimension: the closed disk has an R^2-chart at every interior point and, "using polar coordinates", a
    half-space chart at every point of the circle, and it records that the disjointness of interior and
    boundary points is the non-trivial input, which is Exercise 2(a). That answer states the construction in
    one sentence and writes no chart; the explicit chart (theta, 1-r) is the card's, and it is now stated in
    the solution that the answer supplies the construction and the card supplies the formula. 1522959 by
    Luis Vera asserts that no neighbourhood of a point of S^1 is homeomorphic to an open set of R^2 without
    proof. Rejected in the search: mse 5039847, which has no answer.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 78 Exercise 3, printed p. 476. Charts inside the disc and the explicit half-plane chart (theta, 1 - r) at a boundary point. Checked against the definition of a 2-manifold with boundary printed in the same exercise. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

Show that the closed unit ball in $\RR^2$ is a 2-manifold with boundary.
:::

::: {.solution}
Let
$$
D^2=\{(x,y)\in\RR^2:x^2+y^2\le1\}.
$$
It is Hausdorff and second countable as a subspace of $\RR^2$.

If $p\in D^2$ satisfies $\norm{p}<1$, choose $\varepsilon>0$ with $B(p,\varepsilon)\subset D^2$. This is an open neighborhood of $p$ in $D^2$ homeomorphic to an open subset of $\RR^2$.

Now let $p\in\partial D^2=S^1$. After a rotation we may assume $p=(1,0)$. For sufficiently small $\varepsilon$, the neighborhood $D^2\cap B(p,\varepsilon)$ is carried homeomorphically to an open subset of the closed half-plane
$$
H^2=\{(u,v):v\ge0\}.
$$
One explicit chart is obtained by polar coordinates near $p$: write a nearby point uniquely as
$$
(r\cos\theta,r\sin\theta),
$$
with $r\le1$ and $\abs{\theta}<\delta$, and send it to
$$
(\theta,1-r).
$$
For sufficiently small $\delta$ this is a homeomorphism onto an open subset of $H^2$, with $p\mapsto(0,0)$.

Thus every point has a neighborhood modeled on $\RR^2$ or $H^2$, so $D^2$ is a 2-manifold with boundary. Its boundary in this sense is the usual circle $S^1$.

The same example is worked through, in general dimension, by levap's answer 1522970 (https://math.stackexchange.com/a/1522970), posted 2015-11-10 to Math Stack Exchange question 1522925, "Topological Boundary vs Manifold Boundary" (https://math.stackexchange.com/questions/1522925, asked by the account posting as user153582 on the same day): for the closed unit disk $B$ in $\RR^2$, "using polar coordinates, you can easily construct a homeomorphism from an open neighborhood of each point $x\in B$ with $\norm{x}=1$ to an open neighborhood of $H^2$ mapping $x$ to $\partial H^2$", while a point of $\norm{x}<1$ has the open ball as an $\RR^2$-chart; hence the manifold boundary is the circle. That answer states the construction and gives no chart, the chart $(\theta,1-r)$ above being the card's; it also records, as its second answer 1522959 by Luis Vera does not, that the disjointness of the two kinds of point is the non-trivial part, which is Exercise 2(a) and (b) of this section.
:::
