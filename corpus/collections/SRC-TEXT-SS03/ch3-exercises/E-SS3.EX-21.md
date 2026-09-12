---
schema: qual/card@1
id: E-SS3.EX-21
kind: problem
title: "Certain sets have geometric properties that guarantee they are simply connected"
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
21. Certain sets have geometric properties that guarantee they are simply connected.

(a) An open set $\Omega \subset \mathbb { C }$ is convex if for any two points in Ω, the straight line segment between them is contained in Ω. Prove that a convex open set is simply connected.

(b) More generally, an open set $\Omega \subset \mathbb { C }$ is star-shaped if there exists a point $z _ { 0 } \in \Omega$ such that for any $z \in \Omega ,$ the straight line segment between $z_0$ and $z$ is contained in Ω. Prove that a star-shaped open set is simply connected.
Conclude that the slit plane $\mathbb { C } - \{ ( - \infty , 0 ] \}$ (and more generally any sector, convex or not) is simply connected.

(c) What are other examples of open sets that are simply connected?
:::

::: solution
(a) Let $\Omega$ be convex and fix $z_0\in\Omega$. For any closed curve $\gamma:[0,1]\to\Omega$, define
\[
H(s,t)=(1-s)\gamma(t)+sz_0,
\qquad 0\le s,t\le1.
\]
By convexity, $H(s,t)\in\Omega$ for every $(s,t)$. Thus $H$ is a homotopy in $\Omega$ from $\gamma$ to the constant loop at $z_0$. Hence every closed curve is null-homotopic, so $\Omega$ is simply connected.

(b) The same argument works for a star-shaped open set: by definition there is $z_0\in\Omega$ such that every segment from $z_0$ to $z\in\Omega$ lies in $\Omega$. Therefore the same formula
\[
H(s,t)=(1-s)\gamma(t)+sz_0
\]
contracts every loop to $z_0$.

The slit plane
\[
\mathbb C\setminus(-\infty,0]
\]
is star-shaped with respect to any positive real point, for example $1$: if $z$ is not on the nonpositive real axis, then the segment from $1$ to $z$ cannot cross that ray except possibly at its endpoint, which is excluded. Hence it is simply connected. Likewise any sector of opening at most $2\pi$ that does not wrap around the origin is star-shaped with respect to an interior point sufficiently close to its vertex, and hence simply connected.

(c) Other examples include discs, half-planes, strips, convex polygons with interior, and the whole plane. Each is convex (hence star-shaped), so part (a) applies.
:::
