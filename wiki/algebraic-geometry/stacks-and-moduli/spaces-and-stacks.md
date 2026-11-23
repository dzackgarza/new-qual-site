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
Recall that [[D-ALGSPACE]] presents algebraic spaces by étale atlases from schemes, and [[D-ALGSTACK]] retains the automorphisms of the objects that a coarse moduli space forgets.
The Hilbert functor is represented by a scheme, while the moduli of curves of genus $g\ge2$ is represented by a Deligne--Mumford stack whose geometric points record isomorphism classes of curves ([[D-HILBSCHEME]], [[D-CRVMOD]], [[D-ALGSTACK]]).

## The Hilbert functor

[[D-HILBSCHEME]]

Flatness makes constancy of the Hilbert polynomial a flatness criterion: for an integral noetherian base, a coherent sheaf on $\PP^n_T$ is flat over $T$ exactly when the Hilbert polynomial of every fibre is the same [@Har77, Theorem III.9.9] ([[T-COHFLATCHI]]).
Grothendieck's theorem represents $\operatorname{Hilb}^P_{X/S}$ by a projective $S$-scheme and $\operatorname{Hilb}_{X/S}$ by the disjoint union over $P$ ([[D-HILBSCHEME]]).
The representing object carries a universal family: a closed subscheme of $X\times_S\operatorname{Hilb}^P(X/S)$, flat over the Hilbert scheme, whose pullback along $T\to\operatorname{Hilb}^P(X/S)$ is the family classified by that morphism ([[D-HILBSCHEME]]).

The Stacks theorem concerns a different functor: for a morphism $f\colon X\to B$ of algebraic spaces over a scheme $S$, of finite presentation and separated, the functor $T\mapsto\theset{\text{closed subspaces }Z\subseteq X\times_BT\st Z\to T\text{ flat, proper and of finite presentation}}$ is an algebraic space locally of finite presentation over $B$ (Stacks Project, Situation 99.9.1, tag 0CZY, and Proposition 99.9.4, tag 0D01).
This functor has no Hilbert polynomial or relatively ample sheaf among its data. With $X\to S$ projective and $\OO_X(1)$ fixed, $\operatorname{Hilb}^P_{X/S}$ is the subfunctor on which the fibres have polynomial $P$; Grothendieck's theorem represents this subfunctor by a projective scheme, a conclusion not supplied by Proposition 99.9.4 alone ([[D-HILBSCHEME]]).

## Coarse and fine moduli

[[D-CRVMOD]]

::: {.example title="An isotrivial but nonconstant family of elliptic curves"}
Let $k$ be an algebraically closed field with $\operatorname{char}k\ne2$, and put $T=\GG_{m,k}=\Spec k[t,t^{-1}]$.
The family $ty^2=x^3-x$ over $T$ becomes isomorphic to the constant family $Y^2=x^3-x$ after the étale cover $s^2=t$ by the substitution $Y=sy$, so every geometric fibre has the same $j$-invariant.
It is the quadratic twist by the class of $t$ in $H^1_{\mathrm{et}}(T,\mu_2)$, which is nontrivial because $t$ is not a square in $k(t)$, and therefore is not isomorphic over $T$ to the constant family ([[D-CRVMOD]], [[T-CRVJINV]]).
Its classifying map to a coarse moduli space is constant, so if a universal family represented the moduli functor, this nonconstant family would be a pullback of the universal family along a constant map; hence no fine moduli space represents the functor of [[D-CRVMOD]].
:::

For $g\ge2$ over an algebraically closed field, the coarse moduli space of smooth projective curves is irreducible and quasiprojective of dimension $3g-3$.
Infinitesimally, first-order deformations of a curve are $H^1(C,T_C)$, and Serre duality identifies that with the dual of $H^0(C,\omega_C^{\tensor2})$, of dimension $3g-3$ ([[T-CRVMG]], [[D-CRVMOD]]).

## Algebraic spaces

[[D-ALGSPACE]]

Recall that [[D-ALGSPACE]] defines an étale equivalence relation on $U$ by a monomorphism $(s,t)\colon R\to U\times_SU$ giving an equivalence relation on $T$-valued points with both projections étale, and defines $U/R$ as the étale sheafification of $T\mapsto U(T)/R(T)$.
The defining conditions for an algebraic space are representability of its diagonal and the existence of an étale atlas $U\to X$ from a scheme. If $U\to X$ is an étale atlas, then $U\times_XU$ is an étale equivalence relation with quotient $X$ ([[D-ALGSPACE]]).

Every scheme is an algebraic space with the identity as atlas, and if a finite group $G$ acts freely on a quasiprojective $S$-scheme $U$ then $U/G$ is an algebraic space with atlas $U$ ([[D-ALGSPACE]]).
Properties that are étale-local are checked on an atlas, and the diagonal condition makes every base change of $U\to X$ along a morphism from a scheme again a scheme ([[D-ALGSPACE]]).
Every quotient of a scheme by an étale equivalence relation is an algebraic space, with $U\to U/R$ étale and surjective (Stacks Project, Theorem 65.10.5, tag 02WW) ([[D-ALGSPACE]]).

## Stacks

[[D-ALGSTACK]]

Recall from [[D-ALGSTACK]] that a stack over $S$ is a category $\mathcal X$ fibred in groupoids over $\Sch_{/S}$ whose isomorphism presheaves are étale sheaves and whose étale descent data are effective.
An algebraic stack additionally has a representable diagonal and a representable, smooth, surjective atlas $U\to\mathcal X$ from a scheme; it is Deligne--Mumford when an atlas can be chosen étale ([[D-ALGSTACK]]).
Smoothness of $\mathcal X$ over $S$ is smoothness of $U\to S$ for one, equivalently every, smooth atlas. Open, closed, and locally closed substacks are detected by the corresponding base changes $\mathcal Z\times_{\mathcal X}T\to T$ ([[D-ALGSTACK]]).

The objects of a stack retain their automorphisms. For each scheme $T$ and object $\xi$ over $T$, the base change $\theset{\xi}\times_{\mathcal X}T$ is an algebraic space whose points over $t$ record $\Aut(\xi_t)$, so a stack can distinguish the hyperelliptic curves, which have an involution, from the general curve, which has none, while the coarse space sees only the isomorphism class ([[D-ALGSTACK]], [[D-CRVMOD]]).
The moduli of curves of genus $g\ge2$ is therefore a Deligne--Mumford stack whose coarse space is $\mathcal M_g$, and the two agree only after passing to isomorphism classes ([[D-ALGSTACK]], [[T-CRVMG]]).

## The three levels

The inclusions run strictly: schemes are algebraic spaces, and algebraic spaces are stacks whose objects have no nontrivial automorphisms ([[D-ALGSPACE]], [[D-ALGSTACK]]).
Which level a moduli problem needs is a question about the problem: a fine moduli space exists when the functor is representable, an algebraic space answers the problem when the quotient by a free action exists only étale-locally, and a stack is required as soon as the objects being classified have automorphisms that must be remembered.
The Hilbert functor sits at the first level, the free quotient at the second, and the moduli of curves at the third ([[D-HILBSCHEME]], [[D-ALGSPACE]], [[D-ALGSTACK]], [[D-CRVMOD]]).
