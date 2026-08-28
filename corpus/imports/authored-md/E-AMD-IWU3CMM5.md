---
schema: qual/card@1
id: E-AMD-IWU3CMM5
kind: exercise
title: Groups of order $pq$ with $q<p$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Analyze groups of order $pq$ with $q<p$ prime.

- Show that $G$ is never simple.

- Show that if $q$ does not divide $p-1$, then $G$ is cyclic.

- Classify $G$ when $q \mid (p-1)$.
:::

::: solution
**Goal:** Classify all groups $G$ of order $pq$ where $p, q$ are primes with $q < p$.

<1>1. $G$ is never simple ($P \trianglelefteq G$):
    *Proof:*
    <2>1. By the Sylow theorems, the number $n_p$ of Sylow $p$-subgroups satisfies:
        $$n_p \equiv 1 \pmod p \quad \text{and} \quad n_p \mid q.$$
    <2>2. The only divisors of $q$ are $1$ and $q$.
    <2>3. Since $q < p$, $q \not\equiv 1 \pmod p$ (because $q - 1 < p - 1 < p$).
    <2>4. Thus $n_p = 1$, which means the unique Sylow $p$-subgroup $P \in \operatorname{Syl}_p(G)$ is normal ($P \trianglelefteq G$).
    <2>5. Because $1 < |P| = p < pq$, $P$ is a proper non-trivial normal subgroup, so $G$ is never simple.

<1>2. Semidirect product decomposition:
    *Proof:*
    <2>1. Let $Q \in \operatorname{Syl}_q(G)$ be a Sylow $q$-subgroup, so $P \cong \mathbb{Z}_p$ and $Q \cong \mathbb{Z}_q$.
    <2>2. Since $\gcd(p, q) = 1$, Lagrange's Theorem implies $P \cap Q = \{e\}$.
    <2>3. Because $|PQ| = pq = |G|$ and $P \trianglelefteq G$, $G$ is an internal semidirect product:
        $$G \cong P \rtimes_\theta Q \cong \mathbb{Z}_p \rtimes_\theta \mathbb{Z}_q,$$
        where $\theta: \mathbb{Z}_q \to \operatorname{Aut}(\mathbb{Z}_p)$ is the conjugation homomorphism.

<1>3. If $q \nmid (p - 1)$, then $G$ is cyclic:
    *Proof:*
    <2>1. The automorphism group is $\operatorname{Aut}(\mathbb{Z}_p) \cong (\mathbb{Z}/p\mathbb{Z})^\times \cong \mathbb{Z}_{p-1}$, which has order $p - 1$.
    <2>2. The image of any homomorphism $\theta: \mathbb{Z}_q \to \mathbb{Z}_{p-1}$ has order dividing both $|\mathbb{Z}_q| = q$ and $|\mathbb{Z}_{p-1}| = p - 1$.
    <2>3. Since $q$ is prime and $q \nmid (p - 1)$, $\gcd(q, p - 1) = 1$.
    <2>4. Thus the only homomorphism $\theta$ is the trivial homomorphism $\theta(x) = \operatorname{id}$.
    <2>5. Therefore $G \cong \mathbb{Z}_p \times \mathbb{Z}_q \cong \mathbb{Z}_{pq}$, which is cyclic.

<1>4. Classification when $q \mid (p - 1)$:
    *Proof:*
    <2>1. If $q \mid (p - 1)$, the cyclic group $\operatorname{Aut}(\mathbb{Z}_p) \cong \mathbb{Z}_{p-1}$ contains a unique subgroup of order $q$.
    <2>2. There are $q$ homomorphisms $\theta: \mathbb{Z}_q \to \operatorname{Aut}(\mathbb{Z}_p)$, consisting of $1$ trivial homomorphism and $q - 1$ non-trivial homomorphisms.
    <2>3. The $q - 1$ non-trivial homomorphisms share the same image and differ only by an automorphism of the domain $\mathbb{Z}_q$, so they all yield isomorphic semidirect products.
    <2>4. Thus there are exactly $2$ isomorphism classes: the cyclic group $\mathbb{Z}_{pq}$ and a unique non-abelian group $\mathbb{Z}_p \rtimes \mathbb{Z}_q$.

<1>5. Conclusion:
    $G$ is never simple; $G \cong \mathbb{Z}_{pq}$ whenever $q \nmid (p-1)$; and $G$ is either $\mathbb{Z}_{pq}$ or $\mathbb{Z}_p \rtimes \mathbb{Z}_q$ when $q \mid (p-1)$. Q.E.D.
:::
