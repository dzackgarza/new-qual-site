---
schema: qual/card@1
id: P-AGH446HYPEROSCULATIONPOINTS
kind: problem
title: Counting inflection and hyperosculation points, and the $d^2$ points of order $d$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Genus
  - Elliptic Curves
  - Embeddings
relations: []
review: draft
---

::: {.problem}
a. Let $X$ be a curve of genus $g$ embedded birationally in $\PP^2$ as a curve of degree $d$ with $r$ nodes. Generalize the method of (Ex. 2.3) to show that $X$ has
$$
6(g-1)+ 3d
$$
inflection points. A node does not count as an inflection point. Assume $\characteristic k=0$.

b. Now let $X$ be a curve of genus $g$ embedded as a curve of degree $d$ in $\PP^n$, $n \geq 3$, not contained in any $\PP^{n-1}$. For each point $P \in X$, there is a hyperplane $H$ containing $P$, such that $P$ counts at least $n$ times in the intersection $H \intersect X$. This is called an **osculating** hyperplane at $P$. It generalizes the notion of tangent line for curves in $\PP^2$.

    If $P$ counts at least $n+1$ times in $H \intersect X$, we say $H$ is a **hyperosculating hyperplane**, and that $P$ is a **hyperosculation point**. Use Hurwitz's theorem as above, and induction on $n$, to show that $X$ has
$$
n(n+1)(g-1)+(n+1) d
$$
hyperosculation points.

c. If $X$ is an elliptic curve, for any $d \geq 3$, embed $X$ as a curve of degree $d$ in $\PP^{d-1}$, and conclude that $X$ has exactly $d^2$ points of order $d$ in its group law.
:::
