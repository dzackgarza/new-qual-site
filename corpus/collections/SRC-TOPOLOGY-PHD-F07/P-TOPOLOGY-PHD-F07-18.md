---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-18
kind: problem
title: Fundamental group of a sphere with three points removed
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part Two, question 6 of the Topology Ph.D. Qualifying Exam in assets/attachments/F07phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Sent one puncture to infinity by stereographic projection, reducing to the
    plane minus two points. A compact regular neighborhood of two small meridian
    circles joined by an arc is a pair of pants and collapses to the dumbbell
    graph, which is homotopy equivalent to a wedge of two circles.
---

::: {.problem}
Compute the fundamental group of the (surface of a) sphere when three points on it are removed.
:::

::: {.solution}
Let the three removed points be
\[
p_1,p_2,p_3\in S^2.
\]

<1>1. The three-times punctured sphere is homeomorphic to the plane with two points removed.
::: {.proof}
Stereographic projection from $p_3$ is a homeomorphism
\[
S^2\setminus\{p_3\}\longrightarrow\mathbb R^2.
\]
The distinct points $p_1,p_2$ have distinct images, say $a,b\in\mathbb R^2$.
Restricting stereographic projection therefore gives a homeomorphism
\[
S^2\setminus\{p_1,p_2,p_3\}
\cong
\mathbb R^2\setminus\{a,b\}.
\]
:::

<1>2. The space $\mathbb R^2\setminus\{a,b\}$ deformation retracts onto a graph homeomorphic to two circles joined by an arc.
::: {.proof}
Choose disjoint small closed disks $D_a,D_b$ centered at $a,b$.
Choose an embedded arc $J$ joining one point of $\partial D_a$ to one point of $\partial D_b$, with interior disjoint from the two disks.
Set
\[
\Gamma=\partial D_a\cup J\cup\partial D_b.
\]

Take a sufficiently small closed regular neighborhood $N$ of $\Gamma$ in
\[
\mathbb R^2\setminus\{a,b\}.
\]
The set $N$ is a pair of pants: its complementary components are a punctured neighborhood of $a$, a punctured neighborhood of $b$, and the unbounded exterior component.
Each of these three complementary annular ends can be pushed along its collar onto the corresponding boundary component of $N$.
Doing these three collar deformations, whose supports are disjoint, gives a deformation retraction
\[
\mathbb R^2\setminus\{a,b\}\longrightarrow N.
\]

By construction, a regular neighborhood of a graph collapses along its interval fibers onto the graph itself, so $N$ deformation retracts onto $\Gamma$.
Composing the two deformation retractions gives
\[
\mathbb R^2\setminus\{a,b\}\simeq\Gamma.
\]
The graph $\Gamma$ consists of two circles connected by the contractible arc $J$.
Contracting $J$ to a point gives
\[
\Gamma\simeq S^1\vee S^1.
\]
:::

<1>3. The fundamental group of $S^1\vee S^1$ is the free group on two generators.
::: {.proof}
Let $U$ and $V$ be open neighborhoods in $S^1\vee S^1$ of the first and second circles, enlarged slightly across the wedge point so that
\[
U\cap V
\]
is contractible.
Then
\[
U\simeq S^1,
\qquad
V\simeq S^1,
\qquad
U\cap V\simeq\{*\}.
\]
The Seifert--van Kampen theorem therefore gives
\[
\pi_1(S^1\vee S^1)
\cong
\pi_1(S^1)*\pi_1(S^1)
\cong
\mathbb Z*\mathbb Z.
\]
This is the free group $F_2$ on two generators.
:::

<1>4. Therefore
\[
\boxed{\pi_1\bigl(S^2\setminus\{p_1,p_2,p_3\}\bigr)\cong F_2\cong\mathbb Z*\mathbb Z.}
\]
::: {.proof}
By <1>1, the punctured sphere is homeomorphic to the twice-punctured plane.
By <1>2, that plane has the homotopy type of $S^1\vee S^1$.
Fundamental groups are invariant under homeomorphism and homotopy equivalence, and <1>3 computes the latter group as $F_2$.
:::
:::
