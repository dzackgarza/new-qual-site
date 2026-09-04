---
schema: qual/card@1
id: P-B3VM7
kind: problem
title: Lefschetz fixed-point theorem for finite simplicial complexes, and the case
  $X=S^n$
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Degree
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
---

::: problem
a. State the **Lefschetz Fixed Point Theorem** for a finite simplicial complex $X$.

b. Use degree theory to prove this theorem in case $X = S^n$.
:::


::: {.solution}
<1>1. Let $X$ be a finite simplicial complex and $f:X\to X$ a continuous map.
Its Lefschetz number is
\[
L(f)
=
\sum_{q\ge0}(-1)^q
\operatorname{tr}\left(
f_*:H_q(X;\QQ)\to H_q(X;\QQ)
\right).
\]
The Lefschetz fixed-point theorem states that
\[
L(f)\ne0
\quad\Longrightarrow\quad
f\text{ has a fixed point}.
\]
::: {.proof}
Because $X$ is a finite simplicial complex, each rational homology group is finite-dimensional and vanishes in sufficiently large degree, so the displayed sum and traces are well-defined.
The implication is the Lefschetz fixed-point theorem requested in part (a).
:::

<1>2. For $n\ge1$ and a continuous map $f:S^n\to S^n$,
\[
L(f)=1+(-1)^n\deg(f).
\]
::: {.proof}
The only nonzero rational homology groups of $S^n$ are
\[
H_0(S^n;\QQ)\cong\QQ,
\qquad
H_n(S^n;\QQ)\cong\QQ.
\]
Since $S^n$ is connected, $f_*$ acts as the identity on $H_0$, so its trace there is $1$.
By definition of degree, $f_*$ acts on $H_n(S^n;\QQ)$ as multiplication by $\deg(f)$, so its trace there is $\deg(f)$.
Substitution into <1>1 gives
\[
L(f)=1+(-1)^n\deg(f).
\]
:::

<1>3. If $f:S^n\to S^n$ has no fixed point, then $f$ is homotopic to the antipodal map
\[
A(x)=-x.
\]
::: {.proof}
Regard $S^n$ as the unit sphere in $\RR^{n+1}$ and define
\[
H(x,t)
=
\frac{(1-t)f(x)-tx}
{\lVert(1-t)f(x)-tx\rVert},
\qquad
0\le t\le1.
\]
Suppose the denominator vanished for some $(x,t)$.
Then
\[
(1-t)f(x)=tx.
\]
Taking norms gives $1-t=t$, hence $t=1/2$, and then the vector equality gives $f(x)=x$, contradicting the assumption that $f$ has no fixed point.
Thus $H$ is well-defined and continuous.
Moreover
\[
H(x,0)=f(x),
\qquad
H(x,1)=-x=A(x),
\]
so $f\simeq A$.
:::

<1>4. The antipodal map $A:S^n\to S^n$ has degree
\[
\deg(A)=(-1)^{n+1}.
\]
::: {.proof}
The antipodal map is the restriction to the unit sphere of the linear automorphism
\[
-I:\RR^{n+1}\to\RR^{n+1}.
\]
An invertible linear map induces on the oriented boundary sphere a map whose degree is the sign of its determinant.
Since
\[
\det(-I)=(-1)^{n+1},
\]
one gets
\[
\deg(A)=(-1)^{n+1}.
\]
:::

<1>5. If $f:S^n\to S^n$ has no fixed point, then $L(f)=0$.
::: {.proof}
By <1>3 and homotopy invariance of degree,
\[
\deg(f)=\deg(A).
\]
Using <1>4 and then <1>2,
\[
L(f)
=
1+(-1)^n(-1)^{n+1}
=
1-1
=
0.
\]
:::

<1>6. Therefore the Lefschetz fixed-point theorem holds for $S^n$.
::: {.proof}
Step <1>5 proves the contrapositive:
if $f$ has no fixed point, then $L(f)=0$.
Hence
\[
L(f)\ne0
\quad\Longrightarrow\quad
f\text{ has a fixed point}.
\]
This is exactly the theorem in the case $X=S^n$.
:::

<1>7. The case $n=0$ also satisfies the theorem.
::: {.proof}
The space $S^0$ consists of two points.
A fixed-point-free self-map must interchange them, so its induced map on
\[
H_0(S^0;\QQ)\cong\QQ^2
\]
is the transposition matrix, whose trace is $0$.
Thus again a fixed-point-free map has Lefschetz number $0$.
:::
:::
