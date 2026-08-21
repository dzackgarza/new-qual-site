---
schema: qual/card@1
id: P-APAF04E
kind: problem
title: Group determinant via the regular representation and a circulant evaluation
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
solved: false
---

::: problem
Let $G=\{g_1,\ldots,g_k\}$ be a finite group. Introduce variables $x_{g_1},\ldots,x_{g_k}$ and consider the $k\times k$ matrix
\[
X=\bigl[x_{g_i g_j^{-1}}\bigr].
\]
Let $X=\sum_{i=1}^k A(g_i)x_{g_i}$ so that we can define a map $g_i\mapsto A(g_i)$.

(a) Show that $A$ is the left regular representation of $G$.

(b) Show that
\[
\det(X)=\prod_{\nu=1}^{h}\det\Biggl(\sum_{g\in G}A^{(\nu)}(g)x_g\Biggr)^{n_\nu}
\]
where $A^{(1)},\ldots,A^{(h)}$ are a complete set of representatives of the irreducible representations of $G$ and $n_\nu=\dim(A^{(\nu)})$ for $\nu=1,\ldots,h$.

(c) Use part (b) to show that
\[
\det\begin{bmatrix}
x_0 & x_1 & x_2 & \cdots & x_{n-1}\\
x_{n-1} & x_0 & x_1 & \cdots & x_{n-2}\\
x_{n-2} & x_{n-1} & x_0 & \cdots & x_{n-3}\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
x_1 & x_2 & x_3 & \cdots & x_0
\end{bmatrix}
=\prod_{r=0}^{n-1}\bigl(x_0+\epsilon^r x_1+\epsilon^{2r}x_2+\cdots+\epsilon^{(n-1)r}x_{n-1}\bigr)
\]
where $\epsilon=e^{2\pi i/n}$.
:::
