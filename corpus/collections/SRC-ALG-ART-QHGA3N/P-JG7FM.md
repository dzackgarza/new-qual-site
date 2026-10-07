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

::: {.problem}
Let $n\geq 3$ and $\zeta_n$ be a primitive $n$th root of unity. Show that $[\QQ(\zeta_n + \zeta_n\inv): \QQ] = \phi(n)/2$ for $\phi$ the totient function.
:::

::: {.solution}
Let
\[
K=\QQ(\zeta_n),
\qquad
\alpha=\zeta_n+\zeta_n^{-1}.
\]
Then
\[
\operatorname{Gal}(K/\QQ)\cong (\ZZ/n\ZZ)^\times,
\]
where \(a\in(\ZZ/n\ZZ)^\times\) acts by \(\sigma_a(\zeta_n)=\zeta_n^a\).

<1>1. For \(a\in(\ZZ/n\ZZ)^\times\),
\[
\sigma_a(\alpha)=\zeta_n^a+\zeta_n^{-a}.
\]
::: {.proof}
This follows directly from the definition of \(\sigma_a\).
:::

<1>2. The stabilizer of \(\alpha\) in \(\operatorname{Gal}(K/\QQ)\) is exactly
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
The Galois group has order \(\varphi(n)\). By orbit-stabilizer and step <1>2,
\[
|\operatorname{Orb}(\alpha)|
=\frac{|\operatorname{Gal}(K/\QQ)|}{|\operatorname{Stab}(\alpha)|}
=\frac{\varphi(n)}2.
\]
:::

<1>4. Therefore
\[
\boxed{[\QQ(\zeta_n+\zeta_n^{-1}):\QQ]
=\frac{\varphi(n)}2}.
\]
::: {.proof}
Because \(K/\QQ\) is Galois, the distinct \(\QQ\)-conjugates of \(\alpha\) inside \(K\) are exactly its Galois orbit. The degree of the minimal polynomial of \(\alpha\) over \(\QQ\) is therefore the orbit size from step <1>3. Since
\[
[\QQ(\alpha):\QQ]=\deg m_\alpha,
\]
the claimed formula follows.
:::

<1>5. Q.E.D.
::: {.proof}
Step <1>4 is the required degree formula.
:::
:::
