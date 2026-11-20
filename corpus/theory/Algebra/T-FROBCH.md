---
schema: qual/card@1
id: T-FROBCH
kind: theorem
title: The Frobenius characteristic map
slogan: 'class functions become symmetric functions, with $\chi^\lambda\mapsto s_\lambda$'
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
  - Character Theory
relations: []
review: draft
---

::: {.theorem}
For $n\geq1$ let $\mathrm{Cl}(S_n)$ be the complex-valued class functions on the symmetric group and $\Lambda^n$ the symmetric functions of degree $n$ in $x_1,x_2,\ldots$, with the Hall inner product, in which the Schur functions are orthonormal.
The Frobenius characteristic is the linear map
$$
\operatorname{ch}\colon\mathrm{Cl}(S_n)\to\Lambda^n,\qquad
\operatorname{ch}(\chi)\coloneqq\sum_{\lambda\vdash n}\frac{\chi(C_\lambda)}{z_\lambda}p_\lambda,
\qquad z_\lambda\coloneqq\prod_{i\geq1}i^{m_i}m_i!,
$$
where $m_i$ is the number of parts of $\lambda$ equal to $i$ and $C_\lambda$ the class of cycle type $\lambda$.
It is an isometry from $\mathrm{Cl}(S_n)$ with the inner product $\frac{1}{n!}\sum_{g\in S_n}\chi(g)\overline{\psi(g)}$, and it sends the irreducible character $\chi^\lambda$ to $s_\lambda$.
:::
