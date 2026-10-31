---
schema: qual/card@1
id: E-HAT-1.2-22
kind: problem
title: Wirtinger presentation for fundamental group of knot complement
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Knots
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-reviewed
  by: claude-opus-5.5
  date: 2026-10-31
  note: Part (a) treated the 2-dimensional strips as a 1-skeleton; rewritten to collapse the table and retract the strips to a wedge of circles before attaching the squares. Part (b) now links consecutive under-arcs along the knot.
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 1.2, Exercise 22.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the complex $X_1=T\cup\bigcup_iR_i$, the cyclic word $x_ix_jx_i^{-1}x_k^{-1}$ on each square, and the abelianization. The two parts now sit in one proof as its top-level steps, with the old run-in labels and the second `pf` block removed, and the closing steps of (b) state their arguments instead of naming earlier steps.
---

::: {.problem}
In this exercise we describe an algorithm for computing a presentation of the fundamental group of the complement of a smooth or piecewise linear knot $K$ in $\RR^3$, called the Wirtinger presentation.
To begin, we position the knot to lie almost flat on a table, so that $K$ consists of finitely many disjoint arcs $\alpha_i$ where it intersects the table top together with finitely many disjoint arcs $\beta_\ell$ where $K$ crosses over itself.
We build a 2 dimensional complex $X$ that is a deformation retract of $\RR^3 - K$ by the following three steps.
First, start with the rectangle $T$ formed by the table top.
Next, just above each arc $\alpha_i$ place a long, thin rectangular strip $R_i$, curved to run parallel to $\alpha_i$ along the full length of $\alpha_i$ and arched so that the two long edges of $R_i$ are identified with points of $T$.
Any arcs $\beta_\ell$ that cross over $\alpha_i$ are positioned to lie in $R_i$.
Finally, over each arc $\beta_\ell$ put a square $S_\ell$, bent downward along its four edges so that these edges are identified with points of three strips $R_i$, $R_j$, and $R_k$; namely, two opposite edges of $S_\ell$ are identified with short edges of $R_j$ and $R_k$ and the other two opposite edges of $S_\ell$ are identified with two arcs crossing the interior of $R_i$.

(a) Assuming this bit of geometry, show that $\pi_1(\RR^3 - K)$ has a presentation with one generator $x_i$ for each strip $R_i$ and one relation of the form $x_i x_j x_i^{-1} = x_k$ for each square $S_\ell$, where the indices are as in the figures above.
[To get the correct signs it is helpful to use an orientation of $K$.]

(b) Use this presentation to show that the abelianization of $\pi_1(\RR^3 - K)$ is $\ZZ$.
:::

::: {.solution}
Write $X$ for the two-dimensional complex of the exercise: $X_1=T\cup\bigcup_iR_i$ is its $1$-skeleton, and one square $S_\ell$ is attached at each crossing $\beta_\ell$.
Fix an orientation of $K$ and orient each circle $x_i$ of $X_1$ so that it passes under $K$ in the direction given by the right-hand rule with respect to that orientation.

::: pf

