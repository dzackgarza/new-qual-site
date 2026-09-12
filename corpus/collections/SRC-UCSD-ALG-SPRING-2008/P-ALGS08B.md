---
schema: qual/card@1
id: P-ALGS08B
kind: problem
title: "Classification of all groups with 99 elements"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 2 of the official UCSD Spring 2008 algebra qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Re-derived both Sylow counts and made the internal-direct-product step explicit by proving the normal coprime Sylow subgroups commute elementwise.
---

::: problem
Classify all groups of order $99 = 3^2 \cdot 11$ up to isomorphism.
:::

::: {.solution}
<1>1. The Sylow $11$-subgroup of $G$ is unique and normal.
::: {.proof}
Let $n_{11}$ be the number of Sylow $11$-subgroups.
Sylow's theorem gives
\[
n_{11}\mid 9,
\qquad
n_{11}\equiv 1\pmod{11}.
\]
The divisors of $9$ are $1,3,9$, and only $1$ is congruent to $1$ modulo $11$.
Hence
\[
n_{11}=1.
\]
Write $Q$ for this unique Sylow $11$-subgroup.
Then $Q\trianglelefteq G$, and since $|Q|=11$,
\[
Q\cong C_{11}.
\]
:::

<1>2. The Sylow $3$-subgroup of $G$ is unique and normal.
::: {.proof}
Let $n_3$ be the number of Sylow $3$-subgroups.
Again by Sylow's theorem,
\[
n_3\mid 11,
\qquad
n_3\equiv 1\pmod 3.
\]
The only divisors of $11$ are $1$ and $11$, while $11\equiv2\pmod3$.
Thus
\[
n_3=1.
\]
Write $P$ for the unique Sylow $3$-subgroup.
Then $P\trianglelefteq G$ and $|P|=9$.
:::

<1>3. The group $G$ is the internal direct product $P\times Q$.
::: {.proof}
Since $|P|=9$ and $|Q|=11$ are coprime,
\[
P\cap Q=1.
\]
For $p\in P$ and $q\in Q$, normality of $P$ and $Q$ implies
\[
[p,q]=pqp^{-1}q^{-1}\in P\cap Q=1.
\]
Hence $P$ and $Q$ commute elementwise.
Moreover,
\[
|PQ|=\frac{|P||Q|}{|P\cap Q|}=9\cdot11=99=|G|,
\]
so $PQ=G$.
Therefore
\[
G\cong P\times Q.
\]
:::

<1>4. There are exactly two possibilities for $P$.
::: {.proof}
Every group of order $p^2$ is abelian.
Therefore a group of order $9$ is isomorphic to exactly one of
\[
C_9,
\qquad
C_3\times C_3.
\]
Thus
\[
P\cong C_9
\quad\text{or}\quad
P\cong C_3\times C_3.
\]
:::

<1>5. Consequently there are exactly two groups of order $99$ up to isomorphism:
\[
C_{99}
\qquad\text{and}\qquad
C_3\times C_{33}.
\]
::: {.proof}
If $P\cong C_9$, then by <1>3,
\[
G\cong C_9\times C_{11}\cong C_{99},
\]
because $9$ and $11$ are coprime.
If $P\cong C_3\times C_3$, then
\[
G\cong C_3\times C_3\times C_{11}
\cong C_3\times C_{33}.
\]
These two groups are not isomorphic: the first contains an element of order $99$, whereas every element of the second has order dividing $33$.
:::
:::
