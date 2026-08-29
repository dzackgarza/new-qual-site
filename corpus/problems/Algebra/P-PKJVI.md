---
schema: qual/card@1
id: P-PKJVI
kind: problem
title: Groups of order $pq$ with $p>q$ have a proper nontrivial normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $G$ be a group of order $|G| = p q$, where $p$ and $q$ are distinct primes with $p > q$.
Prove that $G$ possesses a unique (and hence normal) Sylow $p$-subgroup of order $p$.
:::

::: solution
**Goal:** Prove that the Sylow $p$-subgroup of a group of order $pq$ ($p > q$) is normal ($n_p = 1$).

<1>1. Application of Sylow's Theorems for $n_p$:
    *Proof:*
    <2>1. Let $n_p$ be the number of Sylow $p$-subgroups of $G$.
    <2>2. By Sylow's Third Theorem, $n_p$ satisfies:
        - $n_p$ divides the index $[G : P_p] = \frac{p q}{p} = q$.
        - $n_p \equiv 1 \pmod p$.

<1>2. Analysis of the Divisors of $q$:
    *Proof:*
    <2>1. Since $q$ is a prime integer, the only positive integer divisors of $q$ are:
        $$n_p \in \{1, q\}.$$
    <2>2. If $n_p = q$:
        - Then $q \equiv 1 \pmod p$, which means $q = 1 + k p$ for some integer $k \ge 1$.
        - This implies $q \ge 1 + p > p$.
        - But this directly contradicts the given hypothesis that $p > q$!
    <2>3. Therefore, $n_p$ cannot equal $q$.
    <2>4. The only remaining possibility is:
        $$n_p = 1.$$

<1>3. Normality of the Unique Sylow $p$-subgroup:
    *Proof:*
    <2>1. Since $n_p = 1$, there exists a unique Sylow $p$-subgroup $P \le G$ of order $|P| = p$.
    <2>2. Because all Sylow $p$-subgroups are conjugate in $G$, $g P g^{-1} = P$ for all $g \in G$.
    <2>3. Thus $P \trianglelefteq G$ is a non-trivial ($|P| = p > 1$), proper ($|P| = p < p q = |G|$) normal subgroup of $G$.

<1>4. Conclusion:
    $G$ has a unique normal Sylow $p$-subgroup of order $p$. Q.E.D.
:::
