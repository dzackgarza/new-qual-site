---
schema: qual/card@1
id: E-PER08-1.4
kind: problem
title: Homotopy and homeomorphism types of capital letters
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 1.4 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the explicit deformation retraction of A, the local-valence obstruction to A being homeomorphic to O, and the nine graph-homeomorphism classes in the stated skeletal typeface.
---

::: {.problem}
Show carefully that the letter $A$, regarded as a union of closed line segments in $\mathbb R^2$, is homotopy equivalent but not homeomorphic to the letter $O$.

Show briefly that all but one of the capital letters of the alphabet is either contractible or deformation retracts onto a subspace homeomorphic to $O$.
Show that the letters fall into exactly three homotopy types.
How many homeomorphism types are there?

Regard a letter as a finite union of images of paths $[0,1]\to\mathbb R^2$, after choosing a typeface.
:::

::: {.solution}
We use the following skeletal block typeface. Curved strokes are replaced by arcs, and crossings or stroke junctions are vertices. The resulting letters are finite topological graphs. In this typeface $I$ has top and bottom bars, and the letters have the graph-homeomorphism classes listed in <1>4 below.

<1>1. The letter $A$ is homotopy equivalent to $O$.
::: {.proof}
Model $A$ as two sloping legs meeting at the apex, together with a crossbar joining the legs. Let $v_1,v_2$ be the two crossbar junctions. The two sloping segments above $v_1,v_2$, together with the crossbar, form a simple closed curve $C\subset A$, hence $C$ is homeomorphic to $S^1$ and therefore to $O$.

The parts of the two legs below $v_1$ and $v_2$ are closed intervals attached to $C$ at one endpoint. Collapse each such interval linearly to its attaching point while fixing $C$ pointwise. Explicitly, if a lower leg is parametrized by $\ell:[0,1]\to A$ with $\ell(0)=v_i$, set
\[
H_t(\ell(s))=\ell((1-t)s),
\]
and put $H_t(y)=y$ for $y\in C$. The two definitions agree at the attaching points, so they give a deformation retraction of $A$ onto $C$.

Thus
\[
A\simeq C\cong O.
\]
:::

<1>2. The letters $A$ and $O$ are not homeomorphic.
::: {.proof}
At either crossbar junction $v_i$ of $A$, a sufficiently small neighborhood in $A$ is a three-pronged star: deleting $v_i$ from that neighborhood leaves three connected components. Thus $v_i$ has local valence $3$.

Every point of $O\cong S^1$ has a sufficiently small neighborhood homeomorphic to an open interval, and deleting its center leaves exactly two connected components. Hence every point of $O$ has local valence $2$.

Local valence is preserved by homeomorphisms. Therefore no homeomorphism $A\to O$ exists.
:::

<1>3. There are exactly three homotopy types among the letters in this typeface.
::: {.proof}
Suppressing degree-$2$ subdivision vertices does not change a graph's homeomorphism type and makes the classification transparent.

Every letter except
\[
A,B,D,O,P,Q,R
\]
is a tree. Every tree contracts to a point by successively collapsing terminal edges, so these letters are contractible.

Each of
\[
A,D,O,P,Q,R
\]
has exactly one independent cycle. Any trees attached to that cycle can be collapsed edge-by-edge, giving a deformation retraction onto the cycle. Hence each of these letters is homotopy equivalent to $S^1$.

The letter $B$ has two loops meeting at one vertex after degree-$2$ vertices are suppressed, so it is homeomorphic to a subdivision of the figure-eight graph
\[
S^1\vee S^1.
\]
Thus $B$ is the unique letter in the third homotopy type.

These three types are distinct. Their first homology groups are respectively
\[
0,\qquad \mathbb Z,\qquad \mathbb Z^2,
\]
and singular homology is invariant under homotopy equivalence. Therefore the letters have exactly three homotopy types.
:::

<1>4. In the chosen typeface there are exactly nine homeomorphism types.
::: {.proof}
After suppressing degree-$2$ vertices, the classes are:

1. **An interval:** $C,G,J,L,M,N,S,U,V,W,Z$.
2. **A triod** (one degree-$3$ vertex with three leaves): $E,F,T,Y$.
3. **A four-pronged star** (one degree-$4$ vertex with four leaves): $K,X$.
4. **Two degree-$3$ vertices joined by an edge, each carrying two leaves:** $H,I$.
5. **A circle:** $D,O$.
6. **A circle with one pendant edge:** $P,Q$.
7. **A circle with one pendant edge at each of two distinct points:** $A$.
8. **A circle with two pendant edges attached at the same point:** $R$.
9. **A figure eight:** $B$.

Letters within each row are homeomorphic by mapping the corresponding edges monotonically to one another.

Different rows are not homeomorphic. For finite graphs, a homeomorphism preserves the set of points of each local valence and the incidence pattern of the components obtained after deleting those branch points. Rows 1--4 are distinguished by their branch-point data; rows 5--8 are distinguished by the number and placement of branch points and pendant components relative to the unique cycle; row 9 has two independent cycles. Hence no two rows are homeomorphic.

Therefore this typeface has exactly
\[
\boxed{9}
\]
homeomorphism types.
:::

The numerical homeomorphism count depends on the chosen typeface, as the exercise allows; the count $9$ is for the explicit skeletal convention above. The three homotopy types are the point, $S^1$, and $S^1\vee S^1$.
:::
