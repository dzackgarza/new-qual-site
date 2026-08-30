---
schema: qual/card@1
id: P-ALGS24A
kind: problem
title: Groups of order $p^2 q$ are solvable
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Suppose $p$ and $q$ are two distinct primes and $G$ is a group of order $p^2 q$.
Prove that $G$ is solvable.
:::

::: {.solution}
<1>1. Apply Sylow’s Theorems to count Sylow subgroups: <2>1. Let $n_p$ and $n_q$ denote the number of Sylow $p$-subgroups and Sylow $q$-subgroups of $G$, respectively.
Proof: definition.
<2>2. By Sylow’s Theorem:
\[
n_p \equiv 1 \pmod p \quad \text{and} \quad n_p \mid q \implies n_p \in \{1, q\},
\]
\[
n_q \equiv 1 \pmod q \quad \text{and} \quad n_q \mid p^2 \implies n_q \in \{1, p, p^2\}.
\]
Proof: Sylow's Theorem.

<1>2. Show that $G$ has a normal Sylow subgroup: <2>1. **Case $p > q$:** Since $n_p \mid q$ and $n_p \equiv 1 \pmod p$, if $n_p = q$ then $q \equiv 1 \pmod p \implies q \ge p + 1 > p$, contradicting $p > q$.
Thus $n_p = 1$, so the Sylow $p$-subgroup $P \trianglelefteq G$ is normal.
Proof: $n_p \in \{1, q\}$ and $q < p$.
<2>2. **Case $p < q$:** If $n_q = 1$, then the Sylow $q$-subgroup $Q \trianglelefteq G$ is normal.
Proof: $n_q = 1 \implies Q \trianglelefteq G$.
<2>3. If $n_q > 1$, then $n_q \in \{p, p^2\}$.
Since $p < q$, $p \not\equiv 1 \pmod q$, so $n_q = p^2$.
Proof: $p < q \implies p \not\ge q + 1$.
<2>4. $n_q = p^2 \implies p^2 \equiv 1 \pmod q \implies q \mid (p^2 - 1) = (p-1)(p+1)$.
Proof: Sylow congruence $n_q \equiv 1 \pmod q$.
<2>5. Since $q$ is prime and $q > p > p - 1$, $q$ must divide $p + 1$, so $q \le p + 1$.
With $p < q$, this forces $q = p + 1$, so $p = 2$ and $q = 3$.
Proof: the only consecutive primes are $2$ and $3$.
<2>6. For $|G| = 2^2 \cdot 3 = 12$: if $n_3 = 4$, the four Sylow 3-subgroups contain $4 \times (3 - 1) = 8$ distinct elements of order 3. Proof: distinct subgroups of prime order intersect trivially.
<2>7. The remaining $12 - 8 = 4$ elements must comprise the unique Sylow 2-subgroup of order 4, so $n_2 = 1$ and $P \trianglelefteq G$.
Proof: counting elements in $G$.
<2>8. In all cases, $G$ contains a normal Sylow subgroup $N \trianglelefteq G$ of order $p^2$ or $q$.
Proof: <2>1, <2>2, and <2>7.

<1>3. Prove that $G$ is solvable: <2>1. If $N \trianglelefteq G$ has order $p^2$, then $N$ is abelian (any group of order $p^2$ is abelian), hence solvable.
The quotient $G/N$ has order $q$ (prime), hence cyclic and solvable.
Proof: groups of order $p^2$ and $p$ are abelian.
<2>2. If $N \trianglelefteq G$ has order $q$, then $N$ is cyclic of prime order, hence solvable.
The quotient $G/N$ has order $p^2$, hence abelian and solvable.
Proof: <2>1. <2>3. Since $N$ and $G/N$ are both solvable, $G$ is solvable.
Proof: extension of a solvable group by a solvable group is solvable.

<1>4. Conclusion: Every group of order $p^2 q$ is solvable.
Q.E.D. Proof: <1>2 and <1>3.
:::
