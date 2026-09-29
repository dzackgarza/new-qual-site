---
schema: qual/card@1
id: P-TOPS23D
kind: problem
title: "Closed non-orientable 3-manifold has zero Euler characteristic and infinite fundamental group"
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Fundamental Group
  - Manifolds
  - Orientation
relations: []
review: draft
---

::: {.problem}
Let $M^3$ be a closed path-connected non-orientable $3$-manifold.
Show that its Euler characteristic is $0$ and that its fundamental group is infinite.
:::

::: {.solution}

::: pf

::: pf-step
Let $\widehat M\to M$ be the orientation double cover. Then $\widehat M$ is a closed orientable $3$-manifold and
$$\chi(\widehat M)=2\chi(M).$$

::: pf-proof
The orientation cover has two sheets, and Euler characteristic multiplies under finite coverings.
:::

:::

::: pf-step
Poincaré duality on the closed orientable odd-dimensional manifold $\widehat M$ gives $\chi(\widehat M)=0$. Hence
$$\boxed{\chi(M)=0.}$$

::: pf-proof
In odd dimension the Betti numbers pair as $b_i=b_{3-i}$ with opposite signs in the Euler sum, so the sum cancels.
:::

:::

::: {.pf-step #h1-h2-vanish-rationally}
Suppose for contradiction that $\pi_1(M)$ were finite. Then $\pi_1(\widehat M)$ would also be finite, so
$$H_1(\widehat M;\mathbb Q)=H_2(\widehat M;\mathbb Q)=0.$$

::: pf-proof
The first rational homology is the rationalization of the abelianization of the finite group $\pi_1(\widehat M)$, hence zero. Poincaré duality then gives $H_2\cong H^1=0$ rationally.
:::

:::

::: pf-step
The nontrivial deck involution $\tau$ of the orientation cover reverses orientation, hence acts by $-1$ on $H_3(\widehat M;\mathbb Q)$ and by $+1$ on $H_0$.

::: pf-proof
By definition, the deck involution exchanges the two local orientations. On the fundamental class of the connected orientable cover it therefore has degree $-1$.
:::

:::

::: pf-step
Its Lefschetz number is
$$L(\tau)=1-(-1)=2\ne0,$$
so $\tau$ has a fixed point.

::: pf-proof
By step [](#h1-h2-vanish-rationally){.pf-ref}, only degrees $0$ and $3$ contribute. Thus
$$L(\tau)=\operatorname{tr}(H_0)-\operatorname{tr}(H_3)=1-(-1)=2.$$
The Lefschetz fixed-point theorem then forces a fixed point.
:::

:::

::: pf-step
This is impossible for a nontrivial deck transformation. Therefore
$$\boxed{\pi_1(M)\text{ is infinite}.}$$

::: pf-proof
Deck transformations of a connected covering act freely on the total space.
:::

:::

:::

:::
