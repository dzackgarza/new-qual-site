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

::: {.solution}
<1>1. Sylow's Third Theorem Congruence:
<2>1. By Sylow’s Third Theorem, the number $n_p$ of Sylow $p$-subgroups of $G$ satisfies:
\[
n_p \equiv 1 \pmod p.
\]
Proof: Sylow's Third Theorem.
<2>2. Thus $n_p = 1 + k p$ for some non-negative integer $k \in \{0, 1, 2, \dots\}$.
Proof: definition of modular congruence for positive integers.

<1>2. Upper Bound from Divisibility:
<2>1. We are given that $n_p$ divides $q$, where $q$ is a positive integer strictly less than $p$ ($1 \le q < p$).
Proof: hypothesis.
<2>2. Since $n_p \ge 1$ divides $q$, we have $n_p \le q$.
Proof: a positive divisor of a positive integer is less than or equal to the integer.
<2>3. Combining this with $q < p$ yields:
\[
1 \le n_p < p.
\]
Proof: transitivity of order relation.

<1>3. Deduce that $n_p = 1$:
<2>1. If $k \ge 1$, then:
\[
n_p = 1 + k p \ge 1 + p > p,
\]
which contradicts $n_p < p$ from <1>2.
Proof: $k \ge 1 \implies 1 + kp > p$.
<2>2. Therefore $k = 0$.
Proof: $k \in \mathbb{Z}_{\ge 0}$ and $k \not\ge 1$.
<2>3. Substituting $k = 0$ yields:
\[
n_p = 1 + 0 \cdot p = 1.
\]
Proof: <2>2.

<1>4. Consequence (Normality):
<2>1. Since $n_p = 1$, the group $G$ possesses a unique Sylow $p$-subgroup $P$.
Proof: $n_p = 1$.
<2>2. By Sylow’s Second Theorem, all Sylow $p$-subgroups of $G$ are conjugate to $P$.
Since $P$ is unique, $g P g^{-1} = P$ for all $g \in G$, so $P \trianglelefteq G$ is normal.
Proof: invariance under all inner automorphisms.

<1>5. Conclusion:
$n_p \mid q < p \implies n_p = 1$, and the unique Sylow $p$-subgroup is normal in $G$. Q.E.D.
Proof: <1>1 through <1>4.
:::
