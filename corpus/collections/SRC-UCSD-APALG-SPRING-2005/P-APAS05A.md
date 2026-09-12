---
schema: qual/card@1
id: P-APAS05A
kind: problem
title: Skew part map $T(X)=\frac12(X-X^T)$ on $M_n(\mathbb{R})$
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Linear Transformations
relations: []
review: draft
---

::: problem
Let $T\colon M_n(\mathbb{R})\to M_n(\mathbb{R})$ be the transformation such that
\[
T(X) = \frac12\bigl(X - X^T\bigr).
\]

(a) Prove that $T$ is a linear transformation.

(b) Determine the null space of $T$ and find its dimension.

(c) Derive the matrix representation of $T$ in terms of the standard basis for $M_3$.
:::

::: {.solution}
<1>1. The map $T$ is linear.
::: {.proof}
For $X,Y\in M_n(\mathbb R)$ and $a,b\in\mathbb R$,
\[
\begin{aligned}
T(aX+bY)
&=\frac12\bigl(aX+bY-(aX+bY)^T\bigr)\\
&=\frac12\bigl(aX+bY-aX^T-bY^T\bigr)\\
&=aT(X)+bT(Y).
\end{aligned}
\]
:::

<1>2. The null space is the space of symmetric matrices:
\[
\ker T=\{X\in M_n(\mathbb R):X^T=X\}.
\]
Its dimension is
\[
\boxed{\dim\ker T=\frac{n(n+1)}2.}
\]
::: {.proof}
We have
\[
T(X)=0
\iff X-X^T=0
\iff X=X^T.
\]
A symmetric matrix is determined freely by its $n$ diagonal entries and its $n(n-1)/2$ entries above the diagonal. Therefore
\[
\dim\ker T=n+\frac{n(n-1)}2=\frac{n(n+1)}2.
\]
:::

<1>3. For $M_3(\mathbb R)$, use the ordered standard basis
\[
\mathcal B=(E_{11},E_{12},E_{13},E_{21},E_{22},E_{23},E_{31},E_{32},E_{33}).
\]
Then
\[
[T]_{\mathcal B}
=\frac12
\begin{pmatrix}
0&0&0&0&0&0&0&0&0\\
0&1&0&-1&0&0&0&0&0\\
0&0&1&0&0&0&-1&0&0\\
0&-1&0&1&0&0&0&0&0\\
0&0&0&0&0&0&0&0&0\\
0&0&0&0&0&1&0&-1&0\\
0&0&-1&0&0&0&1&0&0\\
0&0&0&0&0&-1&0&1&0\\
0&0&0&0&0&0&0&0&0
\end{pmatrix}.
\]
::: {.proof}
For $i=j$,
\[
T(E_{ii})=0.
\]
For $i\ne j$,
\[
T(E_{ij})=\frac12(E_{ij}-E_{ji}).
\]
Thus, for example,
\[
T(E_{12})=\frac12(E_{12}-E_{21}),
\qquad
T(E_{21})=\frac12(E_{21}-E_{12}),
\]
and similarly for the pairs $(1,3)$ and $(2,3)$. Writing these coordinate vectors as the columns of the matrix in the ordered basis $\mathcal B$ gives exactly the displayed matrix.
:::
:::
