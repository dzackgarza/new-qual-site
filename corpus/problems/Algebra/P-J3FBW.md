---
schema: qual/card@1
id: P-J3FBW
kind: problem
title: Groups of order $28$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Classify the groups of order $28$ up to isomorphism.
:::

::: {.solution}
There are exactly four isomorphism types.

<1>1. Every group $G$ of order $28$ has a normal Sylow $7$-subgroup $P\cong C_7$ and a Sylow $2$-subgroup $Q$ of order $4$.
::: {.proof}
Sylow gives
\[
n_7\equiv1\pmod7,
\qquad
n_7\mid4,
\]
so $n_7=1$. Thus $P\trianglelefteq G$ and $P\cong C_7$. A Sylow $2$-subgroup $Q$ has order $4$, hence
\[
Q\cong C_4
\quad\text{or}\quad
Q\cong C_2\times C_2.
\]
Since $P\cap Q=1$ and $|P||Q|=28$, we have $G=PQ$, so
\[
G\cong C_7\rtimes_\theta Q
\]
for some action
\[
\theta:Q\longrightarrow\Aut(C_7)\cong C_6.
\]
:::

<1>2. If $Q\cong C_4$, there are exactly two isomorphism types.
::: {.proof}
The image of a homomorphism $C_4\to C_6$ has order dividing both $4$ and $6$, hence has order $1$ or $2$.

For the trivial action,
\[
G\cong C_7\times C_4\cong C_{28}.
\]
For a nontrivial action, a generator of $C_4$ acts by the unique involution in $\Aut(C_7)$, namely inversion. Up to automorphisms of $C_4$ and $C_7$, there is only one such action. It gives
\[
C_7\rtimes C_4
=\langle a,t\mid a^7=t^4=1,\ tat^{-1}=a^{-1}\rangle.
\]
:::

<1>3. If $Q\cong C_2\times C_2$, there are exactly two isomorphism types.
::: {.proof}
Any homomorphism
\[
C_2^2\longrightarrow C_6
\]
has image contained in the unique subgroup of order $2$ of $C_6$.

The trivial action gives
\[
G\cong C_7\times C_2^2\cong C_{14}\times C_2.
\]
Any nontrivial action is a surjection $C_2^2\to C_2$. All nonzero homomorphisms $C_2^2\to C_2$ are equivalent under $\Aut(C_2^2)\cong GL_2(\FF_2)$, so there is one nontrivial isomorphism type. Choosing generators $s,u$ with $s$ acting by inversion and $u$ acting trivially gives
\[
G\cong (C_7\rtimes C_2)\times C_2.
\]
:::

<1>4. The four groups are pairwise nonisomorphic.
::: {.proof}
The first two listed direct products are the two abelian groups of order $28$, one cyclic and one noncyclic. The two nonabelian groups have nonisomorphic Sylow $2$-subgroups: one has a cyclic Sylow $2$-subgroup $C_4$, while the other has Sylow $2$-subgroup $C_2^2$. Hence all four types are distinct.
:::

Thus the groups of order $28$ are
\[
C_{28},
\qquad
C_{14}\times C_2,
\qquad
C_7\rtimes C_4\ \text{(inversion action)},
\qquad
(C_7\rtimes C_2)\times C_2.
\]
:::
