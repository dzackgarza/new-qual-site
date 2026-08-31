---
schema: qual/card@1
id: P-ALGF19A
kind: problem
title: Non-Sylow $p$-subgroup has $p$ dividing $|N_G(P)/P|$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Suppose $G$ is a finite group and $P$ is a $p$-subgroup of $G$ which is not a Sylow $p$-subgroup.
Prove that $p$ divides $|N_G(P)/P|$.
:::

::: {.solution}
<1>1. Containment in a strictly larger Sylow $p$-subgroup:
<2>1. By the Sylow Theorems, every $p$-subgroup of a finite group $G$ is contained in some Sylow $p$-subgroup.
Since $P$ is not a Sylow $p$-subgroup, there exists a Sylow $p$-subgroup $Q \le G$ such that:
\[
P \subsetneq Q.
\]

<1>2. Action of $P$ on the coset space $Q/P$:
<2>1. Let $X = Q/P = \{xP \mid x \in Q\}$ be the set of left cosets of $P$ in $Q$.
Because $P \subsetneq Q$ and $Q$ is a $p$-group, $|X| = [Q : P] = p^k$ for some integer $k \ge 1$.
<2>2. Let $P$ act on $X$ by left multiplication: $y \cdot (xP) = (yx)P$ for $y \in P, x \in Q$.
Since $P$ is a $p$-group, the number of fixed points satisfies the fixed point congruence:
\[
|X^P| \equiv |X| \equiv 0 \pmod p.
\]
<2>3. A coset $xP \in X$ is fixed by $P$ if and only if:
\[
y x P = x P \quad \forall y \in P \iff x^{-1} y x \in P \quad \forall y \in P \iff x \in N_Q(P).
\]
Therefore the fixed point set is $X^P = N_Q(P) / P$.
<2>4. The coset $eP = P$ is always fixed, so $|X^P| \ge 1$.
Since $p \mid |X^P|$ and $|X^P| \ge 1$, we have $|X^P| = [N_Q(P) : P] \ge p$, and:
\[
p \mid [N_Q(P) : P].
\]

<1>3. Divisibility of $|N_G(P)/P|$:
<2>1. Since $N_Q(P) = N_G(P) \cap Q$, we have the tower of subgroups $P \le N_Q(P) \le N_G(P)$.
By the multiplicativity of subgroup indices:
\[
|N_G(P) / P| = [N_G(P) : P] = [N_G(P) : N_Q(P)] \cdot [N_Q(P) : P].
\]
<2>2. Since $p$ divides $[N_Q(P) : P]$, $p$ divides $|N_G(P)/P|$.

<1>4. Conclusion:
$p$ divides $|N_G(P)/P|$. Q.E.D.
:::
