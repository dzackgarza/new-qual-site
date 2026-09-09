---
schema: qual/card@1
id: P-TRZ3O
kind: problem
title: $\Aut(\ZZ/p)$, $\Aut((\ZZ/p)^n)$, and $\Aut(\ZZ/n)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Cyclic Groups
  - Matrix Groups
relations: []
review: draft
---

::: problem
Identify
\[
\operatorname{Aut}(\ZZ/p\ZZ),
\qquad
\operatorname{Aut}((\ZZ/p\ZZ)^n),
\qquad
\operatorname{Aut}(\ZZ/n\ZZ).
\]
:::

::: solution
For the additive cyclic group $C_p=\ZZ/p\ZZ$, every automorphism is determined by the image of $1$, which may be any nonzero residue class. Thus
\[
\operatorname{Aut}(\ZZ/p\ZZ)\cong(\ZZ/p\ZZ)^\times.
\]
Since $p$ is prime, this is a cyclic group of order $p-1$.

The group
\[
(\ZZ/p\ZZ)^n
\]
is the additive group of the $n$-dimensional vector space $\FF_p^n$. Its group automorphisms are exactly the invertible $\FF_p$-linear maps, so
\[
\operatorname{Aut}((\ZZ/p\ZZ)^n)\cong GL_n(\FF_p).
\]

Finally, for the additive cyclic group $\ZZ/n\ZZ$, an endomorphism is determined by
\[
1\longmapsto a\pmod n.
\]
It is invertible exactly when $a$ is a unit modulo $n$. Therefore
\[
\operatorname{Aut}(\ZZ/n\ZZ)\cong(\ZZ/n\ZZ)^\times.
\]
:::
