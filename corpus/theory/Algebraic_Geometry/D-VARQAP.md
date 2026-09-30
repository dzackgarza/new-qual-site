---
schema: qual/card@1
id: D-VARQAP
kind: definition
title: Affine, quasi-affine, projective, and quasi-projective varieties; the affine charts of $\PP^n$
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
- If $X$ is projective and $F$ is homogeneous of degree $d$, show that $\theset{x \in X \st F(x) \neq 0}$ is an open affine subset of $X$.
---

::: {.definition title="Affine, quasi-affine, projective, and quasi-projective varieties"}
An \dfn{affine} variety is an irreducible closed subset of $\AA^n$; a \dfn{quasi-affine} variety is an open subset of one.
A \dfn{projective} variety is an irreducible closed subset of $\PP^n$; a \dfn{quasi-projective} variety is an open subset of one.
Affine, quasi-affine, and projective varieties are quasi-projective.
:::

::: {.proposition title="Standard charts"}
$U_i \definedas \theset{x_i \neq 0} \subseteq \PP^n$ is open, the map
$$
\phi_i: U_i \to \AA^n, \qquad \thevector{x_0 : \cdots : x_n} \mapsto \qty{ x_0/x_i, \ldots, \widehat{x_i/x_i}, \ldots, x_n/x_i }
$$
is an isomorphism of varieties, and $\PP^n = \union_{i=0}^n U_i$.
:::

::: {.remark}
For $Y \subseteq \PP^n$ closed, $\phi_i(Y\cap U_i)$ is the affine variety cut out by the dehomogenizations $f(x_0,\ldots,1,\ldots,x_n)$, with $1$ in position $i$, for $f \in I(Y)$.
For $Z\subseteq\AA^n\cong U_0$ closed, the projective closure of $Z$ is cut out by the homogenizations of all elements of $I(Z)$.

Homogenizing only a generating set can give a larger set: for the twisted cubic $Z=V(y-x^2,z-x^3)$, the homogenizations $yw-x^2$ and $zw^2-x^3$ both vanish on the line $V(w,x)$ at infinity, which is not contained in the projective closure of $Z$.
:::
