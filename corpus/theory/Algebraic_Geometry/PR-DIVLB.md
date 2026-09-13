---
schema: qual/card@1
id: PR-DIVLB
kind: proposition
title: Cartier divisors, invertible sheaves, and the Picard group
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cartier Divisors
  - Picard Group
  - Invertible Sheaves
relations:
- kind: uses
  target: D-DIVOD
- kind: uses
  target: D-5PQ5W
review: draft
prompts:
- What is the correspondence between Cartier divisors and invertible sheaves?
- Why is $\Pic(X) = H^1(X, \OO_X\units)$?
- Which line bundles come from divisors?
---

::: {.proposition}
$D \mapsto \OO_X(D)$ is an injection $\CaCl(X) \injects \Pic(X)$, and it is a bijection onto the invertible subsheaves of $\mck$.
When $X$ is integral every invertible sheaf is such a subsheaf, so $\CaCl(X) \cong \Pic(X)$.
:::

::: {.proposition}
$\Pic(X) \cong H^1(X, \OO_X\units)$, and the sequence
\[
0 \to \OO_X\units \to \mck\units \to \mck\units/\OO_X\units \to 0
\]
has cohomology sequence $\mck(X)\units \to \Div_{\mathrm{Ca}}(X) \to \Pic(X) \to H^1(X, \mck\units)$.
:::

::: {.remark}
Both halves are the same observation: gluing data for a line bundle is a cocycle $g_{ij} \in \OO\units(U_{ij})$, and Cartier data $f_i$ produces the cocycle $g_{ij} = f_i/f_j$.
Saying "a Cartier divisor is a line bundle together with a choice of rational section" is the cleanest one-line answer, and it explains the failure of surjectivity for non-integral $X$: a line bundle with no rational section is not a divisor.

Combined with the injection $\CaCl \injects \Cl$, the chain to recite is
\[
\Pic(X) \cong \CaCl(X) \injects \Cl(X) ,
\]
an isomorphism throughout when $X$ is locally factorial.
The gap at the second arrow is measured by the singularities.
:::
