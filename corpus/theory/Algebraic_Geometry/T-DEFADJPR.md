---
schema: qual/card@1
id: T-DEFADJPR
kind: proposition
title: The standard adjoint pairs
slogan: 'Adjunction predicts exactness: left adjoints are right exact, right adjoints are left exact, and open restriction is both, hence exact.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Category Theory
  - Adjunctions
relations:
- kind: uses
  target: D-DEFADJ
- kind: uses
  target: T-DEFRAPL
review: draft
prompts:
- List the adjoint pairs used constantly in algebraic geometry, saying which functor is the left adjoint.
- Why is $i^{-1}$ exact for an open immersion $i$?
---

::: {.proposition title="Useful adjoint pairs"}
The left adjoint is named first in each pair.

- Free and forgetful functors: free group on a set and the underlying set; sheafification and the inclusion of sheaves into presheaves.

- For $X=\Spec A$, the functor $M\mapsto\widetilde M$ from $A$-modules to quasicoherent $\OO_X$-modules and global sections $\Gamma(X,-)$.

- Tensor $\wait \tensor_A N$ and $\Hom_A(N,\wait)$, as functors $\mods{A} \to \mods{A}$ for a fixed $A$-module $N$.

- Inverse image $\pi^{-1}$ and pushforward $\pi_*$, between sheaves on $X$ and sheaves on $Y$, for a fixed $\pi: X \to Y$.

- Pullback $\pi^*$ and pushforward $\pi_*$, between $\OO_X$-modules and $\OO_Y$-modules.

- Extension by zero $i_!$ and inverse image $i^{-1}$, for an open immersion $i: U \injects X$.
:::

::: {.remark}
For the adjunctions between abelian categories, [[T-DEFRAPL]] implies that an additive left adjoint is right exact and an additive right adjoint is left exact. Thus $\wait\tensor_A N$ is right exact, $\Hom_A(N,\wait)$ and $\pi_*$ are left exact, and their failures of exactness lead to $\Tor$, $\Ext$, and $R^i\pi_*$. This exactness language does not apply to the Set/Grp adjunction in the first bullet.

For an open immersion, $i^{-1}$ is a right adjoint (of $i_!$) and a left adjoint (of $i_*$) at the same time, so it is exact; in particular, restricting a short exact sequence of sheaves to an open set keeps it exact.
:::
