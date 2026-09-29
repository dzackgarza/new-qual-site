---
schema: qual/card@1
id: P-AGH454PLANEMODELSGENUSFOUR
kind: problem
title: Least degree of a nodal plane model of a nonhyperelliptic curve of genus $4$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Linear Systems
  - Embeddings
  - Canonical Divisor
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.5.4 together with IV.3.11, the generic projection
    theorem for curves, and the genus-four quadric/ruling description from
    IV.5.3. Cross-checked the projection-from-a-canonical-point construction
    against published notes treating the smooth-quadric and quadric-cone
    cases. The proof below identifies the singularity types from tangent
    planes and the total delta invariant rather than only counting secants.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Another way of distinguishing curves of genus $g$ is to ask, what is the least degree of a birational plane model with only nodes as singularities (3.11)? Let $X$ be nonhyperelliptic of genus 4. Then:

a. if $X$ has two $g_3^1$'s, it can be represented as a plane quintic with two nodes, and conversely;

b. if $X$ has one $g_3^1$, then it can be represented as a plane quintic with a tacnode (I, Ex.
5.14d), but the least degree of a plane representation with only nodes is 6.
:::

::: {.solution}
Let
$$
C\subseteq\PP^3
$$
be the canonical model of the nonhyperelliptic genus-$4$ curve $X$.  By
[[P-AGH453MODULIGENUSFOUR|Exercise IV.5.3]],
$$
C=Q\cap F_3,
$$
where $Q$ is the unique quadric containing $C$.  The curve has two
$g^1_3$'s when $Q$ is smooth and one when $Q$ is a rank-$3$ quadric cone.

::: pf

