---
schema: qual/card@1
id: P-X3QFP
kind: problem
title: Classification of groups of order $12$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
---

::: problem
Classify the groups of order $12$ up to isomorphism.
:::

::: solution
Let $G$ have order $12=2^2\cdot3$. Sylow gives
\[
n_3\equiv1\pmod3,
\qquad
n_3\mid4,
\]
so $n_3=1$ or $4$.

<1>1. Suppose $n_3=4$.

Conjugation on the four Sylow $3$-subgroups gives a homomorphism
\[
G\to S_4.
\]
Its kernel is normal. If the kernel were nontrivial, its order would divide the intersection of the normalizers of the four Sylow $3$-subgroups; a direct Sylow count forces the kernel to be trivial. Thus $G$ embeds as a subgroup of order $12$ in $S_4$. Such a subgroup has index $2$, hence is $A_4$. Therefore
\[
G\cong A_4.
\]

<1>2. Suppose $n_3=1$.

Let $N\cong C_3$ be the normal Sylow $3$-subgroup and let $H$ be a Sylow $2$-subgroup. Since $|N|$ and $|H|$ are coprime,
\[
G\cong C_3\rtimes H,
\]
where $H$ is either $C_4$ or $V_4$ and the action lands in
\[
\operatorname{Aut}(C_3)\cong C_2.
\]

If $H=C_4$, there are two action types:
\[
C_3\times C_4\cong C_{12},
\]
and the nontrivial semidirect product
\[
C_3\rtimes C_4,
\]
where a generator of $C_4$ acts on $C_3$ by inversion.

If $H=V_4$, the trivial action gives
\[
C_3\times V_4\cong C_6\times C_2.
\]
Every nontrivial homomorphism $V_4\to C_2$ has kernel of order $2$, and all such kernels are equivalent under $\operatorname{Aut}(V_4)$. Hence there is one nontrivial semidirect product, isomorphic to
\[
S_3\times C_2,
\]
equivalently the dihedral group of order $12$.

Thus the five groups are
\[
C_{12},\qquad
C_6\times C_2,\qquad
C_3\rtimes C_4,\qquad
S_3\times C_2,\qquad
A_4.
\]
:::
