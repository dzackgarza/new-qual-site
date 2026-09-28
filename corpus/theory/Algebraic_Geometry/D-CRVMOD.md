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
- What conditions define a coarse moduli space?
- What does a fine moduli space have that a coarse one does not?
- What obstructs the existence of a fine moduli space of curves?
- Exhibit a nonconstant family all of whose fibres are isomorphic.
---

::: {.definition title="Coarse moduli space"}
Let $k$ be an algebraically closed field.
A variety $M_g$ over $k$ is a \dfn{coarse moduli space} for curves of genus $g$ when:

1. the closed points of $M_g$ are in bijection with isomorphism classes of smooth projective curves of genus $g$ over $k$;

2. every flat family $\mathcal{X} \to T$ whose fibres are such curves induces a morphism $h\colon T \to M_g$ with $h(t)$ the class of the fibre $\mathcal{X}_t$, compatibly with pullback of families along morphisms $T'\to T$; and

3. for every scheme $N$ with an assignment of morphisms $T\to N$ to families as in (2), compatible with pullback, there is a unique morphism $M_g\to N$ through which that assignment factors.
:::

::: {.definition title="Fine moduli space"}
$M_g$ is a \dfn{fine moduli space} when it represents the functor sending $T$ to the set of flat families over $T$ up to isomorphism: the classifying maps of (2) give a bijection
$$
\operatorname{Hom}(T, M_g) \longleftrightarrow \ts{\text{families over } T}/{\cong}
$$
natural in $T$.
Equivalently $M_g$ carries a \dfn{universal family} $\mathcal{U} \to M_g$ such that every family $\mathcal{X}\to T$ is isomorphic to the pullback of $\mathcal{U}$ along a unique morphism $T\to M_g$.
:::

::: {.proposition title="Automorphisms and fine moduli"}
Let $C$ be a smooth projective curve of genus $g$ over $k$, and let $T$ be a connected scheme over $k$.
Families over $T$ that become isomorphic to $C\times T$ étale-locally on $T$ are classified up to isomorphism by $H^1_{\mathrm{et}}(T,\Aut C)$.
The classifying map of each such family is the constant map to the point $[C]$.
Hence, if some such family is not isomorphic to $C\times T$, then two non-isomorphic families have the same classifying map, and no fine moduli space exists.
:::

::: {.example title="A quadratic twist"}
Let $\operatorname{char}k\ne2,3$, and let $E\colon v^2=u^3+au+b$ be an elliptic curve with origin $p_0$ at infinity.
Over $T = \AA^1 \smz$ with coordinate $t$, put
$$
\mathcal{E}_t : y^2 = x^3 + a t^2 x + b t^3 .
$$
Over a square root $s$ of $t$, the substitution $x = s^2 u$, $y = s^3 v$ identifies $\mathcal E_t$ with $E$, so every fibre is isomorphic to $E$ and the classifying map is constant.
The family is the twist of $E\times T$ by the $\mu_2$-torsor $s\mapsto s^2=t$ over $\GG_m$, acting through $-1\in\Aut(E,p_0)$.
That torsor is nontrivial, since $t$ has no square root in $k[t,t^{-1}]$, so $\mathcal E\to T$ is not isomorphic to $E\times T$.
:::

::: {.remark}
Every genus $g \geq 2$ has hyperelliptic curves, and each carries the hyperelliptic involution $\iota$.
For $\operatorname{char}k\ne2$, the twist of $C\times\GG_m$ by the squaring $\mu_2$-torsor acting through $\iota$ is not isomorphic to $C\times\GG_m$.
So there is no fine moduli space of curves of genus $g\ge2$, although a general curve of genus $g \geq 3$ has trivial automorphism group.

The moduli stack $\mathcal{M}_g$ ([[D-ALGSTACK]], [[T-MGSMOOTH]]) has as objects over $T$ the families over $T$ and as morphisms the isomorphisms of families; the automorphism group of the point $[C]$ of $\mathcal M_g$ is $\Aut C$, and $M_g$ is the coarse moduli space of $\mathcal{M}_g$.
:::
