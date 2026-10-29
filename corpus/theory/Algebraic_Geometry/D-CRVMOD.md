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
\operatorname{Hom}(T, M_g) \longleftrightarrow \theset{\text{families over } T}/{\cong}
$$
natural in $T$.
Equivalently $M_g$ carries a \dfn{universal family} $\mathcal{U}\to M_g$ whose pullback along each classifying morphism recovers the corresponding family, compatibly with base change.
:::

::: {.remark}
For a coarse moduli space, families induce classifying maps; for a fine moduli space, this correspondence is bijective and natural in the base.
Condition (2) alone does not imply that every map to $M_g$ comes from a family or that two families with the same classifying map are isomorphic.
Representability requires the natural transformation to be an isomorphism of functors, not merely universal among maps from the moduli functor to representable functors.

Nontrivial automorphisms produce an obstruction by twisting.
If $C/k$ has finite constant automorphism group $G$ and a family over $T$ is étale-locally isomorphic to $C\times T$, its forms are classified by the pointed set
$$
H^1_{\acute{e}tale}(T,G).
$$
A nontrivial class gives an isotrivial but nonconstant family whose coarse classifying map is the constant map to $[C]$. Such a family cannot be obtained by pulling a single universal family back along that constant map.

For a concrete witness, let $k$ be algebraically closed of characteristic different from $2$, fix an elliptic curve
$$
E\colon v^2=u^3+au+b,
$$
and put $T=\GG_{m,k}$ with coordinate $t$. Define
$$
\mathcal{E}_t : y^2 = x^3 + a t^2 x + b t^3 .
$$
After the étale cover $T'\to T$ given by $s^2=t$, the substitution
$$
x=s^2u,\qquad y=s^3v
$$
identifies $\mathcal E_{T'}$ with $E\times T'$. Thus every geometric fibre is isomorphic to $E$, while the family over $T$ is the nontrivial quadratic twist corresponding to the class of the cover $s^2=t$ in $H^1_{\acute{e}tale}(T,\mu_2)$.
The $\mu_2$ here is $\pm 1 \subseteq \Aut(E, p_0)$, where $p_0$ is the point at infinity of $E$, so the example is powered by exactly the automorphism that the moduli problem forgets.

The same failure persists for every $g \geq 2$ even though a general curve of genus $g \geq 3$ has no nontrivial automorphisms: the hyperelliptic locus is nonempty in every genus and every curve on it carries the hyperelliptic involution.
It is enough that *some* curve has an automorphism, since the twisted family over that one point's worth of moduli already breaks representability.
The repair is not a better variety but a different kind of object — the stack quotient that remembers $\Aut C$ at the point $[C]$ — and $M_g$ is its coarse space.
:::
