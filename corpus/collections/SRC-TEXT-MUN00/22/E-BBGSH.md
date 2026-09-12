---
schema: qual/card@1
id: E-BBGSH
kind: problem
title: Quotients of the plane by level-set relations
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
  - Homeomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) Define an equivalence relation on the plane $X = \mathbb{R}^2$ as follows:

$$
x_0 \times y_0 \sim x_1 \times y_1 \quad \text{if } x_0 + y_0^2 = x_1 + y_1^2.
$$

Let $X^*$ be the corresponding quotient space.
It is homeomorphic to a familiar space; what is it?
[Hint: Set $g(x \times y) = x + y^2$.]

(b) Repeat (a) for the equivalence relation

$$
x_0 \times y_0 \sim x_1 \times y_1 \quad \text{if } x_0^2 + y_0^2 = x_1^2 + y_1^2.
$$
:::

::: {.solution}
(a) Define
\[
g:\mathbb R^2\to\mathbb R,\qquad g(x,y)=x+y^2.
\]
Its fibers are exactly the equivalence classes. The map
\[
H:\mathbb R^2\to\mathbb R^2,\qquad H(x,y)=(x+y^2,y)
\]
is a homeomorphism with inverse $H^{-1}(u,v)=(u-v^2,v)$, and
\[
g=\pi_1\circ H.
\]
Since the projection $\pi_1$ is an open quotient map, so is $g$. Therefore the induced bijection
\[
\bar g:X^*\to\mathbb R
\]
is a homeomorphism. Thus $X^*\cong\mathbb R$.

(b) Now let
\[
h(x,y)=x^2+y^2.
\]
Its fibers are the circles centered at the origin, with the origin as the radius-zero fiber, so the equivalence classes are exactly its fibers. The norm map
\[
r(x,y)=\sqrt{x^2+y^2}:\mathbb R^2\to[0,\infty)
\]
is open onto $[0,\infty)$: if $B_\varepsilon(z)$ is a small disk about a point of radius $r_0$, its set of radii contains a relative interval about $r_0$. Hence $r$ is quotient. Squaring is a homeomorphism $[0,\infty)\to[0,\infty)$, so $h=r^2$ is quotient. Consequently the induced map identifies the quotient with
\[
[0,\infty).
\]
:::
