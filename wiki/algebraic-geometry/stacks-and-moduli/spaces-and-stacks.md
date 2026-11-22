---
title: Hilbert schemes, algebraic spaces and stacks
order: 2
topics:
- Hilbert Schemes
- Algebraic Spaces
- Algebraic Stacks
---

# Hilbert schemes, algebraic spaces and stacks

A moduli problem is a functor of points, and the first question about it is whether a scheme represents it ([[PR-SCHFOP]]).
When none does, representability is weakened in three steps — a scheme, then an algebraic space, then a stack — and each step keeps more of the functor's data: a scheme is a sheaf on the Zariski site represented by an object of the category, an algebraic space is an étale sheaf with an étale atlas from a scheme, and a stack is a category fibred in groupoids in which the automorphisms of the objects are part of the structure ([[D-ALGSPACE]], [[D-ALGSTACK]]).
Two examples mark the endpoints: the Hilbert functor is represented by a scheme, and the moduli of curves of genus $g\ge2$ is represented only by a stack, whose coarse space $\mathcal M_g$ forgets the automorphisms ([[D-HILBSCHEME]], [[D-CRVMOD]]).

## The Hilbert functor

[[D-HILBSCHEME]]

For a noetherian scheme $S$, a projective morphism $X\to S$ with a relatively very ample $\OO_X(1)$, and a polynomial $P\in\QQ[m]$, the Hilbert functor sends a locally noetherian $S$-scheme $T$ to the closed subschemes $Z\subseteq X\times_ST$ flat over $T$ whose fibres have Hilbert polynomial $P$ ([[D-HILBSCHEME]]).
Flatness is what makes the polynomial a condition rather than a hope: for an integral noetherian base, a coherent sheaf on $\PP^n_T$ is flat over $T$ exactly when the Hilbert polynomial of every fibre is the same [@Har77, Theorem III.9.9] ([[T-COHFLATCHI]]).
Representability is a theorem with hypotheses of its own, in the form the Stacks Project proves: for a morphism $f\colon X\to B$ of algebraic spaces which is of finite presentation and separated, $\operatorname{Hilb}_{X/B}$ is an algebraic space, locally of finite presentation over $B$ (Stacks Project, Proposition 99.9.4, tag 0D01), and a representing object carries a universal family, the image of the identity under the Yoneda bijection ([[D-HILBSCHEME]]).
In the classical situation of the definition — $S$ noetherian, $X\to S$ projective with a relatively very ample $\OO_X(1)$ — the refinement is Grothendieck's theorem: each $\operatorname{Hilb}^P_{X/S}$ is represented by a projective $S$-scheme, the Hilbert scheme, and $\operatorname{Hilb}_{X/S}$ by the disjoint union over $P$ ([[D-HILBSCHEME]]).

The two calculations to keep are the point case and the hypersurface case over $\PP^n_k$: the polynomial $P=1$ gives $\operatorname{Hilb}^1(\PP^n_k)\cong\PP^n_k$, and the Hilbert polynomial of a degree-$d$ hypersurface gives $\operatorname{Hilb}^P(\PP^n_k)\cong\PP(H^0(\PP^n_k,\OO(d)))$, so that the parameter space of hypersurfaces of degree $d$ is the projective space of degree-$d$ forms ([[D-HILBSCHEME]]).
In both cases the universal family is the tautological subscheme, and representability is the statement that every flat family of such subschemes is its pullback along a unique morphism.

## Coarse and fine moduli

[[D-CRVMOD]]

Let $\mathcal F_g(T)$ be the isomorphism classes of flat families of smooth projective curves of genus $g$ over $T$.
A coarse moduli space is a variety $M_g$ with a natural transformation $\mathcal F_g\to h_{M_g}$ that is a bijection on geometric points and is universal among such transformations, while a fine moduli space is one that represents $\mathcal F_g$, equivalently one carrying a universal family ([[D-CRVMOD]]).
The difference is exactly the automorphisms: an elliptic curve has the automorphism $-1$, and the family $ty^2=x^3-x$ over $\Spec k[t,t^{-1}]$ has every geometric fibre isomorphic to $y^2=x^3-x$ without being isomorphic to the constant family, since the isomorphism $y\mapsto\sqrt ty$ is defined only after adjoining $\sqrt t$ ([[D-CRVMOD]], [[T-CRVJINV]]).
A fine moduli space would make that family the pullback of the universal one along a constant map, so no fine moduli space exists.

