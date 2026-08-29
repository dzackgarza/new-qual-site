---
schema: qual/card@1
id: P-6FFAX
kind: problem
title: Groups of order $45$ are abelian
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Abelian Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: problem
- Show that all groups of order 45 are abelian.
:::

::: solution
**Goal:** Prove that every group of order $45$ is abelian.

<1>1. Normality of Sylow subgroups:
    *Proof:*
    <2>1. The order of $G$ is $|G| = 45 = 3^2 \cdot 5 = 9 \cdot 5$.
    <2>2. **Sylow 5-subgroups:** By the Sylow theorems, $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 9$.
        The divisors of $9$ are $\{1, 3, 9\}$, and only $1 \equiv 1 \pmod 5$.
        Thus $n_5 = 1$, so the unique Sylow 5-subgroup $Q \in \operatorname{Syl}_5(G)$ is normal ($Q \trianglelefteq G$), with $Q \cong \mathbb{Z}_5$.
    <2>3. **Sylow 3-subgroups:** By the Sylow theorems, $n_3 \equiv 1 \pmod 3$ and $n_3 \mid 5$.
        The divisors of $5$ are $\{1, 5\}$. Since $5 \equiv 2 \not\equiv 1 \pmod 3$, we have $n_3 = 1$.
        Thus the unique Sylow 3-subgroup $P \in \operatorname{Syl}_3(G)$ of order $9$ is normal ($P \trianglelefteq G$).

<1>2. $P$ is abelian:
    *Proof:*
    <2>1. The order of $P$ is $p^2 = 3^2$.
    <2>2. Every group of order $p^2$ (for $p$ prime) is abelian: the center $Z(P)$ is non-trivial ($|Z(P)| \in \{p, p^2\}$), so $P / Z(P)$ cannot have order $p$ (since cyclic quotient by center implies abelian), forcing $Z(P) = P$.
    <2>3. Thus $P$ is abelian (either $\mathbb{Z}_9$ or $\mathbb{Z}_3 \times \mathbb{Z}_3$).

<1>3. Direct product decomposition:
    *Proof:*
    <2>1. Since $|P| = 9$ and $|Q| = 5$ are coprime, $P \cap Q = \{e\}$.
    <2>2. The product $PQ$ has order $|PQ| = \frac{|P| |Q|}{|P \cap Q|} = 45 = |G|$, so $G = PQ$.
    <2>3. Because both $P \trianglelefteq G$ and $Q \trianglelefteq G$, $G$ is the internal direct product:
        $$G \cong P \times Q.$$

<1>4. Conclusion:
    $G$ is the direct product of two abelian groups ($P$ and $Q$), so $G$ is abelian (isomorphic to either $\mathbb{Z}_{45}$ or $\mathbb{Z}_3 \times \mathbb{Z}_{15}$). Q.E.D.
:::
