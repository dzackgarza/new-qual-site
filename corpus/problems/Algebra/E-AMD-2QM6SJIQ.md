---
schema: qual/card@1
id: E-AMD-2QM6SJIQ
kind: problem
title: The Galois group of $x^n-1$ over $\QQ$ is $(\ZZ/n\ZZ)^\times$
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
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Compute the Galois group of $x^n - 1 \in \QQ[x]$ as a function of $n$.
:::

::: {.solution}
Let \(\zeta_n=e^{2\pi i/n}\). The roots of \(x^n-1\) are exactly
\[
1,\zeta_n,\zeta_n^2,\dots,\zeta_n^{n-1},
\]
so its splitting field is \(K=\QQ(\zeta_n)\).

<1>1. Every \(\QQ\)-automorphism of \(K\) sends \(\zeta_n\) to \(\zeta_n^a\) for some \(a\in(\ZZ/n\ZZ)^\times\).
::: {.proof}
An automorphism preserves multiplicative order. Since \(\zeta_n\) has order \(n\), its image must be another primitive \(n\)-th root of unity, hence \(\zeta_n^a\) with \(\gcd(a,n)=1\).
:::

<1>2. The map
\[
\Phi:\Gal(K/\QQ)\longrightarrow(\ZZ/n\ZZ)^\times,
\qquad
\sigma\longmapsto a\pmod n
\]
where \(\sigma(\zeta_n)=\zeta_n^a\), is an injective homomorphism.
::: {.proof}
Composition multiplies exponents modulo \(n\), so \(\Phi\) is a homomorphism. Since \(K=\QQ(\zeta_n)\), an automorphism fixing \(\zeta_n\) is the identity, hence \(\Phi\) is injective.
:::

<1>3. The map \(\Phi\) is surjective.
::: {.proof}
The minimal polynomial of \(\zeta_n\) over \(\QQ\) is the cyclotomic polynomial \(\Phi_n(x)\), which is irreducible of degree \(\varphi(n)\). Hence
\[
|\Gal(K/\QQ)|=[K:\QQ]=\varphi(n)=|(\ZZ/n\ZZ)^\times|.
\]
An injective map between these finite groups is therefore bijective.
:::

Thus
\[
\boxed{\Gal(\QQ(\zeta_n)/\QQ)\cong(\ZZ/n\ZZ)^\times}.
\]
:::
