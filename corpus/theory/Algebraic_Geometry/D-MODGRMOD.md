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
$$
\Gamma_*(\mcf) \da \bigoplus_{n \in \ZZ} \Gamma(X, \mcf(n)) ,
$$
a graded $S$-module, where $\mcf(n) \da \mcf \tensor_{\OO_X} \OO_X(n)$.
:::

::: {.theorem}
For $S$ generated in degree $1$ over a Noetherian ring $S_0$, every quasicoherent $\mcf$ on $\Proj S$ satisfies $\widetilde{\Gamma_*(\mcf)} \cong \mcf$, and $\OO_X(n) = \widetilde{S(n)}$.
:::

::: {.remark}
Under the hypotheses of the theorem, the functor $M\mapsto\tilde M$ is essentially surjective onto quasicoherent sheaves, with $\mcf\cong\widetilde{\Gamma_*(\mcf)}$, and it is not an equivalence.
A graded homomorphism $M\to M'$ that is an isomorphism in all sufficiently large degrees induces an isomorphism $\tilde M\cong\tilde M'$, and a graded module with $M_n=0$ for all $n\gg0$ has $\tilde M=0$; for example, $\widetilde{S/S_+}=0$ while $S/S_+\ne0$.
The category $\QCoh(\Proj S)$ is the quotient of the category of graded $S$-modules by the modules annihilated by a power of $S_+$.
:::
