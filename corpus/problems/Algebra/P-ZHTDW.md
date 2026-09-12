---
schema: qual/card@1
id: P-ZHTDW
kind: problem
title: $\Aut((\ZZ/p)^n)$ as a matrix group
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Matrix Groups
  - Finite Fields
relations: []
review: draft
---

::: problem
- Identify $\Aut_\Grp(\bigoplus_{i=1}^n \ZZ/p)$ as a matrix group and determine its size.
:::


::: {.solution}
Write
\[
V=(\ZZ/p)^n\cong \FF_p^n.
\]
Every group endomorphism of the elementary abelian $p$-group $V$ is automatically $\FF_p$-linear, because for $a\in\FF_p$ and $v\in V$,
\[
\phi(av)=\phi(v+\cdots+v)=a\phi(v).
\]
Hence
\[
\End_{\Grp}(V)=\End_{\FF_p}(V)\cong M_n(\FF_p),
\]
and the automorphisms are exactly the invertible linear maps:
\[
\Aut_{\Grp}(V)\cong \GL_n(\FF_p).
\]

To count them, choose the columns of an invertible matrix successively. The first column can be any nonzero vector, giving $p^n-1$ choices. Once $j$ linearly independent columns have been chosen, their span has $p^j$ elements, so the next column has $p^n-p^j$ choices. Therefore
\[
\left|\Aut_{\Grp}\bigl((\ZZ/p)^n\bigr)\right|
=|\GL_n(\FF_p)|
=\prod_{j=0}^{n-1}(p^n-p^j).
\]
:::
