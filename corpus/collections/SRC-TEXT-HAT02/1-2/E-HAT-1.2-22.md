---
schema: qual/card@1
id: E-HAT-1.2-22
kind: exercise
title: Wirtinger presentation for fundamental group of knot complement
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Knots
  - Van Kampen
relations: []
review: draft
---

In this exercise we describe an algorithm for computing a presentation of the fundamental group of the complement of a smooth or piecewise linear knot $K$ in $\mathbb{R}^3$, called the Wirtinger presentation.
To begin, we position the knot to lie almost flat on a table, so that $K$ consists of finitely many disjoint arcs $\alpha_i$ where it intersects the table top together with finitely many disjoint arcs $\beta_\ell$ where $K$ crosses over itself.
We build a 2 dimensional complex $X$ that is a deformation retract of $\mathbb{R}^3 - K$ by the following three steps.
First, start with the rectangle $T$ formed by the table top.
Next, just above each arc $\alpha_i$ place a long, thin rectangular strip $R_i$, curved to run parallel to $\alpha_i$ along the full length of $\alpha_i$ and arched so that the two long edges of $R_i$ are identified with points of $T$.
Any arcs $\beta_\ell$ that cross over $\alpha_i$ are positioned to lie in $R_i$.
Finally, over each arc $\beta_\ell$ put a square $S_\ell$, bent downward along its four edges so that these edges are identified with points of three strips $R_i$, $R_j$, and $R_k$; namely, two opposite edges of $S_\ell$ are identified with short edges of $R_j$ and $R_k$ and the other two opposite edges of $S_\ell$ are identified with two arcs crossing the interior of $R_i$.

(a) Assuming this bit of geometry, show that $\pi_1(\mathbb{R}^3 - K)$ has a presentation with one generator $x_i$ for each strip $R_i$ and one relation of the form $x_i x_j x_i^{-1} = x_k$ for each square $S_\ell$, where the indices are as in the figures above.
[To get the correct signs it is helpful to use an orientation of $K$.]

(b) Use this presentation to show that the abelianization of $\pi_1(\mathbb{R}^3 - K)$ is $\mathbb{Z}$.
