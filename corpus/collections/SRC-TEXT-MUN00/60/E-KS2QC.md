---
schema: qual/card@1
id: E-KS2QC
kind: problem
title: The projective line and its covering
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
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
    Checked line by line against Munkres, Topology (2000), Section 60 Exercise 4, printed p. 375,
    with Theorem 60.3 and the compact-to-Hausdorff argument of Theorem 26.6. $P^1=S^1/(x\sim-x)$ and $z\mapsto z^2$ factors through a continuous bijection from the compact quotient onto the Hausdorff circle, hence a homeomorphism; the standard covering is exactly $z\mapsto z^2$. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
---

::: {.exercise}

The space $P^1$ and the covering map $p: S^1 \to P^1$ are familiar ones.
What are they?
:::

::: {.solution}
The real projective line $P^1$ is the set of one-dimensional linear subspaces of $\RR^2$. A line through the origin is determined by either of the two antipodal unit vectors lying on it. Hence
$$
P^1=S^1/(x\sim -x).
$$

This quotient is itself homeomorphic to a circle. In complex notation, identify $S^1\subset\CC$. The map
$$
q:S^1\to S^1,\qquad q(z)=z^2,
$$
has exactly the antipodal pairs $\{z,-z\}$ as its fibers, so it factors through a continuous bijection
$$
P^1\longrightarrow S^1.
$$
Since $P^1$ is compact and $S^1$ Hausdorff, this bijection is a homeomorphism.

Under this identification, the standard covering
$$
p:S^1\to P^1,
\qquad p(x)=\RR x,
$$
is exactly the familiar two-sheeted circle covering $z\mapsto z^2$.
:::
