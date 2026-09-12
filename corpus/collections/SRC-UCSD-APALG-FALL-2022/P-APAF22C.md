---
schema: qual/card@1
id: P-APAF22C
kind: problem
title: Approximate rank-nullity for a nearly vanishing unit vector
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $V$ and $W$ be two finite-dimensional real inner product spaces, $\dim V = \dim W = n$, and let $\phi \colon V \to W$ be a linear map.

Suppose there exists a vector $v_0 \in V$, $\|v_0\| = 1$, such that $\|\phi(v_0)\| \leq 10^{-10}$.

Prove the following “approximate rank–nullity” statement: there exists a subspace $W' \subseteq W$ with $\dim W' \leq n - 1$, with the property that
\[
\forall v \in V,\ \|v\| \leq 1:\ \exists w \in W':\ \|\phi(v) - w\| \leq 10^{-10}.
\]

[Hint: you can use the singular value decomposition, or argue directly.]
:::

::: {.solution}
Let
\[
U=v_0^\perp\subseteq V
\]
and define
\[
W'=\phi(U)\subseteq W.
\]

<1>1. The subspace $W'$ has dimension at most $n-1$.
::: {.proof}
Since $\|v_0\|=1$, the vector $v_0$ is nonzero. Therefore its orthogonal complement $U=v_0^\perp$ has codimension one in $V$, so
\[
\dim U=n-1.
\]
The image of a linear map has dimension at most the dimension of its domain, hence
\[
\dim W'=\dim\phi(U)\le \dim U=n-1.
\]
:::

<1>2. Every $v\in V$ has a unique orthogonal decomposition
\[
v=av_0+u,
\qquad u\in U,
\]
where
\[
|a|\le\|v\|.
\]
::: {.proof}
Because $\|v_0\|=1$, take
\[
a=\langle v,v_0\rangle,
\qquad
u=v-av_0.
\]
Then
\[
\langle u,v_0\rangle
=\langle v,v_0\rangle-a\langle v_0,v_0\rangle
=a-a=0,
\]
so $u\in U$. By Cauchy--Schwarz,
\[
|a|=|\langle v,v_0\rangle|
\le\|v\|\,\|v_0\|
=\|v\|.
\]
:::

<1>3. If $\|v\|\le1$, there exists $w\in W'$ such that
\[
\|\phi(v)-w\|\le10^{-10}.
\]
::: {.proof}
Write
\[
v=av_0+u
\]
as in <1>2 and set
\[
w=\phi(u).
\]
Since $u\in U$, one has $w\in W'$. Moreover
\[
\phi(v)-w
=\phi(av_0+u)-\phi(u)
=a\phi(v_0).
\]
Therefore
\[
\|\phi(v)-w\|
=|a|\,\|\phi(v_0)\|
\le \|v\|\,10^{-10}
\le10^{-10}.
\]
:::

<1>4. Thus $W'=\phi(v_0^\perp)$ satisfies the required approximate rank--nullity statement.
::: {.proof}
The dimension bound is <1>1 and the approximation property for every vector in the unit ball is <1>3.
:::
:::
