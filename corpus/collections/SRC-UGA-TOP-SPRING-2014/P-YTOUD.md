---
schema: qual/card@1
id: P-YTOUD
kind: problem
title: A map $S^n\to S^n$ has a fixed point unless its degree equals that of the antipodal
  map
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
  date: 2026-09-04
  note: Checked the statement against problem 8 of the official UGA Spring 2014 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Verified the normalized straight-line homotopy from a fixed-point-free map to the antipodal map and the nonvanishing of its denominator.
---

::: problem
Show that a map $S^n \to S^n$ has a fixed point unless its degree is equal to the degree of the antipodal map $a : x \to -x$.
:::

::: {.solution}
<1>1. Let $f:S^n\to S^n$ be fixed-point-free.
For $(x,t)\in S^n\times[0,1]$, define
\[
v(x,t)=(1-t)f(x)-tx.
\]
Then $v(x,t)\ne0$ for every $(x,t)$.
::: {.proof}
Suppose instead that
\[
(1-t)f(x)-tx=0.
\]
The cases $t=0$ and $t=1$ are impossible because $f(x)$ and $x$ are unit vectors.
Hence $0<t<1$ and
\[
(1-t)f(x)=tx.
\]
Taking Euclidean norms and using
\[
\|f(x)\|=\|x\|=1
\]
gives
\[
1-t=t,
\]
so $t=1/2$.
Substituting back gives
\[
f(x)=x,
\]
contrary to the assumption that $f$ has no fixed point.
Thus $v$ never vanishes.
:::

<1>2. The formula
\[
H(x,t)=\frac{(1-t)f(x)-tx}{\|(1-t)f(x)-tx\|}
\]
defines a homotopy from $f$ to the antipodal map
\[
a(x)=-x.
\]
::: {.proof}
By <1>1 the denominator is everywhere nonzero, so $H$ is a well-defined continuous map
\[
H:S^n\times[0,1]\to S^n.
\]
At $t=0$,
\[
H(x,0)=\frac{f(x)}{\|f(x)\|}=f(x),
\]
while at $t=1$,
\[
H(x,1)=\frac{-x}{\|-x\|}=-x=a(x).
\]
Therefore
\[
f\simeq a.
\]
:::

<1>3. Every fixed-point-free map $f:S^n\to S^n$ has the same degree as the antipodal map.
::: {.proof}
Degree is invariant under homotopy.
By <1>2,
\[
f\simeq a,
\]
so
\[
\deg f=\deg a.
\]
:::

<1>4. Consequently, if
\[
\deg f\ne\deg a,
\]
then $f$ has a fixed point.
::: {.proof}
This is the contrapositive of <1>3.
:::

<1>5. In particular,
\[
\deg a=(-1)^{n+1},
\]
so the conclusion can be written as
\[
\boxed{\deg f\ne(-1)^{n+1}\Longrightarrow f\text{ has a fixed point}.}
\]
::: {.proof}
The antipodal map is the restriction to $S^n$ of the linear isomorphism
\[
-I:\mathbb R^{n+1}\to\mathbb R^{n+1}.
\]
The degree of the sphere map induced by an invertible linear map is the sign of its determinant.
Since
\[
\det(-I)=(-1)^{n+1},
\]
the displayed degree formula follows.
:::
:::
