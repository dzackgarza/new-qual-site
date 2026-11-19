---
schema: qual/card@1
id: PR-4GQIZ
kind: proposition
title: Equivalent conditions for an operator to have a cyclic vector
slogan: 'A linear operator is cyclic exactly when its minimal and characteristic polynomials agree, equivalently its rational form has one block.'
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Minimal and Characteristic Polynomials
  - Modules
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field, let $V$ be a nonzero finite-dimensional $k$-vector space, and let $T\colon V \to V$ be a $k$-linear map.
Make $V$ a $k[x]$-module by $f(x) \cdot v \coloneqq f(T)v$, and let $\min_T(x)$ be the [[D-GK5SF|minimal polynomial]] of $T$.
The following are equivalent:

- $V \cong k[x]/\generators{\min_T}$ as $k[x]$-modules.

- $V$ admits a cyclic vector: there is $v \in V$ such that $v, Tv, T^2v, \ldots$ span $V$. For such $v$, $\min_T$ is the monic polynomial $p$ of least degree with $p(T)v = 0$.

- $V$ is a [[D-HY7UU|cyclic]] $k[x]$-module. Its annihilator is then the ideal $\generators{\min_T}$.

- The matrix of $T$ in some basis of $V$ is the [[D-HJR7M|companion matrix]] $C_{\min_T}$.

- $\min_T(x) = \det(xI - T)$, the monic [[D-QFYAC|characteristic polynomial]] of $T$.

- $V$ has exactly one [[FD-JTWOB|invariant factor]] as a $k[x]$-module.

- The [[FD-XT6HD|rational canonical form]] of $T$ has a single block.
:::

::: {.example}
If $T$ has $\dim_k V$ distinct eigenvalues in $k$, then $T$ satisfies these conditions, but the converse fails.
The characteristic polynomial is then a product of distinct linear factors, each of which divides the minimal polynomial, so the two polynomials are equal.
For the converse, let $n=\dim_k V\geq 2$ and let $T$ have matrix the Jordan block $J_n(\lambda)$ for some $\lambda\in k$.
Its minimal and characteristic polynomials are both $(x-\lambda)^n$, but $\lambda$ is its only eigenvalue.
:::

::: {.proof}
Write $A\coloneqq T$ and $n\coloneqq\dim_k V$, and let $\min_A$ and $\chi_A$ be the minimal and characteristic polynomials of $A$.

If $v$ is a cyclic vector, then $v, Av, \ldots, A^{n-1}v$ is a basis of $V$.
Were $n'\coloneqq\deg\min_A < n$, the relation $\min_A(A)v = 0$ would be a linear dependence among $v, Av, \ldots, A^{n'}v$, which is a contradiction.
Hence $\deg\min_A = n = \deg\chi_A$, and since $\min_A$ divides $\chi_A$ and both are monic, $\min_A = \chi_A$.

Conversely, by the structure theorem $V\cong\bigoplus_{i=1}^m k[x]/\generators{p_i}$ with nonconstant invariant factors $p_1\divides\cdots\divides p_m$, where $\chi_A = \prod_i p_i$ and $\min_A = p_m$.
If $\min_A = \chi_A$, comparing degrees gives $m=1$, so $V\cong k[x]/\generators{p_m}$ is cyclic as a $k[x]$-module.
If $v$ generates $V$, then $V = \theset{f(A)v \st f\in k[x]}$ is spanned by $v, Av, A^2v, \ldots$, and by Cayley--Hamilton by $v, Av, \ldots, A^{n-1}v$, so $v$ is a cyclic vector.
:::
