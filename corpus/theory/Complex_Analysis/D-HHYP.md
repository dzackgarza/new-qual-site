---
schema: qual/card@1
id: D-HHYP
kind: definition
title: Hyperbolic metric on the upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Hyperbolic Metric
  - Upper Half-Plane
relations: []
review: draft
---

::: {.definition}
The \dfn{hyperbolic metric} on $\HH$ is the metric pulled back from the hyperbolic metric of the disc, [[D-2HXLN]], by a [[D-TM4TE|biholomorphism]] $\HH\to\DD$.
For the Cayley transform $\Psi(z)=(z-i)/(z+i)$ it is
$$
\rho_{\HH}(z)\abs{\dz}=\frac{\abs{\dz}}{2\Im z},
\qquad
d_{\HH}(z,w)=\operatorname{artanh}\frac{\abs{z-w}}{\abs{z-\bar w}} .
$$
The result does not depend on the biholomorphism chosen, because the disc metric is invariant under the automorphisms of $\DD$ ([[T-SCHPK]]).

This is the noneuclidean length of [@Ahl73, ch. 4, §3.4, Exercise 8], which asks how it is to be defined in the upper half plane; the definition above is the transport of [[D-2HXLN]] by $\Psi$, and the two identities $\abs{\Psi'(z)}=2/\abs{z+i}^2$ and $1-\abs{\Psi(z)}^2=4\Im z/\abs{z+i}^2$ give the formula.
:::
