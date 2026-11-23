---
title: Subschemes and points
order: 5
topics:
- Subschemes
- Points
- Scheme-Theoretic Image
---

# Subschemes and points

Recall that a [[D-SCHSUB|closed subscheme]] of $X$ is a closed subset with a quasicoherent sheaf of ideals on it, and that a subscheme is a closed subscheme of an open subscheme ([[D-MORIMM]]); the two halves behave differently, since an open subset carries exactly one scheme structure while a closed subset carries as many as there are quasicoherent ideal sheaves cutting it out ([[D-SCHSUB]]).
That asymmetry is the source of the two constructions this chapter is about.
The reduced induced structure picks the smallest of the closed structures on a given closed set, and it is the one that ignores multiplicity.
The scheme-theoretic image of a morphism picks the closed subscheme of the target that the morphism factors through universally, and it is the one that records multiplicity; whether that image is reduced is a separate question from whether the source is, and the two are separated below.

## Open and closed subschemes

[[D-SCHSUB]]

A closed immersion is a morphism that is a homeomorphism onto a closed subset and is surjective on structure sheaves, and closed subschemes of $X$ correspond to quasicoherent ideal sheaves $\mci\subseteq\OO_X$ by $Z\mapsto\OO_X/\mci$; for $X=\Spec A$ this is the correspondence between ideals of $A$ and closed subschemes of $X$ [@Har77, Corollary II.5.10] ([[D-SCHSUB]]).
A closed immersion $i\colon Z\to X$ therefore carries an exact sequence of $\OO_X$-modules
$$
0\to\mci\to\OO_X\to i_*\OO_Z\to0 ,
$$
which tensors with a locally free sheaf to give $0\to\mcl(-D)\to\mcl\to\mcl\restrict_D\to0$ when $Z=D$ is an effective Cartier divisor [@Har77, Proposition II.6.18] ([[D-SCHSUB]]).

The map on global sections of a closed immersion need not be surjective, so a closed subscheme is not determined by its global functions: for $Z=\theset{0,\infty}\subseteq\PP^1_k$ with the reduced structure, $\OO_X(X)=k$ maps to $\OO_Z(Z)=k\times k$ as the diagonal ([[D-SCHSUB]]).
The two structures on the same closed set are the content of the next section: $V(x)$ and $V(x^2)$ in $\AA^1$ have the same support and different ideal sheaves.

## The reduced induced structure

[[D-SCHRED]]

On a closed subset $Z\subseteq X$ there is exactly one reduced closed subscheme with underlying space $Z$, obtained affinely by giving $Z$ the structure $\Spec(A/\mfa)$ with $\mfa=\bigcap_{\mfp\in Z}\mfp$ and gluing [@Har77, Example II.3.2.6] ([[D-SCHRED]]).
It is the smallest closed subscheme supported on $Z$, in the sense that every other one contains it, and it is characterized by a universal property: a morphism $T\to X$ from a reduced scheme with image in $Z$ factors uniquely through $Z^\red$ ([[D-SCHRED]]).
The universal property is what makes the reduced structure the right answer when a problem asks only for equations, and the wrong answer when it asks for multiplicity: it is a quotient of every other structure on the same set by the nilpotents.

## The scheme-theoretic image

[[D-SCHIMG]]

For a morphism $f\colon X\to Y$, to say that the image of $f$ lies in a closed subscheme $Z\subseteq Y$ with ideal sheaf $\mci_Z$ means that the composite $\mci_Z\to\OO_Y\to f_*\OO_X$ is zero — equivalently, that $f$ factors through $Z$.
The scheme-theoretic image of $f$ is the unique smallest closed subscheme through which $f$ factors [@Har77, Exercise II.3.11], and its ideal sheaf is $\ker(\OO_Y\to f_*\OO_X)$ whenever that kernel is quasicoherent, which holds for $f$ quasicompact and quasiseparated ([[D-SCHIMG]], [@Vak25, §9.4]).

Three properties follow from the definition and are what it is used for.
For affine $f$, induced by $\varphi\colon A\to B$, the image is $\Spec(A/\ker\varphi)$, whose underlying space is the closure of the set-theoretic image rather than the image itself: for $k[t]\to k[t,t^{-1}]$ the kernel is zero, so the scheme-theoretic image is $\Spec k[t]$ while the set-theoretic image is the open set $D(t)$.
For $X$ reduced, the scheme-theoretic image is the closure of the set-theoretic image with its reduced induced structure [@Har77, Exercise II.3.11]: a reduced source gives a reduced image, and in that case the two constructions of this chapter agree.

