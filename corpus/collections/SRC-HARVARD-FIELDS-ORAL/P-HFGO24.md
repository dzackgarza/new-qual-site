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
Determine the Galois group of $x^8-1$ over $\mathbb Q$.
:::

::: {.solution}
Let $\zeta_8=e^{2\pi i/8}$ be a primitive eighth root of unity.

<1>1. The splitting field of $x^8-1$ over $\mathbb Q$ is $K=\mathbb Q(\zeta_8)$.
::: {.proof}
The roots of $x^8-1$ are exactly $1,\zeta_8,\ldots,\zeta_8^7$, so adjoining $\zeta_8$ adjoins every root. Conversely, every splitting field contains a primitive eighth root, hence contains $\mathbb Q(\zeta_8)$.
:::

<1>2. One has
\[
K=\mathbb Q(i,\sqrt2)
\quad\text{and}\quad
[K:\mathbb Q]=\varphi(8)=4.
\]
::: {.proof}
Since $\zeta_8^2=i$ and $\zeta_8+\zeta_8^{-1}=\sqrt2$, one has $\mathbb Q(i,\sqrt2)\subseteq K$. Conversely,
\[
\zeta_8=\frac{1+i}{\sqrt2}\in\mathbb Q(i,\sqrt2),
\]
so equality holds. The degree is also the degree of the cyclotomic polynomial
\[
\Phi_8(x)=x^4+1,
\]
namely $\varphi(8)=4$.
:::

<1>3. Every $\mathbb Q$-automorphism of $K$ is uniquely determined by
\[
\zeta_8\longmapsto \zeta_8^a,
\qquad a\in(\mathbb Z/8\mathbb Z)^\times,
\]
and every such choice occurs.
::: {.proof}
The conjugates of the primitive eighth root $\zeta_8$ over $\mathbb Q$ are exactly the primitive eighth roots $\zeta_8^a$ with $\gcd(a,8)=1$. Since $K=\mathbb Q(\zeta_8)$, an automorphism is determined by the image of $\zeta_8$, and the standard cyclotomic automorphisms realize all four choices.
:::

<1>4. Hence
\[
\operatorname{Gal}(K/\mathbb Q)
\cong(\mathbb Z/8\mathbb Z)^\times
=\{1,3,5,7\}
\cong C_2\times C_2.
\]
::: {.proof}
Composition corresponds to multiplication of exponents modulo $8$. Each of $3,5,7$ has square $1$ modulo $8$, so every nonidentity element of $(\mathbb Z/8\mathbb Z)^\times$ has order $2$. A group of order $4$ with three nonidentity involutions is the Klein four group $C_2\times C_2$.
:::
:::
