---
schema: qual/card@1
id: P-QY54D
kind: problem
title: Center and central quotient of $Q_8$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Groups
  - Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against an independent Hungerford solutions-manual transcription for II.6.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
What is the center of the quaternion group $Q_8$?
Show that $Q_8/Z(Q_8)$ is abelian.
:::

::: solution
Write
\[
Q_8=\{\pm1,\pm i,\pm j,\pm k\},
\]
with $i^2=j^2=k^2=ijk=-1$.

<1>1. The center of $Q_8$ is
\[
Z(Q_8)=\{\pm1\}.
\]
::: proof
The elements $1$ and $-1$ commute with every element of $Q_8$, so
$\{\pm1\}\subseteq Z(Q_8)$.

On the other hand,
\[
ij=k\qquad\text{while}\qquad ji=-k,
\]
so neither $i$ nor $-i$ is central. Cyclically permuting $i,j,k$ shows that none
of $\pm j,\pm k$ is central either. Thus no further elements lie in the center.
:::

<1>2. The quotient $Q_8/Z(Q_8)$ has four elements, each of order dividing $2$.
::: proof
By <1>1, the quotient has order $8/2=4$. Its cosets are
\[
Z(Q_8),\quad iZ(Q_8),\quad jZ(Q_8),\quad kZ(Q_8).
\]
Moreover,
\[
(iZ(Q_8))^2=i^2Z(Q_8)=(-1)Z(Q_8)=Z(Q_8),
\]
and similarly for the $j$- and $k$-cosets.
:::

<1>3. Hence
\[
Q_8/Z(Q_8)\cong \ZZ_2\oplus\ZZ_2,
\]
in particular the quotient is abelian.
::: proof
By <1>2 the quotient has order $4$ and no element of order $4$, so it is the
Klein four group rather than the cyclic group of order $4$. Therefore it is
isomorphic to $\ZZ_2\oplus\ZZ_2$ and is abelian.
:::
:::
