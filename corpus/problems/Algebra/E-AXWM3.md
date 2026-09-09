---
schema: qual/card@1
id: E-AXWM3
kind: problem
title: Galois group of $x^{n}-1$ over $\mathbb{Q}$ is abelian
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Roots of Unity
  - Abelian Groups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
24. Prove that the Galois group of the polynomial $x^{n}-1$ over $\mathbb{Q}$ is abelian.
:::


::: {.solution}
Let $\zeta_n$ be a primitive $n$th root of unity.

<1>1. The splitting field of $x^n-1$ over $\mathbb{Q}$ is $K=\mathbb{Q}(\zeta_n)$.
::: {.proof}
Every $n$th root of unity has the form $\zeta_n^j$, so all roots of $x^n-1$ lie in $\mathbb{Q}(\zeta_n)$. Conversely, any splitting field contains a primitive $n$th root of unity, hence contains $\mathbb{Q}(\zeta_n)$. Therefore this is the splitting field.
:::

<1>2. For every $\sigma\in\operatorname{Gal}(K/\mathbb{Q})$, there is a unique class
\[
a_\sigma\in(\mathbb{Z}/n\mathbb{Z})^\times
\]
such that
\[
\sigma(\zeta_n)=\zeta_n^{a_\sigma}.
\]
::: {.proof}
An automorphism preserves multiplicative order, so $\sigma(\zeta_n)$ is again a primitive $n$th root of unity. The primitive $n$th roots are exactly $\zeta_n^a$ with $\gcd(a,n)=1$, and the exponent is unique modulo $n$.
:::

<1>3. The map
\[
\Phi:\operatorname{Gal}(K/\mathbb{Q})\longrightarrow(\mathbb{Z}/n\mathbb{Z})^\times,
\qquad
\Phi(\sigma)=a_\sigma,
\]
is an injective group homomorphism.
::: {.proof}
If $\sigma,\tau\in\operatorname{Gal}(K/\mathbb{Q})$, then
\[
(\sigma\tau)(\zeta_n)
=\sigma(\zeta_n^{a_\tau})
=\sigma(\zeta_n)^{a_\tau}
=\zeta_n^{a_\sigma a_\tau},
\]
so $a_{\sigma\tau}\equiv a_\sigma a_\tau\pmod n$. Thus $\Phi$ is a homomorphism. If $\Phi(\sigma)=1$, then $\sigma(\zeta_n)=\zeta_n$; since $K=\mathbb{Q}(\zeta_n)$ and $\sigma$ fixes $\mathbb{Q}$, this forces $\sigma=1$. Hence $\Phi$ is injective.
:::

<1>4. Therefore the Galois group of $x^n-1$ over $\mathbb{Q}$ is abelian.
::: {.proof}
The group $(\mathbb{Z}/n\mathbb{Z})^\times$ is abelian. By <1>3, the Galois group is isomorphic to a subgroup of this abelian group, hence is abelian.
:::
:::
