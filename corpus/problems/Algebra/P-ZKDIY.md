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
Let $x,y \in \CC$ and consider the matrix

$$M =
\left[\begin{array}{ccc}
     1 & 0 & x \\
     0 & 1 & 0 \\
     y & 0 & 1
\end{array}\right]$$

(a) Show that $[0, 1, 0]^t$ is an eigenvector of $M$.

(b) Compute the rank of $M$ as a function of $x$ and $y$.

(c) Find all values of $x$ and $y$ for which $M$ is diagonalizable.
:::

::: {.solution}
Let $e_1,e_2,e_3$ be the standard basis. The subspace $\langle e_1,e_3\rangle$ is $M$-invariant, and in the ordered basis $(e_1,e_3)$ the restriction of $M$ is
$$
B=\begin{pmatrix}1&x\\ y&1\end{pmatrix},
$$
so $M$ is similar to $[1]\oplus B$.

::: pf

::: pf-step

(a) $e_2=[0,1,0]^t$ is an eigenvector of $M$ with eigenvalue $1$.

::: pf-proof

The second column of $M$ is $e_2$, so $Me_2=e_2$.

:::

:::

::: pf-step

(b) $\rank M=\boxed{3}$ if $xy\ne1$ and $\rank M=\boxed{2}$ if $xy=1$.

::: pf-proof

$\rank M=1+\rank B$ and $\det B=1-xy$. If $xy\ne1$, $B$ is invertible. If $xy=1$, then $x\ne0$, so $B$ is nonzero with determinant $0$ and has rank $1$.

:::

:::

::: pf-step

(c) $M$ is diagonalizable if and only if $\boxed{xy\ne0\text{ or }x=y=0}$.

::: pf-proof

$M$ is diagonalizable exactly when $B$ is. The characteristic polynomial of $B$ is $(t-1)^2-xy$. If $xy\ne0$, its roots $1\pm\sqrt{xy}$ are distinct, so $B$ is diagonalizable. If $x=y=0$, then $M=I_3$. If exactly one of $x,y$ is nonzero, then $B=I+N$ with $N=\begin{pmatrix}0&x\\y&0\end{pmatrix}$ nonzero and $N^2=0$; the only eigenvalue of $B$ is $1$, and $B\ne I$, so $B$ is not diagonalizable.

:::

:::

:::

:::
