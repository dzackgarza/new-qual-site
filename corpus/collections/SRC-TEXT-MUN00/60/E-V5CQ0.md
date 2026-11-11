---
schema: qual/card@1
id: E-V5CQ0
kind: problem
title: Antipodal identification on the disk gives the projective plane
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 60 Exercise 2, printed p. 375,
    with Theorem 60.3 and the definition of $P^2$ as $S^2$ modulo antipodes. The upper hemisphere is homeomorphic to $B^2$ by dropping the third coordinate, and every antipodal pair meets it in exactly one point unless the pair lies on the equator, where the two representatives are antipodal boundary points; so both quotients identify the same pairs, and the compact-to-Hausdorff argument makes the induced bijection a homeomorphism. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
---

::: {.exercise}

Let $X$ be the quotient space obtained from $B^2$ by identifying each point $x$ of $S^1$ with its antipode $-x$.
Show that $X$ is homeomorphic to the projective plane $P^2$.
:::

::: {.solution}
Recall that the real projective plane is
$$
P^2=S^2/(x\sim -x).
$$
Let
$$
S^2_+=\{(x_1,x_2,x_3)\in S^2:x_3\ge0\}
$$
be the closed upper hemisphere. Projection onto the first two coordinates gives a homeomorphism
$$
\phi:S^2_+\longrightarrow B^2,
\qquad
\phi(x_1,x_2,x_3)=(x_1,x_2),
$$
with inverse
$$
(u,v)\longmapsto (u,v,\sqrt{1-u^2-v^2}).
$$
Every antipodal pair in $S^2$ has exactly one representative in the open upper hemisphere; pairs lying on the equator have two representatives in $S^2_+$, and these are antipodal equatorial points. Under $\phi$, the equator corresponds to $S^1=\partial B^2$, and the antipodal relation on the equator becomes exactly
$$
x\sim -x\qquad(x\in S^1).
$$
Thus the quotient map $S^2\to P^2$, restricted to the upper hemisphere, identifies precisely the same boundary pairs as the quotient
$$
B^2/(x\sim -x\text{ on }S^1).
$$
Therefore it induces a continuous bijection
$$
B^2/(x\sim -x)\longrightarrow P^2.
$$
The domain is compact and $P^2$ is Hausdorff, so this bijection is a homeomorphism. Hence the quotient space in the exercise is $P^2$.
:::
