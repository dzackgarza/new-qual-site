---
schema: qual/card@1
id: P-6LBCE
kind: problem
title: CW structure and cellular homology of two intersecting spheres in $\RR^3$
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked all three parts against problem 7 of the official UGA Spring 2017 topology exam and repaired the malformed display of the two sphere equations.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the four-cap CW structure and the cellular boundary map of rank one, giving H_2 = Z^3, H_1 = 0, and H_0 = Z.
---

::: problem
Let $X = S_1 \cup S_2 \subset \RR^3$ be the union of two spheres of radius 2, one about $(1, 0, 0)$ and the other about $(-1, 0, 0)$, i.e.
\[
\begin{aligned}
S_1 &= \theset{(x,y,z) \mid (x-1)^2+y^2+z^2=4},\\
S_2 &= \theset{(x,y,z) \mid (x+1)^2+y^2+z^2=4}.
\end{aligned}
\]

(a) Give a description of $X$ as a CW complex.

(b) Write out the cellular chain complex of $X$.

(c) Calculate $H_*(X;\ZZ)$.
:::

::: {.solution}
Let
\[
C=S_1\cap S_2.
\]

<1>1. The intersection is the circle
\[
C=\theset{(0,y,z)\in\RR^3\mid y^2+z^2=3}.
\]
::: {.proof}
If $(x,y,z)\in S_1\cap S_2$, subtracting the two sphere equations gives
\[
(x-1)^2-(x+1)^2=0,
\]
so
\[
-4x=0
\]
and therefore $x=0$. Substitution into either sphere equation gives
\[
1+y^2+z^2=4,
\]
hence $y^2+z^2=3$. The converse is immediate, so the displayed circle is exactly the intersection.
:::

<1>2. A CW structure on $X$ has one $0$-cell, one $1$-cell, and four $2$-cells.
::: {.proof}
Choose a point $v\in C$. Give the circle $C$ its standard CW structure with one $0$-cell $v$ and one $1$-cell $e$.

For each $i=1,2$, the circle $C\subset S_i$ separates the sphere $S_i$ into two open disks. Let their closures be
\[
D_{i,+},D_{i,-}.
\]
Each $D_{i,\pm}$ is a closed disk whose boundary is $C$, and its interior is disjoint from the other three disk interiors. Thus
\[
X=C\cup D_{1,+}\cup D_{1,-}\cup D_{2,+}\cup D_{2,-}
\]
is obtained from the $1$-skeleton $C$ by attaching four $2$-cells, each along a homeomorphism
\[
S^1\longrightarrow C.
\]
This is the required CW structure.
:::

<1>3. After orienting the four $2$-cells suitably, the cellular chain complex is
\[
0\longrightarrow\ZZ^4
\xrightarrow{\ d_2\ }
\ZZ
\xrightarrow{\ d_1\ }
\ZZ
\longrightarrow0,
\]
where
\[
d_2(a_1,a_2,a_3,a_4)=a_1+a_2+a_3+a_4,
\qquad
d_1=0.
\]
::: {.proof}
There are four $2$-cells, one $1$-cell, and one $0$-cell, so the cellular chain groups are
\[
C_2(X)\cong\ZZ^4,
\qquad
C_1(X)\cong\ZZ,
\qquad
C_0(X)\cong\ZZ.
\]

The attaching map of each $2$-cell restricts to a homeomorphism from its boundary circle onto $C$. Hence its degree on the quotient
\[
C/C^0\cong S^1
\]
is $\pm1$. Orient each $2$-cell so that this degree is $+1$. The cellular boundary matrix is therefore
\[
d_2=\begin{bmatrix}1&1&1&1\end{bmatrix}.
\]
The unique $1$-cell is a loop with both endpoints at the unique $0$-cell, so $d_1=0$.
:::

<1>4. The homology groups are
\[
\boxed{
H_n(X;\ZZ)\cong
\begin{cases}
\ZZ, & n=0,\\
0, & n=1,\\
\ZZ^3, & n=2,\\
0, & n\ge3.
\end{cases}}
\]
::: {.proof}
The map $d_2:\ZZ^4\to\ZZ$ is surjective, so
\[
H_1(X;\ZZ)=\ker d_1/\operatorname{im}d_2
=\ZZ/\ZZ
=0.
\]
Also
\[
H_2(X;\ZZ)=\ker d_2
=\theset{(a_1,a_2,a_3,a_4)\in\ZZ^4\mid a_1+a_2+a_3+a_4=0}
\cong\ZZ^3.
\]
Finally $d_1=0$ gives
\[
H_0(X;\ZZ)\cong\ZZ,
\]
and there are no cells in dimensions at least $3$.
:::
:::
