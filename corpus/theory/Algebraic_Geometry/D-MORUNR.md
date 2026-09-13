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
$f : X \to Y$ locally of finite type is **unramified** if for every $x \in X$ with $y = f(x)$,
\[
f^\sharp(\mfm_y) \OO_{X,x} = \mfm_x
\qquad\text{and}\qquad
\kappa(x)/\kappa(y) \text{ is a finite separable extension.}
\]
Equivalently, $\Omega_{X/Y} = 0$; equivalently, $\Delta_{X/Y}$ is an open immersion.
:::

::: {.remark}
The three formulations are three different tools and it is worth being able to move between them.
The first says the fibres are reduced and the maximal ideal is not squashed; the second is the computable one; the third is why unramified morphisms behave like local isomorphisms of topological spaces, since an open diagonal is the formal version of "locally injective".

For a dominant map of smooth curves $f : X \to Y$ the local picture is $f^\sharp(\mfm_{f(p)}) \OO_{X,p} = \mfm_p^{e_p}$, and $f$ is unramified exactly when every ramification index $e_p$ equals $1$.
$t \mapsto t^n$ on $\AA^1$ is ramified at the origin, and in characteristic $p$ dividing $n$ it is ramified in the worse, inseparable way that the separability clause is there to exclude.
This is the same $e_p$ that appears in Riemann--Hurwitz, so the definition is not a formality: it is the condition that makes the genus formula have no correction term.
:::
