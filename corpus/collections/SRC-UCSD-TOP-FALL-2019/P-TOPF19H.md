---
schema: qual/card@1
id: P-TOPF19H
kind: problem
title: "Half die half alive: kernel of boundary inclusion on H_1 has dimension g"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Manifolds
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $M$ be a compact, orientable $3$-dimensional manifold.
Suppose the boundary of $M$ is a surface $\Sigma$ of genus $g$.
Let $i_* : H_1(\Sigma; \mathbb{Q}) \to H_1(M; \mathbb{Q})$ be the map induced by the inclusion of the boundary.
Show that the dimension of $\ker i_*$ equals $g$.
:::

::: {.solution}
<1>1. $\dim_\QQ H_1(\Sigma; \QQ) = 2g$.
::: {.proof}
$\Sigma$ is a closed orientable surface of genus $g$, so its first Betti number is $2g$.
:::

<1>2. By Poincaré–Lefschetz duality, $H_1(M; \QQ) \cong H^2(M, \partial M; \QQ)$.
::: {.proof}
duality for a compact orientable $3$-manifold with boundary.
:::

<1>3. The long exact sequence of the pair $(M, \partial M)$ gives
$$H_1(\partial M) \xrightarrow{i_*} H_1(M) \to H_1(M, \partial M) \to H_0(\partial M) \to H_0(M).$$
::: {.proof}
homology long exact sequence of the pair.
:::

<1>4. $H_0(\partial M) \to H_0(M)$ is an isomorphism (both $\cong \QQ$, since $\partial M$ and $M$ are connected).
::: {.proof}
$\Sigma$ is connected and $M$ is connected.
:::

<1>5. Hence $H_1(M, \partial M) \to H_0(\partial M)$ is injective, so the sequence
$$H_1(\partial M) \xrightarrow{i_*} H_1(M) \to H_1(M, \partial M) \to 0$$
is exact.
::: {.proof}
<1>3 and <1>4.
:::

<1>6. Therefore $\operatorname{im} i_* \cong H_1(M)/\ker$, and $\dim \operatorname{im} i_* = \dim H_1(M) - \dim \ker i_*$.
::: {.proof}
rank-nullity.
:::

<1>7. By duality, $\dim H_1(M; \QQ) = \dim H^2(M, \partial M; \QQ) = \dim H_1(M, \partial M; \QQ)$.
::: {.proof}
<1>2 and the universal coefficient theorem over $\QQ$.
:::

<1>8. From the exact sequence in <1>5, $\dim H_1(\partial M) = \dim \operatorname{im} i_* + \dim H_1(M, \partial M)$.
::: {.proof}
exactness at $H_1(M)$.
:::

<1>9. Substituting: $2g = \dim \operatorname{im} i_* + \dim H_1(M)$.
::: {.proof}
<1>1, <1>7, <1>8.
:::

<1>10. Also $\dim H_1(\partial M) = \dim \ker i_* + \dim \operatorname{im} i_*$, so $2g = \dim \ker i_* + \dim \operatorname{im} i_*$.
::: {.proof}
rank-nullity for $i_*$.
:::

<1>11. Comparing <1>9 and <1>10, $\dim \ker i_* = \dim H_1(M)$.
::: {.proof}
both equal $2g - \dim \operatorname{im} i_*$.
:::

<1>12. The image of $i_*$ is a Lagrangian (half-dimensional) subspace: $\dim \operatorname{im} i_* = g$.
::: {.proof}
the intersection form on $H_1(\Sigma)$ vanishes on $\operatorname{im} i_*$ (the boundary of $M$ is null-homologous in $M$), and $\operatorname{im} i_*$ is a maximal isotropic subspace, hence has dimension $g$.
:::

<1>13. Hence $\dim \ker i_* = 2g - g = g$.
::: {.proof}
<1>10 and <1>12.
:::

<1>14. Q.E.D.
::: {.proof}
<1>13.
:::
:::
