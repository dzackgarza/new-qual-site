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
:::
