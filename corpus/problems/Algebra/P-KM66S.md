---
schema: qual/card@1
id: P-KM66S
kind: problem
title: Solvable groups, a nonabelian example, solvability of $A_4$, and normality
  of its index-$3$ subgroup
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Permutations
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Define a solvable group.
Give an example of a solvable nonabelian group.

Show \(A_4\) is solvable.
Do the Sylow theorems tell you anything about whether this index 3 subgroup of \(A_4\) is normal?
:::

::: {.solution}
<1>1. Definition of a solvable group:
<2>1. A group $G$ is called **solvable** if it possesses a finite subnormal series:
\[
\{e\} = G_0 \triangleleft G_1 \triangleleft G_2 \triangleleft \cdots \triangleleft G_k = G
\]
such that each consecutive quotient group $G_{i+1}/G_i$ is abelian for all $i \in \{0, \dots, k-1\}$.
Equivalently, the derived series $G^{(0)} = G$, $G^{(n+1)} = [G^{(n)}, G^{(n)}]$ satisfies $G^{(k)} = \{e\}$ for some $k \ge 0$.
Proof: standard definition in group theory.

<1>2. Example of a solvable nonabelian group:
<2>1. The symmetric group on 3 elements $S_3$ has order $|S_3| = 6$.
It is nonabelian (e.g. $(12)(23) \neq (23)(12)$) and has the subnormal series:
\[
\{e\} \triangleleft A_3 \triangleleft S_3,
\]
where $A_3 \cong \mathbb{Z}/3\mathbb{Z}$ and $S_3/A_3 \cong \mathbb{Z}/2\mathbb{Z}$ are both abelian.
Proof: verification of subnormal series.

<1>3. Proof that $A_4$ is solvable:
<2>1. The alternating group $A_4$ has order $|A_4| = 12$.
Consider the Klein four-subgroup:
\[
V_4 = \{ e, (12)(34), (13)(24), (14)(23) \} \le A_4.
\]
Proof: $V_4$ is closed under multiplication and consists of permutations of cycle type $(2, 2)$ and the identity.
<2>2. Conjugation in $S_4$ preserves the cycle type of permutations, so $V_4 \triangleleft S_4$, which implies $V_4 \triangleleft A_4$.
Proof: normality of cycle type conjugacy classes.
<2>3. Form the subnormal series:
\[
\{e\} \triangleleft V_4 \triangleleft A_4.
\]
The quotient factors are:
- $V_4 / \{e\} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ (abelian),
- $A_4 / V_4$ has order $\frac{12}{4} = 3$, so $A_4 / V_4 \cong \mathbb{Z}/3\mathbb{Z}$ (abelian).
Thus $A_4$ is solvable.
Proof: abelian quotient criteria.

<1>4. Sylow theorems and normality of the index-3 subgroup:
<2>1. The subgroup $V_4$ has order $|V_4| = 4 = 2^2$.
Since $|A_4| = 12 = 2^2 \cdot 3$, $V_4$ is a Sylow 2-subgroup of $A_4$.
Proof: $|V_4| = 2^2$ is the highest power of 2 dividing $|A_4|$.
<2>2. By the Sylow Theorems, the number $n_2$ of Sylow 2-subgroups of $A_4$ satisfies:
\[
n_2 \mid 3 \quad \text{and} \quad n_2 \equiv 1 \pmod 2 \implies n_2 \in \{1, 3\}.
\]
Proof: Sylow congruence and divisibility.
<2>3. $A_4$ contains exactly 8 elements of order 3 (the eight 3-cycles) and exactly 3 elements of order 2 (the three double transpositions in $V_4$).
Since any Sylow 2-subgroup of order 4 contains 3 elements of order 2, and there are only 3 elements of order 2 in the entire group $A_4$, there cannot be more than one Sylow 2-subgroup.
Thus $n_2 = 1$.
Proof: element order count in $A_4$.
<2>4. By Sylow theory, a Sylow $p$-subgroup is normal if and only if $n_p = 1$.
Therefore, $V_4$ is the unique Sylow 2-subgroup of $A_4$, and is consequently a normal subgroup of $A_4$.
Proof: uniqueness of normal Sylow subgroups.

<1>5. Conclusion:
$A_4$ is solvable, and the Sylow theorems together with element counts establish that its unique Sylow 2-subgroup (the index-3 Klein four-group) is normal. Q.E.D.
Proof: <1>1 through <1>4.
:::
