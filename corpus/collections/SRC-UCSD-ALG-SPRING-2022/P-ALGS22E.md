---
schema: qual/card@1
id: P-ALGS22E
kind: problem
title: "Galois group of Q(zeta_n) is (Z/nZ)*"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $\zeta \in \mathbb{C}$ be a primitive $n$th root of unity for $n \geq 3$.
Let $K = \mathbb{Q}(\zeta)$.

Prove that $\operatorname{Gal}(K/\mathbb{Q})$ is isomorphic to $\mathbb{Z}_n^\times$, the group of units of integers mod $n$.
(You may assume that the $n$th cyclotomic polynomial $\Phi_n(x)$ is irreducible over $\mathbb{Q}$.)
:::


::: {.solution}
<1>1. Every \(\sigma\in\operatorname{Gal}(K/\mathbb Q)\) sends \(\zeta\) to another primitive \(n\)th root of unity, hence
\[
\sigma(\zeta)=\zeta^a
\]
for a unique residue class \(a\in(\mathbb Z/n\mathbb Z)^\times\).
::: {.proof}
Since \(\sigma\) fixes \(\mathbb Q\), it preserves the relation \(\zeta^n=1\), so \(\sigma(\zeta)^n=1\). It also preserves multiplicative order, so \(\sigma(\zeta)\) still has order \(n\). The primitive \(n\)th roots are exactly the \(\zeta^a\) with \(\gcd(a,n)=1\).
:::

<1>2. Define
\[
\Theta:\operatorname{Gal}(K/\mathbb Q)\longrightarrow(\mathbb Z/n\mathbb Z)^\times,
\qquad
\Theta(\sigma)=a\pmod n
\]
when \(\sigma(\zeta)=\zeta^a\). Then \(\Theta\) is an injective group homomorphism.
::: {.proof}
If \(\sigma(\zeta)=\zeta^a\) and \(\tau(\zeta)=\zeta^b\), then
\[
(\sigma\tau)(\zeta)=\sigma(\zeta^b)=\sigma(\zeta)^b=\zeta^{ab},
\]
so \(\Theta(\sigma\tau)=\Theta(\sigma)\Theta(\tau)\). If \(\Theta(\sigma)=1\), then \(\sigma(\zeta)=\zeta\); since \(K=\mathbb Q(\zeta)\), this forces \(\sigma=\operatorname{id}\).
:::

<1>3. The map \(\Theta\) is surjective.
::: {.proof}
Fix \(a\) with \(\gcd(a,n)=1\). Then \(\zeta^a\) is a primitive \(n\)th root, hence a root of the cyclotomic polynomial \(\Phi_n(x)\). By hypothesis \(\Phi_n\) is irreducible over \(\mathbb Q\), so it is the minimal polynomial of \(\zeta\). Therefore there is a \(\mathbb Q\)-embedding
\[
\sigma_a:\mathbb Q(\zeta)\hookrightarrow\mathbb C,
\qquad
\sigma_a(\zeta)=\zeta^a.
\]
Its image is \(\mathbb Q(\zeta^a)\). Since \(a\) is invertible mod \(n\), choose \(b\) with \(ab\equiv1\pmod n\); then \(\zeta=(\zeta^a)^b\), so \(\mathbb Q(\zeta^a)=\mathbb Q(\zeta)=K\). Thus \(\sigma_a\) is an automorphism of \(K\), and \(\Theta(\sigma_a)=a\).
:::

<1>4. Hence
\[
\operatorname{Gal}(K/\mathbb Q)\cong(\mathbb Z/n\mathbb Z)^\times.
\]
::: {.proof}
By <1>2 and <1>3, \(\Theta\) is a bijective homomorphism.
:::
:::
