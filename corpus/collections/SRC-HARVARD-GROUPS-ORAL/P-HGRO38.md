---
schema: qual/card@1
id: P-HGRO38
kind: problem
title: Sylow 3-subgroups from S3 through S9
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
Use pictures to describe the Sylow $3$-subgroups of $S_3,S_4,\ldots,S_9$.
:::

::: solution
It is useful to picture the letters in blocks of three.

<1>1. For $S_3,S_4,S_5$, a Sylow $3$-subgroup is cyclic of order $3$.
::: proof
The $3$-part of $n!$ is $3$ for $n=3,4,5$. Thus
\[
\langle(123)\rangle
\]
is Sylow in each case, fixing any remaining letters.
:::

<1>2. For $S_6,S_7,S_8$, a Sylow $3$-subgroup is
\[
\langle(123),(456)\rangle\cong C_3\times C_3.
\]
::: proof
For $n=6,7,8$,
\[
v_3(n!)=2,
\]
so a Sylow $3$-subgroup has order $9$. The two displayed $3$-cycles are
disjoint and commute, hence generate $C_3\times C_3$ of order $9$. Any letters
beyond $6$ are fixed.
:::

<1>3. For $S_9$, a Sylow $3$-subgroup is the wreath product
\[
C_3\wr C_3=(C_3)^3\rtimes C_3
\]
of order $81$.
::: proof
Partition the letters into three blocks
\[
\{1,2,3\},\qquad \{4,5,6\},\qquad \{7,8,9\}.
\]
Let
\[
a=(123),\qquad b=(456),\qquad c=(789),
\]
which independently rotate the three blocks, and let
\[
d=(147)(258)(369),
\]
which cyclically permutes the blocks. Then
\[
\langle a,b,c\rangle\cong(C_3)^3,
\]
$d$ has order $3$, and conjugation by $d$ cyclically permutes $a,b,c$.
Hence
\[
P=\langle a,b,c,d\rangle\cong(C_3)^3\rtimes C_3
\]
has order $27\cdot3=81$.

Legendre's formula gives
\[
v_3(9!)=\left\lfloor\frac93\right\rfloor
+\left\lfloor\frac99\right\rfloor=3+1=4,
\]
so $81=3^4$ is the full $3$-part of $9!$. Thus $P$ is Sylow.
:::

<1>4. Every Sylow $3$-subgroup in each $S_n$ is conjugate to the displayed
one.
::: proof
This is Sylow conjugacy.
:::
:::
