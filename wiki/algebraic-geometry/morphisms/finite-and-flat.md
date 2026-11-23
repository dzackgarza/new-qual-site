---
title: Finite and flat
order: 2
topics:
- Finite Morphisms
- Flatness
- Going Up
- Going Down
---

# Finite and flat

A finite morphism is the algebraic model of a branched covering: it is affine, closed, of finite type with finite fibres, and it is proper, so its fibres are the fibres of a family rather than of a map with missing points.
Flatness is the condition that makes a family vary continuously, and for a finite morphism over a connected noetherian base the two conditions together say that the fibre is a finite scheme of constant length.
The two properties are independent, and the standard failures of each are worth keeping: a finite morphism need not be flat, and a flat morphism need not be finite.
A nonconstant morphism of smooth projective curves is flat whenever the source is reduced and every irreducible component dominates the target, since the target is integral and regular of dimension one [@Har77, Proposition III.9.7].

## Going up and going down

[[PR-RJ3P7]]

Three theorems govern an integral extension $A\subseteq B$, and all three are statements about the map $f\colon\Spec B\to\Spec A$ on prime spectra.
Lying over: if $A\injects B$, every prime $\mfp$ of $A$ is the contraction of a prime of $B$, so $f$ is surjective [@AM18, Theorem 5.10].
Incomparability: two primes of $B$ lying over the same prime of $A$ are incomparable, so the fibres of $f$ carry no chain of length one [@AM18, Corollary 5.9].
Going up: a chain $\mfp_1\subseteq\cdots\subseteq\mfp_n$ of primes of $A$, together with a chain $\mfq_1\subseteq\cdots\subseteq\mfq_m$ of primes of $B$ with $m<n$ over its first $m$ terms, extends to a chain over the whole of it [@AM18, Theorem 5.11] ([[PR-RJ3P7]]).

Geometrically, an integral morphism is affine and universally closed (Stacks Project, Lemma 29.45.7, tag 01WM), hence closed, and it is of finite type and proper when the rings are finitely generated; it is finite exactly when each $B$ is a finite $A$-module (Stacks Project, Definition 29.45.1, tag 01WH).
Surjectivity is a separate hypothesis and is what lying over supplies, since lying over needs $A\injects B$: the integral ring map $\ZZ\to\ZZ/2$ is not injective, and $\Spec\ZZ/2\to\Spec\ZZ$ has image the single closed point $(2)$.
For a finite surjective morphism the fibre over a point is a finite nonempty scheme, which is the sense in which a finite morphism is a branched cover.

Going down is the same chain condition with the order reversed, and it does not hold for a general integral extension.
Let $A\subseteq B$ be domains with $A$ integrally closed and $B$ integral over $A$; then a chain $\mfp_1\supseteq\cdots\supseteq\mfp_n$ of primes of $A$, together with a chain of primes of $B$ over its first $m<n$ terms, extends downwards [@AM18, Theorem 5.16] ([[PR-RJ3P7]]).
The integrally closed hypothesis is not redundant, and it is the reason the hypothesis does not appear in the flat version of the statement: going down holds for every flat ring map $A\to B$, with no normality and no integrality, in the form that for primes $\mfp\subseteq\mfp'$ of $A$ and a prime $\mfq'$ of $B$ over $\mfp'$ there is a prime $\mfq\subseteq\mfq'$ over $\mfp$ (Stacks Project, Lemma 10.39.19, tag 00HS).
In geometric terms, going down says that a generization of a point of the image lifts to a generization of any chosen point above it, which is what makes the image of a flat morphism behave well under specialization ([[PR-RJ3P7]]).

## Flatness and fibres

[[D-MORFLAT]]

