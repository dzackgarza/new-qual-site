---
schema: qual/card@1
id: D-MODIDEAL
kind: definition
title: The ideal sheaf of a closed subscheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ideal Sheaves
  - Closed Subschemes
  - Quasicoherent Sheaves
relations:
- kind: uses
  target: D-QNTZY
- kind: uses
  target: D-MODPULL
review: draft
prompts:
- What is the ideal sheaf of a closed subscheme?
- What is the correspondence between closed subschemes and ideal sheaves?
- What is the closed subscheme exact sequence?
---

::: {.definition title="Ideal sheaf"}
For a closed immersion $i: Z \injects X$, the **ideal sheaf** is
\[
\mci_Z \da \ker\qty{\OO_X \mapsvia{i^\sharp} i_*\OO_Z} .
\]
:::

::: {.theorem}
$Z \mapsto \mci_Z$ is a bijection between closed subschemes of $X$ and quasicoherent sheaves of ideals on $X$, and there is a short exact sequence
\[
0 \to \mci_Z \to \OO_X \to i_*\OO_Z \to 0 .
\]
:::

::: {.remark}
This is the sheaf-level version of the correspondence between ideals of $A$ and closed subschemes of $\Spec A$, and quasicoherence is exactly the condition that makes the local statements glue: a non-quasicoherent subsheaf of $\OO_X$ is not cut out by equations.

The exact sequence is the workhorse.
Twisting it by $\OO(d)$ and taking cohomology is how one computes $h^0$ of a hypersurface or a curve in $\PP^n$ from the ambient space, since $\mci_Z = \OO_{\PP^n}(-d)$ when $Z$ is a degree-$d$ hypersurface.
Restricting it to $Z$ produces the conormal sheaf $\mci_Z/\mci_Z^2$, which is where the sequence meets [differentials](wiki/algebraic-geometry/sheaves-of-modules/differentials.html).
:::
