---
order: 69
title: "Algebra qual prep: linear algebra"
---

# Algebra qual prep: linear algebra

## References

[Jordan canonical form exercises (Math 122 homework 8, Spring 2016)](http://www.math.lsa.umich.edu/~jchw/2016Math122Material/Homework8-Math122-Sp2016.pdf)

[Computing a Jordan canonical form: an example](https://empslocal.ex.ac.uk/people/staff/rjchapma/courses/jcf.pdf)

### Jordan canonical form and the minimal and characteristic polynomials

Let $F$ be an algebraically closed field, $A\in \Mat_n(F)$, and $\operatorname{Spec}(A)$ the set of eigenvalues of $A$.
Write $J(d,\lambda)$ for the Jordan block of size $d$ with eigenvalue $\lambda$, and call it a Jordan $\lambda$-block.

1. For $\lambda\in F$, $\lambda\in\operatorname{Spec}(A)$ if and only if the Jordan canonical form of $A$ contains at least one Jordan $\lambda$-block.
2. The characteristic polynomial is $\chi_A(x)=\prod_{\lambda\in\operatorname{Spec}(A)}(x-\lambda)^{s_\lambda}$, where $s_\lambda$ is the sum of the sizes of all Jordan $\lambda$-blocks.
3. The minimal polynomial is $\mu_A(x)=\prod_{\lambda\in\operatorname{Spec}(A)}(x-\lambda)^{m_\lambda}$, where $m_\lambda$ is the maximum size of a Jordan $\lambda$-block.

For $\lambda\in F$ and $k\geq 1$, the number $n_A(k,\lambda)$ of Jordan $\lambda$-blocks of size at least $k$ is
\[
n_A(k,\lambda)=\rank\big((A-\lambda I)^{k-1}\big)-\rank\big((A-\lambda I)^{k}\big).
\]

Let $T$ be a nilpotent operator on an $n$-dimensional vector space $V$ with $T^{n-1}\neq 0$.

1. For $0\leq k\leq n$, $\im T^k=\ker T^{n-k}$.
2. If $v_{n-1}\notin \im T=\ker T^{n-1}$ and $v_i=Tv_{i+1}$ for $n-2\geq i\geq 0$, then $\{v_0,\dots,v_{n-1}\}$ is a Jordan basis for $T$.

## Practice

::: {.example}
Let
\[
A=\begin{bmatrix}1&1&0\\0&1&2\\0&0&3\end{bmatrix}.
\]
The characteristic polynomial is $(3-\lambda)(1-\lambda)^2$, so the eigenvalues are $\lambda_1=3$ and $\lambda_2=1$, with eigenvectors $\mathbf v_1=(1,2,2)$ and $\mathbf v_2=(1,0,0)$.
A generalized eigenvector for $\lambda_2$ is a vector $\mathbf v_3\neq\mathbf 0$ with $(A-\lambda_2I)^2\mathbf v_3=\mathbf 0$ and $(A-\lambda_2 I)\mathbf v_3\neq\mathbf 0$; take $\mathbf v_3=(0,1,0)$, for which $(A-\lambda_2I)\mathbf v_3=\mathbf v_2$.
:::

::: {.example}
Let
\[
A=\begin{bmatrix}1&2&0\\1&1&2\\0&-1&1\end{bmatrix}.
\]
The only eigenvalue is $\lambda=1$, with the single eigenvector $\mathbf v_1=(-2,0,1)$ up to scaling.
Since
\[
(A-I)^2=\begin{bmatrix}2&0&4\\0&0&0\\-1&0&-2\end{bmatrix},
\]
$\mathbf v_2=(0,1,0)$ is a generalized eigenvector, and since $(A-I)^3=\mathbf 0$, $\mathbf v_3=(1,0,0)$ completes a basis of generalized eigenvectors.
:::

::: {.example}
Let
\[
A=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
The only eigenvalue is $\lambda=1$, of algebraic multiplicity $m=2$, and $A$ is in Jordan normal form but not diagonal, so it is not diagonalizable.
The null space of $A-\lambda I$ has dimension $p=1$, so there are $m-p=1$ generalized eigenvectors of rank greater than $1$.
The eigenvector is $\mathbf v_1=(1,0)^T$.
Solving $(A-\lambda I)\mathbf v_2=\mathbf v_1$, that is,
\[
\begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}v_{21}\\v_{22}\end{pmatrix}=\begin{pmatrix}1\\0\end{pmatrix},
\]
gives $v_{22}=1$ with $v_{21}$ unrestricted, so the generalized eigenvectors of rank $2$ are $\mathbf v_2=(a,1)^T$ for scalars $a$.
:::
