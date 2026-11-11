---
schema: qual/card@1
id: E-3CFLD
kind: problem
title: A full-rank proper subgroup of a free abelian group
classification:
  areas:
  - topology
  topics:
  - Free Abelian Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §67 Exercise 5, printed p. 412. Example and proof transcribed from dbFin, Munkres (2000) Topology
    with Solutions, §67 Problem 5 (web page, read 2026-11-11), with the rank count and the properness
    separated as there. Checked against the definition of a free abelian group and of rank on Munkres p. 410
    and Theorem 67.8 on p. 411. One addition: for n = 0 there is no such example, since the only free abelian
    group of rank 0 is the trivial group, and the card states the example for n >= 1.
---

::: {.exercise}

Give an example of a free abelian group $G$ of rank $n$ having a subgroup $H$ of rank $n$ for which $H \neq G$.
:::

::: {.solution}

For $n\ge1$ take $G=\ZZ^n=\bigoplus_{i=1}^n\ZZ\mathbf{e}_i$ with $\mathbf{e}_1,\dots,\mathbf{e}_n$ the standard basis, and

$$
H=2\ZZ\times\ZZ\times\cdots\times\ZZ=\operatorname{span}_{\ZZ}\theset{2\mathbf{e}_1,\mathbf{e}_2,\dots,\mathbf{e}_n}.
$$

For $n=0$ no such example exists: the only free abelian group of rank $0$ is the trivial group, which has no proper subgroup.

::: pf

::: pf-step

$G$ is free abelian of rank $n$.

::: pf-proof

By Theorem 67.8 (printed p. 411) the rank of a free abelian group with a finite basis is the number of elements in a basis, and $\theset{\mathbf{e}_1,\dots,\mathbf{e}_n}$ is a basis of $G$ by the definition on p. 410.

:::

:::

::: pf-step

$H$ is free abelian of rank $n$.

::: pf-proof

$\theset{2\mathbf{e}_1,\mathbf{e}_2,\dots,\mathbf{e}_n}$ generates $H$, and if $c_1(2\mathbf{e}_1)+\sum_{i\ge2}c_i\mathbf{e}_i=\mathbf{0}$ then $(2c_1,c_2,\dots,c_n)=(0,\dots,0)$, so $c_1=\cdots=c_n=0$. A $k$-element basis has rank $k$ by Theorem 67.8, so $\operatorname{rank}H=n$.

:::

:::

::: pf-step

$H\neq G$.

::: pf-proof

Every element $(x_1,\dots,x_n)\in H$ has $x_1\in 2\ZZ$, while $\mathbf{e}_1=(1,0,\dots,0)\in G$ has first coordinate $1\notin2\ZZ$. Hence $\mathbf{e}_1\notin H$ and $H\subsetneq G$; the quotient is $G/H\cong\ZZ/2\ZZ$.

:::

:::

::: pf-qed

$G=\ZZ^n$ and $H=2\ZZ\times\ZZ^{n-1}$ give a subgroup of the same finite rank that is not all of $G$.

:::

:::
:::
