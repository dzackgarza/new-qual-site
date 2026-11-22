---
title: What is a scheme
order: 2
topics:
- Schemes
- Affine Schemes
- Locally Ringed Spaces
---

# What is a scheme

Recall that a [[D-AN662|scheme]] is a locally ringed space covered by open subspaces isomorphic to spectra of rings, so a scheme is assembled from affine pieces and carries both a topological space and a sheaf of rings on it.
Three clauses of that sentence carry the weight, and each answers a question that the cheaper alternative gets wrong.
The points of the affine model are the prime ideals rather than the maximal ones, because the points that are not maximal are where a rational function has a value.
The sheaf is a sheaf of rings rather than a sheaf of functions to a fixed field, because the field a function takes values in depends on the point it is evaluated at.
And morphisms are required to be morphisms of locally ringed spaces rather than of ringed spaces, because without the condition on stalks even the affine correspondence between rings and spaces fails.

## The affine model

[[D-VKR54]]

In $\Spec A$ the closed sets are $V(J)=\theset{\mfp\supseteq J}$ for ideals $J$, the distinguished opens $D(f)$ for $f\in A$ form a basis, and $\OO_{\Spec A}(D(f))=A_f$ [@Har77, §II.2].
The stalk at $\mfp$ is the local ring $A_\mfp$, so the residue field $\kappa(\mfp)=A_\mfp/\mfp A_\mfp$ is the fraction field of $A/\mfp$, and a section $s\in\OO_{\Spec A}(U)$ has a value $s(\mfp)\in\kappa(\mfp)$ at each point of $U$.
That value is an element of a finite field at a closed point of $\Spec\ZZ$ and an element of $\QQ$ at the generic point; on $\AA^1_k$ over an algebraically closed $k$ it is the usual value of the polynomial.

Passing from values to sections is not reversible.
For $A=k[\varepsilon]/(\varepsilon^2)$ the class of $\varepsilon$ is a nonzero element whose value at the only point of $\Spec A$ is its image in $\kappa((\varepsilon))=k$, which is zero, so the collection of values $(s(\mfp))_\mfp$ does not determine the regular function $s$.

## The definition, clause by clause

[[D-AN662]]

The cover clause is where relative notions enter.
An affine scheme is the case of a one-element cover, and an affine-local property of morphisms — of finite type, of finite presentation, flat, smooth, étale — is asserted on the members of an affine open cover, with the affine communication lemma below the statement that the answer does not depend on which cover was chosen; not every property is of this kind, and irreducibility and integrality are the standard exceptions.

Recall that a [[D-AN662|morphism of schemes]] is a morphism of locally ringed spaces: a continuous $f$ with $f^\sharp\colon\OO_Y\to f_*\OO_X$ whose induced maps on stalks $f^\sharp_p\colon\OO_{Y,f(p)}\to\OO_{X,p}$ are local.
Locality is exactly what makes the two directions agree on affine schemes: for rings $A$ and $B$, every morphism of locally ringed spaces $\Spec B\to\Spec A$ is induced by a unique ring homomorphism $A\to B$, so that $\Spec$ is an anti-equivalence [@Har77, Proposition II.2.3].

::: {.example title="Dropping locality breaks the affine correspondence"}
Let $R$ be a discrete valuation ring with fraction field $K$, closed point $\mfm$, and generic point $\eta$.
Send the single point of $\Spec K$ to $\mfm$ and take $f^\sharp$ to be the inclusion $R\injects K$ on the open set $\Spec R$, and the zero map on the open set $\theset{\eta}$, whose preimage is empty.
This is a morphism of ringed spaces, and its map on stalks is the inclusion $R\injects K$, which sends a uniformizer to a unit and so is not local.
No morphism of schemes does this, because the only candidate ring map $R\to K$ is the inclusion and $\Spec$ of the inclusion sends the closed point of $\Spec K$ to the generic point $\eta$ [@Har77, Example II.2.3.2].
:::

## The affine dictionary

[[T-SK599]]

The adjunction in [[T-SK599]] is the computational form of the definition: a morphism $X\to\Spec A$ is a ring homomorphism $A\to\Gamma(X,\OO_X)$, so a scheme over $\Spec A$ is a scheme whose ring of global sections, and every ring of sections of an open subset, is an $A$-algebra [@Har77, Exercise II.2.4].
Applied with $A=k[x_1,\ldots,x_n]$, this says that a morphism $X\to\AA^n_S$ over $S$ is an $n$-tuple of global sections of $\OO_X$, namely the pullbacks of the coordinates ([[D-AN662]]).

