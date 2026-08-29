---
schema: qual/card@1
id: P-BOH76
kind: problem
title: Groups of order $p^2$ and of order $pq$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) What are the groups of order $p^2$ for $p$ prime?
(2) What are the groups of order $pq$ for distinct primes $p < q$?
(3) What if $q \equiv 1 \pmod p$?
:::

::: solution
**Goal:** Classify groups of order $p^2$ and groups of order $pq$ ($p < q$).

<1>1. Groups of order $p^2$:
    *Proof:*
    <2>1. Let $G$ be a group of order $p^2$.
    <2>2. By the class equation for $p$-groups, the center $Z(G)$ is non-trivial, so $|Z(G)| \in \{p, p^2\}$.
    <2>3. If $|Z(G)| = p$, then $|G/Z(G)| = p^2/p = p$, so $G/Z(G)$ is cyclic.
    <2>4. But $G/Z(G)$ cyclic implies $G$ is abelian, forcing $Z(G) = G$, so $|Z(G)| = p^2$.
    <2>5. Thus $G$ is abelian.
    <2>6. By the Fundamental Theorem of Finitely Generated Abelian Groups, there are exactly two isomorphism classes of abelian groups of order $p^2$:
        $$\mathbb{Z}_{p^2} \quad \text{and} \quad \mathbb{Z}_p \times \mathbb{Z}_p.$$

<1>2. Groups of order $pq$ ($p < q$ distinct primes):
    *Proof:*
    <2>1. Let $|G| = pq$ with $p < q$.
    <2>2. By Sylow's Theorems, the number $n_q$ of Sylow $q$-subgroups satisfies $n_q \equiv 1 \pmod q$ and $n_q \mid p$.
    <2>3. Since $p < q$, the only divisor of $p$ is 1 or $p$. Since $p < q$, $p \not\equiv 1 \pmod q$, so $n_q = 1$.
    <2>4. Thus the unique Sylow $q$-subgroup $Q \cong \mathbb{Z}_q$ is normal: $Q \trianglelefteq G$.
    <2>5. Let $P \cong \mathbb{Z}_p$ be a Sylow $p$-subgroup.
    <2>6. Since $P \cap Q = \{e\}$ and $|P Q| = |P||Q| = pq = |G|$, $G$ is a semidirect product:
        $$G \cong Q \rtimes_\theta P \cong \mathbb{Z}_q \rtimes_\theta \mathbb{Z}_p$$
        where $\theta: \mathbb{Z}_p \to \operatorname{Aut}(\mathbb{Z}_q) \cong \mathbb{Z}_{q-1}$.

<1>3. Analysis of the homomorphism $\theta: \mathbb{Z}_p \to \mathbb{Z}_{q-1}$:
    *Proof:*
    <2>1. The size of the image $|\operatorname{im}\theta|$ must divide both $|\mathbb{Z}_p| = p$ and $|\operatorname{Aut}(\mathbb{Z}_q)| = q-1$.
    <2>2. **Case A: $p \nmid (q - 1)$ (i.e. $q \not\equiv 1 \pmod p$):**
        - $\gcd(p, q-1) = 1$, so the only homomorphism $\theta$ is the trivial homomorphism $\theta(x) = \operatorname{id}$.
        - Thus the semidirect product is direct: $G \cong \mathbb{Z}_q \times \mathbb{Z}_p \cong \mathbb{Z}_{pq}$.
        - In this case, $\mathbb{Z}_{pq}$ is the **unique** group of order $pq$.
    <2>3. **Case B: $p \mid (q - 1)$ (i.e. $q \equiv 1 \pmod p$):**
        - The cyclic group $\operatorname{Aut}(\mathbb{Z}_q) \cong \mathbb{Z}_{q-1}$ contains a unique subgroup of order $p$.
        - There are $p$ homomorphisms $\theta: \mathbb{Z}_p \to \operatorname{Aut}(\mathbb{Z}_q)$: 1 trivial and $p-1$ non-trivial.
        - The trivial homomorphism gives the abelian group $\mathbb{Z}_{pq} \cong \mathbb{Z}_p \times \mathbb{Z}_q$.
        - The $p-1$ non-trivial homomorphisms all have the same image (the unique subgroup of order $p$ in $\operatorname{Aut}(\mathbb{Z}_q)$), and differing choices of generator for $P$ show they all yield **isomorphic non-abelian semidirect products**.
        - Presentation: $\langle x, y \mid x^q = 1, \, y^p = 1, \, y x y^{-1} = x^r \rangle$ where $r \not\equiv 1 \pmod q$ and $r^p \equiv 1 \pmod q$.
        - (For instance, when $p = 2$, this is the dihedral group $D_q$).

<1>4. Conclusion:
    - Order $p^2$: exactly 2 groups ($\mathbb{Z}_{p^2}$ and $\mathbb{Z}_p \times \mathbb{Z}_p$), both abelian.
    - Order $pq$ with $q \not\equiv 1 \pmod p$: unique group $\mathbb{Z}_{pq}$ (cyclic).
    - Order $pq$ with $q \equiv 1 \pmod p$: exactly 2 groups ($\mathbb{Z}_{pq}$ and non-abelian $\mathbb{Z}_q \rtimes \mathbb{Z}_p$). Q.E.D.
:::
