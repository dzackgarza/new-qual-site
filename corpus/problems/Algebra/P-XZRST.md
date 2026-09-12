---
schema: qual/card@1
id: P-XZRST
kind: problem
title: Whether $L^1$ has a natural multiplication making it an algebra
classification:
  areas:
  - algebra
  topics:
  - Convolution
  - Algebras
  - Function Spaces
relations: []
review: draft
---

::: problem
Does $L^1$ have a natural multiplication making it an algebra? Distinguish pointwise multiplication on a general measure space from convolution on a locally compact group.
:::

::: {.solution}
There is no single answer for a bare symbol $L^1$: the multiplication depends on the underlying measure-theoretic structure.

<1>1. Pointwise multiplication does not make a general $L^1(X,\mu)$ into an algebra.
If $f,g\in L^1$, the product $fg$ need not lie in $L^1$. For example, on $(0,1)$ with Lebesgue measure,
\[
f(x)=x^{-2/3}
\]
lies in $L^1(0,1)$, but
\[
f(x)^2=x^{-4/3}\notin L^1(0,1).
\]
Thus $L^1(X,\mu)$ is not generally closed under pointwise multiplication.

A standard pointwise algebra is instead
\[
L^1\cap L^\infty,
\]
since
\[
\|fg\|_1\le \|f\|_1\|g\|_\infty.
\]

<1>2. Convolution gives the canonical $L^1$ algebra on a locally compact group.
Let $G$ be a locally compact group with a left Haar measure. For $f,g\in L^1(G)$ define
\[
(f*g)(x)=\int_G f(y)g(y^{-1}x)\,dy.
\]
Then $f*g\in L^1(G)$ and Young's inequality gives
\[
\|f*g\|_1\le \|f\|_1\|g\|_1.
\]
Convolution is associative, so
\[
L^1(G)
\]
is a Banach algebra under convolution.

If $G$ is discrete, this specializes to the usual convolution algebra $\ell^1(G)$. If $G$ is abelian, the convolution algebra is commutative.

Thus a general $L^1$ space has no canonical multiplication from the notation alone, while group structure plus Haar measure supplies the natural convolution product.
:::
