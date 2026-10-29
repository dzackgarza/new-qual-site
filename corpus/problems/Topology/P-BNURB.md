---
schema: qual/card@1
id: P-BNURB
kind: problem
title: Homology of the Klein bottle via Mayer–Vietoris
classification:
  areas:
  - topology
  topics:
  - Mayer-Vietoris
  - Homology
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Compute the homology of the Klein bottle using the Mayer-Vietoris sequence and a decomposition $K = M \disjoint_f M$
:::

::: {.solution}

The Klein bottle $K$ is the union of two Möbius bands $M_1$ and $M_2$ glued along their boundary circles. Let $U,V\subset K$ be open collars of $M_1$ and $M_2$, so that $U\cap V$ is an open annulus around the common boundary circle $\gamma$. Let $a$ and $b$ be the core circles of $M_1$ and $M_2$.

::: pf

::: {.pf-step #pieces}

$H_1(U)\cong\ZZ\langle a\rangle$, $H_1(V)\cong\ZZ\langle b\rangle$, $H_1(U\cap V)\cong\ZZ\langle\gamma\rangle$, all three are path-connected, and their homology vanishes in degrees $\ge2$.

::: pf-proof

$U$ and $V$ deformation retract onto the Möbius bands and then onto their core circles, and the annulus $U\cap V$ deformation retracts onto $\gamma$.

:::

:::

::: {.pf-step #phi1}

The Mayer-Vietoris map $\Phi_1=((i_1)_*,-(i_2)_*):H_1(U\cap V)\to H_1(U)\oplus H_1(V)$ is $\ZZ\to\ZZ^2$, $1\mapsto(2,-2)$.

::: pf-proof

The boundary circle of a Möbius band wraps twice around its core circle, so $(i_1)_*[\gamma]=2[a]$ and $(i_2)_*[\gamma]=2[b]$.

:::

:::

::: pf-step

$H_2(K)=0$ and $H_k(K)=0$ for $k\ge3$.

::: pf-proof

By step [](#pieces){.pf-ref}, the Mayer-Vietoris sequence gives $H_k(K)=0$ for $k\ge3$ and $0\to H_2(K)\to H_1(U\cap V)\xrightarrow{\Phi_1}H_1(U)\oplus H_1(V)$. By step [](#phi1){.pf-ref}, $\Phi_1$ is injective, so $H_2(K)\cong\ker\Phi_1=0$.

:::

:::

::: pf-step

$H_1(K)\cong\ZZ\oplus\ZZ/2\ZZ$.

::: pf-proof

The sequence continues $H_1(U)\oplus H_1(V)\to H_1(K)\to H_0(U\cap V)\xrightarrow{\Phi_0}H_0(U)\oplus H_0(V)$, where $\Phi_0:\ZZ\to\ZZ^2$, $1\mapsto(1,-1)$, is injective. So $H_1(K)\cong\coker\Phi_1=\ZZ^2/\langle(2,-2)\rangle$. In the basis $u=(1,0)$, $v=(1,-1)$ of $\ZZ^2$, the subgroup is $\langle 2v\rangle$, so the quotient is $\ZZ u\oplus\ZZ v/2\ZZ v\cong\ZZ\oplus\ZZ/2\ZZ$.

:::

:::

::: pf-step

$H_0(K)\cong\ZZ$.

::: pf-proof

$K$ is path-connected.

:::

:::

:::

:::
