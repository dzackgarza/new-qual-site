---
schema: qual/card@1
id: E-MD9QR
kind: exercise
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

::: solution
**Theorem.**  
Let $\mathrm{Ord}^2$ be the unit square with the order topology from the lexicographic order.

1. Every point of a linearly ordered topological space has a basis of open intervals.
   Intervals are connected in a linear order.
   Therefore every point has a neighborhood basis of connected sets, so $\mathrm{Ord}^2$ is locally connected.

2. Let $p=(x_0,y_0)$ with $0<y_0<1$.
   Any neighborhood of $p$ contains points with first coordinate both $<x_0$ and $>x_0$ and points with same $x_0$ but varying $y$.
   A path image in an ordered space is connected and therefore has order interval image.
   If a path started at $p$ moved to a nearby point with different first coordinate, it would force an order interval crossing the full jump from $y=1$ to $y=0$ at some $x$, which does not lie in a small convex neighborhood.
   Hence such neighborhoods are not path connected; $\mathrm{Ord}^2$ is not locally path connected.

3. A path in $\mathrm{Ord}^2$ has continuous first coordinate, so it lies in one vertical fiber
   $\{x\}\times[0,1]$ once it is started at any point of that fiber.
4. Conversely, each vertical fiber is the image of $[0,1]$ under $t\mapsto(x,t)$, so each is path connected.
   Thus path components are exactly the vertical fibers $\{x\}\times[0,1]$ for $x\in[0,1]$.

Hence the space is locally connected but not locally path connected, with path components the vertical fibers. ∎
:::
