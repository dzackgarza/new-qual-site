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
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
24. Prove that the Galois group of the polynomial $x^{n}-1$ over $Q$ is abelian.
:::


::: {.solution}
<1>1. Let \(\zeta_n\) be a primitive \(n\)-th root of unity and let
\[
K=\mathbb Q(\zeta_n).
\]
Then \(K\) is the splitting field of \(x^n-1\) over \(\mathbb Q\).
::: {.proof}
Every root of \(x^n-1\) is a power of \(\zeta_n\), hence belongs to \(\mathbb Q(\zeta_n)\). Conversely, every splitting field contains a primitive \(n\)-th root of unity, so it contains \(\mathbb Q(\zeta_n)\).
:::

<1>2. For every \(\sigma\in\operatorname{Gal}(K/\mathbb Q)\), there is a unique residue class \(a_\sigma\in(\mathbb Z/n\mathbb Z)^\times\) such that
\[
\sigma(\zeta_n)=\zeta_n^{a_\sigma}.
\]
::: {.proof}
An automorphism preserves multiplicative order, so \(\sigma(\zeta_n)\) is again a primitive \(n\)-th root of unity. The primitive \(n\)-th roots are exactly \(\zeta_n^a\) with \(\gcd(a,n)=1\), and the exponent is unique modulo \(n\).
:::

<1>3. The map
\[
\Theta:\operatorname{Gal}(K/\mathbb Q)\longrightarrow (\mathbb Z/n\mathbb Z)^\times,
\qquad
\Theta(\sigma)=a_\sigma,
\]
is an injective group homomorphism.
::: {.proof}
If \(\sigma(\zeta_n)=\zeta_n^a\) and \(\tau(\zeta_n)=\zeta_n^b\), then
\[
(\sigma\tau)(\zeta_n)
=\sigma(\zeta_n^b)
=\sigma(\zeta_n)^b
=\zeta_n^{ab},
\]
so \(\Theta(\sigma\tau)=\Theta(\sigma)\Theta(\tau)\). If \(\Theta(\sigma)=1\), then \(\sigma(\zeta_n)=\zeta_n\). Since \(K=\mathbb Q(\zeta_n)\), this forces \(\sigma=\operatorname{id}_K\). Hence \(\Theta\) is injective.
:::

<1>4. Therefore \(\operatorname{Gal}(x^n-1/\mathbb Q)\) is abelian.
::: {.proof}
By <1>3, the Galois group is isomorphic to a subgroup of \((\mathbb Z/n\mathbb Z)^\times\), and this latter group is abelian. Every subgroup of an abelian group is abelian.
:::
:::
