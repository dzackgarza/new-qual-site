---
schema: qual/card@1
id: D-SHFFINE
kind: definition
title: Soft and fine sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaf Cohomology
  - Acyclic Sheaves
  - Partitions of Unity
relations:
- kind: related-to
  target: D-COHFLQ
review: draft
prompts:
- What is a fine sheaf?
- What is a soft sheaf?
---

::: {.definition title="Soft and fine sheaves"}
Let $X$ be a paracompact Hausdorff space and $\mathcal{F}$ a sheaf of abelian groups on $X$.

- $\mathcal{F}$ is \dfn{soft} if for every closed $Z \subseteq X$ the restriction $\Gamma(X, \mathcal{F}) \to \Gamma(Z, \mathcal{F}|_Z)$ is surjective.
- $\mathcal{F}$ is \dfn{fine} if for every locally finite open cover $\{U_i\}$ of $X$ there are sheaf endomorphisms $\eta_i \colon \mathcal{F} \to \mathcal{F}$ with the support of $\eta_i$ contained in $U_i$ and $\sum_i \eta_i = \mathrm{id}_{\mathcal{F}}$.
:::

::: {.proposition}
On a paracompact Hausdorff space, flasque sheaves and fine sheaves are soft, and soft sheaves are acyclic: $H^i(X, \mathcal{F}) = 0$ for $i > 0$.
So a resolution of a sheaf by fine sheaves computes its cohomology.
:::

::: {.example}
On a smooth manifold $M$, the sheaf $\mathcal{C}^\infty_M$ of smooth functions is fine, using a smooth partition of unity subordinate to the cover, and so is every sheaf of $\mathcal{C}^\infty_M$-modules, such as the sheaves $\mathcal{A}^p$ of smooth $p$-forms.
The de Rham complex $0 \to \ul{\RR} \to \mathcal{A}^0 \to \mathcal{A}^1 \to \cdots$ is a fine resolution of the constant sheaf, which proves $H^p(M, \RR) \cong H^p_{\mathrm{dR}}(M)$.
The sheaf of holomorphic functions on $\CC$ is not soft: a function holomorphic near the closed set $\{0, 1\}$, equal to $0$ near $0$ and $1$ near $1$, does not extend to an entire function.
:::
