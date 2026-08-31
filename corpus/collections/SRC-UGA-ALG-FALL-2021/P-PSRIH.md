---
schema: qual/card@1
id: P-PSRIH
kind: problem
title: Presentation of the nonabelian group of order $63$ with an element of order
  $9$
classification:
  areas:
  - algebra
  topics:
  - Group Presentations
  - Semidirect Products
  - Classification
relations: []
review: draft
---

::: problem
Give generators and relations (a presentation) for a non-abelian group $G$ of order $63$ containing an element of order $9$.
:::

::: solution
**Goal:** Construct a non-abelian group of order $63$ with an element of order $9$ as a semidirect product $\mathbb{Z}/7\mathbb{Z} \rtimes_\theta \mathbb{Z}/9\mathbb{Z}$ and derive its presentation.

<1>1. Sylow structure and semidirect product:
    *Proof:*
    <2>1. The order of $G$ is $|G| = 63 = 3^2 \cdot 7$.
    <2>2. By Sylow's Theorems, the number $n_7$ of Sylow 7-subgroups satisfies $n_7 \equiv 1 \pmod 7$ and $n_7 \mid 9$.
    <2>3. The only divisor of 9 congruent to $1 \pmod 7$ is $n_7 = 1$.
    <2>4. Thus the unique Sylow 7-subgroup $P \cong \mathbb{Z}/7\mathbb{Z}$ is normal in $G$ ($P \trianglelefteq G$).
    <2>5. By hypothesis, $G$ contains an element of order 9, so the Sylow 3-subgroup $Q \le G$ of order 9 is cyclic: $Q \cong \mathbb{Z}/9\mathbb{Z}$.
    <2>6. Since $P \trianglelefteq G$, $P \cap Q = \{e\}$ (coprime orders), and $|P Q| = |P||Q| = 63$, $G$ is the semidirect product:
    $$G \cong P \rtimes_\theta Q \cong \mathbb{Z}/7\mathbb{Z} \rtimes_\theta \mathbb{Z}/9\mathbb{Z},$$
    determined by a homomorphism $\theta: \mathbb{Z}/9\mathbb{Z} \to \operatorname{Aut}(\mathbb{Z}/7\mathbb{Z})$.

<1>2. Classification of homomorphisms $\theta: \mathbb{Z}/9\mathbb{Z} \to \operatorname{Aut}(\mathbb{Z}/7\mathbb{Z})$:
    *Proof:*
    <2>1. The automorphism group of the cyclic group $\mathbb{Z}/7\mathbb{Z}$ is
    $$\operatorname{Aut}(\mathbb{Z}/7\mathbb{Z}) \cong (\mathbb{Z}/7\mathbb{Z})^\times \cong \mathbb{Z}/6\mathbb{Z}.$$
    <2>2. Any homomorphism $\theta: \mathbb{Z}/9\mathbb{Z} \to (\mathbb{Z}/7\mathbb{Z})^\times$ is uniquely determined by $\theta(1) = k \in (\mathbb{Z}/7\mathbb{Z})^\times$, where the order of $k$ must divide $\gcd(9, 6) = 3$.
    <2>3. In $(\mathbb{Z}/7\mathbb{Z})^\times$, the elements of order dividing 3 satisfy $k^3 \equiv 1 \pmod 7$:
    $$1^3 \equiv 1 \pmod 7, \quad 2^3 = 8 \equiv 1 \pmod 7, \quad 4^3 = 64 \equiv 1 \pmod 7.$$
    <2>4. Since $G$ is non-abelian, $\theta$ must be non-trivial, so $\operatorname{ord}(k) = 3$, meaning $k \in \{2, 4\} \pmod 7$.
    <2>5. Choosing $k = 2$ defines the action $\theta(y)(x) = x^2$, where $x$ generates $\mathbb{Z}/7\mathbb{Z}$ and $y$ generates $\mathbb{Z}/9\mathbb{Z}$. (The choice $k = 4$ corresponds to replacing generator $y$ with $y^2$, yielding an isomorphic group.)

<1>3. Presentation of $G$:
    *Proof:*
    <2>1. Let $x$ be a generator of $P \cong \mathbb{Z}/7\mathbb{Z}$, giving the relation $x^7 = e$.
    <2>2. Let $y$ be a generator of $Q \cong \mathbb{Z}/9\mathbb{Z}$, giving the relation $y^9 = e$.
    <2>3. The conjugation action $\theta(y)(x) = x^2$ yields the relation $y x y^{-1} = x^2$.
    <2>4. Consistency check:
    $$y^9 x y^{-9} = x^{2^9} = x^{512} = x^{7 \cdot 73 + 1} = x^1 = x,$$
    which is compatible with $y^9 = e$.
    <2>5. Thus a presentation for $G$ is:
    $$G = \langle x, y \mid x^7 = e, \, y^9 = e, \, y x y^{-1} = x^2 \rangle.$$

<1>4. Conclusion:
    *Proof:*
    $G = \langle x, y \mid x^7 = e, \, y^9 = e, \, y x y^{-1} = x^2 \rangle$ is a non-abelian group of order 63 containing an element $y$ of order 9.
:::
