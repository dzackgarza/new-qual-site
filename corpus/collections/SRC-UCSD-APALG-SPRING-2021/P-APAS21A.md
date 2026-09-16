---
schema: qual/card@1
id: P-APAS21A
kind: problem
title: Schur form; deflating a simple eigenpair and the angle between $x$ and $y$
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex components, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

(a) State, but do not prove, the Schur decomposition theorem for a matrix $A \in M_n$.

(b) Let $(\lambda, x)$ be a simple eigenpair of $A \in M_n$ with $x^H x = 1$.
Prove that there exists a nonsingular matrix $\begin{pmatrix} x & X \end{pmatrix}$ with inverse $\begin{pmatrix} y & Y \end{pmatrix}^H$ such that
\[
\begin{pmatrix} y^H \\ Y^H \end{pmatrix}
A
\begin{pmatrix} x & X \end{pmatrix}
=
\begin{pmatrix} \lambda & 0 \\ 0 & M \end{pmatrix}.
\]

(c) Hence prove that the angle $\theta$ between $x$ and $y$ satisfies $\sec \theta = \|y\|_2$.
:::

::: {.solution}
(a) The Schur decomposition theorem states that for every $A\in M_n$ there is a unitary matrix $Q$ such that $Q^HAQ=T$ is upper triangular. The diagonal entries of $T$ are the eigenvalues of $A$, counted with algebraic multiplicity.

(b) Put $N=A-\lambda I$. Since $\lambda$ is a simple eigenvalue, $\dim\ker N=1$ and the generalized $\lambda$-eigenspace has dimension $1$. Hence
\[
\ker N\cap\operatorname{im}N=\{0\}.
\]
Indeed, if $0\ne v=Nw\in\ker N$, then $N^2w=0$ while $Nw\ne0$, which would give a Jordan chain of length at least $2$ for $\lambda$, contradicting algebraic multiplicity one. Rank-nullity now gives
\[
\mathbb C^n=\ker N\oplus\operatorname{im}N
=\mathbb Cx\oplus\operatorname{im}(A-\lambda I).
\]
The subspace $\operatorname{im}N$ is $A$-invariant, because $A$ commutes with $N$: if $v=Nu$, then $Av=N(Au)\in\operatorname{im}N$.

Choose the columns of $X$ to be a basis of $\operatorname{im}N$. Then $S=(x\;X)$ is nonsingular. Relative to the decomposition above, $A$ acts by $\lambda$ on $\mathbb Cx$ and preserves $\operatorname{im}N$, so for some $(n-1)\times(n-1)$ matrix $M$,
\[
S^{-1}AS=\begin{pmatrix}\lambda&0\\0&M\end{pmatrix}.
\]
Write
\[
S^{-1}=\begin{pmatrix}y^H\\Y^H\end{pmatrix}.
\]
Then $y^Hx=1$ and $y^HX=0$. Since the columns of $X$ span $\operatorname{im}(A-\lambda I)$, the latter identity says
\[
y^H(A-\lambda I)=0,
\]
so $y$ is a left eigenvector for $\lambda$. This gives exactly the required factorization
\[
\begin{pmatrix}y^H\\Y^H\end{pmatrix}
A(x\;X)=\begin{pmatrix}\lambda&0\\0&M\end{pmatrix}.
\]

(c) For complex vectors, define the acute angle by
\[
\cos\theta=\frac{|y^Hx|}{\|y\|_2\,\|x\|_2}.
\]
Here $y^Hx=1$ and $\|x\|_2=1$, so
\[
\cos\theta=\frac1{\|y\|_2}.
\]
Therefore
\[
\boxed{\sec\theta=\|y\|_2}.
\]
:::
