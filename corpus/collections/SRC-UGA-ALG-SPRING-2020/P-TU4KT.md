---
schema: qual/card@1
id: P-TU4KT
kind: problem
title: 'Groups of order $2020$: solvability, classification of abelian groups, and
  a nonabelian example'
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Classification
  - Structure Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
a. Show that any group of order 2020 is solvable.

a. Give (without proof) a classification of all abelian groups of order 2020.

c. Describe one nonabelian group of order 2020.
:::

::: {.solution}
Since
\[
2020=2^2\cdot5\cdot101,
\]
Sylow's theorem gives
\[
n_{101}\mid 20,\qquad n_{101}\equiv1\pmod{101}.
\]
Hence $n_{101}=1$, so the Sylow $101$-subgroup $N$ is normal. The quotient $G/N$ has order $20$. In a group of order $20$, the number of Sylow $5$-subgroups divides $4$ and is congruent to $1$ modulo $5$, hence equals $1$. Thus $G/N$ has a normal subgroup of order $5$ with quotient of order $4$. Both that subgroup and the quotient are abelian, so $G/N$ is solvable. Since $N\cong C_{101}$ is abelian, $G$ is an extension of solvable groups and is therefore solvable.

For the abelian classification, the $2$-primary part has order $4$, so it is either $C_4$ or $C_2\times C_2$. The $5$- and $101$-primary parts are cyclic. Hence, up to isomorphism, the abelian groups are
\[
C_4\times C_5\times C_{101}\cong C_{2020}
\]
and
\[
C_2\times C_2\times C_5\times C_{101}\cong C_2\times C_{1010}.
\]

A nonabelian example is
\[
D_{202}\times C_{10},
\]
where $D_{202}$ denotes the dihedral group of order $202$; this has order $2020$ and is nonabelian.
:::
