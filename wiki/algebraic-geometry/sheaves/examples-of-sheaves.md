---
title: Examples of sheaves
order: 3
topics:
- Sheaves
- Skyscraper Sheaves
- Local Systems
---

# Examples of sheaves

A constant sheaf records nothing of the space, a locally constant sheaf records its monodromy, and a skyscraper sheaf records one group at one point ([[D-SHFLOCSYS]], [[D-SHFSKYSCRAPER]]).

## Constant and locally constant sheaves

[[D-SHFLOCSYS]]

Recall that a [[D-SHFLOCSYS|constant sheaf]] has sections over an open set the continuous maps to a discrete group, so on a connected open set there is exactly one section per element.
On an irreducible space, and in particular on the underlying space of an irreducible scheme, every constant sheaf is flabby, and a flabby sheaf is acyclic for global sections ([[D-COHFLQ]]); hence $H^i(X,\underline{A})=0$ for $i>0$ when $X$ is irreducible.

## Skyscraper sheaves

[[D-SHFSKYSCRAPER]]

The support of the skyscraper $i_p(A)$ is $\closure{\theset{p}}$, and its stalk is $A$ at every point of that closure ([[D-SHFSKYSCRAPER]], [[D-UDIVH]]).

[[FE-SHFPONE]]

## Sheaves of functions

[[FE-SHFFUNCS]]

Each of these is a sheaf for the same reason: a function is continuous, smooth, or holomorphic exactly when its restriction to every member of an open cover is, and the values on overlaps determine the glued function.
The stalks of the holomorphic sheaf are rings of convergent power series, which are local rings, so a complex manifold is a locally ringed space and the maximal ideal at a point is the ideal of functions vanishing there ([[algebraic-geometry/schemes/ringed-spaces|ringed spaces]]).
The sheaf of holomorphic functions is a proper subsheaf of the sheaf of continuous functions, and the exponential shows the difference on global sections: $\exp$ is onto on stalks and not onto on $\OO_X(X)$ when $X=\CC\sm\theset{0}$ ([[FE-DNTT6]]).

## A presheaf that is not a sheaf

[[FE-AM5Z8]]

A presheaf is a sheaf exactly when both axioms hold, and sheafification is the universal morphism from a presheaf to a sheaf ([[T-3VX80]]), so it repairs a failure of either axiom.

## Stalks do not determine a sheaf

[[FE-SHFISOSTALKS]]

A morphism of sheaves $\varphi\colon\mcf\to\mcg$ is an isomorphism exactly when every stalk map $\varphi_x$ is an isomorphism, while sheaves with isomorphic stalks need not be isomorphic ([[FE-SHFISOSTALKS]]).

## Constructible sheaves

[[D-SHFCONSTR]]

A constructible sheaf is what a finite stratification whose strata carry locally constant sheaves produces, the locally constant and skyscraper sheaves being the two extremes.
The proper base change and vanishing theorems are stated for constructible coefficients ([[T-LADICPROPER]]).
