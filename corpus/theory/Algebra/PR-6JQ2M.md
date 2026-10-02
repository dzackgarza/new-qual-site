---
schema: qual/card@1
id: PR-6JQ2M
kind: proposition
title: Automorphisms of powers of a finite cyclic group
slogan: 'Automorphisms of $C_m^n$ are invertible matrices over $\ZZ/m\ZZ$.'
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Abelian Groups
  - Linear Algebra
relations: []
review: draft
---

::: {.proposition}
For $m\geq2$ and $n\geq1$,
$$
\Aut(C_m^n)\cong\GL_n(\ZZ/m\ZZ).
$$
For a prime $p$, this specializes to
$$
\Aut(C_p^n)\cong\GL_n(\FF_p),
$$
and
$$
\abs{\GL_n(\FF_p)}
=\prod_{k=0}^{n-1}(p^n-p^k).
$$
:::

::: {.proof}
Identify $C_m^n$ additively with the free $(\ZZ/m\ZZ)$-module $(\ZZ/m\ZZ)^n$.
Every group homomorphism is automatically $\ZZ$-linear and annihilates $m$, hence is $(\ZZ/m\ZZ)$-linear.
Thus group endomorphisms are exactly $n\times n$ matrices over $\ZZ/m\ZZ$, and the automorphisms are exactly the invertible matrices.
This gives the first isomorphism and its specialization to $m=p$.

For the order formula, an invertible matrix over $\FF_p$ is the same as an ordered basis of $\FF_p^n$.
There are $p^n-1$ choices for the first basis vector, $p^n-p$ choices for the second, and after $k$ linearly independent vectors have been chosen there are $p^n-p^k$ choices for the next.
Multiplying these counts gives
$$
\abs{\GL_n(\FF_p)}
=\prod_{k=0}^{n-1}(p^n-p^k).
$$
:::
