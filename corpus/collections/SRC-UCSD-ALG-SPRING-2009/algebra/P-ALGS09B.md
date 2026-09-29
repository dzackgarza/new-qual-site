---
schema: qual/card@1
id: P-ALGS09B
kind: problem
title: "Normal Sylow subgroups and non-abelian group of order 105"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 2 of the official UCSD Spring 2009 algebra qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Repaired the cyclic-by-cyclic gap using the conjugation action on C15 and corrected the nonnilpotence argument to use the nonnormal Sylow 3-subgroup.
---

::: {.problem}
Let $G$ be a group of order $105 = 3 \cdot 5 \cdot 7$.

(a) Suppose that $G$ does not have a normal Sylow 7-subgroup.
Show in this case that $G$ has a normal Sylow 3-subgroup and a normal Sylow 5-subgroup.
Prove then that $G$ is abelian, a contradiction.

(b) Show that there is a non-abelian group $G$ of order 105. Explain why your group $G$ is solvable, but not nilpotent.
:::

::: {.solution}
**Part (a).**

::: pf

::: {.pf-step #s1}

If the Sylow $7$-subgroup is not normal, then $n_7=15$.

::: pf-proof

Sylow's theorem gives
\[
n_7\mid 15,
\qquad
n_7\equiv1\pmod7.
\]
Hence $n_7\in\{1,15\}$, and the hypothesis excludes $1$.

:::

:::

::: pf-step

The Sylow $3$-subgroup is normal.

::: pf-proof

Sylow's theorem gives $n_3\mid35$ and $n_3\equiv1\pmod3$, so $n_3\in\{1,7\}$.
If $n_3=7$, then the seven Sylow $3$-subgroups contribute $7(3-1)=14$ nonidentity elements.
By step [](#s1){.pf-ref}, the fifteen Sylow $7$-subgroups contribute $15(7-1)=90$ nonidentity elements.
Distinct subgroups of prime order meet only in the identity, so these sets are disjoint.
Together with the identity this would give
\[
14+90+1=105
\]
elements, leaving no element of order $5$, contradicting Cauchy's theorem.
Thus $n_3=1$.

:::

:::

::: pf-step

The Sylow $5$-subgroup is normal.

::: pf-proof

Sylow's theorem gives $n_5\mid21$ and $n_5\equiv1\pmod5$, so $n_5\in\{1,21\}$.
If $n_5=21$, then the Sylow $5$-subgroups contribute $21(5-1)=84$ nonidentity elements, while the Sylow $7$-subgroups contribute $90$ by step [](#s1){.pf-ref}, impossible in a group of order $105$.
Hence $n_5=1$.

:::

:::

::: {.pf-step #s4}

If $P_3$ and $P_5$ denote the unique Sylow $3$- and $5$-subgroups, then
\[
N=P_3P_5\cong C_{15}
\]
is a normal subgroup of $G$.

::: pf-proof

Both subgroups are normal, and their coprime orders imply $P_3\cap P_5=1$.
For $x\in P_3$ and $y\in P_5$, the commutator $[x,y]$ belongs to both normal subgroups, hence to their trivial intersection.
Thus they commute elementwise and
\[
N=P_3\times P_5\cong C_3\times C_5\cong C_{15}.
\]
The product of normal subgroups is normal.

:::

:::

::: {.pf-step #s5}

The conjugation action of $G$ on $N$ is trivial.

::: pf-proof

Because $N\trianglelefteq G$, conjugation gives a homomorphism
\[
G\longrightarrow \operatorname{Aut}(N).
\]
Since $N$ is abelian, $N$ lies in the kernel, so the action factors through
\[
G/N\cong C_7.
\]
But
\[
|\operatorname{Aut}(C_{15})|=\varphi(15)=8.
\]
The image of a group of order $7$ in a group of order $8$ must be trivial.
Therefore every element of $G$ centralizes $N$.

:::

:::

::: pf-step

The group $G$ is abelian, a contradiction.

::: pf-proof

The quotient $G/N$ is cyclic of order $7$.
Choose $g\in G$ whose coset generates $G/N$.
Then $G=\langle N,g\rangle$.
By step [](#s5){.pf-ref}, $g$ commutes with every element of $N$, and $N$ is abelian by step [](#s4){.pf-ref}. Hence all generators of $G$ commute, so $G$ is abelian.
An abelian group has every subgroup normal, contradicting the assumption that its Sylow $7$-subgroup is not normal.

**Part (b).**

:::

:::

::: pf-step

There is a nonabelian group of order $21$ of the form
\[
H=C_7\rtimes C_3.
\]

::: pf-proof

Since
\[
\operatorname{Aut}(C_7)\cong C_6,
\]
there is an automorphism of order $3$.
Using the corresponding nontrivial homomorphism $C_3\to\operatorname{Aut}(C_7)$ gives a semidirect product $H=C_7\rtimes C_3$.
The action is nontrivial, so $H$ is nonabelian.

:::

:::

::: pf-step

The group
\[
G=H\times C_5
\]
is a nonabelian group of order $105$.

::: pf-proof

Its order is $21\cdot5=105$, and it contains the nonabelian factor $H$.

:::

:::

::: pf-step

The group $G$ is solvable.

::: pf-proof

The subgroup $C_7\trianglelefteq H$ has cyclic quotient $C_3$, so $H$ is solvable.
Taking the direct product with the abelian group $C_5$ preserves solvability.
Equivalently,
\[
1\trianglelefteq C_7\trianglelefteq H\trianglelefteq H\times C_5
\]
has abelian successive quotients $C_7$, $C_3$, and $C_5$.

:::

:::

::: pf-step

The group $G$ is not nilpotent.

::: pf-proof

In the nontrivial semidirect product $H=C_7\rtimes C_3$, a Sylow $3$-subgroup is not normal; otherwise both Sylow subgroups of $H$ would be normal and, having coprime orders, would commute, forcing $H$ to be the direct product $C_7\times C_3$ and hence abelian.
Therefore the corresponding Sylow $3$-subgroup of $G=H\times C_5$ is not normal.
Every finite nilpotent group has all Sylow subgroups normal, so $G$ is not nilpotent.

:::

:::

:::

:::
