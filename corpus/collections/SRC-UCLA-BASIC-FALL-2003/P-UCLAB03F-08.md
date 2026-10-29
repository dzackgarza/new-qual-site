---
schema: qual/card@1
id: P-UCLAB03F-08
kind: problem
title: Rank-nullity, adjoints, and equality of row and column rank
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 of the official UCLA Basic Exam Fall 2003 PDF.
---

::: {.problem}
Prove the following three statements.
You may choose their order and use earlier statements to prove later ones.

(a) If $T:V\to W$ is linear between finite-dimensional real vector spaces, then
\[
\dim(\operatorname{im}T)=\dim V-\dim(\ker T).
\]

(b) If $T:V\to V$ is linear on a finite-dimensional real inner-product space and $T^*$ is its adjoint, then
\[
\operatorname{im}(T^*)=(\ker T)^\perp.
\]

(c) If $A$ is a real $n\times n$ matrix, then its row rank equals its column rank.
:::

::: {.solution}

::: pf

::: pf-step

Let
\[
k=\dim\ker T.
\]
Choose a basis
\[
v_1,\ldots,v_k
\]
of $\ker T$ and extend it to a basis
\[
v_1,\ldots,v_k,v_{k+1},\ldots,v_n
\]
of $V$.


::: pf-proof

Every basis of a subspace of a finite-dimensional vector space extends to a basis of the whole space.

:::

:::

::: {.pf-step #s1-2}

The vectors
\[
Tv_{k+1},\ldots,Tv_n
\]
form a basis of $\operatorname{im}T$.


::: pf-proof

Every $v\in V$ can be written
\[
v=\sum_{i=1}^n a_iv_i.
\]
Since $Tv_i=0$ for $i\le k$,
\[
Tv=\sum_{i=k+1}^n a_iTv_i,
\]
so the displayed vectors span $\operatorname{im}T$.

Suppose
\[
\sum_{i=k+1}^n a_iTv_i=0.
\]
Then
\[
T\left(\sum_{i=k+1}^n a_iv_i\right)=0,
\]
so the vector in parentheses lies in $\ker T$, hence in
\[
\operatorname{span}\{v_1,\ldots,v_k\}.
\]
But it also lies in
\[
\operatorname{span}\{v_{k+1},\ldots,v_n\}.
\]
These two spans intersect only in $0$ because the full list is a basis. Thus all $a_i=0$, proving linear independence.

:::

:::

::: {.pf-step #s1-3}

Therefore
\[
\boxed{\dim(\operatorname{im}T)=\dim V-\dim(\ker T)}.
\]


::: pf-proof

By step [](#s1-2){.pf-ref},
\[
\dim(\operatorname{im}T)=n-k.
\]
Since $n=\dim V$ and $k=\dim\ker T$, the formula follows.

:::

:::

::: {.pf-step #s1-4}

For a linear map $T:V\to V$ on a finite-dimensional real inner-product space,
\[
(\operatorname{im}T^*)^\perp=\ker T.
\]


::: pf-proof

Let $w\in V$. Then
\[
w\in(\operatorname{im}T^*)^\perp
\]
if and only if
\[
\langle T^*v,w\rangle=0
\]
for every $v\in V$. By the defining property of the adjoint, this is equivalent to
\[
\langle v,Tw\rangle=0
\]
for every $v\in V$. The only vector orthogonal to every vector in $V$ is $0$, so this holds exactly when
\[
Tw=0.
\]
Thus the two subspaces are equal.

:::

:::

::: {.pf-step #s1-5}

One has
\[
\boxed{\operatorname{im}(T^*)=(\ker T)^\perp}.
\]


::: pf-proof

Take orthogonal complements in step [](#s1-4){.pf-ref}. In a finite-dimensional inner-product space,
\[
(Y^\perp)^\perp=Y
\]
for every subspace $Y$. Hence
\[
\operatorname{im}(T^*)
=
\bigl((\operatorname{im}T^*)^\perp\bigr)^\perp
=
(\ker T)^\perp.
\]

:::

:::

::: {.pf-step #s1-6}

For every real $n\times n$ matrix $A$,
\[
\operatorname{rank}(A^t)=\operatorname{rank}(A).
\]


::: pf-proof

View $A$ as the matrix of a linear map
\[
T:\RR^n\to\RR^n
\]
with the standard inner product. Then $T^*$ has matrix $A^t$. By step [](#s1-5){.pf-ref},
\[
\dim\operatorname{im}T^*
=
\dim(\ker T)^\perp
=
n-\dim\ker T.
\]
By step [](#s1-3){.pf-ref},
\[
n-\dim\ker T
=
\dim\operatorname{im}T.
\]
Therefore
\[
\operatorname{rank}(A^t)
=
\dim\operatorname{im}T^*
=
\dim\operatorname{im}T
=
\operatorname{rank}(A).
\]

:::

:::

::: {.pf-step #s1-7}

The row rank of $A$ equals its column rank.


::: pf-proof

The column rank of $A$ is
\[
\operatorname{rank}(A),
\]
because the columns span the image of the associated linear map. The rows of $A$ are the columns of $A^t$, so the row rank of $A$ is
\[
\operatorname{rank}(A^t).
\]
Step [](#s1-6){.pf-ref} shows these two ranks are equal.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), step [](#s1-5){.pf-ref} proves part (b), and step [](#s1-7){.pf-ref} proves part (c).

:::

:::

:::
