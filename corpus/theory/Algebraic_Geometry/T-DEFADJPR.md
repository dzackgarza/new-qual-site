---
schema: qual/card@1
id: T-DEFADJPR
kind: proposition
title: The standard adjoint pairs
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

::: {.proposition title="useful adjoint pairs"}
The left adjoint is named first in each pair.

- "-ify" and "forget": free group on a set and the underlying set; sheafification and the inclusion of sheaves into presheaves; $\widetilde{\wait}$ from $\Gamma(X,\OO_X)$-modules to $\OO_X$-modules and global sections.

- Tensor $\wait \tensor_A N$ and $\Hom_A(N,\wait)$, as functors $\mods{A} \to \mods{A}$ for a fixed $A$-module $N$.

- Inverse image $\pi^{-1}$ and pushforward $\pi_*$, between sheaves on $X$ and sheaves on $Y$, for a fixed $\pi: X \to Y$.

- Pullback $\pi^*$ and pushforward $\pi_*$, between $\OO_X$-modules and $\OO_Y$-modules.

- Extension by zero $i_!$ and inverse image $i^{-1}$, for an open immersion $i: U \injects X$.
:::

::: {.remark}
By RAPL and LAPC each left adjoint here is right exact and each right adjoint left exact, so the list doubles as a table of which functors have interesting derived functors: $R^i\pi_*$ for pushforward, $\Tor$ for tensor, $\Ext$ for $\Hom$.

The last pair is the one with a surprise in it.
For an open immersion, $i^{-1}$ is a right adjoint (of $i_!$) and a left adjoint (of $i_*$) at the same time, so it is exact --- which is why restricting a short exact sequence of sheaves to an open set keeps it exact, and why exactness of sheaves may be checked on any open cover or on stalks.
:::
