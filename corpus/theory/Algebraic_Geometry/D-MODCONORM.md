---
schema: qual/card@1
id: D-MODCONORM
kind: definition
title: The conormal and normal sheaves, and adjunction
classification:
  areas:
  - algebraic-geometry
  topics:
  - Conormal Sheaf
  - Canonical Sheaf
  - Closed Subschemes
relations:
- kind: uses
  target: D-MODIDEAL
- kind: uses
  target: D-4GCH6
review: draft
prompts:
- What is the conormal sheaf of a closed subscheme?
- State the adjunction formula.
- What is the canonical sheaf of a degree $d$ plane curve?
---

::: {.definition title="Conormal and normal"}
For a closed immersion $i: Z \injects X$ with ideal sheaf $\mci$, the \dfn{conormal sheaf} is $\mci/\mci^2$, an $\OO_Z$-module, and the **normal sheaf** is its dual $\mcn_{Z/X} \da \sheafhom_{\OO_Z}(\mci/\mci^2, \OO_Z)$.
:::

::: {.theorem title="Adjunction"}
If $Z$ and $X$ are smooth over $k$ of dimensions $m$ and $n$, the conormal sequence is short exact,
\[
0 \to \mci/\mci^2 \to \ro{\Omega_{X/k}}{Z} \to \Omega_{Z/k} \to 0 ,
\]
$\mci/\mci^2$ is locally free of rank $n - m$, and taking determinants gives
\[
\omega_Z \cong \ro{\omega_X}{Z} \tensor_{\OO_Z} \Extpower^{n-m}\mcn_{Z/X} ,
\]
where $\mcn_{Z/X}$ is already an $\OO_Z$-module, so $\omega_X$ is restricted to $Z$ before tensoring.
:::

::: {.theorem title="Adjunction for a divisor"}
For $Z \subseteq X$ a smooth effective divisor, $\mci = \OO_X(-Z)$ and
\[
\omega_Z = \ro{\qty{\omega_X \tensor \OO_X(Z)}}{Z} .
\]
:::

::: {.remark}
The conormal sheaf is $\mci$ restricted to $Z$: the quotient by $\mci^2$ is what makes an $\OO_X$-module into an $\OO_Z$-module, and geometrically it is the first-order data of how $Z$ sits inside $X$, the equations modulo their squares.
Local freeness of it is a smoothness statement and is what makes the determinant argument legal; without it the conormal sequence is only right exact and there is no adjunction.

The divisor form is the working tool.
For a degree-$d$ plane curve $C \subseteq \PP^2$, $\omega_{\PP^2} = \OO(-3)$ and $\OO(C) = \OO(d)$, so $\omega_C = \OO_C(d-3)$, which has degree $d(d-3)$ and gives $g = \binom{d-1}{2}$ by $\deg \omega_C = 2g-2$.
That derivation is the standard follow-up to any question about differentials, and the examiner is usually waiting for it.
:::
