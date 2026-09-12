---
schema: qual/card@1
id: P-APAS23B
kind: problem
title: Real eigenvalues of Hermitian matrices; Courant–Fischer; Rayleigh extrema
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
relations: []
review: draft
---

::: problem
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex components, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

Consider a Hermitian matrix $A \in M_n$.

(a) Show that the eigenvalues of $A$ are real.

(b) Assume that the eigenvalues of $A$ are ordered so that $\lambda_n \le \lambda_{n-1} \le \cdots \le \lambda_2 \le \lambda_1$.
State, but do not prove, the Courant–Fischer theorem.

(c) Prove that
\[
\lambda_n = \min_{x^H x = 1} x^H A x,
\quad\text{and}\quad
\lambda_1 = \max_{x^H x = 1} x^H A x.
\]
:::


::: solution
(a) Let $Av=\lambda v$ with $v\ne0$. Since $A=A^H$,
\[
\lambda\,v^Hv=v^HAv=(v^HAv)^*=\overline\lambda\,v^Hv.
\]
Because $v^Hv>0$, it follows that $\lambda=\overline\lambda$, so every eigenvalue is real.

(b) With eigenvalues ordered
\[
\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_n,
\]
the Courant--Fischer theorem states that for $1\le k\le n$,
\[
\lambda_k
=
\max_{\substack{S\le\mathbb C^n\\ \dim S=k}}
\ \min_{\substack{x\in S\\x^Hx=1}}x^HAx
=
\min_{\substack{S\le\mathbb C^n\\ \dim S=n-k+1}}
\ \max_{\substack{x\in S\\x^Hx=1}}x^HAx.
\]

(c) By the spectral theorem, there is an orthonormal eigenbasis $u_1,\ldots,u_n$ with $Au_i=\lambda_i u_i$. Write a unit vector as
\[
x=\sum_{i=1}^n c_i u_i,
\qquad
\sum_{i=1}^n|c_i|^2=1.
\]
Then
\[
x^HAx
=
\sum_{i=1}^n\lambda_i|c_i|^2.
\]
This is a convex combination of the real numbers $\lambda_1,\ldots,\lambda_n$, hence
\[
\lambda_n\le x^HAx\le\lambda_1.
\]
Taking $x=u_n$ gives equality on the left, and taking $x=u_1$ gives equality on the right. Therefore
\[
\boxed{\lambda_n=\min_{x^Hx=1}x^HAx,
\qquad
\lambda_1=\max_{x^Hx=1}x^HAx.}
\]
:::
