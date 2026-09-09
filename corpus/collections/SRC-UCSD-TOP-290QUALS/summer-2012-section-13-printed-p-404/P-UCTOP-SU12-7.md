---
schema: qual/card@1
id: P-UCTOP-SU12-7
kind: problem
title: H_2 of simply-connected closed 4-manifold is free of rank chi-2
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
---

Show that the second homology group $H_2(X; \mathbb{Z})$ of a closed, path-connected, simply-connected 4-manifold $X$ is free and has rank $\chi(X) - 2$, where $\chi(X)$ is the Euler characteristic.

::: {.solution}
<1>1. The manifold $X$ is orientable.
::: {.proof}
A connected manifold is orientable iff its orientation character $\pi_1(X)\to\{\pm1\}$ is trivial. Since $X$ is simply connected, this character is trivial.
:::

<1>2. We have
$$
H_1(X;\mathbb Z)=H_3(X;\mathbb Z)=0.
$$
::: {.proof}
Simple connectivity gives $H_1=0$. Poincaré duality gives
$$
H_3(X)\cong H^1(X),
$$
and the universal coefficient theorem gives $H^1(X)=\operatorname{Hom}(H_1(X),\mathbb Z)=0$.
:::

<1>3. The group $H_2(X;\mathbb Z)$ is free abelian.
::: {.proof}
Poincaré duality gives $H_2(X)\cong H^2(X)$. The cohomological universal coefficient theorem gives
$$
0\to\operatorname{Ext}(H_1(X),\mathbb Z)\to H^2(X)\to\operatorname{Hom}(H_2(X),\mathbb Z)\to0.
$$
Since $H_1(X)=0$, this becomes
$$
H^2(X)\cong\operatorname{Hom}(H_2(X),\mathbb Z),
$$
which is free abelian. Therefore the isomorphic group $H_2(X)$ is free abelian as well.
:::

<1>4. If $b_2=\operatorname{rank}H_2(X)$, then
$$
\chi(X)=2+b_2.
$$
::: {.proof}
For a closed connected oriented $4$-manifold,
$$
H_0(X)\cong H_4(X)\cong\mathbb Z.
$$
By <1>2, $H_1$ and $H_3$ vanish. Thus
$$
\chi(X)=1+b_2+1=2+b_2.
$$
:::

<1>5. Hence
$$
\boxed{H_2(X;\mathbb Z)\cong\mathbb Z^{\chi(X)-2}}.
$$
::: {.proof}
Combine <1>3 and <1>4.
:::
:::
