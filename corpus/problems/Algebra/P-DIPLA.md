---
schema: qual/card@1
id: P-DIPLA
kind: problem
title: Fundamental theorem of Galois theory
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Normal Subgroups
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
Let $K/F$ be a finite Galois extension and let $E$ be an intermediate field ($F \subseteq E \subseteq K$).

(1) Prove that $K/E$ is always Galois with $\Gal(K/E) \le \Gal(K/F)$.

(2) Prove that $E/F$ is Galois if and only if $\Gal(K/E) \trianglelefteq \Gal(K/F)$.

(3) Prove that when $E/F$ is Galois, $\Gal(E/F) \cong \Gal(K/F) / \Gal(K/E)$.
:::

::: {.solution}
Write $G=\Gal(K/F)$ and $H=\Gal(K/E)$.

::: pf

::: pf-step
(1) $K/E$ is Galois and $H\le G$.

::: pf-proof
Since $K/F$ is finite Galois, $K$ is the splitting field over $F$ of a separable polynomial $f\in F[x]$.
Then $K=F(\text{roots of }f)=E(\text{roots of }f)$, so $K$ is also the splitting field of $f$ over $E$, and $K/E$ is Galois.
Every automorphism of $K$ that fixes $E$ fixes $F$, so $H\le G$.
:::

:::

::: {.pf-step #normal}
(2) $E/F$ is Galois if and only if $H\trianglelefteq G$.

::: pf-proof

::: {.pf-step #conj}
For $\sigma\in G$, the fixed field of $\sigma H\sigma^{-1}$ is $\sigma(E)$.

::: pf-proof
An element $\tau\in G$ fixes $\sigma(E)$ pointwise if and only if $\sigma^{-1}\tau\sigma$ fixes $E$ pointwise, that is, $\sigma^{-1}\tau\sigma\in H$.
Thus $\Gal(K/\sigma(E))=\sigma H\sigma^{-1}$, and the Galois correspondence for $K/F$ gives the claim.
:::

:::

::: pf-qed
By step [](#conj){.pf-ref} and the injectivity of the Galois correspondence, $H\trianglelefteq G$ if and only if $\sigma(E)=E$ for every $\sigma\in G$.
Since $E/F$ is separable, this condition is equivalent to $E/F$ being normal, hence Galois.
:::

:::

:::

::: pf-step
(3) If $E/F$ is Galois, then $\Gal(E/F)\cong G/H=\Gal(K/F)/\Gal(K/E)$.

::: pf-proof
By step [](#normal){.pf-ref}, $\sigma(E)=E$ for every $\sigma\in G$, so restriction defines a homomorphism $\rho:G\to\Gal(E/F)$, $\rho(\sigma)=\sigma|_E$.
Its kernel is exactly $H$.
Every $F$-automorphism of $E$ extends to an $F$-automorphism of the normal extension $K/F$, so $\rho$ is surjective.
The first isomorphism theorem gives $\Gal(E/F)\cong G/H$.
:::

:::

:::

:::