Flatness is a stalkwise condition: $f\colon X\to Y$ is flat at $x$ when $\OO_{X,x}$ is a flat $\OO_{Y,f(x)}$-module, and $f$ is faithfully flat when it is flat and surjective ([[D-MORFLAT]]).
For a finite flat morphism $f\colon X\to Y$ with $Y$ locally noetherian and connected, $f_*\OO_X$ is locally free of constant rank $d$ and every fibre has length $d$ (Stacks Project, Definition 29.49.1, tag 02KA; Lemmas 29.49.2 and 29.49.4, tags 02KB and 02KD; [[D-MORFLAT]]).
Thus a finite flat family over a connected locally noetherian base has constant degree; for a flat projective family over a connected noetherian base, the corresponding constant invariant is the fibres' Hilbert polynomial ([[T-COHFLATCHI]]).

Flatness over a regular curve of dimension one has a criterion in terms of associated points: if $X$ is noetherian, $Y$ is integral, regular, and of dimension one, then $f$ is flat exactly when every associated point of $X$ maps to the generic point of $Y$ [@Har77, Proposition III.9.7] ([[D-MORFLAT]]).
When $X$ is reduced the associated points are the generic points of its irreducible components, and the criterion becomes the statement that every component dominates $Y$.

## Where flatness fails

[[FE-MORNOTFLAT]]

Two morphisms fail flatness for the same reason at different scales.
The blowup $\Bl_0\AA^2\to\AA^2$ is projective and has every fibre over $p\neq0$ a single point, while the fibre over $0$ is a $\PP^1$; a flat projective morphism would have fibres with locally constant Hilbert polynomial, and here the fibre dimension jumps ([[FE-MORNOTFLAT]]).
The normalisation of a nodal cubic has two points over the node and one elsewhere, so if it were flat then $f_*\OO_{\tilde X}$ would be a locally free sheaf of rank $1$ — invertible — while its stalk at the node needs two generators ([[FE-MORNOTFLAT]]).
In both cases the obstruction is a fibre that is too large at one point, which is exactly what a flat family cannot do.

## Flatness in examples

[[FE-SCHFFLAT]]

$\AA^n_R\to\Spec R$ is flat for every ring $R$, because $R[x_1,\ldots,x_n]$ is a free $R$-module ([[FE-SCHFFLAT]]).
An $R$-module $M$ is faithfully flat exactly when it is flat and $-\tensor_RM$ is a faithful functor, which combines the two conditions a base change needs: flatness to preserve short exact sequences, and faithfulness so that a nonzero module does not become zero ([[FE-SCHFFLAT]]).

## Criteria for flatness

[[T-FLATCRIT]]

Flatness is local and infinitesimal, and there is a criterion that reduces it to a Tor-vanishing statement: for a noetherian ring $A$, an ideal $I$, a noetherian $A$-algebra $B$ with $IB$ in the Jacobson radical, and a finitely generated $B$-module $M$, flatness of $M$ over $A$ is equivalent to $M/IM$ being flat over $A/I$ together with $\Tor_1^A(A/I,M)=0$, and to $M/I^nM$ being flat over $A/I^n$ for every $n\ge1$ ([[T-FLATCRIT]]).
For a local homomorphism of noetherian local rings this reduces to the residue field: $M$ is flat over $A$ exactly when $\Tor_1^A(k,M)=0$ ([[T-FLATCRIT]]).

[[PR-MIRACLEFLAT]]

Miracle flatness supplies the geometric counterpart: a finite morphism of locally noetherian schemes is flat if the local rings of the source are Cohen--Macaulay, those of the target are regular, and the dimensions match at every point [@Har77, Exercise III.10.9] ([[PR-MIRACLEFLAT]]).
In particular a finite surjective morphism between smooth varieties of the same dimension over a field is flat, so the finite maps that a geometer writes down are flat unless a singularity is being resolved.

[[T-COHFLATCHI]]

Over an integral noetherian base the Hilbert polynomial decides flatness: a coherent sheaf on $\PP^n_T$ is flat over $T$ exactly when the Hilbert polynomial of its restriction to $\PP^n_t$ is the same for every $t\in T$ ([[T-COHFLATCHI]]).
This is the theorem that makes constancy of the Hilbert polynomial a criterion rather than a consequence, and it is what identifies the flat families of subschemes with a fixed Hilbert polynomial as the points of a Hilbert scheme.
