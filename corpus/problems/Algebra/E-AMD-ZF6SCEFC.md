---
schema: qual/card@1
id: E-AMD-ZF6SCEFC
kind: problem
title: Groups of order $p^2q^2$ are abelian when $q\nmid p^2-1$ and $p\nmid q^2-1$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Abelian Groups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
Show that a group of order $p^2 q^2$ where $q$ does not divide $p^2-1$ and $p$ does not divide $q^2-1$ is abelian.
:::

::: solution
**Goal:** Prove that a group $G$ of order $|G| = p^2 q^2$ (with distinct primes $p$ and $q$) satisfying $q \nmid (p^2 - 1)$ and $p \nmid (q^2 - 1)$ is abelian.

<1>1. Sylow subgroup count constraints:
    *Proof:*
    <2>1. Let $n_p$ denote the number of Sylow $p$-subgroups and $n_q$ the number of Sylow $q$-subgroups of $G$.
    <2>2. By Sylow's Third Theorem, $n_p$ divides $[G : P] = q^2$ and $n_p \equiv 1 \pmod p$.
    <2>3. The positive divisors of $q^2$ are $1, q, q^2$.
    <2>4. If $n_p = q$, then $q \equiv 1 \pmod p$, which implies $p \mid (q - 1)$. Since $q - 1 \mid (q^2 - 1)$, this would mean $p \mid (q^2 - 1)$, contradicting the hypothesis $p \nmid (q^2 - 1)$.
    <2>5. If $n_p = q^2$, then $q^2 \equiv 1 \pmod p$, which means $p \mid (q^2 - 1)$, again contradicting $p \nmid (q^2 - 1)$.
    <2>6. Therefore $n_p = 1$, which proves that the unique Sylow $p$-subgroup $P$ is normal: $P \trianglelefteq G$.

<1>2. Normality of the Sylow $q$-subgroup:
    *Proof:*
    <2>1. Symmetrically, $n_q$ divides $[G : Q] = p^2$ and $n_q \equiv 1 \pmod q$.
    <2>2. The positive divisors of $p^2$ are $1, p, p^2$.
    <2>3. If $n_q = p$, then $p \equiv 1 \pmod q \implies q \mid (p - 1) \implies q \mid (p^2 - 1)$, contradicting $q \nmid (p^2 - 1)$.
    <2>4. If $n_q = p^2$, then $p^2 \equiv 1 \pmod q \implies q \mid (p^2 - 1)$, contradicting $q \nmid (p^2 - 1)$.
    <2>5. Therefore $n_q = 1$, so the unique Sylow $q$-subgroup $Q$ is normal: $Q \trianglelefteq G$.

<1>3. Direct product structure $G \cong P \times Q$:
    *Proof:*
    <2>1. Since $|P| = p^2$ and $|Q| = q^2$ with $\gcd(p^2, q^2) = 1$, Lagrange's Theorem implies $P \cap Q = \{e\}$.
    <2>2. Since $P \trianglelefteq G$ and $Q \trianglelefteq G$, the product $PQ$ is a normal subgroup of $G$ with cardinality
    $$|PQ| = \frac{|P| \cdot |Q|}{|P \cap Q|} = \frac{p^2 q^2}{1} = p^2 q^2 = |G|.$$
    Thus $G = PQ$.
    <2>3. For any $x \in P$ and $y \in Q$, consider the commutator $[x, y] = x y x^{-1} y^{-1} = (x y x^{-1}) y^{-1} = x (y x^{-1} y^{-1})$.
    <2>4. Since $Q \trianglelefteq G$, $x y x^{-1} \in Q$, so $[x, y] \in Q y^{-1} = Q$.
    <2>5. Since $P \trianglelefteq G$, $y x^{-1} y^{-1} \in P$, so $[x, y] \in x P = P$.
    <2>6. Thus $[x, y] \in P \cap Q = \{e\}$, which proves $xy = yx$ for all $x \in P, y \in Q$.
    <2>7. Therefore the internal product map $(x, y) \mapsto xy$ is an isomorphism $G \cong P \times Q$.

<1>4. Abelian property of $P$ and $Q$:
    *Proof:*
    <2>1. Every group of order $p^2$ (for any prime $p$) is abelian (isomorphic to either $C_{p^2}$ or $C_p \times C_p$).
    <2>2. Thus $P$ is abelian, and $Q$ is abelian.
    <2>3. The direct product of two abelian groups is abelian, so $P \times Q \cong G$ is abelian.

<1>5. Conclusion:
    *Proof:*
    The group $G$ is abelian.
:::
