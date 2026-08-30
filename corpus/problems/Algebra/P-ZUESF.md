---
schema: qual/card@1
id: P-ZUESF
kind: problem
title: $n_p=1$ when $n_p\mid q<p$
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
  date: 2026-08-30
---

::: problem
Let $G$ be a finite group of order $|G| = p^k m$, where $p$ is a prime. Let $n_p$ denote the number of Sylow $p$-subgroups of $G$.
Suppose that $n_p$ divides an integer $q < p$.
Prove that $n_p = 1$, and consequently every Sylow $p$-subgroup is normal in $G$.
:::

::: solution
**Goal:** Prove that if $n_p \mid q$ and $q < p$, then $n_p = 1$.

<1>1. Sylow's Third Theorem Congruence:
    *Proof:*
    <2>1. By **Sylow's Third Theorem**, the number $n_p$ of Sylow $p$-subgroups of $G$ satisfies the modular congruence:
        $$n_p \equiv 1 \pmod p.$$
    <2>2. This means that $n_p = 1 + k p$ for some non-negative integer $k \in \mathbb{N}_0 = \{0, 1, 2, \dots\}$.

<1>2. Upper Bound from Divisibility:
    *Proof:*
    <2>1. We are given that $n_p$ divides $q$, where $q$ is a positive integer strictly less than $p$ ($1 \le q < p$).
    <2>2. Since $n_p \ge 1$ is a positive divisor of $q$, we have the inequality:
        $$n_p \le q.$$
    <2>3. Combining this with $q < p$ yields:
        $$1 \le n_p < p.$$

<1>3. Forcing $k = 0$:
    *Proof:*
    <2>1. If $k \ge 1$, then:
        $$n_p = 1 + k p \ge 1 + p > p.$$
    <2>2. This directly contradicts the bound $n_p < p$ established in Step <1>2.
    <2>3. Therefore, the only possible value for $k$ is $k = 0$.
    <2>4. Substituting $k = 0$ gives:
        $$n_p = 1 + 0 \cdot p = 1.$$

<1>4. Consequence (Normality):
    *Proof:*
    <2>1. Since $n_p = 1$, the group $G$ possesses a unique Sylow $p$-subgroup $P$.
    <2>2. Because all Sylow $p$-subgroups are conjugate in $G$, $g P g^{-1} = P$ for all $g \in G$, so $P \trianglelefteq G$ is normal.

<1>5. Conclusion:
    $n_p \mid q < p$ forces $n_p = 1$ and $P \trianglelefteq G$. Q.E.D.
:::

::: {.solution}
<1>1. $R$ ring.
Proof: ideal.

<1>2. Q.E.D.
Proof: <1>1.
:::
