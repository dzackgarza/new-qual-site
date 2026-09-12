---
schema: qual/card@1
id: P-DUKEBA14-9
kind: problem
title: Local normal form of a full-rank $C^1$ map
classification:
  areas: [real-analysis]
  topics: [Inverse Function Theorem, Constant Rank Theorem]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Part II, Problem 3 of the preserved Duke Winter 2014 Basic Analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $U\subset\mathbb R^p$ be open and let $f:U\to\mathbb R^n$ be $C^1$. Suppose that for some $x_0\in U$, the derivative $Df_{x_0}$ has rank $p$. Prove that, after suitable local changes of coordinates near $x_0$ and $f(x_0)$, the map $f$ is the standard linear inclusion
\[
u\longmapsto (u,0)\in\mathbb R^p\times\mathbb R^{n-p}.
\]
:::

::: solution
<1>1. Choose $p$ target coordinates with an invertible Jacobian minor.
::: proof
Since $Df_{x_0}$ has rank $p$, some $p\times p$ minor is invertible. After permuting the coordinates of $\mathbb R^n$, assume it is the minor formed by the first $p$ components. Write
\[
F=(f_1,\ldots,f_p):U\to\mathbb R^p.
\]
Then $DF_{x_0}$ is invertible.
:::

<1>2. Use $F$ as a coordinate system on the domain.
::: proof
By the inverse function theorem, there are neighborhoods $V$ of $x_0$ and $W$ of $F(x_0)$ such that
\[
F:V\to W
\]
is a $C^1$ diffeomorphism. Let $H=F^{-1}$.

In the new domain coordinate $u=F(x)$, write
\[
f(H(u))=(u,\phi(u)),
\]
where
\[
\phi(u)=\bigl(f_{p+1}(H(u)),\ldots,f_n(H(u))\bigr).
\]
:::

<1>3. Straighten the graph in the target.
::: proof
Near $(F(x_0),\phi(F(x_0)))=f(x_0)$ define
\[
\Psi(u,v)=(u,v-\phi(u)),
\qquad
(u,v)\in\mathbb R^p\times\mathbb R^{n-p}.
\]
Its derivative has block form
\[
D\Psi=
\begin{pmatrix}
I_p&0\\
-D\phi&I_{n-p}
\end{pmatrix},
\]
which is invertible everywhere. In fact the inverse is explicitly
\[
\Psi^{-1}(u,w)=(u,w+\phi(u)).
\]
Thus $\Psi$ is a local $C^1$ change of target coordinates.
:::

<1>4. Compute the map in the new coordinates.
::: proof
For $u\in W$,
\[
\Psi(f(H(u)))
=\Psi(u,\phi(u))
=(u,0).
\]
Hence, after the domain coordinate change $x\mapsto F(x)$ and the target coordinate change $\Psi$, the map $f$ is exactly the standard linear inclusion
\[
u\mapsto(u,0).
\]
:::
:::
