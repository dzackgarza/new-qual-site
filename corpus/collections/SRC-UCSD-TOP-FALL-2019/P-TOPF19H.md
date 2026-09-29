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

::: {.problem}
Let $M$ be a compact, orientable $3$-dimensional manifold.
Suppose the boundary of $M$ is a surface $\Sigma$ of genus $g$.
Let $i_* : H_1(\Sigma; \mathbb{Q}) \to H_1(M; \mathbb{Q})$ be the map induced by the inclusion of the boundary.
Show that the dimension of $\ker i_*$ equals $g$.
:::

::: {.solution}
It is enough to work with the connected component of $M$ whose boundary is $\Sigma$; any additional closed components do not meet $\Sigma$ and do not affect the kernel. Thus assume $M$ is connected.

::: pf

::: {.pf-step #s1}

One has
$$
\dim_{\mathbb Q}H_1(\Sigma;\mathbb Q)=2g.
$$

::: pf-proof

A closed connected orientable surface of genus $g$ has first Betti number $2g$.

:::

:::

::: {.pf-step #s2}

The map
$$
H_0(\Sigma;\mathbb Q)\longrightarrow H_0(M;\mathbb Q)
$$
is an isomorphism.

::: pf-proof

Both $\Sigma$ and $M$ are connected, and inclusion sends the generator represented by a point of $\Sigma$ to the generator represented by the same point in $M$.

:::

:::

::: {.pf-step #s3}

The long exact sequence of $(M,\Sigma)$ therefore gives a surjection
$$
H_1(M;\mathbb Q)\twoheadrightarrow H_1(M,\Sigma;\mathbb Q)
$$
whose kernel is $\operatorname{im}i_*$.

::: pf-proof

The relevant segment is
$$
H_1(\Sigma)\xrightarrow{i_*}H_1(M)\longrightarrow H_1(M,\Sigma)
\longrightarrow H_0(\Sigma)\longrightarrow H_0(M).
$$
By step [](#s2){.pf-ref} the last arrow is injective, so exactness forces the preceding connecting map to be zero. Hence $H_1(M)\to H_1(M,\Sigma)$ is surjective and its kernel is $\operatorname{im}i_*$.

:::

:::

::: {.pf-step #s4}

Poincaré--Lefschetz duality gives
$$
\dim H_1(M,\Sigma;\mathbb Q)=b_2(M).
$$

::: pf-proof

For an orientable compact $3$-manifold,
$$
H_1(M,\partial M;\mathbb Q)\cong H^{2}(M;\mathbb Q).
$$
Over the field $\mathbb Q$, the universal coefficient theorem gives
$\dim H^2(M;\mathbb Q)=\dim H_2(M;\mathbb Q)=b_2(M)$.

:::

:::

::: {.pf-step #s5}

Consequently
$$
\dim\operatorname{im}i_*=b_1(M)-b_2(M).
$$

::: pf-proof

Take dimensions in the short exact sequence furnished by step [](#s3){.pf-ref} and apply step [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

The Euler characteristics satisfy
$$
\chi(\Sigma)=2\chi(M).
$$

::: pf-proof

Double $M$ along its boundary to obtain the closed orientable $3$-manifold $DM$. Inclusion--exclusion for Euler characteristic gives
$$
\chi(DM)=2\chi(M)-\chi(\Sigma).
$$
Every closed orientable odd-dimensional manifold has Euler characteristic $0$ by Poincaré duality, so $0=2\chi(M)-\chi(\Sigma)$.

:::

:::

::: {.pf-step #s7}

Hence
$$
b_1(M)-b_2(M)=g.
$$

::: pf-proof

Since $\Sigma$ has genus $g$, $\chi(\Sigma)=2-2g$, so step [](#s6){.pf-ref} gives $\chi(M)=1-g$. Because $M$ is connected and has nonempty boundary,
$$
b_0(M)=1,\qquad b_3(M)=0.
$$
Thus
$$
1-g=\chi(M)=1-b_1(M)+b_2(M),
$$
which rearranges to $b_1(M)-b_2(M)=g$.

:::

:::

::: {.pf-step #s8}

Therefore
$$
\dim\operatorname{im}i_*=g.
$$

::: pf-proof

Combine steps [](#s5){.pf-ref} and [](#s7){.pf-ref}.

:::

:::

::: pf-step

Finally,
$$
\boxed{\dim\ker i_*=g.}
$$

::: pf-proof

Rank--nullity and steps [](#s1){.pf-ref} and [](#s8){.pf-ref} give
$$
\dim\ker i_*=\dim H_1(\Sigma)-\dim\operatorname{im}i_*=2g-g=g.
$$

:::

:::

:::

:::
