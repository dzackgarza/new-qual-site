---
schema: qual/card@1
id: P-BKF03-2A
kind: problem
title: Eight pairwise nonisomorphic groups of order $36$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 2A of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the Sylow-subgroup and center invariants distinguishing all eight groups.
---

::: {.problem}
List eight groups of order 36 and prove that they are not isomorphic.
:::

::: {.solution}
Write $C_m$ for the cyclic group of order $m$ and $D_{18}$ for the dihedral group of order $18$.
Consider
\[
\begin{aligned}
G_1&=C_2\times C_2\times C_3\times C_3,\\
G_2&=C_2\times C_2\times C_9,\\
G_3&=C_4\times C_3\times C_3,\\
G_4&=C_4\times C_9,\\
G_5&=C_6\times S_3,\\
G_6&=S_3\times S_3,\\
G_7&=C_2\times D_{18},\\
G_8&=C_3\times A_4.
\end{aligned}
\]
Each has order $36$.

<1>1. The four abelian groups $G_1,G_2,G_3,G_4$ are pairwise nonisomorphic.
::: {.proof}
For a finite abelian group, the Sylow subgroups are characteristic and therefore are isomorphism invariants.
Their Sylow $2$- and $3$-subgroups are
\[
\begin{array}{c|c|c}
 & \text{Sylow }2 & \text{Sylow }3\\ \hline
G_1 & C_2\times C_2 & C_3\times C_3\\
G_2 & C_2\times C_2 & C_9\\
G_3 & C_4 & C_3\times C_3\\
G_4 & C_4 & C_9.
\end{array}
\]
The four ordered pairs of Sylow-subgroup isomorphism types are distinct, so the four groups are pairwise nonisomorphic.
:::

<1>2. None of $G_1,G_2,G_3,G_4$ is isomorphic to any of $G_5,G_6,G_7,G_8$.
::: {.proof}
The first four groups are abelian.
The last four are nonabelian because each contains a nonabelian direct factor: $S_3$, $D_{18}$, or $A_4$.
Abelianity is preserved by isomorphism.
:::

<1>3. Among $G_5,G_6,G_7,G_8$, only $G_7$ has a cyclic Sylow $3$-subgroup.
::: {.proof}
A Sylow $3$-subgroup of $D_{18}$ is its rotation subgroup $C_9$.
Hence a Sylow $3$-subgroup of
\[
G_7=C_2\times D_{18}
\]
is $C_9$, which is cyclic.

For $G_5=C_6\times S_3$, a Sylow $3$-subgroup is $C_3\times C_3$.
The same is true for $G_6=S_3\times S_3$.
Finally, $A_4$ has Sylow $3$-subgroups of order $3$, so a Sylow $3$-subgroup of $G_8=C_3\times A_4$ is again $C_3\times C_3$.
Thus only $G_7$ has cyclic Sylow $3$-subgroup.
:::

<1>4. Among the remaining groups $G_5,G_6,G_8$, only $G_8$ has a normal Sylow $2$-subgroup.
::: {.proof}
The Klein four subgroup $V_4\triangleleft A_4$ is the unique Sylow $2$-subgroup of $A_4$.
Hence $\{1\}\times V_4$ is a normal Sylow $2$-subgroup of $G_8=C_3\times A_4$.

In $S_3$, no Sylow $2$-subgroup is normal.
Therefore neither $C_6\times S_3$ nor $S_3\times S_3$ has a normal Sylow $2$-subgroup: projecting a normal Sylow $2$-subgroup to an $S_3$ factor would give a normal Sylow $2$-subgroup there.
:::

<1>5. The remaining groups $G_5$ and $G_6$ are not isomorphic because their centers are different.
::: {.proof}
Since $Z(S_3)=1$,
\[
Z(G_6)=Z(S_3)\times Z(S_3)=1.
\]
On the other hand,
\[
Z(G_5)=Z(C_6)\times Z(S_3)=C_6\times1\cong C_6,
\]
which is nontrivial.
Thus $G_5\not\cong G_6$.
:::

The preceding invariants distinguish all eight groups, so they are pairwise nonisomorphic.
:::
