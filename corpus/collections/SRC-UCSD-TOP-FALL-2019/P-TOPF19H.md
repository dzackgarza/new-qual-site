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

<1>1. One has
$$
\dim_{\mathbb Q}H_1(\Sigma;\mathbb Q)=2g.
$$
::: {.proof}
A closed connected orientable surface of genus $g$ has first Betti number $2g$.
:::

<1>2. The map
$$
H_0(\Sigma;\mathbb Q)\longrightarrow H_0(M;\mathbb Q)
$$
is an isomorphism.
::: {.proof}
Both $\Sigma$ and $M$ are connected, and inclusion sends the generator represented by a point of $\Sigma$ to the generator represented by the same point in $M$.
:::

<1>3. The long exact sequence of $(M,\Sigma)$ therefore gives a surjection
$$
H_1(M;\mathbb Q)\twoheadrightarrow H_1(M,\Sigma;\mathbb Q)
$$
whose kernel is $\operatorname{im}i_*$.
::: {.proof}
The relevant segment is
$$
H_1(\Sigma)\xrightarrow{i_*}H_1(M)\longrightarrow H_1(M,\Sigma)
\longrightarrow H_0(\Sigma)\longrightarrow H_0(M).
$$
By <1>2 the last arrow is injective, so exactness forces the preceding connecting map to be zero. Hence $H_1(M)\to H_1(M,\Sigma)$ is surjective and its kernel is $\operatorname{im}i_*$.
:::

<1>4. Poincaré--Lefschetz duality gives
$$
\dim H_1(M,\Sigma;\mathbb Q)=b_2(M).
$$
::: {.proof}
For an orientable compact $3$-manifold,
$$
H_1(M,\partial M;\mathbb Q)\cong H^{2}(M;\mathbb Q).
$$
Over the field $\mathbb Q$, the universal coefficient theorem gives
$\dim H^2(M;\mathbb Q)=\dim H_2(M;\mathbb Q)=b_2(M)$.
:::

<1>5. Consequently
$$
\dim\operatorname{im}i_*=b_1(M)-b_2(M).
$$
::: {.proof}
Take dimensions in the short exact sequence furnished by <1>3 and apply <1>4.
:::

<1>6. The Euler characteristics satisfy
$$
\chi(\Sigma)=2\chi(M).
$$
::: {.proof}
Double $M$ along its boundary to obtain the closed orientable $3$-manifold $DM$. Inclusion--exclusion for Euler characteristic gives
$$
\chi(DM)=2\chi(M)-\chi(\Sigma).
$$
Every closed orientable odd-dimensional manifold has Euler characteristic $0$ by Poincaré duality, so $0=2\chi(M)-\chi(\Sigma)$.
:::

<1>7. Hence
$$
b_1(M)-b_2(M)=g.
$$
::: {.proof}
Since $\Sigma$ has genus $g$, $\chi(\Sigma)=2-2g$, so <1>6 gives $\chi(M)=1-g$. Because $M$ is connected and has nonempty boundary,
$$
b_0(M)=1,\qquad b_3(M)=0.
$$
Thus
$$
1-g=\chi(M)=1-b_1(M)+b_2(M),
$$
which rearranges to $b_1(M)-b_2(M)=g$.
:::

<1>8. Therefore
$$
\dim\operatorname{im}i_*=g.
$$
::: {.proof}
Combine <1>5 and <1>7.
:::

<1>9. Finally,
$$
\boxed{\dim\ker i_*=g.}
$$
::: {.proof}
Rank--nullity and <1>1, <1>8 give
$$
\dim\ker i_*=\dim H_1(\Sigma)-\dim\operatorname{im}i_*=2g-g=g.
$$
:::
:::
