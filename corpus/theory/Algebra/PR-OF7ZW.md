---
schema: qual/card@1
id: PR-OF7ZW
kind: proposition
title: Equivalent conditions for a finite-dimensional linear operator to be cyclic
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Rational Canonical Form
  - Structure Theorem
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field, let $V$ be a $k$-vector space with $0<\dim_k V<\infty$, and let $T\colon V\to V$ be $k$-linear.
Regard $V$ as a $k[x]$-module with $x$ acting by $T$.
The following are equivalent:

- The [[D-GK5SF|minimal polynomial]] of $T$ equals the monic [[D-QFYAC|characteristic polynomial]] $\det(x\id_V-T)$.

- The invariant factor decomposition of the $k[x]$-module $V$ has exactly one invariant factor.

- The [[FD-XT6HD|rational canonical form]] of $T$ consists of a single block.

- There is a basis of $V$ in which the matrix of $T$ is a [[D-HJR7M|companion matrix]].

- There exists $v\in V$ with $\spanof_k\theset{T^j v \suchthat j\geq 0} = V$.
:::

::: {.example}
If $T$ has $\dim_k V$ distinct eigenvalues in $k$, then $T$ satisfies these conditions, but the converse fails.
The characteristic polynomial is then a product of distinct linear factors, each of which divides the minimal polynomial, so the two polynomials are equal.
For the converse, let $n=\dim_k V\geq 2$ and let $T$ have matrix the Jordan block $J_n(\lambda)$ for some $\lambda\in k$.
Its minimal and characteristic polynomials are both $(x-\lambda)^n$, but $\lambda$ is its only eigenvalue.
:::
