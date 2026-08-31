---
schema: qual/card@1
id: P-PF5MC
kind: problem
title: Galois group of $x^5-2$
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
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Calculate the Galois group of $x^5 - 2$.
:::

::: solution
**Goal:** Determine the Galois group $\operatorname{Gal}(K/\mathbb{Q})$ of the polynomial $f(x) = x^5 - 2$ over $\mathbb{Q}$.

<1>1. Irreducibility and root generation:
    *Proof:*
    <2>1. The polynomial $f(x) = x^5 - 2 \in \mathbb{Q}[x]$ is monic and Eisenstein with respect to the prime $p = 2$.
    <2>2. By Eisenstein's Criterion and Gauss's Lemma, $f(x)$ is irreducible over $\mathbb{Q}$.
    <2>3. Let $\alpha = \sqrt[5]{2} \in \mathbb{R}$ be the real fifth root of 2. Then $[\mathbb{Q}(\alpha) : \mathbb{Q}] = \deg f = 5$.
    <2>4. The five complex roots of $f(x)$ are $\alpha_k = \zeta^k \alpha$ for $k = 0, 1, 2, 3, 4$, where $\zeta = e^{2\pi i/5}$ is a primitive fifth root of unity.

<1>2. Degree of the splitting field $K$:
    *Proof:*
    <2>1. The splitting field of $f(x)$ over $\mathbb{Q}$ is $K = \mathbb{Q}(\alpha, \zeta\alpha, \dots, \zeta^4\alpha) = \mathbb{Q}(\alpha, \zeta)$.
    <2>2. The minimal polynomial of $\zeta$ over $\mathbb{Q}$ is the fifth cyclotomic polynomial
    $$\Phi_5(x) = x^4 + x^3 + x^2 + x + 1,$$
    which is irreducible over $\mathbb{Q}$ with degree $[\mathbb{Q}(\zeta) : \mathbb{Q}] = 4$.
    <2>3. Because $[\mathbb{Q}(\alpha) : \mathbb{Q}] = 5$ and $[\mathbb{Q}(\zeta) : \mathbb{Q}] = 4$ are coprime ($\gcd(5, 4) = 1$), the tower law implies
    $$[K : \mathbb{Q}] = [\mathbb{Q}(\alpha, \zeta) : \mathbb{Q}] = [\mathbb{Q}(\alpha) : \mathbb{Q}] \cdot [\mathbb{Q}(\zeta) : \mathbb{Q}] = 5 \times 4 = 20.$$
    <2>4. In characteristic 0, every algebraic extension is separable, so $K/\mathbb{Q}$ is a normal and separable Galois extension with $|\operatorname{Gal}(K/\mathbb{Q})| = [K : \mathbb{Q}] = 20$.

<1>3. Construction of Galois automorphisms:
    *Proof:*
    <2>1. Since $[K : \mathbb{Q}(\zeta)] = 5$ and the minimal polynomial of $\alpha$ over $\mathbb{Q}(\zeta)$ is $x^5 - 2$, there exists an automorphism $\sigma \in \operatorname{Gal}(K/\mathbb{Q}(\zeta)) \subset \operatorname{Gal}(K/\mathbb{Q})$ satisfying
    $$\sigma(\alpha) = \zeta \alpha, \qquad \sigma(\zeta) = \zeta.$$
    Iterating gives $\sigma^k(\alpha) = \zeta^k \alpha$, so $\sigma$ has order 5 and generates a cyclic subgroup $N = \langle \sigma \rangle \cong C_5$.
    <2>2. Since $[K : \mathbb{Q}(\alpha)] = 4$ and the minimal polynomial of $\zeta$ over $\mathbb{Q}(\alpha)$ is $\Phi_5(x)$, there exists an automorphism $\tau \in \operatorname{Gal}(K/\mathbb{Q}(\alpha)) \subset \operatorname{Gal}(K/\mathbb{Q})$ satisfying
    $$\tau(\alpha) = \alpha, \qquad \tau(\zeta) = \zeta^2.$$
    Because 2 is a primitive root modulo 5 ($2^1 \equiv 2, 2^2 \equiv 4, 2^3 \equiv 3, 2^4 \equiv 1 \pmod 5$), $\tau$ has order 4 and generates a cyclic subgroup $H = \langle \tau \rangle \cong C_4$.

<1>4. Group structure and semidirect product presentation:
    *Proof:*
    <2>1. The subgroup $N = \operatorname{Gal}(K/\mathbb{Q}(\zeta))$ is the kernel of the restriction homomorphism $\operatorname{Gal}(K/\mathbb{Q}) \to \operatorname{Gal}(\mathbb{Q}(\zeta)/\mathbb{Q})$, so $N \trianglelefteq \operatorname{Gal}(K/\mathbb{Q})$.
    <2>2. Since $\gcd(|N|, |H|) = \gcd(5, 4) = 1$, $N \cap H = \{e\}$.
    <2>3. By the product formula, $|NH| = |N| \cdot |H| = 20 = |\operatorname{Gal}(K/\mathbb{Q})|$, so $\operatorname{Gal}(K/\mathbb{Q}) = NH = N \rtimes H$.
    <2>4. Compute the conjugation action of $\tau$ on $\sigma$:
    $$(\tau \sigma \tau^{-1})(\alpha) = \tau(\sigma(\tau^{-1}(\alpha))) = \tau(\sigma(\alpha)) = \tau(\zeta \alpha) = \tau(\zeta) \tau(\alpha) = \zeta^2 \alpha = \sigma^2(\alpha),$$
    $$(\tau \sigma \tau^{-1})(\zeta) = \tau(\sigma(\tau^{-1}(\zeta))) = \tau(\sigma(\zeta^3)) = \tau(\zeta^3) = (\zeta^2)^3 = \zeta^6 = \zeta = \sigma^2(\zeta).$$
    Since $\tau \sigma \tau^{-1}$ and $\sigma^2$ agree on the generators $\alpha$ and $\zeta$, $\tau \sigma \tau^{-1} = \sigma^2$.

<1>5. Conclusion:
    *Proof:*
    The Galois group of $x^5 - 2$ over $\mathbb{Q}$ is the non-abelian Frobenius group of order 20 (isomorphic to the affine linear group $\operatorname{AGL}_1(\mathbb{F}_5)$), with presentation
    $$\operatorname{Gal}(K/\mathbb{Q}) \cong C_5 \rtimes C_4 \cong \langle \sigma, \tau \mid \sigma^5 = e, \; \tau^4 = e, \; \tau \sigma \tau^{-1} = \sigma^2 \rangle.$$
:::
