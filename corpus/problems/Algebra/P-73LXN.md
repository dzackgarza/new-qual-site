---
schema: qual/card@1
id: P-73LXN
kind: problem
title: Galois group of $x^p-2$ over $\QQ$ for odd primes $p$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Roots of Unity
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

::: {.problem}
- Identify all of the elements of the Galois group of $x^p-2$ for $p$ an odd prime (note: this has a complicated presentation).
:::

::: {.solution}
Let \(\alpha=2^{1/p}\) and \(\zeta=\zeta_p\). The roots of \(x^p-2\) are \(\alpha\zeta^a\) for \(a\in\mathbb F_p\), and the splitting field is
\[
K=\mathbb Q(\alpha,\zeta).
\]
Eisenstein at \(2\) gives \([\mathbb Q(\alpha):\mathbb Q]=p\), while \([\mathbb Q(\zeta):\mathbb Q]=p-1\). Their intersection has degree dividing both \(p\) and \(p-1\), hence is \(\mathbb Q\). Therefore
\[
[K:\mathbb Q]=p(p-1).
\]

Every \(\sigma\in G=\operatorname{Gal}(K/\mathbb Q)\) is determined by
\[
\sigma(\alpha)=\alpha\zeta^a,\qquad
\sigma(\zeta)=\zeta^b,
\]
with \(a\in\mathbb F_p\) and \(b\in\mathbb F_p^\times\). There are exactly \(p(p-1)=|G|\) such pairs, hence every pair occurs. Writing the corresponding automorphism as \(\sigma_{a,b}\), composition is
\[
\sigma_{a_1,b_1}\sigma_{a_2,b_2}
=\sigma_{a_1+b_1a_2,\,b_1b_2}.
\]
Thus
\[
G\cong \mathbb F_p\rtimes\mathbb F_p^\times
=\operatorname{AGL}_1(\mathbb F_p).
\]

If \(g\) generates \(\mathbb F_p^\times\), set \(\tau=\sigma_{1,1}\) and \(\omega=\sigma_{0,g}\). Then
\[
\tau^p=1,\qquad \omega^{p-1}=1,\qquad
\omega\tau\omega^{-1}=\tau^g,
\]
so
\[
G=\langle \tau,\omega\mid \tau^p=\omega^{p-1}=1,\ \omega\tau\omega^{-1}=\tau^g\rangle.
\]
These \(p(p-1)\) automorphisms are all elements of the Galois group.
:::
