---
schema: qual/card@1
id: P-APAF25J
kind: problem
title: Isomorphic finite subgroups of $\mathrm{GL}_2(\mathbb{C})$ with different Hilbert series
classification:
  areas:
  - applied-algebra
  topics:
  - Invariant Theory
  - Representation Theory
relations: []
review: draft
---

::: {.problem}
Find two finite matrix groups $G,H\subseteq\mathrm{GL}_2(\mathbb{C})$ such that

- $G$ and $H$ are isomorphic as abstract groups, but

- the Hilbert series of the graded rings $\mathbb{C}[x,y]^G$ and $\mathbb{C}[x,y]^H$ are different.
:::

::: {.solution}
Let
\[
G=\left\langle
\begin{pmatrix}-1&0\\0&1\end{pmatrix}
\right\rangle,
\qquad
H=\left\langle
\begin{pmatrix}-1&0\\0&-1\end{pmatrix}
\right\rangle.
\]
Both groups have order \(2\), so
\[
G\cong C_2\cong H.
\]

<1>1. The invariant ring for \(G\) is
\[
\mathbb C[x,y]^G=\mathbb C[x^2,y].
\]
::: {.proof}
The nontrivial element of \(G\) sends
\[
(x,y)\longmapsto(-x,y).
\]
A monomial \(x^a y^b\) is fixed exactly when \(a\) is even. Hence an invariant polynomial is precisely a polynomial in \(x^2\) and \(y\), giving the stated invariant ring.
:::

<1>2. The Hilbert series of \(\mathbb C[x,y]^G\) is
\[
\operatorname{Hilb}(\mathbb C[x,y]^G;t)
=\frac1{(1-t^2)(1-t)}.
\]
::: {.proof}
The ring \(\mathbb C[x^2,y]\) is a polynomial ring on homogeneous generators of degrees \(2\) and \(1\). Therefore its Hilbert series is the product of the geometric-series factors
\[
\frac1{1-t^2}\cdot\frac1{1-t}.
\]
:::

<1>3. The \(H\)-invariant polynomials are exactly those of even total degree in each homogeneous component.
::: {.proof}
The nontrivial element \(-I\in H\) sends
\[
(x,y)\longmapsto(-x,-y).
\]
Thus a monomial \(x^a y^b\) is multiplied by \((-1)^{a+b}\). It is fixed exactly when \(a+b\) is even. Hence the degree-\(d\) invariant subspace is all of \(\mathbb C[x,y]_d\) when \(d\) is even and is \(0\) when \(d\) is odd.
:::

<1>4. The Hilbert series of \(\mathbb C[x,y]^H\) is
\[
\operatorname{Hilb}(\mathbb C[x,y]^H;t)
=\sum_{m\ge0}(2m+1)t^{2m}
=\frac{1+t^2}{(1-t^2)^2}.
\]
::: {.proof}
The degree \(2m\) homogeneous polynomials in two variables have dimension \(2m+1\), while odd-degree invariants vanish by <1>3. Writing \(u=t^2\),
\[
\sum_{m\ge0}(2m+1)u^m
=2\frac{u}{(1-u)^2}+\frac1{1-u}
=\frac{1+u}{(1-u)^2}.
\]
Substituting \(u=t^2\) gives the formula.
:::

<1>5. The two Hilbert series are different.
::: {.proof}
For example, the coefficient of \(t\) in
\[
\frac1{(1-t^2)(1-t)}
\]
is \(1\), corresponding to the invariant \(y\), while the coefficient of \(t\) in
\[
\frac{1+t^2}{(1-t^2)^2}
\]
is \(0\). Thus the Hilbert series differ even though \(G\cong H\).
:::
:::
