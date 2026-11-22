---
title: Computing cohomology
order: 1
topics:
- Cohomology
- Cech Cohomology
- Twisting Sheaves
---

# Computing cohomology

Sheaf cohomology is the right derived functor of global sections, and for a quasicoherent sheaf on a noetherian separated scheme it is computed by the Čech complex of a finite affine open cover [@Har77, Theorem III.4.5].
The computation on the standard cover of $\PP^n$ then gives $H^i(\PP^n,\OO(d))$ for every $d$, and degree one carries the two interpretations used everywhere else: $H^1$ is the obstruction to lifting a section across a short exact sequence, and $H^1$ is the classification of line bundles and of extensions.

## The Čech complex

[[D-PTIW0]]

For an ordered open cover $\mcu=\theset{U_i}$ and a sheaf of abelian groups $\mcf$, the Čech complex has $C^p(\mcu,\mcf)=\prod_{i_0<\cdots<i_p}\mcf(U_{i_0}\intersect\cdots\intersect U_{i_p})$ with the alternating-sum differential, and there is a natural comparison map $\check H^p(\mcu,\mcf)\to H^p(X,\mcf)$ ([[D-PTIW0]]).
The comparison map is injective in degree one and an isomorphism in all degrees when the cover has no higher cohomology on finite intersections, which is exactly what a cover by affine opens of a scheme provides: finite intersections of affine opens are affine when $X$ is separated, and affine schemes have no higher cohomology for quasicoherent sheaves ([[D-PTIW0]], [[T-COHAFF]]).
So on a noetherian separated scheme, with a finite affine open cover, $\check H^p(\mcu,\mcf)\cong H^p(X,\mcf)$ [@Har77, Theorem III.4.5], and a cover by $n+1$ such opens gives $H^p(X,\mcf)=0$ for $p>n$ ([[D-PTIW0]]).

## Projective space

[[T-IJW1K]]

On $\PP^n_A$ the standard cover by the $n+1$ opens $D_+(x_i)\cong\AA^n_A$ is affine with affine intersections, so the Čech complex computes.
The answer is stated in terms of $S=A[x_0,\ldots,x_n]$: $H^0(\PP^n,\OO(d))=S_d$ of rank $\binom{n+d}{n}$ for $d\ge0$ and $0$ for $d<0$; $H^n(\PP^n,\OO(d))=0$ for $d>-n-1$ and is the free module on the monomials of degree $d$ with every exponent at most $-1$ otherwise, dual to $S_{-d-n-1}$; and $H^p(\PP^n,\OO(d))=0$ for all other $p$ except $p=0$ and $p=n$ [@Har77, Theorem III.5.1] ([[T-IJW1K]]).

The shift $-n-1$ is the twist of the canonical sheaf, $\omega_{\PP^n}=\OO(-n-1)$ [@Har77, Example II.8.20.1] ([[T-IJW1K]]).
With that identification the computation is a perfect pairing $H^0(\PP^n,\OO(d))\times H^n(\PP^n,\OO(-d-n-1))\to H^n(\PP^n,\OO(-n-1))\cong A$, which over a field is Serre duality on $\PP^n$ and over an arbitrary ring is the multiplication of complementary graded pieces of $S$ ([@Har77, Theorem III.5.1], [[T-COHSD]]).

## $H^1$: the obstruction to lifting

[[PR-COHLES]]

