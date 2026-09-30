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
For a closed immersion $i: Z \injects X$, the \dfn{ideal sheaf} is
$$
\mci_Z \definedas \ker\qty{\OO_X \mapsvia{i^\sharp} i_*\OO_Z} .
$$
:::

::: {.theorem}
$Z \mapsto \mci_Z$ is a bijection between closed subschemes of $X$ and quasicoherent sheaves of ideals on $X$, and there is a short exact sequence
$$
0 \to \mci_Z \to \OO_X \to i_*\OO_Z \to 0 .
$$
:::

::: {.remark}
On $X=\Spec A$, the bijection sends $V(I)$ to $\tilde I$ for ideals $I\subseteq A$.
A sheaf of ideals that is not quasicoherent is the ideal sheaf of no closed subscheme: for $X=\AA^1_k$, $U=X\sm\theset{0}$, and $j\colon U\injects X$ the inclusion, the extension by zero $j_!\OO_U\subseteq\OO_X$ is a sheaf of ideals with $\Gamma(X,j_!\OO_U)=0$ and $j_!\OO_U|_U=\OO_U$, so it is not quasicoherent.

For a hypersurface $Z\subseteq\PP^n$ of degree $d$, $\mci_Z \cong \OO_{\PP^n}(-d)$, and for $n\ge2$ the twisted sequence $0\to\OO(m-d)\to\OO(m)\to\OO_Z(m)\to0$ gives $h^0(\OO_Z(m))=h^0(\OO_{\PP^n}(m))-h^0(\OO_{\PP^n}(m-d))$, since $H^1(\PP^n,\OO(m-d))=0$.
The restriction $i^*\mci_Z=\mci_Z/\mci_Z^2$ is the conormal sheaf of $Z$ ([[D-MODCONORM]]).
:::
