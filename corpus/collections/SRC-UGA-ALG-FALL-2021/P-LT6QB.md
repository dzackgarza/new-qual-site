---
schema: qual/card@1
id: P-LT6QB
kind: problem
title: 'Cyclotomic fields $\QQ(\zeta_n)$: degree, Galois group, and quadratic subfields
  of $\QQ(\zeta_{2021})$'
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Recall that for a positive integer $n$, the cyclotomic field $\mathbb{Q}(\zeta_n)$ is generated over $\mathbb{Q}$ by a primitive $n$-th root of unity $\zeta_n$.

(a) What is the degree $[\mathbb{Q}(\zeta_n) : \mathbb{Q}]$?

(b) Define what it means for a finite field extension $L/K$ to be **Galois**, and prove that the cyclotomic field $\mathbb{Q}(\zeta_n)$ is Galois over $\mathbb{Q}$.

(c) What is the Galois group $\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})$?

(d) How many subfields of $\mathbb{Q}(\zeta_{2021})$ have degree 2 over $\mathbb{Q}$? *(Note that $2021 = 43 \cdot 47$).*
:::

::: solution
**Goal:** Determine the degree, Galois group, and number of quadratic subfields of the cyclotomic extension $\mathbb{Q}(\zeta_{2021})/\mathbb{Q}$.

<1>1. Part (a): Degree of the Cyclotomic Extension $[\mathbb{Q}(\zeta_n) : \mathbb{Q}]$:
    *Proof:*
    <2>1. The primitive $n$-th root of unity $\zeta_n$ has minimal polynomial given by the $n$-th **cyclotomic polynomial**:
        $$\Phi_n(x) = \prod_{\substack{1 \le k \le n \\ \gcd(k, n) = 1}} (x - \zeta_n^k) \in \mathbb{Z}[x].$$
    <2>2. Gauss proved that $\Phi_n(x)$ is **irreducible over $\mathbb{Q}$** for every $n \ge 1$.
    <2>3. The degree of $\Phi_n(x)$ is the value of Euler's totient function $\varphi(n)$.
    <2>4. Therefore:
        $$[\mathbb{Q}(\zeta_n) : \mathbb{Q}] = \deg(\Phi_n) = \varphi(n).$$

<1>2. Part (b): Definition of Galois Extension and Proof for $\mathbb{Q}(\zeta_n)/\mathbb{Q}$:
    *Proof:*
    <2>1. **Definition:** A finite field extension $L/K$ is **Galois** if it is **normal** (it is the splitting field of a family of polynomials with coefficients in $K$) and **separable** (every element has a separable minimal polynomial over $K$).
    <2>2. **Separability:** The base field $\mathbb{Q}$ has characteristic 0 (a perfect field), so every algebraic extension of $\mathbb{Q}$ is automatically separable.
    <2>3. **Normality / Splitting Field:**
        - The polynomial $x^n - 1$ has $n$ distinct roots in $\mathbb{C}$: $\{1, \zeta_n, \zeta_n^2, \dots, \zeta_n^{n-1}\}$.
        - All $n$ roots are powers of the single primitive root $\zeta_n$, so they all lie in $\mathbb{Q}(\zeta_n)$.
        - Thus $\mathbb{Q}(\zeta_n)$ is the **splitting field of $x^n - 1$ (and of $\Phi_n(x)$) over $\mathbb{Q}$**.
    <2>4. Since $\mathbb{Q}(\zeta_n)/\mathbb{Q}$ is finite, normal, and separable, it is a **Galois extension**.

