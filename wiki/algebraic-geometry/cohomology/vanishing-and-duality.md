---
title: Vanishing and duality
order: 2
topics:
- Serre Criterion
- Dualizing Sheaf
- Serre Duality
---

# Vanishing and duality

On an affine scheme a quasicoherent sheaf has vanishing higher cohomology, and on a projective variety coherent cohomology vanishes above the dimension.
Kodaira vanishing has two complementary forms: for a smooth projective variety $X$ of dimension $n$ over a field of characteristic zero and an ample line bundle $L$, $H^i(X,\omega_X\tensor L)=0$ for $i>0$, equivalently $H^i(X,L^{-1})=0$ for $i<n$ ([[T-KODVAN]]).
Serre duality on a smooth projective $X$ of dimension $n$ identifies the dual of $H^i(X,\mcl)$ with $H^{n-i}(X,\omega_X\tensor\dualof{\mcl})$, so the two forms of Kodaira vanishing are equivalent.

## Serre's criterion for affineness

[[T-5IOUR]]

For a noetherian scheme $X$ three conditions are equivalent: $X$ is affine; $H^p(X,\mcf)=0$ for every quasicoherent $\mcf$ and every $p>0$; and $H^1(X,\mci)=0$ for every coherent sheaf of ideals $\mci$ [@Har77, Theorem III.3.7] ([[T-5IOUR]]).
The content is that a single degree, tested only against ideals, detects affineness: the proof covers $X$ by principal affine opens $X_f$ built from sections of a coherent ideal and then invokes the affine criterion of [@Har77, Exercise II.2.17].
The noetherian hypothesis is what makes every coherence statement finite, and the vanishing in degree zero is not part of the criterion, since $H^0(X,\mci)$ need not vanish.

## The dualizing sheaf

[[T-COHSD]]

Let $X$ be a proper scheme of dimension $n$ over a field $k$.
A dualizing sheaf for $X$ is a coherent sheaf $\omega_X^\circ$ together with a trace morphism $t\colon H^n(X,\omega_X^\circ)\to k$ such that for every coherent $\mcf$ the pairing
$$
\Hom(\mcf,\omega_X^\circ)\times H^n(X,\mcf)\longrightarrow H^n(X,\omega_X^\circ)\xrightarrow{t}k
$$
is a perfect pairing, that is, $\Hom(\mcf,\omega_X^\circ)\cong H^n(X,\mcf)^\vee$ [@Har77, Chapter III, §7] ([[T-COHSD]]).
The definition is a universal property, so a dualizing sheaf is unique: two of them are identified by a unique isomorphism compatible with the traces [@Har77, Proposition III.7.2].

Existence is a theorem about projective schemes, and the construction is the reason the canonical sheaf appears at all: for a closed subscheme $X\subseteq\PP^N_k$ of codimension $r$, the sheaf $\omega_X^\circ=\mathcal Ext^r_{\PP^N}(\OO_X,\omega_{\PP^N})$ is a dualizing sheaf [@Har77, Proposition III.7.5].
With $\OO_X(1)$ very ample the duality then holds in every degree: there are natural maps $\theta^i\colon\Ext^i(\mcf,\omega_X^\circ)\to H^{n-i}(X,\mcf)^\vee$ with $\theta^0$ the defining map, and $\theta^i$ is an isomorphism for all $i$ and all coherent $\mcf$ exactly when $X$ is Cohen--Macaulay and equidimensional [@Har77, Theorem III.7.6].
For locally free $\mcf$ that gives the familiar form of the statement, $H^i(X,\mcf)\cong H^{n-i}(X,\omega_X^\circ\tensor\dualof{\mcf})^\vee$ [@Har77, Corollary III.7.7] ([[T-COHSD]]).

Two further theorems identify the dualizing sheaf in the cases that occur in practice.
If $X\subseteq\PP^N$ is a local complete intersection of codimension $r$ with ideal sheaf $\mci$, then $\omega_X^\circ\cong\restrictionof{\omega_{\PP^N}}{X}\tensor\wedge^r(\mci/\mci^2)^\vee$, the first factor being the canonical sheaf of the ambient projective space restricted to $X$ and the second an invertible sheaf on $X$, so $\omega_X^\circ$ is invertible [@Har77, Theorem III.7.11].
And if $X$ is a projective nonsingular variety over an algebraically closed field, then $\omega_X^\circ\cong\omega_X=\Omega^n_{X/k}$ [@Har77, Corollary III.7.12].
So the dualizing sheaf is the right generalization of the canonical sheaf to singular or non-CM projective schemes: it exists always, it agrees with $\omega_X$ when $X$ is smooth, and it is invertible under the weaker hypothesis of being a local complete intersection.

## Serre duality on a smooth proper variety

[[T-COHSD]]

Let $X$ be a smooth proper variety of dimension $n$ over $k$ with canonical sheaf $\omega_X=\Omega^n_{X/k}$, and let $\mcl$ be locally free of finite rank.
Then cup product followed by the trace $t_X\colon H^n(X,\omega_X)\to k$ is a perfect pairing $H^i(X,\mcl)\tensor H^{n-i}(X,\omega_X\tensor\dualof{\mcl})\to k$ ([[T-COHSD]]).
The trace corresponds under $H^n(X,\omega_X)\cong H^0(X,\OO_X)^\vee$ to evaluation on the constant section $1$, and it is an isomorphism exactly when $H^0(X,\OO_X)=k$; for $X=\Spec K$ with $K/k$ finite separable of degree greater than one the trace cannot be an isomorphism, which is why the duality statement carries $k$-linearity of the pairing rather than merely a nondegenerate pairing of vector spaces.

