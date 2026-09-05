---
schema: qual/card@1
id: P-PMBN2
kind: problem
title: Fundamental group of $\RR^3$ minus the $z$-axis and the unit circle in the
  $xy$-plane
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 6 of the official UGA Spring 2008 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Used cylindrical coordinates on the complement of the z-axis. They identify
    the requested complement with S^1 times a punctured open half-plane; the
    latter is homeomorphic to R^2 minus the origin and deformation retracts to
    S^1. Thus the complement deformation retracts to T^2 and has fundamental
    group Z^2.
---

::: problem
Let $L$ be the union of the $z$-axis and the unit circle in the $xy\dash$plane.
Compute $\pi_1 (\RR^3 \backslash L, \ast)$.
:::

::: {.solution}
Write
\[
A=\{(0,0,z):z\in\RR\}
\]
for the $z$-axis and
\[
C=\{(x,y,0):x^2+y^2=1\}
\]
for the unit circle, so $L=A\cup C$.

<1>1. There is a homeomorphism
\[
\RR^3\setminus A
\cong
S^1\times(0,\infty)\times\RR
\]
under which $C$ corresponds to
\[
S^1\times\{(1,0)\}.
\]
::: {.proof}
For $(x,y,z)\notin A$, put
\[
r=\sqrt{x^2+y^2}>0,
\qquad
u=\frac{x+iy}{r}\in S^1.
\]
Then
\[
\Phi(x,y,z)=(u,r,z)
\]
defines a continuous map
\[
\Phi:\RR^3\setminus A\longrightarrow S^1\times(0,\infty)\times\RR.
\]
Its inverse is
\[
\Phi^{-1}(u,r,z)
=
(r\operatorname{Re}u,r\operatorname{Im}u,z),
\]
which is continuous, so $\Phi$ is a homeomorphism.

A point of $C$ has $r=1$ and $z=0$, while $u$ ranges over all of $S^1$.
Hence
\[
\Phi(C)=S^1\times\{(1,0)\}.
\]
:::

<1>2. Consequently,
\[
\RR^3\setminus L
\cong
S^1\times
\left(((0,\infty)\times\RR)\setminus\{(1,0)\}\right).
\]
::: {.proof}
Since $L=A\cup C$,
\[
\RR^3\setminus L
=
(\RR^3\setminus A)\setminus C.
\]
Apply the homeomorphism from <1>1 and remove its image of $C$.
:::

<1>3. The space
\[
((0,\infty)\times\RR)\setminus\{(1,0)\}
\]
deformation retracts onto a circle.
::: {.proof}
The map
\[
h:(0,\infty)\times\RR\longrightarrow\RR^2,
\qquad
h(r,z)=(\log r,z),
\]
is a homeomorphism with inverse
\[
h^{-1}(s,z)=(e^s,z).
\]
It sends $(1,0)$ to $(0,0)$.
Hence it restricts to a homeomorphism
\[
((0,\infty)\times\RR)\setminus\{(1,0)\}
\cong
\RR^2\setminus\{0\}.
\]

The punctured plane strongly deformation retracts onto the unit circle by
\[
H(v,t)
=
\left((1-t)+\frac{t}{\lVert v\rVert}\right)v,
\qquad
v\in\RR^2\setminus\{0\},\quad 0\le t\le1.
\]
Therefore the stated space deformation retracts onto $S^1$.
:::

<1>4. The complement $\RR^3\setminus L$ deformation retracts onto the torus $S^1\times S^1$.
::: {.proof}
By <1>2 the complement is a product of $S^1$ with the space considered in <1>3. Taking the product of the identity map of $S^1$ with the deformation retraction from <1>3 gives a deformation retraction
\[
\RR^3\setminus L\simeq S^1\times S^1.
\]
:::

<1>5. Therefore
\[
\pi_1(\RR^3\setminus L,*)\cong\ZZ^2.
\]
::: {.proof}
Fundamental groups are invariant under deformation retraction, and for path-connected spaces
\[
\pi_1(X\times Y)\cong\pi_1(X)\times\pi_1(Y).
\]
Thus <1>4 gives
\[
\pi_1(\RR^3\setminus L,*)
\cong
\pi_1(S^1\times S^1)
\cong
\pi_1(S^1)\times\pi_1(S^1)
\cong
\ZZ\times\ZZ.
\]
Hence
\[
\boxed{\pi_1(\RR^3\setminus L,*)\cong\ZZ^2.}
\]
:::
:::
