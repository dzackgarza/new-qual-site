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
---

::: {.exercise}

Let $X$ be the quotient space obtained from $B^2$ by identifying each point $x$ of $S^1$ with its antipode $-x$.
Show that $X$ is homeomorphic to the projective plane $P^2$.
:::

::: {.solution}
Recall that the real projective plane is
\[
P^2=S^2/(x\sim -x).
\]
Let
\[
S^2_+=\{(x_1,x_2,x_3)\in S^2:x_3\ge0\}
\]
be the closed upper hemisphere. Projection onto the first two coordinates gives a homeomorphism
\[
\phi:S^2_+\longrightarrow B^2,
\qquad
\phi(x_1,x_2,x_3)=(x_1,x_2),
\]
with inverse
\[
(u,v)\longmapsto (u,v,\sqrt{1-u^2-v^2}).
\]
Every antipodal pair in \(S^2\) has exactly one representative in the open upper hemisphere; pairs lying on the equator have two representatives in \(S^2_+\), and these are antipodal equatorial points. Under \(\phi\), the equator corresponds to \(S^1=\partial B^2\), and the antipodal relation on the equator becomes exactly
\[
x\sim -x\qquad(x\in S^1).
\]
Thus the quotient map \(S^2\to P^2\), restricted to the upper hemisphere, identifies precisely the same boundary pairs as the quotient
\[
B^2/(x\sim -x\text{ on }S^1).
\]
Therefore it induces a continuous bijection
\[
B^2/(x\sim -x)\longrightarrow P^2.
\]
The domain is compact and \(P^2\) is Hausdorff, so this bijection is a homeomorphism. Hence the quotient space in the exercise is \(P^2\).
:::
