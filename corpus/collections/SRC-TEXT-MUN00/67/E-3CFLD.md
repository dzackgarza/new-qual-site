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
---

::: {.exercise}

Give an example of a free abelian group $G$ of rank $n$ having a subgroup $H$ of rank $n$ for which $H \neq G$.
:::

::: solution
**Goal:** Provide an explicit example of a free abelian group $G$ of rank $n \ge 1$ containing a proper subgroup $H \subsetneq G$ of full rank $n$, and prove these properties.

<1>1. Definition of $G$ and $H$:
    Let $G = \mathbb{Z}^n = \bigoplus_{i=1}^n \mathbb{Z} \mathbf{e}_i$, where $\{\mathbf{e}_1, \dots, \mathbf{e}_n\}$ is the standard canonical $\mathbb{Z}$-basis.
    Define the subgroup:
    $$H = 2\mathbb{Z} \times \mathbb{Z} \times \dots \times \mathbb{Z} = \operatorname{span}_{\mathbb{Z}}\{2\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n\}.$$

<1>2. Verification that $G$ is free abelian of rank $n$:
    *Proof:* The set $\{\mathbf{e}_1, \dots, \mathbf{e}_n\}$ freely generates $G$ over $\mathbb{Z}$, so $\operatorname{rank}(G) = n$.

<1>3. Verification that $H$ is free abelian of rank $n$:
    *Proof:*
    <2>1. The generating set $\mathcal{B} = \{2\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n\}$ generates $H$ by definition.
    <2>2. If $c_1 (2\mathbf{e}_1) + \sum_{i=2}^n c_i \mathbf{e}_i = \mathbf{0}$ for $c_i \in \mathbb{Z}$, then $(2c_1, c_2, \dots, c_n) = (0, 0, \dots, 0)$, which implies $2c_1 = 0 \implies c_1 = 0$ and $c_2 = \dots = c_n = 0$.
    <2>3. Thus $\mathcal{B}$ is $\mathbb{Z}$-linearly independent, making $H$ a free abelian group with basis of size $n$, so $\operatorname{rank}(H) = n$.

<1>4. Verification that $H$ is a proper subgroup ($H \neq G$):
    *Proof:*
    <2>1. The element $\mathbf{e}_1 = (1, 0, \dots, 0) \in G$.
    <2>2. Every element $(x_1, \dots, x_n) \in H$ has $x_1 \in 2\mathbb{Z}$.
    <2>3. Since $1 \notin 2\mathbb{Z}$, $\mathbf{e}_1 \notin H$, proving $H \subsetneq G$.
    <2>4. In particular, the quotient group is $G/H \cong \mathbb{Z}/2\mathbb{Z}$ of order 2.

<1>5. Conclusion:
    $G = \mathbb{Z}^n$ and $H = 2\mathbb{Z} \times \mathbb{Z}^{n-1}$ provide the required example of a proper full-rank subgroup. Q.E.D.
:::
