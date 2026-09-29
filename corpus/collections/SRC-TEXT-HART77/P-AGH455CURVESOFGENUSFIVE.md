---
schema: qual/card@1
id: P-AGH455CURVESOFGENUSFIVE
kind: problem
title: Canonical models of curves of genus $5$ and the trisecant cubic surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Canonical Divisor
  - Linear Systems
  - Embeddings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.5.5 together with the retained II.7.7 cubic-scroll
    construction and the surrounding genus-four canonical-model exercises.
    The printed assertion in (b) that the plane quintic always has a node is
    false: the unique delta-one singularity can instead be an ordinary cusp.
    The proof below records that erratum, proves the corrected node-or-cusp
    statement, and proves the dimension, cubic-scroll, trisecant, and
    uniqueness conclusions independently.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Assume $X$ is not hyperelliptic.

a. The curves of genus 5 whose canonical model in $\PP^4$ is a complete intersection $F_2 . F_2 . F_2$ form a family of dimension 12.

b. $X$ has a $g_3^1$ if and only if it can be represented as a plane quintic with one node. These form an irreducible family of dimension 11. Hint: If $D \in g_3^1$, use $K-D$ to map $X \to \PP^2$.

c. \* In that case, the conics through the node cut out the canonical system (not counting the fixed points at the node). Mapping $\PP^2 \to \PP^4$ by this linear system of conics, show that the canonical curve $X$ is contained in a cubic surface $V \subseteq \PP^4$, with $V$ isomorphic to $\PP^2$ with one point blown up (II, Ex. 7.7).

    Furthermore, $V$ is the union of all the trisecants of $X$ corresponding to the $g_3^1$ (5.5.3), so $V$ is contained in the intersection of all the quadric hypersurfaces containing $X$. Thus $V$ and the $g_3^1$ are unique.

Note. Conversely, if $X$ does not have a $g_3^1$, then its canonical embedding is a complete intersection, as in (a). More generally, a classical theorem of Enriques and Petri shows that for any nonhyperelliptic curve of genus $g \geq 3$, the canonical model is projectively normal, and it is an intersection of quadric hypersurfaces unless $X$ has a $g_3^1$ or $g=6$ and $X$ has a $g_5^2$. See Saint-Donat.
:::

::: {.remark title="Erratum to part (b)"}
The word "node" in part (b) is too restrictive.  The correct statement is
that $X$ is trigonal if and only if it is the normalization of a plane
quintic having exactly one singularity of delta invariant $1$.  That
singularity can be an ordinary node or an ordinary cusp.  In part (c),
"the node" should accordingly be replaced by "the double point".

