---
schema: qual/card@1
id: P-JG7FM
kind: problem
title: $[\QQ(\zeta_n+\zeta_n^{-1}):\QQ]=\phi(n)/2$
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Field Extensions
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

Let $n\geq 3$ and $\zeta_n$ be a primitive $n$th root of unity. Show that $[\QQ(\zeta_n + \zeta_n\inv): \QQ] = \phi(n)/2$ for $\phi$ the totient function.

::: {.solution}
Let
\[
K=\mathbb Q(\zeta_n),
\qquad
\alpha=\zeta_n+\zeta_n^{-1}.
\]
Then
\[
\operatorname{Gal}(K/\mathbb Q)\cong (\mathbb Z/n\mathbb Z)^\times,
\]
where \(a\in(\mathbb Z/n\mathbb Z)^\times\) acts by \(\sigma_a(\zeta_n)=\zeta_n^a\).

<1>1. For \(a\in(\mathbb Z/n\mathbb Z)^\times\),
\[
\sigma_a(\alpha)=\zeta_n^a+\zeta_n^{-a}.
\]
::: {.proof}
This follows directly from the definition of \(\sigma_a\).
:::

<1>2. The stabilizer of \(\alpha\) in \(\operatorname{Gal}(K/\mathbb Q)\) is exactly
\[
\{\sigma_1,\sigma_{-1}\}.
\]
::: {.proof}
Certainly \(\sigma_1(\alpha)=\alpha\) and \(\sigma_{-1}(\alpha)=\alpha\). Conversely, suppose
\[
\zeta_n^a+\zeta_n^{-a}=\zeta_n+\zeta_n^{-1}.
\]
The two numbers \(\zeta_n^a\) and \(\zeta_n^{-a}\) are the roots of
\[
t^2-(\zeta_n^a+\zeta_n^{-a})t+1,
\]
while \(\zeta_n\) and \(\zeta_n^{-1}\) are the roots of
\[
t^2-(\zeta_n+\zeta_n^{-1})t+1.
\]
The polynomials are equal, so their root sets are equal. Hence
\[
\zeta_n^a\in\{\zeta_n,\zeta_n^{-1}\},
\]
which means \(a\equiv\pm1\pmod n\). Since \(n\ge3\), the residues \(1\) and \(-1\) are distinct, so the stabilizer has order \(2\).
:::

<1>3. The Galois orbit of \(\alpha\) has size
\[
\frac{\varphi(n)}2.
\]
::: {.proof}
The Galois group has order \(\varphi(n)\). By orbit-stabilizer and <1>2,
\[
|\operatorname{Orb}(\alpha)|
=\frac{|\operatorname{Gal}(K/\mathbb Q)|}{|\operatorname{Stab}(\alpha)|}
=\frac{\varphi(n)}2.
\]
:::

<1>4. Therefore
\[
[\mathbb Q(\zeta_n+\zeta_n^{-1}):\mathbb Q]
=\frac{\varphi(n)}2.
\]
::: {.proof}
Because \(K/\mathbb Q\) is Galois, the distinct \(\mathbb Q\)-conjugates of \(\alpha\) inside \(K\) are exactly its Galois orbit. The degree of the minimal polynomial of \(\alpha\) over \(\mathbb Q\) is therefore the orbit size from <1>3. Since
\[
[\mathbb Q(\alpha):\mathbb Q]=\deg m_\alpha,
\]
the claimed formula follows.
:::
:::
