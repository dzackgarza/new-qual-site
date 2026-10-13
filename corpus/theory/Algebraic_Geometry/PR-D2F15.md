---
schema: qual/card@1
id: PR-D2F15
kind: proposition
title: Smoothness and resolution from a fan
slogan: 'For toric varieties, smoothness is a lattice-basis condition and resolution is subdivision of the fan.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Resolution of Singularities
  - Fans
relations:
- kind: uses
  target: PR-O8V3I
review: draft
prompts:
- When is a toric variety smooth?
- How do you resolve a toric singularity?
---

::: {.proposition}
Let $N$ be a lattice, let $\Sigma$ be a fan in $N_\RR$, and let $\sigma\in\Sigma$. For each ray $\rho\in\sigma(1)$, let $v_\rho\in N$ be its primitive generator.
The affine toric variety $U_\sigma$ is smooth exactly when the vectors $\theset{v_\rho}_{\rho\in\sigma(1)}$ extend to a $\ZZ$-basis of $N$; such a cone is \dfn{smooth}.
Consequently, $X_\Sigma$ is smooth exactly when every cone of $\Sigma$ is smooth.

The toric variety $X_\Sigma$ is $\QQ$-factorial exactly when every cone of $\Sigma$ is simplicial.
:::

::: {.proposition title="Toric resolution"}
Every fan $\Sigma$ admits a smooth refinement $\Sigma'$ with $\abs{\Sigma'}=\abs\Sigma$. It may be obtained by a finite sequence of star subdivisions along primitive lattice vectors. The identity map on $N$ induces a proper birational toric morphism
$$
X_{\Sigma'}\longrightarrow X_\Sigma,
$$
and $X_{\Sigma'}$ is smooth, so this morphism is a resolution of singularities.
:::
