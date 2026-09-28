---
schema: qual/card@1
id: E-XAHHJ
kind: problem
title: Galois group of $x^p-2$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Roots of Unity
relations: []
review: draft
---

::: {.exercise}
Let $p \in \mathbb{Z}$ be a prime number.
Then describe the elements of the Galois group of the polynomial $x^{p}-2$.
:::

::: {.solution}
Let $\alpha=\sqrt[p]{2}$ and $\zeta=\zeta_p$, and work over $\QQ$.

<1>1. The splitting field is $L=\QQ(\alpha,\zeta)$, and $[L:\QQ]=p(p-1)$.

::: {.proof}
The roots of $x^p-2$ are $\alpha\zeta^a$, $0\le a<p$, so $L=\QQ(\alpha,\zeta)$.
By Eisenstein at $2$, $[\QQ(\alpha):\QQ]=p$, and $[\QQ(\zeta):\QQ]=p-1$.
Both divide $[L:\QQ]$ and are coprime, so $p(p-1)\mid[L:\QQ]$; and $[L:\QQ]\le[\QQ(\alpha):\QQ][\QQ(\zeta):\QQ]=p(p-1)$.
:::

<1>2. The elements of $\Gal(L/\QQ)$ are the $p(p-1)$ automorphisms
$$\sigma_{a,b}\colon\alpha\mapsto\zeta^a\alpha,\qquad\zeta\mapsto\zeta^b,\qquad a\in\ZZ/p\ZZ,\ b\in(\ZZ/p\ZZ)^\times ,$$
and $\sigma_{a,b}\mapsto\begin{pmatrix}b&a\\0&1\end{pmatrix}$ is an isomorphism $\Gal(L/\QQ)\cong\ZZ/p\ZZ\rtimes(\ZZ/p\ZZ)^\times$.

::: {.proof}
An automorphism sends $\alpha$ to a root of $x^p-2$ and $\zeta$ to a primitive $p$th root of unity, so it is some $\sigma_{a,b}$, and it is determined by $(a,b)$ since $L=\QQ(\alpha,\zeta)$.
By step <1>1 there are $p(p-1)$ automorphisms, so every pair $(a,b)$ occurs.
From $\sigma_{a,b}\sigma_{a',b'}(\alpha)=\sigma_{a,b}(\zeta^{a'}\alpha)=\zeta^{ba'+a}\alpha$ and $\sigma_{a,b}\sigma_{a',b'}(\zeta)=\zeta^{bb'}$, composition matches the product of the matrices.
:::
:::

