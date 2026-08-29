---
schema: qual/card@1
id: P-WL4WF
kind: problem
title: The cyclotomic extension $\QQ(\zeta_{43})/\QQ$ has Galois group $\ZZ_{42}$
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Galois Theory
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Prove that the cyclotomic extension $\mathbb{Q}(\zeta_{43})/\mathbb{Q}$ has degree 42 and that its Galois group is cyclic of order 42:
$$\operatorname{Gal}(\mathbb{Q}(\zeta_{43})/\mathbb{Q}) \cong (\mathbb{Z}/43\mathbb{Z})^\times \cong \mathbb{Z}/42\mathbb{Z}.$$
:::

::: solution
**Goal:** Prove that $\mathbb{Q}(\zeta_{43})/\mathbb{Q}$ is Galois of degree $\varphi(43) = 42$ with cyclic Galois group $\mathbb{Z}_{42}$.

<1>1. The Cyclotomic Polynomial $\Phi_{43}(x)$:
    *Proof:*
    <2>1. Because $p = 43$ is a prime number, the $43$-rd cyclotomic polynomial is:
        $$\Phi_{43}(x) = \frac{x^{43} - 1}{x - 1} = x^{42} + x^{41} + \cdots + x + 1.$$
    <2>2. **Irreducibility over $\mathbb{Q}$:**
        - Substitute $x = y + 1$:
            $$\Phi_{43}(y+1) = \frac{(y+1)^{43} - 1}{y} = y^{42} + \binom{43}{1}y^{41} + \cdots + \binom{43}{42}y + 43.$$
        - The prime $p = 43$ divides all intermediate binomial coefficients $\binom{43}{k}$ for $1 \le k \le 42$.
        - $p = 43$ divides the constant term 43, but $p^2 = 43^2 \nmid 43$.
        - By Eisenstein's Criterion at $p = 43$, $\Phi_{43}(y+1)$ is irreducible in $\mathbb{Z}[y]$, hence $\Phi_{43}(x)$ is irreducible in $\mathbb{Q}[x]$.

<1>2. Degree of the extension $[\mathbb{Q}(\zeta_{43}) : \mathbb{Q}]$:
    *Proof:*
    <2>1. Since $\zeta_{43} = e^{2\pi i / 43}$ is a root of the monic irreducible polynomial $\Phi_{43}(x)$, the minimal polynomial of $\zeta_{43}$ over $\mathbb{Q}$ is $\Phi_{43}(x)$.
    <2>2. Thus $[\mathbb{Q}(\zeta_{43}) : \mathbb{Q}] = \deg(\Phi_{43}) = \varphi(43) = 42$.

<1>3. Normal and Separable (Galois) property:
    *Proof:*
    <2>1. The roots of $\Phi_{43}(x)$ in $\mathbb{C}$ are precisely the primitive $43$-rd roots of unity:
        $$\{\zeta_{43}^k \mid 1 \le k \le 42\}.$$
    <2>2. Every root $\zeta_{43}^k$ is a power of the single generator $\zeta_{43}$, hence belongs to $\mathbb{Q}(\zeta_{43})$.
    <2>3. Thus $\mathbb{Q}(\zeta_{43})$ is the splitting field of the separable polynomial $\Phi_{43}(x)$ over $\mathbb{Q}$, so $\mathbb{Q}(\zeta_{43})/\mathbb{Q}$ is Galois.

<1>4. Structure of the Galois Group:
    *Proof:*
    <2>1. Every automorphism $\sigma \in \operatorname{Gal}(\mathbb{Q}(\zeta_{43})/\mathbb{Q})$ is completely determined by the image $\sigma(\zeta_{43})$, which must be another root $\zeta_{43}^a$ for some $a \in (\mathbb{Z}/43\mathbb{Z})^\times$.
    <2>2. Define the map $\Psi: \operatorname{Gal}(\mathbb{Q}(\zeta_{43})/\mathbb{Q}) \to (\mathbb{Z}/43\mathbb{Z})^\times$ by $\sigma \mapsto a \pmod{43}$ where $\sigma(\zeta_{43}) = \zeta_{43}^a$.
    <2>3. **$\Psi$ is an isomorphism:**
        - $\sigma(\tau(\zeta_{43})) = \sigma(\zeta_{43}^b) = (\sigma(\zeta_{43}))^b = (\zeta_{43}^a)^b = \zeta_{43}^{ab}$, so $\Psi(\sigma\tau) = \Psi(\sigma)\Psi(\tau)$.
        - $\Psi$ is injective because $\zeta_{43}^a = \zeta_{43} \implies a \equiv 1 \pmod{43} \implies \sigma = \operatorname{id}$.
        - Both groups have order 42, so $\Psi$ is an isomorphism.
    <2>4. Because 43 is a prime, the multiplicative group $(\mathbb{Z}/43\mathbb{Z})^\times$ of the finite field $\mathbb{F}_{43}$ is cyclic of order $43 - 1 = 42$.
    <2>5. Therefore:
        $$\operatorname{Gal}(\mathbb{Q}(\zeta_{43})/\mathbb{Q}) \cong (\mathbb{Z}/43\mathbb{Z})^\times \cong \mathbb{Z}/42\mathbb{Z}.$$

<1>5. Conclusion:
    $[\mathbb{Q}(\zeta_{43}) : \mathbb{Q}] = 42$ and $\operatorname{Gal}(\mathbb{Q}(\zeta_{43})/\mathbb{Q}) \cong \mathbb{Z}_{42}$. Q.E.D.
:::