A short exact sequence $0\to\mcf'\to\mcf\to\mcf''\to0$ of sheaves of abelian groups produces a long exact sequence in cohomology, natural in morphisms of short exact sequences, whose connecting map $\delta\colon H^0(X,\mcf'')\to H^1(X,\mcf')$ is the obstruction ([[PR-COHLES]]).
Explicitly, an exact sequence shows that $\delta$ is what fails to be zero: a section $s\in\Gamma(X,\mcf'')$ lifts to $\Gamma(X,\mcf)$ if and only if $\delta(s)=0$.
The class is computed on a cover: choosing local lifts $t_i\in\mcf(U_i)$ of $s\restrict_{U_i}$, the differences $t_j-t_i$ lie in $\mcf'(U_i\intersect U_j)$ and the family $(t_j-t_i)_{i,j}$ is a Čech cocycle whose class is $\delta(s)$ ([[PR-COHLES]], [[D-PTIW0]]).
Two consequences follow immediately, and both are used constantly.
If $H^1(X,\mcf')=0$ then every section of $\mcf''$ lifts, which is the mechanism behind the vanishing criteria for ideals and the lifting of line bundles.
And a different choice of local lifts changes the cocycle by a coboundary, so the obstruction depends only on $s$, not on the cover.

## $H^1$: line bundles and extensions

[[PR-ET5PQ]]

The same degree classifies objects rather than obstructing them: for a ringed space $(X,\OO_X)$, $\Pic X\cong H^1(X,\OO_X^\times)$ [@Har77, Exercise III.4.5] ([[PR-ET5PQ]]).
An invertible sheaf is trivial on the members of a cover, a trivialization is a local unit, and the transition functions on overlaps satisfy the cocycle identity exactly, so the sheaf is the same data as a Čech class in degree one; the class is zero exactly when the sheaf is trivial.
Two refinements are worth having in mind.
Extensions $0\to\mcf\to\mce\to\mcg\to0$ of $\OO_X$-modules are classified by $\Ext^1_{\OO_X}(\mcg,\mcf)$ [@Har77, Exercise III.6.1], and when $\mcg$ is finite locally free this is $H^1(X,\mcf\tensor\mcg^\vee)$ [@Har77, Proposition III.6.7 with Proposition III.6.3], so extension classes and cohomology classes are the same thing ([[PR-ET5PQ]]).

The two interpretations meet in the exponential sequence.
On $X=\CC\sm\theset{0}$ the map $\exp\colon\OO_X\to\OO_X^\times$ is surjective on stalks and not on global sections, and its kernel is the constant sheaf $2\pi i\ZZ_X$, so after identifying that kernel with $\ZZ_X$ there is an exact sequence
$$
0\to\ZZ_X\to\OO_X\xrightarrow{\ \exp\ }\OO_X^\times\to0,
$$
whose connecting map is $\delta\colon H^0(X,\OO_X^\times)\to H^1(X,\ZZ_X)$.
The class $\delta(z)$ of the coordinate function is computed on the cover by $U_1=\CC\sm(-\infty,0]$ and $U_2=\CC\sm[0,\infty)$, on each of which $z$ has a logarithm: taking on $U_1$ the branch with argument in $(-\pi,\pi)$ and on $U_2$ the branch with argument in $(0,2\pi)$, the two logarithms agree on the upper component of $U_1\intersect U_2$ and differ by $2\pi i$ on the lower one, so $\delta(z)$ is the Čech cocycle equal to $0$ on the first component and to $-1$ on the second ([[D-PTIW0]]).
Evaluated on the loop $t\mapsto e^{2\pi it}$, this class takes the value $(2\pi i)^{-1}\oint\mathrm{d}z/z=1$, so $\delta(z)$ is a generator of $H^1(X,\ZZ_X)\cong\ZZ$; in particular $\delta(z)\neq0$, which is the statement that $z$ has no global logarithm ([[algebraic-geometry/sheaves/morphisms-of-sheaves|morphisms of sheaves]]).

## Dévissage

[[D-COHDEVISSAGE]]

Most computations of cohomology of a coherent sheaf are reductions: a coherent sheaf on a noetherian scheme has a finite filtration with successive quotients pushforwards of ideal sheaves on integral closed subschemes, so any statement that passes to extensions along such a filtration may be checked on those quotients ([[D-COHDEVISSAGE]]).
Vanishing, finiteness, and the constancy of the Euler characteristic are statements of that kind, which is why they are proved for an ideal sheaf on an integral subscheme and then transported to arbitrary coherent sheaves.
