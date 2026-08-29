---
schema: qual/card@1
id: P-F6RAE
kind: problem
title: A normal $p$-subgroup is contained in every Sylow $p$-subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $G$ be a finite group, and let $N \trianglelefteq G$ be a normal $p$-subgroup of $G$ (for a prime $p$).
Prove that $N$ is contained in **every** Sylow $p$-subgroup of $G$.
:::

::: solution
**Goal:** Prove that if $N \trianglelefteq G$ is a $p$-subgroup and $P \le G$ is any Sylow $p$-subgroup, then $N \subseteq P$.

<1>1. Setting and Sylow's Second Theorem:
    *Proof:*
    <2>1. Let $P$ be an arbitrary Sylow $p$-subgroup of $G$.
    <2>2. By **Sylow's Second Theorem**, every $p$-subgroup of $G$ is contained in *some* Sylow $p$-subgroup of $G$.
    <2>3. Since $N$ is a $p$-subgroup of $G$, there exists at least one Sylow $p$-subgroup $Q \le G$ such that:
        $$N \subseteq Q.$$

<1>2. Using Normality and Sylow Conjugacy:
    *Proof:*
    <2>1. By Sylow's Theorem, all Sylow $p$-subgroups of $G$ are conjugate to each other.
    <2>2. In particular, for our given Sylow $p$-subgroup $P$, there exists an element $g \in G$ such that:
        $$P = g Q g^{-1}.$$
    <2>3. Conjugating both sides of the inclusion $N \subseteq Q$ by $g$:
        $$g N g^{-1} \subseteq g Q g^{-1} = P.$$
    <2>4. Since $N \trianglelefteq G$ is **normal** in $G$, $g N g^{-1} = N$.
    <2>5. Substituting $g N g^{-1} = N$ gives:
        $$N \subseteq P.$$

<1>3. Alternative Direct Proof via the Subgroup $N P$:
    *Proof:*
    <2>1. Since $N \trianglelefteq G$, the product $N P$ is a subgroup of $G$.
    <2>2. By the Second Isomorphism Theorem, $|N P| = \frac{|N| \cdot |P|}{|N \cap P|}$.
    <2>3. Since both $|N|$ and $|P|$ are powers of $p$, $|N P|$ is a power of $p$, so $N P$ is a $p$-subgroup of $G$.
    <2>4. Since $P \subseteq N P$ and $P$ is a Sylow $p$-subgroup (a $p$-subgroup of maximal possible size in $G$), we must have $N P = P$.
    <2>5. Therefore, $N \subseteq N P = P$.

<1>4. Conclusion:
    $N$ is contained in every Sylow $p$-subgroup $P$ of $G$ (and in fact $N \subseteq \bigcap_{g \in G} g P g^{-1} = O_p(G)$, the $p$-core of $G$). Q.E.D.
:::
