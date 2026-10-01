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
Let $\mathcal F_g(T)$ be the set of isomorphism classes of flat families of smooth projective curves of genus $g$ over $T$.
A variety $M_g$ is a \dfn{coarse moduli space} for $\mathcal F_g$ if there is a natural transformation
$$
\eta\colon \mathcal F_g \longrightarrow h_{M_g},
\qquad
h_{M_g}(T)=\Hom(T,M_g),
$$
such that:

1. for every algebraically closed field extension $K$, the map
$$
\eta_K\colon \mathcal F_g(\Spec K)\longrightarrow M_g(K)
$$
is a bijection, and

2. for every scheme $N$ and every natural transformation $\phi\colon\mathcal F_g\to h_N$, there is a unique morphism $u\colon M_g\to N$ such that $\phi=h_u\circ\eta$.
:::

::: {.definition title="Fine moduli space"}
$M_g$ is a \dfn{fine moduli space} when it represents $\mathcal F_g$: there is a natural bijection
$$
\operatorname{Hom}(T, M_g) \longleftrightarrow \ts{\text{families over } T}/{\cong}
$$
natural in $T$.
Equivalently $M_g$ carries a **universal family** $\mathcal{U} \to M_g$ from which every family is pulled back along its own classifying map, in exactly one way.
:::

::: {.remark}
For a coarse moduli space, families induce classifying maps; for a fine moduli space, this correspondence is bijective and natural in the base.
Condition (2) alone does not imply that every map to $M_g$ comes from a family or that two families with the same classifying map are isomorphic.
Take a family to its classifying map and the map back to a family and the round trip must return what you started with — that is representability, and it fails.

Automorphisms are the obstruction, and the mechanism is twisting.
Families over $T$ with all fibres isomorphic to a fixed curve $C$ are classified by $H^1(T, \Aut C)$, so as soon as $\Aut C \neq 1$ there are nontrivial such families.
The classifying map of any one of them is constant, being the point $[C]$; a universal family would pull back along a constant map to a constant family, so no universal family exists.

The standard witness is a quadratic twist.
Over $T = \AA^1 \smz$ with coordinate $t$, put
$$
\mathcal{E}_t : y^2 = x^3 + a t^2 x + b t^3 .
$$
Over $k = \kbar$ the substitution $x = t u$, $y = t^{3/2} v$ identifies each fibre with the fixed curve $v^2 = u^3 + au + b$, so every fibre is isomorphic and the classifying map is constant.
The family is not $E \times T$: its class in $H^1(T, \mu_2)$ is the squaring cover of $\mathbf{G}_m$, which is nontrivial.
The $\mu_2$ here is $\pm 1 \subseteq \Aut(E, p_0)$, so the example is powered by exactly the automorphism that the moduli problem forgets.

The same failure persists for every $g \geq 2$ even though a general curve of genus $g \geq 3$ has no nontrivial automorphisms: the hyperelliptic locus is nonempty in every genus and every curve on it carries the hyperelliptic involution.
It is enough that *some* curve has an automorphism, since the twisted family over that one point's worth of moduli already breaks representability.
The repair is not a better variety but a different kind of object — the stack quotient that remembers $\Aut C$ at the point $[C]$ — and $M_g$ is its coarse space.
:::
