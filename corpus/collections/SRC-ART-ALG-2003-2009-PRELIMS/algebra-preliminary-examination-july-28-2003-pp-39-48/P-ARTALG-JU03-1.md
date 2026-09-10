---
schema: qual/card@1
id: P-ARTALG-JU03-1
kind: problem
title: 'Sylow subgroups and self-centralizing normalizers at order $84$'
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the order, the 28 Sylow 3-subgroups, and both requested conclusions with July 2003 problem 1 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked all divisors in the Sylow 7-count and proved the normalizer index and both centralizer containments."
---

::: problem
Let $G$ be a group of order 84 with 28 Sylow 3-subgroups.

(a) Find the number of Sylow 7-subgroups of $G$.

(b) Let $Q$ be a Sylow 3-subgroup of $G$.
Let $N_G(Q)$ be the normalizer of $Q$ in $G$, and $Z_G(Q)$ be the centralizer of $Q$ in $G$.
Show that $N_G(Q) = Z_G(Q) = Q$.
:::

::: solution
<1>1. There is exactly one Sylow $7$-subgroup.

::: proof
Since $84=2^2\cdot3\cdot7$, Sylow's theorems give
$$
n_7\mid12,\qquad n_7\equiv1\pmod7
$$
for the number $n_7$ of Sylow $7$-subgroups [@DF04]. The positive
divisors of $12$ are $1,2,3,4,6,12$, and only $1$ is congruent
to $1$ modulo $7$. Thus $n_7=1$.
:::

<1>2. The normalizer of $Q$ has order $3$, and equals $Q$.

::: proof
Conjugation acts transitively on the Sylow $3$-subgroups, by
Sylow conjugacy [@DF04]. The stabilizer of $Q$ is
$$
N_G(Q)=\{g\in G:gQg^{-1}=Q\}.
$$
More explicitly, the map $gN_G(Q)\mapsto gQg^{-1}$ is a
bijection from its left cosets to the Sylow $3$-subgroups:
two conjugates coincide exactly when the representatives differ
by an element of $N_G(Q)$. Hence
$$
[G:N_G(Q)]=28,\qquad |N_G(Q)|=84/28=3.
$$
Every subgroup normalizes itself, so $Q\subseteq N_G(Q)$.
As a Sylow $3$-subgroup, $Q$ also has order $3$. The containment
is therefore equality.
:::

<1>3. The centralizer is also $Q$.

::: proof
Here $Z_G(Q)$ denotes the set of elements commuting with every
element of $Q$, not merely with one chosen element. The group
$Q$ has prime order $3$ and is cyclic, hence abelian. Thus
$Q\subseteq Z_G(Q)$. Every element centralizing $Q$ fixes each
of its elements under conjugation and therefore normalizes $Q$.
Combining this with step <1>2 gives
$$
Q\subseteq Z_G(Q)\subseteq N_G(Q)=Q.
$$
All three subgroups coincide, as required.
:::
:::
