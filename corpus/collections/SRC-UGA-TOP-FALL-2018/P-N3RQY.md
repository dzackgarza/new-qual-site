---
schema: qual/card@1
id: P-N3RQY
kind: problem
title: Homology of the unit sphere union the $z$-axis and the $xy$-plane
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 8 of the official UGA Fall 2018 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the Mayer-Vietoris computation using the contractible union of the xy-plane and z-axis and its three-component intersection with S^2.
---

::: problem
Compute the homology of the subset $X\subset\RR^3$ formed as the union of the unit sphere, the $z$-axis, and the $xy$-plane.
:::

::: {.solution}
Let
\[
P=\{(x,y,0):x,y\in\RR\},
\qquad
L=\{(0,0,z):z\in\RR\},
\]
and set
\[
A=P\cup L,
\qquad
B=S^2.
\]
Then $X=A\cup B$.
Choose a CW structure on $X$ in which $A$ and $B$ are subcomplexes, subdividing along the equator and the two poles; equivalently, use small open regular neighborhoods of these subspaces.
Thus the Mayer--Vietoris sequence applies to this decomposition.

<1>1. The space $A$ is contractible.
::: {.proof}
Scalar contraction gives a homotopy
\[
H:A\times[0,1]\longrightarrow A,
\qquad
H(v,t)=(1-t)v.
\]
Both $P$ and $L$ are invariant under scalar multiplication, so $H$ stays inside $A$.
At $t=1$ every point is sent to the origin.
Hence
\[
H_i(A;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,\\
0,&i>0.
\end{cases}
\]
:::

<1>2. The intersection $A\cap B$ is the disjoint union of the equator and the north and south poles:
\[
A\cap B
=E\amalg\{N\}\amalg\{S\},
\qquad
E\cong S^1.
\]
Consequently,
\[
H_i(A\cap B;\ZZ)\cong
\begin{cases}
\ZZ^3,&i=0,\\
\ZZ,&i=1,\\
0,&i\ge2.
\end{cases}
\]
::: {.proof}
The plane $P$ meets the unit sphere in
\[
E=\{(x,y,0):x^2+y^2=1\}\cong S^1,
\]
while the $z$-axis meets it in
\[
N=(0,0,1),
\qquad
S=(0,0,-1).
\]
These three pieces are pairwise disjoint and are exactly the intersection.
The displayed homology follows from the homology of a circle and of a three-component space.
:::

<1>3. One has
\[
H_2(X;\ZZ)\cong\ZZ^2.
\]
::: {.proof}
Since
\[
H_2(A)=0,
\qquad
H_2(B)=H_2(S^2)\cong\ZZ,
\qquad
H_2(A\cap B)=0,
\]
the Mayer--Vietoris sequence contains
\[
0
\longrightarrow
\ZZ
\longrightarrow
H_2(X)
\longrightarrow
\ZZ
\longrightarrow
0,
\]
where the final $\ZZ$ is $H_1(A\cap B)$ and the next group
\[
H_1(A)\oplus H_1(B)
\]
is zero.
Thus $H_2(X)$ is an extension of $\ZZ$ by $\ZZ$.
Because the quotient group $\ZZ$ is free, the short exact sequence splits, so
\[
H_2(X;\ZZ)\cong\ZZ^2.
\]
:::

<1>4. One has
\[
H_1(X;\ZZ)\cong\ZZ^2.
\]
::: {.proof}
The degree-$1$ and degree-$0$ part of the Mayer--Vietoris sequence is
\[
0
\longrightarrow
H_1(X)
\longrightarrow
H_0(A\cap B)
\xrightarrow{\psi}
H_0(A)\oplus H_0(B)
\longrightarrow
H_0(X)
\longrightarrow0.
\]
By <1>1 and connectedness of $B=S^2$,
\[
H_0(A)\oplus H_0(B)\cong\ZZ^2,
\]
whereas <1>2 gives
\[
H_0(A\cap B)\cong\ZZ^3.
\]
Each of the three components $E,N,S$ lies in the unique component of $A$ and in the unique component of $B$.
Hence, up to the conventional sign in the Mayer--Vietoris map,
\[
\psi(a,b,c)=(a+b+c,-a-b-c).
\]
Therefore
\[
\ker\psi
=\{(a,b,c)\in\ZZ^3:a+b+c=0\}
\cong\ZZ^2.
\]
Exactness gives
\[
H_1(X;\ZZ)\cong\ker\psi\cong\ZZ^2.
\]
:::

<1>5. The remaining homology groups are
\[
H_0(X;\ZZ)\cong\ZZ
\]
and
\[
H_i(X;\ZZ)=0
\qquad(i\ge3).
\]
::: {.proof}
The space $X$ is path connected because both $A$ and $B$ are path connected and
\[
A\cap B\neq\varnothing.
\]
Thus $H_0(X)\cong\ZZ$.
For $i\ge3$, the groups
\[
H_i(A),
\qquad
H_i(B),
\qquad
H_{i-1}(A\cap B)
\]
all vanish, so Mayer--Vietoris gives $H_i(X)=0$.
:::

<1>6. Therefore
\[
\boxed{
H_i(X;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,\\
\ZZ^2,&i=1,2,\\
0,&i\ge3.
\end{cases}}
\]
::: {.proof}
Combine <1>3, <1>4, and <1>5.
:::
:::
