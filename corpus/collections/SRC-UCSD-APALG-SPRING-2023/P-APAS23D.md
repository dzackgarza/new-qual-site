---
schema: qual/card@1
id: P-APAS23D
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

(c) For any $A \in M_n$, define (i) the field of values $F(A)$; (ii) the spectral radius $\rho(A)$; and (iii) the numerical radius $\omega(A)$.
Prove that $\rho(A) \le \omega(A) \le \sigma_1(A)$.
:::


::: {.solution}
(a) **Singular-value decomposition.** For every $A\in M_{m,n}$ there are unitary matrices $U\in M_m$ and $V\in M_n$ such that
\[
A=U\Sigma V^H,
\]
where $\Sigma$ is diagonal rectangular with nonnegative diagonal entries
\[
\sigma_1(A)\ge\sigma_2(A)\ge\cdots\ge0.
\]
These are the singular values of $A$.

(b) By Cauchy--Schwarz,
\[
|y^HAx|\le \|y\|_2\,\|Ax\|_2
\le \|y\|_2\,\sigma_1(A)\|x\|_2.
\]
Hence
\[
\frac{|y^HAx|}{\|y\|_2\|x\|_2}\le\sigma_1(A).
\]
Let $v_1$ and $u_1$ be right and left singular vectors for $\sigma_1(A)$, normalized so that
\[
Av_1=\sigma_1(A)u_1,
\qquad
\|u_1\|_2=\|v_1\|_2=1.
\]
Then
\[
|u_1^HAv_1|=\sigma_1(A),
\]
so equality is attained. Therefore
\[
\boxed{\sigma_1(A)=\max_{x,y\ne0}
\frac{|y^HAx|}{\|y\|_2\|x\|_2}.}
\]

(c) Define
\[
F(A)=\{x^HAx:x\in\mathbb C^n,\ x^Hx=1\},
\]
\[
\rho(A)=\max\{ |\lambda|:\lambda\in\operatorname{spec}(A)\},
\]
and
\[
\omega(A)=\max\{|z|:z\in F(A)\}
=\max_{x^Hx=1}|x^HAx|.
\]
If $Ax=\lambda x$ and $\|x\|_2=1$, then
\[
\lambda=x^HAx\in F(A).
\]
Thus every eigenvalue lies in the field of values, and so
\[
\rho(A)\le\omega(A).
\]
On the other hand, applying part (b) with $y=x$ and $\|x\|_2=1$ gives
\[
|x^HAx|\le\sigma_1(A).
\]
Taking the maximum over unit vectors gives
\[
\omega(A)\le\sigma_1(A).
\]
Hence
\[
\boxed{\rho(A)\le\omega(A)\le\sigma_1(A).}
\]
:::