The criterion for affineness is the assertion that the comparison morphism $X\to\Spec\Gamma(X,\OO_X)$ is an isomorphism, and it fails for $\PP^1_k$, where $\Gamma(\PP^1_k,\OO)=k$ so that the comparison morphism lands in a point, and for the punctured plane, where $\Gamma(\AA^2_k\sm\theset{0},\OO)=k[x,y]$ and the comparison morphism is the open immersion into $\AA^2_k$ ([[T-SK599]]).
Over an algebraically closed field the classical theory embeds: there is a fully faithful functor from varieties over $k$ to schemes over $k$ whose image on a variety $V$ has the nonempty irreducible closed subsets of $V$ as its points and recovers the regular functions on the closed points [@Har77, Proposition II.2.6].

## What the classical picture cannot hold

[[FE-O12TX]]

The three additions are nilpotents, generic points, and bases that are not fields.
A nilpotent is invisible to values and visible to the scheme: $\Spec k[\varepsilon]/(\varepsilon^2)$ is one point with a two-dimensional ring of functions, it is the scheme-theoretic fibre of $\AA^1\to\AA^1$, $t\mapsto t^2$, over the branch point, and its length $2$ is what makes the degree of that map constant ([[FE-O12TX]]).
Morphisms out of the double point are the tangent vectors: a $k$-morphism $\Spec k[\varepsilon]/(\varepsilon^2)\to X$ is a $k$-point together with an element of the Zariski tangent space there ([[PR-SCHFOP]]).

Generic points make "generically" a statement about a point.
On $\Spec\ZZ$ the generic point is $(0)$, its residue field is $\QQ$, and the closed points are the primes with residue fields $\FF_p$; a regular function such as $5/6$ on $D(6)$ therefore has values in different fields at different points, and vanishes exactly at the primes dividing $5$ ([[FE-O12TX]]).

## Checking a property on one affine cover

[[PR-SCHUNITCOVER]]

Two facts make the affine cover usable.
The distinguished opens $D(f_i)$ cover $\Spec R$ exactly when the $f_i$ generate the unit ideal, and the identity $1=\sum a_if_i$ exhibited by that condition already selects finitely many of them, so $\Spec R$ is quasicompact ([[PR-SCHUNITCOVER]]).
And a property that passes to principal localizations and glues along finitely many distinguished opens propagates from one affine cover to every affine open subscheme, which is the affine communication lemma of [@Vak25, Lemma 5.3.2] ([[T-AFFCOMM]]).

Being noetherian, being of finite type over a ring $R$, and being reduced are properties of this kind, and they may be checked on any one affine cover ([[T-AFFCOMM]], [@Har77, Proposition II.3.2]).
Irreducibility and integrality are not: for nonzero domains $A$ and $B$ the elements $(1,0)$ and $(0,1)$ of $A\times B$ generate the unit ideal and the localizations are $A$ and $B$, both domains, while $A\times B$ is not a domain, so $\Spec(A\times B)=\Spec A\sqcup\Spec B$ is covered by integral affine opens and is not integral ([[T-AFFCOMM]]).

## Affineness from cohomology

For noetherian $X$ the criterion above has a cohomological form: $X$ is affine exactly when $H^i(X,\mcf)=0$ for every quasicoherent $\mcf$ and every $i>0$, and exactly when $H^1(X,\mci)=0$ for every coherent sheaf of ideals $\mci$ [@Har77, Theorem III.3.7].
The single vanishing in degree one suffices; the higher vanishing follows from it by dimension shifting.
That criterion, its quasicoherent variant, and the duality that computes the groups being tested are on [[algebraic-geometry/cohomology/vanishing-and-duality|vanishing and duality]] ([[T-5IOUR]]).

## Formal schemes

[[D-SCHFORMAL]]

Completing a noetherian scheme along a closed subscheme gives a locally ringed space whose sections are a compatible system of infinitesimal neighbourhoods rather than a single ring, and $\operatorname{Spf}$ is the affine model for it [@Har77, §II.9].
The formal disc $\operatorname{Spf}k[[t]]$ has underlying space the single closed point, whereas $\Spec k[[t]]$ has a closed and a generic point and its open generic subscheme is $\Spec k((t))$; the two constructions are different, and the punctured formal disc needs a generic fibre or an adic framework to exist ([[D-SCHFORMAL]]).
