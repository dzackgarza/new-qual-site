---
schema: qual/card@1
id: P-WROEI
kind: problem
title: Galois group of $x^7-3$
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
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Compute the Galois group of $p(x) = x^7 - 3$ over $\mathbb{Q}$.
:::

::: solution
**Goal:** Compute the Galois group $\operatorname{Gal}(K/\mathbb{Q})$ where $K$ is the splitting field of $x^7 - 3$ over $\mathbb{Q}$.

<1>1. Irreducibility and roots of $p(x)$:
    *Proof:*
    <2>1. By Eisenstein's Criterion applied to $p(x) = x^7 - 3$ with prime $p = 3$: $3 \mid 3$, $3 \nmid 1$, and $3^2 \nmid 3$. Thus $x^7 - 3$ is irreducible over $\mathbb{Q}$.
    <2>2. The roots of $x^7 - 3$ in $\mathbb{C}$ are:
        $$\alpha_k = \sqrt[7]{3} \, \zeta_7^k \quad \text{for } k = 0, 1, \dots, 6,$$
        where $\sqrt[7]{3} \in \mathbb{R}$ is the real 7-th root and $\zeta_7 = e^{2\pi i/7}$ is a primitive 7-th root of unity.

<1>2. Splitting field and its degree over $\mathbb{Q}$:
    *Proof:*
    <2>1. The splitting field is $K = \mathbb{Q}(\sqrt[7]{3}, \zeta_7)$.
    <2>2. Consider the tower of extensions $\mathbb{Q} \subset \mathbb{Q}(\sqrt[7]{3}) \subset K$:
        - $[\mathbb{Q}(\sqrt[7]{3}) : \mathbb{Q}] = 7$ since $x^7 - 3$ is irreducible of degree 7.
        - The cyclotomic polynomial $\Phi_7(x) = x^6 + x^5 + \cdots + x + 1$ is irreducible over $\mathbb{Q}$, so $[\mathbb{Q}(\zeta_7) : \mathbb{Q}] = 6$.
    <2>3. Since $\gcd(7, 6) = 1$, the degrees are coprime, so $[K : \mathbb{Q}] = 7 \cdot 6 = 42$.
    <2>4. Therefore, $|\operatorname{Gal}(K/\mathbb{Q})| = [K : \mathbb{Q}] = 42$.

<1>3. Generators and relations of the Galois group:
    *Proof:*
    <2>1. Any $\sigma \in \operatorname{Gal}(K/\mathbb{Q})$ is determined by its action on $\sqrt[7]{3}$ and $\zeta_7$:
        $$\sigma(\sqrt[7]{3}) = \sqrt[7]{3} \, \zeta_7^a \quad (a \in \mathbb{Z}/7\mathbb{Z}), \qquad \sigma(\zeta_7) = \zeta_7^b \quad (b \in (\mathbb{Z}/7\mathbb{Z})^\times).$$
    <2>2. Define the automorphisms $\sigma, \tau \in \operatorname{Gal}(K/\mathbb{Q})$:
        - $\sigma$: $\sigma(\sqrt[7]{3}) = \sqrt[7]{3} \, \zeta_7$ and $\sigma(\zeta_7) = \zeta_7$. Then $\sigma$ has order 7, generating a normal Sylow 7-subgroup $N \cong \mathbb{Z}/7\mathbb{Z}$.
        - $\tau$: $\tau(\sqrt[7]{3}) = \sqrt[7]{3}$ and $\tau(\zeta_7) = \zeta_7^3$ (since $3$ is a primitive root modulo 7: $3^1=3, 3^2=2, 3^3=6, 3^4=4, 3^5=5, 3^6=1$). Then $\tau$ has order 6, generating $H \cong \mathbb{Z}/6\mathbb{Z}$.
    <2>3. Conjugation relation:
        $$\tau \sigma \tau^{-1}(\sqrt[7]{3}) = \tau(\sigma(\sqrt[7]{3})) = \tau(\sqrt[7]{3} \, \zeta_7) = \sqrt[7]{3} \, \zeta_7^3 = \sigma^3(\sqrt[7]{3}).$$
        And $\tau \sigma \tau^{-1}(\zeta_7) = \zeta_7 = \sigma^3(\zeta_7)$.
    <2>4. Thus $\tau \sigma \tau^{-1} = \sigma^3$.

<1>4. Identification of the group:
    *Proof:*
    <2>1. $\operatorname{Gal}(K/\mathbb{Q}) \cong \mathbb{Z}/7\mathbb{Z} \rtimes_\theta \mathbb{Z}/6\mathbb{Z} \cong \operatorname{Aff}(\mathbb{F}_7)$, the affine group of the finite field $\mathbb{F}_7$ (transformations $x \mapsto ax + b$ on $\mathbb{F}_7$ with $a \in \mathbb{F}_7^\times, b \in \mathbb{F}_7$).
    <2>2. This is the Frobenius group of order 42.

<1>5. Conclusion:
    $\operatorname{Gal}(x^7 - 3/\mathbb{Q}) \cong \mathbb{Z}_7 \rtimes \mathbb{Z}_6 \cong \operatorname{Aff}(\mathbb{F}_7) \cong F_{42}$. Q.E.D.
:::