Reducedness of the source is sufficient, not necessary, for reducedness of the image.
The morphism $\Spec k[\varepsilon]/(\varepsilon^2)\to\Spec k$ has scheme-theoretic image $\Spec k$, which is reduced although the source is not, so the image can lose multiplicity that the source has.
What a nonreduced source can supply is a nonreduced image, and then the image carries information the underlying set does not: the morphism $\Spec k[\varepsilon]/(\varepsilon^2)\to\AA^1$ sending $\varepsilon$ to $t$ has scheme-theoretic image $V(t^2)$, because the kernel of $k[t]\to k[\varepsilon]/\varepsilon^2$ is $(t^2)$, while the reduced structure on the set-theoretic image is the single point $V(t)$ ([[D-SCHIMG]]).

Multiplicity in a fibre is a third assertion, with hypotheses of its own, and it is not decided by reducedness of the source either.
For $X=\Spec k[s,t]/(s-t^2)\to Y=\Spec k[s]$ over an algebraically closed field $k$, the fibre over $s=a$ for $a\neq0$ is two reduced points with residue field $k$, while the fibre over $s=0$ is the nonreduced one-point scheme $\Spec k[\varepsilon]/(\varepsilon^2)$ [@Har77, Exercise II.3.10].
The two fibres have the same length $2$, the degree of the finite flat morphism, so constancy of the fibre length does not force the fibres to be reduced; [[D-MORFLAT]] records the same failure of reducedness in the flat family $V(y^2-tx)\to\AA^1_t$, whose special fibre is the nonreduced double line $y^2=0$.

The set-theoretic image is not the right object to work with in general, because it need not be locally closed: the morphism $\AA^2\to\AA^2$, $(x,y)\mapsto(x,xy)$, has image the complement of the $y$-axis together with the origin, which is neither open nor closed ([[D-SCHIMG]]).
Chevalley's theorem repairs this as far as possible: for a morphism of finite type of noetherian schemes the image of a constructible set is constructible, so in particular $f(X)$ is constructible [@Har77, Exercise II.3.19].
For $f$ proper the support of the scheme-theoretic image is the whole of $f(X)$, since a proper morphism is closed, and the only remaining information in the image is its non-reduced structure.

## Points and residue fields

[[D-SCHPTS]]

The residue field at $x$ is $\kappa(x)=\OO_{X,x}/\mfm_x$, so a section of the structure sheaf has a value in a field that depends on the point, and evaluating is applying $\OO_X(U)\to\OO_{X,x}\to\kappa(x)$ ([[D-SCHPTS]]).
On $\Spec A$ the closed points are the maximal ideals, the generic point of an irreducible closed subset $Z$ is the point whose closure is $Z$, and specialization $\tilde x\leadsto x$ is the relation $x\in\closure{\theset{\tilde x}}$, equivalently $\mfp_{\tilde x}\subseteq\mfp_x$ inside an affine open ([[D-SCHPTS]]).

Two remarks organise the vocabulary used in statements about families.
A section is not a function to a fixed field: on $\Spec\ZZ$ the element $5$ has values $0\in\FF_5$, $5\in\FF_7$, and $5\in\QQ$ at the generic point, and on a nonreduced scheme a section can be nonzero and vanish at every point ([[D-SCHPTS]]).
And "general" is not "generic": a property holds at a general point when it holds on a dense open set, and the generic point is a single point, so a property of a general point holds at the generic point but not conversely — $\operatorname{trdeg}_k\kappa(x)=1$ holds at the generic point of $\AA^1_k$ and at no closed point ([[D-SCHPTS]]).

## Intersections

[[PR-SCHINT]]

The scheme-theoretic intersection is the fibre product, and for closed subschemes $X_i=\Spec(R/J_i)$ of $Y=\Spec R$ it is $\Spec R/(J_1+J_2)$ ([[PR-SCHINT]]).
The intersection therefore remembers the order of contact: the parabola $C=V(y-x^m)$ and the line $L=V(y)$ in $\AA^2_k$ meet in $\Spec k[x]/(x^m)$, a point of length $m$, although both defining ideals are prime and the set-theoretic intersection is one point ([[PR-SCHINT]]).
So the sum of two radical ideals need not be radical, and the length of the intersection is the number an intersection-theoretic computation is counting.

## Dimension

[[D-SCHDIM]]

Dimension and codimension are defined through the specialization order just described, and they are treated on [[algebraic-geometry/schemes/dimension|dimension]] ([[D-SCHDIM]]).
