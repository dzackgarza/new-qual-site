---
title: Embeddings and Jacobians
order: 9
topics:
- Jacobian
- Abel-Jacobi
- Canonical Embedding
---

# Embeddings and Jacobians

Two constructions attach an object to a smooth projective curve, and they sit at opposite ends of the same theory.
A very ample divisor class gives a closed embedding into a projective space, with the symplectic side of the story being its linear system; the degree-zero part of the Picard group gives the Jacobian, an abelian variety of dimension $g$ whose tangent space at the identity is $H^1(C,\OO_C)$ ([[T-DIVMAPPN]], [[T-CRVJACFUN]]).
The Jacobian is the space of all degree-zero divisors modulo principal divisors, so the divisor theory of a curve is the geometry of a single variety of dimension $g$, and the map from divisors to that variety is Abel--Jacobi ([[T-U5QSY]]).

## Very ample classes and embeddings

[[T-DIVMAPPN]]

An invertible sheaf $\mcl$ with sections $s_0,\ldots,s_n$ that generate it defines a morphism $X\to\PP^n$ with $\mcl\cong\varphi^*\OO(1)$, and every morphism to projective space arises that way [@Har77, Theorem II.7.1] ([[T-DIVMAPPN]]).
A subspace $V\subseteq H^0(X,\mcl)$ gives a morphism on the complement of its base locus $B=\bigcap_iV(s_i)$, sending $x$ to $(s_0(x):\cdots:s_n(x))$, so a linear system without base points is a morphism and a very ample one is a closed embedding ([[T-DIVMAPPN]]).
On a curve the degree of the image is the degree of the divisor: for $V$ of dimension $2$ the morphism $X\to\PP^1$ is finite of degree $\deg\mcl$, and a divisor of degree at least $2g+1$ is very ample, so every smooth projective curve embeds in a projective space by a divisor of bounded degree ([[T-DIVMAPPN]], [[PR-CRVDEGBD]]).

## The canonical embedding

[[T-D8TUX]]

One very ample class is supplied by the curve itself: for $g\ge3$ the canonical divisor is very ample exactly when $C$ is not hyperelliptic, and then the canonical map embeds $C$ in $\PP^{g-1}$ as a curve of degree $2g-2$ ([[T-D8TUX]]).
The canonical embedding is the one that exists without a choice of divisor class, and it is the reason the canonical model is the standard projective model of a nonhyperelliptic curve; the hyperelliptic case and the factorisation of the canonical map through a degree-two map are on [[algebraic-geometry/curves-and-surfaces/special-divisors-and-the-canonical-map|special divisors and the canonical map]] ([[D-CRVHYP]]).

## The Jacobian

[[T-CRVJACFUN]]

For a smooth projective geometrically connected curve $X$ of genus $g$ over $k$ with a rational point $p_0$, the degree-zero relative Picard functor is represented by a smooth proper connected group scheme $\Jac(X)\to\Spec k$ of dimension $g$ ([[T-CRVJACFUN]]).
Concretely, $\Hom_k(T,\Jac(X))\cong\underline{\Pic}^0_{X/k}(T)$, the group law is tensor product of line bundles, the identity is $[\OO_X]$, inversion is duality, and the point $p_0$ gives a normalized Poincaré line bundle on $X\times_k\Jac(X)$ trivialized along $\theset{p_0}\times\Jac(X)$ ([[T-CRVJACFUN]], [[D-MODPIC]]).

The tangent space at the identity is $H^1(X,\OO_X)$, of dimension $g$ ([[T-CRVJACFUN]]).
That identification is also the statement that the two descriptions of the Jacobian agree: the cotangent space at the identity is $H^0(X,\Omega^1_X)$, and Serre duality for a projective nonsingular curve identifies $H^0(X,\omega_X)$ with the dual of $H^1(X,\OO_X)$ [@Har77, Remark III.7.12.2].
So the dimension of the Jacobian is the genus, computed twice, and the identification of tangent spaces is what makes deformation-theoretic arguments transfer to line bundles.

For each $d$ the functor of degree-$d$ line bundles is a torsor under $\Jac(X)$, so it is noncanonically isomorphic to $\Jac(X)$ but carries no distinguished point unless a degree-$d$ divisor is chosen ([[D-MODPIC]], [[T-CRVJACFUN]]).
The genus-one case is where the torsor and the group coincide in a useful way: $p\mapsto\OO_E(p-p_0)$ is an isomorphism $E\to\Pic^0_{E/k}$, which is how a genus-one curve with a chosen point acquires a group law ([[T-CRVJACFUN]]).

## Abel--Jacobi

[[T-U5QSY]]

Over $\CC$ the analytic description is explicit: $\Jac(X)(\CC)\cong H^0(X,\Omega^1_X)^\vee/H_1(X,\ZZ)$, where a homology class acts on a holomorphic differential by integration over a closed loop, and the Abel--Jacobi map sends a degree-zero divisor $\sum_i(p_i-q_i)$ to the functional $\omega\mapsto\sum_i\int_{q_i}^{p_i}\omega$ ([[T-U5QSY]]).
Changing the paths changes the functional by a period, hence by an element of the lattice, so the class in the quotient is well defined.

Abel's theorem is that a degree-zero divisor is principal exactly when its Abel--Jacobi image vanishes, and Jacobi inversion is that the map is surjective; together they give $\Pic^0(X)\cong\Jac(X)(\CC)$ ([[T-U5QSY]]).
Both halves are proved as one statement in Dolgachev, *Topics in Classical Algebraic Geometry*, §5.3.1: the map $\operatorname{aj}\colon\Pic^0(C)\to\Jac(C)$ of (5.19) is an isomorphism because the period map vanishes on principal divisors (Abel's part) and is surjective (Jacobi's inversion).
The two halves have different characters: Abel's theorem computes the kernel, identifying which divisors are principal, and Jacobi inversion says the map is onto ([[T-U5QSY]]).

## The theta divisor

[[D-DIVPOLAR]]

A polarization of an abelian variety is the class of an ample line bundle, and for a principal polarization the associated isogeny $\lambda_{\mcl}\colon A\to\dualof A$, $x\mapsto t_x^*\mcl\tensor\mcl^{-1}$, is an isomorphism ([[D-DIVPOLAR]]).
The Jacobian carries a canonical principal polarization: the image $\Theta$ of the effective divisors of degree $g-1$ under $\Pic^{g-1}(X)\cong\Jac(X)$ is a hypersurface with $h^0(\Theta)=1$ and $[-1]^*\Theta=\Theta$, a symmetric theta divisor, and an abelian variety carrying such a divisor is a principally polarized abelian variety (Dolgachev, *Topics in Classical Algebraic Geometry*, §5.3.1, (5.20)) ([[D-DIVPOLAR]], [[T-U5QSY]]).
The divisor is defined up to the choice of the identification $\Pic^{g-1}(X)\cong\Jac(X)$, that is up to translation, and translations act trivially on $\NS$, so its class is independent of that choice; the polarization therefore comes from the curve rather than being chosen ([[D-DIVPOLAR]]).
