---
schema: qual/card@1
id: P-TOPF06E
kind: problem
title: "Sum of mod-2 Betti numbers equals Euler characteristic mod 2 for closed 2n-manifolds"
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Poincaré Duality
  - Manifolds
  - Mod 2
relations: []
review: draft
---

::: problem
Let $M$ be a $2n$ dimensional compact manifold without boundary.
Show that
$$
\dim H^n(M; \mathbb{Z}/2) = \chi(M) \pmod{2}
$$
where $\chi(M)$ denotes the Euler characteristic of $M$.
:::

::: {.solution}
<1>1. Write $b_i=\dim_{\mathbb F_2}H^i(M;\mathbb F_2)$. Mod-$2$ Poincaré duality gives
$$
b_i=b_{2n-i}.
$$
::: {.proof}
Every closed manifold is orientable over $\mathbb F_2$, so Poincaré duality applies without an orientability hypothesis.
:::

<1>2. The Euler characteristic is
$$
\chi(M)=\sum_{i=0}^{2n}(-1)^i b_i.
$$
Modulo $2$, the signs disappear.
::: {.proof}
Euler characteristic may be computed from homology over any field. In $\mathbb Z/2$, $-1=1$.
:::

<1>3. Pairing the terms $b_i$ and $b_{2n-i}$ for $i<n$, each pair contributes $2b_i\equiv0\pmod2$.
::: {.proof}
Use <1>1; every degree except the middle degree occurs in one such pair.
:::

<1>4. Hence only the middle Betti number survives modulo $2$:
$$
\boxed{\chi(M)\equiv \dim_{\mathbb F_2}H^n(M;\mathbb F_2)\pmod2}.
$$
::: {.proof}
Combine <1>2 and <1>3.
:::
:::
