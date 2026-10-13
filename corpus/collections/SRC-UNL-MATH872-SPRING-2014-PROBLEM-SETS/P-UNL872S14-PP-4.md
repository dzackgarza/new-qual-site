---
schema: qual/card@1
id: P-UNL872S14-PP-4
kind: problem
title: UNL Math 872 Spring 2014 assignment PP.4
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against assignment PP.4 on the retained UNL Math 872 Section 001 Spring 2014 problem-sets page PDF.
---

::: {.problem}
Let X be the topological space built in problem PP.2. Describe a Δ-complex structure for X, and compute the homology groups $\mathrm { H ^ { s i m p l } _ { n } ( X ) }$ for all n. (Hint: Use four prisms.)
:::

::: {.solution}
Use the same quarter-turn face identifications and the same oriented CW cells
\[
A,B;\qquad p,q,r,s;\qquad F_x,F_y,F_z;\qquad C
\]
constructed in PP.2.

## A compatible \(\Delta\)-complex

<1>1. Let
\[
c_0=(1/2,1/2,0),
\qquad
c_1=(1/2,1/2,1)
\]
be the centers of the bottom and top faces.

::: {.proof}
These are the centers of the two opposite \(z\)-faces.
:::

<1>2. Join \(c_0\) to the four bottom vertices. This subdivides the bottom
square into four triangles.

::: {.proof}
The four segments from the center to the four vertices partition the square
into four triangular regions with disjoint interiors.
:::

<1>3. Apply the corresponding subdivision to the top square using \(c_1\).

::: {.proof}
The top-bottom quarter-turn gluing
\[
(x,y,0)\sim(y,1-x,1)
\]
sends the bottom center \(c_0\) to the top center \(c_1\) and permutes the
four corners cyclically. Hence it carries the bottom four-triangle
subdivision to the top four-triangle subdivision.
:::

<1>4. Joining each bottom triangle to the corresponding top triangle divides
the cube into
\[
\boxed{4\text{ triangular prisms}}.
\]

::: {.proof}
Each radial sector of the bottom square is extruded through the \(z\)-direction
to the corresponding sector of the top square. The four resulting prisms
have disjoint interiors and fill the cube.
:::

<1>5. On each rectangular prism face, choose a diagonal, and on every
boundary face paired by a cube identification choose the diagonal on the
paired face to be its image under that identification.

::: {.proof}
Each face pairing is an affine homeomorphism of squares. Thus any chosen
diagonal on one face has a unique image diagonal on its paired face. This
ensures that the subdivisions match under the quotient identifications.
:::

<1>6. Triangulate each triangular prism into three tetrahedra compatibly with
the chosen boundary diagonals.

