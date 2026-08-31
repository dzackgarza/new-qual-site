---
schema: qual/card@1
id: P-TOPF24H
kind: problem
title: Compute $\operatorname{Tor}(\mathbb{Z} \oplus \mathbb{Z}_4, \mathbb{Z}_6 \oplus \mathbb{Z}_8)$
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Compute $\operatorname{Tor}(\mathbb{Z} \oplus \mathbb{Z}_4, \mathbb{Z}_6 \oplus \mathbb{Z}_8)$.
:::

::: solution
**Goal:** Compute the torsion group $\operatorname{Tor}_1^\mathbb{Z}(\mathbb{Z} \oplus \mathbb{Z}_4, \mathbb{Z}_6 \oplus \mathbb{Z}_8)$.

<1>1. Tor of cyclic abelian groups via projective resolutions:
    *Proof:*
    <2>1. For any abelian group $A$, since $\mathbb{Z}$ is a free (hence projective) $\mathbb{Z}$-module, $\operatorname{Tor}_1^\mathbb{Z}(\mathbb{Z}, A) = 0$.
    <2>2. For cyclic groups $\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$ and $\mathbb{Z}_m = \mathbb{Z}/m\mathbb{Z}$, consider the standard free resolution of $\mathbb{Z}_n$:
    $$0 \to \mathbb{Z} \xrightarrow{\times n} \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z} \to 0.$$
    <2>3. Applying the functor $- \otimes_\mathbb{Z} \mathbb{Z}/m\mathbb{Z}$ yields the exact sequence
    $$0 \to \operatorname{Tor}_1^\mathbb{Z}(\mathbb{Z}_n, \mathbb{Z}_m) \to \mathbb{Z} \otimes \mathbb{Z}_m \xrightarrow{n \otimes \operatorname{id}} \mathbb{Z} \otimes \mathbb{Z}_m \to \mathbb{Z}_n \otimes \mathbb{Z}_m \to 0.$$
    <2>4. Identifying $\mathbb{Z} \otimes \mathbb{Z}_m \cong \mathbb{Z}_m$, the map is multiplication by $n$ on $\mathbb{Z}/m\mathbb{Z}$:
    $$\operatorname{Tor}_1^\mathbb{Z}(\mathbb{Z}_n, \mathbb{Z}_m) \cong \ker(\mathbb{Z}/m\mathbb{Z} \xrightarrow{\times n} \mathbb{Z}/m\mathbb{Z}) = \{x \in \mathbb{Z}/m\mathbb{Z} : nx \equiv 0 \pmod m\}.$$
    <2>5. The elements satisfying $nx \equiv 0 \pmod m$ form a cyclic subgroup of $\mathbb{Z}/m\mathbb{Z}$ of order $\gcd(n, m)$, so
    $$\operatorname{Tor}_1^\mathbb{Z}(\mathbb{Z}_n, \mathbb{Z}_m) \cong \mathbb{Z}/\gcd(n, m)\mathbb{Z}.$$

<1>2. Additivity of Tor across direct sums:
    *Proof:*
    <2>1. The Tor functor commutes with arbitrary direct sums in each variable:
    $$\operatorname{Tor}_1^\mathbb{Z}\left( \bigoplus_i A_i, \bigoplus_j B_j \right) \cong \bigoplus_{i, j} \operatorname{Tor}_1^\mathbb{Z}(A_i, B_j).$$
    <2>2. Expanding the given expression:
    $$\operatorname{Tor}_1^\mathbb{Z}(\mathbb{Z} \oplus \mathbb{Z}_4, \mathbb{Z}_6 \oplus \mathbb{Z}_8) \cong \operatorname{Tor}(\mathbb{Z}, \mathbb{Z}_6) \oplus \operatorname{Tor}(\mathbb{Z}, \mathbb{Z}_8) \oplus \operatorname{Tor}(\mathbb{Z}_4, \mathbb{Z}_6) \oplus \operatorname{Tor}(\mathbb{Z}_4, \mathbb{Z}_8).$$

<1>3. Evaluation of components:
    *Proof:*
    <2>1. $\operatorname{Tor}(\mathbb{Z}, \mathbb{Z}_6) = 0$ and $\operatorname{Tor}(\mathbb{Z}, \mathbb{Z}_8) = 0$.
    <2>2. $\operatorname{Tor}(\mathbb{Z}_4, \mathbb{Z}_6) \cong \mathbb{Z}_{\gcd(4, 6)} = \mathbb{Z}_2$.
    <2>3. $\operatorname{Tor}(\mathbb{Z}_4, \mathbb{Z}_8) \cong \mathbb{Z}_{\gcd(4, 8)} = \mathbb{Z}_4$.
    <2>4. Summing the components:
    $$\operatorname{Tor}_1^\mathbb{Z}(\mathbb{Z} \oplus \mathbb{Z}_4, \mathbb{Z}_6 \oplus \mathbb{Z}_8) \cong 0 \oplus 0 \oplus \mathbb{Z}_2 \oplus \mathbb{Z}_4 \cong \mathbb{Z}_2 \oplus \mathbb{Z}_4.$$

<1>4. Conclusion:
    *Proof:*
    $\operatorname{Tor}(\mathbb{Z} \oplus \mathbb{Z}_4, \mathbb{Z}_6 \oplus \mathbb{Z}_8) \cong \mathbb{Z}_2 \oplus \mathbb{Z}_4 \cong \mathbb{Z}/2\mathbb{Z} \oplus \mathbb{Z}/4\mathbb{Z}$.
:::
