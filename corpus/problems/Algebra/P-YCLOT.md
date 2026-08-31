---
schema: qual/card@1
id: P-YCLOT
kind: problem
title: Groups of order $p^2$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Abelian Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
- (**Important**) Classify all groups of order $p^2$.

  > Must be abelian since quotient is cyclic.
  > If there's an element of order $p^2$, cyclic, done.
  > Else every element $a\neq 1$ must have order $p$.
  > Then $\gens{a}\neq G$, so pick $b$ in its complement, it has order $p$.
  > Call these two subgroups $H, K$ Recognize direct products: abelian implies both are normal, $H \intersect K = \ts{1}$.
  > and $\size HK = \size H \size K / \size(H \intersect K) = p\cdot p/1 = p^2$
:::

::: solution
**Goal:** Prove that every group of order $p^2$ (for $p$ prime) is abelian and isomorphic to either $C_{p^2}$ or $C_p \times C_p$.

<1>1. Every group $G$ of order $p^2$ is abelian.
    *Proof:*
    <2>1. By the class equation for the action of $G$ on itself by conjugation,
    $$|G| = |Z(G)| + \sum_{i=1}^k [G : C_G(x_i)],$$
    where the sum runs over representatives of non-central conjugacy classes.
    <2>2. For each non-central $x_i$, the centralizer $C_G(x_i)$ is a proper subgroup containing $Z(G)$ and $x_i$, so $[G : C_G(x_i)] > 1$.
    <2>3. Since $|G| = p^2$, each index $[G : C_G(x_i)]$ is a power of $p$ dividing $|G|$, hence $p \mid [G : C_G(x_i)]$.
    <2>4. Since $p \mid |G|$ and $p$ divides each index term, $p$ divides $|Z(G)|$. Since $e \in Z(G)$, $|Z(G)| \ge p > 0$, so $Z(G)$ is nontrivial.
    <2>5. By Lagrange's theorem, $|Z(G)| \in \{p, p^2\}$.
    <2>6. If $|Z(G)| = p$, then the quotient group $G/Z(G)$ has order $p^2/p = p$, so $G/Z(G)$ is cyclic.
    <2>7. Lemma: If $G/Z(G)$ is cyclic, then $G$ is abelian.
    *Proof of Lemma:* Let $G/Z(G) = \langle g Z(G) \rangle$. Any elements $x, y \in G$ can be written as $x = g^m z_1$ and $y = g^n z_2$ for some $m, n \in \mathbb{Z}$ and $z_1, z_2 \in Z(G)$. Then
    $$xy = (g^m z_1)(g^n z_2) = g^m g^n z_1 z_2 = g^{m+n} z_1 z_2 = g^n g^m z_2 z_1 = (g^n z_2)(g^m z_1) = yx.$$
    Thus $G$ is abelian, so $Z(G) = G$, contradicting $|Z(G)| = p$.
    <2>8. Therefore $|Z(G)| = p^2$, which means $Z(G) = G$, so $G$ is abelian.

<1>2. Classification of abelian groups of order $p^2$.
    *Proof:*
    <2>1. By Lagrange's theorem, the order of every element of $G$ divides $p^2$, so $o(g) \in \{1, p, p^2\}$ for all $g \in G$.
    <2>2. Case 1: $G$ contains an element $a$ of order $p^2$.
    Then the cyclic subgroup $\langle a \rangle$ has order $p^2 = |G|$, so $G = \langle a \rangle \cong C_{p^2}$.
    <2>3. Case 2: Every non-identity element of $G$ has order $p$.
    Pick any $a \in G$ with $a \neq e$, and set $H = \langle a \rangle \cong C_p$.
    Since $|H| = p < p^2$, choose an element $b \in G \setminus H$. The subgroup $K = \langle b \rangle$ has order $p$.
    <2>4. The intersection $H \cap K$ is a subgroup of $H$. Since $|H| = p$ is prime, $|H \cap K| \in \{1, p\}$. Because $b \in K \setminus H$, $H \cap K \neq K$, so $H \cap K = \{e\}$.
    <2>5. Since $G$ is abelian, every subgroup is normal, so $H \trianglelefteq G$ and $K \trianglelefteq G$.
    <2>6. By the product formula,
    $$|HK| = \frac{|H| \cdot |K|}{|H \cap K|} = \frac{p \cdot p}{1} = p^2 = |G|,$$
    so $G = HK$.
    <2>7. The map $\psi: H \times K \to G$ defined by $\psi(h, k) = hk$ is a homomorphism (since $G$ is abelian) with trivial kernel (since $H \cap K = \{e\}$) and full image $HK = G$.
    <2>8. Thus $\psi$ is an isomorphism, so $G \cong H \times K \cong C_p \times C_p$.

<1>3. Conclusion:
    *Proof:*
    Up to isomorphism, the only groups of order $p^2$ are $C_{p^2}$ and $C_p \times C_p$. Both are abelian.
:::
