---
schema: qual/card@1
id: P-QEFMC
kind: problem
title: Galois group of $x^n-1$ over $\QQ$ as a function of $n$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Roots of Unity
  - Abelian Groups
relations: []
review: draft
---

::: problem
Compute the Galois group of $x^n-1$ over $\QQ$ as a function of $n$.
:::

::: {.solution}
The roots of $x^n-1$ are the powers of a primitive $n$th root of unity $\zeta_n$, so the splitting field is
\[
\QQ(\zeta_n).
\]
Every $\QQ$-automorphism is determined by the image of $\zeta_n$, which must again be a primitive $n$th root. Hence
\[
\sigma_a(\zeta_n)=\zeta_n^a
\]
for a unique residue class
\[
a\in(\ZZ/n\ZZ)^\times.
\]
Conversely every such $a$ defines an automorphism. Composition satisfies
\[
\sigma_a\sigma_b=\sigma_{ab}.
\]
Therefore
\[
\operatorname{Gal}(\QQ(\zeta_n)/\QQ)
\cong
(\ZZ/n\ZZ)^\times.
\]
In particular the group is abelian and has order $\varphi(n)$.
:::
