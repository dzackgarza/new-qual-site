---
schema: qual/card@1
id: D-SYMFN
kind: definition
title: Symmetric polynomials and the ring of symmetric functions
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
relations: []
review: draft
---

::: {.definition}
Let $R$ be a commutative ring and let $x_1,\ldots,x_n$ be indeterminates over $R$.
A polynomial $f\in R[x_1,\ldots,x_n]$ is \dfn{symmetric} if $f(x_{\sigma(1)},\ldots,x_{\sigma(n)})=f(x_1,\ldots,x_n)$ for every permutation $\sigma$ of $\{1,\ldots,n\}$.
The symmetric polynomials homogeneous of degree $d$ form the $R$-submodule $\Lambda_n^d\subseteq R[x_1,\ldots,x_n]$, and $\Lambda_n\coloneqq\bigoplus_{d\geq0}\Lambda_n^d$ is the \dfn{ring of symmetric functions in $n$ variables}.

Setting $x_{n+1}=0$ defines a map $\Lambda_{n+1}^d\to\Lambda_n^d$, and it is an isomorphism for $n\geq d$: the monomials of degree $d$ are partitioned into the orbits whose sums are the [[D-MSYMF|monomial symmetric functions]] $m_\lambda$ with $\lambda\vdash d$, which therefore form a basis of $\Lambda_n^d$ for every $n\geq d$, and $m_\lambda$ has at most $d$ parts.
The \dfn{ring of symmetric functions} is $\Lambda\coloneqq\bigoplus_{d\geq0}\Lambda^d$, where $\Lambda^d$ is the common value of $\Lambda_n^d$ for $n\geq d$, and a \dfn{symmetric function of degree $d$} is an element of $\Lambda^d$.
:::
