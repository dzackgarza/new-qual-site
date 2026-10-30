---
schema: qual/card@1
id: P-UWALG07-7
kind: problem
title: Symplectic bases and the dimension of isotropic subspaces
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Bilinear Forms
relations: []
review: draft
---

::: {.problem}
Let $V$ be a vector space over a field $k$ that is not of characteristic two.
Let $\omega:V\times V\to k$ be a non-degenerate skew-symmetric bilinear form, i.e., $\omega(x,y)=-\omega(y,x)$ for all $x,y\in V$, and if $x\neq0$ there is a $y$ such that $\omega(x,y)\neq0$.

(a) Show that there exists a basis $e_1,\ldots,e_n,f_1,\ldots,f_n$ of $V$ such that $\omega(e_i,e_j)=\omega(f_i,f_j)=0$ and $\omega(e_i,f_j)=\delta_{ij}$ for all $i,j$.
(In particular $\dim V=2n$ is even.)

(b) We say a subspace $W\subset V$ is *isotropic* if $\omega(w_1,w_2)=0$ for all $w_1,w_2\in W$.
Show that the dimension of an isotropic subspace is at most $\frac12\dim V$.
:::
