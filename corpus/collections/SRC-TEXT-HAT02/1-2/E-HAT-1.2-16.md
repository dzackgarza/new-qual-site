---
schema: qual/card@1
id: E-HAT-1.2-16
kind: problem
title: Fundamental group of surface of infinite genus is free on infinitely many generators
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Free Groups
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.2, Exercise 16 and the accompanying infinite-genus surface figure; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Exhausted the surface by compact finite-genus subsurfaces with compatible graph spines, then used compactness of loops and nullhomotopies to identify the direct-limit group with a countably generated free group.
---

Show that the fundamental group of the surface of infinite genus shown below is free on an infinite number of generators.

::: {.solution}
Let $X$ denote the pictured surface.

<1>1. Choose an exhaustion
\[
M_1\subset M_2\subset\cdots\subset X,
\qquad
X=\bigcup_{n\ge1}M_n,
\]
where each $M_n$ is a compact connected orientable surface containing finitely many consecutive handles and having two boundary circles in the cylindrical ends.
::: {.proof}
Cut the pictured surface by two transverse circles, one far to the left and one far to the right of the first $n$ chosen handles.
The compact region between these circles is $M_n$.
Move the cutting circles outward as $n$ increases so that every handle is eventually included.
Every point of $X$ lies between some such pair of cuts, so the union is all of $X$.
:::

<1>2. Each $M_n$ deformation retracts onto a finite connected graph $G_n$, and the spines may be chosen so that
\[
G_n\subset G_{n+1}
\]
and $G_{n+1}$ is obtained from $G_n$ by adjoining finitely many new loops along a tree.
::: {.proof}
A compact orientable surface of genus $g$ with two boundary components has the usual handle decomposition with one $0$-handle, $2g+1$ $1$-handles, and no $2$-handle after one boundary component is left unfilled.
Its core graph is therefore a wedge of $2g+1$ circles and is a deformation retract.

For the explicit exhaustion in <1>1, choose the core interval along the cylinder once and, for each handle, add the two standard core loops of that handle.
When the cutting circles are moved outward, the old core graph is unchanged and only the cores of the newly included handles and connecting tree segments are added.
Thus the spines can be chosen compatibly as claimed.
:::

<1>3. For each $n$,
\[
\pi_1(M_n)\cong F(B_n)
\]
for a finite basis $B_n$, and the inclusion
\[
\pi_1(M_n)\longrightarrow\pi_1(M_{n+1})
\]
identifies $F(B_n)$ with a free factor of $F(B_{n+1})$.
::: {.proof}
By <1>2,
\[
\pi_1(M_n)\cong\pi_1(G_n),
\]
and the fundamental group of a finite connected graph is free.
Choose a maximal tree in $G_n$ and extend it to a maximal tree in $G_{n+1}$.
The edges outside the tree give a free basis $B_n$, and the newly added non-tree edges give additional generators in $B_{n+1}$.
Hence
\[
B_n\subset B_{n+1}
\]
and
\[
F(B_{n+1})\cong F(B_n)*F(B_{n+1}\setminus B_n).
\]
:::

<1>4. Let
\[
B=\bigcup_{n\ge1}B_n.
\]
Then $B$ is countably infinite.
::: {.proof}
Each $B_n$ is finite, so their countable union is countable.
The genus of $M_n$ tends to infinity, and each additional handle contributes two new independent graph loops, so the cardinalities $|B_n|$ are unbounded.
Thus $B$ is infinite.
:::

<1>5. The natural homomorphism
\[
\Phi:F(B)\longrightarrow\pi_1(X)
\]
is surjective.
::: {.proof}
Let $\gamma:S^1\to X$ be any based loop.
Its image is compact.
Since the interiors of the exhaustion pieces cover $X$, compactness gives some $n$ with
\[
\gamma(S^1)\subseteq M_n.
\]
Hence $[\gamma]$ lies in the image of
\[
\pi_1(M_n)=F(B_n)\subseteq F(B).
\]
:::

<1>6. The homomorphism $\Phi$ is injective.
::: {.proof}
Let a reduced word $w$ in finitely many generators from $B$ map to the identity in $\pi_1(X)$.
Choose $n$ so that all letters of $w$ lie in $B_n$.
Since $\Phi(w)=1$, a loop in $M_n$ representing $w$ admits a nullhomotopy
\[
H:D^2\to X.
\]
The image $H(D^2)$ is compact, so it is contained in some larger exhaustion piece $M_m$ with $m\ge n$.
Thus $w$ is trivial in
\[
\pi_1(M_m)=F(B_m).
\]
But <1>3 says $F(B_n)$ embeds as a free factor of $F(B_m)$.
Therefore a reduced word in $B_n$ that is trivial in $F(B_m)$ was already trivial in $F(B_n)$.
Hence $w=1$ in $F(B)$.
:::

<1>7. Consequently
\[
\boxed{\pi_1(X)\cong F(B),}
\]
the free group on countably infinitely many generators.
::: {.proof}
By <1>5--<1>6, $\Phi$ is an isomorphism, and <1>4 identifies its basis as countably infinite.
:::
:::
