---
schema: qual/card@1
id: P-EQO46
kind: problem
title: Groups of order 12, and two nonisomorphic subgroups of the same order
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Groups
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
(1) What are all the groups of order 12 up to isomorphism?
(2) Can a group of order 12 have two non-isomorphic subgroups of the same order?
:::

::: {.solution}
There are five groups of order $12$ up to isomorphism:
\[
C_{12},\qquad C_6\times C_2,\qquad A_4,\qquad D_{12},\qquad \operatorname{Dic}_3.
\]
Here $D_{12}$ denotes the dihedral group of order $12$, and
\[
\operatorname{Dic}_3
=\langle a,b\mid a^6=1,\ b^2=a^3,\ bab^{-1}=a^{-1}\rangle.
\]

To see why these are the possibilities, let $G$ have order $12=2^2\cdot3$. Sylow gives
\[
n_3\in\{1,4\},\qquad n_2\in\{1,3\}.
\]
If $n_3=4$, the four Sylow $3$-subgroups contribute eight nonidentity elements, leaving exactly four elements; those four form the unique Sylow $2$-subgroup, so it is normal. This case yields $A_4$.

If $n_3=1$, let $Q\cong C_3$ be the normal Sylow $3$-subgroup and let $P$ be a Sylow $2$-subgroup. Then
\[
G\cong C_3\rtimes P,
\]
with $P\cong C_4$ or $V_4$. Since
\[
\operatorname{Aut}(C_3)\cong C_2,
\]
the possible actions are the trivial action and the unique nontrivial action through a quotient of order $2$. For $P=C_4$ these give $C_{12}$ and $\operatorname{Dic}_3$; for $P=V_4$ they give $C_6\times C_2$ and $D_{12}\cong C_2\times S_3$. Thus there are exactly five isomorphism classes.

Yes, a group of order $12$ can have two nonisomorphic subgroups of the same order. In
\[
D_{12}=\langle r,s\mid r^6=s^2=1,\ srs=r^{-1}\rangle,
\]
the subgroup
\[
\langle r\rangle\cong C_6
\]
has order $6$, while
\[
\langle r^2,s\rangle\cong S_3
\]
also has order $6$. One is abelian and the other is not, so they are not isomorphic.
:::
