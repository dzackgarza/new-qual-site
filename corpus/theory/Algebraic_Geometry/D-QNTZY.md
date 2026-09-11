---
schema: qual/card@1
id: D-QNTZY
kind: definition
title: Quasicoherent and coherent sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quasicoherent Sheaves
  - Coherent Sheaves
  - Modules
relations:
- kind: uses
  target: D-VKR54
review: draft
prompts:
- What is a quasicoherent sheaf?
- What does coherent add?
- How do you check quasicoherence?
---

::: {.definition title="Quasicoherent"}
For an $A$-module $M$, let $\tilde{M}$ be the sheaf on $\Spec A$ with $\tilde{M}(D_f) = M_f$.
An $\OO_X$-module $\mathcal{F}$ is **quasicoherent** if $X$ has an affine cover on which $\mathcal{F}$ is of the form $\tilde{M}$, and **coherent** if in addition each $M$ is finitely generated (over a Noetherian $X$).
:::

::: {.proposition}
On $\Spec A$, the functor $M \mapsto \tilde{M}$ is an exact equivalence from $A$-modules to quasicoherent sheaves, with inverse $\mathcal{F} \mapsto \mathcal{F}(X)$.
:::

::: {.remark}
Quasicoherence is the condition that a sheaf of modules is *determined by algebra*, locally: it is the analogue for modules of "scheme" for spaces.
The equivalence is what makes it useful, and the exactness is what makes cohomology of quasicoherent sheaves on an affine vanish.

The practical test is local and needs no module in hand: $\mathcal{F}$ is quasicoherent exactly when every point has an affine neighbourhood on which $\mathcal{F}$ has a presentation
\[
\OO_X^{(I)} \to \OO_X^{(J)} \to \mathcal{F} \to 0 .
\]
This is the form to use when the question is whether some naturally-occurring sheaf is quasicoherent, because a presentation can usually be written down where a module cannot.
:::
