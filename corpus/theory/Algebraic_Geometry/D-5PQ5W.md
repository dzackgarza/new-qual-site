---
schema: qual/card@1
id: D-5PQ5W
kind: definition
title: Weil and Cartier divisors, and when they agree
classification:
  areas:
  - algebraic-geometry
  topics:
  - Divisors
  - Cartier Divisors
  - Class Groups
relations:
- kind: uses
  target: D-QJ5M9
review: draft
prompts:
- Describe Weil divisors and Cartier divisors on a curve.
- How do you get a Weil divisor from $f \in K^*$?
- When do the two notions agree?
---

::: {.definition title="Weil"}
On a Noetherian integral separated scheme regular in codimension one, a **Weil divisor** is a finite formal $\ZZ$-combination of codimension-one integral closed subschemes.
For $f \in K(X)^*$,
\[
\div(f) = \sum_{\operatorname{codim} Y = 1} v_Y(f) \cdot Y ,
\]
where $v_Y$ is the valuation of the discrete valuation ring $\OO_{X,\eta_Y}$.
The quotient by these **principal** divisors is the class group $\Cl(X)$.
:::

::: {.definition title="Cartier"}
A **Cartier divisor** is a global section of $\mathcal{K}^*/\OO_X^*$: a collection of nonzero rational functions $f_i$ on an open cover whose ratios $f_i/f_j$ are units on overlaps.
Modulo global rational functions this is $\Pic(X)$.
:::

::: {.proposition}
There is an injection $\operatorname{CaCl}(X) \injects \Cl(X)$, an isomorphism when $X$ is locally factorial — in particular when $X$ is regular.
:::

::: {.remark}
The valuation is the whole content of "how do you get a Weil divisor from $f \in K^*$": regularity in codimension one makes each local ring at a codimension-one point a discrete valuation ring, and $v_Y(f)$ is the order of vanishing there.
On a smooth curve every local ring is such, so Weil and Cartier agree and $\Cl = \Pic$.

The gap is exactly non-factoriality, and the standard witness is the quadric cone $V(xy - z^2)$: the ruling line $V(x,z)$ is a Weil divisor that is not Cartier, and $\Cl = \ZZ/2$ while $\Pic = 0$.
A Weil divisor is a subvariety; a Cartier divisor is a local equation.
Where the local ring is not factorial, a subvariety need not have one.
:::
