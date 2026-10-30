---
schema: qual/card@1
id: P-AZBYD
kind: problem
title: Homology and cohomology of $L\times\Sigma L$ when $H_*(L)=(\ZZ,\ZZ_3,0,\ZZ)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cohomology
  - Product Topology
relations: []
review: draft
---

::: {.problem}
Let $L$ be a $3$-manifold whose homology groups are $\ZZ, \ZZ_3, 0, \ZZ$ in dimensions $0, 1, 2, 3$.
Compute the homology $H_*(X;\ZZ)$ and cohomology $H^*(X;\ZZ)$ of the space $X = L \times \Sigma L$.
(Here $\Sigma$ denotes the suspension of a space.)
:::

::: {.solution}

::: pf

::: {.pf-step #suspension}

$H_*(\Sigma L;\ZZ)$ is $\ZZ, 0, \ZZ_3, 0, \ZZ$ in dimensions $0,1,2,3,4$ and zero above.

::: pf-proof

$\widetilde H_i(\Sigma L)\cong\widetilde H_{i-1}(L)$, and $\Sigma L$ is path connected.

:::

:::

::: {.pf-step #kunneth}

The Künneth formula
$$
H_k(L\times\Sigma L)\cong\bigoplus_{i+j=k}H_i(L)\otimes H_j(\Sigma L)\ \oplus\bigoplus_{i+j=k-1}\operatorname{Tor}(H_i(L),H_j(\Sigma L))
$$
has the following nonzero terms.

| $(i,j)$ | term | degree |
|---|---|---|
| $(0,0)$ | $\ZZ\otimes\ZZ=\ZZ$ | $0$ |
| $(1,0)$ | $\ZZ_3\otimes\ZZ=\ZZ_3$ | $1$ |
| $(0,2)$ | $\ZZ\otimes\ZZ_3=\ZZ_3$ | $2$ |
| $(1,2)$ | $\ZZ_3\otimes\ZZ_3=\ZZ_3$ | $3$ |
| $(3,0)$ | $\ZZ\otimes\ZZ=\ZZ$ | $3$ |
| $(0,4)$ | $\ZZ\otimes\ZZ=\ZZ$ | $4$ |
| $(1,2)$ | $\operatorname{Tor}(\ZZ_3,\ZZ_3)=\ZZ_3$ | $4$ |
| $(1,4)$ | $\ZZ_3\otimes\ZZ=\ZZ_3$ | $5$ |
| $(3,2)$ | $\ZZ\otimes\ZZ_3=\ZZ_3$ | $5$ |
| $(3,4)$ | $\ZZ\otimes\ZZ=\ZZ$ | $7$ |

::: pf-proof

Use $H_*(L)$ from the statement and $H_*(\Sigma L)$ from Step [](#suspension){.pf-ref}. A $\operatorname{Tor}$ term is nonzero only when both factors have torsion, which happens only for $(i,j)=(1,2)$.

:::

:::

::: {.pf-step #homology}

$$
H_*(X;\ZZ)\cong \ZZ,\ \ZZ_3,\ \ZZ_3,\ \ZZ\oplus\ZZ_3,\ \ZZ\oplus\ZZ_3,\ \ZZ_3^2,\ 0,\ \ZZ
$$
in dimensions $0,1,\ldots,7$, and $H_k(X)=0$ for $k\ge8$.

::: pf-proof

Sum the rows of Step [](#kunneth){.pf-ref} by degree.

:::

:::

::: pf-qed

By the universal coefficient theorem, $H^k(X;\ZZ)\cong\operatorname{Hom}(H_k(X),\ZZ)\oplus\operatorname{Ext}(H_{k-1}(X),\ZZ)$, which is the free part of $H_k$ plus the torsion of $H_{k-1}$. Step [](#homology){.pf-ref} gives
$$
H^*(X;\ZZ)\cong \ZZ,\ 0,\ \ZZ_3,\ \ZZ\oplus\ZZ_3,\ \ZZ\oplus\ZZ_3,\ \ZZ_3,\ \ZZ_3^2,\ \ZZ
$$
in dimensions $0,1,\ldots,7$, and $H^k(X)=0$ for $k\ge8$.

:::

:::

:::
