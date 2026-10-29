---
schema: qual/card@1
id: P-HFGO24
kind: problem
title: 'Galois group of $x^8-1$'
classification:
  areas: [algebra]
  topics: [Galois Theory]
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Determine the Galois group of $x^8-1$ over $\QQ$.
:::

::: {.solution}
Let $\zeta_8=e^{2\pi i/8}$ be a primitive eighth root of unity.

::: pf

::: pf-step

The splitting field of $x^8-1$ over $\QQ$ is $K=\QQ(\zeta_8)$.

::: pf-proof

The roots of $x^8-1$ are exactly $1,\zeta_8,\ldots,\zeta_8^7$, so adjoining $\zeta_8$ adjoins every root. Conversely, every splitting field contains a primitive eighth root, hence contains $\QQ(\zeta_8)$.

:::

:::

::: pf-step

One has
\[
K=\QQ(i,\sqrt2)
\quad\text{and}\quad
[K:\QQ]=\varphi(8)=4.
\]

::: pf-proof

Since $\zeta_8^2=i$ and $\zeta_8+\zeta_8^{-1}=\sqrt2$, one has $\QQ(i,\sqrt2)\subseteq K$. Conversely,
\[
\zeta_8=\frac{1+i}{\sqrt2}\in\QQ(i,\sqrt2),
\]
so equality holds. The degree is also the degree of the cyclotomic polynomial
\[
\Phi_8(x)=x^4+1,
\]
namely $\varphi(8)=4$.

:::

:::

::: pf-step

Every $\QQ$-automorphism of $K$ is uniquely determined by
\[
\zeta_8\longmapsto \zeta_8^a,
\qquad a\in(\ZZ/8\ZZ)^\times,
\]
and every such choice occurs.

::: pf-proof

The conjugates of the primitive eighth root $\zeta_8$ over $\QQ$ are exactly the primitive eighth roots $\zeta_8^a$ with $\gcd(a,8)=1$. Since $K=\QQ(\zeta_8)$, an automorphism is determined by the image of $\zeta_8$. The minimal polynomial $\Phi_8(x)=x^4+1$ of $\zeta_8$ has these four roots, and $K/\QQ$ is Galois, so each root $\zeta_8^a$ is the image of $\zeta_8$ under some automorphism.

:::

:::

::: pf-step

Hence
\[
\operatorname{Gal}(K/\QQ)
\cong(\ZZ/8\ZZ)^\times
=\{1,3,5,7\}
\cong C_2\times C_2.
\]

::: pf-proof

Composition corresponds to multiplication of exponents modulo $8$. Each of $3,5,7$ has square $1$ modulo $8$, so every nonidentity element of $(\ZZ/8\ZZ)^\times$ has order $2$. A group of order $4$ with three nonidentity involutions is the Klein four group $C_2\times C_2$.

:::

:::

:::

:::
