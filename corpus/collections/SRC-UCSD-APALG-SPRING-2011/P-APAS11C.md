---
schema: qual/card@1
id: P-APAS11C
kind: problem
title: Group determinant factorization and the circulant determinant
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: problem
Let $G=\{g_1,\ldots,g_k\}$ be a finite group.
Introduce variables $x_{g_1},\ldots,x_{g_k}$ and consider the $k\times k$ matrix
\[
X=[x_{g_i g_j^{-1}}].
\]
Let
\[
X=\sum_{i=1}^{k} A(g_i)x_{g_i}
\]
so that we can define a map $g_i\mapsto A(g_i)$.

(a) Show that $A$ is the left regular representation of $G$.

(b) Show that
\[
\det(X)=\prod_{\nu=1}^{h}\det\Biggl(\sum_{g\in G}A^{(\nu)}(g)x_g\Biggr)^{n_\nu}
\]
where $A^{(1)},\ldots,A^{(h)}$ are a complete set of representatives of the irreducible representations of $G$ and $n_\nu=\dim(A^{(\nu)})$ for $\nu=1,\ldots,h$.

(c) Use part (b) to show that
\[
\det\begin{bmatrix}
x_0 & x_1 & x_2 & \cdots & x_{n-1} \\
x_{n-1} & x_0 & x_1 & \cdots & x_{n-2} \\
x_{n-2} & x_{n-1} & x_0 & \cdots & x_{n-3} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
x_1 & x_2 & x_3 & \cdots & x_0
\end{bmatrix}
=
\prod_{r=0}^{n-1}\bigl(x_0+\epsilon^r x_1+\epsilon^{2r} x_2+\cdots+\epsilon^{(n-1)r}x_{n-1}\bigr)
\]
where $\epsilon=e^{2\pi i/n}$.
:::

::: solution
**Theorem.**  
With the matrix data in the statement, the conclusions in (a)–(c) hold.

1. For each $g\in G$, define $A(g)$ by
   \[
   A(g)_{ij}=1 \iff g_i g_j^{-1}=g.
   \]
   If $A(g)$ has row $i$ and column $j$ entry $1$, then $g_i=g g_j$.
   For $g,h\in G$ and any $i,j$,
   \[
   (A(g)A(h))_{ij}
   =\sum_{\ell=1}^k A(g)_{i\ell}A(h)_{\ell j}.
   \]
   Exactly one $\ell$ contributes: $\ell$ is determined by $g_\ell=g^{-1}g_i$ and this
   yields
   \[
   (A(g)A(h))_{ij}=1
   \iff g_i g_j^{-1}=gh.
   \]
   Hence $A(g)A(h)=A(gh)$, so $A$ is a homomorphism and each $A(g)$ is a permutation matrix.
   Thus $A$ is the left regular representation.

2. Write
   \[
   X=\sum_{g\in G}x_gA(g)=\rho\!\left(\sum_{g\in G}x_g g\right)
   \]
   where $\rho:\mathbb C[G]\to M_k(\mathbb C)$ is the left regular representation.

3. Over $\mathbb C$, the regular representation decomposes as
   \[
   \rho \cong \bigoplus_{\nu=1}^h n_\nu A^{(\nu)}.
   \]
   So there exists $P\in GL_k(\mathbb C)$ with
   \[
   PXP^{-1}
   \cong
   \operatorname{diag}\left(
   \underbrace{M_1,\dots,M_1}_{n_1},
   \dots,
   \underbrace{M_h,\dots,M_h}_{n_h}
   \right),
   \]
   where
   \[
   M_\nu=\sum_{g\in G}A^{(\nu)}(g)x_g.
   \]
   Taking determinants gives
   \[
   \det(X)=\prod_{\nu=1}^h \det(M_\nu)^{n_\nu}
   =\prod_{\nu=1}^h \det\!\left(\sum_{g\in G}A^{(\nu)}(g)x_g\right)^{n_\nu}.
   \]

4. For (c), let $G=\mathbb Z_n=\{0,\dots,n-1\}$.
   Its irreducible representations are one-dimensional characters
   \[
   A^{(r)}(j)=\epsilon^{rj},\qquad
   \epsilon=e^{2\pi i/n},\ r=0,\dots,n-1.
   \]
   Therefore
   \[
   M_r=\sum_{j=0}^{n-1}\epsilon^{rj}x_j.
   \]
   Since all multiplicities are $n_r=1$, part (3) becomes
   \[
   \det(X)=\prod_{r=0}^{n-1}\sum_{j=0}^{n-1}\epsilon^{rj}x_j,
   \]
   which is exactly the claimed formula for the circulant determinant.
:::