<1>3. Part (c): The Galois Group $\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})$:
    *Proof:*
    <2>1. Any $\mathbb{Q}$-automorphism $\sigma \in \operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})$ must send the generator $\zeta_n$ to another root of its minimal polynomial $\Phi_n(x)$, which must be of the form $\zeta_n^a$ where $\gcd(a, n) = 1$.
    <2>2. Define the map $\Psi: \operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) \to (\mathbb{Z}/n\mathbb{Z})^\times$ by $\Psi(\sigma_a) = a \pmod n$, where $\sigma_a(\zeta_n) = \zeta_n^a$.
    <2>3. Composition of automorphisms corresponds to multiplication in $(\mathbb{Z}/n\mathbb{Z})^\times$:
        $$\sigma_a(\sigma_b(\zeta_n)) = \sigma_a(\zeta_n^b) = (\zeta_n^a)^b = \zeta_n^{ab} = \sigma_{ab}(\zeta_n).$$
    <2>4. Since $|\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})| = [\mathbb{Q}(\zeta_n) : \mathbb{Q}] = \varphi(n) = |(\mathbb{Z}/n\mathbb{Z})^\times|$, the homomorphism $\Psi$ is an **isomorphism**:
        $$\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) \cong (\mathbb{Z}/n\mathbb{Z})^\times.$$

<1>4. Part (d): Quadratic Subfields of $\mathbb{Q}(\zeta_{2021})$:
    *Proof:*
    <2>1. Given $n = 2021 = 43 \cdot 47$, where $p = 43$ and $q = 47$ are distinct odd primes.
    <2>2. By the Chinese Remainder Theorem:
        $$G \coloneqq \operatorname{Gal}(\mathbb{Q}(\zeta_{2021})/\mathbb{Q}) \cong (\mathbb{Z}/2021\mathbb{Z})^\times \cong (\mathbb{Z}/43\mathbb{Z})^\times \times (\mathbb{Z}/47\mathbb{Z})^\times.$$
    <2>3. Since $43$ and $47$ are primes, their unit groups are cyclic:
        $$(\mathbb{Z}/43\mathbb{Z})^\times \cong \mathbb{Z}_{42} \cong \mathbb{Z}_2 \times \mathbb{Z}_3 \times \mathbb{Z}_7, \qquad (\mathbb{Z}/47\mathbb{Z})^\times \cong \mathbb{Z}_{46} \cong \mathbb{Z}_2 \times \mathbb{Z}_{23}.$$
    <2>4. Thus:
        $$G \cong (\mathbb{Z}_2 \times \mathbb{Z}_3 \times \mathbb{Z}_7) \times (\mathbb{Z}_2 \times \mathbb{Z}_{23}) \cong \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_{3 \cdot 7 \cdot 23}.$$
    <2>5. By the **Fundamental Theorem of Galois Theory**, subfields of degree 2 over $\mathbb{Q}$ correspond bijectively to **subgroups of index 2 in $G$** (or equivalently, surjective homomorphisms $G \to \{\pm 1\} \cong \mathbb{Z}_2$).
    <2>6. Subgroups of index 2 in an abelian group $G$ correspond bijectively to non-trivial homomorphisms $\chi: G \to \mathbb{Z}_2$, which form the dual group $\operatorname{Hom}(G, \mathbb{Z}_2) \cong \operatorname{Hom}(\mathbb{Z}_2 \times \mathbb{Z}_2, \mathbb{Z}_2) \cong \mathbb{Z}_2 \times \mathbb{Z}_2$.
    <2>7. The non-trivial homomorphisms correspond to the $2^2 - 1 = 3$ non-zero elements of $(\mathbb{Z}/2\mathbb{Z})^2$.
    <2>8. Thus there are exactly **3 subgroups of index 2** in $G$.
    <2>9. Explicitly, since $43 \equiv 3 \pmod 4$ and $47 \equiv 3 \pmod 4$, the three unique quadratic subfields are:
        $$\mathbb{Q}(\sqrt{-43}), \quad \mathbb{Q}(\sqrt{-47}), \quad \text{and} \quad \mathbb{Q}(\sqrt{(-43)(-47)}) = \mathbb{Q}(\sqrt{2021}).$$

<1>5. Conclusion:
    (a) $[\mathbb{Q}(\zeta_n):\mathbb{Q}] = \varphi(n)$;
    (b) Finite, normal (splitting field of $x^n-1$), separable (char 0);
    (c) $\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) \cong (\mathbb{Z}/n\mathbb{Z})^\times$;
    (d) Exactly **3** subfields of degree 2. Q.E.D.
:::
