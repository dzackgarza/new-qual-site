---
schema: qual/card@1
id: D-MORUNR
kind: definition
title: Unramified morphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Unramified Morphisms
  - Ramification
  - Differentials
relations:
- kind: related-to
  target: D-MORFT
review: draft
prompts:
- What is an unramified morphism?
- State the characterisation by differentials.
- What does unramified mean for a map of curves?
---

::: {.definition title="Unramified"}
$f : X \to Y$ locally of finite type is \dfn{unramified} if for every $x \in X$ with $y = f(x)$,
\[
f^\sharp(\mfm_y) \OO_{X,x} = \mfm_x
\qquad\text{and}\qquad
\kappa(x)/\kappa(y) \text{ is a finite separable extension.}
\]
Equivalently, $\Omega_{X/Y} = 0$; equivalently, $\Delta_{X/Y}$ is an open immersion.
:::

::: {.remark}
The three formulations emphasize different aspects of the same condition.
The first says the fibres are reduced and the maximal ideal is not squashed; the second is the computable one; the third is why unramified morphisms behave like local isomorphisms of topological spaces, since an open diagonal is the formal version of "locally injective".

For a nonconstant map of smooth integral curves over an algebraically closed field, the local picture at a closed point is $f^\sharp(\mfm_{f(p)}) \OO_{X,p} = \mfm_p^{e_p}$, and $f$ is unramified exactly when every ramification index $e_p$ equals $1$.
For $n>1$, $t \mapsto t^n$ on $\AA^1$ is ramified at the origin. In characteristic $p$ dividing $n$, its differential vanishes everywhere and the induced function-field extension is inseparable.
For a finite separable map of smooth projective curves, unramifiedness makes the ramification term in Riemann--Hurwitz vanish.
:::
