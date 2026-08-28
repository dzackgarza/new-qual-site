---
schema: qual/card@1
id: E-AMD-DGMOEV2O
kind: exercise
title: $P\cap H\in\syl_p(H)$ for $P\in\syl_p(G)$ and $H\trianglelefteq G$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Let $P\in \operatorname{Syl}_p(G)$ where $H\trianglelefteq G$ and show that $P\cap H \in \operatorname{Syl}_p(H)$.
:::

::: solution
**Goal:** Prove that for a normal subgroup $H \trianglelefteq G$ of a finite group $G$ and any Sylow $p$-subgroup $P \in \operatorname{Syl}_p(G)$, the intersection $P \cap H$ is a Sylow $p$-subgroup of $H$.

<1>1. $P \cap H$ is a $p$-subgroup of $H$:
    *Proof:*
    <2>1. $P \cap H$ is a subgroup of $H$.
    <2>2. Since $P$ is a $p$-group, every subgroup of $P$ has order a power of $p$.
    <2>3. Thus $|P \cap H| = p^k$ for some integer $k \ge 0$.

<1>2. Index formula relating $[H : P \cap H]$ to $[G : P]$:
    *Proof:*
    <2>1. Because $H \trianglelefteq G$, the product $P H = H P$ is a subgroup of $G$.
    <2>2. By the Second Isomorphism Theorem, $P H / H \cong P / (P \cap H)$, so $|P H| = \frac{|P| |H|}{|P \cap H|}$.
    <2>3. Using Lagrange's Theorem for $P \cap H \le H \le P H \le G$:
        $$[G : P] = \frac{|G|}{|P|} = \frac{|G|}{|P H|} \cdot \frac{|P H|}{|P|} = [G : P H] \cdot \frac{|H|}{|P \cap H|} = [G : P H] \cdot [H : P \cap H].$$
    <2>4. Thus $[H : P \cap H]$ divides $[G : P]$.

<1>3. Sylow $p$-subgroup deduction:
    *Proof:*
    <2>1. By definition of $P \in \operatorname{Syl}_p(G)$, the index $[G : P]$ is coprime to $p$, meaning $p \nmid [G : P]$.
    <2>2. Since $[H : P \cap H]$ divides $[G : P]$, $p$ cannot divide $[H : P \cap H]$.
    <2>3. Therefore, $P \cap H$ is a $p$-subgroup of $H$ of maximal possible $p$-power order, which means $P \cap H \in \operatorname{Syl}_p(H)$.

<1>4. Conclusion:
    $P \cap H$ is a Sylow $p$-subgroup of $H$. Q.E.D.
:::