On $\PP^n$ the whole theorem is a computation: $\omega_{\PP^n}=\OO(-n-1)$, and the pairing $H^0(\PP^n,\OO(d))\times H^n(\PP^n,\OO(-d-n-1))\to H^n(\PP^n,\OO(-n-1))\cong k$ is the multiplication $S_d\times S_{-d-n-1}\to S_{-n-1}$ of graded pieces of $S=k[x_0,\ldots,x_n]$ [@Har77, Theorem III.5.1 and Example II.8.20.1] ([[T-IJW1K]]).
Taking $n=1$ recovers the curve case: $H^1(C,\OO_C(D))$ is dual to $H^0(C,\OO_C(K-D))$, which is what turns Riemann--Roch into an equality between an Euler characteristic and a degree.

## Riemann--Roch for curves and surfaces

[[T-MWDVL]]

For a smooth projective curve Riemann--Roch is $\ell(D)-\ell(K-D)=\deg D+1-g$ [@Har77, Theorem IV.1.3], and Serre duality identifies $\ell(K-D)$ with $h^1(\OO_C(D))$, so the theorem is the statement $\chi(\OO_C(D))=\deg D+1-g$ together with the identification of the two terms of the Euler characteristic ([[T-MWDVL]]).
Setting $D=K$ gives $\deg K=2g-2$.

On a smooth projective surface the same two ingredients give the Riemann--Roch formula $\chi(\OO_X(D))=\chi(\OO_X)+\tfrac12D\cdot(D-K_X)$, and Serre duality turns $h^2(\OO_X(D))=h^0(\OO_X(K_X-D))$ into a computable correction term.
The resulting effectivity criterion is the one used to prove that a divisor class is represented by a curve: if $h^0(\OO_X(K_X-D))=0$ and $\chi(\OO_X)+\tfrac12D\cdot(D-K_X)>0$, then $H^0(\OO_X(D))\neq0$ ([[T-COHRRS]]).

## Finiteness and vanishing for ample twists

[[T-CARTSERRE]]

For a projective scheme $X$ over a noetherian ring $A$ with $\OO_X(1)$ very ample and $\mcf$ coherent, each $H^i(X,\mcf)$ is a finitely generated $A$-module, $\mcf(m)$ is generated by global sections for $m\gg0$, and $H^i(X,\mcf(m))=0$ for $i>0$ and $m\gg0$ [@Har77, Theorem III.5.2] ([[T-CARTSERRE]]).
Finiteness is what makes $h^i(X,\mcf)$ a number, and the eventual vanishing is what makes the Hilbert polynomial a polynomial: $\chi(\mcf(m))$ agrees with $h^0$ for large $m$.
The analytic counterpart is Cartan--Serre finiteness, that a coherent analytic sheaf on a compact complex space has finite-dimensional cohomology ([[T-CARTSERRE]]).

[[T-KODVAN]]

Kodaira vanishing is the sharp statement in the same direction: for $X$ smooth projective of dimension $n$ over a field of characteristic zero and $L$ ample, $H^i(X,\omega_X\tensor L)=0$ for every $i>0$, equivalently $H^i(X,L^{-1})=0$ for every $i<n$ ([[T-KODVAN]]).
The two forms are Serre duality applied to $L^{-1}$, and the characteristic-zero hypothesis is not superfluous: the statement fails for ample line bundles in positive characteristic.
The pair of theorems separates the two ways a twist can behave — Serre vanishing says a sufficiently positive twist has no higher cohomology, Kodaira vanishing says a sufficiently negative one has none below the top degree.

## GAGA and the topology of hyperplane sections

[[T-GAGA]]

For a projective scheme $X$ over $\CC$ with associated analytic space $X^{an}$ and $h\colon X^{an}\to X$, the natural maps $H^i(X,\mcf)\to H^i(X^{an},\mcf^{an})$ are isomorphisms for every coherent $\mcf$, and $\mcf\mapsto\mcf^{an}$ is an equivalence from coherent $\OO_X$-modules to coherent analytic sheaves [@Har77, Appendix B, Theorem 2.1] ([[T-GAGA]]).
So on a projective complex variety the algebraic and analytic cohomologies of a coherent sheaf agree, and a statement proved by analytic means — finiteness, Hodge theory, vanishing — transfers to the algebraic side.

[[T-LEFHYP]]

[[T-HARDLEF]]

The two Lefschetz theorems are the standard applications of that transfer.
For $X\subseteq\PP^N_\CC$ smooth projective of dimension $n$ and $Y=X\cap H$ a smooth hyperplane section, the restriction maps $H^i(X,\ZZ)\to H^i(Y,\ZZ)$ are isomorphisms for $i<n-1$ and injective for $i=n-1$, and on homotopy groups $\pi_i(Y)\to\pi_i(X)$ are isomorphisms for $i<n-1$ and surjective for $i=n-1$ ([[T-LEFHYP]]).
And for $\omega$ the class of a hyperplane section of a smooth projective $X$ of dimension $n$, cup product with $\omega^k$ is an isomorphism $H^{n-k}(X,\QQ)\to H^{n+k}(X,\QQ)$ for every $0\le k\le n$ ([[T-HARDLEF]]).