::: {.proof}
A triangular prism with bottom vertices \(u_0,u_1,u_2\) and corresponding
top vertices \(u'_0,u'_1,u'_2\) admits the standard triangulation
\[
[u_0,u_1,u_2,u'_2],
\]
\[
[u_0,u_1,u'_1,u'_2],
\]
\[
[u_0,u'_0,u'_1,u'_2].
\]
The induced diagonals on the rectangular faces are exactly the standard
staircase diagonals. Relabel each prism so these agree with the choices in
step <1>5.
:::

<1>7. Thus the cube has a triangulation by
\[
\boxed{12\text{ tetrahedra}}
\]
whose boundary triangulations are preserved by all three quarter-turn face
pairings.

::: {.proof}
There are four prisms by step <1>4 and three tetrahedra in each by step
<1>6. Compatibility on paired boundary faces is step <1>5.
:::

<1>8. Passing to the quotient gives a finite \(\Delta\)-complex structure on
\(X\).

::: {.proof}
The interiors of the tetrahedra map injectively to the quotient. Their faces
are glued by affine maps that preserve the chosen face triangulations.
This is precisely a \(\Delta\)-complex structure.
:::

## Homology

We compute with the smaller finite CW structure from PP.2. Subdivision does
not change homology, so these groups are the simplicial homology groups of
the \(\Delta\)-complex in step <1>8.

<1>9. The cellular chain groups are
\[
\boxed{
0
\longrightarrow
\mathbb Z
\xrightarrow{\partial_3}
\mathbb Z^3
\xrightarrow{\partial_2}
\mathbb Z^4
\xrightarrow{\partial_1}
\mathbb Z^2
\longrightarrow0}.
\]

::: {.proof}
PP.2 gave two \(0\)-cells \(A,B\), four \(1\)-cells \(p,q,r,s\), three
\(2\)-cells \(F_x,F_y,F_z\), and one \(3\)-cell \(C\).
:::

<1>10. With the orientations fixed in PP.2,
\[
\boxed{
\partial_1p=\partial_1q=B-A}
\]
and
\[
\boxed{
\partial_1r=\partial_1s=A-B}.
\]

::: {.proof}
The representatives from PP.2 were
\[
p:000(A)\to100(B),
\qquad
q:000(A)\to010(B),
\]
\[
r:001(B)\to101(A),
\qquad
s:010(B)\to110(A).
\]
The cellular boundary of an oriented \(1\)-cell is terminal vertex minus
initial vertex.
:::

<1>11. Therefore
\[
\boxed{
\partial_1(x_p,x_q,x_r,x_s)
=
(x_p+x_q-x_r-x_s)(B-A)}.
\]

::: {.proof}
Extend the formulas in step <1>10 linearly.
:::

<1>12. The image of \(\partial_1\) is
\[
\boxed{
\mathbb Z\langle B-A\rangle},
\]
so
\[
\boxed{H_0(X)\cong\mathbb Z}.
\]

::: {.proof}
The coefficient map
\[
(x_p,x_q,x_r,x_s)\mapsto x_p+x_q-x_r-x_s
\]
is surjective, so
\[
\operatorname{im}\partial_1
=
\mathbb Z(B-A).
\]
Thus
\[
H_0(X)
=
\mathbb Z\langle A,B\rangle/
\mathbb Z\langle B-A\rangle
\cong
\mathbb Z.
\]
:::

<1>13. The three \(2\)-cell attaching words from PP.2 are
\[
q\,r\,p\,s,
\]
\[
s^{-1}rqp^{-1},
\]
and
\[
pr\,s^{-1}q^{-1}.
\]

::: {.proof}
These were computed from the three pairs of opposite cube faces in PP.2.
:::

<1>14. Hence
\[
\boxed{
\partial_2F_x=p+q+r+s},
\]
\[
\boxed{
\partial_2F_y=-p+q+r-s},
\]
and
\[
\boxed{
\partial_2F_z=p-q+r-s}.
\]

::: {.proof}
For a cellular \(2\)-cell, the boundary coefficient of a \(1\)-cell is the
signed total number of times the attaching word traverses that \(1\)-cell.
Abelianizing the three words in step <1>13 gives the displayed chains.
:::

<1>15. In the ordered bases
\[
(F_x,F_y,F_z)
\]
and
\[
(p,q,r,s),
\]
the matrix of \(\partial_2\) is
\[
\boxed{
M=
\begin{pmatrix}
1&-1&1\\
1&1&-1\\
1&1&1\\
1&-1&-1
\end{pmatrix}}.
\]

::: {.proof}
The columns are the coordinate vectors from step <1>14.
:::

<1>16. The three columns of \(M\) are linearly independent over
\(\mathbb Z\).

::: {.proof}
The \(3\times3\) minor using the first three rows is
\[
\det
\begin{pmatrix}
1&-1&1\\
1&1&-1\\
1&1&1
\end{pmatrix}
=
4\ne0.
\]
Thus the columns are linearly independent over \(\mathbb Q\), hence also
over \(\mathbb Z\).
:::

<1>17. Therefore
\[
\boxed{\ker\partial_2=0}.
\]

::: {.proof}
The domain of \(\partial_2\) is free of rank \(3\), and step <1>16 says the
three images of its basis vectors are independent.
:::

<1>18. Since
\[
\partial_2\partial_3=0,
\]
one has
\[
\boxed{\partial_3=0}.
\]

::: {.proof}
The image of \(\partial_3\) lies in
\[
\ker\partial_2,
\]
which is zero by step <1>17.
:::

<1>19. Hence
\[
\boxed{H_3(X)\cong\mathbb Z}.
\]

::: {.proof}
There are no \(4\)-cells, so
\[
H_3(X)
=
\ker\partial_3
=
\mathbb Z
\]
by step <1>18.
:::

<1>20. Also
\[
\boxed{H_2(X)=0}.
\]

::: {.proof}
By definition,
\[
H_2(X)
=
\ker\partial_2/\operatorname{im}\partial_3.
\]
Both groups are zero by steps <1>17--<1>18.
:::

<1>21. The kernel of \(\partial_1\) consists of
\[
\boxed{
\{(x_p,x_q,x_r,x_s)\in\mathbb Z^4:
x_p+x_q-x_r-x_s=0\}}.
\]

::: {.proof}
This is step <1>11.
:::

<1>22. A basis for \(\ker\partial_1\) is
\[
\boxed{
u_1=(1,0,0,1),\quad
u_2=(0,1,0,1),\quad
u_3=(0,0,1,-1)}.
\]

::: {.proof}
Each vector satisfies the equation in step <1>21. Conversely, if
\[
x_p+x_q-x_r-x_s=0,
\]
then
\[
x_s=x_p+x_q-x_r,
\]
so
\[
(x_p,x_q,x_r,x_s)
=
x_pu_1+x_qu_2+x_ru_3.
\]
:::

<1>23. In the basis \(u_1,u_2,u_3\), the three generators of
\(\operatorname{im}\partial_2\) have coordinate columns
\[
\boxed{
N=
\begin{pmatrix}
1&-1&1\\
1&1&-1\\
1&1&1
\end{pmatrix}}.
\]

::: {.proof}
For
\[
\partial_2F_x=(1,1,1,1),
\]
the coordinates in the basis of step <1>22 are \((1,1,1)\).

For
\[
\partial_2F_y=(-1,1,1,-1),
\]
the coordinates are \((-1,1,1)\).

For
\[
\partial_2F_z=(1,-1,1,-1),
\]
the coordinates are \((1,-1,1)\).
These are the columns of \(N\).
:::

<1>24. The determinant of \(N\) is
\[
\boxed{\det N=4}.
\]

::: {.proof}
A direct expansion gives
\[
\det
\begin{pmatrix}
1&-1&1\\
1&1&-1\\
1&1&1
\end{pmatrix}
=
4.
\]
:::

<1>25. The greatest common divisor of all entries of \(N\) is \(1\), and the
greatest common divisor of its \(2\times2\) minors is \(2\).

::: {.proof}
The entries are all \(\pm1\), so their gcd is \(1\). Every \(2\times2\)
minor is even; for example,
\[
\det
\begin{pmatrix}
1&-1\\
1&1
\end{pmatrix}
=
2,
\]
so the gcd of all \(2\times2\) minors is exactly \(2\).
:::

<1>26. Therefore the Smith normal form of \(N\) is
\[
\boxed{\operatorname{diag}(1,2,2)}.
\]

::: {.proof}
For a full-rank \(3\times3\) integer matrix with Smith invariants
\[
d_1\mid d_2\mid d_3,
\]
one has:
\[
d_1=\gcd(\text{entries}),
\]
\[
d_1d_2=\gcd(\text{\(2\times2\) minors}),
\]
and
\[
d_1d_2d_3=|\det N|.
\]
By steps <1>24--<1>25,
\[
d_1=1,\qquad
d_1d_2=2,\qquad
d_1d_2d_3=4.
\]
Hence
\[
(d_1,d_2,d_3)=(1,2,2).
\]
:::

<1>27. Consequently,
\[
\boxed{
H_1(X)
=
\ker\partial_1/\operatorname{im}\partial_2
\cong
\mathbb Z/2\oplus\mathbb Z/2}.
\]

::: {.proof}
In the basis of step <1>22, the inclusion of
\[
\operatorname{im}\partial_2
\]
into
\[
\ker\partial_1\cong\mathbb Z^3
\]
is represented by \(N\). Step <1>26 gives the quotient
\[
\mathbb Z^3/
N\mathbb Z^3
\cong
\mathbb Z/1\oplus\mathbb Z/2\oplus\mathbb Z/2.
\]
Discard the trivial factor.
:::

<1>28. Thus the simplicial homology groups of the \(\Delta\)-complex from
step <1>8 are
\[
\boxed{
H_n^{\mathrm{simpl}}(X)
\cong
\begin{cases}
\mathbb Z,&n=0,3,\\
\mathbb Z/2\oplus\mathbb Z/2,&n=1,\\
0,&n=2\text{ or }n>3.
\end{cases}}
\]

::: {.proof}
Steps <1>12, <1>19, <1>20, and <1>27 compute the homology groups of the
finite CW structure on the same space. The \(\Delta\)-complex of step <1>8
is a subdivision of this structure, and simplicial homology of a
\(\Delta\)-complex agrees with the homology of the underlying space.
Therefore the same groups are the requested simplicial homology groups.
:::

<1>29. The result is consistent with the fundamental-group computation
\[
\pi_1(X)\cong Q_8
\]
from PP.2, since
\[
Q_8^{\mathrm{ab}}
\cong
\mathbb Z/2\oplus\mathbb Z/2.
\]

::: {.proof}
The commutator subgroup of \(Q_8\) is
\[
\{\pm1\},
\]
and
\[
Q_8/\{\pm1\}
\cong
\mathbb Z/2\oplus\mathbb Z/2.
\]
This matches step <1>27 and the general identity
\[
H_1(X;\mathbb Z)\cong\pi_1(X)^{\mathrm{ab}}.
\]
:::

<1>30. Q.E.D.

::: {.proof}
Steps <1>1--<1>8 describe the requested \(\Delta\)-complex, and step <1>28
gives all simplicial homology groups.
:::
:::
