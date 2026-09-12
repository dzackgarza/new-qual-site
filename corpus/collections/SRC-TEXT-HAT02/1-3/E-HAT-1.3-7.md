---
schema: qual/card@1
id: E-HAT-1.3-7
kind: problem
title: "Local path-connectedness is necessary for the lifting criterion"
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
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 7 and the quasi-circle figure; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the two path components of the topologist sine curve to confine each loop to a contractible finite truncation, then ruled out a lift by factoring it through the quotient and obtaining an impossible section of R to S1.
---

Let $Y$ be the quasi-circle, a closed subspace of $\mathbb{R}^2$ consisting of a portion of the graph of $y = \sin(1/x)$, the segment $[-1, 1]$ in the $y$-axis, and an arc connecting these two pieces.
Collapsing the segment of $Y$ in the $y$-axis to a point gives a quotient map $f: Y \to S^1$.
Show that $f$ does not lift to the covering space $\mathbb{R} \to S^1$, even though $\pi_1(Y) = 0$.
Thus local path-connectedness of $Y$ is a necessary hypothesis in the lifting criterion.

::: {.solution}
Let
\[
L=\{0\}\times[-1,1]
\]
be the vertical segment and let $G$ be the oscillating graph portion of $y=\sin(1/x)$ used in the quasi-circle.
Before the extra connecting arc is added, $L$ and $G$ are the two path components of the topologist sine curve.

<1>1. The image of every path in $Y$ meets only a finite truncation of the oscillating graph $G$ near the $y$-axis.
::: {.proof}
Let
\[
\alpha:I\to Y
\]
be a path.
The only way for a path to pass between $L$ and $G$ is through the added connecting arc, since $L$ and $G$ are distinct path components of the topologist sine curve itself.

Let $b\in G$ be the endpoint of the added arc on the graph, and write its positive $x$-coordinate as $x_b$.
On $G$, projection to the $x$-coordinate is a homeomorphism onto an interval $(0,x_b]$.

Consider the components of the set of parameter values for which $\alpha$ lies in $G\setminus\{b\}$.
Except possibly for the two components meeting the endpoints of $I$, each such component is an open interval whose two endpoint values under $\alpha$ are $b$: leaving the graph can occur only through the attachment point $b$.

The path $\alpha$ is uniformly continuous.
Choose $\delta>0$ such that
\[
|s-t|<\delta
\quad\Longrightarrow\quad
\|\alpha(s)-\alpha(t)\|<x_b/2.
\]
Any graph excursion that reaches a point with $x<x_b/2$ has Euclidean distance at least $x_b/2$ from $b$ in the horizontal coordinate alone.
Hence its parameter interval has length at least $\delta$.
There can be only finitely many pairwise disjoint excursion intervals of length at least $\delta$.

On each of these finitely many intervals, the continuous positive $x$-coordinate attains a positive minimum on the closed interval obtained by adding its endpoints.
The same is true for the at most two components meeting $0$ or $1$.
All remaining excursions stay in $x\ge x_b/2$.
Taking the minimum of these finitely many positive lower bounds and $x_b/2$ gives some $\varepsilon>0$ such that every point of $\alpha(I)\cap G$ has
\[
x\ge\varepsilon.
\]
:::

<1>2. Every loop in $Y$ is contained in a contractible subspace of $Y$.
::: {.proof}
Let $\gamma:S^1\to Y$ be a loop.
By <1>1, choose $\varepsilon>0$ so that the part of its image in $G$ lies in the compact graph segment
\[
G_\varepsilon=G\cap\{x\ge\varepsilon\}.
\]

The union of

- the vertical interval $L$,
- the added connecting arc,
- the finite graph segment from the arc endpoint down to $G_\varepsilon$,

is a finite tree: these three arc pieces are attached without forming a cycle.
It contains the whole image of $\gamma$ and is contractible.
Therefore $\gamma$ is nullhomotopic in $Y$.
:::

<1>3. Consequently
\[
\boxed{\pi_1(Y)=0.}
\]
::: {.proof}
Every loop is nullhomotopic by <1>2.
:::

<1>4. Let
\[
p:\mathbb R\to S^1,
\qquad
p(t)=e^{2\pi i t},
\]
be the standard covering.
Suppose for contradiction that the quotient map
\[
f:Y\to S^1
\]
has a lift
\[
\widetilde f:Y\to\mathbb R
\]
with
\[
p\widetilde f=f.
\]
::: {.proof}
This is the negation of the desired nonlifting statement.
:::

<1>5. The map $\widetilde f$ is constant on the collapsed segment $L$.
::: {.proof}
The quotient map $f$ sends all of $L$ to one point $z_0\in S^1$.
Therefore
\[
\widetilde f(L)\subseteq p^{-1}(z_0).
\]
The fiber $p^{-1}(z_0)$ is a discrete subset of $\mathbb R$, while $L$ is connected.
The continuous image of a connected space in a discrete space is a single point.
Hence $\widetilde f|_L$ is constant.
:::

<1>6. The lift $\widetilde f$ factors through the quotient $f:Y\to S^1$:
there is a continuous map
\[
s:S^1\to\mathbb R
\]
such that
\[
\widetilde f=s\circ f.
\]
::: {.proof}
The map $f$ is precisely the quotient obtained by collapsing $L$ to one point, and it is one-to-one on the remaining quotient classes.
By <1>5, $\widetilde f$ is constant on every fiber of this quotient map.
The universal property of quotient maps therefore gives a unique continuous factor $s$ with
\[
\widetilde f=s f.
\]
:::

<1>7. The map $s$ would be a section of $p$:
\[
p\circ s=\operatorname{id}_{S^1}.
\]
::: {.proof}
Using <1>4 and <1>6,
\[
f=p\widetilde f=p s f.
\]
Since $f:Y\to S^1$ is surjective, equality after composition with $f$ implies
\[
p s=\operatorname{id}_{S^1}.
\]
:::

<1>8. No such section $s$ exists.
::: {.proof}
On fundamental groups, the identity
\[
p s=\operatorname{id}_{S^1}
\]
would give
\[
p_*s_*=\operatorname{id}_{\pi_1(S^1)}.
\]
But
\[
\pi_1(\mathbb R)=0,
\]
so
\[
s_*:\pi_1(S^1)\to\pi_1(\mathbb R)
\]
is the zero map, making $p_*s_*$ zero rather than the identity on
\[
\pi_1(S^1)\cong\mathbb Z.
\]
Contradiction.
:::

<1>9. Therefore $f$ has no lift to $\mathbb R\to S^1$, despite satisfying
\[
f_*(\pi_1(Y))=0.
\]
::: {.proof}
Nonexistence of the lift follows from <1>4--<1>8, while <1>3 gives the trivial subgroup condition.
Thus the local path-connectedness hypothesis in the usual lifting criterion cannot simply be omitted.
:::
:::
