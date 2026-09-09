---
schema: qual/card@1
id: E-HAT-1.3-16
kind: problem
title: "Lifting covering spaces through composites"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 16; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used path-connected evenly covered neighborhoods to prove the intermediate map is locally a disjoint union of homeomorphisms, then descended deck transformations of the normal composite cover by uniqueness of lifts.
---

Given maps $X \to Y \to Z$ such that both $Y \to Z$ and the composition $X \to Z$ are covering spaces, show that $X \to Y$ is a covering space if $Z$ is locally path-connected, and show that this covering space is normal if $X \to Z$ is a normal covering space.

::: {.solution}
Write
\[
p:X\to Y,
\qquad
q:Y\to Z,
\qquad
r=q\circ p:X\to Z.
\]

<1>1. For every $z\in Z$ there is a path-connected open neighborhood $U$ of $z$ that is evenly covered by both $q$ and $r$.
::: {.proof}
Choose evenly covered neighborhoods $U_q$ and $U_r$ of $z$ for the two covering maps.
Their intersection is an open neighborhood of $z$.
Since $Z$ is locally path connected, choose a path-connected open neighborhood
\[
z\in U\subseteq U_q\cap U_r.
\]
Restricting an evenly covered neighborhood to a connected open subset preserves the sheet decomposition, so $U$ is evenly covered by both maps.
:::

<1>2. Let $W$ be a sheet of $r^{-1}(U)$.
Then $p(W)$ lies in a single sheet $V$ of $q^{-1}(U)$.
::: {.proof}
The restriction
\[
r|_W:W\to U
\]
is a homeomorphism, and $U$ is path connected, so $W$ is path connected.
The image $p(W)$ is therefore connected.

Since
\[
q(p(W))=r(W)=U,
\]
one has
\[
p(W)\subseteq q^{-1}(U),
\]
which is a disjoint union of open sheets.
A connected subset of this disjoint union lies in one sheet, say $V$.
:::

<1>3. The restriction
\[
p|_W:W\to V
\]
is a homeomorphism.
::: {.proof}
On $W$ one has
\[
q|_V\circ p|_W=r|_W.
\]
Both
\[
q|_V:V\to U
\quad\text{and}\quad
r|_W:W\to U
\]
are homeomorphisms.
Hence
\[
p|_W=(q|_V)^{-1}\circ r|_W,
\]
which is a homeomorphism from $W$ onto $V$.
:::

<1>4. For each sheet $V$ of $q^{-1}(U)$,
\[
p^{-1}(V)
\]
is a disjoint union of sheets $W$ of $r^{-1}(U)$, each mapped homeomorphically onto $V$.
::: {.proof}
Every point of $p^{-1}(V)$ lies in a unique $r$-sheet $W$ over $U$.
By <1>2, the entire connected sheet $W$ maps into one $q$-sheet; since it contains a point mapping into $V$, that sheet must be $V$.
Conversely every $r$-sheet that maps into $V$ lies in $p^{-1}(V)$.
The homeomorphism statement is <1>3.
:::

<1>5. Therefore $p:X\to Y$ is a covering map.
::: {.proof}
The sheets $V$ arising from all path-connected neighborhoods $U$ in <1>1 form an open cover of $Y$.
By <1>4, every such $V$ is evenly covered by $p$.
:::

<1>6. Now assume $r:X\to Z$ is a normal covering.
Let $x_1,x_2\in X$ satisfy
\[
p(x_1)=p(x_2)=y.
\]
Then there is a deck transformation $h$ of $r$ with
\[
h(x_1)=x_2.
\]
::: {.proof}
The two points lie in the same fiber of $r$ because
\[
r(x_i)=q(p(x_i))=q(y).
\]
For a connected normal covering, the deck transformation group acts transitively on each fiber.
:::

<1>7. Every such deck transformation $h$ is a deck transformation of $p$ whenever it sends one point of a $p$-fiber to another point of the same $p$-fiber.
::: {.proof}
The maps
\[
p\circ h,
\qquad
p:X\to Y
\]
are both lifts through $q$ of the same map $r:X\to Z$, since
\[
qph=rh=r=qp.
\]
At $x_1$ they agree:
\[
(ph)(x_1)=p(x_2)=y=p(x_1).
\]
Since $X$ is path connected for a normal covering, uniqueness of lifts gives
\[
p\circ h=p.
\]
Thus $h$ is a deck transformation of $p$.
:::

<1>8. The deck group of $p$ acts transitively on every fiber, so $p$ is normal.
::: {.proof}
For arbitrary $x_1,x_2$ in one $p$-fiber, <1>6 supplies a deck transformation $h$ of $r$ carrying $x_1$ to $x_2$, and <1>7 shows that the same $h$ is a deck transformation of $p$.
This is the transitivity criterion for normal coverings.
:::
:::
