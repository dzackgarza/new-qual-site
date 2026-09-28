---
schema: qual/card@1
id: P-APAS21B
kind: problem
title: Rayleigh min-characterization of $\lambda_n$; $p$-norm of a diagonal matrix
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Norms
relations: []
review: draft
---

::: {.problem}
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex components, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

(a) Consider any Hermitian $A \in M_n$ with eigenvalues ordered so that $\lambda_n(A) \le \cdots \le \lambda_2(A) \le \lambda_1(A)$.
Prove that
\[
\lambda_n = \min_{x \ne 0} \frac{x^H A x}{x^H x}.
\]

(b) Suppose that $D \in M_n$ with $D = \operatorname{diag}(d_1, d_2, \dots, d_n)$.
Prove that for all $1 \le p \le \infty$ the $p$-norm of $D$ is given by $\|D\|_p = \max_{1 \le i \le n} |d_i|$.
:::

::: {.solution}
(a) Since $A$ is Hermitian, there is an orthonormal basis $u_1,\ldots,u_n$ of eigenvectors with
\[
Au_i=\lambda_i u_i.
\]
Write a nonzero vector as $x=\sum_i c_i u_i$. Then
\[
\frac{x^HAx}{x^Hx}
=
\frac{\sum_i \lambda_i|c_i|^2}{\sum_i |c_i|^2}.
\]
This is a weighted average of the real numbers $\lambda_i$, so it is at least $\lambda_n$. Equality is attained for any nonzero vector in the $\lambda_n$-eigenspace, for instance $x=u_n$. Hence
\[
\boxed{\lambda_n=\min_{x\ne0}\frac{x^HAx}{x^Hx}}.
\]

(b) Let
\[
M=\max_i |d_i|.
\]
For $1\le p<\infty$ and any $x=(x_1,\ldots,x_n)^T$,
\[
\|Dx\|_p^p
=
\sum_{i=1}^n |d_i x_i|^p
\le
M^p\sum_{i=1}^n |x_i|^p
=M^p\|x\|_p^p.
\]
Thus $\|D\|_p\le M$. If $j$ satisfies $|d_j|=M$, then for the standard basis vector $e_j$,
\[
\frac{\|De_j\|_p}{\|e_j\|_p}=|d_j|=M,
\]
so $\|D\|_p=M$.

For $p=\infty$,
\[
\|Dx\|_\infty
=
\max_i |d_i x_i|
\le
M\max_i|x_i|
=M\|x\|_\infty,
\]
and again equality is attained at $e_j$. Therefore for every $1\le p\le\infty$,
\[
\boxed{\|D\|_p=\max_{1\le i\le n}|d_i|}.
\]
:::
