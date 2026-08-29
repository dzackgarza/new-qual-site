---
schema: qual/card@1
id: P-4HGM3
kind: problem
title: Groups of order 8
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Classify all groups of order 8.
:::

::: {.solution}
**Goal.** Classify all groups of order $8$ up to isomorphism.

<1>1. There are five groups of order $8$: three abelian and two nonabelian.
Proof: this is the standard classification.

<1>2. The abelian groups of order $8$.
<2>1. By the fundamental theorem of finite abelian groups, the abelian groups of order $8 = 2^3$ are $\ZZ/8$, $\ZZ/4 \times \ZZ/2$, and $\ZZ/2 \times \ZZ/2 \times \ZZ/2$.
Proof: the partitions of $3$ are $3$, $2+1$, $1+1+1$.

<1>3. The nonabelian groups of order $8$.
<2>1. $D_4$ (the dihedral group of order $8$, symmetries of the square).
Proof: $D_4 = \langle r, s \mid r^4 = s^2 = 1, srs = r^{-1}\rangle$.
<2>2. $Q_8$ (the quaternion group).
Proof: $Q_8 = \theset{\pm 1, \pm i, \pm j, \pm k}$ with $i^2 = j^2 = k^2 = ijk = -1$.

<1>4. These five are all the groups of order $8$.
<2>1. A group of order $8$ is a $2$-group, hence has a nontrivial center.
Proof: a nontrivial $p$-group has a nontrivial center.
<2>2. If $G$ is abelian, it is one of the three in <1>2. Proof: fundamental theorem of finite abelian groups.
<2>3. If $G$ is nonabelian, it is $D_4$ or $Q_8$.
Proof: a nonabelian group of order $8$ has an element of order $4$ (else all elements have order $\le 2$, forcing abelian); the two nonabelian groups of order $8$ are $D_4$ and $Q_8$ (standard classification of groups of order $8$).

<1>5. Q.E.D. Proof: the groups of order $8$ are $\ZZ/8$, $\ZZ/4 \times \ZZ/2$, $(\ZZ/2)^3$, $D_4$, $Q_8$.
:::
