---
schema: qual/card@1
id: P-ESUCT
kind: problem
title: $\mathbb{Q}(\zeta_n)/\mathbb{Q}$ is Galois with group $(\mathbb{Z}/n\mathbb{Z})^\times$,
  and the subfields of $\mathbb{Q}(\zeta_{20})$
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Galois Theory
  - Field Extensions
relations: []
review: draft
---

::: problem
Let $\zeta_n \in \mathbb{C}$ denote a primitive $n$-th root of unity, and let $p_n(x) \in \mathbb{Q}[x]$ be its minimal polynomial over $\mathbb{Q}$. You may assume that the roots of $p_n(x)$ are precisely the primitive $n$-th roots of unity in $\mathbb{C}$.

(a) Show that the field extension $\mathbb{Q}(\zeta_n)/\mathbb{Q}$ is Galois, and prove that its Galois group is isomorphic to $(\mathbb{Z}/n\mathbb{Z})^\times$.

(b) How many subfields are there of $\mathbb{Q}(\zeta_{20})$?
:::

::: solution
**Goal:** Prove that cyclotomic extensions are Galois with abelian Galois group $(\mathbb{Z}/n\mathbb{Z})^\times$ in (a), and count the subfields of $\mathbb{Q}(\zeta_{20})$ via the Galois correspondence in (b).

<1>1. Part (a): $\mathbb{Q}(\zeta_n)/\mathbb{Q}$ is Galois.
    *Proof:*
    <2>1. Splitting field: The polynomial $x^n - 1 \in \mathbb{Q}[x]$ has roots $\{e^{2\pi i k / n} : 0 \le k < n\} = \{\zeta_n^k : 0 \le k < n\}$. All of these roots belong to $\mathbb{Q}(\zeta_n)$.
    <2>2. Thus $\mathbb{Q}(\zeta_n)$ is the splitting field of $x^n - 1$ over $\mathbb{Q}$.
    <2>3. Since $\mathbb{Q}$ has characteristic 0, every algebraic extension over $\mathbb{Q}$ is separable.
    <2>4. Because $\mathbb{Q}(\zeta_n)/\mathbb{Q}$ is a splitting field of a separable polynomial, it is normal and separable, hence Galois.

<1>2. Part (a): $\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) \cong (\mathbb{Z}/n\mathbb{Z})^\times$.
    *Proof:*
    <2>1. Field degree: By hypothesis, the roots of the minimal polynomial $p_n(x)$ of $\zeta_n$ over $\mathbb{Q}$ are precisely the primitive $n$-th roots of unity. The number of primitive $n$-th roots of unity is $\varphi(n)$, so $[\mathbb{Q}(\zeta_n) : \mathbb{Q}] = \deg p_n(x) = \varphi(n)$.
    <2>2. Action on generators: Any automorphism $\sigma \in \operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})$ is uniquely determined by its value $\sigma(\zeta_n)$, since $\mathbb{Q}(\zeta_n) = \mathbb{Q}[\zeta_n]$.
    <2>3. Roots of minimal polynomial: $\sigma(\zeta_n)$ must be a root of $p_n(x)$, which means $\sigma(\zeta_n) = \zeta_n^a$ for some integer $a$ with $1 \le a \le n$ and $\gcd(a, n) = 1$.
    <2>4. Group homomorphism: Define the map
    $$\Psi: \operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) \to (\mathbb{Z}/n\mathbb{Z})^\times, \quad \sigma \mapsto [a]_n \text{ where } \sigma(\zeta_n) = \zeta_n^a.$$
    For any $\sigma, \tau \in \operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})$ with $\sigma(\zeta_n) = \zeta_n^a$ and $\tau(\zeta_n) = \zeta_n^b$:
    $$(\sigma \circ \tau)(\zeta_n) = \sigma(\zeta_n^b) = (\sigma(\zeta_n))^b = (\zeta_n^a)^b = \zeta_n^{ab}.$$
    Thus $\Psi(\sigma \circ \tau) = [ab]_n = [a]_n [b]_n = \Psi(\sigma) \Psi(\tau)$, so $\Psi$ is a group homomorphism.
    <2>5. Injectivity: If $\Psi(\sigma) = [1]_n$, then $\sigma(\zeta_n) = \zeta_n^1 = \zeta_n$. Since $\sigma$ fixes $\mathbb{Q}$ and $\zeta_n$, $\sigma = \operatorname{id}$. Thus $\ker \Psi = \{\operatorname{id}\}$, so $\Psi$ is injective.
    <2>6. Isomorphism: Since $|\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})| = [\mathbb{Q}(\zeta_n) : \mathbb{Q}] = \varphi(n) = |(\mathbb{Z}/n\mathbb{Z})^\times|$, the injective homomorphism $\Psi$ is a bijection, and hence an isomorphism:
    $$\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) \cong (\mathbb{Z}/n\mathbb{Z})^\times.$$

