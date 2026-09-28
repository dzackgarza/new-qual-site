---
schema: qual/card@1
id: P-WDQSY
kind: problem
title: Galois group of $x^n-1$ over $\QQ$
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

::: {.problem}
What is the Galois group of $x^n-1$ over $\QQ$?
:::

::: {.solution}
Let $\zeta_n$ be a primitive $n$th root of unity. The splitting field is
\[
\QQ(\zeta_n).
\]
Every $\QQ$-automorphism is determined by the image of $\zeta_n$, and it must send $\zeta_n$ to another primitive $n$th root,
\[
\zeta_n\longmapsto \zeta_n^a,
\qquad a\in(\ZZ/n\ZZ)^\times.
\]
Conversely, each such $a$ defines an automorphism. Therefore
\[
\operatorname{Gal}(x^n-1/\QQ)
\cong
\operatorname{Gal}(\QQ(\zeta_n)/\QQ)
\cong
(\ZZ/n\ZZ)^\times.
\]
In particular the Galois group is abelian of order $\varphi(n)$.
:::