The coarse space nevertheless exists and is well behaved: for $g\ge2$ it is irreducible and quasiprojective of dimension $3g-3$, and the dimension is visible infinitesimally, since first-order deformations of a curve are $H^1(C,T_C)$ and Serre duality identifies that with the dual of $H^0(C,\omega_C^{\tensor2})$, of dimension $3g-3$ ([[T-CRVMG]], [[D-CRVMOD]]).
So the moduli problem has a good answer at the level of spaces and a defective one at the level of representing objects, which is exactly the gap that algebraic spaces and stacks are designed to fill.

## Algebraic spaces

[[D-ALGSPACE]]

An étale equivalence relation on an $S$-scheme $U$ is a subscheme $R\subseteq U\times_SU$ that is an equivalence relation on $T$-valued points with both projections étale, and its quotient is the étale sheafification of $T\mapsto U(T)/R(T)$ ([[D-ALGSPACE]]).
An algebraic space is an étale sheaf whose diagonal is representable by schemes and which admits a scheme $U$ with $U\to X$ étale and surjective, an étale atlas; the two definitions agree, since $U\times_XU$ is then an étale equivalence relation with quotient $X$ ([[D-ALGSPACE]]).

Every scheme is an algebraic space with the identity as atlas, and if a finite group $G$ acts freely on a quasiprojective $S$-scheme $U$ then $U/G$ is an algebraic space with atlas $U$ ([[D-ALGSPACE]]).
The point of the notion is that the quotient exists as a geometric object with étale-local properties even when it is not a scheme: properties are checked on the atlas, and the diagonal condition is what allows a morphism from a scheme to be base-changed.
The definition is a genuine weakening of representability: the atlas is required only to be étale and surjective, and the quotient of a scheme by an étale equivalence relation is an algebraic space, with $U\to U/R$ étale and surjective (Stacks Project, Theorem 65.10.5, tag 02WW) ([[D-ALGSPACE]]).

## Stacks

[[D-ALGSTACK]]

A stack over $S$ is a category $\mathcal X$ fibred in groupoids over $\Sch_{/S}$ such that the isomorphism presheaves $\operatorname{Isom}(\xi,\eta)$ are étale sheaves and every étale descent datum is effective ([[D-ALGSTACK]]).
An algebraic stack is a stack whose diagonal is representable by algebraic spaces and which admits a representable, smooth, surjective morphism $U\to\mathcal X$ from a scheme; it is Deligne--Mumford when some such atlas is étale ([[D-ALGSTACK]]).
Smoothness of $\mathcal X$ over $S$ means the composite $U\to S$ is smooth for one — hence every — smooth atlas, and open, closed, and locally closed substacks are defined by requiring every base change $\mathcal Z\times_{\mathcal X}T\to T$ to be the corresponding kind of immersion ([[D-ALGSTACK]]).

The reason to pay the price of working with categories rather than functors is that the automorphisms are then part of the data.
For each scheme $T$ and object $\xi$ over $T$, the base change $\theset{\xi}\times_{\mathcal X}T$ is an algebraic space whose points over $t$ record $\Aut(\xi_t)$, so a stack can distinguish the hyperelliptic curves, which have an involution, from the general curve, which has none, while the coarse space sees only the isomorphism class ([[D-ALGSTACK]], [[D-CRVMOD]]).
The moduli of curves of genus $g\ge2$ is therefore a Deligne--Mumford stack whose coarse space is $\mathcal M_g$, and the two agree only after passing to isomorphism classes ([[D-ALGSTACK]], [[T-CRVMG]]).

## The three levels

The inclusions run strictly: schemes are algebraic spaces, and algebraic spaces are stacks whose objects have no nontrivial automorphisms ([[D-ALGSPACE]], [[D-ALGSTACK]]).
Which level a moduli problem needs is a question about the problem: a fine moduli space exists when the functor is representable, an algebraic space answers the problem when the quotient by a free action exists only étale-locally, and a stack is required as soon as the objects being classified have automorphisms that must be remembered.
The Hilbert functor sits at the first level, the free quotient at the second, and the moduli of curves at the third ([[D-HILBSCHEME]], [[D-ALGSPACE]], [[D-ALGSTACK]], [[D-CRVMOD]]).
