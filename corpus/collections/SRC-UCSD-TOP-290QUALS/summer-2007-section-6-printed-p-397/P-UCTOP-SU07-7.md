---
schema: qual/card@1
id: P-UCTOP-SU07-7
kind: problem
title: 2-connected closed 6-manifold has even Euler characteristic
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
---

Show that any closed (i.e. compact, without boundary) 6-manifold which is 2-connected (i.e. is path-connected, simply-connected and has $\pi_2 = 0$) must have even Euler characteristic.

::: {.solution}
<1>1. The manifold $M^6$ is orientable.
::: {.proof}
A connected manifold is orientable exactly when its orientation character $\pi_1(M)\to\{\pm1\}$ is trivial. Since $M$ is simply connected, its fundamental group is trivial, so the orientation character vanishes.
:::

<1>2. We have
$$
H_1(M;\mathbb Z)=H_2(M;\mathbb Z)=0.
$$
:::
::: {.proof}
Simple connectivity gives $H_1=0$. Since $M$ is simply connected, the Hurewicz map $\pi_2(M)\to H_2(M)$ is an isomorphism; the hypothesis $\pi_2(M)=0$ therefore gives $H_2=0$.
:::

<1>3. By Poincaré duality,
$$
b_4=b_2=0,\qquad b_5=b_1=0,\qquad b_6=b_0=1.
$$
:::
::: {.proof}
For the closed orientable $6$-manifold $M$, Poincaré duality over $\mathbb Q$ gives $H_i(M;\mathbb Q)\cong H_{6-i}(M;\mathbb Q)^*$. Combine this with <1>2 and connectedness.
:::

<1>4. The middle Betti number $b_3$ is even.
::: {.proof}
The intersection pairing on the free vector space $H_3(M;\mathbb Q)$ is nondegenerate by Poincaré duality. Graded commutativity in middle dimension gives
$$
\lambda(x,y)=(-1)^{3\cdot3}\lambda(y,x)=-\lambda(y,x),
$$
so $\lambda$ is a nondegenerate skew-symmetric bilinear form. A skew-symmetric matrix of odd size has determinant zero; therefore a nondegenerate skew-symmetric form has even dimension. Hence $b_3$ is even.
:::

<1>5. Therefore
$$
\chi(M)=2-b_3
$$
is even.
:::
::: {.proof}
Using <1>2--<1>3,
$$
\chi(M)=b_0-b_1+b_2-b_3+b_4-b_5+b_6=1-b_3+1=2-b_3.
$$
By <1>4, $b_3$ is even.
:::
:::

