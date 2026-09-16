---
schema: qual/card@1
id: P-AGH2317ZARISKISPACE
kind: problem
title: Zariski spaces, closed points, and stability under specialization
classification:
  areas:
  - algebraic-geometry
  topics:
  - Zariski Spaces
  - Noetherian Spaces
  - Generic Points
relations: []
review: draft
---

::: {.problem}
A topological space $X$ is a **Zariski space** if it is noetherian and every nonempty closed irreducible subset has a unique generic point.

For example, let $R$ be a discrete valuation ring and let $T = \operatorname{sp}(\Spec R)$.
Then $T$ consists of two points: $t_0$, the maximal ideal, and $t_1$, the zero ideal.
The open subsets are $\varnothing$, $\ts{t_1}$, and $T$.
This is an irreducible Zariski space with generic point $t_1$.

a. Show that if $X$ is a noetherian scheme then $\operatorname{sp}(X)$ is a Zariski space.

b. Show that any minimal nonempty closed subset of a Zariski space consists of one point.
We call these closed points.

c. Show that a Zariski space $X$ satisfies the axiom $T_0$: given any two distinct points of $X$, there is an open set containing one but not the other.

d. If $X$ is an irreducible Zariski space, then its generic point is contained in every nonempty open subset of $X$.

e. If $x_0 \in \cl\qty{\ts{x_1}}$, we say $x_0$ is a specialization of $x_1$, or that $x_1$ is a generization of $x_0$.
Now let $X$ be a Zariski space.
Show that the minimal points for the partial ordering determined by $x_1 > x_0$ when $x_0$ is a specialization of $x_1$ are the closed points, and the maximal points are the generic points of the irreducible components of $X$.
Show also that a closed subset contains every specialization of any of its points; we say closed subsets are **stable under specialization**. Similarly, open subsets are stable under generization.

f. Let $t$ be the functor on topological spaces introduced in the proof of Hartshorne II.2.6. If $X$ is a noetherian topological space, show that $t(X)$ is a Zariski space.
Furthermore, $X$ itself is a Zariski space if and only if the map $\alpha: X \to t(X)$ is a homeomorphism.
:::
