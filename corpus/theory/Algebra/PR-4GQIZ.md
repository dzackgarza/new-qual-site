---
schema: qual/card@1
id: PR-4GQIZ
kind: proposition
title: Equivalent conditions for an operator to have a cyclic vector
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

- $V \cong k[x]/\gens{\min_T}$ as $k[x]$-modules.

- $V$ admits a cyclic vector: there is $v \in V$ such that $v, Tv, T^2v, \ldots$ span $V$. For such $v$, $\min_T$ is the monic polynomial $p$ of least degree with $p(T)v = 0$.

- $V$ is a [[D-HY7UU|cyclic]] $k[x]$-module. Its annihilator is then the ideal $\gens{\min_T}$.

- The matrix of $T$ in some basis of $V$ is the [[D-HJR7M|companion matrix]] $C_{\min_T}$.

- $\min_T(x) = \det(xI - T)$, the monic [[D-QFYAC|characteristic polynomial]] of $T$.

- $V$ has exactly one [[FD-JTWOB|invariant factor]] as a $k[x]$-module.

- The [[FD-XT6HD|rational canonical form]] of $T$ has a single block.
:::
