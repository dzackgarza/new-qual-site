---
schema: qual/card@1
id: P-TOPF24A
kind: problem
title: No degree-1 map from lower to higher genus surface
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Homology
relations: []
review: draft
---

::: problem
Let $\Sigma_g$ be the closed orientable surface of genus $g \geq 0$.
Show that if $g < h$, there does not exist a degree 1 map $\Sigma_g \to \Sigma_h$.
:::

::: {.solution}
<1>1. Suppose $f:\Sigma_g\to\Sigma_h$ has degree $1$.
::: {.proof}
We will derive a contradiction from the induced map on first cohomology when $g<h$.
:::

<1>2. The pullback
$$f^*:H^1(\Sigma_h;\mathbb Q)\to H^1(\Sigma_g;\mathbb Q)$$
is injective.
::: {.proof}
A nonzero-degree map between closed oriented manifolds induces an injection on rational cohomology. Indeed, if $0\ne\alpha\in H^k(\Sigma_h;\mathbb Q)$, Poincaré duality gives $\beta$ with $\langle\alpha\smile\beta,[\Sigma_h]\rangle\ne0$, and naturality yields
$$\langle f^*\alpha\smile f^*\beta,[\Sigma_g]\rangle
=\deg(f)\langle\alpha\smile\beta,[\Sigma_h]\rangle\ne0.$$
:::

<1>3. But
$$\dim H^1(\Sigma_h;\mathbb Q)=2h>2g=\dim H^1(\Sigma_g;\mathbb Q).$$
::: {.proof}
The first Betti number of a closed orientable genus-$r$ surface is $2r$.
:::

<1>4. This contradicts injectivity. Therefore
$$\boxed{g<h\implies\text{no degree-}1\text{ map }\Sigma_g\to\Sigma_h.}$$
::: {.proof}
No injective linear map can go from a vector space of larger finite dimension to one of smaller dimension.
:::
:::
