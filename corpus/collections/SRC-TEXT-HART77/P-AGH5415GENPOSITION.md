---
schema: qual/card@1
id: P-AGH5415GENPOSITION
kind: problem
title: Points in general position and exceptional curves on blowups of the plane
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Birational Geometry
  - Intersection Theory
relations: []
review: draft
---

::: {.problem}
Let $P_1, \ldots, P_r$ be a finite set of (ordinary) points of $\PP^2$, no 3 collinear.
We define an **admissible transformation** to be a quadratic transformation (4.2.3) centered at some three of the $P_i$ (call them $P_1, P_2, P_3$).

This gives a new $\PP^2$, and a new set of $r$ points, namely $Q_1, Q_2, Q_3$, and the images of $P_4, \ldots, P_r$.

We say that $P_1, \ldots, P_r$ are **in general position** if no three are collinear, and furthermore after any finite sequence of admissible transformations, the new set of $r$ points also has no three collinear.

a. A set of 6 points is in general position if and only if no three are collinear and not all six lie on a conic.

b. If $P_1, \ldots, P_r$ are in general position, then the $r$ points obtained by any finite sequence of admissible transformations are also in general position.

c. Assume the ground field $k$ is uncountable.
Then given $P_1, \ldots, P_r$ in general position, there is a dense subset $V \subseteq \PP^2$ such that for any $P_{r+1} \in V$, $P_1, \ldots, P_{r+1}$ will be in general position.

Hint: Prove a lemma that when $k$ is uncountable, a variety cannot be equal to the union of a countable family of proper closed subsets.

d. Now take $P_1, \ldots, P_r \in \PP^2$ in general position, and let $X$ be the surface obtained by blowing up $P_1, \ldots, P_r$.
If $r=7$, show that $X$ has exactly 56 irreducible nonsingular curves $C$ with $g=0$, $C^2=-1$, and that these are the only irreducible curves with negative self-intersection.
Ditto for $r=8$, the number being 240.

e. For $r=9$, show that the surface $X$ defined in (d) has infinitely many irreducible nonsingular curves $C$ with $g=0$ and $C^2=-1$.

Hint: Let $L$ be the line joining $P_1$ and $P_2$.
Show that there exist finite sequences of admissible transformations such that the strict transform of $L$ becomes a plane curve of arbitrarily high degree.
This example is apparently due to Kodaira -- see Nagata $[5, II, p. 283]$.
:::
