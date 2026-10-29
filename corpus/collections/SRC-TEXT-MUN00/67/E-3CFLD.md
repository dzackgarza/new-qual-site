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

::: {.solution}

::: pf

::: pf-step

Definition of $G$ and $H$:
    Let $G = \ZZ^n = \bigoplus_{i=1}^n \ZZ \mathbf{e}_i$, where $\{\mathbf{e}_1, \dots, \mathbf{e}_n\}$ is the standard canonical $\ZZ$-basis.
    Define the subgroup:
    $$H = 2\ZZ \times \ZZ \times \dots \times \ZZ = \operatorname{span}_{\ZZ}\{2\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n\}.$$

:::

::: pf-step

Verification that $G$ is free abelian of rank $n$:
    *Proof:* The set $\{\mathbf{e}_1, \dots, \mathbf{e}_n\}$ freely generates $G$ over $\ZZ$, so $\operatorname{rank}(G) = n$.

:::

::: pf-step

Verification that $H$ is free abelian of rank $n$:
    *Proof:*

::: pf-proof

::: pf-step

The generating set $\mathcal{B} = \{2\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n\}$ generates $H$ by definition.

:::

::: pf-step

If $c_1 (2\mathbf{e}_1) + \sum_{i=2}^n c_i \mathbf{e}_i = \mathbf{0}$ for $c_i \in \ZZ$, then $(2c_1, c_2, \dots, c_n) = (0, 0, \dots, 0)$, which implies $2c_1 = 0 \implies c_1 = 0$ and $c_2 = \dots = c_n = 0$.

:::

::: pf-step

Thus $\mathcal{B}$ is $\ZZ$-linearly independent, making $H$ a free abelian group with basis of size $n$, so $\operatorname{rank}(H) = n$.

:::

:::

:::

::: pf-step

Verification that $H$ is a proper subgroup ($H \neq G$):
    *Proof:*

::: pf-proof

::: pf-step

The element $\mathbf{e}_1 = (1, 0, \dots, 0) \in G$.

:::

::: pf-step

Every element $(x_1, \dots, x_n) \in H$ has $x_1 \in 2\ZZ$.

:::

::: pf-step

Since $1 \notin 2\ZZ$, $\mathbf{e}_1 \notin H$, proving $H \subsetneq G$.

:::

::: pf-step

In particular, the quotient group is $G/H \cong \ZZ/2\ZZ$ of order 2.

:::

:::

:::

::: pf-step

Conclusion:

:::

:::

    $G = \ZZ^n$ and $H = 2\ZZ \times \ZZ^{n-1}$ provide the required example of a proper full-rank subgroup. Q.E.D.
:::
