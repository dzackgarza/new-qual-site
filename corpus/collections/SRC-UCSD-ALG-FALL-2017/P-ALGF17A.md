---
schema: qual/card@1
id: P-ALGF17A
kind: problem
title: Groups of order $231$ as $\mathbb{Z}_{77} \rtimes \mathbb{Z}_3$; two isomorphism types
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 1 of the official UCSD Algebra Qualifying Exam, Fall 2017; both parts agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the Sylow argument giving a normal cyclic subgroup of order 77 and the classification of C3-actions through Aut(C77), yielding exactly two isomorphism types.
---

::: {.problem}
Let $G$ be a group of order $231 = (3)(7)(11)$.

(a) Show that $G$ is isomorphic to a semidirect product $\mathbb{Z}_{77} \rtimes \mathbb{Z}_3$.

(b) Show that there are precisely two groups $G$ of order $231$ up to isomorphism.
:::

::: {.solution}
<1>1. The Sylow $11$-subgroup and the Sylow $7$-subgroup of $G$ are both normal.
::: {.proof}
Let $n_{11}$ be the number of Sylow $11$-subgroups. Sylow's theorem gives
\[
n_{11}\equiv1\pmod{11},
\qquad
n_{11}\mid21.
\]
The divisors of $21$ are $1,3,7,21$, and only $1$ is congruent to $1$ modulo $11$. Hence
\[
n_{11}=1.
\]
Thus the Sylow $11$-subgroup $P_{11}$ is normal.

Similarly,
\[
n_7\equiv1\pmod7,
\qquad
n_7\mid33.
\]
The divisors of $33$ are $1,3,11,33$, and only $1$ is congruent to $1$ modulo $7$. Hence
\[
n_7=1,
\]
so the Sylow $7$-subgroup $P_7$ is normal.
:::

<1>2. The product $H:=P_7P_{11}$ is a normal cyclic subgroup of order $77$.
::: {.proof}
Since $P_7$ and $P_{11}$ are normal, their product is a subgroup and is normal in $G$.
Their orders are coprime, so
\[
P_7\cap P_{11}=1
\]
and therefore
\[
|H|=|P_7||P_{11}|=77.
\]
Moreover, for $x\in P_7$ and $y\in P_{11}$, the commutator $[x,y]$ lies in both $P_7$ and $P_{11}$ because both subgroups are normal. Hence
\[
[x,y]\in P_7\cap P_{11}=1.
\]
Thus the two subgroups commute elementwise and
\[
H\cong P_7\times P_{11}
\cong C_7\times C_{11}
\cong C_{77}.
\]
:::

<1>3. One has
\[
G\cong C_{77}\rtimes C_3.
\]
::: {.proof}
Let $Q$ be a Sylow $3$-subgroup of $G$. Then
\[
|Q|=3,
\qquad
Q\cong C_3.
\]
Since $|H|=77$ is relatively prime to $3$,
\[
H\cap Q=1.
\]
Also
\[
|HQ|=\frac{|H||Q|}{|H\cap Q|}=77\cdot3=231=|G|.
\]
Hence $G=HQ$. Since $H\triangleleft G$, this is an internal semidirect product:
\[
G\cong H\rtimes Q
\cong C_{77}\rtimes C_3.
\]
This proves part (a).
:::

<1>4. Up to isomorphism there are only two possible actions of $C_3$ on $C_{77}$.
::: {.proof}
A semidirect product $C_{77}\rtimes C_3$ is determined by a homomorphism
\[
\theta:C_3\longrightarrow\operatorname{Aut}(C_{77}).
\]
By the Chinese remainder theorem,
\[
C_{77}\cong C_7\times C_{11},
\]
and consequently
\[
\operatorname{Aut}(C_{77})
\cong
\operatorname{Aut}(C_7)\times\operatorname{Aut}(C_{11})
\cong C_6\times C_{10}.
\]
The group $C_{10}$ has no nontrivial element of order dividing $3$, while $C_6$ has a unique subgroup of order $3$.
Therefore the image of $\theta$ is either trivial or is that unique subgroup of order $3$.

There are two injective homomorphisms from $C_3$ onto that subgroup, differing by inversion on $C_3$. Precomposing the action with the automorphism
\[
C_3\longrightarrow C_3,
\qquad
q\longmapsto q^{-1},
\]
produces an isomorphic semidirect product. Hence all nontrivial actions yield one isomorphism type.
Thus there are at most two isomorphism types: the trivial action and the nontrivial action.
:::

<1>5. The two actions yield nonisomorphic groups, so there are exactly two groups of order $231$ up to isomorphism.
::: {.proof}
For the trivial action one obtains the direct product
\[
C_{77}\times C_3\cong C_{231},
\]
which is abelian.
For the nontrivial action, the image of $C_3$ in $\operatorname{Aut}(C_{77})$ is nontrivial, so some element of $C_3$ fails to commute with some element of $C_{77}$. Hence the resulting semidirect product is nonabelian.
Therefore the two groups are not isomorphic.
By <1>3 and <1>4, every group of order $231$ is one of these two types.
Thus there are precisely two isomorphism classes.
:::
:::
