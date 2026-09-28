---
schema: qual/card@1
id: P-ZLNVG
kind: problem
title: No simple group of order $70$, and three nonisomorphic groups of that order
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
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $G$ be a group of order 70.

a. Show that $G$ is not simple.

b. Exhibit 3 nonisomorphic groups of order 70 and prove that they are not isomorphic.
:::

::: {.solution}
For (a), let $n_5$ be the number of Sylow $5$-subgroups. Sylow's theorem gives
\[
n_5\equiv1\pmod5,
\qquad
n_5\mid14.
\]
Among the divisors $1,2,7,14$ of $14$, only $1$ is congruent to $1$ modulo $5$. Hence $n_5=1$, so the Sylow $5$-subgroup is normal. Thus $G$ is not simple.

For (b), consider the following three groups of order $70$:
\[
C_{70},
\qquad
D_{70}=\langle r,s\mid r^{35}=s^2=1,\ srs^{-1}=r^{-1}\rangle,
\qquad
C_5\times D_{14},
\]
where $D_{2n}$ denotes the dihedral group of order $2n$.

The first group is abelian, whereas the latter two are nonabelian, so $C_{70}$ is not isomorphic to either of them. To distinguish the latter two, compare centers. Since $35$ is odd, the center of $D_{70}$ is trivial: a central rotation $r^k$ must satisfy $r^k=r^{-k}$, hence $r^{2k}=1$, forcing $k\equiv0\pmod{35}$; no reflection commutes with $r$. Likewise $Z(D_{14})=1$ because $7$ is odd. Therefore
\[
Z(C_5\times D_{14})=C_5\times Z(D_{14})\cong C_5,
\]
while $Z(D_{70})=1$. Hence the three groups are pairwise nonisomorphic.
:::
