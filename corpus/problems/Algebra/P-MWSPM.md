---
schema: qual/card@1
id: P-MWSPM
kind: problem
title: Finitely generated flat modules over Noetherian local rings are free
classification:
  areas:
  - algebra
  topics:
  - Nakayama's Lemma
  - Free Modules
  - Homological Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Show that a finitely generated module over a Noetherian local ring is flat iff it is free.
:::

::: solution
**Goal:** Let $(R, \mathfrak{m}, k)$ be a Noetherian local ring and $M$ a finitely generated $R$-module. Prove $M$ is flat $\iff$ $M$ is free.

<1>1. Free $\implies$ flat (standard):
    *Proof:*
    <2>1. $R$ is flat over itself, and direct sums of flat modules are flat.
    <2>2. Thus $R^n \cong M$ is flat.

<1>2. Flat $\implies$ free:
    *Proof:*
    <2>1. Let $m_1, \dots, m_n \in M$ lift a $k$-basis of $M / \mathfrak{m}M$ (where $k = R / \mathfrak{m}$). By Nakayama's Lemma, $m_1, \dots, m_n$ generate $M$.
    <2>2. Define the surjection $\varphi: R^n \twoheadrightarrow M$ by $e_i \mapsto m_i$, and let $K = \ker\varphi$.
    <2>3. The short exact sequence $0 \to K \to R^n \to M \to 0$ induces, upon tensoring with $k = R/\mathfrak{m}$:
        $$\operatorname{Tor}_1^R(M, k) \to K \otimes_R k \to k^n \to M \otimes_R k \to 0.$$
    <2>4. Because $M$ is flat, $\operatorname{Tor}_1^R(M, k) = 0$.
    <2>5. The map $k^n \to M \otimes_R k \cong M / \mathfrak{m}M \cong k^n$ is an isomorphism (by choice of the $m_i$).
    <2>6. By exactness, $K \otimes_R k \to k^n$ is zero, so $K \otimes_R k = K / \mathfrak{m}K = 0$.
    <2>7. Since $R$ is Noetherian and $K \subseteq R^n$, $K$ is finitely generated.
    <2>8. By Nakayama's Lemma ($K / \mathfrak{m}K = 0$ and $K$ finitely generated), $K = 0$.
    <2>9. Thus $\varphi: R^n \xrightarrow{\sim} M$ is an isomorphism, so $M \cong R^n$ is free.

<1>3. Conclusion:
    A finitely generated module over a Noetherian local ring is flat if and only if it is free. Q.E.D.
:::