::: {.pf-step #s1}

For a general point $P\in C$, projection from $P$ is the morphism
defined by
$$
\boxed{|K-P|:X\longrightarrow\PP^2,}
$$
and it is birational onto a plane quintic.

::: pf-proof

Hyperplanes in $\PP^3$ through $P$ restrict on the canonical curve to
canonical divisors containing $P$.  Removing that fixed point gives the
complete linear system $|K-P|$.  Since
$$
\deg(K-P)=2g-3=5
$$
and
$$
\ell(K-P)=g-1=3,
$$
it gives a morphism to $\PP^2$; geometrically this is the projection of the
canonical curve from $P$, extended across the centre.

Its image spans $\PP^2$, so it is not a line.  If its generic degree were
$e>1$, then
$$
5=e\deg C'
$$
for the plane image $C'$.  Since $5$ is prime, this would force
$\deg C'=1$, a contradiction.  Thus the map is birational and
$$
\deg C'=5.
$$

We can make the required generality explicit.  Each ruling gives a
degree-$3$ map
$$
C\longrightarrow\PP^1,
$$
whose ramification locus is finite in characteristic $0$.  Avoiding the
ramification loci makes the ruling fibre through $P$ reduced, hence gives
three distinct points
$$
P+A+B.
$$
Also avoid the finite canonical Wronskian locus of
[[P-AGH446HYPEROSCULATIONPOINTS|Exercise IV.4.6]].  Then the canonical
vanishing sequence at $P$ is
$$
0,1,2,3.
$$
After subtracting the base point $P$, the system $|K-P|$ has vanishing
sequence
$$
0,1,2,
$$
so its map is immersive at $P$.  The complement of these finite exceptional
sets is nonempty, and we choose $P$ there.

:::

:::

::: {.pf-step #s2}

A line through $P$ identifies two distinct points of
$C\setminus\{P\}$ under this projection if and only if it is a ruling line
of $Q$ through $P$.

::: pf-proof

Suppose distinct
$$
A,B\in C\setminus\{P\}
$$
have the same image.  Then
$$
P,A,B
$$
are collinear.  Their line $L$ meets the quadric $Q$ in a length at least
$3$ subscheme.  Since a line not contained in a quadric meets it in degree
$2$, Bezout forces
$$
L\subseteq Q.
$$
Thus $L$ is a ruling line through $P$.

Conversely, if $L\subseteq Q$ is a ruling line through $P$, then
$$
L\cdot C
=
L\cdot F_3
=3.
$$
For our general $P$,
$$
L\cap C=P+A+B
$$
with $A,B$ distinct from each other and from $P$.  Projection from $P$
contracts $L$, so it identifies $A$ and $B$.

:::

:::

::: {.pf-step #s3}

Assume $Q$ is smooth.  Then the plane quintic of step [](#s1){.pf-ref} has exactly
two singularities, both nodes.

::: pf-proof

A smooth quadric
$$
Q\cong\PP^1\times\PP^1
$$
has exactly two ruling lines through $P$.  By step [](#s2){.pf-ref} they give two
identified residual pairs
$$
A_i,B_i,
\qquad i=1,2.
$$

We first check that each resulting double point is transverse.  Fix one
ruling line $L$ and its residual points $A,B$.  The plane spanned by
$$
P\quad\text{and}\quad T_A C
$$
is the tangent plane $T_AQ$: both contain $L$, and $T_AC\subseteq T_AQ$.
Similarly the plane spanned by $P$ and $T_BC$ is $T_BQ$.  On a smooth
quadric the tangent plane varies nontrivially along a ruling, so
$$
T_AQ\ne T_BQ
$$
for $A\ne B$.  Under projection from $P$, this says that the two branches
at the identified image point have distinct tangent lines.  Hence that
singularity is a node.

Thus the plane image already has two nodes.  A plane quintic has arithmetic
genus
$$
p_a=\frac{(5-1)(5-2)}2=6,
$$
whereas its normalization $X$ has genus $4$.  Therefore the total delta
invariant of all singularities is
$$
6-4=2.
$$
The two nodes contribute
$$
1+1=2.
$$
Hence there are no further singularities.  This proves the forward
assertion in part (a).

:::

:::

::: {.pf-step #s4}

Conversely, the normalization of a plane quintic with two nodes has
two distinct $g^1_3$'s.

::: pf-proof

Let
$$
\nu:X\longrightarrow C'\subseteq\PP^2
$$
be the normalization of an integral plane quintic whose only singularities
are two nodes
$$
N_1,N_2.
$$
The genus formula gives
$$
g(X)
=
6-1-1
=4.
$$

Write
$$
\nu^{-1}(N_i)=\{P_i,Q_i\},
\qquad
A_i=P_i+Q_i.
$$
Let
$$
H=\nu^*\OO_{C'}(1).
$$
The pencil of lines through $N_i$ pulls back, after removing the two fixed
branches above the node, to a base-point-free pencil
$$
|H-A_i|
$$
of degree
$$
5-2=3.
$$
Thus each node gives a $g^1_3$.

These two pencils are distinct.  If
$$
H-A_1\sim H-A_2,
$$
then
$$
A_1\sim A_2.
$$
The effective divisors $A_1$ and $A_2$ are distinct, so this would give
$$
\ell(A_1)\ge2,
$$
that is, a $g^1_2$ on $X$.  Then $X$ would be hyperelliptic, contrary to
the standing hypothesis.  Hence the two degree-$3$ pencils are distinct.
This proves the converse in part (a).

:::

:::

::: {.pf-step #s5}

Assume $Q$ is a rank-$3$ quadric cone.  Then the plane quintic of
step [](#s1){.pf-ref} has exactly one singular point, and it is a tacnode.

::: pf-proof

Through a smooth point $P$ of a quadric cone there is exactly one ruling
line
$$
L\subseteq Q.
$$
For general $P$ write
$$
L\cap C=P+A+B
$$
with $A,B$ distinct.  Step [](#s2){.pf-ref} says that projection identifies precisely
this residual pair.

The crucial difference from the smooth-quadric case is that the tangent
plane to a quadric cone is constant along a ruling.  Thus
$$
T_AQ=T_BQ.
$$
As in step [](#s3){.pf-ref}, the tangent line to the projected branch coming from $A$
is obtained by projecting the plane spanned by $P$ and $T_AC$, namely
$T_AQ$; similarly the tangent line of the branch coming from $B$ is obtained
from $T_BQ$.  The equality above therefore says that the two smooth branches
at the identified image point have the same tangent line.

Two distinct smooth branches with a common tangent have delta invariant at
least $2$.  On the other hand the plane image is again a quintic whose
normalization has genus $4$, so the total delta invariant is
$$
6-4=2.
$$
Consequently this one singularity has delta invariant exactly $2$, there
are no other singularities, and the two branches have intersection
multiplicity exactly $2$.  Equivalently, the singularity is an ordinary
tacnode, analytically of type
$$
y^2=x^4.
$$
This proves the first assertion of part (b).

:::

:::

::: {.pf-step #s6}

If $X$ has only one $g^1_3$, then it has no birational plane model of
degree less than $6$ whose only singularities are nodes.

::: pf-proof

Let an integral nodal plane model have degree $d$ and $r$ nodes.  Its
normalization has genus
$$
4
=
\frac{(d-1)(d-2)}2-r.
$$
For
$$
d\le4
$$
the arithmetic genus is at most $3$, impossible.

If
$$
d=5,
$$
the equation becomes
$$
4=6-r,
$$
so
$$
r=2.
$$
By step [](#s4){.pf-ref}, the normalization of such a two-nodal quintic has two distinct
$g^1_3$'s.  This contradicts the hypothesis that $X$ has only one.
Therefore every nodal plane model has degree at least $6$.

:::

:::

::: {.pf-step #s7}

Every such $X$ has a degree-$6$ plane model whose only singularities
are nodes.

::: pf-proof

Use the canonical embedding
$$
C\subseteq\PP^3.
$$
It has degree
$$
\deg C=\deg K=6.
$$
The [[T-CRVEMBP3|generic projection theorem for curves]] says that projection
from a general point
$$
O\in\PP^3\setminus C
$$
is birational onto a plane curve whose only singularities are nodes.
Because the centre does not lie on $C$, projection preserves the
hyperplane bundle, so the plane image still has degree $6$.

Combining this with step [](#s6){.pf-ref} shows that
$$
\boxed{6}
$$
is the least possible degree of a nodal plane model.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove part (a).  Step [](#s5){.pf-ref} constructs the tacnodal quintic
in the one-$g^1_3$ case, and steps [](#s6){.pf-ref} and [](#s7){.pf-ref} prove that the least degree of
a plane model having only nodes is $6$.

:::

:::

:::
