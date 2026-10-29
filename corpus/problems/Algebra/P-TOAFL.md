---
schema: qual/card@1
id: P-TOAFL
kind: problem
title: Classification of groups of order $10$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
---

::: {.problem}
Classify all groups of order $10$.
:::

::: {.solution}
Let $G$ be a group with $\abs{G}=10=2\cdot5$.

::: pf

::: {.pf-step #sylow5}
The Sylow $5$-subgroup $P\cong C_5$ of $G$ is normal.

::: pf-proof
By Sylow's theorems $n_5\divides 2$ and $n_5\equiv1\pmod5$, so $n_5=1$.
:::

:::

::: {.pf-step #semidirect}
$G\cong C_5\rtimes_\varphi C_2$ for a homomorphism $\varphi:C_2\to\Aut(C_5)\cong C_4$.

::: pf-proof
Let $Q\cong C_2$ be a Sylow $2$-subgroup. Then $P\cap Q=1$ and $\abs{PQ}=10$, so $G=PQ$ with $P$ normal by step [](#sylow5){.pf-ref}.
:::

:::

::: pf-step
Up to isomorphism, the groups of order $10$ are $\boxed{C_{10}\text{ and }D_{10}}$, where $D_{10}$ is the dihedral group of order $10$.

::: pf-proof
$C_4$ has a unique element of order $2$, which acts on $C_5$ by inversion, so by step [](#semidirect){.pf-ref} $\varphi$ is trivial or sends the generator to inversion.
The trivial action gives $C_5\times C_2\cong C_{10}$, and inversion gives $D_{10}$.
These are not isomorphic, since $C_{10}$ is abelian and $D_{10}$ is not.
:::

:::

:::

:::
