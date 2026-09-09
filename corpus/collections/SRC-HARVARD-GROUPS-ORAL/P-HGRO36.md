---
schema: qual/card@1
id: P-HGRO36
kind: problem
title: Sylow 3-subgroups of symmetric groups
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
Describe the Sylow $3$-subgroups of symmetric groups.
:::

::: solution
Write the base-$3$ expansion of $n$ as
\[
n=a_0+a_1 3+a_2 3^2+\cdots+a_r3^r,
\qquad 0\le a_i<3.
\]
For $i\ge1$, let $W_i$ be the iterated wreath product
\[
W_i=C_3\wr C_3\wr\cdots\wr C_3
\]
with $i$ copies of $C_3$, in its natural action on $3^i$ points. Then a Sylow
$3$-subgroup of $S_n$ is
\[
P\cong\prod_{i=1}^r W_i^{\,a_i},
\]
acting independently on $a_i$ disjoint blocks of size $3^i$.

<1>1. The group $W_i$ is a $3$-subgroup of $S_{3^i}$ of order
\[
|W_i|=3^{(3^i-1)/2}.
\]
::: proof
Set $W_1=C_3$. Recursively,
\[
W_i=W_{i-1}^3\rtimes C_3,
\]
where the final $C_3$ cyclically permutes three blocks of size $3^{i-1}$.
If $|W_{i-1}|=3^{e_{i-1}}$, then
\[
e_i=3e_{i-1}+1,
\qquad e_1=1.
\]
Solving this recursion gives
\[
e_i=1+3+\cdots+3^{i-1}=\frac{3^i-1}{2}.
\]
:::

<1>2. The displayed product $P$ has order
\[
3^{\sum_i a_i(3^i-1)/2}.
\]
::: proof
The factors act on disjoint blocks, so their product is direct and their orders
multiply. Apply <1>1 to each of the $a_i$ copies of $W_i$.
:::

<1>3. This exponent equals $v_3(n!)$.
::: proof
Legendre's formula in digit-sum form gives
\[
v_3(n!)=\frac{n-s_3(n)}{3-1},
\]
where
\[
s_3(n)=a_0+a_1+\cdots+a_r.
\]
Therefore
\[
v_3(n!)
=\frac12\sum_i a_i(3^i-1).
\]
This is exactly the exponent in <1>2.
:::

<1>4. Hence $P$ is a Sylow $3$-subgroup of $S_n$.
::: proof
By <1>2--<1>3, $P$ has order equal to the full $3$-part of $|S_n|=n!$.
Thus it is Sylow. Every Sylow $3$-subgroup is conjugate to such a block-wreath
product.
:::
:::
