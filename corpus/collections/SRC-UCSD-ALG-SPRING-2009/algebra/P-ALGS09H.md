---
schema: qual/card@1
id: P-ALGS09H
kind: problem
title: "Radical of the ideal (x^2 - y^3, x - y^2) in C[x,y]"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 8 of the official UCSD Spring 2009 algebra qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Replaced the unsupported nonradicality assertion with the quotient-ring identification C[x,y]/I ≅ C[y]/(y^3(y-1)) and an explicit nilpotent class.
---

::: problem
(a) Consider the ideal $I = (x^2 - y^3,\; x - y^2) \subseteq \mathbb{C}[x, y]$.
Find $\operatorname{rad} I$, the radical of $I$, expressing it as an intersection of prime ideals (do not try to find a generating set for $\operatorname{rad} I$).

(b) Is $I$ a radical ideal?
:::

::: {.solution}
Let
\[
I=(x^2-y^3,\ x-y^2)\subseteq\mathbb C[x,y].
\]

<1>1. There is an isomorphism
\[
\mathbb C[x,y]/I\cong \mathbb C[y]/(y^3(y-1)).
\]
::: {.proof}
First quotient by the relation $x-y^2$.
The substitution homomorphism
\[
\mathbb C[x,y]\longrightarrow\mathbb C[y],
\qquad
x\longmapsto y^2,
\qquad
y\longmapsto y
\]
has kernel $(x-y^2)$, so
\[
\mathbb C[x,y]/(x-y^2)\cong\mathbb C[y].
\]
Under this isomorphism the other generator becomes
\[
x^2-y^3\longmapsto y^4-y^3=y^3(y-1).
\]
The claimed quotient follows.
:::

<1>2. The affine variety of $I$ is
\[
V(I)=\{(0,0),(1,1)\}.
\]
::: {.proof}
Every point of $V(I)$ satisfies
\[
x=y^2.
\]
Substituting into $x^2-y^3=0$ gives
\[
y^4-y^3=y^3(y-1)=0.
\]
Hence $y=0$ or $y=1$, and then $x=y^2$ gives respectively $x=0$ or $x=1$.
Both points satisfy the two generators of $I$.
:::

<1>3. The radical of $I$ is
\[
\sqrt I=(x,y)\cap(x-1,y-1).
\]
::: {.proof}
By Hilbert's Nullstellensatz over the algebraically closed field $\mathbb C$,
\[
\sqrt I=I(V(I)).
\]
By <1>2,
\[
I(V(I))
=I(\{(0,0)\})\cap I(\{(1,1)\})
=(x,y)\cap(x-1,y-1).
\]
Each factor is maximal, hence prime, as requested.
:::

<1>4. The ideal $I$ is not radical.
::: {.proof}
Set
\[
h=y(y-1).
\]
Under the quotient description of <1>1, membership in $I$ is equivalent to divisibility by $y^3(y-1)$ in $\mathbb C[y]$.
The polynomial
\[
y(y-1)
\]
is not divisible by $y^3(y-1)$, so $h\notin I$.
However
\[
h^3=y^3(y-1)^3
\]
is divisible by $y^3(y-1)$, hence $h^3\in I$.
Therefore
\[
h\in\sqrt I\setminus I,
\]
so $I\ne\sqrt I$ and $I$ is not radical.
:::
:::
