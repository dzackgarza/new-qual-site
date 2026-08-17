---
schema: qual/card@1
id: P-ZLOZU
kind: problem
title: If $MN$ has three zero entries then $MN=0$
classification:
  areas:
  - algebra
  topics:
  - matrices
  - rings
  - determinants
relations: []
review: draft
solved: true
---

::: problem
Let
$$
M=\left(\begin{array}{ll}{a} & {b} \\ {c} & {d}\end{array}\right)
\quad \text{and} \quad 
N=\left(\begin{array}{cc}{x} & {u} \\ {-y} & {-v}\end{array}\right)
$$

over a commutative ring $R$, where $b$ and $x$ are units of $R$.
Prove that
$$
M N=\left(\begin{array}{ll}{0} & {0} \\ {0} & {*}\end{array}\right)
\implies MN = 0
.$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Compute the product matrix $MN$:
$$
MN = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x & u \\ -y & -v \end{pmatrix}
= \begin{pmatrix} ax - by & au - bv \\ cx - dy & cu - dv \end{pmatrix}.
$$

We are given that the $(1,1)$, $(1,2)$, and $(2,1)$ entries are zero:
1. $ax - by = 0 \implies by = ax \implies y = b^{-1}ax$ (since $b \in R^\times$).
2. $au - bv = 0 \implies bv = au \implies v = b^{-1}au$ (since $b \in R^\times$).
3. $cx - dy = 0$.

Substitute $y = b^{-1}ax$ into equation (3):
$$
cx - d(b^{-1}ax) = 0 \implies (c - db^{-1}a)x = 0.
$$
Since $x \in R^\times$ is a unit in $R$, multiplying by $x^{-1}$ gives:
$$
c - db^{-1}a = 0 \implies c = db^{-1}a.
$$

Now compute the bottom-right $(2,2)$ entry of $MN$, which is $* = cu - dv$:
Substitute $c = db^{-1}a$ and $v = b^{-1}au$:
$$
cu - dv = (db^{-1}a)u - d(b^{-1}au).
$$
Since $R$ is commutative:
$$
(db^{-1}a)u = d b^{-1} a u = d (b^{-1} a u).
$$
Thus:
$$
cu - dv = d b^{-1} a u - d b^{-1} a u = 0.
$$

Since all four entries of $MN$ are zero, we conclude that $MN = 0$.
:::
