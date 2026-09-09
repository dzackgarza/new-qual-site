---
schema: qual/card@1
id: P-HGRO39
kind: problem
title: Sylow 2-subgroups of S4, S5, and S6
classification:
  areas: [algebra]
  topics: [Sylow Theory, Permutation Groups]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Describe the Sylow $2$-subgroups of $S_4$, $S_5$, and $S_6$.
:::

::: solution
The $2$-parts of the three group orders are
\[
|S_4|=24=2^3\cdot3,
\qquad
|S_5|=120=2^3\cdot15,
\qquad
|S_6|=720=2^4\cdot45.
\]

<1>1. A Sylow $2$-subgroup of $S_4$ is dihedral of order $8$.
::: proof
Set
\[
r=(1234),
\qquad
s=(13).
\]
Then $r$ has order $4$, $s$ has order $2$, and
\[
srs=r^{-1}.
\]
Thus
\[
\langle r,s\rangle\cong D_8
\]
has order $8$, which is the full $2$-part of $|S_4|$.
:::

<1>2. A Sylow $2$-subgroup of $S_5$ is again isomorphic to $D_8$.
::: proof
Embed the subgroup from <1>1 in $S_5$ by letting it fix the point $5$. It still
has order $8$, which is the full $2$-part of $|S_5|$, so it is Sylow.
All Sylow $2$-subgroups are conjugate.
:::

<1>3. A Sylow $2$-subgroup of $S_6$ is isomorphic to $D_8\times C_2$.
::: proof
Let the $D_8$ from <1>1 act on $\{1,2,3,4\}$, and adjoin the disjoint
transposition $(56)$. Since $(56)$ commutes with the first factor,
\[
\langle (1234),(13),(56)\rangle
\cong D_8\times C_2
\]
has order $16$, the full $2$-part of $|S_6|$. Hence it is Sylow, and every
Sylow $2$-subgroup of $S_6$ is conjugate to it.
:::
:::