::: {.pf-step #part-a}
(a) $\pi_1(\RR^3-K)\cong\langle x_1,\ldots,x_m\mid x_ix_jx_i^{-1}=x_k\text{ for each square }S_\ell\rangle$, one generator per strip and one relation per crossing.

::: pf-proof

::: {.pf-step #p1-1}
The subcomplex $X_1=T\cup\bigcup_i R_i$ is homotopy equivalent to a wedge of circles, one circle $x_i$ for each strip, where $x_i$ starts on $T$, crosses $R_i$ once from one long edge to the other, and returns along $T$.

::: pf-proof
The table $T$ is a disk, hence contractible, so collapsing it gives a homotopy equivalence $X_1\to X_1/T$.
Write $R_i=[0,1]\times[0,1]$ with long edges $[0,1]\times\{0\}$ and $[0,1]\times\{1\}$ on $T$.
In $X_1/T$ the strip becomes $[0,1]\times[0,1]$ with both long edges collapsed to the basepoint; this deformation retracts onto the image of a transverse segment $\{1/2\}\times[0,1]$, which is a circle.
The strips meet $T$ only along their long edges, so these retractions combine to a deformation retraction of $X_1/T$ onto a wedge of circles, and the circle for $R_i$ is the image of $x_i$.
:::

:::

::: {.pf-step #p1-2}
In $\pi_1(X_1)$ the four edges of a square $S_\ell$ represent, in cyclic order, $x_i$, $x_j$, $x_i^{-1}$, $x_k^{-1}$, after a choice of paths in $T$ to the basepoint.

::: pf-proof
A short edge of $R_j$ is a transverse segment of $R_j$ with endpoints on $T$, so with a path in $T$ it is homotopic to $x_j^{\pm1}$; the same holds for the short edge of $R_k$.
An arc crossing the interior of $R_i$ from one long edge to the other is likewise homotopic to $x_i^{\pm1}$.
The two edges on $R_i$ are opposite edges of the square, so they are traversed in opposite directions around $\partial S_\ell$, giving $x_i$ and $x_i^{-1}$.
The under-arcs $\alpha_j$ and $\alpha_k$ are consecutive along the oriented knot and pass under $\beta_\ell$ in the same direction, while the boundary of $S_\ell$ crosses their strips in opposite directions; with the orientations fixed above this gives $x_j$ and $x_k^{-1}$, with $j,k$ labelled as in the source figure.
:::

:::

::: {.pf-step #p1-3}
$\pi_1(\RR^3-K)\cong\langle x_1,\ldots,x_m\mid x_ix_jx_i^{-1}=x_k\text{ for each }S_\ell\rangle$.

::: pf-proof
$\RR^3-K$ deformation retracts onto $X$, and $X$ is obtained from $X_1$ by attaching one $2$-cell $S_\ell$ for each crossing.
By step [](#p1-1){.pf-ref}, $\pi_1(X_1)$ is free on the $x_i$.
Attaching a $2$-cell adds its attaching word as a relator, and by step [](#p1-2){.pf-ref} the attaching word of $S_\ell$ is $x_ix_jx_i^{-1}x_k^{-1}$ up to cyclic permutation, which is the relation $x_ix_jx_i^{-1}=x_k$.
:::

:::

:::

:::

::: {.pf-step #part-b}
(b) The abelianization of this group is $\ZZ$.

::: pf-proof

::: {.pf-step #p2-1}
In the abelianization each relation $x_ix_jx_i^{-1}=x_k$ becomes $x_j=x_k$.

::: pf-proof
In an abelian group $x_ix_jx_i^{-1}=x_j$, so the relation of step [](#p1-3){.pf-ref} reads $x_j=x_k$.
:::

:::

::: {.pf-step #p2-2}
The abelianization is generated by $x_1,\ldots,x_m$ subject only to the relations $x_j=x_k$, one for each crossing.

::: pf-proof
Abelianizing the presentation of step [](#p1-3){.pf-ref} keeps the generators and replaces each relator by the one of step [](#p2-1){.pf-ref}, and no other relation is imposed.
:::

:::

::: {.pf-step #p2-3}
Any two generators are joined by a chain of the relations $x_j=x_k$.

::: pf-proof
Follow the oriented knot around once.
It runs through the under-arcs $\alpha_1,\ldots,\alpha_m$ in cyclic order, and between two consecutive under-arcs it passes under one crossing $\beta_\ell$, whose square gives the relation identifying the generators of those two strips.
Starting from any $x_i$ and going around the knot therefore reaches every other generator through a chain of these relations.
:::

:::

::: {.pf-step #p2-4}
The abelianization is infinite cyclic.

::: pf-proof
By step [](#p2-2){.pf-ref} it is generated by the $x_i$ subject to $x_j=x_k$ at each crossing, and by step [](#p2-3){.pf-ref} all generators are equal, so it is generated by one element $x$.
The relations $x_j=x_k$ become trivial after the identification, so no relation is left, and the group is $\langle x\rangle\cong\ZZ$.
:::

:::

:::

:::

:::
:::
