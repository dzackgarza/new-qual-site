---
schema: qual/card@1
id: P-ZKDIY
kind: problem
title: Eigenvector $[0,1,0]^t$, rank, and diagonalizability of $\begin{pmatrix}1&0&x\\0&1&0\\y&0&1\end{pmatrix}$
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Rank and Nullity
relations: []
review: draft
---

::: {.problem}
Let $x,y \in \mathbb{C}$ and consider the matrix

$$M =
\left[\begin{array}{ccc}
     1 & 0 & x \\
     0 & 1 & 0 \\
     y & 0 & 1
\end{array}\right]$$

1.  Show that $[0, 1, 0]^t$ is an eigenvector of $M$.

2.  Compute the rank of $M$ as a function of $x$ and $y$.

3.  Find all values of $x$ and $y$ for which $M$ is diagonalizable.
:::



::: {.solution}
Let $e_2=(0,1,0)^t$. Then
\[
Me_2=e_2,
\]
so $e_2$ is an eigenvector with eigenvalue $1$.

The subspace $\langle e_1,e_3\rangle$ is $M$-invariant, and in the ordered basis $(e_1,e_3)$ the restriction is
\[
B=\begin{pmatrix}1&x\\ y&1\end{pmatrix}.
\]
Thus $M\sim [1]\oplus B$.

<1>1. Rank.
Since
\[
\det B=1-xy,
\]
we have
\[
\rank M=
\begin{cases}
3,&xy\ne1,\\
2,&xy=1.
\end{cases}
\]
Indeed, when $xy=1$, the nonzero matrix $B$ has determinant $0$ and hence rank $1$, while the $e_2$ summand contributes one more dimension.

<1>2. Diagonalizability.
The characteristic polynomial of $B$ is
\[
(t-1)^2-xy.
\]
If $xy\ne0$, its two roots $1\pm\sqrt{xy}$ are distinct, so $B$ and hence $M$ are diagonalizable.

If $xy=0$, then
\[
B=I+N,\qquad N=\begin{pmatrix}0&x\\y&0\end{pmatrix},\qquad N^2=0.
\]
If $x=y=0$, then $N=0$ and $M=I_3$, so $M$ is diagonalizable. If exactly one of $x,y$ is nonzero, then $N\ne0$ is nilpotent, so $B$ has a nontrivial Jordan block for the sole eigenvalue $1$ and is not diagonalizable.

Therefore
\[
\boxed{M\text{ is diagonalizable }\iff xy\ne0\text{ or }(x,y)=(0,0).}
\]
:::
