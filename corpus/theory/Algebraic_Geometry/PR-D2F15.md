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
The affine toric variety $U_\sigma$ is smooth exactly when the vectors $\theset{v_\rho}_{\rho\in\sigma(1)}$ extend to a $\ZZ$-basis of $N$; such a cone is \dfn{smooth} [Cox--Little--Schenck, *Toric Varieties*, Theorem 1.3.12].
Consequently, $X_\Sigma$ is smooth exactly when every cone of $\Sigma$ is smooth.

The toric variety $X_\Sigma$ is $\QQ$-factorial exactly when every cone of $\Sigma$ is simplicial.
Cox--Little--Schenck prove at Theorem 11.4.8 that for a normal toric variety the cone $\Sigma$ being simplicial is equivalent to finite abelian quotient singularities, to being an orbifold, and to rational smoothness, and record in the remark following that theorem the form used here, that a normal toric variety is simplicial exactly when it is $\QQ$-factorial. The extraction read here carries that sentence unnumbered, so the criterion is cited to the theorem it follows rather than to a number of its own.
:::

::: {.proposition title="Toric resolution"}
Every fan $\Sigma$ admits a refinement $\Sigma'$ with $\abs{\Sigma'}=\abs\Sigma$, obtained from $\Sigma$ by a sequence of star subdivisions along primitive lattice vectors, and with $\Sigma'$ simplicial [Cox--Little--Schenck, *Toric Varieties*, Proposition 11.1.7]; refining the simplicial cones that remain singular by further star subdivisions makes $\Sigma'$ smooth.
The identity map on $N$ induces a proper birational toric morphism
$$
X_{\Sigma'}\longrightarrow X_\Sigma,
$$
and $X_{\Sigma'}$ is smooth, so this morphism is a resolution of singularities.
:::
