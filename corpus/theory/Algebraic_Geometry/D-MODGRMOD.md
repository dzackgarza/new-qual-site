---
schema: qual/card@1
id: D-MODGRMOD
kind: definition
title: The sheaf associated to a graded module, and $\Gamma_*$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Graded Modules
  - Proj
  - Twisting Sheaves
relations:
- kind: uses
  target: D-CB9XS
- kind: uses
  target: D-QNTZY
review: draft
prompts:
- Given a graded $S$-module, what sheaf does it define on $\Proj S$?
- What is $\Gamma_*(\mcf)$?
- Is the correspondence between graded modules and quasicoherent sheaves an equivalence?
---

::: {.definition title="$\tilde M$ and $\Gamma_*$"}
For $S$ a graded ring and $M$ a graded $S$-module, $\tilde M$ is the sheaf on $\Proj S$ with $\tilde M(D_+(f)) = (M_f)_0$, the degree-zero part of the localization.
Conversely, for $\mcf \in \mods{\OO_X}$ with $X = \Proj S$,
\[
\Gamma_*(\mcf) \da \bigoplus_{n \in \ZZ} \Gamma(X, \mcf(n)) ,
\]
a graded $S$-module, where $\mcf(n) \da \mcf \tensor_{\OO_X} \OO_X(n)$.
:::

::: {.theorem}
For $S$ generated in degree $1$ over a Noetherian ring $S_0$, every quasicoherent $\mcf$ on $\Proj S$ satisfies $\widetilde{\Gamma_*(\mcf)} \cong \mcf$, and $\OO_X(n) = \widetilde{S(n)}$.
:::

::: {.remark}
The direction that matters is that $\tilde{\wait\,}$ is essentially surjective, not that it is an equivalence — and it is not one.
Two graded modules agreeing in all large degrees give the same sheaf, so the functor kills modules supported at the irrelevant ideal $S_+$, and $\QCoh(\Proj S)$ is the quotient of graded modules by that torsion.
$\Gamma_*$ is the chosen splitting: it picks the saturated module in each class.

This is the projective analogue of $M \leftrightarrow \tilde M$ on $\Spec A$, with the degree-zero part of the localization playing the role of the localization, and the loss of injectivity is exactly the price of the irrelevant ideal.
A qual question here usually wants the failure named, with the example $S/S_+$, whose sheaf is zero.
:::
