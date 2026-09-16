---
schema: qual/card@1
id: PR-TI6YA
kind: proposition
title: Rational canonical form
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Structure Theorem
  - Matrices
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field and $A\in M_n(k)$, and regard $k^n$ as a $k[x]$-module with $x$ acting by $A$.
Let $r_1\divides r_2\divides\cdots\divides r_m$ be the monic nonconstant invariant factors of this module.
Then $A$ is similar to the block diagonal matrix
$$
\RCF(A)=\diag(C_{r_1},\ldots,C_{r_m}),
$$
where $C_{r_i}$ is the [[D-HJR7M|companion matrix]] of $r_i$, and $\RCF(A)$ is the unique matrix of this form similar to $A$.
:::

::: {.proof}
By the structure theorem for finitely generated modules over the PID $k[x]$, $k^n\cong\bigoplus_{i=1}^m k[x]/(r_i)$ as $k[x]$-modules, with the monic $r_i$ uniquely determined.
On $k[x]/(r_i)$, multiplication by $x$ in the basis $1,x,\ldots,x^{\deg r_i-1}$ has matrix $C_{r_i}$.
Two matrices are similar if and only if the corresponding $k[x]$-modules are isomorphic, so uniqueness of the invariant factors gives uniqueness of $\RCF(A)$.
:::
