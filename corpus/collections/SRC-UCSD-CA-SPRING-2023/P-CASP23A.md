---
schema: qual/card@1
id: P-CASP23A
kind: problem
title: "Power series with radius of convergence 1: divergence, absolute convergence, singularities, and nonnegative coefficients"
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Radius of Convergence
  - Analytic Continuation
  - Singularities
relations: []
review: draft
---

::: problem
Let $A(z) = \sum_{n=0}^\infty a_n z^n$ be a power series with radius of convergence equal to one.

(a) Give an example where $A(z)$ diverges at each point of $\mathbb{T}$, and explain why.

(b) Give an example where $A(z)$ converges absolutely on $\mathbb{T}$, and explain why.

(c) Prove that $A(z)$ has a singularity on $\mathbb{T}$, i.e. cannot be analytically continued to an open set containing $\overline{\mathbb{D}}$.

(d) Prove that if $A(z)$ has nonnegative coefficients, the point $z = 1$ is a singularity of $A(z)$.

(e) Verify that $A(z) = \sum_{n=0}^\infty z^{n!}$ has radius of convergence one, and that each point of $\mathbb{T}$ is a singularity of $A(z)$.
:::

::: remark
The official Spring 2023 UCSD exam has $A(z)=\sum_{n=0}^\infty z^{n!}$ in
part (e). An earlier transcription of this card incorrectly read
$\sum n!z^n$, which has radius of convergence $0$.
:::

::: solution
(a) Take
\[
A(z)=\sum_{n=0}^\infty z^n.
\]
Its radius of convergence is $1$. At every $|z|=1$, the terms $z^n$ have
modulus $1$ and hence do not tend to $0$, so the series diverges at every
point of $\mathbb T$.

(b) Take
\[
A(z)=\sum_{n=1}^\infty \frac{z^n}{n^2}.
\]
The root test gives radius $1$, while on $|z|=1$ the series converges
absolutely because $\sum n^{-2}<\infty$.

(c) If $A$ admitted an analytic continuation to an open neighborhood of
$\overline{\mathbb D}$, compactness of $\overline{\mathbb D}$ would give
$\varepsilon>0$ such that the continuation is holomorphic on
$|z|<1+\varepsilon$. Its Taylor series at $0$ would then have radius of
convergence at least $1+\varepsilon$, contradicting the assumed radius $1$.
Thus at least one point of $\mathbb T$ is a singularity.

(d) This is Pringsheim's theorem in this special case. Suppose, to the
contrary, that $A$ were holomorphic in a neighborhood of $1$. Choose
$\delta>0$ such that $A$ is holomorphic on $D(1,2\delta)$, and set
$r=1-\delta$. The function is holomorphic on the union
$\mathbb D\cup D(1,2\delta)$, so its Taylor series about $r$ converges at
$r+\delta=1$ and in fact slightly beyond $1$.

Because $a_n\ge0$, for $k\ge0$ and $0<r<1$,
\[
\frac{A^{(k)}(r)}{k!}
=\sum_{n\ge k}\binom nk a_n r^{n-k}\ge0.
\]
Evaluating the Taylor series about $r$ at a point $r+s>1$ still inside its
disk of convergence and using Tonelli's theorem gives
\[
\sum_{k=0}^\infty \frac{A^{(k)}(r)}{k!}s^k
=\sum_{n=0}^\infty a_n(r+s)^n<\infty.
\]
Hence the original power series converges at a point of modulus $>1$, contrary
to radius $1$. Therefore $z=1$ is singular.

(e) Write
\[
A(z)=\sum_{n=0}^\infty z^{n!}.
\]
As a usual power series, its coefficients are $0$ or $1$, with infinitely many
coefficients equal to $1$, so
\[
\limsup_{m\to\infty}|a_m|^{1/m}=1.
\]
Thus the radius of convergence is $1$. The nonzero exponents satisfy
\[
\frac{(n+1)!}{n!}=n+1\ge2.
\]
By the Hadamard gap theorem, the unit circle is a natural boundary for this
lacunary series. Hence every point of $\mathbb T$ is a singularity.
:::
