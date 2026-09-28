---
schema: qual/card@1
id: D-BLV6F
kind: definition
title: Cyclotomic polynomials
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Polynomials
  - Galois Theory
relations: []
review: draft
---

::: {.definition}
Let $n\geq 1$ and $\zeta_n \coloneqq e^{2\pi i/n}\in\CC$.
The \dfn{$n$th cyclotomic polynomial} is the product over the primitive $n$th roots of unity
$$
\Phi_{n}(x) \coloneqq \prod_{\substack{1\leq k\leq n \\ \gcd(k, n)=1}}\left(x- \zeta_n^k\right) \in \CC[x].
$$
:::

::: {.proposition}
Let $n\geq 1$.
Then $\Phi_n(x)$ lies in $\ZZ[x]$, is monic of degree $\phi(n)$, where $\phi$ is [[D-JX3YC|Euler's totient function]], and is [[D-BVMTZ|irreducible]] in $\QQ[x]$.
Moreover, $\Phi_n$ is the unique monic irreducible polynomial in $\QQ[x]$ that divides $x^n - 1$ and does not divide $x^k-1$ for any $1\leq k<n$.
:::
