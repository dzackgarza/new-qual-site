---
schema: qual/card@1
id: D-CRVMOD
kind: definition
title: Coarse versus fine moduli spaces
classification:
  areas:
  - algebraic-geometry
  topics:
  - Moduli
  - Families of Curves
  - Automorphisms
relations:
- kind: related-to
  target: T-CRVJINV
review: draft
prompts:
- What are the two conditions defining a coarse moduli space?
- What does a fine moduli space have that a coarse one does not?
- What obstructs the existence of a fine moduli space of curves?
- Exhibit a nonconstant family all of whose fibres are isomorphic.
---

::: {.definition title="Coarse moduli space"}
A variety $M_g$ is a **coarse moduli space** for curves of genus $g$ when:

1. the closed points of $M_g$ are in bijection with isomorphism classes of smooth projective curves of genus $g$, and
2. every flat family $\mathcal{X} \to T$ whose fibres are such curves induces a morphism $h\colon T \to M_g$ with $h(t)$ the class of the fibre $\mathcal{X}_t$.
:::

::: {.definition title="Fine moduli space"}
$M_g$ is a **fine moduli space** when it represents the functor sending $T$ to the set of flat families over $T$ up to isomorphism: the assignment of (2) is a bijection
\[
\operatorname{Hom}(T, M_g) \longleftrightarrow \ts{\text{families over } T}/{\cong}
\]
natural in $T$.
Equivalently $M_g$ carries a **universal family** $\mathcal{U} \to M_g$ from which every family is pulled back along its own classifying map, in exactly one way.
:::

::: {.remark}
Coarse asks only that families produce maps; fine asks that maps *be* families, and the gap between the two is where all the content sits.
Condition (2) alone is cheap: it does not say that a map to $M_g$ comes from anything, nor that two families inducing the same map are isomorphic.
Take a family to its classifying map and the map back to a family and the round trip must return what you started with — that is representability, and it fails.

Automorphisms are the obstruction, and the mechanism is twisting.
Families over $T$ with all fibres isomorphic to a fixed curve $C$ are classified by $H^1(T, \Aut C)$, so as soon as $\Aut C \neq 1$ there are nontrivial such families.
The classifying map of any one of them is constant, being the point $[C]$; a universal family would pull back along a constant map to a constant family, so no universal family exists.

The standard witness is a quadratic twist.
Over $T = \AA^1 \smz$ with coordinate $t$, put
\[
\mathcal{E}_t : y^2 = x^3 + a t^2 x + b t^3 .
\]
Over $k = \kbar$ the substitution $x = t u$, $y = t^{3/2} v$ identifies each fibre with the fixed curve $v^2 = u^3 + au + b$, so every fibre is isomorphic and the classifying map is constant.
The family is not $E \times T$: its class in $H^1(T, \mu_2)$ is the squaring cover of $\mathbf{G}_m$, which is nontrivial.
The $\mu_2$ here is $\pm 1 \subseteq \Aut(E, p_0)$, so the example is powered by exactly the automorphism that the moduli problem forgets.

The same failure persists for every $g \geq 2$ even though a general curve of genus $g \geq 3$ has no nontrivial automorphisms: the hyperelliptic locus is nonempty in every genus and every curve on it carries the hyperelliptic involution.
It is enough that *some* curve has an automorphism, since the twisted family over that one point's worth of moduli already breaks representability.
The repair is not a better variety but a different kind of object — the stack quotient that remembers $\Aut C$ at the point $[C]$ — and $M_g$ is its coarse space.
:::
