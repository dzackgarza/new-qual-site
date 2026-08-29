---
schema: qual/card@1
id: P-6VMUH
kind: problem
title: Galois group of $x^4-3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Compute the **Galois group** of the polynomial $f(x) = x^4 - 3$ over $\mathbb{Q}$, and describe its action on the roots.
:::

::: solution
**Goal:** Prove that the splitting field of $f(x) = x^4 - 3$ over $\mathbb{Q}$ has Galois group $\operatorname{Gal}(f/\mathbb{Q}) \cong D_4$ (the dihedral group of order 8).

<1>1. The Four Roots of $f(x)$:
    *Proof:*
    <2>1. Let $\alpha = \sqrt[4]{3} \in \mathbb{R}^+$ be the unique positive real 4th root of 3.
    <2>2. The 4 roots of $f(x) = x^4 - 3 = 0$ in $\mathbb{C}$ are:
        $$\alpha_1 = \alpha, \quad \alpha_2 = i\alpha, \quad \alpha_3 = -\alpha, \quad \alpha_4 = -i\alpha.$$
    <2>3. Geometrically, these 4 roots form the vertices of a square centered at the origin in the complex plane.

<1>2. The Splitting Field $K$ and its Degree:
    *Proof:*
    <2>1. The splitting field of $f(x)$ over $\mathbb{Q}$ is:
        $$K = \mathbb{Q}(\alpha_1, \alpha_2, \alpha_3, \alpha_4) = \mathbb{Q}(\alpha, i).$$
    <2>2. **Degree $[\mathbb{Q}(\alpha) : \mathbb{Q}]$:**
        - $f(x) = x^4 - 3$ is **irreducible over $\mathbb{Q}$** by Eisenstein's Criterion at $p = 3$.
        - Thus $[\mathbb{Q}(\alpha) : \mathbb{Q}] = \deg(f) = 4$.
    <2>3. **Degree $[K : \mathbb{Q}(\alpha)]$:**
        - Since $\alpha \in \mathbb{R}$, $\mathbb{Q}(\alpha) \subset \mathbb{R}$ is a purely real subfield.
        - Since $i = \sqrt{-1} \notin \mathbb{R}$, $i \notin \mathbb{Q}(\alpha)$.
        - The minimal polynomial of $i$ over $\mathbb{Q}(\alpha)$ is $x^2 + 1 = 0$, so $[K : \mathbb{Q}(\alpha)] = [\mathbb{Q}(\alpha, i) : \mathbb{Q}(\alpha)] = 2$.
    <2>4. By the Tower Law:
        $$[K : \mathbb{Q}] = [K : \mathbb{Q}(\alpha)] \cdot [\mathbb{Q}(\alpha) : \mathbb{Q}] = 2 \times 4 = 8.$$
    <2>5. Since $\operatorname{char}(\mathbb{Q}) = 0$, $K/\mathbb{Q}$ is Galois, so:
        $$|\operatorname{Gal}(K/\mathbb{Q})| = [K : \mathbb{Q}] = 8.$$

<1>3. Identifying the Generators of $\operatorname{Gal}(K/\mathbb{Q})$:
    *Proof:*
    <2>1. Any $\mathbb{Q}$-automorphism $\sigma \in \operatorname{Gal}(K/\mathbb{Q})$ is determined by its action on $\alpha$ and $i$:
        $$\sigma(\alpha) \in \{\alpha, i\alpha, -\alpha, -i\alpha\}, \qquad \sigma(i) \in \{i, -i\}.$$
    <2>2. **Automorphism $\sigma$ (Rotation of order 4):**
        Define $\sigma \in \operatorname{Gal}(K/\mathbb{Q})$ by:
        $$\sigma(\alpha) = i\alpha, \qquad \sigma(i) = i.$$
        - $\sigma^2(\alpha) = \sigma(i\alpha) = i(i\alpha) = -\alpha$.
        - $\sigma^3(\alpha) = \sigma(-\alpha) = -i\alpha$.
        - $\sigma^4(\alpha) = \alpha$, so $|\sigma| = 4$.
        - In cyclic notation on the roots $(\alpha_1, \alpha_2, \alpha_3, \alpha_4)$, $\sigma = (1 \, 2 \, 3 \, 4)$.
    <2>3. **Automorphism $\tau$ (Complex conjugation, order 2):**
        Define $\tau \in \operatorname{Gal}(K/\mathbb{Q})$ by:
        $$\tau(\alpha) = \alpha, \qquad \tau(i) = -i.$$
        - $|\tau| = 2$.
        - In cyclic notation, $\tau(\alpha_2) = \tau(i\alpha) = -i\alpha = \alpha_4$, so $\tau = (2 \, 4)$.
    <2>4. **Dihedral Relation:**
        - $(\tau \sigma)(\alpha) = \tau(i\alpha) = -i\alpha$.
        - $(\sigma^{-1} \tau)(\alpha) = \sigma^3(\alpha) = -i\alpha$.
        - $(\tau \sigma)(i) = \tau(i) = -i = (\sigma^{-1} \tau)(i)$.
        - Thus $\tau \sigma \tau^{-1} = \sigma^{-1}$.

<1>4. Conclusion:
    The Galois group is isomorphic to the dihedral group of order 8: $\operatorname{Gal}(\mathbb{Q}(\sqrt[4]{3}, i)/\mathbb{Q}) \cong \langle \sigma, \tau \mid \sigma^4 = 1, \tau^2 = 1, \tau \sigma \tau = \sigma^{-1} \rangle \cong D_4$. Q.E.D.
:::