The cuspidal case really occurs.  Over a field of characteristic zero, the
plane quintic
$$
C=V\left(y^2z^3-x^3z^2+x^5+y^5\right)
\subseteq\PP^2
$$
has an ordinary cusp at $[0:0:1]$ and no other singularity.  Step [](#s9){.pf-ref}
checks that its normalization is a nonhyperelliptic trigonal curve of genus
$5$ and, using the uniqueness proved below, cannot have a nodal plane
quintic model.  Thus replacing "node" by "node or ordinary cusp" is
necessary, not merely a weakening of the proof.
:::

::: {.solution}
Let $K$ denote a canonical divisor on $X$.  We work over the algebraically
closed ground field of Chapter IV.

::: pf

::: {.pf-step #s1}
Smooth complete intersections of three quadrics in $\PP^4$ form an
irreducible family of canonically embedded genus-$5$ curves of dimension
$$
\boxed{12}.
$$

::: pf-proof
Put
$$
W_2=H^0\bigl(\PP^4,\OO_{\PP^4}(2)\bigr),
\qquad \dim W_2=15.
$$
A complete intersection of three quadrics is determined by the
three-dimensional subspace of $W_2$ spanned by its equations.  Hence such
complete intersections are parametrized by the open subset
$$
U\subseteq\operatorname{Gr}(3,W_2)
$$
on which the common zero locus is a smooth curve of codimension $3$.  This
open set is nonempty and irreducible, and
$$
\dim U=3(15-3)=36.
$$

For $C\in U$, adjunction gives
$$
K_C
=
\bigl(K_{\PP^4}+2H+2H+2H\bigr)|_C
=H|_C.
$$
Moreover $\deg C=2^3=8$, so
$$
2g(C)-2=\deg K_C=8,
$$
and therefore $g(C)=5$.  Thus the displayed embedding is the canonical
embedding.

Conversely, for a canonical curve which is such a complete intersection,
its three-dimensional space of quadratic equations recovers the point of
$\operatorname{Gr}(3,W_2)$.  Isomorphic canonical curves differ by an
element of $\PGL_5$.  Since
$$
\dim\PGL_5=25-1=24
$$
and a smooth curve of genus $5$ has a zero-dimensional automorphism group,
the family of isomorphism classes has dimension
$$
36-24=12.
$$
Irreducibility follows from that of $U$.
:::

:::

::: {.pf-step #s2}
If $A$ is a $g^1_3$ on $X$, then $A$ is base-point-free and
$$
L:=K-A
$$
is a base-point-free $g^2_5$.

::: pf-proof
If $A$ had a base point $P$, then
$$
h^0(A-P)=h^0(A)=2,
$$
so $A-P$ would be a $g^1_2$, contradicting the hypothesis that $X$ is not
hyperelliptic.  Thus $A$ is base-point-free.

Since $\deg K=8$, one has $\deg L=5$.  Riemann--Roch gives
$$
h^0(L)-h^0(A)=\deg L+1-g=1,
$$
and hence
$$
h^0(L)=3.
$$

Suppose $P$ were a base point of $L$.  Then $h^0(L-P)=3$, while
Riemann--Roch applied to $L-P=K-A-P$ gives
$$
h^0(L-P)=h^0(A+P).
$$
Thus the degree-$4$ divisor $A+P$ would satisfy $h^0(A+P)=3$, attaining
equality in Clifford's theorem.  Since $0<\deg(A+P)<2g-2$, the equality
case of Clifford's theorem would make $X$ hyperelliptic, a contradiction.
Therefore $L$ is base-point-free, and its degree and number of sections make
it a $g^2_5$.
:::

:::

::: {.pf-step #s3}
The morphism
$$
\phi_L:X\longrightarrow\PP^2
$$
is birational onto an integral plane quintic whose only singularity has
delta invariant $1$.

::: pf-proof
Because $|L|$ is complete and has dimension $2$, its image is not contained
in a line.  If $e$ is the generic degree of $\phi_L$ and $d$ is the degree
of its image, then
$$
5=\deg L=ed.
$$
Since $5$ is prime and $d>1$, necessarily
$$
e=1,
\qquad d=5.
$$
Thus $\phi_L$ is birational onto an integral plane quintic $C$.

The arithmetic genus of a plane quintic is
$$
p_a(C)=\frac{(5-1)(5-2)}2=6,
$$
whereas its normalization $X$ has genus $5$.  Hence
$$
\sum_{q\in\operatorname{Sing}C}\delta_q
=p_a(C)-g(X)=1.
$$
There is therefore exactly one singular point, and its delta invariant is
$1$.  Such a plane double point is either an ordinary node or an ordinary
cusp.  This proves the corrected forward implication in part (b).
:::

:::

::: {.pf-step #s4}
Conversely, the normalization of an integral plane quintic having
exactly one singularity of delta invariant $1$ carries a $g^1_3$.

::: pf-proof
Let
$$
\nu:X\longrightarrow C\subseteq\PP^2
$$
be the normalization and let $p$ be the unique singular point.  Its
multiplicity is $2$.  Blow up $p$:
$$
\pi:S=\operatorname{Bl}_p\PP^2\longrightarrow\PP^2.
$$
For a node or an ordinary cusp, the strict transform $\widetilde C$ is
smooth and is naturally isomorphic to $X$.

Write $H$ for the pullback of a line and $E$ for the exceptional curve.
Then
$$
\widetilde C\sim5H-2E.
$$
The pencil of lines through $p$ has strict-transform class $H-E$, and on
$\widetilde C$ it has degree
$$
(5H-2E)\cdot(H-E)=3.
$$
It has no base point on the blowup.  Hence it cuts out a base-point-free
$g^1_3$ on $X$.  This proves the corrected converse in part (b).
:::

:::

::: {.pf-step #s5}
The conics through the unique double point cut out the complete
canonical system on $X$, and they embed the blowup $S$ as a cubic scroll
$$
V\subseteq\PP^4.
$$

::: pf-proof
On $S$ one has
$$
K_S=-3H+E,
\qquad
\widetilde C\sim5H-2E.
$$
Adjunction therefore gives
$$
K_X
=
\bigl(K_S+\widetilde C\bigr)|_{\widetilde C}
=
(2H-E)|_{\widetilde C}.
$$
The divisor $2H-E$ is exactly the strict-transform system of conics through
$p$.

Its space of global sections has dimension $5$.  The restriction map to
$X$ is injective, since
$$
(2H-E)-\widetilde C=-3H+E
$$
has no nonzero section.  Since $h^0(X,K_X)=5$, restriction is an
isomorphism.  Thus the conics through $p$ cut out the complete canonical
system.

By [[P-AGH277VERONESESURF|Exercise II.7.7(c)]], the complete system
$|2H-E|$ embeds $S$ in $\PP^4$ as a smooth cubic scroll $V$.  Its restriction
to $X$ is the canonical embedding, so the canonical curve lies on $V$.
This argument applies equally to the nodal and cuspidal cases.
:::

:::

::: {.pf-step #s6}
The surface $V$ is the union of the trisecant lines corresponding to
the $g^1_3$.

::: pf-proof
The ruling of $S$ consists of the strict transforms of lines through $p$,
each of class
$$
F=H-E.
$$
Since
$$
(2H-E)\cdot F=1,
$$
the embedding of step [](#s5){.pf-ref} maps every ruling fibre to a line in $\PP^4$.
Moreover
$$
\widetilde C\cdot F
=(5H-2E)\cdot(H-E)=3.
$$
Thus each ruling line meets the canonical curve in a length-$3$ divisor,
namely a member of the $g^1_3$ from step [](#s4){.pf-ref}.  The ruling fibres cover
$S$, so their image lines cover $V$.  Hence $V$ is exactly the union of
these trisecants.
:::

:::

::: {.pf-step #s7}
The common zero locus of all quadrics containing the canonical curve
is exactly $V$.  Consequently both $V$ and the $g^1_3$ are unique.

::: pf-proof
Let $Q\subseteq\PP^4$ be any quadric containing the canonical curve, and
let $\ell$ be one of the ruling lines of step [](#s6){.pf-ref}.  The restriction of the
equation of $Q$ to
$$
\ell\cong\PP^1
$$
has degree $2$, but it vanishes on the length-$3$ subscheme
$\ell\cap X$.  It must therefore vanish identically.  Hence every quadric
containing $X$ contains every ruling line, and therefore contains $V$:
$$
H^0(\PP^4,\mci_X(2))
\subseteq
H^0(\PP^4,\mci_V(2)).
$$

Exercise II.7.7(c) gives $V$ scheme-theoretically as the common zero locus
of three independent quadrics; equivalently,
$$
h^0(\PP^4,\mci_V(2))=3.
$$
On the other hand
$$
h^0(\PP^4,\OO(2))=15,
\qquad
h^0(X,2K)=16+1-5=12,
$$
so the restriction map to $H^0(X,2K)$ has kernel of dimension at least
$15-12=3$.  Therefore
$$
h^0(\PP^4,\mci_X(2))\ge3.
$$
The preceding inclusion forces equality:
$$
H^0(\PP^4,\mci_X(2))
=
H^0(\PP^4,\mci_V(2)).
$$
Thus the intersection of all quadrics through $X$ is precisely $V$.

Now start with any $g^1_3$ on $X$.  Steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, and [](#s6){.pf-ref} construct from it a
cubic scroll, and the argument just given identifies that scroll with the
same intrinsic base locus of the quadrics through $X$.  Hence the scroll is
unique.  A smooth cubic scroll $\operatorname{Bl}_p\PP^2$ has a unique
ruling by lines, and intersecting that ruling with $X$ recovers the
$g^1_3$.  The $g^1_3$ is therefore unique as well.
:::

:::

::: {.pf-step #s8}
The trigonal genus-$5$ curves form an irreducible family of dimension
$$
\boxed{11}.
$$
The nodal plane-quintic models form a dense open subfamily; cuspidal models
form a proper subfamily.

::: pf-proof
Consider pairs
$$
(p,C),
\qquad
p\in\PP^2,
$$
where $C$ is a plane quintic singular at $p$.  For fixed $p$, the condition
that a quintic be singular at $p$ imposes three independent linear
conditions on
$$
\PP H^0(\PP^2,\OO(5))\cong\PP^{20}.
$$
Thus these pairs form an irreducible projective bundle of dimension
$$
2+17=19.
$$

The locus on which $p$ is an ordinary node and $C$ has no other
singularity is nonempty and open, hence irreducible of dimension $19$.
An ordinary cusp is obtained when the quadratic tangent cone acquires a
double factor while the cubic transverse term remains nonzero.  This is one
additional condition, and a small deformation of that quadratic term splits
the double tangent into two distinct tangents.  Since smoothness away from
$p$ is open, the cuspidal locus lies in the closure of the nodal locus.
Therefore the locus of quintics having exactly one delta-one singularity is
irreducible of dimension $19$.

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} identify its normalizations with the trigonal genus-$5$
curves.  By step [](#s7){.pf-ref} the $g^1_3$ is unique, so the residual $g^2_5=|K-A|$
is unique; choosing its three sections only changes coordinates in
$\PP^2$.  Hence two such plane models represent the same curve exactly up
to the action of $\PGL_3$.  Stabilizers are zero-dimensional because a
genus-$5$ curve has a zero-dimensional automorphism group.  Since
$$
\dim\PGL_3=8,
$$
the family of isomorphism classes is irreducible of dimension
$$
19-8=11.
$$
The nodal locus is the nonempty dense open described above; the cuspidal
locus is its codimension-one specialization.
:::

:::

::: {.pf-step #s9}
The cuspidal quintic displayed in the erratum gives a genuine
counterexample to the literal nodal assertion in part (b).

::: pf-proof
Assume the ground field has characteristic zero and set
$$
F=y^2z^3-x^3z^2+x^5+y^5.
$$
At
$$
p=[0:0:1],
$$
the affine equation is
$$
y^2-x^3+x^5+y^5=0.
$$
On the blowup chart $y=xu$, its strict transform has equation
$$
u^2-x+x^3(1+u^5)=0.
$$
This is smooth at $(x,u)=(0,0)$ because its $x$-derivative there is $-1$,
and it meets the exceptional curve $x=0$ there with multiplicity $2$.
Thus $p$ is an ordinary cusp and $\delta_p=1$.

There is no singular point on $z=0$, because there
$$
F_x=5x^4,
\qquad
F_y=5y^4.
$$
On the chart $z=1$, a singular point must satisfy
$$
x^2(-3+5x^2)=0,
\qquad
y(2+5y^3)=0,
\qquad
3y^2-2x^3=0.
$$
If $x=0$, the last equation forces $y=0$.  If $y=0$, it similarly forces
$x=0$.  In the remaining case
$$
x^2=\frac35,
\qquad
y^3=-\frac25,
\qquad
3y^2=2x^3.
$$
Cubing the last equality and substituting the first two gives
$$
\frac{108}{25}=\frac{648}{625}x,
$$
so $x=25/6$, contradicting $x^2=3/5$.  Thus $p$ is the only singular point.
Since its germ at $p$ is unibranch, the quintic is integral: distinct
projective plane components would meet by Bezout, producing either another
singular point or more than one branch at $p$.

Let $X$ be its normalization.  The genus formula gives
$$
g(X)=6-1=5,
$$
and projection from $p$ gives a degree-$3$ map to $\PP^1$.  The curve is not
hyperelliptic: if it also had a degree-$2$ map to $\PP^1$, the product of
the degree-$2$ and degree-$3$ maps would be birational onto a curve of
bidegree $(2,3)$ in $\PP^1\times\PP^1$, because its generic degree divides
both $2$ and $3$.  Such a curve has arithmetic genus
$$
(2-1)(3-1)=2,
$$
contradicting $g(X)=5$.

Finally, let $M$ be the line bundle of any birational plane quintic model
of $X$.  Then $\deg M=5$ and $h^0(M)\ge3$.  Riemann--Roch gives
$$
h^0(K-M)=h^0(M)-1\ge2,
$$
so $K-M$ is a degree-$3$ pencil.  Clifford's theorem forces $h^0(M)=3$,
and step [](#s7){.pf-ref} says that this $g^1_3$ is the unique one.  Hence
$$
M=K-A
$$
for the unique trigonal pencil $A$, so the plane quintic model is unique up
to projective coordinates.  The model above is cuspidal, and therefore this
$X$ has no nodal plane quintic model.  This proves the erratum asserted
above.
:::

:::

::: pf-qed
for the corrected statement.

Step [](#s1){.pf-ref} proves part (a).  Steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, and [](#s4){.pf-ref} prove the corrected equivalence
in part (b), and step [](#s8){.pf-ref} proves its irreducibility and dimension claim.
Steps [](#s5){.pf-ref}, [](#s6){.pf-ref}, and [](#s7){.pf-ref} prove all the cubic-scroll, trisecant, and uniqueness
assertions in part (c).  Step [](#s9){.pf-ref} proves that the printed word "node"
cannot be retained in general.
:::

:::
:::
