---
schema: qual/card@1
id: P-BQVDL
kind: problem
title: A subgroup of index equal to the smallest prime dividing $|G|$ is normal
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Group Actions
  - Cosets and Lagrange
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $G$ be a finite group, and let $H \le G$ be a subgroup of index $[G : H] = p$, where $p$ is the smallest prime dividing $|G|$.
Prove that $H$ is a **normal** subgroup of $G$ ($H \trianglelefteq G$).
:::

::: solution
**Goal:** Prove that a subgroup of index $p = \min \{q \text{ prime} \mid q \text{ divides } |G|\}$ is normal via the coset action representation $\rho: G \to S_p$.

<1>1. Permutation Action on Left Cosets:
    *Proof:*
    <2>1. Let $X = G/H = \{g_1 H, g_2 H, \dots, g_p H\}$ be the set of left cosets of $H$ in $G$, so $|X| = [G : H] = p$.
    <2>2. $G$ acts on $X$ by left translation:
        $$g \cdot (x H) = (g x) H \quad \text{for all } g, x \in G.$$
    <2>3. This group action defines a permutation homomorphism:
        $$\rho: G \longrightarrow S_p = \operatorname{Sym}(X).$$

<1>2. The Normal Core $K = \ker\rho$:
    *Proof:*
    <2>1. The kernel of $\rho$ is the normal core of $H$ in $G$:
        $$K \coloneqq \ker\rho = \{g \in G \mid g x H = x H \ \forall x \in G\} = \bigcap_{x \in G} x H x^{-1}.$$
    <2>2. Being the kernel of a homomorphism, $K \trianglelefteq G$ is a **normal subgroup** of $G$.
    <2>3. Evaluating at the identity coset $e H = H$: $g \in K \implies g H = H \implies g \in H$.
    <2>4. Thus:
        $$K \subseteq H \subseteq G.$$

<1>3. Order and Index of the Quotient $G/K$:
    *Proof:*
    <2>1. By the First Isomorphism Theorem:
        $$G / K \cong \operatorname{im}(\rho) \le S_p.$$
    <2>2. Therefore, by Lagrange's Theorem, the index $[G : K] = |G/K|$ must divide $|S_p| = p!$:
        $$[G : K] \text{ divides } p!.$$
    <2>3. By the Tower Law for subgroup indices:
        $$[G : K] = [G : H] \cdot [H : K] = p \cdot [H : K].$$
    <2>4. Dividing both sides by $p$:
        $$[H : K] \text{ divides } \frac{p!}{p} = (p - 1)!.$$

<1>4. Minimality of the Prime $p$:
    *Proof:*
    <2>1. Since $K \le H \le G$, by Lagrange's Theorem, the index $[H : K] = |H|/|K|$ divides $|H|$, which in turn divides $|G|$.
    <2>2. If $[H : K] > 1$, then $[H : K]$ has a prime factor $q \ge 2$.
    <2>3. Since $q \mid [H : K]$, $q$ divides $|G|$.
    <2>4. By hypothesis, $p$ is the **smallest prime dividing $|G|$**, so:
        $$q \ge p.$$
    <2>5. On the other hand, from Step <1>3, $[H : K]$ divides $(p - 1)! = 1 \cdot 2 \cdot 3 \cdots (p - 1)$.
    <2>6. Therefore, all prime factors of $[H : K]$ must divide $(p - 1)!$, which means every prime factor of $[H : K]$ is **strictly less than $p$**:
        $$q \le p - 1 < p.$$
    <2>7. The two inequalities $q \ge p$ and $q < p$ are mutually contradictory!
    <2>8. Therefore, $[H : K]$ cannot have any prime factors, which forces:
        $$[H : K] = 1.$$
    <2>9. This implies:
        $$H = K = \ker\rho.$$

<1>5. Conclusion:
    Since $H = K = \ker\rho$, $H$ is the kernel of a homomorphism, so $H \trianglelefteq G$ is normal. Q.E.D.
:::
