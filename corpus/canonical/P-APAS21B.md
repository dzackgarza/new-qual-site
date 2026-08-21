---
schema: qual/card@1
id: P-APAS21B
kind: problem
title: Rayleigh min-characterization of $\lambda_n$; $p$-norm of a diagonal matrix
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
solved: false
---

::: problem
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex components, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

(a) Consider any Hermitian $A \in M_n$ with eigenvalues ordered so that $\lambda_n(A) \le \cdots \le \lambda_2(A) \le \lambda_1(A)$. Prove that
\[
\lambda_n = \min_{x \ne 0} \frac{x^H A x}{x^H x}.
\]

(b) Suppose that $D \in M_n$ with $D = \operatorname{diag}(d_1, d_2, \dots, d_n)$. Prove that for all $1 \le p \le \infty$ the $p$-norm of $D$ is given by $\|D\|_p = \max_{1 \le i \le n} |d_i|$.
:::
