---
schema: qual/card@1
id: P-AMD-ASWUIIA5
kind: problem
title: Class sums form an $R$-basis of the center of the group ring $RG$
classification:
  areas:
  - algebra
  topics:
  - Group Rings
  - Conjugacy
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 6, Exercise 6. Restored
    the definition of the ring center and the two source parts concerning class
    sums and the full center of RG.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Conjugation by an element of G permutes each conjugacy class, so every class
    sum is central. Conversely, if z=sum_g a_g g is central, invariance under
    hzh^{-1} for every h forces a_g to be constant on conjugacy classes. Hence
    the class sums span Z(RG); disjoint supports in the standard group basis
    also give linear independence.
---

::: {.problem}
Recall that the center of a ring $S$ is
\[
Z(S)=\{z\in S:zs=sz\text{ for every }s\in S\}.
\]
Let $R$ be a commutative ring, let $G$ be a finite group, and consider the group ring $RG$.

(a) Let
\[
\mathcal K=\{k_1,\ldots,k_m\}
\]
be a conjugacy class in $G$.
Prove that the class sum
\[
K=k_1+\cdots+k_m\in RG
\]
belongs to $Z(RG)$.

(b) Let
\[
\mathcal K_1,\ldots,\mathcal K_r
\]
be the distinct conjugacy classes of $G$, and let
\[
K_i=\sum_{g\in\mathcal K_i}g.
\]
Prove that
\[
Z(RG)
 =\left\{a_1K_1+\cdots+a_rK_r:a_i\in R\right\}.
\]
Equivalently, the class sums $K_1,\ldots,K_r$ form an $R$-basis of $Z(RG)$.
:::

::: {.solution}
<1>1. Conjugation by any $h\in G$ fixes a class sum $K$.
::: {.proof}
Let $\mathcal K$ be a conjugacy class and
\[
K=\sum_{k\in\mathcal K}k.
\]
For $h\in G$, conjugation by $h$ permutes the elements of $\mathcal K$.
Therefore
\[
hKh^{-1}
  =\sum_{k\in\mathcal K}hkh^{-1}
  =\sum_{k\in\mathcal K}k
  =K.
\]
Multiplying on the right by $h$ gives
\[
hK=Kh.
\]
:::

<1>2. Every class sum belongs to $Z(RG)$.
::: {.proof}
By <1>1, $K$ commutes with every basis element $h\in G$.
Since $R$ is commutative, its scalar coefficients commute with every element of $RG$.
Thus for arbitrary
\[
z=\sum_{h\in G}a_hh\in RG,
\]
we have
\[
Kz
  =\sum_{h\in G}a_hKh
  =\sum_{h\in G}a_hhK
  =zK.
\]
Hence $K\in Z(RG)$.
This proves part (a).
:::

<1>3. If
\[
z=\sum_{g\in G}a_gg\in Z(RG),
\]
then its coefficients are constant on conjugacy classes.
::: {.proof}
Fix $h\in G$.
Since $z$ is central,
\[
hzh^{-1}=z.
\]
But
\[
hzh^{-1}
  =\sum_{g\in G}a_g(hgh^{-1}).
\]
The elements of $G$ form an $R$-basis of $RG$, so equality of these two group-ring elements implies equality of the corresponding coefficients.
For every $g\in G$,
\[
a_{hgh^{-1}}=a_g.
\]
Thus $a_g$ depends only on the conjugacy class of $g$.
:::

<1>4. Every central element of $RG$ is an $R$-linear combination of the class sums.
::: {.proof}
Let $z\in Z(RG)$.
By <1>3, there is a coefficient $a_i\in R$ such that every element of $\mathcal K_i$ occurs in $z$ with coefficient $a_i$.
Therefore
\[
z
 =\sum_{i=1}^r a_i\sum_{g\in\mathcal K_i}g
 =\sum_{i=1}^r a_iK_i.
\]
:::

<1>5. Every $R$-linear combination of the class sums is central.
::: {.proof}
Each $K_i$ is central by <1>2, and $Z(RG)$ is an $R$-submodule of $RG$.
Hence
\[
\sum_{i=1}^r a_iK_i\in Z(RG)
\]
for all $a_i\in R$.
:::

<1>6. The class sums are $R$-linearly independent.
::: {.proof}
Suppose
\[
\sum_{i=1}^r a_iK_i=0.
\]
The conjugacy classes partition $G$, so the supports of the $K_i$ in the standard basis $G$ are pairwise disjoint.
For any $g\in\mathcal K_i$, the coefficient of $g$ in the displayed sum is exactly $a_i$.
Since the sum is zero and the elements of $G$ are an $R$-basis of $RG$, every $a_i=0$.
:::

<1>7. The class sums $K_1,\ldots,K_r$ form an $R$-basis of $Z(RG)$.
::: {.proof}
They span by <1>4 and <1>5, and they are linearly independent by <1>6. This proves part (b).
:::

<1>8. Q.E.D.
::: {.proof}
Parts (a) and (b) are <1>2 and <1>7.
:::
:::
