---
schema: qual/card@1
id: P-KN75K
kind: problem
title: Degree-$n$ maps $S^2\to S^2$, and which examples must have a fixed point
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fixed Points
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 5 of the official UGA Fall 2018 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the explicit degree calculations and the normalized straight-line homotopy showing every fixed-point-free self-map of S^2 has degree -1.
---

::: problem
For each $n\in\ZZ$, give an example of a map
\[
f_n:S^2\longrightarrow S^2
\]
of degree $n$.
For which $n$ must your example have a fixed point?
:::

::: {.solution}
Identify the oriented sphere $S^2$ with the Riemann sphere
\[
\widehat{\CC}=\CC\cup\{\infty\}.
\]
For $m\ge1$, define
\[
p_m(z)=z^m,
\qquad
p_m(\infty)=\infty.
\]
Let
\[
a:S^2\longrightarrow S^2,
\qquad
a(x)=-x
\]
be the antipodal map.
Define
\[
f_n=
\begin{cases}
p_n,&n>0,\\
c,&n=0,\\
a\circ p_{-n},&n<0,
\end{cases}
\]
where $c$ is any constant map.

<1>1. For every $m\ge1$,
\[
\deg p_m=m.
\]
::: {.proof}
Take the regular value $1\in\CC\subset\widehat{\CC}$.
Its inverse image under $p_m$ consists of the $m$ distinct $m$th roots of unity.
At each such point,
\[
p_m'(z)=mz^{m-1}\neq0.
\]
Multiplication by a nonzero complex number is orientation-preserving as a real linear map, so every preimage contributes local degree $+1$.
Therefore
\[
\deg p_m=m.
\]
:::

<1>2. The antipodal map on $S^2$ has degree $-1$.
::: {.proof}
The antipodal map is the restriction to the unit sphere of the orthogonal linear map
\[
-I:\RR^3\longrightarrow\RR^3.
\]
For an orthogonal linear map, the degree of its restriction to $S^2$ is the sign of its determinant.
Since
\[
\det(-I_3)=-1,
\]
one has
\[
\deg a=-1.
\]
:::

<1>3. The map $f_n$ has degree $n$ for every $n\in\ZZ$.
::: {.proof}
If $n>0$, this is <1>1.
If $n=0$, a constant map has degree $0$.
If $n<0$, multiplicativity of degree under composition gives
\[
\deg f_n
=\deg(a)\deg(p_{-n})
=(-1)(-n)
=n.
\]
:::

<1>4. Every fixed-point-free continuous map
\[
f:S^2\longrightarrow S^2
\]
has degree $-1$.
::: {.proof}
Assume
\[
f(x)\neq x
\qquad
\text{for every }x\in S^2.
\]
Define
\[
H:S^2\times[0,1]\longrightarrow S^2
\]
by
\[
H(x,t)
=
\frac{(1-t)f(x)-tx}
{\lVert(1-t)f(x)-tx\rVert}.
\]
The denominator never vanishes.
Indeed, if
\[
(1-t)f(x)=tx,
\]
then taking norms gives $1-t=t$, hence $t=1/2$, and then the displayed equality gives $f(x)=x$, contradicting the fixed-point-free hypothesis.
Thus $H$ is a continuous homotopy.
At the endpoints,
\[
H(x,0)=f(x),
\qquad
H(x,1)=-x=a(x).
\]
Hence $f\simeq a$, so homotopy invariance of degree and <1>2 give
\[
\deg f=-1.
\]
:::

<1>5. A degree-$n$ self-map of $S^2$ must have a fixed point exactly when $n\neq-1$.
::: {.proof}
By the contrapositive of <1>4, every self-map of degree $n\neq-1$ has a fixed point.
For $n=-1$, our chosen example is
\[
f_{-1}=a\circ p_1=a,
\]
the antipodal map, which has no fixed point because $x=-x$ on $S^2$ would imply $x=0$.
Thus degree $-1$ is the unique degree for which a fixed point is not forced, and the displayed family realizes that exception.
:::
:::
