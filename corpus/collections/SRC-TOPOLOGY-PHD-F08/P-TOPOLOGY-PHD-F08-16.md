---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-16
kind: problem
title: A deformation-retract exercise in the complement of a circle
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Fundamental Group
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part Two, question 4 of the Topology Ph.D. Qualifying Exam dated January 17, 2009 in assets/attachments/F08phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Used inverse stereographic projection to send the round circle to a great
    circle in S^3. Its complement strongly deformation retracts to the
    complementary great circle. Removing the point at infinity does not change
    pi_1, by van Kampen on a small 3-ball around that point.
---

::: {.problem}
Give the definitions of deformation retract and strong deformation retract for topological spaces.
Compute the fundamental group of $\mathbb R^3-C$ where $C$ denotes the circle $x^2+y^2=1$, $z=0$.
:::

::: {.solution}
<1>1. A subspace $A\subseteq X$ is a deformation retract of $X$ if there is a retraction
\[
r:X\to A,
\qquad
r|_A=\operatorname{id}_A,
\]
such that
\[
i\circ r\simeq\operatorname{id}_X,
\]
where $i:A\hookrightarrow X$ is the inclusion.
It is a strong deformation retract if the homotopy can be chosen to fix $A$ pointwise at every time.
::: {.proof}
Equivalently, a deformation retract is given by a homotopy
\[
H:X\times I\to X
\]
with
\[
H(x,0)=x,
\qquad
H(x,1)=r(x)\in A.
\]
For a strong deformation retract one additionally requires
\[
H(a,t)=a
\]
for every $a\in A$ and $t\in I$.
:::

Let
\[
C=\{(x,y,z)\in\mathbb R^3:x^2+y^2=1,\ z=0\}.
\]

<1>2. Under inverse stereographic projection
\[
\Phi:\mathbb R^3\longrightarrow S^3\setminus\{N\}\subseteq\mathbb R^4,
\]
the circle $C$ becomes the great circle
\[
C_0=\{(x_1,x_2,0,0):x_1^2+x_2^2=1\}.
\]
::: {.proof}
Take
\[
S^3=\{(x_1,x_2,x_3,x_4)\in\mathbb R^4:x_1^2+x_2^2+x_3^2+x_4^2=1\}
\]
and
\[
N=(0,0,0,1).
\]
The inverse stereographic projection is
\[
\Phi(x,y,z)
=\frac{1}{x^2+y^2+z^2+1}
\bigl(2x,2y,2z,x^2+y^2+z^2-1\bigr).
\]
If $(x,y,z)\in C$, then
\[
x^2+y^2+z^2=1
\]
and $z=0$, so
\[
\Phi(x,y,0)=(x,y,0,0).
\]
Thus $\Phi(C)=C_0$.
Consequently
\[
\mathbb R^3\setminus C
\cong
S^3\setminus(C_0\cup\{N\}).
\]
:::

<1>3. The complement
\[
M=S^3\setminus C_0
\]
strongly deformation retracts onto the complementary great circle
\[
D=\{(0,0,x_3,x_4):x_3^2+x_4^2=1\}\cong S^1.
\]
::: {.proof}
Write a point of $S^3$ as
\[
(u,v)\in\mathbb R^2\times\mathbb R^2,
\qquad
\|u\|^2+\|v\|^2=1.
\]
Then
\[
C_0=\{(u,0):\|u\|=1\},
\]
so on $M$ one has $v\ne0$.

Define
\[
H:M\times I\to M
\]
by
\[
H((u,v),t)
=
\frac{((1-t)u,v)}{\sqrt{(1-t)^2\|u\|^2+\|v\|^2}}.
\]
The denominator is nonzero because $v\ne0$.
The second coordinate remains a nonzero scalar multiple of $v$, so the image stays in $M$.
At $t=0$,
\[
H((u,v),0)=(u,v).
\]
At $t=1$,
\[
H((u,v),1)=\left(0,\frac{v}{\|v\|}\right)\in D.
\]
If $(u,v)\in D$, then $u=0$ and $\|v\|=1$, so
\[
H((0,v),t)=(0,v)
\]
for all $t$.
Thus $H$ is a strong deformation retraction of $M$ onto $D$.
:::

<1>4. Therefore
\[
\pi_1(M)\cong\mathbb Z.
\]
::: {.proof}
By <1>3, the inclusion $D\hookrightarrow M$ is a homotopy equivalence.
Hence
\[
\pi_1(M)\cong\pi_1(D)\cong\pi_1(S^1)\cong\mathbb Z.
\]
:::

<1>5. The inclusion
\[
M\setminus\{N\}\hookrightarrow M
\]
induces an isomorphism on fundamental groups.
::: {.proof}
The point $N$ lies in $D$ and is disjoint from $C_0$.
Choose a sufficiently small open $3$-ball
\[
U\subseteq M
\]
around $N$.
Set
\[
V=M\setminus\{N\}.
\]
Then
\[
M=U\cup V,
\qquad
U\cap V=U\setminus\{N\}.
\]
The set $U$ is contractible, while
\[
U\setminus\{N\}\cong B^3\setminus\{0\}
\]
deformation retracts onto $S^2$ and is therefore path-connected and simply connected.

The space $V$ is path-connected.
Indeed, by <1>2 it is homeomorphic to $\mathbb R^3\setminus C$.
Write a point there as $(x,y,z)$ and put
\[
\rho=\sqrt{x^2+y^2}.
\]
If $z\ne0$, the radial path
\[
t\longmapsto((1-t)x,(1-t)y,z)
\]
joins the point to the $z$-axis and never meets $C$, because its third coordinate is nonzero.
If $z=0$ and $\rho<1$, the same radial path stays strictly inside the unit circle and joins the point to the origin.
If $z=0$ and $\rho>1$, first move vertically to $(x,y,1)$, then radially at height $1$ to $(0,0,1)$, and finally down the $z$-axis to the origin.
None of these three path segments meets $C$.
Thus every point can be joined to the origin in $\mathbb R^3\setminus C$, so $V$ is path-connected.

Choose a basepoint in $U\cap V$.
The Seifert--van Kampen theorem gives
\[
\pi_1(M)
\cong
\pi_1(U)*_{\pi_1(U\cap V)}\pi_1(V).
\]
Since
\[
\pi_1(U)=0
\qquad\text{and}\qquad
\pi_1(U\cap V)=0,
\]
the canonical homomorphism
\[
\pi_1(V)\to\pi_1(M)
\]
is an isomorphism.
:::

<1>6. Hence
\[
\boxed{\pi_1(\mathbb R^3\setminus C)\cong\mathbb Z.}
\]
::: {.proof}
By <1>2,
\[
\mathbb R^3\setminus C
\cong
M\setminus\{N\}.
\]
By <1>5,
\[
\pi_1(M\setminus\{N\})\cong\pi_1(M),
\]
and <1>4 computes the latter group as $\mathbb Z$.
:::
:::
