---
schema: qual/card@1
id: E-HAT-2.1-5
kind: problem
title: Simplicial homology of Klein bottle
classification:
  areas:
  - topology
  topics:
  - Homology
  - Simplicial Homology
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the standard square-with-diagonal Delta-complex, obtaining two independent 2-boundaries whose quotient of C1 is Z plus Z/2.
---

Compute the simplicial homology groups of the Klein bottle using the $\Delta$-complex structure described at the beginning of this section.


::: {.solution}
Use the standard square model of the Klein bottle with all four vertices identified, and draw the diagonal from the lower-left vertex to the upper-right vertex.
Let $a$ be the horizontal edge class, $b$ the vertical edge class, and $c$ the diagonal.
Let $U,L$ denote the two oriented $2$-simplices, with orientations chosen so that
\[
\partial U=a+b-c,
\qquad
\partial L=a-b-c.
\]

<1>1. The simplicial chain complex is
\[
0\longrightarrow
\mathbb Z^2
\xrightarrow{\partial_2}
\mathbb Z^3
\xrightarrow{0}
\mathbb Z
\longrightarrow0,
\]
where, in the ordered bases $(U,L)$ and $(a,b,c)$,
\[
[\partial_2]
=
\begin{pmatrix}
1&1\\
1&-1\\
-1&-1
\end{pmatrix}.
\]
::: {.proof}
There are two triangles, three edge classes, and one vertex.
Thus $C_2=\mathbb Z^2$, $C_1=\mathbb Z^3$, and $C_0=\mathbb Z$.
All edge endpoints are the unique vertex, so $\partial_1=0$.
Tracing the three oriented sides of the two triangles in the square model gives the displayed formulas for $\partial U$ and $\partial L$.
:::

<1>2. The map $\partial_2$ is injective.
::: {.proof}
If
\[
x(a+b-c)+y(a-b-c)=0,
\]
then the $b$-coordinate gives $x-y=0$, while the $a$-coordinate gives $x+y=0$.
Hence $x=y=0$.
:::

<1>3. The quotient
\[
C_1/\operatorname{im}\partial_2
\]
is isomorphic to
\[
\mathbb Z\oplus\mathbb Z/2.
\]
::: {.proof}
The two boundary relations are
\[
a+b-c=0,
\qquad
a-b-c=0.
\]
Subtracting them gives
\[
2b=0.
\]
The first relation then expresses
\[
a=c-b.
\]
Thus the quotient is generated freely by $c$ together with $b$ of order two:
\[
C_1/\operatorname{im}\partial_2
\cong
\langle c\rangle\oplus\langle b\mid2b=0\rangle
\cong
\mathbb Z\oplus\mathbb Z/2.
\]
:::

<1>4. Hence the simplicial homology groups of the Klein bottle are
\[
\boxed{
H_0\cong\mathbb Z,
\qquad
H_1\cong\mathbb Z\oplus\mathbb Z/2,
\qquad
H_k=0\quad(k\ge2).
}
\]
::: {.proof}
Since $\partial_1=0$, connectedness gives $H_0\cong\mathbb Z$ and
\[
H_1=C_1/\operatorname{im}\partial_2,
\]
which is <1>3.
Injectivity of $\partial_2$ gives $H_2=0$, and there are no higher simplices.
:::
:::
