---
schema: qual/card@1
id: P-TOPF07H
kind: problem
title: "Euler characteristic of a closed orientable odd-dimensional manifold is zero"
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

::: problem
Show that the Euler characteristic of a closed orientable odd-dimensional manifold is zero.
Is this still true if the manifold is non-orientable?
:::

::: {.solution}
<1>1. If $M$ is a closed orientable manifold of odd dimension $d$, Poincaré duality gives
$$
b_i=b_{d-i}
$$
for its rational Betti numbers.
::: {.proof}
Integral orientability implies Poincaré duality over $\mathbb Q$.
:::

<1>2. Since $d$ is odd, the terms in
$$
\chi(M)=\sum_{i=0}^d(-1)^i b_i
$$
pair with opposite signs, so $\chi(M)=0$.
::: {.proof}
For paired indices $i$ and $d-i$, one has $(-1)^{d-i}=-(-1)^i$ because $d$ is odd, while the Betti numbers agree by <1>1.
:::

<1>3. The conclusion remains true without orientability.
::: {.proof}
Use Poincaré duality with $\mathbb F_2$ coefficients, which holds for every closed manifold. If $c_i=\dim_{\mathbb F_2}H_i(M;\mathbb F_2)$, then $c_i=c_{d-i}$. Euler characteristic can be computed over any field, so
$$
\chi(M)=\sum_i(-1)^i c_i,
$$
and the same opposite-sign pairing shows this integer is zero.
:::

<1>4. Thus
$$
\boxed{\chi(M)=0\text{ for every closed odd-dimensional manifold}.}
$$
::: {.proof}
Combine <1>2 and <1>3.
:::
:::
