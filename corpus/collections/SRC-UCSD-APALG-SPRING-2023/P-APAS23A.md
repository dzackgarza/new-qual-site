---
schema: qual/card@1
id: P-APAS23A
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

(a) State, but do not prove, the Schur decomposition theorem.

(b) Let $(\lambda, x)$ be a simple eigenpair of $A \in M_n$ with $x^H x = 1$.

(i) Prove that there exists a nonsingular matrix $\begin{pmatrix} x & X \end{pmatrix}$ with inverse $\begin{pmatrix} y & Y \end{pmatrix}^H$ such that
\[
\begin{pmatrix} y^H \\ Y^H \end{pmatrix}
A
\begin{pmatrix} x & X \end{pmatrix}
=
\begin{pmatrix} \lambda & 0 \\ 0 & M \end{pmatrix},
\]
with $M \in M_{n-1}$.

(ii) Hence prove that the angle $\theta$ between $x$ and $y$ satisfies $\sec \theta = \|y\|_2$.
:::


::: {.solution}
(a) **Schur decomposition.** For every $A\in M_n$ there is a unitary matrix $Q$ and an upper-triangular matrix $T$ such that
\[
Q^HAQ=T.
\]
The diagonal entries of $T$ are the eigenvalues of $A$, counted with algebraic multiplicity.

(b)(i) Since $\lambda$ is a simple eigenvalue, the left eigenspace for $\lambda$ is one-dimensional. Choose a nonzero vector $y$ such that
\[
y^HA=\lambda y^H.
\]
We claim that $y^Hx\ne0$. Indeed, if $y^Hx=0$, then $x\in(\ker(A^H-\overline\lambda I))^\perp=\operatorname{im}(A-\lambda I)$. Thus $x=(A-\lambda I)z$ for some $z$, and since $(A-\lambda I)x=0$, the vector $z$ would generate a Jordan chain of length at least $2$ for $\lambda$, contradicting simplicity of the eigenvalue.

Scale $y$ so that
\[
y^Hx=1.
\]
Let
\[
W=\ker y^H.
\]
Because $y^HA=\lambda y^H$, if $w\in W$ then
\[
y^HAw=\lambda y^Hw=0,
\]
so $W$ is $A$-invariant. Since $y^Hx=1$, we have $x\notin W$, and therefore
\[
\mathbb C^n=\mathbb Cx\oplus W.
\]
Choose a basis of $W$ and place its vectors in the columns of $X$. Then
\[
S=\begin{pmatrix}x&X\end{pmatrix}
\]
is nonsingular. Write
\[
S^{-1}=\begin{pmatrix}y&Y\end{pmatrix}^H
=\begin{pmatrix}y^H\\Y^H\end{pmatrix}.
\]
The first row is indeed $y^H$, because $y^Hx=1$ and $y^HX=0$.

Now
\[
y^HAx=\lambda,\qquad y^HAX=0,\qquad Y^HAx=\lambda Y^Hx=0.
\]
Since $W$ is invariant, $AX=XM$ for a unique $M\in M_{n-1}$. Therefore
\[
\begin{pmatrix} y^H \\ Y^H \end{pmatrix}
A
\begin{pmatrix}x&X\end{pmatrix}
=
\begin{pmatrix}\lambda&0\\0&M\end{pmatrix}.
\]

(ii) For nonzero complex vectors, define the acute angle $\theta$ by
\[
\cos\theta=\frac{|y^Hx|}{\|y\|_2\|x\|_2}.
\]
Here $\|x\|_2=1$ and $y^Hx=1$, so
\[
\cos\theta=\frac1{\|y\|_2}.
\]
Hence
\[
\boxed{\sec\theta=\|y\|_2}.
\]
:::
