---
schema: qual/card@1
id: P-APAS21C
kind: problem
title: SVD; variational characterization of $\sigma_1$; field of values and numerical radius
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Throughout, $M_{m,n}$ denotes the set of $m \times n$ matrices with complex components, $M_n$ denotes the set $M_{m,n}$ with $m = n$, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

(a) State, but do not prove, the singular-value decomposition theorem.

(b) For a given $A \in M_{m,n}$, prove that
\[
\sigma_1(A) = \max_{x,y \ne 0} \frac{|y^H A x|}{\|y\|_2 \|x\|_2},
\]
where $\sigma_1(A)$ is the largest singular value of $A$.

(c) For any $A \in M_n$, define (i) the field of values $F(A)$; (ii) the spectral radius $\rho(A)$; and the numerical radius $\omega(A)$.
Prove that $\rho(A) \le \omega(A) \le \sigma_1(A)$.
:::

::: {.solution}
(a) The singular-value decomposition theorem states that for every $A\in M_{m,n}$ there exist unitary matrices $U\in M_m$ and $V\in M_n$ such that
\[
A=U\Sigma V^H,
\]
where $\Sigma$ is an $m\times n$ diagonal matrix with nonnegative diagonal entries
\[
\sigma_1(A)\ge\sigma_2(A)\ge\cdots\ge0.
\]
These entries are the singular values of $A$.

(b) For nonzero $x$ and $y$, Cauchy--Schwarz gives
\[
|y^HAx|\le \|y\|_2\,\|Ax\|_2
\le \sigma_1(A)\|y\|_2\,\|x\|_2.
\]
Hence the displayed quotient is at most $\sigma_1(A)$.

Let $v_1$ and $u_1$ be right and left singular vectors for $\sigma_1$, normalized to have norm $1$, so that
\[
Av_1=\sigma_1u_1.
\]
Taking $x=v_1$ and $y=u_1$ gives
\[
|u_1^HAv_1|=\sigma_1.
\]
Therefore
\[
\boxed{\sigma_1(A)=\max_{x,y\ne0}
\frac{|y^HAx|}{\|y\|_2\|x\|_2}}.
\]

(c) The field of values is
\[
F(A)=\{x^HAx:\ x\in\mathbb C^n,\ \|x\|_2=1\}.
\]
The spectral radius is
\[
\rho(A)=\max\{|\lambda|:\lambda\in\operatorname{eig}(A)\},
\]
and the numerical radius is
\[
\omega(A)=\max\{|z|:z\in F(A)\}
=
\max_{\|x\|_2=1}|x^HAx|.
\]

If $Ax=\lambda x$ with $\|x\|_2=1$, then
\[
x^HAx=\lambda,
\]
so every eigenvalue belongs to $F(A)$. Hence
\[
\rho(A)\le\omega(A).
\]

For every unit vector $x$,
\[
|x^HAx|\le \|x\|_2\,\|Ax\|_2\le\sigma_1(A).
\]
Taking the maximum over unit vectors gives
\[
\omega(A)\le\sigma_1(A).
\]
Thus
\[
\boxed{\rho(A)\le\omega(A)\le\sigma_1(A)}.
\]
:::