<1>3. Part (b): Number of subfields of $\mathbb{Q}(\zeta_{20})$.
    *Proof:*
    <2>1. Galois group structure:
        For $n = 20 = 2^2 \cdot 5$, by the Chinese Remainder Theorem:
        $$G = \operatorname{Gal}(\mathbb{Q}(\zeta_{20})/\mathbb{Q}) \cong (\mathbb{Z}/20\mathbb{Z})^\times \cong (\mathbb{Z}/4\mathbb{Z})^\times \times (\mathbb{Z}/5\mathbb{Z})^\times \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/4\mathbb{Z}.$$
    <2>2. Galois Correspondence: By the Fundamental Theorem of Galois Theory, the subfields $E$ with $\mathbb{Q} \subseteq E \subseteq \mathbb{Q}(\zeta_{20})$ correspond bijectively to the subgroups of $G \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/4\mathbb{Z}$.
    <2>3. Classification of subgroups of $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/4\mathbb{Z}$:
        - Order 1 (index 8): Exactly 1 subgroup: $\{(0, 0)\}$, corresponding to $\mathbb{Q}(\zeta_{20})$.
        - Order 2 (index 4): The elements of order 2 in $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/4\mathbb{Z}$ are $(1, 0)$, $(0, 2)$, and $(1, 2)$. Each generates a distinct cyclic subgroup of order 2:
        $$H_1 = \langle (1, 0) \rangle, \quad H_2 = \langle (0, 2) \rangle, \quad H_3 = \langle (1, 2) \rangle.$$
        There are exactly 3 subgroups of order 2.
        - Order 4 (index 2):
            - Cyclic subgroups of order 4: The elements of order 4 are $(0, 1)$, $(0, 3)$, $(1, 1)$, and $(1, 3)$. They generate 2 cyclic subgroups:
            $$K_1 = \langle (0, 1) \rangle = \langle (0, 3) \rangle, \quad K_2 = \langle (1, 1) \rangle = \langle (1, 3) \rangle.$$
            - Non-cyclic subgroup ($\cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$): Generated by the elements of order 2:
            $$K_3 = \{(0, 0), (1, 0), (0, 2), (1, 2)\}.$$
            There are exactly $2 + 1 = 3$ subgroups of order 4.
        - Order 8 (index 1): Exactly 1 subgroup: $G$ itself, corresponding to $\mathbb{Q}$.
    <2>4. Total count:
        $$1 + 3 + 3 + 1 = 8 \text{ subgroups}.$$
    <2>5. Therefore $\mathbb{Q}(\zeta_{20})$ has exactly 8 subfields.

<1>4. Conclusion:
    *Proof:*
    $\mathbb{Q}(\zeta_n)/\mathbb{Q}$ is Galois with group $(\mathbb{Z}/n\mathbb{Z})^\times$, and $\mathbb{Q}(\zeta_{20})$ has 8 subfields.
:::

