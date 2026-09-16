---
schema: qual/card@1
id: D-VARQAP
kind: definition
title: The four classes of variety, and the affine charts of $\PP^n$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Varieties
  - Projective Varieties
  - Affine Charts
relations:
- kind: uses
  target: D-CP2MH
review: draft
prompts:
- What is a quasi-affine variety? A quasi-projective variety?
- How is $\PP^n$ covered by affine spaces?
- Derive the rational parametrization $\AA^1 \to V(a^2 + b^2 - 1)$ and its inverse, with their domains, and projectivize both maps.
- If $X$ is projective and $F$ is homogeneous of degree $d$, show that $\ts{x \in X \st F(x) \neq 0}$ is an open affine subset of $X$.
---

::: {.definition title="The four classes"}
An \dfn{affine} variety is an irreducible closed subset of $\AA^n$; a **quasi-affine** variety is an open subset of one.
A **projective** variety is an irreducible closed subset of $\PP^n$; a **quasi-projective** variety is an open subset of one.
Quasi-projective contains all four.
:::

::: {.proposition title="Standard charts"}
$U_i \da \ts{x_i \neq 0} \subseteq \PP^n$ is open, the map
\[
\phi_i: U_i \to \AA^n, \qquad \tv{x_0 : \cdots : x_n} \mapsto \qty{ x_0/x_i, \ldots, \widehat{x_i/x_i}, \ldots, x_n/x_i }
\]
is an isomorphism of varieties, and $\PP^n = \union_{i=0}^n U_i$.
:::

::: {.remark}
The charts are what make every local question on a projective variety an affine question, and they are the reason dehomogenising and homogenising is a computation rather than a construction: $Y \subseteq \PP^n$ meets $U_i$ in the affine variety cut out by $\restrictionof{f}{x_i = 1}$ for $f \in I(Y)$, and the projective closure of an affine $Z$ is cut out by the homogenisations of *all* of $I(Z)$.

The usual trap is homogenising a generating set rather than the whole ideal: for the twisted cubic the homogenisations of $y - x^2, z - x^3$ do not generate $I(Y)$, and the projective closure acquires a line at infinity that is not on the curve.
:::
