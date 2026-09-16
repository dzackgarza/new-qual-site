---
schema: qual/card@1
id: P-TOPS07G
kind: problem
title: "Closed 2-connected 6-manifold has even Euler characteristic"
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Manifolds
  - Poincaré Duality
relations: []
review: draft
---

::: {.problem}
Show that any closed (i.e. compact, without boundary) $6$-manifold which is $2$-connected (i.e. is path-connected, simply-connected and has $\pi_2 = 0$) must have even Euler characteristic.
:::

::: {.solution}
<1>1. Since $M$ is $2$-connected, $H_1(M;\mathbb Z)=H_2(M;\mathbb Z)=0$.
::: {.proof}
Simple connectivity gives $H_1=0$. Since $\pi_1=\pi_2=0$, the Hurewicz theorem gives $H_2=0$ as well.
:::

<1>2. The manifold is orientable, and Poincaré duality gives
$$
H_4(M;\mathbb Z)=H_5(M;\mathbb Z)=0,
$$
while $H_0\cong H_6\cong\mathbb Z$.
::: {.proof}
A simply connected manifold is orientable. Integral Poincaré duality identifies $H_i$ with $H^{6-i}$; the universal coefficient theorem and the vanishing of $H_1,H_2$ give the corresponding vanishing in degrees $5,4$. Connectedness and orientability give the bottom and top homology groups.
:::

<1>3. Hence
$$
\chi(M)=2-b_3(M).
$$
::: {.proof}
All Betti numbers vanish except $b_0=b_6=1$ and possibly $b_3$, so the alternating sum is $1- b_3+1$.
:::

<1>4. The middle-dimensional intersection form on $H_3(M;\mathbb Q)$ is skew-symmetric and nondegenerate, so $b_3(M)$ is even.
::: {.proof}
For an oriented $6$-manifold, the intersection pairing in dimension $3$ satisfies $x\cdot y=(-1)^{3\cdot3}y\cdot x=-y\cdot x$. Poincaré duality makes this pairing nondegenerate. A nondegenerate skew-symmetric bilinear form over a field of characteristic different from $2$ has even dimension.
:::

<1>5. Therefore
$$
\boxed{\chi(M)\text{ is even}.}
$$
::: {.proof}
By <1>3, $\chi(M)=2-b_3(M)$, and <1>4 shows $b_3(M)$ is even.
:::
:::
