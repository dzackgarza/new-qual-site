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

::: problem
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
